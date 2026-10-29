# Context for NDQ - generated 2026-10-28 23:25 New York

Candles are labelled by their OPEN time, like TradingView. The **signal candle** is the one that closed when the bot entered; the trade opened at the open of the next candle. Prices are OANDA mid prices.


## Gate check for NDQ: would the new rules have blocked these trades?

Applied with each book's installed settings (15m/1h books: chop 58.5 + fresh cross + RSI direction + trend gate; 4h: chop + trend gate + oversized candle; daily: chop only; his EMA21+RSI55 book: chop only). 'not covered' = Playbook, Practice, momentum and other books the rules do not touch.

| Opened (NY) | Book | Side | Result | How it ended | Verdict | Reasons |
|---|---|---|---|---|---|---|
| 10-22 16:45 | my_rsi_15m | short | open |  | **BLOCKED** | the RSI 60/40 15m book is retired; choppy (CHOP 58.6 >= 58.5); not a fresh cross (price on this side of the EMA21 for 27 candles, limit 2) |
| 10-28 01:30 | my_rsi_15m | long | +0.39R | close_past_ema21 | **BLOCKED** | the RSI 60/40 15m book is retired; not a fresh cross (price on this side of the EMA21 for 57 candles, limit 2) |
| 10-28 06:00 | my_ema_rsi_15m | long | -0.47R | close_past_ema21 | **BLOCKED** | choppy (CHOP 61.7 >= 58.5) |
| 10-28 09:45 | my_ema_rsi_15m | short | +0.17R | stop | **BLOCKED** | choppy (CHOP 59.9 >= 58.5); not a fresh cross (price on this side of the EMA21 for 5 candles, limit 2); against the 1h trend (bullish) |
| 10-28 12:00 | my_ema_rsi_15m | short | -1.00R | stop | **BLOCKED** | not a fresh cross (price on this side of the EMA21 for 14 candles, limit 2); RSI not falling for a sell (RSI 44, 43 three candles ago); against the 1h trend (bullish) |
| 10-28 13:00 | my_ema_rsi_1h | long | -0.15R | pre-news: Federal Funds Rate | **BLOCKED** | choppy (CHOP 61.0 >= 58.5) |
| 10-28 15:45 | my_ema_rsi_15m | long | +0.21R | trail_through | **BLOCKED** | choppy (CHOP 61.4 >= 58.5); not a fresh cross (price on this side of the EMA21 for 6 candles, limit 2) |

**Summary NDQ:** 7 EMA/RSI trades checked, **7 blocked**, 0 kept; closed R of the blocked ones -0.85R (6 closed), of the kept ones +0.00R (0 closed); 0 trades from books the rules do not touch.


## my_ema_rsi_15m · LONG · entered 10-28 06:00 → exited 10-28 06:15 · close_past_ema21 · R -0.466 (best 0.06)

Logged entry reason: `my_ema_rsi_15m: 15min close 29815.10 > EMA21 29795.11, RSI 56.1, CHOP 62, Supertrend up`

Signal candle: **10-28 05:45** (15min); the trade opened right after it closed at 06:00.

| Measure | Value |
|---|---|
| close | 29815.10 |
| ema21 | 29795.11 |
| beyond EMA21 (ATR) | 0.59 |
| candles on this side of EMA21 (1 = this one just crossed) | 2 |
| RSI | 56.15 |
| RSI before | 51.90 |
| CHOP | 61.67 |
| EMA21 side changes in last 12 candles | 2 |
| Supertrend | 1 |
| last 3 closes | ↓↑↑ |
| signal candle body / range | 0.66 |
| signal candle range (ATR) | 0.91 |
| move since the 20-candle extreme (ATR) | 2.03 |
| closed beyond the prior 10-candle extreme | False |
| ADX(14) | 18.29 |
| EMA9 beyond EMA21 in the trade direction (ATR) | 0.15 |
| EMA9/21 crossed this many candles ago | >19 |
| EMA9/21 crosses in the last 20 candles | 0 |
| EMA21 slope over 8 candles in the trade direction (ATR) | 0.08 |
| RSI change over 3 candles | 6.06 |

Higher timeframes at that moment: 1h: close above EMA21, EMA21 > EMA50, RSI 68, Supertrend up → **with the trade**; 4h: close above EMA21, EMA21 < EMA50, RSI 65, Supertrend up → **with the trade**

