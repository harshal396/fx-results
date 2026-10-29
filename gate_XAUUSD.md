# Context for XAUUSD - generated 2026-10-28 23:25 New York

Candles are labelled by their OPEN time, like TradingView. The **signal candle** is the one that closed when the bot entered; the trade opened at the open of the next candle. Prices are OANDA mid prices.


## Gate check for XAUUSD: would the new rules have blocked these trades?

Applied with each book's installed settings (15m/1h books: chop 58.5 + fresh cross + RSI direction + trend gate; 4h: chop + trend gate + oversized candle; daily: chop only; his EMA21+RSI55 book: chop only). 'not covered' = Playbook, Practice, momentum and other books the rules do not touch.

| Opened (NY) | Book | Side | Result | How it ended | Verdict | Reasons |
|---|---|---|---|---|---|---|
| 10-22 11:15 | my_rsi_15m | short | open |  | **BLOCKED** | the RSI 60/40 15m book is retired; not a fresh cross (price on this side of the EMA21 for 9 candles, limit 2); RSI not falling for a sell (RSI 38, 33 three candles ago) |
| 10-28 05:00 | my_ema_rsi_1h | long | -0.42R | close_past_ema21 | kept |  |
| 10-28 08:15 | ema21_rsi55 | long | -0.23R | close_below_ema21 | kept | his book: chop cutoff only |
| 10-28 08:15 | my_ema_rsi_15m | long | -0.30R | close_past_ema21 | kept |  |
| 10-28 09:00 | my_ema_cross_4h | long | -0.20R | pre-news: Federal Funds Rate | **BLOCKED** | against the 1D trend (bearish) |
| 10-28 11:30 | my_ema_rsi_15m | short | +0.29R | stop | **BLOCKED** | not a fresh cross (price on this side of the EMA21 for 7 candles, limit 2); RSI not falling for a sell (RSI 44, 38 three candles ago) |
| 10-28 15:00 | ema21_rsi55 | short | -0.64R | close_above_ema21 | kept | his book: chop cutoff only |
| 10-28 15:00 | my_ema_cross_1h | short | -1.00R | stop | **BLOCKED** | not a fresh cross (price on this side of the EMA21 for 5 candles, limit 2) |
| 10-28 15:00 | my_ema_rsi_1h | short | -1.00R | stop | **BLOCKED** | not a fresh cross (price on this side of the EMA21 for 5 candles, limit 2) |
| 10-28 15:15 | ema21_rsi55 | long | +0.31R | session_flat | kept | his book: chop cutoff only |
| 10-28 15:15 | my_ema_rsi_15m | long | +0.21R | stop | **BLOCKED** | against the 1h trend (bearish) |
| 10-28 17:00 | my_ema_rsi_4h | long | -0.57R | close_past_ema21 | **BLOCKED** | against the 1D trend (bearish) |
| 10-28 20:15 | my_ema_cross_15m | short | -0.44R | close_past_ema21 | **BLOCKED** | against the 1h trend (bullish) |
| 10-28 20:30 | my_ema_rsi_15m | short | -0.64R | close_past_ema21 | **BLOCKED** | against the 1h trend (bullish) |
| 10-28 21:45 | my_ema_cross_15m | long | -0.17R | close_past_ema21 | **BLOCKED** | not a fresh cross (price on this side of the EMA21 for 3 candles, limit 2); against the 1h trend (bearish) |
| 10-28 22:00 | my_ema_rsi_15m | long | -0.36R | close_past_ema21 | **BLOCKED** | not a fresh cross (price on this side of the EMA21 for 4 candles, limit 2) |
| 10-28 22:00 | my_ema_rsi_1h | long | -0.36R | close_past_ema21 | **BLOCKED** | against the 4h trend (bearish) |
| 10-28 22:45 | my_ema_cross_15m | short | open |  | **BLOCKED** | not a fresh cross (price on this side of the EMA21 for 3 candles, limit 2); against the 1h trend (bullish) |

**Summary XAUUSD:** 18 EMA/RSI trades checked, **13 blocked**, 5 kept; closed R of the blocked ones -4.23R (11 closed), of the kept ones -1.28R (5 closed); 0 trades from books the rules do not touch.


## ema21_rsi55 · LONG · entered 10-28 08:15 → exited 10-28 10:00 · close_below_ema21 · R -0.228 (best 0.49)

Logged entry reason: `EMA21+RSI55: 15m close 4052.65 > EMA21 4047.39, RSI 57.9`

Signal candle: **10-28 08:00** (15min); the trade opened right after it closed at 08:15.

| Measure | Value |
|---|---|
| close | 4052.65 |
| ema21 | 4047.39 |
| beyond EMA21 (ATR) | 1.08 |
| candles on this side of EMA21 (1 = this one just crossed) | 1 |
| RSI | 57.93 |
| RSI before | 48.13 |
| CHOP | 56.12 |
| EMA21 side changes in last 12 candles | 6 |
| Supertrend | 1 |
| last 3 closes | ↑↓↑ |
| signal candle body / range | 0.84 |
| signal candle range (ATR) | 1.76 |
| move since the 20-candle extreme (ATR) | 4.05 |
| closed beyond the prior 10-candle extreme | False |
| ADX(14) | 20.33 |
| EMA9 beyond EMA21 in the trade direction (ATR) | 0.24 |
| EMA9/21 crossed this many candles ago | 16 |
| EMA9/21 crosses in the last 20 candles | 1 |
| EMA21 slope over 8 candles in the trade direction (ATR) | 0.08 |
| RSI change over 3 candles | 6.98 |

Higher timeframes at that moment: 1h: close above EMA21, EMA21 > EMA50, RSI 53, Supertrend down → **with the trade**; 4h: close above EMA21, EMA21 < EMA50, RSI 52, Supertrend down → **with the trade**

| Candle (opens, NY) | O | H | L | C | EMA21 | RSI | CHOP | ST | |
|---|---|---|---|---|---|---|---|---|---|
| 10-28 06:00 | 4055.6 | 4055.6 | 4048.0 | 4049.9 | 4047.0 | 54.7 | 36 | up |  |
| 10-28 06:15 | 4049.7 | 4050.7 | 4045.8 | 4046.2 | 4047.0 | 49.5 | 38 | up |  |
| 10-28 06:30 | 4046.2 | 4048.4 | 4044.8 | 4047.5 | 4047.0 | 51.2 | 42 | up |  |
| 10-28 06:45 | 4047.4 | 4047.7 | 4044.4 | 4045.0 | 4046.8 | 47.7 | 46 | up |  |
| 10-28 07:00 | 4045.1 | 4047.0 | 4043.1 | 4046.7 | 4046.8 | 50.2 | 48 | up |  |
| 10-28 07:15 | 4046.6 | 4047.9 | 4045.3 | 4047.2 | 4046.8 | 51.0 | 57 | up |  |
| 10-28 07:30 | 4047.2 | 4049.3 | 4046.8 | 4048.5 | 4047.0 | 53.0 | 56 | up |  |
| 10-28 07:45 | 4048.5 | 4049.3 | 4044.8 | 4045.5 | 4046.9 | 48.1 | 56 | up |  |
| 10-28 08:00 | 4045.5 | 4053.0 | 4044.4 | 4052.7 | 4047.4 | 57.9 | 56 | up | **SIGNAL candle (closed → entry)** |
| 10-28 08:15 | 4052.6 | 4060.2 | 4052.4 | 4056.8 | 4048.3 | 62.4 | 53 | up | next candle (entry price) |
| 10-28 08:30 | 4056.8 | 4057.0 | 4053.4 | 4054.5 | 4048.8 | 58.7 | 52 | up |  |
| 10-28 08:45 | 4054.6 | 4055.3 | 4050.4 | 4053.4 | 4049.2 | 56.9 | 52 | up |  |
| 10-28 09:00 | 4053.5 | 4057.9 | 4052.4 | 4054.5 | 4049.7 | 58.2 | 52 | up |  |
| 10-28 09:15 | 4054.5 | 4054.9 | 4050.4 | 4051.8 | 4049.9 | 53.9 | 52 | up |  |
| 10-28 09:30 | 4051.8 | 4052.8 | 4045.8 | 4050.3 | 4050.0 | 51.6 | 52 | up |  |
| 10-28 09:45 | 4050.3 | 4051.9 | 4047.8 | 4049.9 | 4050.0 | 50.9 | 52 | up | ← exit decided on this close |
| 10-28 10:00 | 4049.9 | 4050.4 | 4045.5 | 4047.6 | 4049.7 | 47.2 | 52 | up |  |
| 10-28 10:15 | 4047.5 | 4049.0 | 4041.1 | 4042.0 | 4049.0 | 39.9 | 51 | up |  |

## ema21_rsi55 · SHORT · entered 10-28 15:00 → exited 10-28 15:15 · close_above_ema21 · R -0.638 (best 0.19)

Logged entry reason: `EMA21+RSI45 short: 15m close 4033.16 < EMA21 4041.94, RSI 42.4`

Signal candle: **10-28 14:45** (15min); the trade opened right after it closed at 15:00.

| Measure | Value |
|---|---|
| close | 4033.16 |
| ema21 | 4041.94 |
| beyond EMA21 (ATR) | 0.88 |
| candles on this side of EMA21 (1 = this one just crossed) | 1 |
| RSI | 42.42 |
| RSI before | 62.48 |
| CHOP | 45.83 |
| EMA21 side changes in last 12 candles | 2 |
| Supertrend | 1 |
| last 3 closes | ↑↑↓ |
| signal candle body / range | 0.75 |
| signal candle range (ATR) | 2.91 |
| move since the 20-candle extreme (ATR) | 3.47 |
| closed beyond the prior 10-candle extreme | False |
| ADX(14) | 22.86 |
| EMA9 beyond EMA21 in the trade direction (ATR) | 0.17 |
| EMA9/21 crossed this many candles ago | 19 |
| EMA9/21 crosses in the last 20 candles | 1 |
| EMA21 slope over 8 candles in the trade direction (ATR) | 0.26 |
| RSI change over 3 candles | 6.67 |

