#!/usr/bin/env python3
"""Re-adds Harshal's book hooks to the three files he shares with upstream:
    config.yaml                              book settings + the `modes:` list (+ chop_filter on his ema21_rsi55 book)
    fxagents/agents/ema_rsi_trader.py        the chop gate on his EMA21 + RSI 55 book (three small insertions)
    fxagents/agents/setup_first.py           MODES tuple + the dispatch to agents/my_books.py
    fxagents/dashboard/static/index.html     names / colours / descriptions, and the "RSI · EMA" group in the book list
Idempotent (safe to run twice). The books are read from fxagents/agents/my_books.py (SPECS + MOM), so adding a book
there and running this script is all that is needed. Books that are no longer defined there are removed again.
Policy: books upstream turns on stay on, except DROP below.   Run from the repo root:  python3 apply_my_hooks.py
"""
import ast
import re
import sys
from pathlib import Path

DROP = {"gold_breakout",                      # upstream shadow books Harshal does not want to run
        "my_rsi_15m"}                         # RSI 60/40 on 15 minutes: retired (the other 15m books stay)
CHOP_MAX = 58.5                              # choppy-market cutoff written into every book that does not have one yet
def gates_for(book: str) -> list[tuple[str, str, str]]:
    """(key, value, comment) of the round-4 gates for a book, by its timeframe; back-tested on 13 markets (backtest 4 and 5)."""
    tf = book.rsplit("_", 1)[-1]
    trend = ("trend_gate", "true", "no buy while the next timeframe up is bearish, no sell while it is bullish")
    if tf in ("15m", "1h"):
        return [trend, ("fresh", "2", "the price must have crossed the EMA21 within the last 2 candles (0 = off)"),
                ("rsi_momentum", "true", "a buy needs the RSI rising, a sell the RSI falling (and not at a 10-candle extreme)")]
    if tf == "4h":
        return [trend, ("skip_big", "2.5", "skip a signal candle larger than 2.5 ATR (0 = off)"),
                ("stop_cap", "true", "cap the stop at 3 ATR instead of skipping the trade")]
    return []                                                              # daily books: no round-4 gates (they did not help)


TFN = {"15m": "15 minutes", "1h": "1 hour", "4h": "4 hours", "1d": "1 day"}
FAM = {"my_ema_rsi": ("EMA21 + RSI 55/44", "#4f8cff", "buy: close > EMA21 + RSI up through 55; sell mirrored"),
       "my_rsi": ("RSI 60/40", "#a97cf5", "buy: higher-timeframe RSI > 60 + RSI up through 60; sell: < 40 and down through 40"),
       "my_ema_cross": ("EMA 9/21 cross", "#2ec4a6", "buy: EMA9 crosses above EMA21 + close above EMA21; sell mirrored")}
TINT = {"15m": 0, "1h": 1, "4h": 2, "1d": 3}


def shade(hex_color: str, k: int) -> str:                           # a lighter / darker variant per timeframe
    r, g, b = (int(hex_color[i:i + 2], 16) for i in (1, 3, 5))
    f = [0.78, 1.0, 1.18, 1.36][k]
    r, g, b = (max(0, min(255, int(v * f))) for v in (r, g, b))
    return f"#{r:02x}{g:02x}{b:02x}"


def info(book: str):
    """(dashboard name, colour, description, config comment)"""
    if book == "my_intraday_mom":
        return ("My Intraday momentum", "#ff9f1c", "mine: NDQ / US30 first half-hour sets the 15:30-16:00 trade",
                "NDQ / US30, first-half-hour return (prev close -> 10:00) sets a 15:30 -> 16:00 trade (Gao, Han, Li, Zhou 2018)")
    for fam, (nm, col, desc) in FAM.items():
        m = re.fullmatch(rf"{fam}_(15m|1h|4h|1d)", book)
        if m:
            tf = m.group(1)
            return (f"My {nm} · {tf}", shade(col, TINT[tf]), f"mine: {nm}, {TFN[tf]}, never against Supertrend",
                    f"{nm}, {TFN[tf]}, long and short, never against the Supertrend (10, 3); {desc}")
    return None


def my_books() -> list[str]:
    tree = ast.parse(Path("fxagents/agents/my_books.py").read_text())
    names: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            t, v = node.targets[0].id, node.value
            if t == "SPECS" and isinstance(v, ast.Dict):
                names += [k.value for k in v.keys if isinstance(k, ast.Constant)]
            if t == "MOM" and isinstance(v, ast.Constant):
                names.append(v.value)
    out = [n for n in dict.fromkeys(names) if info(n) and n not in DROP]
    if not out:
        sys.exit("apply_my_hooks: no books found in fxagents/agents/my_books.py")
    return out