| Candle (opens, NY) | O | H | L | C | EMA21 | RSI | CHOP | ST | |
|---|---|---|---|---|---|---|---|---|---|
| 10-28 03:45 | 29808.2 | 29843.6 | 29769.3 | 29841.2 | 29792.5 | 62.9 | 55 | up |  |
| 10-28 04:00 | 29841.4 | 29854.2 | 29817.4 | 29827.4 | 29795.7 | 59.4 | 55 | up |  |
| 10-28 04:15 | 29827.1 | 29841.4 | 29803.3 | 29811.2 | 29797.1 | 55.5 | 56 | up |  |
| 10-28 04:30 | 29811.8 | 29812.8 | 29781.4 | 29795.0 | 29796.9 | 51.9 | 64 | up |  |
| 10-28 04:45 | 29794.6 | 29809.1 | 29778.6 | 29790.2 | 29796.3 | 50.8 | 64 | up |  |
| 10-28 05:00 | 29791.2 | 29793.4 | 29777.1 | 29787.0 | 29795.4 | 50.1 | 64 | up |  |
| 10-28 05:15 | 29787.1 | 29813.2 | 29767.0 | 29768.8 | 29793.0 | 46.0 | 66 | up |  |
| 10-28 05:30 | 29768.6 | 29794.8 | 29756.1 | 29794.2 | 29793.1 | 51.9 | 61 | up |  |
| 10-28 05:45 | 29794.6 | 29816.6 | 29785.6 | 29815.1 | 29795.1 | 56.1 | 62 | up | **SIGNAL candle (closed → entry)** |
| 10-28 06:00 | 29815.2 | 29820.2 | 29757.0 | 29785.4 | 29794.2 | 49.5 | 64 | up | ← exit decided on this close |
| 10-28 06:15 | 29785.4 | 29809.1 | 29783.1 | 29802.2 | 29795.0 | 52.9 | 64 | up |  |
| 10-28 06:30 | 29802.3 | 29834.7 | 29796.6 | 29834.3 | 29798.5 | 58.6 | 64 | up |  |

## my_ema_rsi_15m · SHORT · entered 10-28 09:45 → exited 10-28 10:05 · stop · R 0.165 (best 1.05)

Logged entry reason: `my_ema_rsi_15m: 15min close 29743.40 < EMA21 29789.37, RSI 41.5, CHOP 60, Supertrend down`

Signal candle: **10-28 09:30** (15min); the trade opened right after it closed at 09:45.

| Measure | Value |
|---|---|
| close | 29743.40 |
| ema21 | 29789.37 |
| beyond EMA21 (ATR) | 1.15 |
| candles on this side of EMA21 (1 = this one just crossed) | 5 |
| RSI | 41.48 |
| RSI before | 50.35 |
| CHOP | 59.92 |
| EMA21 side changes in last 12 candles | 5 |
| Supertrend | -1 |
| last 3 closes | ↑↑↓ |
| signal candle body / range | 0.55 |
| signal candle range (ATR) | 2.27 |
| move since the 20-candle extreme (ATR) | 2.44 |
| closed beyond the prior 10-candle extreme | True |
| ADX(14) | 11.25 |
| EMA9 beyond EMA21 in the trade direction (ATR) | 0.19 |
| EMA9/21 crossed this many candles ago | 5 |
| EMA9/21 crosses in the last 20 candles | 1 |
| EMA21 slope over 8 candles in the trade direction (ATR) | 0.25 |
| RSI change over 3 candles | -3.13 |

Higher timeframes at that moment: 1h: close above EMA21, EMA21 > EMA50, RSI 61, Supertrend up → **AGAINST the trade**; 4h: close above EMA21, EMA21 < EMA50, RSI 63, Supertrend up → **AGAINST the trade**

