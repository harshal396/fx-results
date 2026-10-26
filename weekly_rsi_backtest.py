#!/usr/bin/env python3
"""Weekly-RSI strategies on OANDA daily bid/ask data.

STRATEGY 1 - the weekly RSI alone. Decisions are made only on COMPLETED weeks (a week ends Friday 17:00 New York) and executed at the next
daily open, buying at the ask and selling at the bid. Three readings of "buy above 60, sell below 40":
  W1  long while weekly RSI > 60, short while it is < 40, flat in between
  W2  long once it is > 60 and STAY long until it is < 40, then short until it is > 60 (always in the market after the first signal)
  W3  long-only: long while weekly RSI > 60, otherwise flat
STRATEGY 2 - weekly regime + daily trigger: weekly RSI > 60 AND the daily RSI crosses up through 60 -> buy; weekly RSI < 40 AND the daily
RSI crosses down through 40 -> sell. You did not give an exit, so four sensible ones are compared (each with an initial protective stop:
8-day swing +/- 0.25 ATR, kept between 0.5 and 3 daily ATR):
  X1  exit when the daily RSI falls back through 50 (long) / rises back through 50 (short)
  X2  exit when the weekly regime ends (weekly RSI <= 60 for a long, >= 40 for a short)
  X3  exit when a daily candle closes back across the daily EMA21
  X4  exit only by a 3 ATR trailing stop
Results are in % per trade (and R for strategy 2), after the real spread, with a bootstrap 95% interval, split into the markets we tuned
other rules on and ones we never looked at, by year, and compared with simply holding the market. Not modelled: swap/financing, slippage.

Run in a throwaway container so the live bot is untouched:
  docker compose run --rm --no-deps -T -e FX_MODE=sim fxagents python - --years 5 < ~/weekly_rsi_backtest.py > ~/fx-results/weekly_1.md
Options: --years N  --markets A,B,C  --insample A,B,C  --holdout-months 18  --selftest
"""
import argparse
import json
import os
import sys
import time
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone

import numpy as np
import pandas as pd

sys.path.insert(0, os.getcwd())
from fxagents.indicators import atr, ema, rsi      # noqa: E402

NY = "America/New_York"
INST = {"XAUUSD": "XAU_USD", "NDQ": "NAS100_USD", "US30": "US30_USD", "EURUSD": "EUR_USD", "GBPUSD": "GBP_USD", "USDJPY": "USD_JPY",
        "AUDUSD": "AUD_USD", "USDCAD": "USD_CAD", "XAGUSD": "XAG_USD", "SPX500": "SPX500_USD", "DE30": "DE30_EUR", "UK100": "UK100_GBP",
        "WTI": "WTICO_USD"}
ALL = "XAUUSD,NDQ,US30,EURUSD,GBPUSD,USDJPY,AUDUSD,USDCAD,XAGUSD,SPX500,DE30,UK100,WTI"
S1 = ("W1", "W2", "W3")
S2 = ("X1", "X2", "X3", "X4")