def cfg_block(book: str) -> str:
    pad = " " * max(1, 30 - len(book) - 3)
    s = f"  {book}:{pad}# Harshal: {info(book)[3]}\n"
    if book == "my_intraday_mom":
        return s + "    symbols: [NDQ, US30]\n    risk_pct: 0.005\n    stop_atr: 3.0         # protective stop = 3 x ATR(14, 15m); the trade is closed at 16:00 anyway\n"
    return (s + f"    symbols: [{'XAUUSD, NDQ' if book.endswith('_15m') else 'XAUUSD, NDQ, US30'}]\n    risk_pct: 0.005\n"
            "    use_chop: true          # no entry when CHOP(14) >= chop_max\n"
            f"    chop_max: {CHOP_MAX}        # choppy-market cutoff (the bot's default is 61.8)\n"
            + "".join(f"    {k}: {v}{' ' * max(1, 22 - len(k) - len(v))}# {c}\n" for k, v, c in gates_for(book)) +
            "    use_supertrend: false   # true = buys only while Supertrend(10, 3) is up, sells only while it is down\n"
            "    use_hours: false        # true = gold 20:00-11:00, NDQ / US30 20:00-16:00 New York, none 03:00-06:00 (never for daily books)\n"
            "    use_partials: true      # Jev decides partial profit (once +0.5R: continuation < 0.45 books half of what is open, max twice)\n")


def ensure_key(s: str, section: str, key: str, line: str, after: str | None = None) -> str:
    """Add `line` to `section` of config.yaml if the section has no `key` yet; an existing value is never touched."""
    m = re.search(rf"^  {section}:[^\n]*\n((?:    [^\n]*\n)*)", s, re.M)
    if not m or re.search(rf"^    {key}:", m.group(1), re.M):
        return s
    block = m.group(1)
    a = re.search(rf"^    {after}:[^\n]*\n", block, re.M) if after else None
    pos = (m.start(1) + a.end()) if a else m.end()
    return s[:pos] + line + s[pos:]


def do_config(books: list[str]) -> str:
    p = Path("config.yaml"); s = p.read_text()
    lines = s.split("\n")
    out, skip = [], False
    for ln in lines:                                                   # drop sections of my_* books that no longer exist
        m = re.match(r"^  (my_[a-z0-9_]+):", ln)
        if m:
            skip = m.group(1) not in books
            if skip:
                continue
        elif skip and (ln.startswith("    ") or ln.strip() == ""):
            if ln.strip() == "" and out and out[-1].strip() == "":
                pass
            continue
        else:
            skip = False
        out.append(ln)
    s = "\n".join(out)
    for b in books:
        if b != "my_intraday_mom":
            s = ensure_key(s, b, "chop_max", f"    chop_max: {CHOP_MAX}        # choppy-market cutoff (the bot's default is 61.8)\n", after="use_chop")
    for b in books:
        if b == "my_intraday_mom":
            continue
        for k, v, c in reversed(gates_for(b)):                            # each missing key goes right under chop_max; a value you set is never touched
            s = ensure_key(s, b, k, f"    {k}: {v}{' ' * max(1, 22 - len(k) - len(v))}# {c}\n", after="chop_max")
        if b.endswith("_15m"):                                             # US30 loses on 15 minutes: drop it once, if the list is still the old default
            s = re.sub(rf"(^  {b}:[^\n]*\n(?:    [^\n]*\n)*?    symbols: )\[XAUUSD, NDQ, US30\]", r"\g<1>[XAUUSD, NDQ]", s, count=1, flags=re.M)
    m = re.search(r"^  modes: \[([^\]]*)\](.*)$", s, re.M)
    if not m:
        sys.exit("apply_my_hooks: no `  modes: [...]` line in config.yaml")
    add = "".join(cfg_block(b) for b in books if not re.search(rf"^  {b}:", s, re.M))
    modes = [x.strip() for x in m.group(1).split(",") if x.strip() and x.strip() not in DROP and not (x.strip().startswith("my_") and x.strip() not in books)]
    modes += [b for b in books if b not in modes]
    s = s[:m.start()] + add + f"  modes: [{', '.join(modes)}]{m.group(2)}" + s[m.end():]
    p.write_text(s)
    return ", ".join(modes)


