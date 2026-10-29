"""Harshal's own shadow books. Same pattern as the ema21_rsi55 / h1_vol_trend books: virtual fills, no orders, each book
with its own journal, shown in the dashboard's book list under "RSI · EMA". Rules are frozen (fxagents/my_rules.py).

Families, each on the timeframes listed (book name = my_<family>_<timeframe>):
  my_ema_rsi_15m / 1h / 4h / 1d    EMA21 + RSI 55 / 44        buy: close > EMA21, RSI crosses up through 55
  my_rsi_15m / 1h / 4h             RSI 60 / 40 multi-timeframe  15m: 1h + 4h RSI above 60, 15m RSI crosses 60 (mirror 40)
                                                                1h: 4h + daily RSI | 4h: daily RSI only
  my_ema_cross_15m / 1h / 4h / 1d  EMA 9 / 21 cross + close beyond EMA21
  my_intraday_mom                  NDQ / US30: first-half-hour return (previous close -> 10:00 NY) sets the side of a
                                   15:30 -> 16:00 NY trade (Gao, Han, Li, Zhou, J. Financial Economics 2018)
Round-4 gates (all per book, all default OFF, installed per timeframe by apply_my_hooks.py; each was back-tested on 13 markets):
  trend_gate: no buy while the NEXT timeframe up is bearish, no sell while it is bullish (15m -> 1h, 1h -> 4h, 4h -> 1D; bullish = close above
              its EMA21 with Supertrend up or RSI > 50, bearish = the mirror, neutral allows both)
  fresh: N  the price must have crossed the EMA21 within the last N candles (the candle before that run was on the other side)
  rsi_momentum: a buy needs the RSI higher than 3 candles ago and not at a 10-candle low, a sell the mirror
  skip_big: X  skip a signal candle whose high-low range is more than X ATR
  stop_cap: cap the stop at max_stop_atr instead of skipping the trade when the swing stop is wider
Gates (switches in config.yaml, per book): use_chop (default ON): no entry in a choppy market, CHOP(14) >= chop_max
(config; 61.8 if not set, 58.5 as installed).
use_supertrend (default OFF): buys only while Supertrend(10, 3) of the book's own timeframe is up, sells only while it
is down. use_hours (default OFF): gold 20:00-11:00, NDQ / US30 20:00-16:00 New York, none 03:00-06:00 (daily books never).
Only the market-closed weekend and, for the 15m books, Friday 16:00 onward are always refused.
Exit: the first completed candle that closes back across EMA21 (the position manager closes it on the next
bar) or the dynamic stop, whichever comes first. Partial profit: once a trade is +0.5R or better, Jev is asked at every
candle close how likely price is to extend another 1R (jev.continuation); if that is below 0.45 half of what is still open
is booked (at most twice). It never acts without a live Jev answer, and it can only reduce exposure. Dynamic stop: starts beyond the low (high) of the last 8 candles
+ 0.25 x ATR (kept between 0.5 and 3 ATR); once the trade has been +1R it goes to breakeven and then trails 2 x ATR
behind the best price; stops only ever move toward profit. Trades are held overnight and over weekends (positions carry
hold_overnight, which exempts them from the 15:50 session flatten); the 15m books are flat before the weekend (Friday
16:00). The kill switch and the pre-news protection still apply. No adds, no target; Jev's grade is logged, never used.
"""
from __future__ import annotations

import json
import math

import numpy as np
import pandas as pd

from ..broker import OrderRejected
from ..indicators import atr, ema, rsi
from ..models import Bar, Leg, Position
from ..my_rules import build, build_tf, supertrend
from ..regime import CHOP_HI
from .core import Agent
from .trading import floor_step, half_spread, qty_rules