# ───────────────────────────── data ─────────────────────────────
def fetch_daily(inst, start_utc):
    token, host = os.environ.get("OANDA_API_TOKEN", ""), "https://api-fxpractice.oanda.com"
    rows, cur = [], start_utc.strftime("%Y-%m-%dT%H:%M:%SZ")
    while True:
        q = urllib.parse.urlencode({"granularity": "D", "price": "BA", "count": 5000, "from": cur, "dailyAlignment": 17,
                                    "alignmentTimezone": "America/New_York"})
        req = urllib.request.Request(f"{host}/v3/instruments/{inst}/candles?{q}", headers={"Authorization": f"Bearer {token}"})
        for attempt in range(6):
            try:
                cs = json.load(urllib.request.urlopen(req, timeout=90)).get("candles", [])
                break
            except Exception as ex:                                      # noqa: BLE001
                if attempt == 5:
                    raise
                print(f"  retry {attempt + 1} after {type(ex).__name__}: {ex}", file=sys.stderr, flush=True)
                time.sleep(3 * (attempt + 1))
        for c in cs:
            if c.get("complete"):
                b, a = c["bid"], c["ask"]
                rows.append((c["time"], *(float(b[k]) for k in "ohlc"), *(float(a[k]) for k in "ohlc")))
        if not cs or cs[-1]["time"] == cur or not cs[-1].get("complete", True):
            break
        cur = cs[-1]["time"]
    df = pd.DataFrame(rows, columns=["t", "bo", "bh", "bl", "bc", "ao", "ah", "al", "ac"])
    df.index = pd.DatetimeIndex(pd.to_datetime(df.pop("t"), utc=True)).tz_convert(NY)
    df = df[~df.index.duplicated(keep="last")].sort_index()
    for k in "ohlc":
        df["m" + k] = (df["b" + k] + df["a" + k]) / 2
    return df


def weekly_from_daily(d):
    """Trading weeks (Sunday 17:00 -> Friday 17:00 New York) from daily candles. Returns (weekly OHLC, avail) where avail[j] is the time
    (UTC ns) at which week j is COMPLETE: the end of its last daily candle."""
    ix = d.index
    dow = np.asarray(ix.dayofweek)
    lab = ix.normalize().tz_localize(None) - pd.to_timedelta((dow + 1) % 7, unit="D")       # the Sunday that starts the trading week
    g = d.groupby(lab)
    w = pd.DataFrame({"open": g["mo"].first(), "high": g["mh"].max(), "low": g["ml"].min(), "close": g["mc"].last()})
    last_label = pd.Series(ix, index=ix).groupby(lab).max()
    ll = pd.DatetimeIndex(last_label.to_list())
    avail = ll.as_unit("ns").asi8 + 24 * 3600 * 10 ** 9                                       # UTC nanoseconds (unit made explicit)
    if len(avail) and ll[-1].tz_convert(NY).dayofweek != 3:                                    # the newest week has not reached Friday's session yet:
        avail[-1] = np.iinfo(np.int64).max                                                     # it is still in progress, never use it
    return w, avail


# ───────────────────────────── strategy 1 ─────────────────────────────
def want_s1(mode, r, pos):
    if not np.isfinite(r):
        return pos
    if mode == "W1":
        return 1 if r > 60 else -1 if r < 40 else 0
    if mode == "W2":
        return 1 if r > 60 else -1 if r < 40 else pos
    return 1 if r > 60 else 0                                              # W3


def run_s1(X, rsi_w, widx, mode, start_k):
    """X: dict of arrays (bo, ao, bc, ac). The target position is set from the last COMPLETED week at the close of each daily candle and
    executed at the next daily open (ask when buying, bid when selling)."""
    n = len(X["bo"]); pos, trades, ent = 0, [], None
    for k in range(n - 1):
        j = widx[k]
        r = rsi_w[j] if j >= 0 else np.nan
        want = want_s1(mode, r, pos) if k >= start_k - 1 else 0
        if want != pos:
            if pos != 0:                                                   # close at the next open
                px = X["bo"][k + 1] if pos > 0 else X["ao"][k + 1]
                trades.append(dict(k_in=ent[0], k_out=k + 1, side=pos, ret=_ret(pos, ent[1], px)))
            if want != 0:
                ent = (k + 1, X["ao"][k + 1] if want > 0 else X["bo"][k + 1])
            pos = want
    if pos != 0:                                                           # still open at the end: mark at the last close
        px = X["bc"][n - 1] if pos > 0 else X["ac"][n - 1]
        trades.append(dict(k_in=ent[0], k_out=n - 1, side=pos, ret=_ret(pos, ent[1], px), open=True))
    return trades


def _ret(side, entry, exit_):
    return (exit_ - entry) / entry * 100 if side > 0 else (entry - exit_) / entry * 100


