#!/usr/bin/env python3
"""Report on the RSI / EMA books' trades and skipped signals, from the journals. Read-only, standard library only.

Run it INSIDE the bot's container (the journals live there), writing a Markdown file on the host:
  docker compose exec -T fxagents python - --hours 30 < ~/books_report.py > ~/fx-results/books_report.md
Options:  --hours N (window, default 24)   --since "2026-10-21 00:00" (New York time, overrides --hours)
          --books a,b,c (default: every my_* book except my_intraday_mom, plus ema21_rsi55)   --all (every book)
          --data DIR (default /app/data)   --glob PATTERN (default journal*.sqlite)
Contains no tokens, keys or account numbers: only trades, prices, reasons and verdicts.
"""
import argparse
import glob
import json
import os
import re
import sqlite3
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
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


def f2(x, nd=2):
    return "" if x is None else f"{x:.{nd}f}"


def rows(db, q, args=()):
    try:
        cur = db.execute(q, args)
        cols = [c[0] for c in cur.description]
        return [dict(zip(cols, r)) for r in cur.fetchall()]
    except sqlite3.Error:
        return []


def norm(why):
    return re.sub(r"[-+]?\d+(\.\d+)?", "#", why or "")[:75]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--hours", type=float, default=24)
    ap.add_argument("--since")
    ap.add_argument("--books")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--data", default="/app/data")
    ap.add_argument("--glob", default="journal*.sqlite")
    a = ap.parse_args()
    now = datetime.now(NY)
    cutoff = parse(a.since) if a.since else now - timedelta(hours=a.hours)
    prefix = a.glob.split("*")[0]
    want = set(a.books.split(",")) if a.books else None
    out, trades_all = [], []
    out.append(f"# RSI / EMA books report\n\nGenerated {now:%Y-%m-%d %H:%M} New York. Window: since {cutoff:%Y-%m-%d %H:%M} "
               f"({(now - cutoff).total_seconds() / 3600:.0f} h). R = profit as a multiple of the risk at the first stop.\n")
    summary, reasons, analyst, causes, timelines, books_seen = [], {}, {}, defaultdict(lambda: [0, 0.0]), [], []
    for f in sorted(glob.glob(os.path.join(a.data, a.glob))):
        book = os.path.basename(f)[len(prefix):-len(".sqlite")].strip("_") or "live"
        keep = (book in want) if want else (a.all or book == "ema21_rsi55" or (book.startswith("my_") and book != "my_intraday_mom"))
        if not keep:
            continue
        try:
            db = sqlite3.connect(f"file:{f}?mode=ro", uri=True)
        except sqlite3.Error:
            db = sqlite3.connect(f)
        books_seen.append(book)
        tr = [t for t in rows(db, "SELECT * FROM trades ORDER BY opened") if t["status"] == "open"
              or (parse(t["opened"]) and parse(t["opened"]) >= cutoff) or (parse(t["closed"]) and parse(t["closed"]) >= cutoff)]
        closed = [t for t in tr if t["status"] == "closed"]
        wins = [t for t in closed if (t["realized"] or 0) > 0]
        part = sum(1 for t in tr for e in json.loads(t["events"] or "[]") if e.get("kind") == "partial")
        held = [(parse(t["closed"]) - parse(t["opened"])).total_seconds() / 3600 for t in closed if parse(t["closed"]) and parse(t["opened"])]
        summary.append((book, len(tr), len(closed), len(tr) - len(closed), len(wins), sum(t["r_multiple"] or 0 for t in closed),
                        sum(t["realized"] or 0 for t in closed), sum(t["mfe_r"] or 0 for t in closed) / len(closed) if closed else 0,
                        sum(held) / len(held) if held else 0, part))
        sig = rows(db, "SELECT ts, action, why FROM signals")
        reasons[book] = Counter((s["action"], norm(s["why"])) for s in sig if parse(s["ts"]) and parse(s["ts"]) >= cutoff)
        an = rows(db, "SELECT check_name, COUNT(*) n, AVG(value) v, SUM(value > 0) good FROM analyst_outcome GROUP BY 1")
        if an:
            analyst[book] = an
        for t in tr:
            r, ev = t["r_multiple"], json.loads(t["events"] or "[]")
            if t["status"] == "closed" and r is not None and r < 0:
                mfe = t["mfe_r"] or 0
                cat = ("gave back: was +0.5R or better first" if mfe >= 0.5 else
                       "closed on the EMA exit at a loss" if "ema" in (t["exit_reason"] or "") else
                       "stopped at the first stop" if abs((t["final_stop"] or 0) - (t["initial_stop"] or 1)) < 1e-9 else "stopped after the stop moved")
                causes[cat][0] += 1; causes[cat][1] += r
            row = dict(book=book, id=str(t["id"])[:8], sym=t["symbol"], side=t["side"], opened=parse(t["opened"]), closed=parse(t["closed"]),
                       entry=t["entry"], exit=t["exit_price"], stop0=t["initial_stop"], stop=t["final_stop"], qty=t["qty_initial"],
                       pnl=t["realized"], r=r, mfe=t["mfe_r"], mae=t["mae_r"], why=t["exit_reason"] or ("OPEN" if t["status"] == "open" else ""),
                       reason=(t["reason"] or "")[:110])
            trades_all.append(row)
            if t["status"] == "open" or (r is not None and r < 0):
                ev_txt = "; ".join(f"{(parse(e.get('ts')) or now):%H:%M} {e.get('kind')}" + (f" ({str(e.get('why') or e.get('stop') or e.get('verdict') or '')[:48]})" if (e.get('why') or e.get('stop') or e.get('verdict')) else "")
                                   for e in ev[:14])
                timelines.append(f"- **{book}** {t['symbol']} {t['side']} {str(t['id'])[:8]} → {row['why']}"
                                 f" ({f2(r)}R, best {f2(t['mfe_r'])}R): {ev_txt}")
    out.append(f"Books read: {', '.join(books_seen) or 'none found - wrong --data / --glob?'}\n")
    out.append("## 1. Per book\n\n| Book | Trades | Closed | Open | Wins | Total R | P&L | Avg best R | Avg hours held | Jev partials |\n|---|---|---|---|---|---|---|---|---|---|")
    for s in summary:
        out.append(f"| {s[0]} | {s[1]} | {s[2]} | {s[3]} | {s[4]} | {s[5]:+.2f} | {s[6]:+.2f} | {s[7]:.2f} | {s[8]:.1f} | {s[9]} |")
    tot_r, tot_n = sum(s[5] for s in summary), sum(s[2] for s in summary)
    out.append(f"\nAll listed books: {tot_n} closed trades, {tot_r:+.2f} R.\n")
    out.append("## 2. Why the losing trades lost\n")
    if causes:
        out.append("| Cause | Trades | R |\n|---|---|---|")
        out += [f"| {c} | {n} | {r:+.2f} |" for c, (n, r) in sorted(causes.items(), key=lambda kv: kv[1][1])]
    else:
        out.append("No losing closed trades in the window.")
    out.append("\n## 3. Skipped signals (what the filters blocked)\n")
    for book, c in reasons.items():
        if not c:
            continue
        out.append(f"**{book}**: " + "; ".join(f"{n}x {act}: {why}" for (act, why), n in c.most_common(8)))
    out.append("\n## 4. Trade analyst (shadow) - how its advice scored\n")
    if analyst:
        out.append("| Book | Check | Times | Avg value in R (positive = its advice would have helped) | Helpful |\n|---|---|---|---|---|")
        for book, an in analyst.items():
            out += [f"| {book} | {x['check_name']} | {x['n']} | {x['v']:+.2f} | {int(x['good'] or 0)} |" for x in an]
    else:
        out.append("No scored analyst advice yet (it scores advice only when a trade closes).")
    out.append("\n## 5. Every trade in the window\n\n| Book | Id | Market | Side | Opened (NY) | Closed (NY) | Entry | Exit | First stop | Stop at end | Qty | P&L | R | Best R | Worst R | How it ended |\n|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for t in sorted(trades_all, key=lambda x: (x["book"], x["opened"] or now)):
        out.append(f"| {t['book']} | {t['id']} | {t['sym']} | {t['side']} | {t['opened']:%m-%d %H:%M} | {t['closed']:%m-%d %H:%M} | " if t["closed"] else
                   f"| {t['book']} | {t['id']} | {t['sym']} | {t['side']} | {t['opened']:%m-%d %H:%M} | open | ")
        out[-1] += f"{f2(t['entry'])} | {f2(t['exit'])} | {f2(t['stop0'])} | {f2(t['stop'])} | {f2(t['qty'])} | {f2(t['pnl'])} | {f2(t['r'])} | {f2(t['mfe'])} | {f2(t['mae'])} | {t['why']} |"
    out.append("\n## 6. Timelines of the losing and the open trades\n")
    out += timelines or ["None."]
    out.append("\n## 7. Entry reasons of every trade\n")
    out += [f"- {t['book']} {t['id']} {t['sym']} {t['side']}: {t['reason']}" for t in sorted(trades_all, key=lambda x: (x["book"], x["opened"] or now))]
    print("\n".join(out))


if __name__ == "__main__":
    main()