def do_setup_first(books: list[str]) -> None:
    p = Path("fxagents/agents/setup_first.py"); s = p.read_text()
    m = re.search(r"^MODES = \((.*?)\)\n", s, re.M | re.S)
    if not m:
        sys.exit("apply_my_hooks: no MODES tuple in setup_first.py")
    names = [n for n in re.findall(r'"([a-z0-9_]+)"', m.group(1)) if not (n.startswith("my_") and n not in books)]
    names += [b for b in books if b not in names]
    base = [n for n in names if not n.startswith("my_")]
    mine = [n for n in names if n.startswith("my_")]
    body = ", ".join(f'"{n}"' for n in base) + (",\n         " + ", ".join(f'"{n}"' for n in mine) if mine else "")
    s = s[:m.start(1)] + body + s[m.end(1):]
    spec_books = [b for b in books if b != "my_intraday_mom"]
    tup = ", ".join(f'"{b}"' for b in spec_books)
    block = (f"    elif mode in ({tup}):   # Harshal's books (agents/my_books.py)\n"
             "        from .my_books import MyBookTrader\n        trader = MyBookTrader(sctx, mode)\n")
    if "my_intraday_mom" in books:
        block += ('    elif mode == "my_intraday_mom":\n        from .my_books import MyIntradayMomTrader\n'
                  "        trader = MyIntradayMomTrader(sctx, mode)\n")
    old = re.search(r'    elif mode in \(("my_[a-z0-9_]+",? ?)+\):.*\n        from \.my_books import MyBookTrader\n'
                    r'        trader = MyBookTrader\(sctx, mode\)\n'
                    r'(    elif mode == "my_intraday_mom":\n        from \.my_books import MyIntradayMomTrader\n'
                    r'        trader = MyIntradayMomTrader\(sctx, mode\)\n)?', s)
    if old:
        s = s[:old.start()] + block + s[old.end():]
    else:
        anchor = '    elif mode == "ema21_rsi55":'
        if anchor not in s:
            sys.exit("apply_my_hooks: anchor for the dispatch block not found in setup_first.py")
        s = s.replace(anchor, block + anchor, 1)
    p.write_text(s)


GROUP_JS = '''// Harshal: the "RSI · EMA" group in the book list (my books + EMA21 + RSI 55; not the daily RSI2/ADX2 book)
const BOOK_GROUP = b => (b === "ema21_rsi55" || /^my_(ema|rsi)_/.test(b)) ? "RSI · EMA" : "";
const bookOrder = bs => [...bs.filter(b => !BOOK_GROUP(b)), ...bs.filter(b => BOOK_GROUP(b))];
'''
GROUP_CSS = ('.bookpane{max-height:80vh;overflow-y:auto} .bookpane h5.bgh{margin:12px 10px 2px;font-size:11px;letter-spacing:.07em;'
             'text-transform:uppercase;color:var(--muted);font-weight:600}\n')


def do_dashboard(books: list[str]) -> int:
    p = Path("fxagents/dashboard/static/index.html"); s = p.read_text()
    s = re.sub(r',\s*my_[a-z0-9_]+:"[^"]*"', "", s)                      # clear my entries, then add the current ones
    rx = re.compile(r'ema21_rsi55:"([^"]*)"')
    out, last, n = [], 0, 0
    for m in rx.finditer(s):
        val = m.group(1)
        kind = "color" if val.startswith("#") else "name" if val.startswith("EMA21 + RSI 55") else "desc"
        pairs = []
        for b in books:
            nm, col, desc, _ = info(b)
            pairs.append(f'{b}:"{ {"color": col, "name": nm, "desc": desc}[kind] }"')
        out.append(s[last:m.end()] + "".join(f", {x}" for x in pairs))
        last = m.end(); n += 1
    out.append(s[last:])
    if n < 4:
        sys.exit(f"apply_my_hooks: expected 4 dashboard name tables, found {n}")
    s = "".join(out)
    if "const bookOrder" in s:                                          # already wired: refresh the group rule only
        s = re.sub(r'// Harshal: the "RSI · EMA" group[^\n]*\nconst BOOK_GROUP[^\n]*\nconst bookOrder[^\n]*\n', lambda _: GROUP_JS, s, count=1)
    else:                                                               # the grouped book list (first time)
        a1 = "const bookColor = b => b === \"live\""
        a2 = '["live", ...BOOKS].map(b => {'
        a3 = 'return `<button class="bi ${b===BOOK?"on":""}"'
        a4 = ".bookpane .foot{"
        for a in (a1, a2, a3, a4):
            if s.count(a) != 1:
                sys.exit(f"apply_my_hooks: dashboard anchor not found exactly once: {a[:50]}")
        s = s.replace(a1, GROUP_JS + a1, 1)
        s = s.replace(a2, 'bookOrder(["live", ...BOOKS]).map((b, i, arr) => {', 1)
        s = s.replace(a3, 'return ((BOOK_GROUP(b) && BOOK_GROUP(b) !== BOOK_GROUP(arr[i-1] || "")) ? `<h5 class="bgh">${BOOK_GROUP(b)}</h5>` : "") + '
                          + a3[len("return "):], 1)
        s = s.replace(a4, GROUP_CSS + a4, 1)
    p.write_text(s)
    return n