# ───────────────────────────── strategy 2 ─────────────────────────────
def run_s2(X, rsi_d, rsi_w, widx, e21, a, mode, start_k):
    n = len(X["bo"]); trades, busy = [], -1
    for k in range(max(start_k, 30), n - 2):
        if k <= busy:
            continue
        j = widx[k]
        if j < 0 or not np.isfinite(rsi_w[j]) or not np.isfinite(a[k]) or a[k] <= 0:
            continue
        up = rsi_w[j] > 60 and rsi_d[k - 1] <= 60 < rsi_d[k]
        dn = rsi_w[j] < 40 and rsi_d[k - 1] >= 40 > rsi_d[k]
        if not (up or dn):
            continue
        s = 1 if up else -1
        entry = X["ao"][k + 1] if s > 0 else X["bo"][k + 1]
        ext = X["ml"][max(k - 7, 0):k + 1].min() if s > 0 else X["mh"][max(k - 7, 0):k + 1].max()
        dist = min(max((entry - (ext - s * 0.25 * a[k])) * s, 0.5 * a[k]), 3.0 * a[k])
        stop = entry - s * dist
        res = _hold_s2(X, rsi_d, rsi_w, widx, e21, a, mode, k + 1, s, entry, stop, dist)
        res.update(side=s, k_in=k + 1, R=_r(res["px"], entry, s, dist), ret=_ret(s, entry, res["px"]))
        trades.append(res)
        busy = res["k_out"] - 1
    return trades


def _r(px, entry, s, dist):
    return (px - entry) * s / dist


def _hold_s2(X, rsi_d, rsi_w, widx, e21, a, mode, k0, s, entry, stop, dist):
    n = len(X["bo"]); stopv = stop; best_close = entry
    for k in range(k0, n):
        if s > 0 and X["bl"][k] <= stopv:
            return dict(px=min(stopv, X["bo"][k]) if X["bo"][k] < stopv else stopv, k_out=k, reason="stop")
        if s < 0 and X["ah"][k] >= stopv:
            return dict(px=max(stopv, X["ao"][k]) if X["ao"][k] > stopv else stopv, k_out=k, reason="stop")
        if k + 1 >= n:
            return dict(px=X["bc"][k] if s > 0 else X["ac"][k], k_out=k, reason="end of data")
        c = X["mc"][k]; j = widx[k]; rw = rsi_w[j] if j >= 0 else np.nan
        done = None
        if mode == "X1" and ((s > 0 and rsi_d[k] < 50) or (s < 0 and rsi_d[k] > 50)):
            done = "daily RSI through 50"
        elif mode == "X2" and np.isfinite(rw) and ((s > 0 and rw <= 60) or (s < 0 and rw >= 40)):
            done = "weekly regime ended"
        elif mode == "X3" and ((s > 0 and c < e21[k]) or (s < 0 and c > e21[k])):
            done = "EMA21 break"
        if done:
            return dict(px=X["bo"][k + 1] if s > 0 else X["ao"][k + 1], k_out=k + 1, reason=done)
        if mode == "X4":                                                   # 3 ATR chandelier, only ever tightens
            best_close = max(best_close, c) if s > 0 else min(best_close, c)
            new = best_close - s * 3.0 * a[k]
            stopv = max(stopv, new) if s > 0 else min(stopv, new)
    return dict(px=X["bc"][n - 1] if s > 0 else X["ac"][n - 1], k_out=n - 1, reason="end of data")