SPECS = {
    "my_ema_rsi_15m": {"rule": "ema_rsi", "tf": "15min"}, "my_ema_rsi_1h": {"rule": "ema_rsi", "tf": "1h"},
    "my_ema_rsi_4h": {"rule": "ema_rsi", "tf": "4h"}, "my_ema_rsi_1d": {"rule": "ema_rsi", "tf": "1D"},
    "my_rsi_15m": {"rule": "rsi_mtf", "tf": "15min"}, "my_rsi_1h": {"rule": "rsi_mtf", "tf": "1h"},
    "my_rsi_4h": {"rule": "rsi_mtf", "tf": "4h"},
    "my_ema_cross_15m": {"rule": "ema_cross", "tf": "15min"}, "my_ema_cross_1h": {"rule": "ema_cross", "tf": "1h"},
    "my_ema_cross_4h": {"rule": "ema_cross", "tf": "4h"}, "my_ema_cross_1d": {"rule": "ema_cross", "tf": "1D"},
}
MOM = "my_intraday_mom"
BOOKS = tuple(SPECS) + (MOM,)
DEFAULTS = {"symbols": ["XAUUSD", "NDQ", "US30"], "risk_pct": 0.005, "stop_lookback": 8, "stop_buffer_atr": 0.25,
            "min_stop_atr": 0.5, "max_stop_atr": 3.0, "trail_atr": 2.0,
            "entry_end": {"XAUUSD": "11:00", "NDQ": "16:00", "US30": "16:00"}, "entry_start": "20:00",
            "no_entry": ["03:00", "06:00"],
            "use_chop": True, "chop_max": CHOP_HI, "use_supertrend": False, "use_hours": False,   # the gates (see the docstring)
            "trend_gate": False, "fresh": 0, "rsi_momentum": False, "skip_big": 0.0, "stop_cap": False,   # round-4 gates (docstring)
            "use_partials": True, "partial_min_r": 0.5, "partial_below": 0.45, "partial_fraction": 0.5, "max_partials": 2}
H4_HOURS = (1, 5, 9, 13, 17, 21)                                       # 4h candles end at these New York hours


def _hm(s: str) -> int:
    h, m = s.split(":")
    return int(h) * 60 + int(m)