Higher timeframes at that moment: 1h: close below EMA21, EMA21 > EMA50, RSI 43, Supertrend down → **with the trade**; 4h: close above EMA21, EMA21 < EMA50, RSI 49, Supertrend down → **AGAINST the trade**

| Candle (opens, NY) | O | H | L | C | EMA21 | RSI | CHOP | ST | |
|---|---|---|---|---|---|---|---|---|---|
| 10-28 12:45 | 4040.6 | 4048.4 | 4039.4 | 4042.5 | 4044.5 | 45.6 | 57 | dn |  |
| 10-28 13:00 | 4042.5 | 4042.9 | 4040.9 | 4041.5 | 4044.2 | 44.2 | 56 | dn |  |
| 10-28 13:15 | 4041.6 | 4042.1 | 4038.0 | 4038.5 | 4043.7 | 39.9 | 60 | dn |  |
| 10-28 13:30 | 4038.5 | 4041.7 | 4037.8 | 4038.2 | 4043.2 | 39.4 | 64 | dn |  |
| 10-28 13:45 | 4038.2 | 4041.8 | 4037.5 | 4040.3 | 4042.9 | 43.8 | 63 | dn |  |
| 10-28 14:00 | 4040.3 | 4047.6 | 4030.3 | 4034.1 | 4042.1 | 35.8 | 54 | dn |  |
| 10-28 14:15 | 4034.1 | 4037.4 | 4029.6 | 4036.4 | 4041.6 | 40.1 | 55 | dn |  |
| 10-28 14:30 | 4036.3 | 4067.7 | 4024.7 | 4054.8 | 4042.8 | 62.5 | 38 | up |  |
| 10-28 14:45 | 4054.8 | 4062.0 | 4033.0 | 4033.2 | 4041.9 | 42.4 | 46 | up | **SIGNAL candle (closed → entry)** |
| 10-28 15:00 | 4033.2 | 4054.8 | 4027.3 | 4051.6 | 4042.8 | 55.5 | 51 | up | ← exit decided on this close |
| 10-28 15:15 | 4051.6 | 4055.3 | 4040.6 | 4055.0 | 4043.9 | 57.4 | 53 | up |  |
| 10-28 15:30 | 4054.9 | 4062.2 | 4049.3 | 4060.2 | 4045.4 | 60.3 | 55 | up |  |

## ema21_rsi55 · LONG · entered 10-28 15:15 → exited 10-28 15:50 · session_flat · R 0.309 (best 0.33)

Logged entry reason: `EMA21+RSI55: 15m close 4051.62 > EMA21 4042.82, RSI 55.5`

Signal candle: **10-28 15:00** (15min); the trade opened right after it closed at 15:15.

| Measure | Value |
|---|---|
| close | 4051.62 |
| ema21 | 4042.82 |
| beyond EMA21 (ATR) | 0.78 |
| candles on this side of EMA21 (1 = this one just crossed) | 1 |
| RSI | 55.53 |
| RSI before | 42.42 |
| CHOP | 51.15 |
| EMA21 side changes in last 12 candles | 3 |
| Supertrend | 1 |
| last 3 closes | ↑↓↑ |
| signal candle body / range | 0.67 |
| signal candle range (ATR) | 2.45 |
| move since the 20-candle extreme (ATR) | 2.40 |
| closed beyond the prior 10-candle extreme | False |
| ADX(14) | 22.71 |
| EMA9 beyond EMA21 in the trade direction (ATR) | -0.03 |
| EMA9/21 crossed this many candles ago | >19 |
| EMA9/21 crosses in the last 20 candles | 0 |
| EMA21 slope over 8 candles in the trade direction (ATR) | -0.13 |
| RSI change over 3 candles | 15.46 |

Higher timeframes at that moment: 1h: close below EMA21, EMA21 > EMA50, RSI 43, Supertrend down → **AGAINST the trade**; 4h: close above EMA21, EMA21 < EMA50, RSI 49, Supertrend down → **with the trade**

| Candle (opens, NY) | O | H | L | C | EMA21 | RSI | CHOP | ST | |
|---|---|---|---|---|---|---|---|---|---|
| 10-28 13:00 | 4042.5 | 4042.9 | 4040.9 | 4041.5 | 4044.2 | 44.2 | 56 | dn |  |
| 10-28 13:15 | 4041.6 | 4042.1 | 4038.0 | 4038.5 | 4043.7 | 39.9 | 60 | dn |  |
| 10-28 13:30 | 4038.5 | 4041.7 | 4037.8 | 4038.2 | 4043.2 | 39.4 | 64 | dn |  |
| 10-28 13:45 | 4038.2 | 4041.8 | 4037.5 | 4040.3 | 4042.9 | 43.8 | 63 | dn |  |
| 10-28 14:00 | 4040.3 | 4047.6 | 4030.3 | 4034.1 | 4042.1 | 35.8 | 54 | dn |  |
| 10-28 14:15 | 4034.1 | 4037.4 | 4029.6 | 4036.4 | 4041.6 | 40.1 | 55 | dn |  |
| 10-28 14:30 | 4036.3 | 4067.7 | 4024.7 | 4054.8 | 4042.8 | 62.5 | 38 | up |  |
| 10-28 14:45 | 4054.8 | 4062.0 | 4033.0 | 4033.2 | 4041.9 | 42.4 | 46 | up |  |
| 10-28 15:00 | 4033.2 | 4054.8 | 4027.3 | 4051.6 | 4042.8 | 55.5 | 51 | up | **SIGNAL candle (closed → entry)** |
| 10-28 15:15 | 4051.6 | 4055.3 | 4040.6 | 4055.0 | 4043.9 | 57.4 | 53 | up | next candle (entry price) |
| 10-28 15:30 | 4054.9 | 4062.2 | 4049.3 | 4060.2 | 4045.4 | 60.3 | 55 | up | ← exit decided on this close |
| 10-28 15:45 | 4060.3 | 4076.0 | 4058.9 | 4075.2 | 4048.1 | 67.0 | 51 | up |  |
| 10-28 16:00 | 4075.2 | 4082.8 | 4066.9 | 4069.0 | 4050.0 | 62.3 | 48 | up |  |

## my_ema_cross_15m · SHORT · entered 10-28 20:15 → exited 10-28 21:15 · close_past_ema21 · R -0.439 (best 0.37)

Logged entry reason: `my_ema_cross_15m: 15min close 4044.66 < EMA21 4053.31, RSI 44.2, CHOP 43, Supertrend up`

Signal candle: **10-28 20:00** (15min); the trade opened right after it closed at 20:15.

| Measure | Value |
|---|---|
| close | 4044.66 |
| ema21 | 4053.31 |
| beyond EMA21 (ATR) | 0.94 |
| candles on this side of EMA21 (1 = this one just crossed) | 1 |
| RSI | 44.16 |
| RSI before | 50.90 |
| CHOP | 43.08 |
| EMA21 side changes in last 12 candles | 5 |
| Supertrend | 1 |
| last 3 closes | ↓↑↓ |
| signal candle body / range | 0.85 |
| signal candle range (ATR) | 1.26 |
| move since the 20-candle extreme (ATR) | 4.16 |
| closed beyond the prior 10-candle extreme | True |
| ADX(14) | 17.20 |
| EMA9 beyond EMA21 in the trade direction (ATR) | 0.02 |
| EMA9/21 crossed this many candles ago | 1 |
| EMA9/21 crosses in the last 20 candles | 2 |
| EMA21 slope over 8 candles in the trade direction (ATR) | 0.15 |
| RSI change over 3 candles | -5.62 |

Higher timeframes at that moment: 1h: close above EMA21, EMA21 > EMA50, RSI 54, Supertrend up → **AGAINST the trade**; 4h: close above EMA21, EMA21 < EMA50, RSI 56, Supertrend down → **AGAINST the trade**

| Candle (opens, NY) | O | H | L | C | EMA21 | RSI | CHOP | ST | |
|---|---|---|---|---|---|---|---|---|---|
| 10-28 18:00 | 4065.9 | 4068.1 | 4062.7 | 4063.0 | 4054.6 | 55.9 | 52 | up |  |
| 10-28 18:15 | 4063.0 | 4064.1 | 4053.8 | 4054.7 | 4054.6 | 50.9 | 53 | up |  |
| 10-28 18:30 | 4054.9 | 4056.8 | 4053.8 | 4054.0 | 4054.6 | 50.5 | 50 | up |  |
| 10-28 18:45 | 4054.1 | 4054.5 | 4051.1 | 4051.9 | 4054.4 | 49.3 | 49 | up |  |
| 10-28 19:00 | 4052.0 | 4057.1 | 4050.9 | 4055.4 | 4054.4 | 51.4 | 44 | up |  |
| 10-28 19:15 | 4055.4 | 4056.4 | 4051.1 | 4052.9 | 4054.3 | 49.8 | 39 | up |  |
| 10-28 19:30 | 4052.8 | 4055.7 | 4051.3 | 4052.6 | 4054.2 | 49.6 | 43 | up |  |
| 10-28 19:45 | 4052.6 | 4058.5 | 4052.6 | 4054.4 | 4054.2 | 50.9 | 49 | up |  |
| 10-28 20:00 | 4054.5 | 4055.7 | 4044.2 | 4044.7 | 4053.3 | 44.2 | 43 | up | **SIGNAL candle (closed → entry)** |
| 10-28 20:15 | 4044.7 | 4047.8 | 4039.9 | 4042.4 | 4052.3 | 42.7 | 36 | up | next candle (entry price) |
| 10-28 20:30 | 4042.4 | 4044.1 | 4037.0 | 4039.7 | 4051.2 | 41.1 | 42 | up |  |
| 10-28 20:45 | 4039.6 | 4040.3 | 4036.4 | 4037.0 | 4049.9 | 39.4 | 37 | up |  |
| 10-28 21:00 | 4037.0 | 4056.0 | 4036.2 | 4053.7 | 4050.2 | 52.3 | 39 | up | ← exit decided on this close |
| 10-28 21:15 | 4053.7 | 4068.9 | 4052.9 | 4066.0 | 4051.7 | 59.3 | 46 | up |  |
| 10-28 21:30 | 4066.0 | 4067.0 | 4052.7 | 4055.7 | 4052.0 | 52.4 | 49 | up |  |

