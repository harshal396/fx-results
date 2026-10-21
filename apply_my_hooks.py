#!/usr/bin/env python3
"""Re-adds Harshal's book hooks to the three files he shares with upstream:
    config.yaml                              book settings + the `modes:` list
    fxagents/agents/setup_first.py           MODES tuple + the dispatch to agents/my_books.py
    fxagents/dashboard/static/index.html     names / colours / descriptions on the dashboard
Idempotent (safe to run twice). The books are read from fxagents/agents/my_books.py, so adding a book there and
running this script is all that is needed. Policy: books upstream turns on stay on, except DROP below.
Run from the repo root:  python3 apply_my_hooks.py
"""
import ast
import re
import sys
from pathlib import Path

DROP = {"gold_breakout"}                      # upstream shadow books Harshal does not want to run
INFO = {                                      # book -> (dashboard name, colour, description, config comment)
    "my_ema21_rsi_1h": ("My EMA21 + RSI 55/44 (1h)", "#5bc0eb", "mine: 1h EMA21 + RSI, long & short",
                        "1h, buy close > EMA21 + RSI up through 55, sell close < EMA21 + RSI down through 44"),
    "my_rsi_mtf_1h": ("My RSI 60/40 multi-TF (1h)", "#c77dff", "mine: 1h RSI with 4h + daily",
                      "1h, 4h + daily RSI > 60 and 1h RSI up through 58 (sell: < 40 and down through 41)"),
    "my_s1_1h": ("My Strategy 1 · 1h long", "#2ec4b6", "mine: EMA21 + RSI + structure, 1h, long only",
                 "strategy 1 (EMA21 + RSI + structure), 1h, LONG only - the backtest-passing version"),
    "my_s1_15m": ("My Strategy 1 · 15m", "#ff9f1c", "mine: EMA21 + RSI + structure, 15m",
                  "strategy 1 on 15m, long and short, flat before the weekend"),
    "my_s2_15m": ("My Strategy 2 · RSI 15m", "#e76f9a", "mine: RSI 60/40 on 15m + 1h + 4h",
                  "strategy 2 (RSI 60/40: 1h + 4h RSI beyond 60/40, 15m RSI crossing 60/40), long and short, flat before the weekend"),
}
NEW_INDEX_END = {"XAUUSD": "11:00", "NDQ": "16:00", "US30": "16:00"}


def my_books() -> list[str]:
    tree = ast.parse(Path("fxagents/agents/my_books.py").read_text())
    names: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            t, v = node.targets[0].id, node.value
            if t in ("V1_BOOKS", "BOOKS") and isinstance(v, ast.Tuple):
                names += [e.value for e in v.elts if isinstance(e, ast.Constant)]
            if t == "SPECS" and isinstance(v, ast.Dict):
                names += [k.value for k in v.keys if isinstance(k, ast.Constant)]
    out = [n for n in dict.fromkeys(names) if n in INFO]
    if not out:
        sys.exit("apply_my_hooks: no books found in fxagents/agents/my_books.py")
    return out


def cfg_block(book: str) -> str:
    v1 = book in ("my_ema21_rsi_1h", "my_rsi_mtf_1h")
    s = f"  {book}:" + " " * max(1, 30 - len(book) - 3) + f"# Harshal: {INFO[book][3]}\n    symbols: [XAUUSD, NDQ, US30]\n    risk_pct: 0.005\n"
    if not v1:
        e = ", ".join(f'{k}: "{v}"' for k, v in NEW_INDEX_END.items())
        s += f"    entry_end: {{{e}}}\n"
    return s


def do_config(books: list[str]) -> str:
    p = Path("config.yaml"); s = p.read_text()
    m = re.search(r"^  modes: \[([^\]]*)\](.*)$", s, re.M)
    if not m:
        sys.exit("apply_my_hooks: no `  modes: [...]` line in config.yaml")
    add = "".join(cfg_block(b) for b in books if not re.search(rf"^  {b}:", s, re.M))
    modes = [x.strip() for x in m.group(1).split(",") if x.strip() and x.strip() not in DROP]
    modes += [b for b in books if b not in modes]
    line = f"  modes: [{', '.join(modes)}]{m.group(2)}"
    s = s[:m.start()] + add + line + s[m.end():]
    p.write_text(s)
    return ", ".join(modes)


def do_setup_first(books: list[str]) -> None:
    p = Path("fxagents/agents/setup_first.py"); s = p.read_text()
    m = re.search(r"^MODES = \((.*?)\)\n", s, re.M | re.S)
    if not m:
        sys.exit("apply_my_hooks: no MODES tuple in setup_first.py")
    have = re.findall(r'"([a-z0-9_]+)"', m.group(1))
    missing = [b for b in books if b not in have]
    if missing:
        inner = m.group(1).rstrip()
        s = s[:m.start(1)] + inner + ",\n         " + ", ".join(f'"{b}"' for b in missing) + s[m.end(1):]
    tup = ", ".join(f'"{b}"' for b in books)
    block = ("    elif mode in (%s):   # Harshal's books (agents/my_books.py)\n"
             "        from .my_books import MyBookTrader\n        trader = MyBookTrader(sctx, mode)\n") % tup
    old = re.search(r'    elif mode in \(("my_[a-z0-9_]+",? ?)+\):.*\n        from \.my_books import MyBookTrader\n        trader = MyBookTrader\(sctx, mode\)\n', s)
    if old:
        s = s[:old.start()] + block + s[old.end():]
    else:
        anchor = '    elif mode == "ema21_rsi55":'
        if anchor not in s:
            sys.exit("apply_my_hooks: anchor for the dispatch block not found in setup_first.py")
        s = s.replace(anchor, block + anchor, 1)
    p.write_text(s)


def do_dashboard(books: list[str]) -> int:
    p = Path("fxagents/dashboard/static/index.html"); s = p.read_text()
    rx = re.compile(r'ema21_rsi55:"([^"]*)"')
    out, last, n = [], 0, 0
    for m in rx.finditer(s):
        val = m.group(1)
        kind = "color" if val.startswith("#") else "name" if val.startswith("EMA21 + RSI 55") else "desc"
        seg = s[m.end(): m.end() + 1500]
        pairs = []
        for b in books:
            if re.search(rf'\b{b}:"', seg[:900]):        # already there (just after this entry)
                continue
            nm, col, desc, _ = INFO[b]
            pairs.append(f'{b}:"{ {"color": col, "name": nm, "desc": desc}[kind] }"')
        out.append(s[last:m.end()] + ("".join(f", {x}" for x in pairs)))
        last = m.end(); n += 1
    out.append(s[last:])
    if n < 4:
        sys.exit(f"apply_my_hooks: expected 4 dashboard name tables, found {n}")
    p.write_text("".join(out))
    return n


if __name__ == "__main__":
    books = my_books()
    modes = do_config(books)
    do_setup_first(books)
    n = do_dashboard(books)
    print(f"apply_my_hooks: books {books}\n  modes now: [{modes}]\n  dashboard tables updated: {n}")