class _Base(Agent):
    """Shared by every book: config, entry hours, rejection log, Jev grade (logged only) and opening a virtual position."""
    name = "trader"
    spec: dict | None = None

    def __init__(self, ctx, book: str) -> None:
        super().__init__(ctx)
        assert book in BOOKS, book
        self.book = book

    def start(self):
        super().start()
        self.c = {**DEFAULTS, **((self.cfg.get("shadow") or {}).get(self.book) or {})}
        self.symbols = [s for s in self.c["symbols"] if s in self.cfg["instruments"]]
        self.risk_pct = float(self.c["risk_pct"])
        self.last: dict = {}
        self.use_chop, self.use_supertrend = bool(self.c["use_chop"]), bool(self.c["use_supertrend"])
        self.chop_max = float(self.c["chop_max"])
        self.trend_gate, self.fresh = bool(self.c["trend_gate"]), int(self.c["fresh"])
        self.rsi_momentum, self.skip_big, self.stop_cap = bool(self.c["rsi_momentum"]), float(self.c["skip_big"]), bool(self.c["stop_cap"])
        self.use_hours, self.use_partials = bool(self.c["use_hours"]), bool(self.c["use_partials"])
        self.bus.subscribe("bar_1m", self.on_bar)

    # ── restart safety: shadow positions live in memory only, so re-open this book's trades from its journal ──
    def stale(self, opened: pd.Timestamp) -> bool:
        """A 15m book is flat before every weekend (Friday 16:00), so a 15m trade still 'open' from before the last Friday 16:00
        is a leftover row from an earlier restart, not a live position."""
        if self.spec is None or self.spec["tf"] != "15min":
            return False
        now = self.now().tz_convert(self.cfg["timezone"])
        fri = (now - pd.Timedelta(days=(now.weekday() - 4) % 7)).replace(hour=16, minute=0, second=0, microsecond=0, nanosecond=0)
        if now < fri:
            fri -= pd.Timedelta(days=7)
        return opened.tz_convert(self.cfg["timezone"]) < fri

    def adopt(self) -> int:
        """Re-open this book's still-open trades after a restart: current stop, booked partials, events. Without this
        a restart (an update, a reboot) would silently drop trades that are meant to be held for hours or days."""
        try:
            rows = [r for r in self.ctx.journal.trades(limit=100, status="open") if r.get("strategy") == self.book]
        except Exception as e:  # noqa: BLE001
            self.log.warning("%s: could not read open trades: %s", self.book, e)
            return 0
        n = 0
        for r in rows:
            if r["symbol"] not in self.symbols or any(p.id == r["id"] for p in self.state.positions.values()):
                continue
            side = 1 if r["side"] == "LONG" else -1
            opened, entry, init_stop = pd.Timestamp(r["opened"]), float(r["entry"]), float(r["initial_stop"])
            if self.stale(opened):
                self.log.info("%s: ignoring stale open row %s from %s (older than the last weekend flat)", self.book, r["id"], r["opened"])
                continue
            pos = Position(r["symbol"], side, self.book, float(r["final_stop"]), init_stop, abs(entry - init_stop), 99.0, opened,
                           id=r["id"], reason=r.get("reason") or "", bias_mode="n/a")
            pos.add_leg(Leg(float(r["qty_initial"]), entry, opened, "initial"))
            try:
                pos.events = json.loads(r.get("events") or "[]")
            except ValueError:
                pos.events = []
            booked = [e for e in pos.events if e.get("kind") == "partial"]
            if booked:                                              # partial profit already taken before the restart
                pos.closed_qty = round(sum(float(e.get("qty", 0)) for e in booked), 6)
                pos.partial_done = True
                pos.meta["agent_partials"] = len(booked)
            pos.realized = float(r.get("realized") or 0)
            pos.meta.update(external_mgmt=True, no_pyramid=True, hold_overnight=True, max_hold=10 ** 6)
            pos.mfe_r, pos.mae_r = float(r.get("mfe_r") or 0), float(r.get("mae_r") or 0)
            pos.last_price = entry
            pos.log(self.now(), "readopted", why="bot restarted; trade restored from the journal")
            self.state.positions[pos.id] = pos
            getattr(self.ctx.broker, "open_positions", {})[pos.id] = pos
            self.log.info("%s: re-adopted open %s trade %s from %s", self.book, pos.symbol, pos.id, r["opened"])
            n += 1
        return n

    def entry_allowed(self, sym: str, t: pd.Timestamp, windows: bool | None = None) -> bool:
        windows = getattr(self, "windows", False) if windows is None else windows       # off unless use_hours
        loc = t.tz_convert(self.cfg["timezone"]) if t.tzinfo else t
        m = loc.hour * 60 + loc.minute
        if loc.dayofweek == 5 or (loc.dayofweek == 4 and m >= 17 * 60) or (loc.dayofweek == 6 and m < 18 * 60):
            return False                                            # market closed for the weekend
        if self.spec and self.spec["tf"] == "15min" and loc.dayofweek == 4 and m >= 16 * 60:
            return False                                            # the 15m books are flat before the weekend
        if not windows:
            return True
        a, z = self.c["no_entry"]
        if _hm(a) <= m < _hm(z):
            return False
        return m >= _hm(self.c["entry_start"]) or m < _hm(self.c["entry_end"].get(sym, "11:00"))

    def _reject(self, rec: dict, why: str):
        self.ctx.journal.add_signal(rec | {"action": "rejected", "why": why})
        self.log.info("%s: no trade %s: %s", self.book, rec["symbol"], why)

    def mine(self, sym: str):
        return [p for p in self.state.positions.values() if p.symbol == sym and p.status == "open" and p.strategy == self.book]

    async def jev_grade(self, sym, side, entry, stop, a, rsi_v, ema_v) -> dict | None:
        jev = getattr(self.ctx, "jev", None)
        if jev is None:
            return None
        bias = self.state.bias.get(sym, {})
        info = {"symbol": sym, "strategy": self.book, "side": "LONG" if side > 0 else "SHORT", "entry": round(entry, 4),
                "stop": stop, "reason": f"{self.book}: rule-based entry (see my_rules.py)", "risk_atr": round(abs(entry - stop) / a, 2),
                "htf_bias": 1 if bias.get("score", 0) > 0 else -1 if bias.get("score", 0) < 0 else 0,
                "rsi": round(float(rsi_v), 1), "ema21": round(float(ema_v), 4), "time_ny": str(self.now()),
                "question": f"Is the move likely to continue {'up' if side > 0 else 'down'} from here?"}
        try:
            return await jev.rate_signal(info)
        except Exception as e:  # noqa: BLE001
            self.log.warning("%s: Jev grade failed for %s: %s", self.book, sym, e)
            return None

    async def open_virtual(self, sym, side, mid, e0, stop, dist, a, rec, why, meta, g):
        """Halt / news / sizing checks, then the virtual fill. Returns True if a position was opened."""
        if not self.state.trading_enabled:
            self._reject(rec, f"trading halted: {self.state.halt_reason}"); return False
        nb = self.ctx.news.blocked(self.now()) if self.ctx.news else None
        if nb:
            self._reject(rec, f"news blackout: {nb['title']}"); return False
        ic = self.cfg["instruments"][sym]
        mult = float(ic["multiplier"])
        equity = self.state.equity or await self.ctx.broker.equity()
        if not equity or equity <= 0:
            self._reject(rec, "equity unknown"); return False
        step, min_u = qty_rules(ic)
        qty = min(floor_step(equity * self.risk_pct / (dist * mult), step), float(ic["max_units"]))
        if qty < min_u:
            self._reject(rec, f"{min_u:g} unit(s) exceed the {self.risk_pct:.2%} risk budget"); return False
        pos = Position(sym, side, self.book, stop, stop, dist, 99.0, self.now(), jev_source=(g or {}).get("source", "none"),
                       reason=why, bias_mode="n/a")
        pos.meta.update(external_mgmt=True, no_pyramid=True, max_hold=10 ** 6, hold_overnight=True,
                        jev_quality=(g or {}).get("quality"), jev_confidence=(g or {}).get("confidence"), **meta)
        try:
            px = await self.ctx.broker.open(pos, qty, mid)
        except OrderRejected as e:                                  # e.g. the broker's "stop within 10% of price" guard
            self._reject(rec, f"broker guard: {e}"); return False
        pos.risk_per_unit = abs(px - pos.initial_stop)
        pos.last_price = px
        pos.log(self.now(), "entry", price=px, qty=qty, stop=stop, risk_ccy=round(qty * pos.risk_per_unit * mult, 2),
                jev=(g or {}).get("quality"))
        self.state.positions[pos.id] = pos
        self.ctx.journal.add_signal(rec | {"action": "taken", "why": f"qty {qty}, jev {(g or {}).get('quality')}"})
        await self.bus.publish("position_opened", pos)
        return True