## my_ema_cross_15m · LONG · entered 10-28 21:45 → exited 10-28 22:15 · close_past_ema21 · R -0.165 (best 0.45)

Logged entry reason: `my_ema_cross_15m: 15min close 4055.74 > EMA21 4052.03, RSI 52.4, CHOP 49, Supertrend up`

Signal candle: **10-28 21:30** (15min); the trade opened right after it closed at 21:45.

| Measure | Value |
|---|---|
| close | 4055.74 |
| ema21 | 4052.03 |
| beyond EMA21 (ATR) | 0.37 |
| candles on this side of EMA21 (1 = this one just crossed) | 3 |
| RSI | 52.43 |
| RSI before | 59.25 |
| CHOP | 48.96 |
| EMA21 side changes in last 12 candles | 5 |
| Supertrend | 1 |
| last 3 closes | ↑↑↓ |
| signal candle body / range | 0.72 |
| signal candle range (ATR) | 1.41 |
| move since the 20-candle extreme (ATR) | 1.92 |
| closed beyond the prior 10-candle extreme | False |
| ADX(14) | 17.98 |
| EMA9 beyond EMA21 in the trade direction (ATR) | 0.03 |
| EMA9/21 crossed this many candles ago | 1 |
| EMA9/21 crosses in the last 20 candles | 2 |
| EMA21 slope over 8 candles in the trade direction (ATR) | -0.21 |
| RSI change over 3 candles | 13.04 |

Higher timeframes at that moment: 1h: close below EMA21, EMA21 > EMA50, RSI 46, Supertrend up → **AGAINST the trade**; 4h: close below EMA21, EMA21 < EMA50, RSI 47, Supertrend down → **AGAINST the trade**

| Candle (opens, NY) | O | H | L | C | EMA21 | RSI | CHOP | ST | |
|---|---|---|---|---|---|---|---|---|---|
| 10-28 19:30 | 4052.8 | 4055.7 | 4051.3 | 4052.6 | 4054.2 | 49.6 | 43 | up |  |
| 10-28 19:45 | 4052.6 | 4058.5 | 4052.6 | 4054.4 | 4054.2 | 50.9 | 49 | up |  |
| 10-28 20:00 | 4054.5 | 4055.7 | 4044.2 | 4044.7 | 4053.3 | 44.2 | 43 | up |  |
| 10-28 20:15 | 4044.7 | 4047.8 | 4039.9 | 4042.4 | 4052.3 | 42.7 | 36 | up |  |
| 10-28 20:30 | 4042.4 | 4044.1 | 4037.0 | 4039.7 | 4051.2 | 41.1 | 42 | up |  |
| 10-28 20:45 | 4039.6 | 4040.3 | 4036.4 | 4037.0 | 4049.9 | 39.4 | 37 | up |  |
| 10-28 21:00 | 4037.0 | 4056.0 | 4036.2 | 4053.7 | 4050.2 | 52.3 | 39 | up |  |
| 10-28 21:15 | 4053.7 | 4068.9 | 4052.9 | 4066.0 | 4051.7 | 59.3 | 46 | up |  |
| 10-28 21:30 | 4066.0 | 4067.0 | 4052.7 | 4055.7 | 4052.0 | 52.4 | 49 | up | **SIGNAL candle (closed → entry)** |
| 10-28 21:45 | 4055.8 | 4066.2 | 4050.9 | 4062.5 | 4053.0 | 56.0 | 51 | up | next candle (entry price) |
| 10-28 22:00 | 4062.6 | 4064.9 | 4049.4 | 4052.7 | 4053.0 | 50.1 | 54 | up | ← exit decided on this close |
| 10-28 22:15 | 4052.6 | 4054.6 | 4045.7 | 4045.8 | 4052.3 | 46.4 | 56 | up |  |
| 10-28 22:30 | 4045.7 | 4047.0 | 4039.8 | 4043.3 | 4051.5 | 45.1 | 56 | up |  |

## my_ema_cross_15m · SHORT · entered 10-28 22:45 → OPEN ·  · R - (best 0.00)

Logged entry reason: `my_ema_cross_15m: 15min close 4043.28 < EMA21 4051.49, RSI 45.1, CHOP 56, Supertrend up`

Signal candle: **10-28 22:30** (15min); the trade opened right after it closed at 22:45.

| Measure | Value |
|---|---|
| close | 4043.28 |
| ema21 | 4051.49 |
| beyond EMA21 (ATR) | 0.78 |
| candles on this side of EMA21 (1 = this one just crossed) | 3 |
| RSI | 45.08 |
| RSI before | 46.42 |
| CHOP | 55.99 |
| EMA21 side changes in last 12 candles | 3 |
| Supertrend | 1 |
| last 3 closes | ↓↓↓ |
| signal candle body / range | 0.34 |
| signal candle range (ATR) | 0.69 |
| move since the 20-candle extreme (ATR) | 2.65 |
| closed beyond the prior 10-candle extreme | False |
| ADX(14) | 16.71 |
| EMA9 beyond EMA21 in the trade direction (ATR) | 0.09 |
| EMA9/21 crossed this many candles ago | 1 |
| EMA9/21 crosses in the last 20 candles | 3 |
| EMA21 slope over 8 candles in the trade direction (ATR) | -0.03 |
| RSI change over 3 candles | -10.96 |

Higher timeframes at that moment: 1h: close above EMA21, EMA21 > EMA50, RSI 56, Supertrend up → **AGAINST the trade**; 4h: close below EMA21, EMA21 < EMA50, RSI 47, Supertrend down → **with the trade**

| Candle (opens, NY) | O | H | L | C | EMA21 | RSI | CHOP | ST | |
|---|---|---|---|---|---|---|---|---|---|
| 10-28 20:30 | 4042.4 | 4044.1 | 4037.0 | 4039.7 | 4051.2 | 41.1 | 42 | up |  |
| 10-28 20:45 | 4039.6 | 4040.3 | 4036.4 | 4037.0 | 4049.9 | 39.4 | 37 | up |  |
| 10-28 21:00 | 4037.0 | 4056.0 | 4036.2 | 4053.7 | 4050.2 | 52.3 | 39 | up |  |
| 10-28 21:15 | 4053.7 | 4068.9 | 4052.9 | 4066.0 | 4051.7 | 59.3 | 46 | up |  |
| 10-28 21:30 | 4066.0 | 4067.0 | 4052.7 | 4055.7 | 4052.0 | 52.4 | 49 | up |  |
| 10-28 21:45 | 4055.8 | 4066.2 | 4050.9 | 4062.5 | 4053.0 | 56.0 | 51 | up |  |
| 10-28 22:00 | 4062.6 | 4064.9 | 4049.4 | 4052.7 | 4053.0 | 50.1 | 54 | up |  |
| 10-28 22:15 | 4052.6 | 4054.6 | 4045.7 | 4045.8 | 4052.3 | 46.4 | 56 | up |  |
| 10-28 22:30 | 4045.7 | 4047.0 | 4039.8 | 4043.3 | 4051.5 | 45.1 | 56 | up | **SIGNAL candle (closed → entry)** |
| 10-28 22:45 | 4043.2 | 4050.4 | 4042.2 | 4047.8 | 4051.2 | 47.9 | 57 | up | next candle (entry price) |
| 10-28 23:00 | 4047.7 | 4048.4 | 4037.0 | 4039.5 | 4050.1 | 43.5 | 59 | up |  |

## my_ema_cross_1h · SHORT · entered 10-28 15:00 → exited 10-28 15:59 · stop · R -1.0 (best 0.15)

Logged entry reason: `my_ema_cross_1h: 1h close 4033.16 < EMA21 4042.80, RSI 43.5, CHOP 54, Supertrend down`

Signal candle: **10-28 14:00** (1h); the trade opened right after it closed at 15:00.

| Measure | Value |
|---|---|
| close | 4033.16 |
| ema21 | 4042.80 |
| beyond EMA21 (ATR) | 0.76 |
| candles on this side of EMA21 (1 = this one just crossed) | 5 |
| RSI | 43.47 |
| RSI before | 48.39 |
| CHOP | 53.77 |
| EMA21 side changes in last 12 candles | 1 |
| Supertrend | -1 |
| last 3 closes | ↑↓↓ |
| signal candle body / range | 0.17 |
| signal candle range (ATR) | 3.38 |
| move since the 20-candle extreme (ATR) | 2.96 |
| closed beyond the prior 10-candle extreme | True |
| ADX(14) | 20.41 |
| EMA9 beyond EMA21 in the trade direction (ATR) | 0.06 |
| EMA9/21 crossed this many candles ago | 1 |
| EMA9/21 crosses in the last 20 candles | 1 |
| EMA21 slope over 8 candles in the trade direction (ATR) | 0.03 |
| RSI change over 3 candles | -6.16 |

Higher timeframes at that moment: 1h: close below EMA21, EMA21 > EMA50, RSI 43, Supertrend down → **with the trade**; 4h: close above EMA21, EMA21 < EMA50, RSI 49, Supertrend down → **AGAINST the trade**