# ───────────────────────────── statistics and report ─────────────────────────────
def boot(x, reps=600):
    x = np.asarray(x, float)
    if len(x) < 5:
        return float(x.mean()) if len(x) else 0.0, float(x.mean()) if len(x) else 0.0
    rng = np.random.default_rng(1); step = max(1, int(2_000_000 // len(x)))
    m = np.concatenate([x[rng.integers(0, len(x), size=(min(step, reps - i), len(x)))].mean(axis=1) for i in range(0, reps, step)])
    return float(np.percentile(m, 2.5)), float(np.percentile(m, 97.5))


def row(x):
    x = np.asarray(x, float)
    if len(x) == 0:
        return "0 | - | - | - | - | -"
    lo, hi = boot(x)
    gl = -x[x < 0].sum(); pf = x[x > 0].sum() / gl if gl > 0 else float("inf")
    cum = np.cumsum(x); dd = float((np.maximum.accumulate(cum) - cum).max())
    return f"{len(x)} | {(x > 0).mean() * 100:.0f}% | {x.sum():+.1f} | {x.mean():+.2f} ({lo:+.2f}..{hi:+.2f}) | {('%.2f' % pf) if pf != float('inf') else 'inf'} | {dd:.1f}"


def table(T, key, variants, col, title, args, unit):
    L = [f"\n### {title}\n", f"| Variant | Trades | Win | Total {unit} | Avg {unit} per trade (95% interval) | PF | Deepest fall ({unit}) |\n|---|---|---|---|---|---|---|"]
    for v in variants:
        L.append(f"| {v} | " + row(T[T[key] == v][col]) + " |")
    return L


def report(T, bh, variants, key, label, col, unit, args, cut, extra_col=None):
    ins = set(args.insample.split(","))
    L = [f"\n## {label}\n"]
    L += table(T, key, variants, col, f"All markets together ({unit})", args, unit)
    L.append(f"\n### Markets we tuned other rules on ({','.join(sorted(ins))}) versus markets we never looked at\n")
    L.append(f"| Variant | Tuned: trades | Tuned: total {unit} | Tuned: avg | Untouched: trades | Untouched: total {unit} | Untouched: avg (95% interval) |\n|---|---|---|---|---|---|---|")
    for v in variants:
        x = T[T[key] == v]; a_, b_ = x[x.market.isin(ins)][col], x[~x.market.isin(ins)][col]
        lo, hi = boot(b_)
        L.append(f"| {v} | {len(a_)} | {a_.sum():+.1f} | {a_.mean() if len(a_) else 0:+.2f} | {len(b_)} | {b_.sum():+.1f} | {b_.mean() if len(b_) else 0:+.2f} ({lo:+.2f}..{hi:+.2f}) |")
    L.append(f"\n### Build period versus holdout (everything after {cut:%Y-%m-%d}): total {unit} and average per trade\n")
    L.append("| Variant | Build trades | Build total | Build avg | Holdout trades | Holdout total | Holdout avg |\n|---|---|---|---|---|---|---|")
    for v in variants:
        x = T[T[key] == v]; bd, ho = x[x.t_in < cut][col], x[x.t_in >= cut][col]
        L.append(f"| {v} | {len(bd)} | {bd.sum():+.1f} | {bd.mean() if len(bd) else 0:+.2f} | {len(ho)} | {ho.sum():+.1f} | {ho.mean() if len(ho) else 0:+.2f} |")
    mk = sorted(T.market.unique())
    L.append(f"\n### Total {unit} by market (trades)\n")
    L.append("| Variant | " + " | ".join(mk) + " |\n|---|" + "---|" * len(mk))
    for v in variants:
        x = T[T[key] == v]
        L.append(f"| {v} | " + " | ".join(f"{x[x.market == m][col].sum():+.1f} ({(x.market == m).sum()})" for m in mk) + " |")
    yrs = sorted(T.t_in.dt.year.unique())
    L.append(f"\n### Total {unit} by year of entry\n")
    L.append("| Variant | " + " | ".join(str(y) for y in yrs) + " |\n|---|" + "---|" * len(yrs))
    for v in variants:
        x = T[T[key] == v]
        L.append(f"| {v} | " + " | ".join(f"{x[x.t_in.dt.year == y][col].sum():+.1f}" for y in yrs) + " |")
    L.append("\n### Long trades versus short trades\n")
    L.append(f"| Variant | Long trades | Long total {unit} | Long avg | Short trades | Short total {unit} | Short avg |\n|---|---|---|---|---|---|---|")
    for v in variants:
        x = T[T[key] == v]; lg, sh = x[x.side > 0][col], x[x.side < 0][col]
        L.append(f"| {v} | {len(lg)} | {lg.sum():+.1f} | {lg.mean() if len(lg) else 0:+.2f} | {len(sh)} | {sh.sum():+.1f} | {sh.mean() if len(sh) else 0:+.2f} |")
    if extra_col:
        L.append("\n### Average days held, and how trades ended\n")
        rs = sorted(T.reason.dropna().unique())
        L.append("| Variant | Avg days held | " + " | ".join(rs) + " |\n|---|---|" + "---|" * len(rs))
        for v in variants:
            x = T[T[key] == v]
            L.append(f"| {v} | {x.days.mean() if len(x) else 0:.0f} | " + " | ".join(f"{(x.reason == r).mean() * 100:.0f}%" for r in rs) + " |")
    return L


# ───────────────────────────── self-test ─────────────────────────────
def selftest():
    ok = True

    def chk(name, cond):
        nonlocal ok
        print(("PASS " if cond else "FAIL ") + name); ok &= bool(cond)
    # 1) trading weeks: Sunday-17:00 labelled days belong to the week that ends on the Friday after
    idx = pd.DatetimeIndex([pd.Timestamp(x, tz=NY) for x in ("2026-10-11 17:00", "2026-10-12 17:00", "2026-10-13 17:00", "2026-10-14 17:00",
                                                             "2026-10-15 17:00", "2026-10-18 17:00", "2026-10-19 17:00")])   # Sun..Thu, then the next Sun, Mon
    d = pd.DataFrame({"mo": np.arange(7.), "mh": np.arange(7.) + 1, "ml": np.arange(7.) - 1, "mc": np.arange(7.) + .5}, index=idx)
    w, av = weekly_from_daily(d)
    chk("two weeks found: 5 days and 2 days", list(len(g) for _, g in d.groupby(d.index.normalize().tz_localize(None) - pd.to_timedelta((np.asarray(d.index.dayofweek) + 1) % 7, unit="D"))) == [5, 2])
    chk("week 1 OHLC: open of Sunday, high of Thursday, close of Thursday", w.iloc[0].open == 0 and w.iloc[0].high == 5 and w.iloc[0].close == 4.5)
    chk("week 1 is complete at Friday 17:00 New York", pd.Timestamp(av[0], tz="UTC").tz_convert(NY) == pd.Timestamp("2026-10-16 17:00", tz=NY))
    # 2) a daily candle only sees COMPLETED weeks: Thursday's candle (decided Friday 17:00) already sees week 1, Wednesday's does not
    dec = (idx + pd.Timedelta("24h")).as_unit("ns").asi8
    widx = np.searchsorted(av, dec, side="right") - 1
    chk("a week is visible from the close of its last daily candle, not before; the unfinished newest week never", list(widx) == [-1, -1, -1, -1, 0, 0, 0])
    # 3) strategy 1 state machines on a hand-made weekly RSI path (executed at the NEXT open)
    n = 12; bo = np.arange(n) + 100.; X = dict(bo=bo - .1, ao=bo + .1, bc=bo - .1, ac=bo + .1)
    path = np.array([50, 50, 65, 65, 55, 55, 35, 35, 45, 45, 65, 65.])
    ident = np.arange(n)
    w1 = run_s1(X, path, ident, "W1", 0); w2 = run_s1(X, path, ident, "W2", 0); w3 = run_s1(X, path, ident, "W3", 0)
    chk("W1: long at 65, flat at 55, short at 35, flat at 45, long again at 65", [(t["side"], t["k_in"], t["k_out"]) for t in w1] == [(1, 3, 5), (-1, 7, 9), (1, 11, 11)])
    chk("W2: long at 65 and stays long through 55, reverses to short at 35, stays short through 45, long at 65",
        [(t["side"], t["k_in"], t["k_out"]) for t in w2] == [(1, 3, 7), (-1, 7, 11), (1, 11, 11)])
    chk("W3: long only: long at 65, flat at 55", [(t["side"], t["k_in"], t["k_out"]) for t in w3][:1] == [(1, 3, 5)])
    chk("buys at the ask and sells at the bid (cost is paid)", abs(w1[0]["ret"] - ((bo[5] - .1) - (bo[3] + .1)) / (bo[3] + .1) * 100) < 1e-9)
    # 4) strategy 2: weekly > 60 and daily RSI crossing up through 60 starts a long; nothing without the weekly condition
    n = 60; bo = np.full(n, 100.); X2 = dict(bo=bo - .1, ao=bo + .1, bc=bo - .1, ac=bo + .1, bl=bo - .5, ah=bo + .5, mo=bo, mh=bo + .3, ml=bo - .3, mc=bo)
    rd = np.full(n, 50.); rd[40] = 61.; rd[39] = 58.
    rw = np.full(n, 65.); ew = np.full(n, 90.); aa = np.full(n, 1.)
    t_up = run_s2(X2, rd, rw, np.zeros(n, int), ew, aa, "X4", 0)
    chk("strategy 2: one long, entered at the open after the daily RSI crossed 60", len(t_up) == 1 and t_up[0]["side"] == 1 and t_up[0]["k_in"] == 41)
    chk("strategy 2: no trade when the weekly RSI is not above 60", len(run_s2(X2, rd, np.full(n, 55.), np.zeros(n, int), ew, aa, "X4", 0)) == 0)
    rd2 = np.full(n, 50.); rd2[40] = 39.; rd2[39] = 42.
    t_dn = run_s2(X2, rd2, np.full(n, 35.), np.zeros(n, int), np.full(n, 110.), aa, "X4", 0)
    chk("strategy 2: a short when weekly < 40 and the daily RSI crosses down through 40", len(t_dn) == 1 and t_dn[0]["side"] == -1)
    # 5) exits: X1 leaves when the daily RSI drops back through 50
    rd3 = rd.copy(); rd3[45:] = 45.
    t1 = run_s2(X2, rd3, rw, np.zeros(n, int), ew, aa, "X1", 0)
    chk("X1 exits at the open after the daily RSI fell through 50", t1[0]["reason"] == "daily RSI through 50" and t1[0]["k_out"] == 46)
    # 6) the initial stop works (price collapses below the stop)
    X3 = {k: v.copy() for k, v in X2.items()}; X3["bl"][43] = 90.; X3["bo"][43] = 99.
    t_s = run_s2(X3, rd, rw, np.zeros(n, int), ew, aa, "X4", 0)
    chk("the protective stop is hit", t_s[0]["reason"] == "stop" and t_s[0]["R"] < 0)
    print("SELFTEST", "OK" if ok else "FAILED")
    return ok


# ───────────────────────────── main ─────────────────────────────
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--years", type=float, default=5)
    ap.add_argument("--markets", default=ALL)
    ap.add_argument("--insample", default="XAUUSD,NDQ,US30")
    ap.add_argument("--holdout-months", type=int, default=18)
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        sys.exit(0 if selftest() else 1)
    now = datetime.now(timezone.utc); start = now - timedelta(days=int(args.years * 365))
    rows1, rows2, bh, problems = [], [], [], []
    for mk in args.markets.split(","):
        try:
            print(f"fetching {mk} ...", file=sys.stderr, flush=True)
            d = fetch_daily(INST[mk], start - timedelta(days=200))              # warm-up for the weekly RSI (14 weeks) and the daily EMA / ATR
            w, avail = weekly_from_daily(d)
            rsi_w = rsi(w["close"], 14).to_numpy()
            dm = pd.DataFrame({"open": d["mo"], "high": d["mh"], "low": d["ml"], "close": d["mc"]})
            rsi_d, e21, a = rsi(dm["close"], 14).to_numpy(), ema(dm["close"], 21).to_numpy(), atr(dm, 14).to_numpy()
            dec = (d.index + pd.Timedelta("24h")).as_unit("ns").asi8
            widx = np.searchsorted(avail, dec, side="right") - 1
            X = {k: d[k].to_numpy() for k in ("bo", "bh", "bl", "bc", "ao", "ah", "al", "ac", "mo", "mh", "ml", "mc")}
            start_k = int(np.searchsorted(d.index.as_unit("ns").asi8, pd.Timestamp(start).as_unit("ns").value))
            idx = d.index.tz_convert(NY)
            for mode in S1:
                for t in run_s1(X, rsi_w, widx, mode, start_k):
                    rows1.append(dict(market=mk, variant=mode, side=t["side"], ret=t["ret"], t_in=idx[t["k_in"]], days=t["k_out"] - t["k_in"],
                                      reason="still open" if t.get("open") else "signal"))
            for mode in S2:
                for t in run_s2(X, rsi_d, rsi_w, widx, e21, a, mode, start_k):
                    rows2.append(dict(market=mk, variant=mode, side=t["side"], ret=t["ret"], R=t["R"], t_in=idx[t["k_in"]],
                                      days=t["k_out"] - t["k_in"], reason=t["reason"]))
            bh.append((mk, (d["mc"].iloc[-1] / d["mo"].iloc[start_k] - 1) * 100, len(d) - start_k))
            print(f"  {mk}: done", file=sys.stderr, flush=True)
        except Exception as ex:                                                  # noqa: BLE001
            import traceback
            traceback.print_exc()
            problems.append(f"{mk}: {type(ex).__name__}: {ex}")
    if not rows1 and not rows2:
        print("no trades - check the data fetch (OANDA_API_TOKEN set?)\n" + "\n".join(problems))
        return
    T1, T2 = pd.DataFrame(rows1), pd.DataFrame(rows2)
    for T in (T1, T2):
        T["t_in"] = pd.to_datetime(T["t_in"], utc=True).dt.tz_convert(NY)
    cut = max(T1.t_in.max() if len(T1) else pd.Timestamp.min.tz_localize(NY), T2.t_in.max() if len(T2) else pd.Timestamp.min.tz_localize(NY)) - pd.DateOffset(months=args.holdout_months)
    L = ["# Weekly-RSI strategies\n",
         f"Generated {now:%Y-%m-%d %H:%M} UTC. OANDA daily bid/ask, {args.years:g} years, markets {args.markets}. Decisions on COMPLETED weeks / days only, "
         "executed at the next daily open (buy at the ask, sell at the bid). % = return on the price per trade, one unit, no leverage, no swap.\n",
         "Reference, the market itself over the same period (buy and hold, % change, mid prices): " + ", ".join(f"{m} {r:+.0f}%" for m, r, _ in bh) + "\n"]
    if len(T1):
        L += report(T1, bh, S1, "variant", "STRATEGY 1: the weekly RSI alone (W1 long>60 / short<40 / flat between, W2 always in the market, W3 long-only)", "ret", "%", args, cut, extra_col=True)
    if len(T2):
        L += report(T2, bh, S2, "variant", "STRATEGY 2: weekly RSI regime + daily RSI crossing 60 / 40 (X1-X4 = the four exits)", "ret", "%", args, cut, extra_col=True)
        L += table(T2, "variant", S2, "R", "Strategy 2 in R (risk = distance to the initial stop)", args, "R")
    if problems:
        L.append("\n## Problems during the run (these markets are missing)\n\n" + "\n".join(f"- {p}" for p in problems))
    print("\n".join(L))


if __name__ == "__main__":
    main()