| Candle (opens, NY) | O | H | L | C | EMA21 | RSI | CHOP | ST | |
|---|---|---|---|---|---|---|---|---|---|
| 10-28 07:30 | 29781.8 | 29819.6 | 29778.2 | 29818.8 | 29799.3 | 54.7 | 67 | up |  |
| 10-28 07:45 | 29818.6 | 29833.4 | 29783.3 | 29785.0 | 29798.0 | 48.4 | 68 | up |  |
| 10-28 08:00 | 29785.1 | 29812.4 | 29765.6 | 29797.2 | 29797.9 | 50.6 | 69 | up |  |
| 10-28 08:15 | 29797.1 | 29810.0 | 29787.2 | 29800.3 | 29798.1 | 51.2 | 68 | up |  |
| 10-28 08:30 | 29800.2 | 29803.6 | 29773.1 | 29785.1 | 29796.9 | 48.2 | 70 | up |  |
| 10-28 08:45 | 29785.2 | 29788.6 | 29755.6 | 29765.4 | 29794.1 | 44.6 | 68 | up |  |
| 10-28 09:00 | 29765.3 | 29805.6 | 29760.8 | 29793.4 | 29794.0 | 50.3 | 69 | up |  |
| 10-28 09:15 | 29793.6 | 29799.7 | 29763.2 | 29793.6 | 29794.0 | 50.3 | 69 | up |  |
| 10-28 09:30 | 29793.3 | 29817.3 | 29726.2 | 29743.4 | 29789.4 | 41.5 | 60 | dn | **SIGNAL candle (closed → entry)** |
| 10-28 09:45 | 29743.2 | 29743.8 | 29635.6 | 29723.8 | 29783.4 | 38.6 | 43 | dn | ← exit decided on this close |
| 10-28 10:00 | 29723.2 | 29738.7 | 29658.2 | 29698.3 | 29775.7 | 35.2 | 46 | dn |  |
| 10-28 10:15 | 29698.6 | 29718.1 | 29664.0 | 29708.4 | 29769.6 | 37.6 | 48 | dn |  |

## my_ema_rsi_15m · SHORT · entered 10-28 12:00 → exited 10-28 12:55 · stop · R -1.0 (best 0.42)

Logged entry reason: `my_ema_rsi_15m: 15min close 29712.80 < EMA21 29740.75, RSI 43.7, CHOP 54, Supertrend down`

Signal candle: **10-28 11:45** (15min); the trade opened right after it closed at 12:00.

| Measure | Value |
|---|---|
| close | 29712.80 |
| ema21 | 29740.75 |
| beyond EMA21 (ATR) | 0.60 |
| candles on this side of EMA21 (1 = this one just crossed) | 14 |
| RSI | 43.73 |
| RSI before | 45.36 |
| CHOP | 53.91 |
| EMA21 side changes in last 12 candles | 0 |
| Supertrend | -1 |
| last 3 closes | ↓↑↓ |
| signal candle body / range | 0.27 |
| signal candle range (ATR) | 0.92 |
| move since the 20-candle extreme (ATR) | 2.57 |
| closed beyond the prior 10-candle extreme | False |
| ADX(14) | 23.44 |
| EMA9 beyond EMA21 in the trade direction (ATR) | 0.52 |
| EMA9/21 crossed this many candles ago | 14 |
| EMA9/21 crosses in the last 20 candles | 1 |
| EMA21 slope over 8 candles in the trade direction (ATR) | 0.91 |
| RSI change over 3 candles | 0.59 |

Higher timeframes at that moment: 1h: close above EMA21, EMA21 > EMA50, RSI 54, Supertrend up → **AGAINST the trade**; 4h: close above EMA21, EMA21 < EMA50, RSI 63, Supertrend up → **AGAINST the trade**