| Candle (opens, NY) | O | H | L | C | EMA21 | RSI | CHOP | ST | |
|---|---|---|---|---|---|---|---|---|---|
| 10-28 06:00 | 4055.6 | 4055.6 | 4044.4 | 4045.0 | 4043.1 | 52.8 | 42 | dn |  |
| 10-28 07:00 | 4045.1 | 4049.3 | 4043.1 | 4045.5 | 4043.4 | 53.1 | 43 | dn |  |
| 10-28 08:00 | 4045.5 | 4060.2 | 4044.4 | 4053.4 | 4044.3 | 57.7 | 46 | dn |  |
| 10-28 09:00 | 4053.5 | 4057.9 | 4045.8 | 4049.9 | 4044.8 | 55.1 | 48 | dn |  |
| 10-28 10:00 | 4049.9 | 4050.4 | 4036.9 | 4041.8 | 4044.5 | 49.5 | 54 | dn |  |
| 10-28 11:00 | 4041.7 | 4046.5 | 4040.5 | 4041.9 | 4044.3 | 49.6 | 56 | dn |  |
| 10-28 12:00 | 4042.0 | 4048.4 | 4036.1 | 4042.5 | 4044.1 | 50.0 | 57 | dn |  |
| 10-28 13:00 | 4042.5 | 4042.9 | 4037.5 | 4040.3 | 4043.8 | 48.4 | 57 | dn |  |
| 10-28 14:00 | 4040.3 | 4067.7 | 4024.7 | 4033.2 | 4042.8 | 43.5 | 54 | dn | ← exit decided on this close |
| 10-28 15:00 | 4033.2 | 4076.0 | 4027.3 | 4075.2 | 4045.7 | 65.7 | 55 | up |  |
| 10-28 16:00 | 4075.2 | 4082.8 | 4055.5 | 4067.3 | 4047.7 | 60.9 | 54 | up |  |

## my_ema_cross_4h · LONG · entered 10-28 09:00 → exited 10-28 13:55 · pre-news: Federal Funds Rate · R -0.196 (best 0.06)

Logged entry reason: `my_ema_cross_4h: 4h close 4053.41 > EMA21 4041.62, RSI 52.0, CHOP 53, Supertrend down`

Signal candle: **10-28 05:00** (4h); the trade opened right after it closed at 09:00.

| Measure | Value |
|---|---|
| close | 4053.41 |
| ema21 | 4041.62 |
| beyond EMA21 (ATR) | 0.46 |
| candles on this side of EMA21 (1 = this one just crossed) | 2 |
| RSI | 52.02 |
| RSI before | 51.90 |
| CHOP | 53.15 |
| EMA21 side changes in last 12 candles | 3 |
| Supertrend | -1 |
| last 3 closes | ↓↑↑ |
| signal candle body / range | 0.02 |
| signal candle range (ATR) | 0.67 |
| move since the 20-candle extreme (ATR) | 3.04 |
| closed beyond the prior 10-candle extreme | False |
| ADX(14) | 34.04 |
| EMA9 beyond EMA21 in the trade direction (ATR) | 0.04 |
| EMA9/21 crossed this many candles ago | 1 |
| EMA9/21 crosses in the last 20 candles | 1 |
| EMA21 slope over 8 candles in the trade direction (ATR) | 0.17 |
| RSI change over 3 candles | -2.82 |

Higher timeframes at that moment: 1h: close above EMA21, EMA21 > EMA50, RSI 58, Supertrend down → **with the trade**; 4h: close above EMA21, EMA21 < EMA50, RSI 52, Supertrend down → **with the trade**

| Candle (opens, NY) | O | H | L | C | EMA21 | RSI | CHOP | ST | |
|---|---|---|---|---|---|---|---|---|---|
| 10-26 21:00 | 4009.5 | 4025.6 | 4004.0 | 4010.7 | 4037.2 | 36.3 | 69 | dn |  |
| 10-27 01:00 | 4010.8 | 4012.2 | 3989.2 | 3994.9 | 4033.4 | 32.6 | 69 | dn |  |
| 10-27 05:00 | 3994.9 | 4028.6 | 3993.4 | 4023.2 | 4032.4 | 43.7 | 68 | dn |  |
| 10-27 09:00 | 4023.2 | 4064.9 | 4020.6 | 4059.2 | 4034.9 | 54.1 | 54 | dn |  |
| 10-27 13:00 | 4059.2 | 4065.7 | 4054.4 | 4060.3 | 4037.2 | 54.4 | 54 | dn |  |
| 10-27 17:00 | 4061.2 | 4070.8 | 4057.7 | 4061.9 | 4039.4 | 54.8 | 48 | dn |  |
| 10-27 21:00 | 4061.9 | 4064.4 | 4035.9 | 4036.7 | 4039.2 | 47.3 | 50 | dn |  |
| 10-28 01:00 | 4036.7 | 4058.3 | 4028.2 | 4053.0 | 4040.4 | 51.9 | 51 | dn |  |
| 10-28 05:00 | 4053.0 | 4060.2 | 4043.1 | 4053.4 | 4041.6 | 52.0 | 53 | dn | **SIGNAL candle (closed → entry)** |
| 10-28 09:00 | 4053.5 | 4057.9 | 4036.1 | 4042.5 | 4041.7 | 48.7 | 53 | dn | ← exit decided on this close |
| 10-28 13:00 | 4042.5 | 4082.8 | 4024.7 | 4067.3 | 4044.0 | 55.6 | 53 | dn |  |
| 10-28 17:00 | 4065.9 | 4068.1 | 4036.4 | 4037.0 | 4043.4 | 47.3 | 52 | dn |  |

## my_ema_rsi_15m · LONG · entered 10-28 08:15 → exited 10-28 10:00 · close_past_ema21 · R -0.299 (best 0.65)

Logged entry reason: `my_ema_rsi_15m: 15min close 4052.65 > EMA21 4047.39, RSI 57.9, CHOP 56, Supertrend up`

Signal candle: **10-28 08:00** (15min); the trade opened right after it closed at 08:15.

| Measure | Value |
|---|---|
| close | 4052.65 |
| ema21 | 4047.39 |
| beyond EMA21 (ATR) | 1.08 |
| candles on this side of EMA21 (1 = this one just crossed) | 1 |
| RSI | 57.93 |
| RSI before | 48.13 |
| CHOP | 56.12 |
| EMA21 side changes in last 12 candles | 6 |
| Supertrend | 1 |
| last 3 closes | ↑↓↑ |
| signal candle body / range | 0.84 |
| signal candle range (ATR) | 1.76 |
| move since the 20-candle extreme (ATR) | 4.05 |
| closed beyond the prior 10-candle extreme | False |
| ADX(14) | 20.33 |
| EMA9 beyond EMA21 in the trade direction (ATR) | 0.24 |
| EMA9/21 crossed this many candles ago | 16 |
| EMA9/21 crosses in the last 20 candles | 1 |
| EMA21 slope over 8 candles in the trade direction (ATR) | 0.08 |
| RSI change over 3 candles | 6.98 |

Higher timeframes at that moment: 1h: close above EMA21, EMA21 > EMA50, RSI 53, Supertrend down → **with the trade**; 4h: close above EMA21, EMA21 < EMA50, RSI 52, Supertrend down → **with the trade**

| Candle (opens, NY) | O | H | L | C | EMA21 | RSI | CHOP | ST | |
|---|---|---|---|---|---|---|---|---|---|
| 10-28 06:00 | 4055.6 | 4055.6 | 4048.0 | 4049.9 | 4047.0 | 54.7 | 36 | up |  |
| 10-28 06:15 | 4049.7 | 4050.7 | 4045.8 | 4046.2 | 4047.0 | 49.5 | 38 | up |  |
| 10-28 06:30 | 4046.2 | 4048.4 | 4044.8 | 4047.5 | 4047.0 | 51.2 | 42 | up |  |
| 10-28 06:45 | 4047.4 | 4047.7 | 4044.4 | 4045.0 | 4046.8 | 47.7 | 46 | up |  |
| 10-28 07:00 | 4045.1 | 4047.0 | 4043.1 | 4046.7 | 4046.8 | 50.2 | 48 | up |  |
| 10-28 07:15 | 4046.6 | 4047.9 | 4045.3 | 4047.2 | 4046.8 | 51.0 | 57 | up |  |
| 10-28 07:30 | 4047.2 | 4049.3 | 4046.8 | 4048.5 | 4047.0 | 53.0 | 56 | up |  |
| 10-28 07:45 | 4048.5 | 4049.3 | 4044.8 | 4045.5 | 4046.9 | 48.1 | 56 | up |  |
| 10-28 08:00 | 4045.5 | 4053.0 | 4044.4 | 4052.7 | 4047.4 | 57.9 | 56 | up | **SIGNAL candle (closed → entry)** |
| 10-28 08:15 | 4052.6 | 4060.2 | 4052.4 | 4056.8 | 4048.3 | 62.4 | 53 | up | next candle (entry price) |
| 10-28 08:30 | 4056.8 | 4057.0 | 4053.4 | 4054.5 | 4048.8 | 58.7 | 52 | up |  |
| 10-28 08:45 | 4054.6 | 4055.3 | 4050.4 | 4053.4 | 4049.2 | 56.9 | 52 | up |  |
| 10-28 09:00 | 4053.5 | 4057.9 | 4052.4 | 4054.5 | 4049.7 | 58.2 | 52 | up |  |
| 10-28 09:15 | 4054.5 | 4054.9 | 4050.4 | 4051.8 | 4049.9 | 53.9 | 52 | up |  |
| 10-28 09:30 | 4051.8 | 4052.8 | 4045.8 | 4050.3 | 4050.0 | 51.6 | 52 | up |  |
| 10-28 09:45 | 4050.3 | 4051.9 | 4047.8 | 4049.9 | 4050.0 | 50.9 | 52 | up | ← exit decided on this close |
| 10-28 10:00 | 4049.9 | 4050.4 | 4045.5 | 4047.6 | 4049.7 | 47.2 | 52 | up |  |
| 10-28 10:15 | 4047.5 | 4049.0 | 4041.1 | 4042.0 | 4049.0 | 39.9 | 51 | up |  |