class MyBookTrader(_Base):
    """EMA + RSI, RSI 60/40 multi-timeframe and EMA 9/21 books on 15m / 1h / 4h / 1D candles."""

    def __init__(self, ctx, book: str) -> None:
        super().__init__(ctx, book)
        self.spec = SPECS[book]
        self.tf, self.rule = self.spec["tf"], self.spec["rule"]
        self.windows = False

    def start(self):
        super().start()
        self.windows = self.use_hours and self.tf != "1D"            # the hours rule never applies to the daily books
        self.adopt()

    HTF = {"15min": "1h", "1h": "4h", "4h": "1D"}

    def htf_state(self, h1: pd.DataFrame, wall: pd.Timestamp) -> int:
        """+1 bullish / -1 bearish / 0 neutral on the next timeframe up, from its last COMPLETED candle: close vs EMA21 with Supertrend or RSI
        agreeing (the same definition the back-test used)."""
        nxt = self.HTF.get(self.tf)
        if not nxt or not len(h1):
            return 0
        if nxt == "1h":
            d = h1
        else:
            d, end = build_tf(h1, nxt)
            d = d[end <= wall]
        if len(d) < 30:
            return 0
        c = d["close"]
        e21, r = float(ema(c, 21).iloc[-1]), float(rsi(c, 14).iloc[-1])
        st = int(supertrend(d["high"].to_numpy(), d["low"].to_numpy(), c.to_numpy())[-1])
        cv = float(c.iloc[-1])
        if cv > e21 and (st > 0 or r > 50):
            return 1
        if cv < e21 and (st < 0 or r < 50):
            return -1
        return 0

    async def on_bar(self, bar: Bar):
        self.beat()
        sym = bar.symbol
        if sym not in self.symbols:
            return
        t = bar.ts + pd.Timedelta("1min")
        boundary = t.floor("15min" if self.tf == "15min" else "1h")
        if self.last.get(sym) is not None and boundary <= self.last[sym]:
            return
        self.last[sym] = boundary
        if t - boundary > pd.Timedelta("5min"):
            return                                                 # too late after the candle closed: skip it
        wall = boundary.tz_convert(self.cfg["timezone"]).tz_localize(None)
        if (self.tf == "4h" and wall.hour not in H4_HOURS) or (self.tf == "1D" and wall.hour != 17):
            return
        h1 = self.ctx.store.h1(sym)
        h1 = h1[h1.index + pd.Timedelta("1h") <= boundary]          # completed hourly candles only
        if not len(h1):
            return
        if self.tf == "1h":
            df, end = h1, None
        elif self.tf == "15min":
            df = self.ctx.store.tf(sym, "15min")
            df = df[df.index + pd.Timedelta("15min") <= boundary]
            end = None
        else:
            df, end = build_tf(h1, self.tf)
            keep = end <= wall
            df = df[keep]
            end = end[keep]
        if not len(df):
            return
        if end is not None:
            if end[-1] != wall:
                return                                             # the newest candle is not the one that just closed
        elif df.index[-1] + pd.Timedelta("15min" if self.tf == "15min" else "1h") != boundary:
            return
        b = build(df, h1, self.rule, self.tf)
        await self.manage(sym, b, boundary)
        await self.maybe_enter(sym, b, boundary, bar, self.htf_state(h1, wall) if self.trend_gate else 0)

    # ── open positions: EMA exit, weekend flat (15m books), then the dynamic stop ──
    async def manage(self, sym: str, b: pd.DataFrame, boundary: pd.Timestamp):
        c, e, a = float(b.c.iloc[-1]), float(b.ema21.iloc[-1]), float(b.atr.iloc[-1])
        q = float(self.cfg["instruments"][sym]["tick_size"])
        for pos in self.mine(sym):
            if pd.Timestamp(pos.opened_ts) >= boundary or pos.meta.get("pending_close"):
                continue
            if (pos.side > 0 and c < e) or (pos.side < 0 and c > e):
                pos.meta["pending_close"] = "close_past_ema21"
                pos.log(self.now(), "exit_signal", close=round(c, 4), ema21=round(e, 4))
                continue
            if self.tf == "15min":
                loc = boundary.tz_convert(self.cfg["timezone"])
                if loc.dayofweek == 4 and loc.hour * 60 + loc.minute >= 16 * 60:        # flat before the weekend
                    pos.meta["pending_close"] = "weekend_close"
                    pos.log(self.now(), "exit_signal", why="flat before the weekend")
                    continue
            if self.use_partials:
                await self.agent_partial(sym, pos, b)
                if pos.status != "open" or pos.open_qty <= 0:
                    continue
            R = pos.risk_per_unit
            if not R or pos.mfe_r < 1.0 or not np.isfinite(a):
                continue
            best = pos.entry + pos.side * pos.mfe_r * R
            new = pos.stop
            for lv in (pos.entry, best - pos.side * float(self.c["trail_atr"]) * a):   # breakeven, then 2×ATR trail
                lv = math.floor(lv / q) * q if pos.side > 0 else math.ceil(lv / q) * q
                new = max(new, lv) if pos.side > 0 else min(new, lv)
            if (new - pos.stop) * pos.side < q / 2:
                continue
            last = self.state.last_prices.get(sym, c)
            if (last - new) * pos.side <= 0:                      # price is already through the new stop
                pos.meta["pending_close"] = "trail_through"
                pos.log(self.now(), "trail_through", stop=new)
                continue
            try:
                await self.ctx.broker.move_stop(pos, new)
            except OrderRejected as e:
                self.log.warning("%s: stop move refused for %s: %s", self.book, sym, e)
                continue
            pos.log(self.now(), "stop_moved", stop=pos.stop, why="breakeven / 2×ATR trail after +1R")
            await self.bus.publish("position_updated", {"position": pos, "event": "stop_to_profit",
                                                        "msg": f"stop -> {pos.stop} (locks {pos.r_now(pos.stop):+.2f}R)"})

    # ── partial profit: Jev decides ──
    async def agent_partial(self, sym: str, pos: Position, b: pd.DataFrame):
        """Once a trade is in profit, ask Jev at every candle close whether price is likely to extend another 1R. A low
        answer (< partial_below) books `partial_fraction` of what is still open, at most `max_partials` times. Nothing
        happens without a live Jev answer, and the only thing it can do is reduce the position."""
        jev = getattr(self.ctx, "jev", None)
        done = int(pos.meta.get("agent_partials", 0))
        if jev is None or done >= int(self.c["max_partials"]) or pos.open_qty <= 0:
            return
        c, e = float(b.c.iloc[-1]), float(b.ema21.iloc[-1])
        r_now = pos.r_now(c)
        if r_now < float(self.c["partial_min_r"]):
            return
        side_ok = (c > e and float(b.rsi.iloc[-1]) > 50) if pos.side > 0 else (c < e and float(b.rsi.iloc[-1]) < 50)
        info = {"symbol": sym, "side": "LONG" if pos.side > 0 else "SHORT", "strategy": self.book, "timeframe": self.tf,
                "r_now": round(r_now, 2), "mfe_r": round(float(pos.mfe_r), 2), "stage": done,
                "stop_locked_r": round(pos.r_now(pos.stop), 2), "momentum_aligned": int(side_ok),
                "rsi": round(float(b.rsi.iloc[-1]), 1), "adx": None,
                "news_next_hours": self.ctx.news.brief(self.now(), 2) if self.ctx.news else [],
                "recent_bars": b[["o", "h", "l", "c"]].iloc[-8:].round(4).to_numpy().tolist()}
        try:
            res = await jev.continuation(info)
        except Exception as ex:  # noqa: BLE001
            self.log.warning("%s: Jev continuation failed for %s: %s", self.book, sym, ex)
            return
        if pos.status != "open":
            return
        prob, src, below = float(res["prob"]), res.get("source"), float(self.c["partial_below"])
        if src != "jev":
            pos.log(self.now(), "agent_check", prob=round(prob, 2), source=src, action="hold", why="no live Jev answer")
            return
        if prob >= below:
            pos.log(self.now(), "agent_check", prob=round(prob, 2), source=src, action="hold", r=round(r_now, 2),
                    why=f"continuation {prob:.2f} ≥ {below:g}")
            return
        step, min_u = qty_rules(self.cfg["instruments"][sym])
        cut = floor_step(pos.open_qty * float(self.c["partial_fraction"]), step)
        if cut < min_u or pos.open_qty - cut < min_u:
            pos.log(self.now(), "agent_check", prob=round(prob, 2), source=src, action="hold", why="too small to split")
            return
        before = pos.closed_qty
        try:
            px = await self.ctx.broker.reduce(pos, cut, self.state.last_prices.get(sym, c))
        except OrderRejected as ex:
            pos.log(self.now(), "partial_failed", why=str(ex)[:200]); return
        if px is None or pos.closed_qty - before <= 1e-9:
            pos.log(self.now(), "partial_noop", why="broker reduced nothing"); return
        pos.meta["agent_partials"] = done + 1
        pos.partial_done = True
        pos.log(self.now(), "partial", price=px, qty=cut, r=round(r_now, 2), prob=round(prob, 2),
                why=f"Jev: continuation {prob:.2f} < {below:g}")
        await self.bus.publish("position_updated", {"position": pos, "event": "partial",
                                                    "msg": f"booked {cut} @ {px} (+{r_now:.1f}R, Jev {prob:.2f})"})

    # ── new entries: signal, then Supertrend (optional), chop, hours (optional), stop width ──
    async def maybe_enter(self, sym: str, b: pd.DataFrame, boundary: pd.Timestamp, bar: Bar, htf: int = 0):
        raw = int(b.raw.iloc[-1])
        side = 1 if raw > 0 else -1 if raw < 0 else 0
        if not side or self.mine(sym):
            return
        mid = self.state.last_prices.get(sym, bar.close)
        hs = half_spread(self.cfg, sym)
        q = float(self.cfg["instruments"][sym]["tick_size"])
        a = float(b.atr.iloc[-1])
        e0 = mid + side * hs
        n = int(self.c["stop_lookback"])
        ext = float(b.l.iloc[-n:].min()) if side > 0 else float(b.h.iloc[-n:].max())
        stop = ext - side * float(self.c["stop_buffer_atr"]) * a
        dist = (e0 - stop) * side
        if dist < float(self.c["min_stop_atr"]) * a:
            dist = float(self.c["min_stop_atr"]) * a
            stop = e0 - side * dist
        if self.stop_cap and np.isfinite(a) and a > 0 and dist > float(self.c["max_stop_atr"]) * a:
            dist = float(self.c["max_stop_atr"]) * a                       # capped instead of skipped
            stop = e0 - side * dist
        stop = math.floor(stop / q) * q if side > 0 else math.ceil(stop / q) * q
        dist = (e0 - stop) * side
        rec = {"ts": self.now().isoformat(), "symbol": sym, "strategy": self.book, "side": side, "entry": round(e0, 6),
               "stop": stop, "quality": None, "confidence": None}
        if self.skip_big and np.isfinite(a) and a > 0:
            rng = float(b.h.iloc[-1] - b.l.iloc[-1]) / a
            if rng > self.skip_big:
                return self._reject(rec, f"oversized signal candle ({rng:.1f} ATR, limit {self.skip_big:g})")
        if self.fresh:
            sg = np.sign(b.c.to_numpy() - b.ema21.to_numpy())
            i = len(sg) - 1
            run = 1
            while i - run >= 0 and sg[i - run] == sg[i]:
                run += 1
            if run > self.fresh or i - run < 0 or sg[i - run] != -sg[i]:
                return self._reject(rec, f"not a fresh cross (the price has been {'above' if side > 0 else 'below'} the EMA21 for {run} "
                                         f"candles, limit {self.fresh})")
        if self.rsi_momentum:
            rv = b.rsi.to_numpy()
            i = len(rv) - 1
            if i >= 10:
                if side > 0 and (rv[i] <= rv[i - 3] or rv[i] <= rv[i - 10:i].min()):
                    return self._reject(rec, f"RSI not rising (RSI {rv[i]:.1f}, {rv[i - 3]:.1f} three candles ago) - no buy")
                if side < 0 and (rv[i] >= rv[i - 3] or rv[i] >= rv[i - 10:i].max()):
                    return self._reject(rec, f"RSI not falling (RSI {rv[i]:.1f}, {rv[i - 3]:.1f} three candles ago) - no sell")
        st = int(b.st.iloc[-1])
        if self.use_supertrend and side * st <= 0:
            return self._reject(rec, f"against Supertrend ({'up' if st > 0 else 'down'}) - a {'buy' if side > 0 else 'sell'} "
                                     f"needs it {'up' if side > 0 else 'down'}")
        chop = float(b.chop.iloc[-1])
        if self.use_chop and chop >= self.chop_max:
            return self._reject(rec, f"choppy market (CHOP {chop:.1f} ≥ {self.chop_max:g})")
        if self.trend_gate and htf and side * htf < 0:
            return self._reject(rec, f"against the {self.HTF.get(self.tf, '')} trend ({'bearish' if htf < 0 else 'bullish'}) - "
                                     f"no {'buy' if side > 0 else 'sell'}")
        if not self.entry_allowed(sym, boundary):
            return self._reject(rec, "outside entry hours" if self.windows else "market closed (weekend / flat before the weekend)")
        if not np.isfinite(a) or a <= 0 or dist <= 0 or dist > float(self.c["max_stop_atr"]) * a + (q if self.stop_cap else 0.0):
            return self._reject(rec, f"stop too wide ({dist / a:.1f} ATR)" if a > 0 else "no ATR yet")
        g = await self.jev_grade(sym, side, e0, stop, a, b.rsi.iloc[-1], b.ema21.iloc[-1])      # logged only
        if g:
            rec.update(quality=g.get("quality"), confidence=g.get("confidence"))
        why = (f"{self.book}: {self.tf} close {b.c.iloc[-1]:.2f} {'>' if side > 0 else '<'} EMA21 {b.ema21.iloc[-1]:.2f}, "
               f"RSI {b.rsi.iloc[-1]:.1f}, CHOP {chop:.0f}, Supertrend {'up' if st > 0 else 'down'}")
        await self.open_virtual(sym, side, mid, e0, stop, dist, a, rec, why,
                                {"atr_tf": round(a, 4), "rsi": round(float(b.rsi.iloc[-1]), 2), "chop": round(chop, 1),
                                 "supertrend": st}, g)


