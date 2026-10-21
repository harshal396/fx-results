#!/usr/bin/env python3
"""Context for every trade of the RSI / EMA books on ONE market: the candles around it (labelled like TradingView, by OPEN
time), the indicators, and measures that show whether the entry was late, a bounce, against a higher timeframe, or in chop.
Optionally scans a time window for setups that were NOT taken. Read-only. Needs OANDA_API_TOKEN (already in the container).

Run it INSIDE the bot's container, writing a Markdown file on the host:
  docker compose exec -T fxagents python - --symbol NDQ --hours 30 < ~/books_context.py > ~/fx-results/context_NDQ.md
Options: --symbol NDQ|US30|XAUUSD   --hours N | --since "2026-10-21 00:00" (New York)   --books a,b,c (default: my_* + ema21_rsi55)
         --scan "2026-10-21 09:30,2026-10-21 11:30" (also list every candle in that window with its signals and flags)
         --scan-tf 15min|1h|4h      --data DIR (default /app/data)   --glob PATTERN (default journal*.sqlite)
Contains no tokens or account numbers.
"""
import argparse
import glob
import json
import os
import sqlite3
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd

sys.path.insert(0, os.getcwd())
from fxagents import my_rules as M            # noqa: E402
from fxagents.indicators import ema           # noqa: E402

NY = ZoneInfo("America/New_York")
INST = {"NDQ": "NAS100_USD", "US30": "US30_USD", "XAUUSD": "XAU_USD"}
DELTA = {"15min": pd.Timedelta("15min"), "1h": pd.Timedelta("1h"), "4h": pd.Timedelta("4h"), "1D": pd.Timedelta("24h")}


def fetch(inst, gran, start_utc):
    """Mid-price candles from OANDA practice (read-only), paged until the newest completed candle."""
    token, host = os.environ.get("OANDA_API_TOKEN", ""), "https://api-fxpractice.oanda.com"
    rows, cur = [], start_utc.strftime("%Y-%m-%dT%H:%M:%SZ")
    while True:
        q = urllib.parse.urlencode({"granularity": gran, "price": "M", "count": 5000, "from": cur,
                                    "dailyAlignment": 17, "alignmentTimezone": "America/New_York"})
        req = urllib.request.Request(f"{host}/v3/instruments/{inst}/candles?{q}", headers={"Authorization": f"Bearer {token}"})
        cs = json.load(urllib.request.urlopen(req, timeout=60)).get("candles", [])
        for c in cs:
            if c.get("complete"):
                m = c["mid"]
                rows.append((c["time"], float(m["o"]), float(m["h"]), float(m["l"]), float(m["c"])))
        if not cs or cs[-1]["time"] == cur or not cs[-1].get("complete", True):
            break
        cur = cs[-1]["time"]
    df = pd.DataFrame(rows, columns=["t", "open", "high", "low", "close"])
    df.index = pd.DatetimeIndex(pd.to_datetime(df.pop("t"), utc=True)).tz_convert(NY)
    return df[~df.index.duplicated(keep="last")].sort_index()


def parse(s):
    if not s:
        return None
    try:
        d = datetime.fromisoformat(str(s).replace("Z", "+00:00"))
    except ValueError:
        return None
    return (d if d.tzinfo else d.replace(tzinfo=NY)).astimezone(NY)


def book_tf(book):
    for suf, tf in (("_15m", "15min"), ("_1h", "1h"), ("_4h", "4h"), ("_1d", "1D")):
        if book.endswith(suf):
            return tf
    return "15min"                                              # his ema21_rsi55 book trades 15m


def book_rule(book):
    return "rsi_mtf" if "_rsi_" in book and "ema" not in book.split("my_")[-1][:3] else "ema_rsi"


def frames(sym, start_utc, fetch_fn=None):
    fetch_fn = fetch_fn or fetch                               # resolved at call time (so tests can replace fetch)
    inst = INST[sym]
    m15 = fetch_fn(inst, "M15", start_utc)
    h1 = fetch_fn(inst, "H1", start_utc - timedelta(days=50))
    return {"15min": m15, "1h": h1, "4h": M.build_tf(h1, "4h")[0], "1D": M.build_tf(h1, "1D")[0]}, h1


def ends(df, tf):
    return df.index.tz_convert(NY).tz_localize(None) + DELTA[tf]


def indicators(fr, h1):
    out = {}
    for tf, df in fr.items():
        if len(df) < 40:
            continue
        b = M.build(df, h1, "ema_rsi", tf)
        b["ema50"] = ema(df["close"], 50)
        out[tf] = b
    return out


def last_done(b, tf, t):
    """Index of the last candle of `b` that had closed by time t (New York)."""
    e = ends(b, tf)
    i = int(np.searchsorted(e.to_numpy(), np.datetime64(t.astimezone(NY).replace(tzinfo=None)), side="right")) - 1
    return i