## my_ema_rsi_15m · SHORT · entered 10-28 11:30 → exited 10-28 14:01 · stop · R 0.287 (best 0.65)

Logged entry reason: `my_ema_rsi_15m: 15min close 4043.49 < EMA21 4047.00, RSI 43.7, CHOP 45, Supertrend down`

Signal candle: **10-28 11:15** (15min); the trade opened right after it closed at 11:30.

| Measure | Value |
|---|---|
| close | 4043.49 |
| ema21 | 4047.00 |
| beyond EMA21 (ATR) | 0.70 |
| candles on this side of EMA21 (1 = this one just crossed) | 7 |
| RSI | 43.70 |
| RSI before | 44.50 |
| CHOP | 45.43 |
| EMA21 side changes in last 12 candles | 1 |
| Supertrend | -1 |
| last 3 closes | ↑↑↓ |
| signal candle body / range | 0.16 |
| signal candle range (ATR) | 0.65 |
| move since the 20-candle extreme (ATR) | 3.31 |
| closed beyond the prior 10-candle extreme | False |
| ADX(14) | 19.30 |
| EMA9 beyond EMA21 in the trade direction (ATR) | 0.34 |
| EMA9/21 crossed this many candles ago | 5 |
| EMA9/21 crosses in the last 20 candles | 1 |
| EMA21 slope over 8 candles in the trade direction (ATR) | 0.58 |
| RSI change over 3 candles | 5.35 |

Higher timeframes at that moment: 1h: close below EMA21, EMA21 > EMA50, RSI 50, Supertrend down → **with the trade**; 4h: close above EMA21, EMA21 < EMA50, RSI 52, Supertrend down → **AGAINST the trade**

| Candle (opens, NY) | O | H | L | C | EMA21 | RSI | CHOP | ST | |
|---|---|---|---|---|---|---|---|---|---|
| 10-28 09:15 | 4054.5 | 4054.9 | 4050.4 | 4051.8 | 4049.9 | 53.9 | 52 | up |  |
| 10-28 09:30 | 4051.8 | 4052.8 | 4045.8 | 4050.3 | 4050.0 | 51.6 | 52 | up |  |
| 10-28 09:45 | 4050.3 | 4051.9 | 4047.8 | 4049.9 | 4050.0 | 50.9 | 52 | up |  |
| 10-28 10:00 | 4049.9 | 4050.4 | 4045.5 | 4047.6 | 4049.7 | 47.2 | 52 | up |  |
| 10-28 10:15 | 4047.5 | 4049.0 | 4041.1 | 4042.0 | 4049.0 | 39.9 | 51 | up |  |
| 10-28 10:30 | 4042.0 | 4044.2 | 4036.9 | 4040.7 | 4048.3 | 38.3 | 45 | dn |  |
| 10-28 10:45 | 4040.6 | 4043.3 | 4039.6 | 4041.8 | 4047.7 | 40.4 | 45 | dn |  |
| 10-28 11:00 | 4041.7 | 4045.1 | 4041.1 | 4044.1 | 4047.3 | 44.5 | 46 | dn |  |
| 10-28 11:15 | 4044.0 | 4046.2 | 4042.9 | 4043.5 | 4047.0 | 43.7 | 45 | dn | **SIGNAL candle (closed → entry)** |
| 10-28 11:30 | 4043.4 | 4046.5 | 4040.7 | 4045.4 | 4046.9 | 47.2 | 44 | dn | next candle (entry price) |
| 10-28 11:45 | 4045.4 | 4045.5 | 4040.5 | 4041.9 | 4046.4 | 42.1 | 46 | dn |  |
| 10-28 12:00 | 4042.0 | 4042.6 | 4036.1 | 4037.7 | 4045.6 | 36.9 | 46 | dn |  |
| 10-28 12:15 | 4037.6 | 4041.3 | 4037.2 | 4040.3 | 4045.1 | 41.7 | 46 | dn |  |
| 10-28 12:30 | 4040.3 | 4041.3 | 4038.8 | 4040.6 | 4044.7 | 42.2 | 50 | dn |  |
| 10-28 12:45 | 4040.6 | 4048.4 | 4039.4 | 4042.5 | 4044.5 | 45.6 | 57 | dn |  |
| 10-28 13:00 | 4042.5 | 4042.9 | 4040.9 | 4041.5 | 4044.2 | 44.2 | 56 | dn |  |
| 10-28 13:15 | 4041.6 | 4042.1 | 4038.0 | 4038.5 | 4043.7 | 39.9 | 60 | dn |  |
| 10-28 13:30 | 4038.5 | 4041.7 | 4037.8 | 4038.2 | 4043.2 | 39.4 | 64 | dn |  |
| 10-28 13:45 | 4038.2 | 4041.8 | 4037.5 | 4040.3 | 4042.9 | 43.8 | 63 | dn | ← exit decided on this close |
| 10-28 14:00 | 4040.3 | 4047.6 | 4030.3 | 4034.1 | 4042.1 | 35.8 | 54 | dn |  |
| 10-28 14:15 | 4034.1 | 4037.4 | 4029.6 | 4036.4 | 4041.6 | 40.1 | 55 | dn |  |

## my_ema_rsi_15m · LONG · entered 10-28 15:15 → exited 10-28 16:29 · stop · R 0.213 (best 1.03)

Logged entry reason: `my_ema_rsi_15m: 15min close 4051.62 > EMA21 4042.82, RSI 55.5, CHOP 51, Supertrend up`

Signal candle: **10-28 15:00** (15min); the trade opened right after it closed at 15:15.

| Measure | Value |
|---|---|
| close | 4051.62 |
| ema21 | 4042.82 |
| beyond EMA21 (ATR) | 0.78 |
| candles on this side of EMA21 (1 = this one just crossed) | 1 |
| RSI | 55.53 |
| RSI before | 42.42 |
| CHOP | 51.15 |
| EMA21 side changes in last 12 candles | 3 |
| Supertrend | 1 |
| last 3 closes | ↑↓↑ |
| signal candle body / range | 0.67 |
| signal candle range (ATR) | 2.45 |
| move since the 20-candle extreme (ATR) | 2.40 |
| closed beyond the prior 10-candle extreme | False |
| ADX(14) | 22.71 |
| EMA9 beyond EMA21 in the trade direction (ATR) | -0.03 |
| EMA9/21 crossed this many candles ago | >19 |
| EMA9/21 crosses in the last 20 candles | 0 |
| EMA21 slope over 8 candles in the trade direction (ATR) | -0.13 |
| RSI change over 3 candles | 15.46 |

Higher timeframes at that moment: 1h: close below EMA21, EMA21 > EMA50, RSI 43, Supertrend down → **AGAINST the trade**; 4h: close above EMA21, EMA21 < EMA50, RSI 49, Supertrend down → **with the trade**

| Candle (opens, NY) | O | H | L | C | EMA21 | RSI | CHOP | ST | |
|---|---|---|---|---|---|---|---|---|---|
| 10-28 13:00 | 4042.5 | 4042.9 | 4040.9 | 4041.5 | 4044.2 | 44.2 | 56 | dn |  |
| 10-28 13:15 | 4041.6 | 4042.1 | 4038.0 | 4038.5 | 4043.7 | 39.9 | 60 | dn |  |
| 10-28 13:30 | 4038.5 | 4041.7 | 4037.8 | 4038.2 | 4043.2 | 39.4 | 64 | dn |  |
| 10-28 13:45 | 4038.2 | 4041.8 | 4037.5 | 4040.3 | 4042.9 | 43.8 | 63 | dn |  |
| 10-28 14:00 | 4040.3 | 4047.6 | 4030.3 | 4034.1 | 4042.1 | 35.8 | 54 | dn |  |
| 10-28 14:15 | 4034.1 | 4037.4 | 4029.6 | 4036.4 | 4041.6 | 40.1 | 55 | dn |  |
| 10-28 14:30 | 4036.3 | 4067.7 | 4024.7 | 4054.8 | 4042.8 | 62.5 | 38 | up |  |
| 10-28 14:45 | 4054.8 | 4062.0 | 4033.0 | 4033.2 | 4041.9 | 42.4 | 46 | up |  |
| 10-28 15:00 | 4033.2 | 4054.8 | 4027.3 | 4051.6 | 4042.8 | 55.5 | 51 | up | **SIGNAL candle (closed → entry)** |
| 10-28 15:15 | 4051.6 | 4055.3 | 4040.6 | 4055.0 | 4043.9 | 57.4 | 53 | up | next candle (entry price) |
| 10-28 15:30 | 4054.9 | 4062.2 | 4049.3 | 4060.2 | 4045.4 | 60.3 | 55 | up |  |
| 10-28 15:45 | 4060.3 | 4076.0 | 4058.9 | 4075.2 | 4048.1 | 67.0 | 51 | up |  |
| 10-28 16:00 | 4075.2 | 4082.8 | 4066.9 | 4069.0 | 4050.0 | 62.3 | 48 | up | ← exit decided on this close |
| 10-28 16:15 | 4069.0 | 4070.1 | 4056.9 | 4057.6 | 4050.7 | 54.7 | 49 | up |  |
| 10-28 16:30 | 4057.7 | 4070.1 | 4055.5 | 4070.0 | 4052.5 | 60.4 | 51 | up |  |

## my_ema_rsi_15m · SHORT · entered 10-28 20:30 → exited 10-28 21:15 · close_past_ema21 · R -0.639 (best 0.31)

Logged entry reason: `my_ema_rsi_15m: 15min close 4042.37 < EMA21 4052.31, RSI 42.7, CHOP 36, Supertrend up`

Signal candle: **10-28 20:15** (15min); the trade opened right after it closed at 20:30.