| Candle (opens, NY) | O | H | L | C | EMA21 | RSI | CHOP | ST | |
|---|---|---|---|---|---|---|---|---|---|
| 10-28 09:45 | 29743.2 | 29743.8 | 29635.6 | 29723.8 | 29783.4 | 38.6 | 43 | dn |  |
| 10-28 10:00 | 29723.2 | 29738.7 | 29658.2 | 29698.3 | 29775.7 | 35.2 | 46 | dn |  |
| 10-28 10:15 | 29698.6 | 29718.1 | 29664.0 | 29708.4 | 29769.6 | 37.6 | 48 | dn |  |
| 10-28 10:30 | 29709.1 | 29728.7 | 29671.6 | 29688.1 | 29762.2 | 34.8 | 49 | dn |  |
| 10-28 10:45 | 29688.4 | 29700.2 | 29649.1 | 29669.6 | 29753.7 | 32.5 | 50 | dn |  |
| 10-28 11:00 | 29669.3 | 29725.1 | 29667.6 | 29717.8 | 29750.5 | 43.1 | 51 | dn |  |
| 10-28 11:15 | 29717.3 | 29726.3 | 29696.2 | 29696.2 | 29745.5 | 40.1 | 53 | dn |  |
| 10-28 11:30 | 29696.3 | 29728.3 | 29692.3 | 29723.6 | 29743.5 | 45.4 | 53 | dn |  |
| 10-28 11:45 | 29724.4 | 29734.1 | 29690.8 | 29712.8 | 29740.7 | 43.7 | 54 | dn | **SIGNAL candle (closed → entry)** |
| 10-28 12:00 | 29712.3 | 29730.7 | 29705.3 | 29713.5 | 29738.3 | 43.9 | 54 | dn | next candle (entry price) |
| 10-28 12:15 | 29713.2 | 29716.9 | 29695.2 | 29713.5 | 29736.0 | 43.9 | 53 | dn |  |
| 10-28 12:30 | 29713.6 | 29727.4 | 29705.8 | 29721.0 | 29734.7 | 45.6 | 52 | dn | ← exit decided on this close |
| 10-28 12:45 | 29720.9 | 29786.9 | 29700.5 | 29753.3 | 29736.3 | 52.3 | 54 | dn |  |
| 10-28 13:00 | 29753.0 | 29759.6 | 29713.5 | 29719.8 | 29734.8 | 45.9 | 59 | dn |  |

## my_ema_rsi_15m · LONG · entered 10-28 15:45 → exited 10-28 16:15 · trail_through · R 0.213 (best 1.75)

Logged entry reason: `my_ema_rsi_15m: 15min close 29783.00 > EMA21 29742.32, RSI 55.4, CHOP 61, Supertrend down`

Signal candle: **10-28 15:30** (15min); the trade opened right after it closed at 15:45.

| Measure | Value |
|---|---|
| close | 29783.00 |
| ema21 | 29742.32 |
| beyond EMA21 (ATR) | 0.56 |
| candles on this side of EMA21 (1 = this one just crossed) | 6 |
| RSI | 55.40 |
| RSI before | 50.37 |
| CHOP | 61.36 |
| EMA21 side changes in last 12 candles | 4 |
| Supertrend | -1 |
| last 3 closes | ↓↓↑ |
| signal candle body / range | 0.56 |
| signal candle range (ATR) | 0.97 |
| move since the 20-candle extreme (ATR) | 1.83 |
| closed beyond the prior 10-candle extreme | False |
| ADX(14) | 25.08 |
| EMA9 beyond EMA21 in the trade direction (ATR) | 0.12 |
| EMA9/21 crossed this many candles ago | 5 |
| EMA9/21 crosses in the last 20 candles | 1 |
| EMA21 slope over 8 candles in the trade direction (ATR) | 0.19 |
| RSI change over 3 candles | 1.15 |

Higher timeframes at that moment: 1h: close above EMA21, EMA21 > EMA50, RSI 59, Supertrend up → **with the trade**; 4h: close above EMA21, EMA21 < EMA50, RSI 63, Supertrend up → **with the trade**

