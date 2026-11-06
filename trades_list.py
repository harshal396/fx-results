#!/usr/bin/env python3
"""Every trade of the RSI / EMA books in a window, one line each, with what an analysis needs. Read-only, standard library only.
Run it INSIDE the bot's container (the journals live there):
  docker compose exec -T fxagents python - --since "2026-11-04 18:00" < ~/trades_list.py > ~/fx-results/trades_1106.md
Options:  --since "YYYY-MM-DD HH:MM" (New York time; default 48 h back)   --until "YYYY-MM-DD HH:MM"
          --books auto|a,b,c   (auto = every my_* book except my_intraday_mom, plus ema21_rsi55; closed books such as my_ema_cross_* are included)
          --symbols XAUUSD,NDQ,US30,US2000 (default)   --csv   (comma-separated lines for a spreadsheet instead of a table)
          --data DIR (default /app/data)   --glob PATTERN (default journal*.sqlite)
A trade is listed if it was opened or closed inside the window, or is still open. Contains no tokens, keys or account numbers.
Points = the average price move captured over all legs (P&L / size, partials included), signed for the side; Pips = points x 10 for gold
(a pip is $0.10), = points for the indices; Last leg = the move from entry to the final exit price only."""
import argparse
import csv
import glob
import json
import os
import re
import sqlite3
import sys
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

NY = ZoneInfo("America/New_York")
PIP = {"XAUUSD": 10.0}


def parse(s):
    if not s:
        return None
    try:
        d = datetime.fromisoformat(str(s).replace("Z", "+00:00"))
    except ValueError:
        return None
    return (d if d.tzinfo else d.replace(tzinfo=NY)).astimezone(NY)


def f(x, nd=2):
    return "" if x is None else f"{x:.{nd}f}"


def family(book):
    m = re.match(r"^(my_[a-z_]+?)_(15m|1h|4h|1d)$", book)
    return (m.group(1), m.group(2)) if m else (book, "15m" if book == "ema21_rsi55" else "")


def row(book, r):
    fam, tf = family(book)
    ev = []
    try:
        ev = json.loads(r["events"] or "[]")
    except (ValueError, TypeError):
        pass
    mode = chop = None
    for e in ev:
        if e.get("kind") == "mode":
            mode, chop = e.get("mode"), e.get("chop")
    reason = r["reason"] or ""
    if chop is None:
        m = re.search(r"CHOP (\d+(?:\.\d+)?)", reason)
        chop = float(m.group(1)) if m else None
    m = re.search(r"RSI (\d+(?:\.\d+)?)", reason)
    rsi = float(m.group(1)) if m else None
    parts = [e for e in ev if e.get("kind") == "partial"]
    liq = sum(str(e.get("why", "")).startswith("liquidity") for e in parts)
    side = 1 if str(r["side"]).upper().startswith("L") else -1
    op, cl = parse(r["opened"]), parse(r["closed"])
    qty = r["qty_initial"] or r["qty_gross"] or 0
    pl = r["realized"]
    is_open = r["status"] != "closed"
    pts = (pl / qty) if (pl is not None and qty and not is_open) else None      # an open trade has no final result: P&L is only what partials banked
    last = ((r["exit_price"] - r["entry"]) * side) if (r["exit_price"] and r["entry"]) else None
    held = ((cl or datetime.now(NY)) - op).total_seconds() / 3600 if op else None
    sym = r["symbol"]
    return {"entry": op, "book": book, "tf": tf, "market": sym, "side": "LONG" if side > 0 else "SHORT",
            "exit": cl, "held_h": held, "entry_px": r["entry"], "exit_px": r["exit_price"], "stop": r["initial_stop"],
            "last_leg": last, "points": pts, "pips": (pts * PIP.get(sym, 1.0)) if pts is not None else None, "qty": qty,
            "pnl": pl, "r": r["r_multiple"], "best_r": r["mfe_r"], "worst_r": r["mae_r"], "mode": mode or ("n/a (his book)" if book == "ema21_rsi55" else "before modes"), "chop": chop, "rsi": rsi,
            "partials": f"{len(parts)} ({liq} liq, {len(parts) - liq} Jev)" if parts else "0", "how": r["exit_reason"] or ("OPEN" if r["status"] != "closed" else ""),
            "open": is_open, "fam": fam}