def do_his_ema_chop() -> str:
    """The chop gate on his EMA21 + RSI 55 book: a config switch (shadow.ema21_rsi55.chop_filter) and three small
    insertions in agents/ema_rsi_trader.py. Idempotent."""
    c = Path("config.yaml"); s = c.read_text()
    m = re.search(r"^  ema21_rsi55:[^\n]*\n((?:    [^\n]*\n)+)", s, re.M)
    if not m:
        return "his ema21_rsi55 section not found in config.yaml (skipped)"
    if "chop_filter" not in m.group(0):
        s = s[:m.end()] + "    chop_filter: true           # Harshal: no entry when CHOP(14, 15m) >= chop_max (agents/ema_rsi_trader.py)\n" + s[m.end():]
    s = ensure_key(s, "ema21_rsi55", "chop_max", f"    chop_max: {CHOP_MAX}            # choppy-market cutoff for the chop gate above\n", after="chop_filter")
    c.write_text(s)
    p = Path("fxagents/agents/ema_rsi_trader.py"); x = p.read_text()
    if "self.chop_filter" in x:
        if "self.chop_max" not in x:                                   # upgrade an older install: the cutoff becomes a setting
            mm = re.search(r"^( *)self\.chop_filter = [^\n]*\n", x, re.M)
            x = x[:mm.end()] + f'{mm.group(1)}self.chop_max = float(c.get("chop_max", CHOP_HI))                # Harshal: chop cutoff (config)\n' + x[mm.end():]
            x = x.replace("if ch >= CHOP_HI:", "if ch >= self.chop_max:").replace("(CHOP {ch:.1f} ≥ {CHOP_HI})", "(CHOP {ch:.1f} ≥ {self.chop_max:g})")
            p.write_text(x)
            return "chop cutoff is now a setting (chop_max) on his EMA21 + RSI 55 book"
        return "chop filter already in place"
    a1 = "from ..simple_rules import ema, wilder\n"
    a2 = '        self.stop_atr = float(c.get("stop_atr", 3.0))\n'
    a3 = "        g = await self.jev_grade(sym, b, e0, stop, atr, side)"
    for a in (a1, a2, a3):
        if x.count(a) != 1:
            return f"ema_rsi_trader.py changed upstream - anchor missing: {a[:40]!r} (chop filter NOT applied)"
    x = x.replace(a1, a1 + "from ..regime import CHOP_HI, chop_index\n", 1)
    x = x.replace(a2, a2 + '        self.chop_filter = bool(c.get("chop_filter", False))             # Harshal: chop gate (config)\n'
                  '        self.chop_max = float(c.get("chop_max", CHOP_HI))                # Harshal: chop cutoff (config)\n', 1)
    x = x.replace(a3, ("        if self.chop_filter:                                              # Harshal: the same chop gate as his own books\n"
                       '            ch = float(chop_index(pd.DataFrame({"high": b.h, "low": b.l, "close": b.c})).iloc[-1])\n'
                       "            if ch >= self.chop_max:\n"
                       '                return self._reject(rec, f"choppy market (CHOP {ch:.1f} ≥ {self.chop_max:g})")\n') + a3, 1)
    p.write_text(x)
    return "chop filter added to his EMA21 + RSI 55 book"


if __name__ == "__main__":
    books = my_books()
    modes = do_config(books)
    do_setup_first(books)
    n = do_dashboard(books)
    chop = do_his_ema_chop()
    print(f"apply_my_hooks: {len(books)} books\n  modes now: [{modes}]\n  dashboard tables updated: {n}\n  his EMA21 + RSI 55 book: {chop}")