| Candle (opens, NY) | O | H | L | C | EMA21 | RSI | CHOP | ST | |
|---|---|---|---|---|---|---|---|---|---|
| 10-28 13:30 | 29685.4 | 29716.9 | 29679.3 | 29707.8 | 29728.3 | 45.1 | 57 | dn |  |
| 10-28 13:45 | 29707.5 | 29741.2 | 29703.5 | 29731.1 | 29728.5 | 49.4 | 55 | dn |  |
| 10-28 14:00 | 29731.0 | 29779.8 | 29671.0 | 29686.3 | 29724.7 | 42.5 | 59 | dn |  |
| 10-28 14:15 | 29686.4 | 29734.8 | 29653.8 | 29727.3 | 29724.9 | 49.5 | 62 | dn |  |
| 10-28 14:30 | 29727.2 | 29875.6 | 29664.0 | 29813.8 | 29733.0 | 60.4 | 50 | dn |  |
| 10-28 14:45 | 29813.8 | 29834.4 | 29705.5 | 29771.8 | 29736.5 | 54.2 | 54 | dn |  |
| 10-28 15:00 | 29769.9 | 29838.2 | 29689.4 | 29750.3 | 29737.8 | 51.4 | 59 | dn |  |
| 10-28 15:15 | 29749.5 | 29769.8 | 29695.3 | 29742.8 | 29738.3 | 50.4 | 60 | dn |  |
| 10-28 15:30 | 29743.3 | 29791.8 | 29720.8 | 29783.0 | 29742.3 | 55.4 | 61 | dn | **SIGNAL candle (closed → entry)** |
| 10-28 15:45 | 29783.2 | 29868.8 | 29775.5 | 29859.5 | 29753.0 | 63.1 | 64 | up | next candle (entry price) |
| 10-28 16:00 | 29858.6 | 30045.0 | 29774.1 | 29774.9 | 29755.0 | 52.3 | 49 | up | ← exit decided on this close |
| 10-28 16:15 | 29774.8 | 29797.8 | 29643.4 | 29652.2 | 29745.6 | 41.4 | 50 | up |  |
| 10-28 16:30 | 29652.3 | 29673.2 | 29567.0 | 29596.3 | 29732.0 | 37.5 | 45 | dn |  |

## my_ema_rsi_1h · LONG · entered 10-28 13:00 → exited 10-28 13:55 · pre-news: Federal Funds Rate · R -0.15 (best 0.04)

Logged entry reason: `my_ema_rsi_1h: 1h close 29753.30 > EMA21 29712.37, RSI 57.7, CHOP 61, Supertrend up`

Signal candle: **10-28 12:00** (1h); the trade opened right after it closed at 13:00.

| Measure | Value |
|---|---|
| close | 29753.30 |
| ema21 | 29712.37 |
| beyond EMA21 (ATR) | 0.48 |
| candles on this side of EMA21 (1 = this one just crossed) | 2 |
| RSI | 57.74 |
| RSI before | 54.07 |
| CHOP | 61.01 |
| EMA21 side changes in last 12 candles | 2 |
| Supertrend | 1 |
| last 3 closes | ↓↑↑ |
| signal candle body / range | 0.45 |
| signal candle range (ATR) | 1.08 |
| move since the 20-candle extreme (ATR) | 1.38 |
| closed beyond the prior 10-candle extreme | False |
| ADX(14) | 35.68 |
| EMA9 beyond EMA21 in the trade direction (ATR) | 0.38 |
| EMA9/21 crossed this many candles ago | >19 |
| EMA9/21 crosses in the last 20 candles | 0 |
| EMA21 slope over 8 candles in the trade direction (ATR) | 0.47 |
| RSI change over 3 candles | 1.87 |

Higher timeframes at that moment: 1h: close above EMA21, EMA21 > EMA50, RSI 58, Supertrend up → **with the trade**; 4h: close above EMA21, EMA21 < EMA50, RSI 63, Supertrend up → **with the trade**

| Candle (opens, NY) | O | H | L | C | EMA21 | RSI | CHOP | ST | |
|---|---|---|---|---|---|---|---|---|---|
| 10-28 04:00 | 29841.4 | 29854.2 | 29778.6 | 29790.2 | 29672.3 | 66.6 | 54 | up |  |
| 10-28 05:00 | 29791.2 | 29816.6 | 29756.1 | 29815.1 | 29685.3 | 68.2 | 57 | up |  |
| 10-28 06:00 | 29815.2 | 29841.1 | 29757.0 | 29813.3 | 29696.9 | 67.9 | 57 | up |  |
| 10-28 07:00 | 29813.2 | 29833.4 | 29775.2 | 29785.0 | 29704.9 | 63.9 | 58 | up |  |
| 10-28 08:00 | 29785.1 | 29812.4 | 29755.6 | 29765.4 | 29710.4 | 61.2 | 62 | up |  |
| 10-28 09:00 | 29765.3 | 29817.3 | 29635.6 | 29723.8 | 29711.6 | 55.9 | 60 | up |  |
| 10-28 10:00 | 29723.2 | 29738.7 | 29649.1 | 29669.6 | 29707.8 | 49.7 | 61 | up |  |
| 10-28 11:00 | 29669.3 | 29734.1 | 29667.6 | 29712.8 | 29708.3 | 54.1 | 60 | up |  |
| 10-28 12:00 | 29712.3 | 29786.9 | 29695.2 | 29753.3 | 29712.4 | 57.7 | 61 | up | ← exit decided on this close |
| 10-28 13:00 | 29753.0 | 29759.6 | 29678.8 | 29731.1 | 29714.1 | 55.1 | 61 | up |  |
| 10-28 14:00 | 29731.0 | 29875.6 | 29653.8 | 29771.8 | 29719.3 | 58.8 | 63 | up |  |