def arrows(c, i, n=3):
    return "".join("↑" if c[j] > c[j - 1] else "↓" if c[j] < c[j - 1] else "→" for j in range(i - n + 1, i + 1))


def diagnose(b, i, side, tf, ind):
    c, h, l, o = b["c"].to_numpy(), b["h"].to_numpy(), b["l"].to_numpy(), b["o"].to_numpy()
    e21, a, r = b["ema21"].to_numpy(), b["atr"].to_numpy(), b["rsi"].to_numpy()
    on_side = (c > e21) if side > 0 else (c < e21)
    run = 0
    while i - run >= 0 and on_side[i - run]:
        run += 1
    k = np.sign(c[max(i - 11, 0):i + 1] - e21[max(i - 11, 0):i + 1])
    crosses = int((k[1:] != k[:-1]).sum())
    ext = ((c[i] - l[max(i - 19, 0):i + 1].min()) if side > 0 else (h[max(i - 19, 0):i + 1].max() - c[i])) / a[i]
    prior = slice(max(i - 10, 0), i)
    bos = c[i] > h[prior].max() if side > 0 else c[i] < l[prior].min()
    rng = (h[i] - l[i]) or 1e-9
    d = {"close": c[i], "ema21": e21[i], "beyond EMA21 (ATR)": (c[i] - e21[i]) * side / a[i],
         "candles on this side of EMA21 (1 = this one just crossed)": run, "RSI": r[i], "RSI before": r[i - 1],
         "CHOP": b["chop"].iloc[i], "EMA21 side changes in last 12 candles": crosses, "Supertrend": int(b["st"].iloc[i]),
         "last 3 closes": arrows(c, i), "signal candle body / range": abs(c[i] - o[i]) / rng, "signal candle range (ATR)": rng / a[i],
         "move since the 20-candle extreme (ATR)": ext, "closed beyond the prior 10-candle extreme": bool(bos)}
    return d


def htf_view(ind, t, side):
    parts = []
    for tf in ("1h", "4h"):
        b = ind.get(tf)
        if b is None:
            continue
        i = last_done(b, tf, t)
        if i < 50:
            continue
        c, e21, e50, r = b["c"].iloc[i], b["ema21"].iloc[i], b["ema50"].iloc[i], b["rsi"].iloc[i]
        same = (c > e21) == (side > 0)
        parts.append(f"{tf}: close {'above' if c > e21 else 'below'} EMA21, EMA21 {'>' if e21 > e50 else '<'} EMA50, RSI {r:.0f}, "
                     f"Supertrend {'up' if b['st'].iloc[i] > 0 else 'down'} → **{'with' if same else 'AGAINST'} the trade**")
    return "; ".join(parts)


