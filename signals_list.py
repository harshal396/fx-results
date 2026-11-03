#!/usr/bin/env python3
"""Every signal the RSI / EMA books saw, one line each: time, book, market, side, price, what happened and why.
Read-only, standard library only. Run it INSIDE the bot's container (the journals live there):
  docker compose exec -T fxagents python - --since "2026-11-02 00:00" < ~/signals_list.py > ~/fx-results/signals_1102.md
Options:  --since "YYYY-MM-DD HH:MM" (New York time; default: 24 h back)   --hours N
          --books a,b   (default: the 15-minute books: my_ema_rsi_15m, my_ema_cross_15m, my_rsi_15m)
          --symbols XAUUSD,NDQ (default)   --actions rejected (default)  or  all  or  rejected,taken
          --data DIR (default /app/data)   --glob PATTERN (default journal*.sqlite)
Contains no tokens, keys or account numbers: only signals, prices and reasons."""
import argparse
import glob
import os
import sqlite3
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

NY = ZoneInfo("America/New_York")


def parse(s):
    if not s:
        return None
    try:
        d = datetime.fromisoformat(str(s).replace("Z", "+00:00"))
    except ValueError:
        return None
    return (d if d.tzinfo else d.replace(tzinfo=NY)).astimezone(NY)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--since")
    ap.add_argument("--hours", type=float, default=24)
    ap.add_argument("--books", default="my_ema_rsi_15m,my_ema_cross_15m,my_rsi_15m")
    ap.add_argument("--symbols", default="XAUUSD,NDQ")
    ap.add_argument("--actions", default="rejected")
    ap.add_argument("--data", default="/app/data")
    ap.add_argument("--glob", default="journal*.sqlite")
    a = ap.parse_args()
    now = datetime.now(NY)
    cutoff = parse(a.since) if a.since else now - timedelta(hours=a.hours)
    prefix = a.glob.split("*")[0]
    books = set(a.books.split(","))
    syms = set(a.symbols.split(","))
    acts = None if a.actions == "all" else set(a.actions.split(","))
    out = [f"# Signals seen by {', '.join(sorted(books))}\n", f"Generated {now:%Y-%m-%d %H:%M} New York. Since {cutoff:%Y-%m-%d %H:%M}. "
           f"Markets: {', '.join(sorted(syms))}. Actions: {a.actions}.\n",
           "| Time (NY) | Book | Market | Side | Price | What happened | Why |", "|---|---|---|---|---|---|---|"]
    rows, seen = [], []
    for f in sorted(glob.glob(os.path.join(a.data, a.glob))):
        book = os.path.basename(f)[len(prefix):-len(".sqlite")].strip("_") or "live"
        if book not in books:
            continue
        seen.append(book)
        try:
            db = sqlite3.connect(f"file:{f}?mode=ro", uri=True)
        except sqlite3.Error:
            db = sqlite3.connect(f)
        try:
            for ts, sym, side, entry, action, why in db.execute("SELECT ts, symbol, side, entry, action, why FROM signals ORDER BY id"):
                t = parse(ts)
                if t and t >= cutoff and sym in syms and (acts is None or action in acts):
                    rows.append((t, book, sym, side, entry, action, (why or "").replace("|", "/")))
        except sqlite3.Error as ex:
            out.append(f"\n(could not read {book}: {ex})")
    rows.sort(key=lambda r: (r[0], r[1]))
    for t, book, sym, side, entry, action, why in rows:
        out.append(f"| {t:%m-%d %H:%M} | {book} | {sym} | {side} | {'' if entry is None else f'{entry:.2f}'} | {action} | {why} |")
    out.append(f"\n{len(rows)} signals from {len(seen)} book(s): {', '.join(seen) or 'none found'}.")
    print("\n".join(out))


if __name__ == "__main__":
    main()