## my_rsi_15m · SHORT · entered 10-22 16:45 → OPEN ·  · R - (best 0.00)

Logged entry reason: `my_rsi_15m: 15min close 28968.60 < EMA21 29041.31, RSI 38.9, CHOP 59, Supertrend down`

Signal candle: **10-22 16:30** (15min); the trade opened right after it closed at 16:45.

| Measure | Value |
|---|---|
| close | 28968.60 |
| ema21 | 29041.31 |
| beyond EMA21 (ATR) | 1.01 |
| candles on this side of EMA21 (1 = this one just crossed) | 27 |
| RSI | 38.89 |
| RSI before | 41.14 |
| CHOP | 58.60 |
| EMA21 side changes in last 12 candles | 0 |
| Supertrend | -1 |
| last 3 closes | ↑↓↓ |
| signal candle body / range | 0.84 |
| signal candle range (ATR) | 0.45 |
| move since the 20-candle extreme (ATR) | 3.61 |
| closed beyond the prior 10-candle extreme | False |
| ADX(14) | 36.44 |
| EMA9 beyond EMA21 in the trade direction (ATR) | 0.75 |
| EMA9/21 crossed this many candles ago | >19 |
| EMA9/21 crosses in the last 20 candles | 0 |
| EMA21 slope over 8 candles in the trade direction (ATR) | 1.06 |
| RSI change over 3 candles | -2.42 |

Higher timeframes at that moment: 1h: close below EMA21, EMA21 < EMA50, RSI 29, Supertrend down → **with the trade**; 4h: close below EMA21, EMA21 < EMA50, RSI 34, Supertrend down → **with the trade**

| Candle (opens, NY) | O | H | L | C | EMA21 | RSI | CHOP | ST | |
|---|---|---|---|---|---|---|---|---|---|
| 10-22 14:30 | 28974.0 | 28979.6 | 28940.6 | 28975.9 | 29117.3 | 29.4 | 51 | dn |  |
| 10-22 14:45 | 28975.8 | 28979.8 | 28927.0 | 28933.2 | 29100.6 | 26.7 | 46 | dn |  |
| 10-22 15:00 | 28932.8 | 28974.6 | 28905.3 | 28953.6 | 29087.2 | 30.0 | 43 | dn |  |
| 10-22 15:15 | 28953.4 | 29007.8 | 28947.4 | 29005.0 | 29079.7 | 37.7 | 42 | dn |  |
| 10-22 15:30 | 29004.9 | 29007.7 | 28899.8 | 28916.2 | 29064.9 | 31.3 | 43 | dn |  |
| 10-22 15:45 | 28916.2 | 29011.8 | 28886.9 | 28999.2 | 29058.9 | 41.3 | 49 | dn |  |
| 10-22 16:00 | 28998.4 | 29067.6 | 28967.6 | 29003.8 | 29053.9 | 41.8 | 62 | dn |  |
| 10-22 16:15 | 29003.6 | 29007.0 | 28982.2 | 28995.6 | 29048.6 | 41.1 | 59 | dn |  |
| 10-22 16:30 | 28995.7 | 28996.0 | 28963.9 | 28968.6 | 29041.3 | 38.9 | 59 | dn | **SIGNAL candle (closed → entry)** |
| 10-22 16:45 | 28969.0 | 28969.2 | 28930.2 | 28944.9 | 29032.5 | 37.0 | 58 | dn | next candle (entry price) |
| 10-22 18:00 | 28980.8 | 29001.7 | 28967.2 | 28989.8 | 29028.7 | 42.7 | 60 | dn |  |
| 10-22 18:15 | 28989.6 | 29018.4 | 28971.0 | 28990.0 | 29025.1 | 42.7 | 62 | dn |  |
| 10-22 18:30 | 28990.2 | 28990.2 | 28956.9 | 28973.5 | 29020.5 | 41.2 | 60 | dn |  |
| 10-22 18:45 | 28974.0 | 28992.2 | 28959.9 | 28976.2 | 29016.4 | 41.5 | 57 | dn |  |
| 10-22 19:00 | 28976.0 | 28982.7 | 28936.0 | 28947.2 | 29010.1 | 38.6 | 58 | dn |  |
| 10-22 19:15 | 28947.0 | 28951.3 | 28925.4 | 28930.6 | 29002.9 | 37.0 | 56 | dn |  |
| 10-22 19:30 | 28930.8 | 28935.7 | 28895.4 | 28921.0 | 28995.5 | 36.1 | 55 | dn |  |