def table(b, tf, lo, hi, mark):
    ix = b.index.tz_convert(NY)
    lines = ["| Candle (opens, NY) | O | H | L | C | EMA21 | RSI | CHOP | ST | |", "|---|---|---|---|---|---|---|---|---|---|"]
    for j in range(max(lo, 0), min(hi, len(b) - 1) + 1):
        r = b.iloc[j]
        lines.append(f"| {ix[j]:%m-%d %H:%M} | {r.o:.1f} | {r.h:.1f} | {r.l:.1f} | {r.c:.1f} | {r.ema21:.1f} | {r.rsi:.1f} | {r.chop:.0f} | "
                     f"{'up' if r.st > 0 else 'dn'} | {mark.get(j, '')} |")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--symbol", required=True)
    ap.add_argument("--hours", type=float, default=30)
    ap.add_argument("--since")
    ap.add_argument("--books")
    ap.add_argument("--scan")
    ap.add_argument("--scan-tf", default="15min")
    ap.add_argument("--data", default="/app/data")
    ap.add_argument("--glob", default="journal*.sqlite")
    a = ap.parse_args()
    sym, now = a.symbol, datetime.now(NY)
    cutoff = parse(a.since) if a.since else now - timedelta(hours=a.hours)
    prefix = a.glob.split("*")[0]
    want = set(a.books.split(",")) if a.books else None
    trades, sigs = [], []
    for f in sorted(glob.glob(os.path.join(a.data, a.glob))):
        book = os.path.basename(f)[len(prefix):-len(".sqlite")].strip("_") or "live"
        if not ((book in want) if want else (book == "ema21_rsi55" or (book.startswith("my_") and book != "my_intraday_mom"))):
            continue
        db = sqlite3.connect(f"file:{f}?mode=ro", uri=True)
        db.row_factory = sqlite3.Row
        for t in db.execute("SELECT * FROM trades WHERE symbol=? ORDER BY opened", (sym,)).fetchall():
            t = dict(t)
            if t["status"] == "open" or (parse(t["opened"]) and parse(t["opened"]) >= cutoff):
                t["book"] = book
                trades.append(t)
        for s in db.execute("SELECT ts, action, why FROM signals WHERE symbol=? ORDER BY ts", (sym,)).fetchall():
            if parse(s["ts"]) and parse(s["ts"]) >= cutoff:
                sigs.append(dict(s, book=book))
    start = min([parse(t["opened"]) for t in trades] + [cutoff]).astimezone(timezone.utc) - timedelta(days=12)
    fr, h1 = frames(sym, start)
    ind = indicators(fr, h1)
    out = [f"# Context for {sym} - generated {now:%Y-%m-%d %H:%M} New York\n",
           "Candles are labelled by their OPEN time, like TradingView. The **signal candle** is the one that closed when the bot "
           "entered; the trade opened at the open of the next candle. Prices are OANDA mid prices.\n"]
    for t in trades:
        book, side = t["book"], 1 if t["side"] == "LONG" else -1
        tf = book_tf(book)
        b = ind.get(tf)
        if b is None:
            continue
        opened, closed = parse(t["opened"]), parse(t["closed"])
        i = last_done(b, tf, opened)
        j = last_done(b, tf, closed) if closed else min(i + 6, len(b) - 1)
        out.append(f"\n## {book} · {t['side']} · entered {opened:%m-%d %H:%M} → {('exited ' + closed.strftime('%m-%d %H:%M')) if closed else 'OPEN'}"
                   f" · {t['exit_reason'] or ''} · R {t['r_multiple'] if t['r_multiple'] is not None else '-'} (best {t['mfe_r'] or 0:.2f})\n")
        out.append(f"Logged entry reason: `{t['reason']}`\n")
        sig_t = b.index.tz_convert(NY)[i]
        out.append(f"Signal candle: **{sig_t:%m-%d %H:%M}** ({tf}); the trade opened right after it closed at {opened:%H:%M}.\n")
        d = diagnose(b, i, side, tf, ind)
        out.append("| Measure | Value |\n|---|---|\n" + "\n".join(f"| {k} | {v:.2f} |" if isinstance(v, (float, np.floating)) else f"| {k} | {v} |" for k, v in d.items()))
        out.append("\nHigher timeframes at that moment: " + htf_view(ind, opened, side) + "\n")
        out.append(table(b, tf, i - 8, j + 2, {i: "**SIGNAL candle (closed → entry)**", i + 1: "next candle (entry price)" if i + 1 <= j else "",
                                              j: "← exit decided on this close" if closed else ""}))
    if a.scan:
        t0, t1 = (parse(x.strip()) for x in a.scan.split(","))
        tf = a.scan_tf
        b = ind[tf]
        ix = b.index.tz_convert(NY)
        out.append(f"\n## Scan {t0:%m-%d %H:%M} → {t1:%m-%d %H:%M} on {tf}: every candle, with the books' signals\n")
        out.append("| Candle (opens) | Close | EMA21 | RSI (before) | CHOP | ST | EMA+RSI rule | EMA9/21 rule | candles above EMA21 | note |\n|---|---|---|---|---|---|---|---|---|---|")
        rs, rc = M.build(fr[tf], h1, "ema_rsi", tf), M.build(fr[tf], h1, "ema_cross", tf)
        for j in range(len(b)):
            if not (t0 <= ix[j] + DELTA[tf] <= t1):
                continue
            c = b["c"].iloc[j]
            above = 0
            while j - above >= 0 and ((b["c"].iloc[j - above] > b["ema21"].iloc[j - above]) == (c > b["ema21"].iloc[j])):
                above += 1
            rv = {1: "BUY", -1: "SELL", 0: ""}[int(rs["raw"].iloc[j])]
            cv = {1: "BUY", -1: "SELL", 0: ""}[int(rc["raw"].iloc[j])]
            note = ""
            if rv == "" and b["rsi"].iloc[j] > 55 and c > b["ema21"].iloc[j]:
                note = "above EMA21 and RSI>55, but RSI did not CROSS 55 on this candle (no signal by rule)"
            elif rv == "" and b["rsi"].iloc[j] < 44 and c < b["ema21"].iloc[j]:
                note = "below EMA21 and RSI<44, but RSI did not CROSS 44 on this candle"
            out.append(f"| {ix[j]:%m-%d %H:%M} | {c:.1f} | {b['ema21'].iloc[j]:.1f} | {b['rsi'].iloc[j]:.1f} ({b['rsi'].iloc[j - 1]:.1f}) | "
                       f"{b['chop'].iloc[j]:.0f} | {'up' if b['st'].iloc[j] > 0 else 'dn'} | {rv} | {cv} | {above}{' ↑' if c > b['ema21'].iloc[j] else ' ↓'} | {note} |")
    out.append(f"\n## Every logged signal on {sym} in the window (taken and skipped)\n")
    out.append("| Time (NY) | Book | What happened | Why |\n|---|---|---|---|")
    for s in sorted(sigs, key=lambda s: parse(s["ts"]))[:300]:
        out.append(f"| {parse(s['ts']):%m-%d %H:%M} | {s['book']} | {s['action']} | {(s['why'] or '')[:110]} |")
    print("\n".join(out))


if __name__ == "__main__":
    main()