| Measure | Value |
|---|---|
| close | 4042.37 |
| ema21 | 4052.31 |
| beyond EMA21 (ATR) | 1.09 |
| candles on this side of EMA21 (1 = this one just crossed) | 2 |
| RSI | 42.73 |
| RSI before | 44.16 |
| CHOP | 36.10 |
| EMA21 side changes in last 12 candles | 5 |
| Supertrend | 1 |
| last 3 closes | ↑↓↓ |
| signal candle body / range | 0.29 |
| signal candle range (ATR) | 0.87 |
| move since the 20-candle extreme (ATR) | 4.45 |
| closed beyond the prior 10-candle extreme | True |
| ADX(14) | 16.95 |
| EMA9 beyond EMA21 in the trade direction (ATR) | 0.14 |
| EMA9/21 crossed this many candles ago | 2 |
| EMA9/21 crosses in the last 20 candles | 2 |
| EMA21 slope over 8 candles in the trade direction (ATR) | 0.26 |
| RSI change over 3 candles | -6.86 |

Higher timeframes at that moment: 1h: close above EMA21, EMA21 > EMA50, RSI 54, Supertrend up → **AGAINST the trade**; 4h: close above EMA21, EMA21 < EMA50, RSI 56, Supertrend down → **AGAINST the trade**

| Candle (opens, NY) | O | H | L | C | EMA21 | RSI | CHOP | ST | |
|---|---|---|---|---|---|---|---|---|---|
| 10-28 18:15 | 4063.0 | 4064.1 | 4053.8 | 4054.7 | 4054.6 | 50.9 | 53 | up |  |
| 10-28 18:30 | 4054.9 | 4056.8 | 4053.8 | 4054.0 | 4054.6 | 50.5 | 50 | up |  |
| 10-28 18:45 | 4054.1 | 4054.5 | 4051.1 | 4051.9 | 4054.4 | 49.3 | 49 | up |  |
| 10-28 19:00 | 4052.0 | 4057.1 | 4050.9 | 4055.4 | 4054.4 | 51.4 | 44 | up |  |
| 10-28 19:15 | 4055.4 | 4056.4 | 4051.1 | 4052.9 | 4054.3 | 49.8 | 39 | up |  |
| 10-28 19:30 | 4052.8 | 4055.7 | 4051.3 | 4052.6 | 4054.2 | 49.6 | 43 | up |  |
| 10-28 19:45 | 4052.6 | 4058.5 | 4052.6 | 4054.4 | 4054.2 | 50.9 | 49 | up |  |
| 10-28 20:00 | 4054.5 | 4055.7 | 4044.2 | 4044.7 | 4053.3 | 44.2 | 43 | up |  |
| 10-28 20:15 | 4044.7 | 4047.8 | 4039.9 | 4042.4 | 4052.3 | 42.7 | 36 | up | **SIGNAL candle (closed → entry)** |
| 10-28 20:30 | 4042.4 | 4044.1 | 4037.0 | 4039.7 | 4051.2 | 41.1 | 42 | up | next candle (entry price) |
| 10-28 20:45 | 4039.6 | 4040.3 | 4036.4 | 4037.0 | 4049.9 | 39.4 | 37 | up |  |
| 10-28 21:00 | 4037.0 | 4056.0 | 4036.2 | 4053.7 | 4050.2 | 52.3 | 39 | up | ← exit decided on this close |
| 10-28 21:15 | 4053.7 | 4068.9 | 4052.9 | 4066.0 | 4051.7 | 59.3 | 46 | up |  |
| 10-28 21:30 | 4066.0 | 4067.0 | 4052.7 | 4055.7 | 4052.0 | 52.4 | 49 | up |  |

## my_ema_rsi_15m · LONG · entered 10-28 22:00 → exited 10-28 22:15 · close_past_ema21 · R -0.358 (best 0.07)

Logged entry reason: `my_ema_rsi_15m: 15min close 4062.53 > EMA21 4052.99, RSI 56.0, CHOP 51, Supertrend up`

Signal candle: **10-28 21:45** (15min); the trade opened right after it closed at 22:00.

| Measure | Value |
|---|---|
| close | 4062.53 |
| ema21 | 4052.99 |
| beyond EMA21 (ATR) | 0.91 |
| candles on this side of EMA21 (1 = this one just crossed) | 4 |
| RSI | 56.04 |
| RSI before | 52.43 |
| CHOP | 50.52 |
| EMA21 side changes in last 12 candles | 4 |
| Supertrend | 1 |
| last 3 closes | ↑↓↑ |
| signal candle body / range | 0.44 |
| signal candle range (ATR) | 1.45 |
| move since the 20-candle extreme (ATR) | 2.50 |
| closed beyond the prior 10-candle extreme | False |
| ADX(14) | 18.29 |
| EMA9 beyond EMA21 in the trade direction (ATR) | 0.13 |
| EMA9/21 crossed this many candles ago | 2 |
| EMA9/21 crosses in the last 20 candles | 2 |
| EMA21 slope over 8 candles in the trade direction (ATR) | -0.11 |
| RSI change over 3 candles | 3.70 |

Higher timeframes at that moment: 1h: close above EMA21, EMA21 > EMA50, RSI 56, Supertrend up → **with the trade**; 4h: close below EMA21, EMA21 < EMA50, RSI 47, Supertrend down → **AGAINST the trade**

| Candle (opens, NY) | O | H | L | C | EMA21 | RSI | CHOP | ST | |
|---|---|---|---|---|---|---|---|---|---|
| 10-28 19:45 | 4052.6 | 4058.5 | 4052.6 | 4054.4 | 4054.2 | 50.9 | 49 | up |  |
| 10-28 20:00 | 4054.5 | 4055.7 | 4044.2 | 4044.7 | 4053.3 | 44.2 | 43 | up |  |
| 10-28 20:15 | 4044.7 | 4047.8 | 4039.9 | 4042.4 | 4052.3 | 42.7 | 36 | up |  |
| 10-28 20:30 | 4042.4 | 4044.1 | 4037.0 | 4039.7 | 4051.2 | 41.1 | 42 | up |  |
| 10-28 20:45 | 4039.6 | 4040.3 | 4036.4 | 4037.0 | 4049.9 | 39.4 | 37 | up |  |
| 10-28 21:00 | 4037.0 | 4056.0 | 4036.2 | 4053.7 | 4050.2 | 52.3 | 39 | up |  |
| 10-28 21:15 | 4053.7 | 4068.9 | 4052.9 | 4066.0 | 4051.7 | 59.3 | 46 | up |  |
| 10-28 21:30 | 4066.0 | 4067.0 | 4052.7 | 4055.7 | 4052.0 | 52.4 | 49 | up |  |
| 10-28 21:45 | 4055.8 | 4066.2 | 4050.9 | 4062.5 | 4053.0 | 56.0 | 51 | up | **SIGNAL candle (closed → entry)** |
| 10-28 22:00 | 4062.6 | 4064.9 | 4049.4 | 4052.7 | 4053.0 | 50.1 | 54 | up | ← exit decided on this close |
| 10-28 22:15 | 4052.6 | 4054.6 | 4045.7 | 4045.8 | 4052.3 | 46.4 | 56 | up |  |
| 10-28 22:30 | 4045.7 | 4047.0 | 4039.8 | 4043.3 | 4051.5 | 45.1 | 56 | up |  |

## my_ema_rsi_1h · LONG · entered 10-28 05:00 → exited 10-28 11:00 · close_past_ema21 · R -0.425 (best 0.25)

Logged entry reason: `my_ema_rsi_1h: 1h close 4052.97 > EMA21 4041.68, RSI 59.0, CHOP 41, Supertrend down`

Signal candle: **10-28 04:00** (1h); the trade opened right after it closed at 05:00.

| Measure | Value |
|---|---|
| close | 4052.97 |
| ema21 | 4041.68 |
| beyond EMA21 (ATR) | 1.03 |
| candles on this side of EMA21 (1 = this one just crossed) | 2 |
| RSI | 59.05 |
| RSI before | 54.44 |
| CHOP | 40.85 |
| EMA21 side changes in last 12 candles | 2 |
| Supertrend | -1 |
| last 3 closes | ↑↑↑ |
| signal candle body / range | 0.54 |
| signal candle range (ATR) | 1.39 |
| move since the 20-candle extreme (ATR) | 3.79 |
| closed beyond the prior 10-candle extreme | False |
| ADX(14) | 24.60 |
| EMA9 beyond EMA21 in the trade direction (ATR) | 0.26 |
| EMA9/21 crossed this many candles ago | >19 |
| EMA9/21 crosses in the last 20 candles | 0 |
| EMA21 slope over 8 candles in the trade direction (ATR) | 0.01 |
| RSI change over 3 candles | 14.64 |

Higher timeframes at that moment: 1h: close above EMA21, EMA21 > EMA50, RSI 59, Supertrend down → **with the trade**; 4h: close above EMA21, EMA21 < EMA50, RSI 52, Supertrend down → **with the trade**