## my_rsi_15m · LONG · entered 10-28 01:30 → exited 10-28 04:45 · close_past_ema21 · R 0.387 (best 0.98)

Logged entry reason: `my_rsi_15m: 15min close 29795.60 > EMA21 29753.03, RSI 63.2, CHOP 46, Supertrend up`

Signal candle: **10-28 01:15** (15min); the trade opened right after it closed at 01:30.

| Measure | Value |
|---|---|
| close | 29795.60 |
| ema21 | 29753.03 |
| beyond EMA21 (ATR) | 1.35 |
| candles on this side of EMA21 (1 = this one just crossed) | 57 |
| RSI | 63.20 |
| RSI before | 59.68 |
| CHOP | 45.55 |
| EMA21 side changes in last 12 candles | 0 |
| Supertrend | 1 |
| last 3 closes | ↓↑↑ |
| signal candle body / range | 0.82 |
| signal candle range (ATR) | 0.75 |
| move since the 20-candle extreme (ATR) | 4.02 |
| closed beyond the prior 10-candle extreme | False |
| ADX(14) | 27.01 |
| EMA9 beyond EMA21 in the trade direction (ATR) | 0.69 |
| EMA9/21 crossed this many candles ago | >19 |
| EMA9/21 crosses in the last 20 candles | 0 |
| EMA21 slope over 8 candles in the trade direction (ATR) | 1.03 |
| RSI change over 3 candles | 5.35 |

Higher timeframes at that moment: 1h: close above EMA21, EMA21 > EMA50, RSI 69, Supertrend up → **with the trade**; 4h: close above EMA21, EMA21 < EMA50, RSI 64, Supertrend up → **with the trade**

