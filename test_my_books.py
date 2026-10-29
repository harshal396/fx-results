"""Harshal's shadow books (agents/my_books.py, my_rules.py): Supertrend, the three rule families, 4h / 1D candles on the
New York clock, the gates (chop on; Supertrend and hours as switches), exits, the dynamic stop, Jev-driven partial profit,
the chop gate on his EMA21 + RSI 55 book, and the intraday-momentum book - driven through the same bus / store / paper
broker as the real books."""
import asyncio
import copy

import numpy as np
import pandas as pd
import pytest

from fxagents import my_rules as M
from fxagents.agents.core import Ctx
from fxagents.agents.my_books import BOOKS, MOM, SPECS, MyBookTrader, MyIntradayMomTrader
from fxagents.broker import PaperBroker
from fxagents.bus import Bus
from fxagents.config import load_config
from fxagents.data import BarStore
from fxagents.models import Bar, Position
from fxagents.state import LiveState

CFG = load_config("config.yaml")
TZ = CFG["timezone"]
OHLC = ["open", "high", "low", "close"]


def h1_series(n=24 * 80, seed=3, start="2026-01-05 18:00", trend=True):
    idx = pd.date_range(start, periods=n, freq="1h", tz=TZ)
    idx = idx[~((idx.dayofweek == 5) | ((idx.dayofweek == 4) & (idx.hour >= 17)) | ((idx.dayofweek == 6) & (idx.hour < 18))
                | (idx.hour == 17))]
    rng = np.random.default_rng(seed)
    drift = np.repeat(rng.normal(0, 0.0015, len(idx) // 60 + 1), 60)[:len(idx)]
    c = 4000 * np.exp(np.cumsum(rng.normal(drift, 0.004)))
    o = np.r_[c[0], c[:-1]]
    df = pd.DataFrame({"open": o, "high": np.maximum(o, c) * 1.001, "low": np.minimum(o, c) * 0.999, "close": c}, index=idx)
    if trend:                                                  # a long climb then a long fall: both directions get exercised
        k = len(df)
        df = df.mul(np.exp(np.r_[np.linspace(0, 0.25, k // 2), np.linspace(0.25, -0.05, k - k // 2)]), axis=0)
    return df


def m15_from_h1(h1, seed=1):
    """Four 15-minute candles per hour inside each hourly candle (open/close consistent with the hour)."""
    rng = np.random.default_rng(seed)
    rows, idx = [], []
    for t, r in h1.iterrows():
        path = np.linspace(r.open, r.close, 5) + np.r_[0, rng.normal(0, (r.high - r.low) / 8, 3), 0]
        for k in range(4):
            o, c = path[k], path[k + 1]
            rows.append((o, min(max(o, c) * 1.0004, r.high), max(min(o, c) * 0.9996, r.low), c))
            idx.append(t + pd.Timedelta(minutes=15 * k))
    return pd.DataFrame(rows, columns=OHLC, index=pd.DatetimeIndex(idx))


# ───────────────────────── configuration ─────────────────────────
RETIRED = {"my_rsi_15m"}                                            # defined in the code, switched off in config (apply_my_hooks.DROP)


def test_config_registers_all_books():
    assert set(BOOKS) - RETIRED <= set(CFG["shadow"]["modes"])
    assert not (RETIRED & set(CFG["shadow"]["modes"]))
    for b in set(SPECS) - RETIRED:
        c = CFG["shadow"][b]
        assert c["symbols"] == (["XAUUSD", "NDQ"] if b.endswith("_15m") else ["XAUUSD", "NDQ", "US30"]), b
        assert (c["use_chop"], c["use_supertrend"], c["use_hours"], c["use_partials"]) == (True, False, False, True)
    assert CFG["shadow"][MOM]["symbols"] == ["NDQ", "US30"]
    assert "daily_rsi2_adx2" in CFG["shadow"]["modes"]                  # his book stays, outside the RSI · EMA group
    assert CFG["shadow"]["ema21_rsi55"]["chop_filter"] is True
    for b in set(SPECS) - RETIRED:                                     # the choppy-market cutoff installed in every book
        assert CFG["shadow"][b]["chop_max"] == 58.5, b
    assert CFG["shadow"]["ema21_rsi55"]["chop_max"] == 58.5


# ───────────────────────── Supertrend ─────────────────────────
def ref_supertrend(h, l, c, period=10, mult=3.0):
    """Independent, plain-python implementation of the textbook definition, to check the production one against."""
    n = len(c)
    tr = [h[0] - l[0]] + [max(h[i] - l[i], abs(h[i] - c[i - 1]), abs(l[i] - c[i - 1])) for i in range(1, n)]
    atr = [None] * n
    atr[period - 1] = sum(tr[:period]) / period
    for i in range(period, n):
        atr[i] = (atr[i - 1] * (period - 1) + tr[i]) / period
    up_b, lo_b, direction = {}, {}, {}
    for i in range(period - 1, n):
        mid = (h[i] + l[i]) / 2
        bu, bl = mid + mult * atr[i], mid - mult * atr[i]
        if i == period - 1:
            up_b[i], lo_b[i], direction[i] = bu, bl, (1 if c[i] >= mid else -1)
            continue
        up_b[i] = bu if (bu < up_b[i - 1] or c[i - 1] > up_b[i - 1]) else up_b[i - 1]
        lo_b[i] = bl if (bl > lo_b[i - 1] or c[i - 1] < lo_b[i - 1]) else lo_b[i - 1]
        if direction[i - 1] == 1:
            direction[i] = -1 if c[i] < lo_b[i] else 1
        else:
            direction[i] = 1 if c[i] > up_b[i] else -1
    return np.array([direction.get(i, 0) for i in range(n)])


@pytest.mark.parametrize("seed", [1, 2, 3])
def test_supertrend_matches_reference(seed):
    d = h1_series(n=900, seed=seed)
    h, l, c = d.high.to_numpy(), d.low.to_numpy(), d.close.to_numpy()
    got = M.supertrend(h, l, c)
    assert (got == ref_supertrend(h, l, c)).all()
    assert (got[:9] == 0).all() and set(np.unique(got[9:])) <= {-1, 1}
    assert (got[9:] == 1).any() and (got[9:] == -1).any()


def test_supertrend_follows_a_clear_trend_and_flips_on_a_break():
    c = np.r_[np.linspace(100, 140, 40), np.linspace(140, 80, 40)]     # a steady rise, then a steady fall
    h, l = c + 0.5, c - 0.5
    d = M.supertrend(h, l, c)
    assert (d[15:40] == 1).all()                                       # up while rising
    assert d[-1] == -1 and (d[60:] == -1).all()                        # down after the fall breaks the line
    flip = int(np.argmax((d[:-1] == 1) & (d[1:] == -1))) + 1
    assert 40 < flip < 60                                              # it flips only after the reversal, not at the top


def test_supertrend_never_looks_ahead():
    d = h1_series(n=700, seed=4)
    h, l, c = d.high.to_numpy(), d.low.to_numpy(), d.close.to_numpy()
    full = M.supertrend(h, l, c)
    for cut in (120, 333, 500):
        assert (M.supertrend(h[:cut], l[:cut], c[:cut]) == full[:cut]).all()


# ───────────────────────── candles on the New York clock ─────────────────────────
def test_4h_and_daily_candles_start_when_oanda_starts_them_across_a_dst_change():
    h1 = h1_series(n=24 * 12, start="2026-03-02 18:00", trend=False)     # covers Sunday 8 March 2026 (clocks go forward)
    d4, e4 = M.build_tf(h1, "4h")
    dd, ed = M.build_tf(h1, "1D")
    assert set(d4.index.tz_convert(TZ).hour) <= {1, 5, 9, 13, 17, 21}
    assert set(dd.index.tz_convert(TZ).hour) == {17}
    assert ((e4 - d4.index.tz_convert(TZ).tz_localize(None)) == pd.Timedelta("4h")).all()      # wall-clock length, DST or not
    assert ((ed - dd.index.tz_convert(TZ).tz_localize(None)) == pd.Timedelta("24h")).all()
    first = dd.index[2].tz_convert(TZ).tz_localize(None)               # one daily candle, recomputed by hand from its hours
    loc = h1.index.tz_convert(TZ).tz_localize(None)
    sel = h1[(loc >= first) & (loc < first + pd.Timedelta("24h"))]
    row = dd.iloc[2]
    assert row.open == sel.open.iloc[0] and row.close == sel.close.iloc[-1]
    assert row.high == sel.high.max() and row.low == sel.low.min()


def test_higher_timeframe_rsi_uses_only_closed_candles():
    h1 = h1_series(n=24 * 40, trend=False)
    for rule in ("1h", "4h", "1D"):
        w = pd.DatetimeIndex([pd.Timestamp("2026-02-10 16:00", tz=TZ), pd.Timestamp("2026-02-10 17:00", tz=TZ),
                              pd.Timestamp("2026-02-10 21:00", tz=TZ)])
        full = M.htf_rsi_vec(h1, rule, w)
        for k, t in enumerate(w):                                     # data after the decision time must not matter
            cut = M.htf_rsi_vec(h1[h1.index + pd.Timedelta("1h") <= t], rule, w[k:k + 1])
            assert np.isclose(full[k], cut[0], equal_nan=True)


# ───────────────────────── rules: exact and causal ─────────────────────────
CASES = [("ema_rsi", "15min"), ("ema_rsi", "1h"), ("ema_rsi", "4h"), ("ema_rsi", "1D"), ("ema_cross", "15min"),
         ("ema_cross", "1h"), ("ema_cross", "4h"), ("ema_cross", "1D"), ("rsi_mtf", "15min"), ("rsi_mtf", "1h"), ("rsi_mtf", "4h")]


def frames(tf, n_hours=24 * 150, seed=3):
    h1 = h1_series(n=n_hours, seed=seed)
    if tf == "15min":
        return m15_from_h1(h1, seed), h1
    if tf == "1h":
        return h1, h1
    return M.build_tf(h1, tf)[0], h1


@pytest.mark.parametrize("rule,tf", CASES)
def test_rules_match_their_definition_and_never_look_ahead(rule, tf):
    df, h1 = frames(tf)
    b = M.build(df, h1, rule, tf)
    c, e21, e9, r = b.c.to_numpy(), b.ema21.to_numpy(), b.ema9.to_numpy(), b.rsi.to_numpy()
    pc, pr = np.r_[np.nan, c[:-1]], np.r_[np.nan, r[:-1]]
    pe21, pe9 = np.r_[np.nan, e21[:-1]], np.r_[np.nan, e9[:-1]]
    with np.errstate(invalid="ignore"):
        if rule == "ema_rsi":
            up, dn = (c > e21) & (pr <= 55) & (r > 55) & (c > pc), (c < e21) & (pr >= 44) & (r < 44) & (c < pc)
        elif rule == "ema_cross":
            up, dn = (pe9 <= pe21) & (e9 > e21) & (c > e21), (pe9 >= pe21) & (e9 < e21) & (c < e21)
        else:
            hs = [b[f"htf{k + 1}"].to_numpy() for k in range(len(M.HTF[tf]))]
            up = np.all([x > 60 for x in hs], axis=0) & (pr <= 60) & (r > 60)
            dn = np.all([x < 40 for x in hs], axis=0) & (pr >= 40) & (r < 40)
    want = np.where(up, 1, np.where(dn, -1, 0))
    want[np.arange(len(b)) < M.WARMUP[tf]] = 0
    assert (b.raw.to_numpy() == want).all()
    assert (b.raw != 0).sum() > 0, "the test series must produce signals"
    full = b
    for cut in (len(df) // 3, len(df) // 2, 2 * len(df) // 3):
        part = M.build(df.iloc[:cut], h1[h1.index + pd.Timedelta("1h") <= df.index[cut - 1] + pd.Timedelta(tf if tf != "1D" else "24h")], rule, tf)
        for col in ("raw", "st"):
            assert (part[col].to_numpy() == full[col].iloc[:cut].to_numpy()).all(), (rule, tf, col, cut)
        assert np.allclose(part.chop.to_numpy(), full.chop.iloc[:cut].to_numpy(), equal_nan=True)


def test_rsi_60_40_asks_the_right_higher_timeframes():
    assert M.HTF["15min"] == ("1h", "4h") and M.HTF["1h"] == ("4h", "1D") and M.HTF["4h"] == ("1D",)


# ───────────────────────── trader plumbing ─────────────────────────
class J:
    def __init__(self): self.signals = []
    def add_signal(self, s): self.signals.append(s)


class FakeJev:
    """Stands in for Jev: a fixed continuation probability and source; records every question."""
    def __init__(self, prob=0.3, source="jev"):
        self.prob, self.source, self.calls = prob, source, []

    async def rate_signal(self, info):
        return {"quality": 0.6, "confidence": 0.5, "source": "jev"}

    async def continuation(self, info):
        self.calls.append(info)
        return {"prob": self.prob, "source": self.source}


GATES_OFF = {"trend_gate": False, "fresh": 0, "rsi_momentum": False, "skip_big": 0.0, "stop_cap": False}   # the round-4 gates start OFF in every test


def prep_cfg(book, symbols, over=None):
    cfg = copy.deepcopy(CFG)
    cfg["shadow"][book] = {**(cfg["shadow"].get(book) or {}), **GATES_OFF, "symbols": symbols, "risk_pct": 0.005, **(over or {})}
    cfg["instruments"]["XAUUSD"].update(multiplier=1, tick_size=0.01, qty_step=0.01, min_units=0.01, max_units=200,
                                        commission_per_unit=0)
    cfg["instruments"]["NDQ"].update(multiplier=1, tick_size=0.1, qty_step=0.01, min_units=0.01, max_units=200,
                                     commission_per_unit=0)
    return cfg


def make_trader(book, symbols=("XAUUSD",), over=None, jev=None, journal=None):
    cfg = prep_cfg(book, list(symbols), over)
    st = LiveState(); st.equity = st.day_start_equity = st.equity_peak = 2000.0
    bus = Bus()
    tr_cls = MyIntradayMomTrader if book == MOM else MyBookTrader
    tr = tr_cls(Ctx(cfg, bus, st, BarStore(TZ, max_days=5), PaperBroker(cfg, st, bus), J() if journal is None else journal, jev, None), book)
    tr.start()
    return tr


def test_no_hours_rule_by_default_only_the_market_closure_and_the_15m_friday_rule():
    t = lambda x: pd.Timestamp(x, tz=TZ)                                  # noqa: E731  (2026-10-12 is a Monday)
    for book in ("my_ema_rsi_15m", "my_rsi_1h", "my_ema_cross_4h", "my_ema_rsi_1d"):
        tr = make_trader(book)
        for when in ("2026-10-13 04:00", "2026-10-13 11:00", "2026-10-13 14:00", "2026-10-13 18:30", "2026-10-14 23:00"):
            assert tr.entry_allowed("XAUUSD", t(when)) and tr.entry_allowed("NDQ", t(when)), (book, when)
        assert not tr.entry_allowed("XAUUSD", t("2026-10-17 12:00")) and not tr.entry_allowed("XAUUSD", t("2026-10-18 10:00"))
    quarter, hourly = make_trader("my_ema_rsi_15m"), make_trader("my_ema_rsi_1h")
    assert quarter.entry_allowed("NDQ", t("2026-10-16 15:45")) and not quarter.entry_allowed("NDQ", t("2026-10-16 16:00"))
    assert hourly.entry_allowed("NDQ", t("2026-10-16 16:00")) and not hourly.entry_allowed("NDQ", t("2026-10-16 17:00"))


def test_hours_rule_can_be_switched_back_on():
    t = lambda x: pd.Timestamp(x, tz=TZ)                                  # noqa: E731
    hourly, daily = make_trader("my_ema_rsi_1h", over={"use_hours": True}), make_trader("my_ema_rsi_1d", over={"use_hours": True})
    assert hourly.entry_allowed("XAUUSD", t("2026-10-13 21:00")) and not hourly.entry_allowed("XAUUSD", t("2026-10-13 11:00"))
    assert not hourly.entry_allowed("XAUUSD", t("2026-10-13 04:00"))                      # nothing 03:00-06:00
    assert hourly.entry_allowed("NDQ", t("2026-10-13 15:45")) and not hourly.entry_allowed("NDQ", t("2026-10-13 16:00"))
    assert not hourly.entry_allowed("US30", t("2026-10-13 18:00"))
    assert daily.entry_allowed("XAUUSD", t("2026-10-14 17:00"))                           # the daily books never have the hours rule


def frame_with(raw, st=1, chop=40.0, n=40, price=100.0):
    idx = pd.date_range("2026-10-13 00:00", periods=n, freq="1h", tz=TZ)
    b = pd.DataFrame({"o": price, "h": price + 1, "l": price - 1, "c": price, "ema21": price, "ema9": price, "rsi": 50.0,
                      "atr": 1.0, "chop": chop, "st": st, "raw": 0, "stop_long": price - 2, "stop_short": price + 2}, index=idx)
    b.loc[b.index[-1], "raw"] = raw
    return b


def fire(tr, b, when, sym="XAUUSD", htf=0):
    bnd = pd.Timestamp(when, tz=TZ)
    tr.state.now = bnd
    tr.state.last_prices[sym] = 100.0
    asyncio.run(tr.maybe_enter(sym, b, bnd, Bar(sym, bnd - pd.Timedelta("1min"), 100.0, 100.1, 99.9, 100.0, 1.0), htf))
    return tr.ctx.journal.signals[-1] if tr.ctx.journal.signals else None


def test_default_gate_is_chop_only_and_the_other_gates_are_switches():
    night, day = "2026-10-13 22:00", "2026-10-13 14:00"
    tr = make_trader("my_ema_rsi_1h")                                      # defaults: chop on, Supertrend off, hours off
    s = fire(tr, frame_with(1, st=-1), day)                                # Supertrend down, 2 PM: still a buy, nothing gates it
    assert s["action"] == "taken" and next(iter(tr.state.positions.values())).side == 1
    s = fire(make_trader("my_ema_rsi_1h"), frame_with(1, st=1, chop=70.0), night)
    assert s["action"] == "rejected" and "choppy" in s["why"]
    s = fire(make_trader("my_ema_rsi_1h", over={"use_chop": False}), frame_with(1, st=1, chop=70.0), night)
    assert s["action"] == "taken"                                          # chop can be switched off too
    st_on = make_trader("my_ema_rsi_1h", over={"use_supertrend": True})
    assert "against Supertrend" in fire(st_on, frame_with(1, st=-1), night)["why"]
    assert "against Supertrend" in fire(st_on, frame_with(-1, st=1), night)["why"]
    assert fire(st_on, frame_with(1, st=1), night)["action"] == "taken"
    hrs = make_trader("my_ema_rsi_1h", over={"use_hours": True})
    assert "outside entry hours" in fire(hrs, frame_with(1, st=1), day)["why"]
    assert fire(hrs, frame_with(1, st=1), night)["action"] == "taken"
    sell = make_trader("my_rsi_1h")
    s = fire(sell, frame_with(-1, st=1), night)                            # a sell against an up Supertrend is fine by default
    assert s["action"] == "taken" and next(iter(sell.state.positions.values())).side == -1
    p = next(iter(sell.state.positions.values()))
    assert p.stop > 100 and p.meta["hold_overnight"]


def test_the_chop_cutoff_is_a_per_book_setting():
    night = "2026-10-13 22:00"
    from fxagents.agents.my_books import DEFAULTS
    assert DEFAULTS["chop_max"] == 61.8                                                                      # code default when a book has no setting
    assert fire(make_trader("my_ema_rsi_1h", over={"chop_max": 61.8}), frame_with(1, chop=60.0), night)["action"] == "taken"   # 60 passes at 61.8
    assert fire(make_trader("my_ema_rsi_1h"), frame_with(1, chop=60.0), night)["action"] == "rejected"          # the installed config says 58.5
    tr = make_trader("my_ema_rsi_1h", over={"chop_max": 58.5})
    s = fire(tr, frame_with(1, chop=60.0), night)
    assert s["action"] == "rejected" and "choppy market" in s["why"] and "58.5" in s["why"]                      # 58.5: 60 is blocked
    assert fire(make_trader("my_ema_rsi_1h", over={"chop_max": 58.5}), frame_with(1, chop=58.4), night)["action"] == "taken"
    assert "choppy" in fire(make_trader("my_ema_rsi_1h", over={"chop_max": 58.5}), frame_with(1, chop=58.5), night)["why"]   # the cutoff itself blocks
    assert fire(make_trader("my_ema_rsi_1h", over={"chop_max": 58.5, "use_chop": False}), frame_with(1, chop=70.0), night)["action"] == "taken"


def test_a_stop_beyond_the_brokers_10_percent_guard_is_logged_not_raised():
    tr = make_trader("my_ema_cross_1d")
    b = frame_with(1, st=1)
    b["atr"], b["l"] = 10.0, 85.0                                       # swing stop ~17% below the price, but within 3 ATR
    s = fire(tr, b, "2026-10-14 17:00")
    assert s["action"] == "rejected" and "stop distance" in s["why"] and not tr.state.positions


def test_daily_books_obey_the_chop_gate_and_the_optional_supertrend():
    assert fire(make_trader("my_ema_cross_1d"), frame_with(1, st=1), "2026-10-14 17:00")["action"] == "taken"
    assert "choppy" in fire(make_trader("my_ema_cross_1d"), frame_with(1, st=1, chop=65.0), "2026-10-14 17:00")["why"]
    on = make_trader("my_ema_cross_1d", over={"use_supertrend": True, "use_hours": True})
    assert "against Supertrend" in fire(on, frame_with(1, st=-1), "2026-10-14 17:00")["why"]
    assert fire(on, frame_with(1, st=1), "2026-10-14 17:00")["action"] == "taken"       # hours switch never gates a daily book


def test_session_flatten_spares_hold_overnight_positions():
    tr = make_trader("my_ema_rsi_1h")
    from fxagents.agents.trading import PositionManagerAgent
    st, broker, bus = tr.state, tr.ctx.broker, tr.bus
    pm = PositionManagerAgent(Ctx(tr.cfg, bus, st, BarStore(TZ, max_days=2), broker, J(), None, None)); pm.start()
    opened = pd.Timestamp("2026-10-07 21:00", tz=TZ)
    mine = Position("XAUUSD", 1, "my_ema_rsi_1h", 4100.0, 4100.0, 20.0, 99.0, opened)
    mine.meta.update(external_mgmt=True, no_pyramid=True, max_hold=10 ** 6, hold_overnight=True)
    his = Position("XAUUSD", 1, "ema21_rsi55", 4100.0, 4100.0, 20.0, 99.0, opened)
    his.meta.update(external_mgmt=True, no_pyramid=True, max_hold=10 ** 6)

    async def go():
        for p in (mine, his):
            st.now = opened
            await broker.open(p, 1.0, 4120.0)
            st.positions[p.id] = p
        st.now = pd.Timestamp("2026-10-08 15:55", tz=TZ)
        bar = Bar("XAUUSD", st.now - pd.Timedelta("1min"), 4125.0, 4126.0, 4124.0, 4125.0, 1.0)
        st.last_prices["XAUUSD"] = 4125.0
        await pm.on_bar(bar)
    asyncio.run(go())
    assert his.status == "closed" and his.exit_reason == "session_flat"
    assert mine.status == "open"


def test_only_the_15m_books_are_flat_before_the_weekend():
    friday = pd.Timestamp("2026-10-16 16:00", tz=TZ)
    for book, expect in (("my_ema_rsi_15m", "weekend_close"), ("my_ema_rsi_1h", None), ("my_ema_cross_4h", None)):
        tr = make_trader(book)
        pos = Position("XAUUSD", 1, book, 4100.0, 4100.0, 20.0, 99.0, friday - pd.Timedelta("20h"))
        pos.meta.update(external_mgmt=True, hold_overnight=True)
        tr.state.positions[pos.id] = pos
        asyncio.run(tr.manage("XAUUSD", frame_with(0, price=4125.0), friday))
        assert pos.meta.get("pending_close") == expect, book
    thu = make_trader("my_ema_rsi_15m")
    pos = Position("XAUUSD", 1, "my_ema_rsi_15m", 4100.0, 4100.0, 20.0, 99.0, friday - pd.Timedelta("44h"))
    pos.meta.update(external_mgmt=True, hold_overnight=True)
    thu.state.positions[pos.id] = pos
    asyncio.run(thu.manage("XAUUSD", frame_with(0, price=4125.0), friday - pd.Timedelta("24h")))
    assert not pos.meta.get("pending_close")


# ───────────────────────── Jev decides partial profit ─────────────────────────
def open_trade(tr, when="2026-10-13 22:00"):
    """Open a long through the real entry path; returns the position (entry ~100, stop ~ 97.5)."""
    assert fire(tr, frame_with(1, st=1), when)["action"] == "taken"
    return next(iter(tr.state.positions.values()))


def at_r(tr, pos, r, when="2026-10-14 01:00"):
    """Run one candle close with the price at +r R and return nothing; the position manager stand-in is not needed."""
    price = pos.entry + r * pos.risk_per_unit
    b = frame_with(0, price=price)
    b["ema21"] = price - 1.0                                          # on the right side of EMA21: no EMA exit
    b["rsi"] = 60.0
    tr.state.now = pd.Timestamp(when, tz=TZ)
    tr.state.last_prices["XAUUSD"] = price
    pos.mfe_r = max(pos.mfe_r, r)
    asyncio.run(tr.manage("XAUUSD", b, pd.Timestamp(when, tz=TZ)))
    return price


def test_jev_low_continuation_books_half_and_leaves_a_runner():
    jev = FakeJev(prob=0.30)
    tr = make_trader("my_ema_rsi_1h", jev=jev)
    pos = open_trade(tr)
    q0 = pos.open_qty
    assert at_r(tr, pos, 0.2) is not None and not jev.calls            # below +0.5R: Jev is not even asked
    at_r(tr, pos, 1.2)
    assert len(jev.calls) == 1 and jev.calls[0]["r_now"] >= 1.0 and jev.calls[0]["side"] == "LONG"
    assert pos.partial_done and pos.meta["agent_partials"] == 1
    assert 0.45 * q0 <= pos.closed_qty <= 0.55 * q0 and pos.open_qty > 0 and pos.status == "open"
    ev = [e for e in pos.events if e["kind"] == "partial"]
    assert len(ev) == 1 and ev[0]["prob"] == 0.3 and "Jev" in ev[0]["why"]
    at_r(tr, pos, 1.4, "2026-10-14 02:00")                              # a second low answer: second (smaller) partial
    assert pos.meta["agent_partials"] == 2 and pos.open_qty > 0
    q_after_two = pos.open_qty
    at_r(tr, pos, 1.6, "2026-10-14 03:00")                              # never more than two
    assert pos.meta["agent_partials"] == 2 and pos.open_qty == q_after_two and len(jev.calls) == 2


def test_jev_high_continuation_holds_and_a_non_jev_answer_never_acts():
    for prob, source in ((0.70, "jev"), (0.10, "heuristic")):
        jev = FakeJev(prob=prob, source=source)
        tr = make_trader("my_ema_rsi_1h", jev=jev)
        pos = open_trade(tr)
        q0 = pos.open_qty
        at_r(tr, pos, 1.2)
        assert len(jev.calls) == 1 and pos.open_qty == q0 and not pos.partial_done
        holds = [e for e in pos.events if e["kind"] == "agent_check"]
        assert holds and holds[-1]["action"] == "hold"
        assert ("no live Jev" in holds[-1]["why"]) == (source != "jev")


def test_partials_can_be_switched_off_and_never_close_the_whole_position():
    jev = FakeJev(prob=0.1)
    tr = make_trader("my_ema_rsi_1h", jev=jev, over={"use_partials": False})
    pos = open_trade(tr)
    at_r(tr, pos, 1.5)
    assert not jev.calls and not pos.partial_done
    tr2 = make_trader("my_ema_rsi_1h", jev=FakeJev(0.1))               # too small to split: one minimum unit cannot be halved
    pos2 = open_trade(tr2)
    tr2.state.equity = 0.01
    pos2.legs[0].qty = 0.01
    at_r(tr2, pos2, 1.5)
    assert pos2.open_qty == 0.01 and not pos2.partial_done


def test_jev_failure_cannot_break_the_book():
    class Boom(FakeJev):
        async def continuation(self, info):
            raise RuntimeError("network down")
    tr = make_trader("my_ema_rsi_1h", jev=Boom())
    pos = open_trade(tr)
    at_r(tr, pos, 1.2)
    assert pos.status == "open" and not pos.partial_done


# ───────────────────────── a restart must not drop open trades ─────────────────────────
def test_open_trades_survive_a_restart_with_their_stop_and_partials(tmp_path):
    from fxagents.journal import Journal
    jr = Journal(str(tmp_path / "j.sqlite"))
    tr = make_trader("my_ema_rsi_1h", jev=FakeJev(prob=0.2))
    pos = open_trade(tr)
    mult = float(tr.cfg["instruments"]["XAUUSD"]["multiplier"])
    jr.upsert_trade(pos, mult)                                          # what the journal agent does when the trade opens
    at_r(tr, pos, 1.3)                                                  # a Jev partial and a stop move happen ...
    assert pos.partial_done and pos.stop > pos.initial_stop
    jr.upsert_trade(pos, mult)                                          # ... and are written to the journal as they happen
    other = Position("XAUUSD", 1, "ema21_rsi55", 4100.0, 4100.0, 20.0, 99.0, pd.Timestamp("2026-10-13 22:00", tz=TZ))
    tr.ctx.broker.open_positions.clear()
    asyncio.run(tr.ctx.broker.open(other, 1.0, 4120.0))
    jr.upsert_trade(other, mult)                                        # another book's trade in the same journal
    # ── restart: a fresh state and broker, the same journal ──
    tr2 = make_trader("my_ema_rsi_1h", jev=FakeJev(prob=0.9), journal=jr)
    back = [p for p in tr2.state.positions.values()]
    assert len(back) == 1 and back[0].id == pos.id and back[0].strategy == "my_ema_rsi_1h"      # only this book's trade
    q = back[0]
    assert q.side == pos.side and q.stop == pos.stop and q.initial_stop == pos.initial_stop     # the trailed stop, not the first one
    assert q.partial_done and q.meta["agent_partials"] == 1 and abs(q.closed_qty - pos.closed_qty) < 1e-6
    assert abs(q.open_qty - pos.open_qty) < 1e-6 and q.entry == pos.entry and q.meta["hold_overnight"]
    assert any(e["kind"] == "readopted" for e in q.events) and tr2.ctx.broker.open_positions[q.id] is q
    assert tr2.adopt() == 0                                              # never adopted twice
    # the restored trade is managed again: price falls through its stop and the broker closes what is left
    tr2.state.now = pd.Timestamp("2026-10-14 03:00", tz=TZ)
    asyncio.run(tr2.ctx.broker.on_bar(Bar("XAUUSD", tr2.state.now, q.entry, q.entry, q.stop - 1.0, q.stop - 1.0, 1.0)))
    assert q.open_qty == 0
    # a book that does not trade that market leaves the trade alone
    assert make_trader("my_ema_rsi_1h", symbols=("NDQ",), journal=jr).state.positions == {}


def test_a_stale_15m_row_from_before_the_last_weekend_is_not_revived(tmp_path):
    from fxagents.journal import Journal
    from fxagents.models import Leg
    jr = Journal(str(tmp_path / "j.sqlite"))
    ts = lambda s_: pd.Timestamp(s_, tz=TZ)                              # noqa: E731  (2026-10-22 is a Thursday, 10-24 a Saturday)
    for book, opened in (("my_ema_rsi_15m", "2026-10-22 15:30"), ("my_ema_cross_1h", "2026-10-22 11:00")):
        p = Position("US30", 1, book, 52000.0, 52000.0, 100.0, 99.0, ts(opened))
        p.add_leg(Leg(1.0, 52100.0, ts(opened), "initial"))
        jr.upsert_trade(p, 1.0)

    def start(book, now):
        cfg = prep_cfg(book, ["US30"])
        st = LiveState(); st.equity = st.day_start_equity = st.equity_peak = 2000.0; st.now = ts(now)
        bus = Bus()
        tr = MyBookTrader(Ctx(cfg, bus, st, BarStore(TZ, max_days=5), PaperBroker(cfg, st, bus), jr, None, None), book)
        tr.start()
        return tr
    assert start("my_ema_rsi_15m", "2026-10-24 12:00").state.positions == {}      # opened Thursday, the weekend flat has passed: leftover, ignored
    assert len(start("my_ema_cross_1h", "2026-10-24 12:00").state.positions) == 1  # a 1h trade legitimately spans the weekend: adopted
    fri = start("my_ema_rsi_15m", "2026-10-23 12:00")                              # on Friday noon
    assert fri.stale(ts("2026-10-23 10:00")) is False                              # this morning's trade is live
    assert fri.stale(ts("2026-10-22 15:30")) is False                              # Thursday's can still be live: this week's flat has not happened yet
    assert fri.stale(ts("2026-10-15 15:30")) is True                               # one from before last Friday 16:00 cannot be


# ───────────────────────── round-4 gates: fresh cross, RSI direction, trend, oversized candle, stop cap ─────────────────────────
NIGHT = "2026-10-13 22:00"


def cross_frame(side, run, n=40):
    """The close has been on the trade side of the EMA21 for exactly `run` candles, after being on the other side before."""
    b = frame_with(side, n=n)
    b["ema21"] = 100.0
    c = np.full(n, 100.0 - side)
    c[n - run:] = 100.0 + side
    b["c"] = c
    return b


def test_the_new_gates_are_all_off_by_default():
    from fxagents.agents.my_books import DEFAULTS
    assert (DEFAULTS["trend_gate"], DEFAULTS["fresh"], DEFAULTS["rsi_momentum"], DEFAULTS["skip_big"], DEFAULTS["stop_cap"]) == (False, 0, False, 0.0, False)


def test_fresh_cross_gate_allows_a_cross_within_n_candles_only():
    for side in (1, -1):
        for run, ok in ((1, True), (2, True), (3, False), (40, False)):
            s = fire(make_trader("my_ema_rsi_1h", over={"fresh": 2}), cross_frame(side, run), NIGHT)
            assert (s["action"] == "taken") is ok, (side, run, s)
            if not ok:
                assert "not a fresh cross" in s["why"]
    s = fire(make_trader("my_ema_rsi_1h", over={"fresh": 0}), cross_frame(1, 5), NIGHT)           # off: any run length is fine
    assert s["action"] == "taken"


def test_rsi_direction_gate():
    n = 40
    up, dn = np.linspace(40, 60, n), np.linspace(60, 40, n)
    for side, good, bad in ((1, up, dn), (-1, dn, up)):
        b = frame_with(side); b["rsi"] = good
        assert fire(make_trader("my_ema_rsi_1h", over={"rsi_momentum": True}), b, NIGHT)["action"] == "taken"
        b = frame_with(side); b["rsi"] = bad
        s = fire(make_trader("my_ema_rsi_1h", over={"rsi_momentum": True}), b, NIGHT)
        assert s["action"] == "rejected" and "RSI not" in s["why"]
        assert fire(make_trader("my_ema_rsi_1h"), b, NIGHT)["action"] == "taken"                  # switch off: the old behaviour
    b = frame_with(-1); r = np.full(n, 50.0); r[-1] = 55.0; b["rsi"] = r                          # a sell while the RSI just made a 10-candle high
    assert fire(make_trader("my_ema_rsi_1h", over={"rsi_momentum": True}), b, NIGHT)["action"] == "rejected"


def test_oversized_signal_candle_is_skipped():
    b = frame_with(1); b.loc[b.index[-1], ["h", "l"]] = [105.0, 99.0]                              # range 6 ATR (the low stays at the swing low)
    s = fire(make_trader("my_ema_rsi_1h", over={"skip_big": 2.5}), b, NIGHT)
    assert s["action"] == "rejected" and "oversized" in s["why"]
    assert fire(make_trader("my_ema_rsi_1h", over={"skip_big": 2.5}), frame_with(1), NIGHT)["action"] == "taken"
    assert fire(make_trader("my_ema_rsi_1h"), b, NIGHT)["action"] == "taken"                       # off by default


def test_trend_gate_blocks_trades_against_the_higher_timeframe_only():
    for side, htf, ok in ((1, 1, True), (1, 0, True), (1, -1, False), (-1, -1, True), (-1, 0, True), (-1, 1, False)):
        s = fire(make_trader("my_ema_rsi_1h", over={"trend_gate": True}), frame_with(side), NIGHT, htf=htf)
        assert (s["action"] == "taken") is ok, (side, htf, s)
        if not ok:
            assert "against the 4h trend" in s["why"]
    assert fire(make_trader("my_ema_rsi_1h"), frame_with(1), NIGHT, htf=-1)["action"] == "taken"   # gate off: the state is ignored
    s = fire(make_trader("my_ema_rsi_15m", over={"trend_gate": True}), frame_with(1), NIGHT, htf=-1)
    assert "against the 1h trend" in s["why"]                                                       # a 15m book looks at the 1h


def test_stop_cap_trades_with_a_capped_stop_instead_of_skipping():
    b = frame_with(1); b.loc[b.index[-3], "l"] = 90.0                                               # the swing low is ~10 ATR away
    s = fire(make_trader("my_ema_rsi_1h"), b, NIGHT)
    assert s["action"] == "rejected" and "stop too wide" in s["why"]                                # today's behaviour
    tr = make_trader("my_ema_rsi_1h", over={"stop_cap": True})
    s = fire(tr, b, NIGHT)
    assert s["action"] == "taken"
    pos = list(tr.state.positions.values())[0]
    from fxagents.agents.trading import half_spread
    e0 = 100.0 + half_spread(tr.cfg, "XAUUSD")                                                      # the entry price the book sized the stop from
    assert abs((e0 - pos.stop) - 3.0) < 0.02                                                        # exactly 3 ATR (ATR = 1), to the tick


def _h1(n, drift):
    idx = pd.date_range("2026-08-01 00:00", periods=n, freq="1h", tz=TZ)
    c = 100 + np.cumsum(np.full(n, drift)) + np.sin(np.arange(n) / 5.0)
    return pd.DataFrame({"open": c - 0.1, "high": c + 0.5, "low": c - 0.5, "close": c, "volume": 1.0}, index=idx)


def test_higher_timeframe_state_follows_the_trend_and_uses_completed_candles():
    rising, falling = _h1(24 * 60, 0.15), _h1(24 * 60, -0.15)
    wall = rising.index[-1].tz_localize(None) + pd.Timedelta("1h")
    for book, tf in (("my_ema_rsi_15m", "1h"), ("my_ema_rsi_1h", "4h"), ("my_ema_rsi_4h", "1D")):
        tr = make_trader(book)
        assert tr.HTF[tr.tf] == tf
        assert tr.htf_state(rising, wall) == 1, book
        assert tr.htf_state(falling, wall) == -1, book
        assert tr.htf_state(rising.iloc[:20], wall) == 0, book                                      # not enough history: neutral
    assert make_trader("my_ema_rsi_1d").htf_state(rising, wall) == 0                                # nothing above the daily


def test_round_4_settings_per_timeframe_in_the_config():
    sh = CFG["shadow"]
    for b in ("my_ema_rsi_15m", "my_ema_cross_15m", "my_ema_rsi_1h", "my_rsi_1h", "my_ema_cross_1h"):
        c = sh[b]
        assert (c["trend_gate"], c["fresh"], c["rsi_momentum"]) == (True, 2, True), b
    for b in ("my_ema_rsi_4h", "my_rsi_4h", "my_ema_cross_4h"):
        c = sh[b]
        assert (c["trend_gate"], c["skip_big"], c["stop_cap"]) == (True, 2.5, True), b
        assert not c.get("fresh") and not c.get("rsi_momentum"), b
    for b in ("my_ema_rsi_1d", "my_ema_cross_1d"):
        assert not any(sh[b].get(k) for k in ("trend_gate", "fresh", "rsi_momentum", "skip_big", "stop_cap")), b
    for b in ("my_ema_rsi_15m", "my_ema_cross_15m"):
        assert sh[b]["symbols"] == ["XAUUSD", "NDQ"], b                                             # US30 loses on 15 minutes


# ───────────────────────── the chop gate on his EMA21 + RSI 55 book ─────────────────────────
def his_book(chop_filter, chop_max=None):
    from fxagents.agents.ema_rsi_trader import EmaRsiTrader
    cfg = prep_cfg("ema21_rsi55", ["XAUUSD"], {"chop_filter": chop_filter, **({"chop_max": chop_max} if chop_max is not None else {})})
    st = LiveState(); st.equity = st.day_start_equity = st.equity_peak = 100000.0
    bus = Bus()
    tr = EmaRsiTrader(Ctx(cfg, bus, st, BarStore(TZ, max_days=5), PaperBroker(cfg, st, bus), J(), None, None))
    tr.start()
    return tr


def his_frame(choppy, n=70):
    idx = pd.date_range("2026-10-13 00:00", periods=n, freq="15min", tz=TZ)
    c = np.full(n, 100.0)
    if choppy:
        c[:] = np.where(np.arange(n) % 2 == 0, 99.0, 101.0)             # up, down, up, down: lots of range travelled, no progress
    else:
        c = 100 + np.arange(n) * 1.0                                    # a straight climb
    ema = c.copy()
    ema[-1], ema[-2] = c[-1] - 0.5, c[-2] + 0.5                         # previous close <= EMA21, this close > EMA21
    b = pd.DataFrame({"c": c, "h": c + 0.5, "l": c - 0.5, "ema21": ema, "rsi": 60.0, "atr": 1.0}, index=idx)
    return b


def test_his_ema21_rsi55_book_skips_choppy_markets_only_when_the_switch_is_on():
    when = pd.Timestamp("2026-10-13 10:00", tz=TZ)

    def run(tr, b):
        tr.state.now = when
        tr.state.last_prices["XAUUSD"] = float(b.c.iloc[-1])
        asyncio.run(tr.maybe_enter("XAUUSD", b, when, Bar("XAUUSD", when - pd.Timedelta("1min"), 1.0, 1.0, 1.0, 1.0, 1.0)))
        return tr.ctx.journal.signals[-1]

    s = run(his_book(True), his_frame(choppy=True))
    assert s["action"] == "rejected" and "choppy market" in s["why"]
    assert run(his_book(False), his_frame(choppy=True))["action"] == "taken"          # switch off: exactly his original behaviour
    assert run(his_book(True), his_frame(choppy=False))["action"] == "taken"          # trending market: the gate lets it through


# ───────────────────────── full runs through the paper broker ─────────────────────────
def run_book(book, days=30, seed=5, warm_days=6, hist_days=120, sym="XAUUSD", series=None, sparse=False, over=None, jev=None):
    cfg = prep_cfg(book, [sym], over)
    h1 = series if series is not None else h1_series(n=24 * (days + warm_days + hist_days), seed=seed)
    split = h1.index[-24 * days]
    store = BarStore(TZ, max_days=days + warm_days + 5)
    store.load_h1(sym, h1[h1.index < split - pd.Timedelta(days=warm_days)])
    st = LiveState(); st.equity = st.day_start_equity = st.equity_peak = 2000.0
    bus = Bus()
    events = []
    bus.subscribe("position_updated", lambda ev: events.append(ev))
    broker = PaperBroker(cfg, st, bus)
    ctx = Ctx(cfg, bus, st, store, broker, J(), jev, None)
    tr = MyBookTrader(ctx, book); tr.start()
    rng = np.random.default_rng(seed)
    stops_seen = {}

    def path_of(r):
        p = np.linspace(r.open, r.close, 60) + rng.normal(0, (r.high - r.low) / 6, 60)
        return np.clip(p, r.low, r.high)

    def bars_of(t, r):
        """The hour as 1-minute bars; `sparse` = four bars (minutes 0, 20, 40, 59) that still make exactly this hourly candle."""
        if sparse:
            o, hi, lo, c = float(r.open), float(r.high), float(r.low), float(r.close)
            return [Bar(sym, t, o, o, o, o, 1.0), Bar(sym, t + pd.Timedelta(minutes=20), o, hi, o, hi, 1.0),
                    Bar(sym, t + pd.Timedelta(minutes=40), hi, hi, lo, lo, 1.0), Bar(sym, t + pd.Timedelta(minutes=59), lo, max(lo, c), lo, c, 1.0)]
        return [Bar(sym, t + pd.Timedelta(minutes=k), float(p), float(p) + 0.2, float(p) - 0.2, float(p), 1.0)
                for k, p in enumerate(path_of(r))]

    async def go():
        for t, r in h1[(h1.index >= split - pd.Timedelta(days=warm_days)) & (h1.index < split)].iterrows():
            for bar in bars_of(t, r):                                       # warm-up for the 15m frames
                store.append(bar)
        for t, r in h1[h1.index >= split].iterrows():
            for bar in bars_of(t, r):
                ts, p = bar.ts, bar.close
                store.append(bar)
                st.now = ts + pd.Timedelta("1min"); st.last_prices[sym] = p
                await broker.on_bar(bar)
                for pos in list(st.positions.values()):                       # stand-in for the position manager
                    if pos.status != "open":
                        continue
                    if pos.open_qty <= 0 and pos.id not in broker.open_positions:
                        pos.status, pos.exit_reason = "closed", "stop"; continue
                    pos.mfe_r = max(pos.mfe_r, pos.r_now(bar.high if pos.side > 0 else bar.low))
                    prev = stops_seen.get(pos.id)
                    assert prev is None or (pos.stop - prev) * pos.side >= -1e-9      # stops only move toward profit
                    stops_seen[pos.id] = pos.stop
                    if pos.meta.get("pending_close"):
                        await broker.close(pos, p)
                        pos.status, pos.exit_reason = "closed", pos.meta["pending_close"]
                await tr.on_bar(bar)
    asyncio.run(go())
    for ev in events:                                                         # the journal / notifier read ev["position"]
        assert isinstance(ev, dict) and "position" in ev and "event" in ev
    return st, ctx


def check_run(book, st, ctx, spec, over=None):
    over = over or {}
    ps = [p for p in st.positions.values() if p.strategy == book]
    assert ps, f"{book} took no trades in the test period"
    tf_min = {"15min": 15, "1h": 60, "4h": 60, "1D": 60}[spec["tf"]]
    for p in ps:
        assert (p.entry - p.initial_stop) * p.side > 0 and p.meta["hold_overnight"]
        assert p.meta["chop"] < 61.8, "a trade must never be taken in a choppy market"
        if over.get("use_supertrend"):
            assert p.meta["supertrend"] == p.side, "with the Supertrend gate on, no trade goes against it"
        assert p.opened_ts.minute % tf_min <= 5                                 # at a candle boundary (up to 5 min late)
        wall = p.opened_ts.tz_convert(TZ)
        if spec["tf"] == "4h":
            assert wall.hour in (1, 5, 9, 13, 17, 21)
        if spec["tf"] == "1D":
            assert wall.hour == 17
        elif over.get("use_hours"):
            m = wall.hour * 60 + wall.minute
            assert (m >= 20 * 60 or m < 11 * 60) and not (3 * 60 <= m < 6 * 60)     # gold window, never 03-06
    why = " ".join(s["why"] for s in ctx.journal.signals if s["action"] == "rejected")
    return ps, why


@pytest.mark.parametrize("book,days,sparse", [("my_ema_rsi_15m", 25, False), ("my_rsi_1h", 40, False), ("my_ema_cross_4h", 120, True),
                                              ("my_ema_rsi_4h", 120, True), ("my_ema_rsi_1d", 260, True), ("my_ema_cross_1d", 260, True)])
def test_book_runs_end_to_end_and_respects_every_rule(book, days, sparse):
    st, ctx = run_book(book, days=days, seed=11, warm_days=6, sparse=sparse)
    ps, why = check_run(book, st, ctx, SPECS[book])
    assert "choppy" in why or "stop too wide" in why or "stop distance" in why or len(ps) > 3
    assert any(p.exit_reason for p in ps)


@pytest.mark.parametrize("book,days", [("my_ema_rsi_15m", 25), ("my_ema_cross_1h", 40)])
def test_with_the_optional_gates_switched_on_the_old_rules_hold(book, days):
    over = {"use_supertrend": True, "use_hours": True}
    st, ctx = run_book(book, days=days, seed=11, warm_days=6, over=over)
    ps, why = check_run(book, st, ctx, SPECS[book], over)
    assert "outside entry hours" in why or "against Supertrend" in why


def test_a_whole_run_with_jev_booking_partials_keeps_the_books_consistent():
    jev = FakeJev(prob=0.2)
    st, ctx = run_book("my_ema_rsi_1h", days=40, seed=11, warm_days=6, jev=jev)
    ps = [p for p in st.positions.values() if p.strategy == "my_ema_rsi_1h"]
    parts = [p for p in ps if p.partial_done]
    assert jev.calls and parts, "Jev was asked and at least one trade booked a partial"
    for p in parts:
        assert p.meta["agent_partials"] <= 2
        assert p.closed_qty > 0 and p.gross_qty + 1e-9 >= p.closed_qty              # never more closed than was opened
        assert [e["kind"] for e in p.events].count("partial") == p.meta["agent_partials"]


# ───────────────────────── intraday momentum ─────────────────────────
def mom_bars(days=14, seed=2, start="2026-09-28"):
    """1-minute NDQ bars for weekday sessions (18:00 the evening before -> 17:00), with a known 16:00 close and 10:00 price."""
    rng = np.random.default_rng(seed)
    rows, facts, prev_close = [], {}, 20000.0
    for d in pd.bdate_range(start, periods=days):
        t0 = pd.Timestamp(d, tz=TZ).replace(hour=0)
        times = pd.date_range(t0 - pd.Timedelta(hours=6), t0 + pd.Timedelta(hours=17), freq="1min", inclusive="left")
        loc = times.tz_convert(TZ)
        mins = loc.hour * 60 + loc.minute
        sign = 1 if rng.random() < 0.5 else -1
        p10 = prev_close * (1 + sign * rng.uniform(0.002, 0.008))
        price = np.empty(len(times))
        before = mins >= 18 * 60                                                 # the evening before (18:00-24:00)
        price[:] = np.nan
        m10, m1530, m16 = 10 * 60, 15 * 60 + 30, 16 * 60
        for i, (m, bf) in enumerate(zip(mins, before)):
            if bf or m < m10:
                f = ((m - 18 * 60) % 1440) / ((m10 - 18 * 60) % 1440 or 1)
                price[i] = prev_close + (p10 - prev_close) * min(1.0, f)
            elif m < m1530:
                price[i] = p10 * (1 + 0.0004 * np.sin(m / 40))
            elif m < m16:
                price[i] = p10 * (1 + (m - m1530) / 30 * 0.0006 * -sign)         # the last half-hour fades the morning move
            else:
                price[i] = p10 * (1 - 0.0006 * sign)
        price += rng.normal(0, 0.4, len(price))
        close16 = float(price[np.argmax(mins == m16 - 1)])
        facts[d.date()] = {"prev_close": prev_close, "p10": float(price[np.argmax(mins == m10 - 1)])}
        prev_close = close16
        for ts, p in zip(times, price):
            rows.append(Bar("NDQ", ts, float(p), float(p) + 0.3, float(p) - 0.3, float(p), 1.0))
    return rows, facts


def run_mom(bars):
    cfg = prep_cfg(MOM, ["NDQ"])
    store = BarStore(TZ, max_days=30)
    st = LiveState(); st.equity = st.day_start_equity = st.equity_peak = 2000.0
    bus = Bus()
    broker = PaperBroker(cfg, st, bus)
    ctx = Ctx(cfg, bus, st, store, broker, J(), None, None)
    tr = MyIntradayMomTrader(ctx, MOM); tr.start()
    closed_at = {}

    async def go():
        for bar in bars:
            store.append(bar)
            st.now = bar.ts + pd.Timedelta("1min"); st.last_prices["NDQ"] = bar.close
            await broker.on_bar(bar)
            for pos in list(st.positions.values()):
                if pos.status != "open":
                    continue
                if pos.open_qty <= 0 and pos.id not in broker.open_positions:
                    pos.status, pos.exit_reason = "closed", "stop"; closed_at[pos.id] = st.now; continue
                pos.mfe_r = max(pos.mfe_r, pos.r_now(bar.high if pos.side > 0 else bar.low))
                if pos.meta.get("pending_close"):
                    await broker.close(pos, bar.close)
                    pos.status, pos.exit_reason = "closed", pos.meta["pending_close"]; closed_at[pos.id] = st.now
            await tr.on_bar(bar)
    asyncio.run(go())
    return st, ctx, tr, closed_at


def test_intraday_momentum_direction_timing_and_exit():
    bars, facts = mom_bars()
    st, ctx, tr, closed_at = run_mom(bars)
    ps = [p for p in st.positions.values() if p.strategy == MOM]
    assert len(ps) >= 8, "most weekdays should produce a trade"
    days = [p.opened_ts.tz_convert(TZ).date() for p in ps]
    assert len(days) == len(set(days)), "one trade per index per day"
    for p in ps:
        loc = p.opened_ts.tz_convert(TZ)
        assert (loc.hour, loc.minute) == (15, 30) and loc.dayofweek < 5          # always at 15:30
        f = facts[loc.date()]
        want = 1 if f["p10"] / f["prev_close"] - 1 > 0 else -1                    # sign of (16:00 close -> 10:00) return
        assert p.side == want, (loc.date(), p.side, want)
        assert abs(p.meta["r1"] - (f["p10"] / f["prev_close"] - 1)) < 0.0015      # noise in the synthetic prices only
        assert (p.entry - p.initial_stop) * p.side > 0 and p.meta["hold_overnight"]
        out = closed_at[p.id].tz_convert(TZ)
        assert out.date() == loc.date() and out.hour * 60 + out.minute <= 16 * 60 + 1     # out by 16:00, never overnight
        assert p.exit_reason in ("session_close", "stop")


def test_intraday_momentum_skips_weekends_and_missing_data():
    bars, _ = mom_bars(days=3)
    st, ctx, tr, _ = run_mom(bars[: 60 * 12])                                      # data ends before the 10:00 print
    assert not [p for p in st.positions.values() if p.strategy == MOM]
    assert all(s["action"] == "rejected" for s in ctx.journal.signals)


def test_his_book_uses_the_chop_cutoff_setting(monkeypatch):
    import fxagents.agents.ema_rsi_trader as ert
    when = pd.Timestamp("2026-10-13 10:00", tz=TZ)
    monkeypatch.setattr(ert, "chop_index", lambda df, *a, **k: pd.Series(60.0, index=df.index))      # CHOP reads 60 everywhere

    def run(tr):
        b = his_frame(choppy=False)
        tr.state.now = when
        tr.state.last_prices["XAUUSD"] = float(b.c.iloc[-1])
        asyncio.run(tr.maybe_enter("XAUUSD", b, when, Bar("XAUUSD", when - pd.Timedelta("1min"), 1.0, 1.0, 1.0, 1.0, 1.0)))
        return tr.ctx.journal.signals[-1]
    assert run(his_book(True, chop_max=58.5))["action"] == "rejected"       # 60 >= 58.5
    assert run(his_book(True, chop_max=61.8))["action"] == "taken"          # 60 < 61.8
    assert run(his_book(True))["action"] == "rejected"                      # the installed setting is 58.5