| Candle (opens, NY) | O | H | L | C | EMA21 | RSI | CHOP | ST | |
|---|---|---|---|---|---|---|---|---|---|
| 10-27 20:00 | 4062.7 | 4070.8 | 4059.4 | 4061.9 | 4041.6 | 69.0 | 27 | up |  |
| 10-27 21:00 | 4061.9 | 4064.4 | 4045.3 | 4048.9 | 4042.3 | 57.5 | 33 | up |  |
| 10-27 22:00 | 4048.8 | 4051.6 | 4044.6 | 4046.6 | 4042.7 | 55.7 | 36 | up |  |
| 10-27 23:00 | 4046.6 | 4049.6 | 4042.7 | 4042.8 | 4042.7 | 52.8 | 40 | up |  |
| 10-28 00:00 | 4042.8 | 4043.7 | 4035.9 | 4036.7 | 4042.1 | 48.5 | 42 | up |  |
| 10-28 01:00 | 4036.7 | 4037.8 | 4030.2 | 4030.4 | 4041.1 | 44.4 | 40 | dn |  |
| 10-28 02:00 | 4030.3 | 4034.7 | 4028.2 | 4030.8 | 4040.1 | 44.8 | 36 | dn |  |
| 10-28 03:00 | 4030.8 | 4044.9 | 4028.2 | 4044.7 | 4040.6 | 54.4 | 39 | dn |  |
| 10-28 04:00 | 4044.7 | 4058.3 | 4043.0 | 4053.0 | 4041.7 | 59.0 | 41 | dn | **SIGNAL candle (closed → entry)** |
| 10-28 05:00 | 4053.0 | 4056.1 | 4049.8 | 4055.6 | 4042.9 | 60.4 | 41 | dn | next candle (entry price) |
| 10-28 06:00 | 4055.6 | 4055.6 | 4044.4 | 4045.0 | 4043.1 | 52.8 | 42 | dn |  |
| 10-28 07:00 | 4045.1 | 4049.3 | 4043.1 | 4045.5 | 4043.4 | 53.1 | 43 | dn |  |
| 10-28 08:00 | 4045.5 | 4060.2 | 4044.4 | 4053.4 | 4044.3 | 57.7 | 46 | dn |  |
| 10-28 09:00 | 4053.5 | 4057.9 | 4045.8 | 4049.9 | 4044.8 | 55.1 | 48 | dn |  |
| 10-28 10:00 | 4049.9 | 4050.4 | 4036.9 | 4041.8 | 4044.5 | 49.5 | 54 | dn | ← exit decided on this close |
| 10-28 11:00 | 4041.7 | 4046.5 | 4040.5 | 4041.9 | 4044.3 | 49.6 | 56 | dn |  |
| 10-28 12:00 | 4042.0 | 4048.4 | 4036.1 | 4042.5 | 4044.1 | 50.0 | 57 | dn |  |

## my_ema_rsi_1h · SHORT · entered 10-28 15:00 → exited 10-28 15:59 · stop · R -1.0 (best 0.15)

Logged entry reason: `my_ema_rsi_1h: 1h close 4033.16 < EMA21 4042.80, RSI 43.5, CHOP 54, Supertrend down`

Signal candle: **10-28 14:00** (1h); the trade opened right after it closed at 15:00.

| Measure | Value |
|---|---|
| close | 4033.16 |
| ema21 | 4042.80 |
| beyond EMA21 (ATR) | 0.76 |
| candles on this side of EMA21 (1 = this one just crossed) | 5 |
| RSI | 43.47 |
| RSI before | 48.39 |
| CHOP | 53.77 |
| EMA21 side changes in last 12 candles | 1 |
| Supertrend | -1 |
| last 3 closes | ↑↓↓ |
| signal candle body / range | 0.17 |
| signal candle range (ATR) | 3.38 |
| move since the 20-candle extreme (ATR) | 2.96 |
| closed beyond the prior 10-candle extreme | True |
| ADX(14) | 20.41 |
| EMA9 beyond EMA21 in the trade direction (ATR) | 0.06 |
| EMA9/21 crossed this many candles ago | 1 |
| EMA9/21 crosses in the last 20 candles | 1 |
| EMA21 slope over 8 candles in the trade direction (ATR) | 0.03 |
| RSI change over 3 candles | -6.16 |

Higher timeframes at that moment: 1h: close below EMA21, EMA21 > EMA50, RSI 43, Supertrend down → **with the trade**; 4h: close above EMA21, EMA21 < EMA50, RSI 49, Supertrend down → **AGAINST the trade**

| Candle (opens, NY) | O | H | L | C | EMA21 | RSI | CHOP | ST | |
|---|---|---|---|---|---|---|---|---|---|
| 10-28 06:00 | 4055.6 | 4055.6 | 4044.4 | 4045.0 | 4043.1 | 52.8 | 42 | dn |  |
| 10-28 07:00 | 4045.1 | 4049.3 | 4043.1 | 4045.5 | 4043.4 | 53.1 | 43 | dn |  |
| 10-28 08:00 | 4045.5 | 4060.2 | 4044.4 | 4053.4 | 4044.3 | 57.7 | 46 | dn |  |
| 10-28 09:00 | 4053.5 | 4057.9 | 4045.8 | 4049.9 | 4044.8 | 55.1 | 48 | dn |  |
| 10-28 10:00 | 4049.9 | 4050.4 | 4036.9 | 4041.8 | 4044.5 | 49.5 | 54 | dn |  |
| 10-28 11:00 | 4041.7 | 4046.5 | 4040.5 | 4041.9 | 4044.3 | 49.6 | 56 | dn |  |
| 10-28 12:00 | 4042.0 | 4048.4 | 4036.1 | 4042.5 | 4044.1 | 50.0 | 57 | dn |  |
| 10-28 13:00 | 4042.5 | 4042.9 | 4037.5 | 4040.3 | 4043.8 | 48.4 | 57 | dn |  |
| 10-28 14:00 | 4040.3 | 4067.7 | 4024.7 | 4033.2 | 4042.8 | 43.5 | 54 | dn | ← exit decided on this close |
| 10-28 15:00 | 4033.2 | 4076.0 | 4027.3 | 4075.2 | 4045.7 | 65.7 | 55 | up |  |
| 10-28 16:00 | 4075.2 | 4082.8 | 4055.5 | 4067.3 | 4047.7 | 60.9 | 54 | up |  |

## my_ema_rsi_1h · LONG · entered 10-28 22:00 → exited 10-28 23:00 · close_past_ema21 · R -0.363 (best 0.05)

Logged entry reason: `my_ema_rsi_1h: 1h close 4062.53 > EMA21 4048.96, RSI 56.1, CHOP 58, Supertrend up`

Signal candle: **10-28 21:00** (1h); the trade opened right after it closed at 22:00.

| Measure | Value |
|---|---|
| close | 4062.53 |
| ema21 | 4048.96 |
| beyond EMA21 (ATR) | 0.80 |
| candles on this side of EMA21 (1 = this one just crossed) | 1 |
| RSI | 56.08 |
| RSI before | 45.91 |
| CHOP | 57.74 |
| EMA21 side changes in last 12 candles | 4 |
| Supertrend | 1 |
| last 3 closes | ↑↓↑ |
| signal candle body / range | 0.78 |
| signal candle range (ATR) | 1.91 |
| move since the 20-candle extreme (ATR) | 2.22 |
| closed beyond the prior 10-candle extreme | False |
| ADX(14) | 24.28 |
| EMA9 beyond EMA21 in the trade direction (ATR) | 0.19 |
| EMA9/21 crossed this many candles ago | 6 |
| EMA9/21 crosses in the last 20 candles | 2 |
| EMA21 slope over 8 candles in the trade direction (ATR) | 0.28 |
| RSI change over 3 candles | 3.35 |

Higher timeframes at that moment: 1h: close above EMA21, EMA21 > EMA50, RSI 56, Supertrend up → **with the trade**; 4h: close below EMA21, EMA21 < EMA50, RSI 47, Supertrend down → **AGAINST the trade**

| Candle (opens, NY) | O | H | L | C | EMA21 | RSI | CHOP | ST | |
|---|---|---|---|---|---|---|---|---|---|
| 10-28 12:00 | 4042.0 | 4048.4 | 4036.1 | 4042.5 | 4044.1 | 50.0 | 57 | dn |  |
| 10-28 13:00 | 4042.5 | 4042.9 | 4037.5 | 4040.3 | 4043.8 | 48.4 | 57 | dn |  |
| 10-28 14:00 | 4040.3 | 4067.7 | 4024.7 | 4033.2 | 4042.8 | 43.5 | 54 | dn |  |
| 10-28 15:00 | 4033.2 | 4076.0 | 4027.3 | 4075.2 | 4045.7 | 65.7 | 55 | up |  |
| 10-28 16:00 | 4075.2 | 4082.8 | 4055.5 | 4067.3 | 4047.7 | 60.9 | 54 | up |  |
| 10-28 18:00 | 4065.9 | 4068.1 | 4051.1 | 4051.9 | 4048.1 | 52.7 | 54 | up |  |
| 10-28 19:00 | 4052.0 | 4058.5 | 4050.9 | 4054.4 | 4048.7 | 53.8 | 52 | up |  |
| 10-28 20:00 | 4054.5 | 4055.7 | 4036.4 | 4037.0 | 4047.6 | 45.9 | 55 | up |  |
| 10-28 21:00 | 4037.0 | 4068.9 | 4036.2 | 4062.5 | 4049.0 | 56.1 | 58 | up | **SIGNAL candle (closed → entry)** |
| 10-28 22:00 | 4062.6 | 4064.9 | 4039.8 | 4047.8 | 4048.8 | 50.2 | 60 | up | ← exit decided on this close |

## my_ema_rsi_4h · LONG · entered 10-28 17:00 → exited 10-28 21:00 · close_past_ema21 · R -0.573 (best 0.01)

Logged entry reason: `my_ema_rsi_4h: 4h close 4067.29 > EMA21 4044.02, RSI 55.6, CHOP 53, Supertrend down`

Signal candle: **10-28 13:00** (4h); the trade opened right after it closed at 17:00.

| Measure | Value |
|---|---|
| close | 4067.29 |
| ema21 | 4044.02 |
| beyond EMA21 (ATR) | 0.84 |
| candles on this side of EMA21 (1 = this one just crossed) | 4 |
| RSI | 55.60 |
| RSI before | 48.73 |
| CHOP | 52.88 |
| EMA21 side changes in last 12 candles | 3 |
| Supertrend | -1 |
| last 3 closes | ↑↓↑ |
| signal candle body / range | 0.43 |
| signal candle range (ATR) | 2.10 |
| move since the 20-candle extreme (ATR) | 3.31 |
| closed beyond the prior 10-candle extreme | False |
| ADX(14) | 31.26 |
| EMA9 beyond EMA21 in the trade direction (ATR) | 0.13 |
| EMA9/21 crossed this many candles ago | 3 |
| EMA9/21 crosses in the last 20 candles | 1 |
| EMA21 slope over 8 candles in the trade direction (ATR) | 0.42 |
| RSI change over 3 candles | 3.70 |