class MyIntradayMomTrader(_Base):
    """Market intraday momentum: the return from the previous 16:00 close to 10:00 New York sets the direction of a
    15:30 -> 16:00 trade (long if positive, short if negative). One trade per index per day."""

    def start(self):
        super().start()
        self.c = {**{"symbols": ["NDQ", "US30"], "risk_pct": 0.005, "stop_atr": 3.0}, **((self.cfg.get("shadow") or {}).get(self.book) or {})}
        self.symbols = [s for s in self.c["symbols"] if s in self.cfg["instruments"]]
        self.risk_pct = float(self.c["risk_pct"])
        self.done: set = set()
        self.adopt()

    def first_half_hour_return(self, sym: str, loc: pd.Timestamp):
        """(return, previous close, price at 10:00) or None when the data is missing."""
        m1 = self.ctx.store.m1(sym)
        t10 = loc.replace(hour=10, minute=0)
        y = m1[(m1.index >= t10 - pd.Timedelta("5min")) & (m1.index < t10)]
        if not len(y):
            return None
        p10 = float(y["close"].iloc[-1])
        for k in range(1, 6):                                      # most recent earlier session with a 16:00 close
            t16 = (loc - pd.Timedelta(days=k)).replace(hour=16, minute=0)
            x = m1[(m1.index >= t16 - pd.Timedelta("5min")) & (m1.index < t16)]
            if len(x):
                pc = float(x["close"].iloc[-1])
                return p10 / pc - 1.0, pc, p10
        return None

    async def on_bar(self, bar: Bar):
        self.beat()
        sym = bar.symbol
        if sym not in self.symbols:
            return
        loc = (bar.ts + pd.Timedelta("1min")).tz_convert(self.cfg["timezone"])
        m = loc.hour * 60 + loc.minute
        key = (sym, loc.date())
        if m == 15 * 60 + 30 and key not in self.done and loc.dayofweek < 5:
            self.done.add(key)
            await self.maybe_enter(sym, loc, bar)
        if not (15 * 60 + 30 <= m < 16 * 60):                      # out of the 15:30-16:00 window: close what is left
            for pos in self.mine(sym):
                if not pos.meta.get("pending_close"):
                    pos.meta["pending_close"] = "session_close"
                    pos.log(self.now(), "exit_signal", why="end of the 15:30-16:00 window")

    async def maybe_enter(self, sym: str, loc: pd.Timestamp, bar: Bar):
        mid = self.state.last_prices.get(sym, bar.close)
        rec = {"ts": self.now().isoformat(), "symbol": sym, "strategy": self.book, "side": 0, "entry": round(mid, 6),
               "stop": None, "quality": None, "confidence": None}
        fh = self.first_half_hour_return(sym, loc)
        if fh is None:
            return self._reject(rec, "no 16:00 close / 10:00 price in the data")
        r1, pc, p10 = fh
        if abs(r1) < 1e-5:
            return self._reject(rec, f"first half-hour return is flat ({r1:+.4%})")
        side = 1 if r1 > 0 else -1
        df = self.ctx.store.tf(sym, "15min")
        df = df[df.index + pd.Timedelta("15min") <= loc.floor("15min")]
        a = float(atr(df, 14).iloc[-1]) if len(df) > 20 else float("nan")
        if not np.isfinite(a) or a <= 0:
            return self._reject(rec, "no ATR yet")
        q = float(self.cfg["instruments"][sym]["tick_size"])
        e0 = mid + side * half_spread(self.cfg, sym)
        dist = float(self.c["stop_atr"]) * a
        stop = e0 - side * dist
        stop = math.floor(stop / q) * q if side > 0 else math.ceil(stop / q) * q
        dist = (e0 - stop) * side
        rec.update(side=side, stop=stop)
        if self.mine(sym):
            return
        why = (f"{self.book}: first half-hour {r1:+.3%} (16:00 close {pc:.2f} -> 10:00 {p10:.2f}) -> "
               f"{'long' if side > 0 else 'short'} 15:30-16:00")
        await self.open_virtual(sym, side, mid, e0, stop, dist, a, rec, why, {"r1": round(r1, 6), "atr15": round(a, 4)}, None)