| Candle (opens, NY) | O | H | L | C | EMA21 | RSI | CHOP | ST | |
|---|---|---|---|---|---|---|---|---|---|
| 10-27 23:15 | 29775.8 | 29788.9 | 29767.3 | 29777.6 | 29720.5 | 65.0 | 56 | up |  |
| 10-27 23:30 | 29777.4 | 29790.8 | 29773.6 | 29787.2 | 29726.5 | 66.4 | 54 | up |  |
| 10-27 23:45 | 29787.1 | 29826.0 | 29786.4 | 29800.4 | 29733.2 | 68.2 | 44 | up |  |
| 10-28 00:00 | 29800.1 | 29807.4 | 29787.1 | 29796.2 | 29739.0 | 67.0 | 44 | up |  |
| 10-28 00:15 | 29796.1 | 29800.6 | 29776.3 | 29782.6 | 29742.9 | 62.9 | 43 | up |  |
| 10-28 00:30 | 29782.6 | 29786.4 | 29756.0 | 29764.6 | 29744.9 | 57.8 | 45 | up |  |
| 10-28 00:45 | 29765.1 | 29775.0 | 29754.3 | 29757.4 | 29746.0 | 55.9 | 47 | up |  |
| 10-28 01:00 | 29757.6 | 29776.8 | 29746.3 | 29776.1 | 29748.8 | 59.7 | 46 | up |  |
| 10-28 01:15 | 29776.2 | 29796.1 | 29772.3 | 29795.6 | 29753.0 | 63.2 | 46 | up | **SIGNAL candle (closed → entry)** |
| 10-28 01:30 | 29795.6 | 29796.1 | 29773.0 | 29781.2 | 29755.6 | 59.1 | 44 | up | next candle (entry price) |
| 10-28 01:45 | 29781.3 | 29790.6 | 29766.1 | 29778.6 | 29757.7 | 58.4 | 47 | up |  |
| 10-28 02:00 | 29779.2 | 29818.1 | 29776.8 | 29808.6 | 29762.3 | 63.9 | 56 | up |  |
| 10-28 02:15 | 29808.8 | 29818.4 | 29793.6 | 29796.0 | 29765.4 | 60.3 | 55 | up |  |
| 10-28 02:30 | 29795.8 | 29829.3 | 29795.0 | 29822.4 | 29770.6 | 64.8 | 57 | up |  |
| 10-28 02:45 | 29822.6 | 29827.3 | 29808.6 | 29816.6 | 29774.7 | 63.1 | 57 | up |  |
| 10-28 03:00 | 29815.6 | 29851.7 | 29807.1 | 29846.3 | 29781.2 | 67.8 | 51 | up |  |
| 10-28 03:15 | 29846.0 | 29846.3 | 29822.8 | 29828.4 | 29785.5 | 62.6 | 49 | up |  |
| 10-28 03:30 | 29828.3 | 29836.6 | 29801.6 | 29808.3 | 29787.6 | 57.4 | 50 | up |  |
| 10-28 03:45 | 29808.2 | 29843.6 | 29769.3 | 29841.2 | 29792.5 | 62.9 | 55 | up |  |
| 10-28 04:00 | 29841.4 | 29854.2 | 29817.4 | 29827.4 | 29795.7 | 59.4 | 55 | up |  |
| 10-28 04:15 | 29827.1 | 29841.4 | 29803.3 | 29811.2 | 29797.1 | 55.5 | 56 | up |  |
| 10-28 04:30 | 29811.8 | 29812.8 | 29781.4 | 29795.0 | 29796.9 | 51.9 | 64 | up | ← exit decided on this close |
| 10-28 04:45 | 29794.6 | 29809.1 | 29778.6 | 29790.2 | 29796.3 | 50.8 | 64 | up |  |
| 10-28 05:00 | 29791.2 | 29793.4 | 29777.1 | 29787.0 | 29795.4 | 50.1 | 64 | up |  |

## Every logged signal on NDQ in the window (taken and skipped)

| Time (NY) | Book | What happened | Why |
|---|---|---|---|
| 10-28 01:30 | my_rsi_15m | taken | qty 5.98, jev 0.4475 |
| 10-28 06:00 | my_ema_rsi_15m | taken | qty 5.17, jev 0.485 |
| 10-28 06:45 | my_ema_rsi_15m | rejected | choppy market (CHOP 63.9 ≥ 61.8) |
| 10-28 08:45 | my_ema_cross_15m | rejected | choppy market (CHOP 69.5 ≥ 61.8) |
| 10-28 09:45 | my_ema_rsi_15m | taken | qty 3.49, jev 0.2825 |
| 10-28 12:00 | my_ema_rsi_15m | taken | qty 9.11, jev 0.4325 |
| 10-28 13:00 | my_ema_rsi_1h | taken | qty 2.48, jev 0.27 |
| 10-28 13:30 | my_ema_rsi_15m | rejected | news blackout: Federal Funds Rate |
| 10-28 14:15 | my_ema_rsi_15m | rejected | news blackout: Federal Funds Rate |
| 10-28 14:45 | my_ema_cross_15m | rejected | trading halted: daily loss limit hit ($-1,941) |
| 10-28 14:45 | my_ema_rsi_15m | rejected | news blackout: FOMC Press Conference |
| 10-28 15:45 | my_ema_rsi_15m | taken | qty 2.37, jev 0.275 |
| 10-28 16:00 | my_rsi_15m | rejected | choppy market (CHOP 63.7 ≥ 61.8) |
| 10-28 16:30 | my_ema_rsi_15m | rejected | stop too wide (4.5 ATR) |
| 10-28 16:45 | my_ema_cross_15m | rejected | stop too wide (5.0 ATR) |
| 10-28 19:00 | my_ema_cross_1h | rejected | stop too wide (4.1 ATR) |
| 10-28 19:00 | my_ema_rsi_1h | rejected | stop too wide (4.1 ATR) |
| 10-28 21:15 | my_ema_rsi_15m | rejected | choppy market (CHOP 66.0 ≥ 61.8) |