Higher timeframes at that moment: 1h: close above EMA21, EMA21 > EMA50, RSI 61, Supertrend up → **with the trade**; 4h: close above EMA21, EMA21 < EMA50, RSI 56, Supertrend down → **with the trade**

| Candle (opens, NY) | O | H | L | C | EMA21 | RSI | CHOP | ST | |
|---|---|---|---|---|---|---|---|---|---|
| 10-27 05:00 | 3994.9 | 4028.6 | 3993.4 | 4023.2 | 4032.4 | 43.7 | 68 | dn |  |
| 10-27 09:00 | 4023.2 | 4064.9 | 4020.6 | 4059.2 | 4034.9 | 54.1 | 54 | dn |  |
| 10-27 13:00 | 4059.2 | 4065.7 | 4054.4 | 4060.3 | 4037.2 | 54.4 | 54 | dn |  |
| 10-27 17:00 | 4061.2 | 4070.8 | 4057.7 | 4061.9 | 4039.4 | 54.8 | 48 | dn |  |
| 10-27 21:00 | 4061.9 | 4064.4 | 4035.9 | 4036.7 | 4039.2 | 47.3 | 50 | dn |  |
| 10-28 01:00 | 4036.7 | 4058.3 | 4028.2 | 4053.0 | 4040.4 | 51.9 | 51 | dn |  |
| 10-28 05:00 | 4053.0 | 4060.2 | 4043.1 | 4053.4 | 4041.6 | 52.0 | 53 | dn |  |
| 10-28 09:00 | 4053.5 | 4057.9 | 4036.1 | 4042.5 | 4041.7 | 48.7 | 53 | dn |  |
| 10-28 13:00 | 4042.5 | 4082.8 | 4024.7 | 4067.3 | 4044.0 | 55.6 | 53 | dn | **SIGNAL candle (closed → entry)** |
| 10-28 17:00 | 4065.9 | 4068.1 | 4036.4 | 4037.0 | 4043.4 | 47.3 | 52 | dn | ← exit decided on this close |
| 10-28 21:00 | 4037.0 | 4068.9 | 4036.2 | 4047.8 | 4043.8 | 50.1 | 53 | dn |  |

## my_rsi_15m · SHORT · entered 10-22 11:15 → OPEN ·  · R - (best 1.14)

Logged entry reason: `my_rsi_15m: 15min close 4055.01 < EMA21 4068.51, RSI 38.3, CHOP 49, Supertrend down`

Signal candle: **10-22 11:00** (15min); the trade opened right after it closed at 11:15.

| Measure | Value |
|---|---|
| close | 4055.01 |
| ema21 | 4068.51 |
| beyond EMA21 (ATR) | 1.26 |
| candles on this side of EMA21 (1 = this one just crossed) | 9 |
| RSI | 38.33 |
| RSI before | 40.76 |
| CHOP | 49.03 |
| EMA21 side changes in last 12 candles | 2 |
| Supertrend | -1 |
| last 3 closes | ↑↓↓ |
| signal candle body / range | 0.50 |
| signal candle range (ATR) | 0.86 |
| move since the 20-candle extreme (ATR) | 3.50 |
| closed beyond the prior 10-candle extreme | False |
| ADX(14) | 31.14 |
| EMA9 beyond EMA21 in the trade direction (ATR) | 0.74 |
| EMA9/21 crossed this many candles ago | >19 |
| EMA9/21 crosses in the last 20 candles | 0 |
| EMA21 slope over 8 candles in the trade direction (ATR) | 1.13 |
| RSI change over 3 candles | 4.96 |

Higher timeframes at that moment: 1h: close below EMA21, EMA21 < EMA50, RSI 35, Supertrend down → **with the trade**; 4h: close below EMA21, EMA21 < EMA50, RSI 36, Supertrend down → **with the trade**

| Candle (opens, NY) | O | H | L | C | EMA21 | RSI | CHOP | ST | |
|---|---|---|---|---|---|---|---|---|---|
| 10-22 09:00 | 4088.1 | 4088.4 | 4076.6 | 4076.6 | 4080.6 | 46.0 | 53 | dn |  |
| 10-22 09:15 | 4076.7 | 4081.5 | 4074.7 | 4076.8 | 4080.2 | 46.2 | 54 | dn |  |
| 10-22 09:30 | 4076.8 | 4080.8 | 4059.8 | 4059.8 | 4078.4 | 37.4 | 58 | dn |  |
| 10-22 09:45 | 4059.8 | 4067.5 | 4054.2 | 4057.0 | 4076.4 | 36.2 | 56 | dn |  |
| 10-22 10:00 | 4056.9 | 4060.9 | 4044.8 | 4051.5 | 4074.2 | 33.9 | 50 | dn |  |
| 10-22 10:15 | 4051.6 | 4054.7 | 4047.0 | 4050.3 | 4072.0 | 33.4 | 50 | dn |  |
| 10-22 10:30 | 4050.3 | 4061.4 | 4050.1 | 4059.7 | 4070.9 | 40.8 | 50 | dn |  |
| 10-22 10:45 | 4059.6 | 4065.0 | 4056.1 | 4059.6 | 4069.9 | 40.8 | 49 | dn |  |
| 10-22 11:00 | 4059.6 | 4063.1 | 4053.8 | 4055.0 | 4068.5 | 38.3 | 49 | dn | **SIGNAL candle (closed → entry)** |
| 10-22 11:15 | 4055.1 | 4061.2 | 4051.6 | 4051.8 | 4067.0 | 36.7 | 48 | dn | next candle (entry price) |
| 10-22 11:30 | 4051.9 | 4055.9 | 4048.8 | 4050.7 | 4065.5 | 36.1 | 46 | dn |  |
| 10-22 11:45 | 4050.7 | 4055.1 | 4050.2 | 4051.9 | 4064.3 | 37.3 | 45 | dn |  |
| 10-22 12:00 | 4052.0 | 4053.3 | 4045.1 | 4047.8 | 4062.8 | 35.0 | 43 | dn |  |
| 10-22 12:15 | 4047.8 | 4050.9 | 4043.5 | 4047.8 | 4061.4 | 35.0 | 44 | dn |  |
| 10-22 12:30 | 4047.8 | 4048.2 | 4041.3 | 4042.2 | 4059.7 | 31.9 | 47 | dn |  |
| 10-22 12:45 | 4042.2 | 4042.3 | 4034.3 | 4038.0 | 4057.7 | 29.7 | 42 | dn |  |
| 10-22 13:00 | 4038.0 | 4041.1 | 4034.7 | 4040.3 | 4056.1 | 32.4 | 50 | dn |  |

## Every logged signal on XAUUSD in the window (taken and skipped)

| Time (NY) | Book | What happened | Why |
|---|---|---|---|
| 10-28 04:00 | my_ema_rsi_15m | rejected | stop too wide (3.7 ATR) |
| 10-28 04:30 | my_ema_cross_15m | rejected | stop too wide (4.9 ATR) |
| 10-28 05:00 | my_ema_rsi_1h | taken | qty 12.5, jev 0.2475 |
| 10-28 08:15 | ema21_rsi55 | taken | qty 4.7, jev 0.315 |
| 10-28 08:15 | my_ema_rsi_15m | taken | qty 31.9, jev 0.2575 |
| 10-28 09:00 | my_ema_cross_4h | taken | qty 4.9, jev 0.26 |
| 10-28 10:30 | my_ema_cross_15m | rejected | stop too wide (3.4 ATR) |
| 10-28 10:30 | my_ema_rsi_15m | rejected | stop too wide (3.4 ATR) |
| 10-28 11:30 | my_ema_rsi_15m | taken | qty 32.6, jev 0.415 |
| 10-28 14:45 | ema21_rsi55 | rejected | news blackout: FOMC Press Conference |
| 10-28 14:45 | my_ema_rsi_15m | rejected | stop too wide (3.8 ATR) |
| 10-28 15:00 | ema21_rsi55 | taken | qty 2.3, jev 0.3825 |
| 10-28 15:00 | my_ema_cross_1h | taken | qty 9.1, jev 0.4225 |
| 10-28 15:00 | my_ema_rsi_15m | rejected | stop too wide (3.7 ATR) |
| 10-28 15:00 | my_ema_rsi_1h | taken | qty 9.1, jev 0.385 |
| 10-28 15:15 | ema21_rsi55 | taken | qty 2.0, jev 0.2875 |
| 10-28 15:15 | my_ema_rsi_15m | taken | qty 11.7, jev 0.25 |
| 10-28 15:30 | my_ema_cross_15m | rejected | trading halted: daily loss limit hit ($-1,941) |
| 10-28 16:00 | my_ema_cross_1h | rejected | stop too wide (3.6 ATR) |
| 10-28 16:00 | my_ema_rsi_1h | rejected | stop too wide (3.6 ATR) |
| 10-28 16:45 | my_ema_rsi_15m | rejected | stop too wide (3.7 ATR) |
| 10-28 17:00 | my_ema_rsi_4h | taken | qty 6.4, jev 0.49 |
| 10-28 20:15 | my_ema_cross_15m | taken | qty 15.9, jev 0.35 |
| 10-28 20:30 | my_ema_rsi_15m | taken | qty 18.6, jev 0.34 |
| 10-28 21:30 | my_ema_rsi_15m | rejected | stop too wide (3.3 ATR) |
| 10-28 21:45 | my_ema_cross_15m | taken | qty 15.6, jev 0.48 |
| 10-28 22:00 | my_ema_rsi_15m | taken | qty 12.0, jev 0.4975 |
| 10-28 22:00 | my_ema_rsi_1h | taken | qty 8.2, jev 0.48 |
| 10-28 22:45 | my_ema_cross_15m | taken | qty 12.2, jev 0.305 |
| 10-28 23:15 | my_ema_rsi_15m | rejected | not a fresh cross (the price has been below the EMA21 for 5 candles, limit 2) |
