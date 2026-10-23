#!/usr/bin/env python3
"""Backtest of the RSI / EMA books: today's rules (A) against the changes we agreed (B-E), on OANDA bid/ask candles.
Signals come from fxagents/my_rules.py, i.e. the SAME code the live books run, so the test cannot drift from the bot.

Variants (each adds to the one before unless noted):
  A   today's rules: CHOP gate 61.8 everywhere, stop = 8-candle swing +/- 0.25 ATR (signal skipped if wider than 3 ATR)
  B   agreed filters: 15m CHOP gate 58.8 (1h stays 61.8), skip a signal candle over 2.5 ATR, stop CAPPED at 3 ATR instead of skipping
  C   B + trend gate on every entry (nearest higher timeframe: 1h for 15m books, 4h for 1h books)
  D1  B + trend gate on CONTINUATION entries only; a fresh breakout (cross within 3 candles after 2+ closes on the other side,
      EMA9/21 gap <= 0.35 ATR, candle 0.8-2.5 ATR) bypasses the chop gate and the trend gate
  D2  D1 where a breakout must also close beyond the prior 10-candle high / low
  E1  D2 + reversal-pattern exit (shooting star / hammer at a new 10-candle extreme, then a candle closing beyond it)
  E2  D2 + mechanical partial: half closed at +1R  (stand-in for Jev's live partial, which cannot be backtested)
  E3  D2 + both
Round 2 (each change ALONE on top of A, to see which ones help; T = trend gate on the nearest higher timeframe):
  T   A + trend gate           T2  A + trend gate on BOTH higher timeframes      TN  T with no chop gate at all
  K   A + 15m chop cutoff 58.8 only      G   A + skip candles over 2.5 ATR only      P   A + stop cap (3 ATR) only
  X1  T with the EMA exit only after TWO closes beyond EMA21      X2  T with NO EMA exit (stop / trail only)
Timeframes: 15min, 1h, 4h, 1D (4h and 1D candles are built from the hourly bid/ask candles on the New York clock).
Exits in every variant: the first of stop / candle closing back across EMA21 (exit at the next open) / [15m books] Friday 16:00 flat.
Stop moves to breakeven once the trade has been +1R, then trails 2 x ATR behind the best price.
Fills: buys at the ask, sells at the bid (real spread); entry at the open after the signal candle. NOT modelled: daily loss limit,
news blackout, Jev. R = result as a multiple of the initial risk (entry to stop).

Run in a throwaway container so the live bot is untouched:
  docker compose run --rm --no-deps -T fxagents python - --years 3 < ~/books_backtest.py > ~/fx-results/backtest_1.md
Options: --years N  --markets XAUUSD,NDQ,US30  --tfs 15min,1h  --families ema_rsi,ema_cross,rsi_mtf,fresh_state
         --variants A,B,C,D1,D2,E1,E2,E3  --holdout-months 12  --selftest (checks the simulator on hand-made paths and exits)
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
from fxagents import my_rules as M          # noqa: E402
from fxagents.indicators import ema, rsi     # noqa: E402

NY = "America/New_York"
INST = {"XAUUSD": "XAU_USD", "NDQ": "NAS100_USD", "US30": "US30_USD",
        # markets the rules were never tuned on (out-of-sample check)
        "EURUSD": "EUR_USD", "GBPUSD": "GBP_USD", "USDJPY": "USD_JPY", "AUDUSD": "AUD_USD", "USDCAD": "USD_CAD",
        "XAGUSD": "XAG_USD", "SPX500": "SPX500_USD", "DE30": "DE30_EUR", "UK100": "UK100_GBP", "WTI": "WTICO_USD"}
DELTA = {"15min": pd.Timedelta("15min"), "1h": pd.Timedelta("1h"), "4h": pd.Timedelta("4h"), "1D": pd.Timedelta("24h")}
BIG, CAPATR, MINATR, BEAR = 2.5, 3.0, 0.5, 0.35
VARIANTS = {
    "A":  dict(chop15=61.8, skip_big=False, cap=False, trend="off",  brk=None, pattern=False, partial=False),
    "T":  dict(chop15=61.8, skip_big=False, cap=False, trend="all",  brk=None, pattern=False, partial=False),
    "T2": dict(chop15=61.8, skip_big=False, cap=False, trend="both", brk=None, pattern=False, partial=False),
    "TN": dict(chop15=999,  skip_big=False, cap=False, trend="all",  brk=None, pattern=False, partial=False, chop1h=999),
    "K":  dict(chop15=58.8, skip_big=False, cap=False, trend="off",  brk=None, pattern=False, partial=False),
    "G":  dict(chop15=61.8, skip_big=True,  cap=False, trend="off",  brk=None, pattern=False, partial=False),
    "P":  dict(chop15=61.8, skip_big=False, cap=True,  trend="off",  brk=None, pattern=False, partial=False),
    "X1": dict(chop15=61.8, skip_big=False, cap=False, trend="all",  brk=None, pattern=False, partial=False, ema="two"),
    "X2": dict(chop15=61.8, skip_big=False, cap=False, trend="all",  brk=None, pattern=False, partial=False, ema="none"),
    "B":  dict(chop15=58.8, skip_big=True,  cap=True,  trend="off",  brk=None, pattern=False, partial=False),
    "C":  dict(chop15=58.8, skip_big=True,  cap=True,  trend="all",  brk=None, pattern=False, partial=False),
    "D1": dict(chop15=58.8, skip_big=True,  cap=True,  trend="cont", brk="d1", pattern=False, partial=False),
    "D2": dict(chop15=58.8, skip_big=True,  cap=True,  trend="cont", brk="d2", pattern=False, partial=False),
    "E1": dict(chop15=58.8, skip_big=True,  cap=True,  trend="cont", brk="d2", pattern=True,  partial=False),
    "E2": dict(chop15=58.8, skip_big=True,  cap=True,  trend="cont", brk="d2", pattern=False, partial=True),
    "E3": dict(chop15=58.8, skip_big=True,  cap=True,  trend="cont", brk="d2", pattern=True,  partial=True),
}
CHOP1H = 61.8


# ───────────────────────────── data ─────────────────────────────
def fetch_ba(inst, gran, start_utc):
    token, host = os.environ.get("OANDA_API_TOKEN", ""), "https://api-fxpractice.oanda.com"
    rows, cur = [], start_utc.strftime("%Y-%m-%dT%H:%M:%SZ")
    while True:
        q = urllib.parse.urlencode({"granularity": gran, "price": "BA", "count": 5000, "from": cur,
                                    "dailyAlignment": 17, "alignmentTimezone": "America/New_York"})
        req = urllib.request.Request(f"{host}/v3/instruments/{inst}/candles?{q}", headers={"Authorization": f"Bearer {token}"})
        for attempt in range(6):                                         # OANDA sometimes answers 502/504: wait and retry
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
        df["mid_" + k] = (df["b" + k] + df["a" + k]) / 2
    return df


def agg_ba(h1, tf):
    """4h / 1D bid-ask candles from hourly ones, on the same New York clock as fxagents/my_rules.py."""
    lab, dur = M._labels(h1, tf)
    g = h1.groupby(lab)
    cols = {}
    for pre in ("b", "a", "mid_"):
        cols[pre + "o"], cols[pre + "h"], cols[pre + "l"], cols[pre + "c"] = g[pre + "o"].first(), g[pre + "h"].max(), g[pre + "l"].min(), g[pre + "c"].last()
    df = pd.DataFrame(cols)
    df.index = df.index.tz_localize(NY, ambiguous=np.ones(len(df), dtype=bool), nonexistent="shift_forward")
    return df


def zero_state():
    return np.zeros(0, int), np.zeros(0, dtype="datetime64[ns]")


def mid(df):
    return df.rename(columns={"mid_o": "open", "mid_h": "high", "mid_l": "low", "mid_c": "close"})[["open", "high", "low", "close"]]


# ───────────────────────────── trade simulator ─────────────────────────────
def sim_trade(k0, s, entry, stop, X, pattern=False, partial=False, ema_mode="one"):
    """Walk candles from k0 (the entry candle). Returns dict(k, px, reason, R, mfe). Pure function of arrays: unit-tested."""
    n = len(X["c"]); risk = abs(entry - stop); best = entry; stopv = stop; part_done = False; banked = 0.0
    for k in range(k0, n):
        # 1) stop, evaluated with the stop as it stood at the start of the candle
        if s > 0 and X["bl"][k] <= stopv:
            px = min(stopv, X["bo"][k]) if X["bo"][k] < stopv else stopv
            return _fin(k, px, "stop", s, entry, risk, best, banked, part_done)
        if s < 0 and X["ah"][k] >= stopv:
            px = max(stopv, X["ao"][k]) if X["ao"][k] > stopv else stopv
            return _fin(k, px, "stop", s, entry, risk, best, banked, part_done)
        # 2) best price this candle (favourable side, real bid / ask)
        fav = X["bh"][k] if s > 0 else X["al"][k]
        best = max(best, fav) if s > 0 else min(best, fav)
        mfe = (best - entry) * s / risk
        if partial and not part_done and mfe >= 1.0:
            banked, part_done = 0.5 * 1.0, True                       # half closed at +1R
        # 3) decisions at the close of candle k, executed at the open of k+1
        if k + 1 >= n:
            return _fin(k, X["bc"][k] if s > 0 else X["ac"][k], "end of data", s, entry, risk, best, banked, part_done)
        c, e = X["c"][k], X["ema21"][k]
        exit_now = None
        beyond = (s > 0 and c < e) or (s < 0 and c > e)
        if ema_mode == "two":
            beyond = beyond and k > k0 and ((s > 0 and X["c"][k - 1] < X["ema21"][k - 1]) or (s < 0 and X["c"][k - 1] > X["ema21"][k - 1]))
        if beyond and ema_mode != "none":
            exit_now = "EMA exit"
        elif X["wk"][k]:
            exit_now = "weekend flat"
        elif pattern and _reversal(X, k, s):
            exit_now = "reversal pattern"
        if exit_now:
            return _fin(k + 1, X["bo"][k + 1] if s > 0 else X["ao"][k + 1], exit_now, s, entry, risk, best, banked, part_done)
        if mfe >= 1.0:                                                  # breakeven, then 2 x ATR trail; only ever tightens
            a = X["atr"][k]
            new = max(entry, best - 2 * a) if s > 0 else min(entry, best + 2 * a)
            stopv = max(stopv, new) if s > 0 else min(stopv, new)
    return _fin(n - 1, X["bc"][n - 1] if s > 0 else X["ac"][n - 1], "end of data", s, entry, risk, best, banked, part_done)


def _reversal(X, k, s):
    """Candle k-1 is a shooting star (long) / hammer (short) at a new 10-candle extreme and candle k closes beyond it."""
    if k < 11:
        return False
    o, h, l, c = X["o"][k - 1], X["h"][k - 1], X["l"][k - 1], X["c"][k - 1]
    rng = h - l
    if rng <= 0:
        return False
    body = abs(c - o)
    if s > 0:
        wick = h - max(o, c)
        return (wick >= 2 * max(body, 1e-9) and body <= 0.35 * rng and h >= X["h"][k - 11:k - 1].max()
                and X["c"][k] < X["o"][k] and X["c"][k] < l)
    wick = min(o, c) - l
    return (wick >= 2 * max(body, 1e-9) and body <= 0.35 * rng and l <= X["l"][k - 11:k - 1].min()
            and X["c"][k] > X["o"][k] and X["c"][k] > h)


def _fin(k, px, reason, s, entry, risk, best, banked, part_done):
    rest = (px - entry) * s / risk
    R = banked + (0.5 * rest if part_done else rest)
    return dict(k=k, px=px, reason=reason, R=R, mfe=(best - entry) * s / risk)


# ───────────────────────────── signals and classification ─────────────────────────────
def fresh_state_raw(b):
    """The pattern described in the review: price crossed EMA21 within 3 candles (after 2+ closes on the other side),
    EMA9/21 gap narrow, RSI as a STATE (long >= 55 and rising, short <= 45 and falling) instead of an RSI cross."""
    c, e21, e9, r, a = (b[k].to_numpy() for k in ("c", "ema21", "ema9", "rsi", "atr"))
    n = len(b); sg = np.sign(c - e21); cand = np.ones(n, int)
    for i in range(1, n):
        cand[i] = cand[i - 1] + 1 if sg[i] == sg[i - 1] else 1
    raw = np.zeros(n, int)
    for i in range(14, n):
        j = i - cand[i]
        if cand[i] > 3 or j < 1 or sg[j] != -sg[i] or sg[j - 1] != -sg[i] or sg[i] == 0:
            continue
        if abs(e9[i] - e21[i]) > BEAR * a[i]:
            continue
        if sg[i] > 0 and r[i] >= 55 and r[i] > r[i - 1]:
            raw[i] = 1
        elif sg[i] < 0 and r[i] <= 45 and r[i] < r[i - 1]:
            raw[i] = -1
    raw[:M.WARMUP["1h"]] = 0
    return raw


def features(b):
    c, e21, e9, a, h, l, o = (b[k].to_numpy() for k in ("c", "ema21", "ema9", "atr", "h", "l", "o"))
    n = len(b); sg = np.sign(c - e21); cand = np.ones(n, int)
    for i in range(1, n):
        cand[i] = cand[i - 1] + 1 if sg[i] == sg[i - 1] else 1
    return dict(sg=sg, cand=cand, gap=(e9 - e21) / a, rng=(h - l) / a)


def is_breakout(F, b, i, s, mode):
    cand = F["cand"][i]; j = i - cand
    if cand > 3 or j < 1 or F["sg"][j] != -F["sg"][i] or F["sg"][j - 1] != -F["sg"][i]:
        return False
    if abs(F["gap"][i]) > BEAR or not (0.8 <= F["rng"][i] <= BIG):
        return False
    if mode == "d2":
        c, h, l = b["c"].to_numpy(), b["h"].to_numpy(), b["l"].to_numpy()
        return bool(c[i] > h[max(i - 10, 0):i].max()) if s > 0 else bool(c[i] < l[max(i - 10, 0):i].min())
    return True


def htf_state(df_htf, tf_delta):
    """+1 bullish / -1 bearish / 0 neutral per higher-timeframe candle: close vs EMA21, with Supertrend or RSI agreeing."""
    d = df_htf[["open", "high", "low", "close"]]
    c = d["close"]
    e21, r = ema(c, 21).to_numpy(), rsi(c, 14).to_numpy()
    st = M.supertrend(d["high"].to_numpy(), d["low"].to_numpy(), c.to_numpy())
    cv = c.to_numpy()
    state = np.where((cv > e21) & ((st > 0) | (r > 50)), 1, np.where((cv < e21) & ((st < 0) | (r < 50)), -1, 0))
    ends = (d.index.tz_convert(NY).tz_localize(None) + tf_delta).to_numpy()
    return state, ends


# ───────────────────────────── one book, one variant ─────────────────────────────
def run_book(ba, b, raw, tf, var, F, hs, he, market, family, vname, hs2=None, he2=None):
    n = len(b); delta = DELTA[tf]
    X = dict(bo=ba["bo"].to_numpy(), bh=ba["bh"].to_numpy(), bl=ba["bl"].to_numpy(), bc=ba["bc"].to_numpy(),
             ao=ba["ao"].to_numpy(), ah=ba["ah"].to_numpy(), al=ba["al"].to_numpy(), ac=ba["ac"].to_numpy(),
             c=b["c"].to_numpy(), o=b["o"].to_numpy(), h=b["h"].to_numpy(), l=b["l"].to_numpy(),
             ema21=b["ema21"].to_numpy(), atr=b["atr"].to_numpy())
    idx = b.index.tz_convert(NY)
    dec = idx + delta
    wall = dec.tz_localize(None)
    X["wk"] = (np.array([(w.dayofweek == 4 and w.hour * 60 + w.minute >= 16 * 60) for w in wall]) if tf == "15min" else np.zeros(n, bool))
    chop = b["chop"].to_numpy(); a = X["atr"]
    chop_thr = var["chop15"] if tf == "15min" else var.get("chop1h", CHOP1H)
    st_map = np.searchsorted(he, wall.to_numpy(), side="right") - 1
    st_map2 = np.searchsorted(he2, wall.to_numpy(), side="right") - 1 if he2 is not None else None
    out, busy = [], -1
    for i in np.where(raw != 0)[0]:
        if i <= busy or i + 1 >= n or not np.isfinite(a[i]) or a[i] <= 0:
            continue
        if idx[i + 1] - dec[i] > delta:
            continue                                                     # market closed after this candle (break / weekend)
        s = int(raw[i])
        if var["skip_big"] and F["rng"][i] > BIG:
            continue
        brk = bool(var["brk"]) and is_breakout(F, b, i, s, var["brk"])
        if not brk:
            if chop[i] >= chop_thr:
                continue
        if var["trend"] != "off" and not (var["trend"] == "cont" and brk):
            j = st_map[i]
            hv = hs[j] if j >= 0 else 0
            if (s > 0 and hv < 0) or (s < 0 and hv > 0):
                continue
            if var["trend"] == "both" and st_map2 is not None:
                j2 = st_map2[i]
                hv2 = hs2[j2] if j2 >= 0 else 0
                if (s > 0 and hv2 < 0) or (s < 0 and hv2 > 0):
                    continue
        entry = X["ao"][i + 1] if s > 0 else X["bo"][i + 1]
        ext = b["l"].to_numpy()[max(i - 7, 0):i + 1].min() if s > 0 else b["h"].to_numpy()[max(i - 7, 0):i + 1].max()
        dist = (entry - (ext - s * 0.25 * a[i])) * s
        dist = max(dist, MINATR * a[i])
        if dist > CAPATR * a[i]:
            if not var["cap"]:
                continue
            dist = CAPATR * a[i]
        stop = entry - s * dist
        res = sim_trade(i + 1, s, entry, stop, X, pattern=var["pattern"], partial=var["partial"], ema_mode=var.get("ema", "one"))
        busy = res["k"] - 1          # flat from the open (or stop) of candle k, so that candle's close can start a new trade, as live
        out.append(dict(market=market, tf=tf, family=family, variant=vname, t=idx[i + 1], side=s, R=res["R"], mfe=res["mfe"],
                        reason=res["reason"], brk=brk, held=res["k"] - (i + 1)))
    return out


# ───────────────────────────── statistics and report ─────────────────────────────
def stats(R):
    R = np.asarray(R, float)
    if len(R) == 0:
        return dict(n=0, win=0.0, tot=0.0, avg=0.0, pf=0.0, dd=0.0, lo=0.0, hi=0.0)
    cum = np.cumsum(R); dd = float((np.maximum.accumulate(cum) - cum).max())
    gl = -R[R < 0].sum()
    rng = np.random.default_rng(1)
    if len(R) >= 5:                                        # bootstrap in small batches: memory stays tiny however many trades
        step = max(1, int(2_000_000 // len(R)))
        bs = np.concatenate([R[rng.integers(0, len(R), size=(min(step, 600 - k), len(R)))].mean(axis=1) for k in range(0, 600, step)])
    else:
        bs = np.array([R.mean()])
    return dict(n=len(R), win=float((R > 0).mean()), tot=float(R.sum()), avg=float(R.mean()), pf=float(R[R > 0].sum() / gl) if gl > 0 else float("inf"),
                dd=dd, lo=float(np.percentile(bs, 2.5)), hi=float(np.percentile(bs, 97.5)))


def fmt(s):
    return (f"{s['n']} | {s['win'] * 100:.0f}% | {s['tot']:+.1f} | {s['avg']:+.3f} ({s['lo']:+.2f}..{s['hi']:+.2f}) | "
            f"{('%.2f' % s['pf']) if s['pf'] != float('inf') else 'inf'} | {s['dd']:.1f}")


def report(T, variants, holdout_cut, args):
    L = ["# Backtest: today's rules vs the agreed changes\n",
         f"Generated {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC. Data: OANDA bid/ask, {args.years} years, markets {args.markets}, "
         f"timeframes {args.tfs}, families {args.families}. Build period = everything before {holdout_cut:%Y-%m-%d}; holdout = after.",
         "R = result as a multiple of the risk at the first stop. One position per book and market. Not modelled: daily loss limit, news blackout, Jev.",
         "In the tables: avg R is followed by its 95% bootstrap interval; PF = profit factor; DD = deepest fall of the cumulative R curve.\n"]
    for tf in args.tfs.split(","):
        d = T[T.tf == tf]
        if d.empty:
            continue
        L.append(f"\n## {tf} books - all markets and families together\n")
        L.append("| Variant | Trades | Win | Total R | Avg R (95% interval) | PF | DD (R) |\n|---|---|---|---|---|---|---|")
        for v in variants:
            L.append(f"| {v} | " + fmt(stats(d[d.variant == v].R)) + " |")
        L.append(f"\n### {tf}: build period vs holdout (total R and average R per trade)\n")
        L.append("| Variant | Build trades | Build total R | Build avg R | Holdout trades | Holdout total R | Holdout avg R |\n|---|---|---|---|---|---|---|")
        for v in variants:
            x = d[d.variant == v]; bd, ho = x[x.t < holdout_cut].R, x[x.t >= holdout_cut].R
            L.append(f"| {v} | {len(bd)} | {bd.sum():+.1f} | {bd.mean() if len(bd) else 0:+.3f} | {len(ho)} | {ho.sum():+.1f} | {ho.mean() if len(ho) else 0:+.3f} |")
        L.append(f"\n### {tf}: total R by market\n")
        mk = sorted(d.market.unique())
        L.append("| Variant | " + " | ".join(mk) + " |\n|---|" + "---|" * len(mk))
        for v in variants:
            x = d[d.variant == v]
            L.append(f"| {v} | " + " | ".join(f"{x[x.market == m].R.sum():+.1f} ({(x.market == m).sum()})" for m in mk) + " |")
        L.append(f"\n### {tf}: total R by family\n")
        fm = sorted(d.family.unique())
        L.append("| Variant | " + " | ".join(fm) + " |\n|---|" + "---|" * len(fm))
        for v in variants:
            x = d[d.variant == v]
            L.append(f"| {v} | " + " | ".join(f"{x[x.family == f].R.sum():+.1f} ({(x.family == f).sum()})" for f in fm) + " |")
        L.append(f"\n### {tf}: total R by year\n")
        yrs = sorted(d.t.dt.year.unique())
        L.append("| Variant | " + " | ".join(str(y) for y in yrs) + " |\n|---|" + "---|" * len(yrs))
        for v in variants:
            x = d[d.variant == v]
            L.append(f"| {v} | " + " | ".join(f"{x[x.t.dt.year == y].R.sum():+.1f}" for y in yrs) + " |")
        L.append(f"\n### {tf}: average R by how the trade ended (number of trades)\n")
        rs0 = sorted(d.reason.unique())
        L.append("| Variant | " + " | ".join(rs0) + " |\n|---|" + "---|" * len(rs0))
        for v in variants:
            x = d[d.variant == v]
            L.append(f"| {v} | " + " | ".join((f"{x[x.reason == r].R.mean():+.2f} ({(x.reason == r).sum()})" if (x.reason == r).any() else "-") for r in rs0) + " |")
        for v in [q for q in args.detail.split(",") if q in variants]:
            x = d[d.variant == v]
            fm0, mk0 = sorted(x.family.unique()), sorted(x.market.unique())
            L.append(f"\n### {tf}, variant {v}: total R by family x market (trades)\n")
            L.append("| Family | " + " | ".join(mk0) + " |\n|---|" + "---|" * len(mk0))
            for f in fm0:
                L.append(f"| {f} | " + " | ".join(f"{x[(x.family == f) & (x.market == m)].R.sum():+.1f} ({((x.family == f) & (x.market == m)).sum()})" for m in mk0) + " |")
        L.append(f"\n### {tf}: how trades ended (share of trades)\n")
        rs = sorted(d.reason.unique())
        L.append("| Variant | " + " | ".join(rs) + " |\n|---|" + "---|" * len(rs))
        for v in variants:
            x = d[d.variant == v]
            L.append(f"| {v} | " + " | ".join(f"{(x.reason == r).mean() * 100:.0f}%" for r in rs) + " |")
    br = T[T.brk]
    if len(br):
        L.append("\n## Breakout entries (D/E variants only): how the exempted trades did\n")
        L.append("| Variant | Trades | Win | Total R | Avg R (95% interval) | PF | DD (R) |\n|---|---|---|---|---|---|---|")
        for v in variants:
            x = br[br.variant == v]
            if len(x):
                L.append(f"| {v} | " + fmt(stats(x.R)) + " |")
    return "\n".join(L)


# ───────────────────────────── self-test ─────────────────────────────
def selftest():
    n = 40
    def arrs(price=100.0, spread=0.2):
        p = np.full(n, price)
        X = dict(bo=p - spread / 2, bh=p - spread / 2, bl=p - spread / 2, bc=p - spread / 2, ao=p + spread / 2, ah=p + spread / 2,
                 al=p + spread / 2, ac=p + spread / 2, c=p.copy(), o=p.copy(), h=p + 0.3, l=p - 0.3, ema21=np.full(n, price - 5.0),
                 atr=np.full(n, 1.0), wk=np.zeros(n, bool))
        return X
    ok = True
    def chk(name, cond):
        nonlocal ok
        print(("PASS " if cond else "FAIL ") + name); ok &= bool(cond)
    # 1) long hits its stop: exit at the stop, R = -1 plus the half-spread paid on entry
    X = arrs(); X["bl"][5] = 97.0
    r = sim_trade(1, 1, 100.1, 98.0, X)
    chk("long stop: exit at the stop price", abs(r["px"] - 98.0) < 1e-9 and r["reason"] == "stop")
    chk("long stop: R is exactly (98.0-100.1)/2.1 = -1.0", abs(r["R"] + 1.0) < 1e-9)
    # 2) gap through the stop exits at the (worse) open, not at the stop
    X = arrs(); X["bo"][5] = 96.0; X["bl"][5] = 95.0
    r = sim_trade(1, 1, 100.1, 98.0, X)
    chk("gap through the stop: exit at the gap open 96.0, R below -1", abs(r["px"] - 96.0) < 1e-9 and r["R"] < -1.5)
    # 3) short mirrors: ask high through the stop (EMA21 sits above price for a short)
    X = arrs(); X["ema21"][:] = 105.0; X["ah"][4] = 103.0
    r = sim_trade(1, -1, 99.9, 102.0, X)
    chk("short stop: exit at 102.0, R = -1", abs(r["px"] - 102.0) < 1e-9 and abs(r["R"] + 1.0) < 1e-9)
    # 4) EMA exit: a close below EMA21 exits at the NEXT candle's bid open
    X = arrs(); X["c"][6] = 90.0; X["bo"][7] = 99.5
    r = sim_trade(1, 1, 100.1, 98.0, X)
    chk("EMA exit at the next open (bid)", r["reason"] == "EMA exit" and r["k"] == 7 and abs(r["px"] - 99.5) < 1e-9)
    # 5) breakeven + trail: price climbs steadily (a consistent path), the stop trails 2 ATR behind, a drop stops us out above entry
    def ramp():
        X = arrs(); X["ema21"][:] = 90.0
        for k in range(1, n):
            pk = 100.0 + 2.0 * (min(k, 5) - 1)                # 100, 102, 104, 106, 108, then flat at 108
            X["bo"][k] = X["bl"][k] = X["bc"][k] = pk - 0.1
            X["bh"][k] = pk + 2.0 - 0.1
            X["ao"][k] = X["al"][k] = X["ac"][k] = pk + 0.1
            X["ah"][k] = pk + 2.0 + 0.1
            X["c"][k] = pk
        return X
    X = ramp(); X["bl"][9] = 100.0
    r = sim_trade(1, 1, 100.1, 98.1, X)               # risk 2.0
    chk("trail: stopped out ABOVE entry after running (R > 1)", r["reason"] == "stop" and r["R"] > 1.0 and r["px"] > 100.1)
    # 6) nothing happens before breakeven: stop does not move before +1R
    X = arrs(); X["bh"][2] = 100.5; X["bl"][4] = 97.9
    r = sim_trade(1, 1, 100.1, 98.0, X)
    chk("no trailing before +1R: original stop still applies", r["reason"] == "stop" and abs(r["px"] - 98.0) < 1e-9)
    # 7) weekend flat
    X = arrs(); X["wk"][6] = True; X["bo"][7] = 100.0
    r = sim_trade(1, 1, 100.1, 98.0, X)
    chk("weekend flat exits at the next open", r["reason"] == "weekend flat" and r["k"] == 7)
    # 8) partial: half banked at +1R, the other half follows the trade
    X = ramp(); X["bl"][9] = 100.0
    full = sim_trade(1, 1, 100.1, 98.1, X)
    part = sim_trade(1, 1, 100.1, 98.1, X, partial=True)
    chk("partial: R = 0.5 banked + half of the rest", abs(part["R"] - (0.5 + 0.5 * (part["px"] - 100.1) / 2.0)) < 1e-9 and part["px"] == full["px"])
    # 9) reversal pattern exit (long): shooting star at a new high, then a candle closing below its low
    X = arrs()
    for k in range(1, 12):
        X["h"][k] = 100.3
    X["o"][12], X["c"][12], X["h"][12], X["l"][12] = 100.0, 100.05, 102.0, 99.9          # long upper wick, small body, new high
    X["o"][13], X["c"][13], X["h"][13], X["l"][13] = 100.0, 99.5, 100.1, 99.4             # red candle closing below the star's low
    X["bo"][14] = 99.4
    r = sim_trade(1, 1, 100.1, 90.0, X, pattern=True)
    chk("reversal pattern exits at the next open", r["reason"] == "reversal pattern" and r["k"] == 14)
    # 9b) EMA exit modes: one close, two closes, none
    X = arrs(); X["c"][6] = 90.0; X["bo"][7] = 99.5; X["bo"][8] = 99.4
    one = sim_trade(1, 1, 100.1, 98.0, X, ema_mode="one")
    two = sim_trade(1, 1, 100.1, 98.0, X, ema_mode="two")
    X["c"][7] = 90.0
    two2 = sim_trade(1, 1, 100.1, 98.0, X, ema_mode="two")
    non = sim_trade(1, 1, 100.1, 98.0, X, ema_mode="none")
    chk("EMA exit: one close exits, a single close does not exit in 'two' mode", one["reason"] == "EMA exit" and two["reason"] != "EMA exit")
    chk("EMA exit 'two': exits after the second close, at the next open", two2["reason"] == "EMA exit" and two2["k"] == 8)
    chk("EMA exit 'none': never exits on the EMA", non["reason"] != "EMA exit")
    # 10) classification helpers
    b = pd.DataFrame({"c": [1, 2, 3, 4.0], "ema21": [2, 2, 2, 2.0], "ema9": [2, 2, 2, 2.0], "atr": [1.0] * 4, "h": [1, 2, 3, 4.0], "l": [0, 1, 2, 3.0], "o": [1, 2, 3, 4.0]})
    F = features(b)
    chk("run length: closes above EMA21 counted correctly", list(F["cand"]) == [1, 1, 1, 2])
    print("SELFTEST", "OK" if ok else "FAILED")
    return ok


# ───────────────────────────── main ─────────────────────────────
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--years", type=float, default=3)
    ap.add_argument("--markets", default="XAUUSD,NDQ,US30")
    ap.add_argument("--tfs", default="15min,1h,4h,1D")
    ap.add_argument("--families", default="ema_rsi,ema_cross,rsi_mtf,fresh_state")
    ap.add_argument("--variants", default="A,T,T2,TN,K,G,P,X1,X2,C,D2,E1")
    ap.add_argument("--detail", default="A,T", help="variants that also get a family x market table")
    ap.add_argument("--holdout-months", type=int, default=12)
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        sys.exit(0 if selftest() else 1)
    start = datetime.now(timezone.utc) - timedelta(days=int(args.years * 365))
    variants = args.variants.split(",")
    allr, problems = [], []
    for mk in args.markets.split(","):
      try:
        print(f"fetching {mk} ...", file=sys.stderr, flush=True)
        tfs = args.tfs.split(",")
        m15 = fetch_ba(INST[mk], "M15", start) if "15min" in tfs else None        # 15m data is only downloaded when asked for
        h1 = fetch_ba(INST[mk], "H1", start - timedelta(days=60))
        h1c = h1[h1.index >= (m15.index[0] if m15 is not None else pd.Timestamp(start).tz_convert(NY)) - pd.Timedelta("1h")]
        frames = {"15min": m15, "1h": h1c, "4h": agg_ba(h1c, "4h"), "1D": agg_ba(h1c, "1D")}
        h1m = mid(h1)
        s1h, s4h, s1d = htf_state(h1m, DELTA["1h"]), htf_state(M.build_tf(h1m, "4h")[0], DELTA["4h"]), htf_state(M.build_tf(h1m, "1D")[0], DELTA["1D"])
        htf = {"15min": (s1h, s4h), "1h": (s4h, s1d), "4h": (s1d, zero_state()), "1D": (zero_state(), zero_state())}
        for tf in args.tfs.split(","):
            ba = frames[tf]
            dm = mid(ba)
            for fam in args.families.split(","):
              try:
                rule = "ema_rsi" if fam == "fresh_state" else fam
                b = M.build(dm, h1m, rule, tf)
                raw = fresh_state_raw(b) if fam == "fresh_state" else b["raw"].to_numpy()
                F = features(b)
                (hs, he), (hs2, he2) = htf[tf]
                for v in variants:
                    allr += run_book(ba, b, raw, tf, VARIANTS[v], F, hs, he, mk, fam, v, hs2, he2)
                print(f"  {mk} {tf} {fam}: done", file=sys.stderr, flush=True)
              except Exception as ex:                                       # noqa: BLE001
                import traceback
                traceback.print_exc()
                problems.append(f"{mk} {tf} {fam}: {type(ex).__name__}: {ex}")
      except Exception as ex:                                               # noqa: BLE001
        import traceback
        traceback.print_exc()
        problems.append(f"{mk}: {type(ex).__name__}: {ex}")
    if not allr:
        print("no trades produced - check the data fetch (OANDA_API_TOKEN set?)")
        return
    T = pd.DataFrame(allr)
    T["t"] = pd.to_datetime(T["t"], utc=True).dt.tz_convert(NY)
    cut = T.t.max() - pd.DateOffset(months=args.holdout_months)
    txt = report(T, variants, cut, args)
    if problems:
        txt += "\n\n## Problems during the run (these parts are missing from the tables above)\n\n" + "\n".join(f"- {p}" for p in problems)
    print(txt)


if __name__ == "__main__":
    main()