COLS = [("Entry (NY)", lambda x: f"{x['entry']:%m-%d %H:%M}" if x["entry"] else ""), ("Exit (NY)", lambda x: "open" if x["open"] else f"{x['exit']:%m-%d %H:%M}" if x["exit"] else ""),
        ("Held h", lambda x: f(x["held_h"], 1)), ("Book", lambda x: x["book"]), ("Market", lambda x: x["market"]), ("Side", lambda x: x["side"]),
        ("Entry px", lambda x: f(x["entry_px"])), ("Exit px", lambda x: f(x["exit_px"])), ("Last leg", lambda x: f(x["last_leg"])),
        ("Points", lambda x: f(x["points"])), ("Pips", lambda x: f(x["pips"], 1)), ("Size", lambda x: f(x["qty"])), ("P&L $", lambda x: f(x["pnl"])),
        ("R", lambda x: f(x["r"])), ("Best R", lambda x: f(x["best_r"])), ("Worst R", lambda x: f(x["worst_r"])), ("Mode", lambda x: x["mode"]),
        ("CHOP", lambda x: f(x["chop"], 0)), ("RSI", lambda x: f(x["rsi"], 0)), ("Partials", lambda x: x["partials"]), ("How it ended", lambda x: x["how"])]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--since")
    ap.add_argument("--until")
    ap.add_argument("--hours", type=float, default=48)
    ap.add_argument("--books", default="auto")
    ap.add_argument("--symbols", default="XAUUSD,NDQ,US30,US2000")
    ap.add_argument("--csv", action="store_true")
    ap.add_argument("--data", default="/app/data")
    ap.add_argument("--glob", default="journal*.sqlite")
    a = ap.parse_args()
    now = datetime.now(NY)
    since = parse(a.since) if a.since else now - timedelta(hours=a.hours)
    until = parse(a.until) if a.until else now
    prefix = a.glob.split("*")[0]
    want = None if a.books == "auto" else set(a.books.split(","))
    syms = set(a.symbols.split(","))
    rows, seen = [], []
    for fn in sorted(glob.glob(os.path.join(a.data, a.glob))):
        book = os.path.basename(fn)[len(prefix):-len(".sqlite")].strip("_") or "live"
        ok = (book in want) if want is not None else ((book.startswith("my_") and book != "my_intraday_mom") or book == "ema21_rsi55")
        if not ok:
            continue
        try:
            db = sqlite3.connect(f"file:{fn}?mode=ro", uri=True)
        except sqlite3.Error:
            db = sqlite3.connect(fn)
        db.row_factory = sqlite3.Row
        try:
            for r in db.execute("SELECT * FROM trades"):
                if r["symbol"] not in syms:
                    continue
                op, cl = parse(r["opened"]), parse(r["closed"])
                if r["status"] == "closed" and not ((op and since <= op <= until) or (cl and since <= cl <= until)):
                    continue
                if r["status"] != "closed" and (op is None or op > until):
                    continue
                rows.append(row(book, r))
        except sqlite3.Error as ex:
            print(f"(could not read {book}: {ex})", file=sys.stderr)
        seen.append(book)
    rows.sort(key=lambda x: (x["entry"] or now, x["book"]))
    if a.csv:
        w = csv.writer(sys.stdout)
        w.writerow([c for c, _ in COLS])
        for x in rows:
            w.writerow([g(x) for _, g in COLS])
        return
    out = [f"# RSI / EMA trades, {since:%Y-%m-%d %H:%M} to {until:%Y-%m-%d %H:%M} New York\n",
           f"Markets {', '.join(sorted(syms))}. Books read: {', '.join(seen) or 'none found'}. Pips: gold points x 10, indices = points. "
           "Points are averaged over all legs (partials included); Last leg is entry to the final exit price. For an OPEN trade, P&L is only what its partials "
           "have banked so far, and Points / Pips are left blank.\n",
           "| " + " | ".join(c for c, _ in COLS) + " |", "|" + "---|" * len(COLS)]
    for x in rows:
        out.append("| " + " | ".join(g(x) for _, g in COLS) + " |")
    out.append(f"\n{len(rows)} trades ({sum(x['open'] for x in rows)} still open).\n")
    for title, key in (("By book", "book"), ("By market", "market"), ("By mode", "mode")):
        agg = {}
        for x in rows:
            if x["open"]:
                continue
            g = agg.setdefault(x[key], [0, 0, 0.0, 0.0])
            g[0] += 1
            g[1] += 1 if (x["r"] or 0) > 0 else 0
            g[2] += x["pnl"] or 0
            g[3] += x["r"] or 0
        out += [f"\n## {title} (closed trades)\n", f"| {key.capitalize()} | Trades | Wins | P&L $ | R |", "|---|---|---|---|---|"]
        for k, (n, w, p, r) in sorted(agg.items()):
            out.append(f"| {k} | {n} | {w} | {p:.2f} | {r:.2f} |")
    print("\n".join(out))


if __name__ == "__main__":
    main()
