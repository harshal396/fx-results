# Context for US30 - generated 2026-10-28 23:25 New York

Candles are labelled by their OPEN time, like TradingView. The **signal candle** is the one that closed when the bot entered; the trade opened at the open of the next candle. Prices are OANDA mid prices.


## Gate check for US30: would the new rules have blocked these trades?

Applied with each book's installed settings (15m/1h books: chop 58.5 + fresh cross + RSI direction + trend gate; 4h: chop + trend gate + oversized candle; daily: chop only; his EMA21+RSI55 book: chop only). 'not covered' = Playbook, Practice, momentum and other books the rules do not touch.

| Opened (NY) | Book | Side | Result | How it ended | Verdict | Reasons |
|---|---|---|---|---|---|---|
| 10-22 09:00 | my_ema_rsi_4h | long | open |  | kept |  |
| 10-22 12:00 | my_ema_rsi_1h | long | open |  | **BLOCKED** | not a fresh cross (price on this side of the EMA21 for 3 candles, limit 2) |
| 10-22 13:00 | my_rsi_4h | long | open |  | kept |  |
| 10-22 15:30 | my_ema_rsi_15m | long | open |  | **BLOCKED** | US30 is no longer traded by the 15m books; choppy (CHOP 59.5 >= 58.5) |
| 10-22 16:00 | my_rsi_15m | long | open |  | **BLOCKED** | the RSI 60/40 15m book is retired; choppy (CHOP 60.8 >= 58.5); not a fresh cross (price on this side of the EMA21 for 4 candles, limit 2) |
| 10-22 16:00 | my_rsi_1h | long | open |  | **BLOCKED** | not a fresh cross (price on this side of the EMA21 for 7 candles, limit 2) |
| 10-28 04:15 | ema21_rsi55 | short | -0.36R | close_above_ema21 | kept | his book: chop cutoff only |
| 10-28 11:00 | my_ema_cross_1h | long | +0.10R | stop | **BLOCKED** | not a fresh cross (price on this side of the EMA21 for 3 candles, limit 2) |
| 10-28 15:15 | my_ema_rsi_15m | short | -0.36R | close_past_ema21 | **BLOCKED** | US30 is no longer traded by the 15m books; against the 1h trend (bullish) |
| 10-28 16:00 | my_ema_rsi_15m | long | +0.17R | trail_through | **BLOCKED** | US30 is no longer traded by the 15m books |
| 10-28 16:00 | my_ema_rsi_1h | long | open |  | **BLOCKED** | not a fresh cross (price on this side of the EMA21 for 8 candles, limit 2); RSI not rising for a buy (RSI 60, 65 three candles ago) |
| 10-28 17:00 | my_ema_cross_4h | long | open |  | **BLOCKED** | choppy (CHOP 61.6 >= 58.5) |
| 10-28 17:00 | my_ema_rsi_1d | long | open |  | **BLOCKED** | choppy (CHOP 59.1 >= 58.5) |
| 10-28 19:15 | my_ema_rsi_15m | long | -0.58R | close_past_ema21 | **BLOCKED** | US30 is no longer traded by the 15m books; not a fresh cross (price on this side of the EMA21 for 11 candles, limit 2) |
| 10-28 20:15 | my_ema_rsi_15m | long | open |  | **BLOCKED** | US30 is no longer traded by the 15m books; RSI not rising for a buy (RSI 56, 56 three candles ago) |

**Summary US30:** 15 EMA/RSI trades checked, **12 blocked**, 3 kept; closed R of the blocked ones -0.67R (4 closed), of the kept ones -0.36R (1 closed); 0 trades from books the rules do not touch.


## ema21_rsi55 · SHORT · entered 10-28 04:15 → exited 10-28 04:45 · close_above_ema21 · R -0.365 (best 0.12)

Logged entry reason: `EMA21+RSI45 short: 15m close 52291.70 < EMA21 52312.67, RSI 44.4`

Signal candle: **10-28 04:00** (15min); the trade opened right after it closed at 04:15.

| Measure | Value |
|---|---|
| close | 52291.70 |
| ema21 | 52312.67 |
| beyond EMA21 (ATR) | 0.60 |
| candles on this side of EMA21 (1 = this one just crossed) | 1 |
| RSI | 44.39 |
| RSI before | 54.22 |
| CHOP | 57.99 |
| EMA21 side changes in last 12 candles | 2 |
| Supertrend | 1 |
| last 3 closes | ↓↑↓ |
| signal candle body / range | 0.86 |
| signal candle range (ATR) | 1.68 |
| move since the 20-candle extreme (ATR) | 1.68 |
| closed beyond the prior 10-candle extreme | False |
| ADX(14) | 23.84 |
| EMA9 beyond EMA21 in the trade direction (ATR) | 0.37 |
| EMA9/21 crossed this many candles ago | >19 |
| EMA9/21 crosses in the last 20 candles | 0 |
| EMA21 slope over 8 candles in the trade direction (ATR) | 0.63 |
| RSI change over 3 candles | 2.20 |

Higher timeframes at that moment: 1h: close below EMA21, EMA21 < EMA50, RSI 46, Supertrend down → **with the trade**; 4h: close below EMA21, EMA21 > EMA50, RSI 45, Supertrend up → **with the trade**

| Candle (opens, NY) | O | H | L | C | EMA21 | RSI | CHOP | ST | |
|---|---|---|---|---|---|---|---|---|---|
| 10-28 02:00 | 52301.2 | 52307.2 | 52279.7 | 52292.2 | 52334.8 | 35.1 | 48 | dn |  |
| 10-28 02:15 | 52291.7 | 52292.2 | 52262.2 | 52266.2 | 52328.6 | 30.6 | 42 | dn |  |
| 10-28 02:30 | 52267.7 | 52280.7 | 52244.2 | 52279.2 | 52324.1 | 35.1 | 37 | dn |  |
| 10-28 02:45 | 52279.7 | 52282.2 | 52264.2 | 52271.2 | 52319.3 | 33.6 | 39 | dn |  |
| 10-28 03:00 | 52269.7 | 52310.2 | 52257.2 | 52296.2 | 52317.2 | 41.7 | 43 | dn |  |
| 10-28 03:15 | 52294.2 | 52300.2 | 52279.2 | 52297.7 | 52315.4 | 42.2 | 43 | dn |  |
| 10-28 03:30 | 52297.2 | 52306.7 | 52270.2 | 52277.2 | 52311.9 | 37.8 | 46 | dn |  |
| 10-28 03:45 | 52276.7 | 52344.2 | 52256.7 | 52343.2 | 52314.8 | 54.2 | 54 | up |  |
| 10-28 04:00 | 52342.7 | 52343.2 | 52284.2 | 52291.7 | 52312.7 | 44.4 | 58 | up | **SIGNAL candle (closed → entry)** |
| 10-28 04:15 | 52290.2 | 52314.7 | 52281.7 | 52307.2 | 52312.2 | 47.5 | 59 | up | next candle (entry price) |
| 10-28 04:30 | 52307.7 | 52327.7 | 52277.2 | 52327.2 | 52313.5 | 51.2 | 62 | up | ← exit decided on this close |
| 10-28 04:45 | 52326.7 | 52351.2 | 52308.2 | 52335.2 | 52315.5 | 52.7 | 61 | up |  |
| 10-28 05:00 | 52337.2 | 52345.2 | 52317.2 | 52332.2 | 52317.0 | 52.1 | 62 | up |  |

## my_ema_cross_1h · LONG · entered 10-28 11:00 → exited 10-28 14:01 · stop · R 0.1 (best 0.78)

Logged entry reason: `my_ema_cross_1h: 1h close 52480.80 > EMA21 52383.58, RSI 58.4, CHOP 52, Supertrend down`

Signal candle: **10-28 10:00** (1h); the trade opened right after it closed at 11:00.

| Measure | Value |
|---|---|
| close | 52480.80 |
| ema21 | 52383.58 |
| beyond EMA21 (ATR) | 1.00 |
| candles on this side of EMA21 (1 = this one just crossed) | 3 |
| RSI | 58.43 |
| RSI before | 58.22 |
| CHOP | 51.54 |
| EMA21 side changes in last 12 candles | 1 |
| Supertrend | -1 |
| last 3 closes | ↑↑↑ |
| signal candle body / range | 0.02 |
| signal candle range (ATR) | 1.29 |
| move since the 20-candle extreme (ATR) | 2.44 |
| closed beyond the prior 10-candle extreme | False |
| ADX(14) | 15.06 |
| EMA9 beyond EMA21 in the trade direction (ATR) | 0.11 |
| EMA9/21 crossed this many candles ago | 1 |
| EMA9/21 crosses in the last 20 candles | 1 |
| EMA21 slope over 8 candles in the trade direction (ATR) | 0.07 |
| RSI change over 3 candles | 16.27 |

Higher timeframes at that moment: 1h: close above EMA21, EMA21 < EMA50, RSI 58, Supertrend down → **with the trade**; 4h: close above EMA21, EMA21 > EMA50, RSI 51, Supertrend up → **with the trade**

| Candle (opens, NY) | O | H | L | C | EMA21 | RSI | CHOP | ST | |
|---|---|---|---|---|---|---|---|---|---|
| 10-28 02:00 | 52301.2 | 52307.2 | 52244.2 | 52271.2 | 52376.8 | 39.1 | 50 | dn |  |
| 10-28 03:00 | 52269.7 | 52344.2 | 52256.7 | 52343.2 | 52373.7 | 46.3 | 50 | dn |  |
| 10-28 04:00 | 52342.7 | 52351.2 | 52277.2 | 52335.2 | 52370.2 | 45.7 | 48 | dn |  |
| 10-28 05:00 | 52337.2 | 52357.7 | 52299.7 | 52354.2 | 52368.8 | 47.6 | 49 | dn |  |
| 10-28 06:00 | 52353.7 | 52356.2 | 52256.7 | 52296.7 | 52362.2 | 42.8 | 49 | dn |  |
| 10-28 07:00 | 52297.2 | 52362.7 | 52282.2 | 52289.2 | 52355.6 | 42.2 | 52 | dn |  |
| 10-28 08:00 | 52288.7 | 52465.2 | 52282.2 | 52442.2 | 52363.5 | 55.8 | 58 | dn |  |
| 10-28 09:00 | 52442.7 | 52526.8 | 52371.2 | 52477.8 | 52373.9 | 58.2 | 54 | dn |  |
| 10-28 10:00 | 52478.2 | 52566.8 | 52441.8 | 52480.8 | 52383.6 | 58.4 | 52 | dn | **SIGNAL candle (closed → entry)** |
| 10-28 11:00 | 52479.2 | 52586.8 | 52454.8 | 52566.8 | 52400.2 | 64.0 | 49 | up | next candle (entry price) |
| 10-28 12:00 | 52566.2 | 52676.6 | 52512.6 | 52585.2 | 52417.0 | 65.1 | 42 | up |  |
| 10-28 13:00 | 52585.6 | 52587.2 | 52522.2 | 52561.2 | 52430.2 | 62.5 | 43 | up | ← exit decided on this close |
| 10-28 14:00 | 52559.6 | 52645.2 | 52406.6 | 52455.6 | 52432.5 | 52.4 | 48 | up |  |
| 10-28 15:00 | 52456.2 | 52578.2 | 52373.2 | 52568.6 | 52444.8 | 59.9 | 53 | up |  |

## my_ema_cross_4h · LONG · entered 10-28 17:00 → OPEN ·  · R - (best 0.00)

Logged entry reason: `my_ema_cross_4h: 4h close 52614.60 > EMA21 52460.36, RSI 57.5, CHOP 62, Supertrend up`

Signal candle: **10-28 13:00** (4h); the trade opened right after it closed at 17:00.

| Measure | Value |
|---|---|
| close | 52614.60 |
| ema21 | 52460.36 |
| beyond EMA21 (ATR) | 0.71 |
| candles on this side of EMA21 (1 = this one just crossed) | 3 |
| RSI | 57.48 |
| RSI before | 56.39 |
| CHOP | 61.60 |
| EMA21 side changes in last 12 candles | 5 |
| Supertrend | 1 |
| last 3 closes | ↑↑↑ |
| signal candle body / range | 0.07 |
| signal candle range (ATR) | 2.01 |
| move since the 20-candle extreme (ATR) | 2.53 |
| closed beyond the prior 10-candle extreme | False |
| ADX(14) | 15.16 |
| EMA9 beyond EMA21 in the trade direction (ATR) | 0.07 |
| EMA9/21 crossed this many candles ago | 1 |
| EMA9/21 crosses in the last 20 candles | 2 |
| EMA21 slope over 8 candles in the trade direction (ATR) | -0.03 |
| RSI change over 3 candles | 11.74 |

Higher timeframes at that moment: 1h: close above EMA21, EMA21 > EMA50, RSI 62, Supertrend up → **with the trade**; 4h: close above EMA21, EMA21 > EMA50, RSI 57, Supertrend up → **with the trade**

| Candle (opens, NY) | O | H | L | C | EMA21 | RSI | CHOP | ST | |
|---|---|---|---|---|---|---|---|---|---|
| 10-27 05:00 | 52435.5 | 52627.0 | 52383.0 | 52504.0 | 52465.9 | 52.2 | 51 | up |  |
| 10-27 09:00 | 52502.5 | 52515.8 | 52261.6 | 52363.8 | 52456.6 | 46.7 | 59 | up |  |
| 10-27 13:00 | 52365.2 | 52497.7 | 52341.8 | 52426.7 | 52453.9 | 49.3 | 60 | up |  |
| 10-27 17:00 | 52430.7 | 52477.7 | 52402.2 | 52421.7 | 52451.0 | 49.1 | 65 | up |  |
| 10-27 21:00 | 52422.2 | 52430.2 | 52267.7 | 52321.7 | 52439.2 | 45.1 | 66 | up |  |
| 10-28 01:00 | 52321.2 | 52351.2 | 52244.2 | 52335.2 | 52429.8 | 45.7 | 65 | up |  |
| 10-28 05:00 | 52337.2 | 52465.2 | 52256.7 | 52442.2 | 52430.9 | 50.7 | 69 | up |  |
| 10-28 09:00 | 52442.7 | 52676.6 | 52371.2 | 52585.2 | 52444.9 | 56.4 | 68 | up |  |
| 10-28 13:00 | 52585.6 | 52812.6 | 52373.2 | 52614.6 | 52460.4 | 57.5 | 62 | up | **SIGNAL candle (closed → entry)** |
| 10-28 17:00 | 52584.6 | 52638.1 | 52510.6 | 52603.1 | 52473.3 | 56.9 | 59 | up | next candle (entry price) |
| 10-28 21:00 | 52603.6 | 52778.6 | 52603.1 | 52710.1 | 52494.9 | 61.0 | 59 | up |  |

## my_ema_rsi_15m · LONG · entered 10-22 15:30 → OPEN ·  · R - (best 0.00)

Logged entry reason: `my_ema_rsi_15m: 15min close 52851.00 > EMA21 52781.32, RSI 57.8, CHOP 59, Supertrend up`

Signal candle: **10-22 15:15** (15min); the trade opened right after it closed at 15:30.

| Measure | Value |
|---|---|
| close | 52851.00 |
| ema21 | 52781.32 |
| beyond EMA21 (ATR) | 0.81 |
| candles on this side of EMA21 (1 = this one just crossed) | 2 |
| RSI | 57.75 |
| RSI before | 53.94 |
| CHOP | 59.47 |
| EMA21 side changes in last 12 candles | 2 |
| Supertrend | 1 |
| last 3 closes | ↓↑↑ |
| signal candle body / range | 0.75 |
| signal candle range (ATR) | 0.75 |
| move since the 20-candle extreme (ATR) | 3.68 |
| closed beyond the prior 10-candle extreme | False |
| ADX(14) | 19.25 |
| EMA9 beyond EMA21 in the trade direction (ATR) | 0.32 |
| EMA9/21 crossed this many candles ago | >19 |
| EMA9/21 crosses in the last 20 candles | 0 |
| EMA21 slope over 8 candles in the trade direction (ATR) | 0.36 |
| RSI change over 3 candles | 5.03 |

Higher timeframes at that moment: 1h: close above EMA21, EMA21 > EMA50, RSI 55, Supertrend up → **with the trade**; 4h: close above EMA21, EMA21 > EMA50, RSI 62, Supertrend up → **with the trade**

| Candle (opens, NY) | O | H | L | C | EMA21 | RSI | CHOP | ST | |
|---|---|---|---|---|---|---|---|---|---|
| 10-22 13:15 | 52765.0 | 52831.4 | 52757.0 | 52823.0 | 52749.9 | 56.2 | 49 | up |  |
| 10-22 13:30 | 52822.4 | 52868.4 | 52813.0 | 52840.4 | 52758.1 | 57.2 | 48 | up |  |
| 10-22 13:45 | 52840.0 | 52841.0 | 52776.4 | 52806.0 | 52762.4 | 54.5 | 44 | up |  |
| 10-22 14:00 | 52806.4 | 52834.0 | 52714.0 | 52812.4 | 52767.0 | 54.9 | 47 | up |  |
| 10-22 14:15 | 52813.0 | 52885.4 | 52784.4 | 52802.0 | 52770.2 | 54.1 | 55 | up |  |
| 10-22 14:30 | 52800.0 | 52800.0 | 52757.4 | 52786.4 | 52771.6 | 52.7 | 58 | up |  |
| 10-22 14:45 | 52786.0 | 52811.0 | 52766.0 | 52771.0 | 52771.6 | 51.4 | 60 | up |  |
| 10-22 15:00 | 52770.4 | 52841.4 | 52741.0 | 52802.0 | 52774.4 | 53.9 | 61 | up |  |
| 10-22 15:15 | 52802.4 | 52860.0 | 52795.0 | 52851.0 | 52781.3 | 57.8 | 59 | up | **SIGNAL candle (closed → entry)** |
| 10-22 15:30 | 52849.0 | 52867.0 | 52823.4 | 52848.0 | 52787.4 | 57.4 | 59 | up | next candle (entry price) |
| 10-22 15:45 | 52847.4 | 52932.0 | 52812.0 | 52911.0 | 52798.6 | 62.1 | 61 | up |  |
| 10-22 16:00 | 52910.4 | 52960.9 | 52887.9 | 52894.4 | 52807.3 | 60.2 | 57 | up |  |
| 10-22 16:15 | 52894.9 | 52927.9 | 52876.9 | 52918.9 | 52817.5 | 62.0 | 56 | up |  |
| 10-22 16:30 | 52919.4 | 52923.9 | 52903.9 | 52919.9 | 52826.8 | 62.1 | 52 | up |  |
| 10-22 16:45 | 52921.4 | 52928.9 | 52909.9 | 52916.4 | 52834.9 | 61.7 | 50 | up |  |
| 10-22 18:00 | 52926.4 | 52946.9 | 52917.9 | 52937.4 | 52844.2 | 63.4 | 49 | up |  |
| 10-22 18:15 | 52936.9 | 52978.9 | 52930.4 | 52973.4 | 52856.0 | 66.3 | 46 | up |  |

## my_ema_rsi_15m · SHORT · entered 10-28 15:15 → exited 10-28 15:45 · close_past_ema21 · R -0.361 (best 0.23)

Logged entry reason: `my_ema_rsi_15m: 15min close 52436.60 < EMA21 52498.99, RSI 44.0, CHOP 54, Supertrend up`

Signal candle: **10-28 15:00** (15min); the trade opened right after it closed at 15:15.

| Measure | Value |
|---|---|
| close | 52436.60 |
| ema21 | 52498.99 |
| beyond EMA21 (ATR) | 0.68 |
| candles on this side of EMA21 (1 = this one just crossed) | 2 |
| RSI | 43.98 |
| RSI before | 45.86 |
| CHOP | 54.29 |
| EMA21 side changes in last 12 candles | 3 |
| Supertrend | 1 |
| last 3 closes | ↑↓↓ |
| signal candle body / range | 0.10 |
| signal candle range (ATR) | 2.08 |
| move since the 20-candle extreme (ATR) | 2.63 |
| closed beyond the prior 10-candle extreme | False |
| ADX(14) | 37.19 |
| EMA9 beyond EMA21 in the trade direction (ATR) | -0.02 |
| EMA9/21 crossed this many candles ago | >19 |
| EMA9/21 crosses in the last 20 candles | 0 |
| EMA21 slope over 8 candles in the trade direction (ATR) | -0.03 |
| RSI change over 3 candles | -6.06 |

Higher timeframes at that moment: 1h: close above EMA21, EMA21 > EMA50, RSI 52, Supertrend up → **AGAINST the trade**; 4h: close above EMA21, EMA21 > EMA50, RSI 56, Supertrend up → **AGAINST the trade**

| Candle (opens, NY) | O | H | L | C | EMA21 | RSI | CHOP | ST | |
|---|---|---|---|---|---|---|---|---|---|
| 10-28 13:00 | 52585.6 | 52587.2 | 52542.2 | 52551.6 | 52496.1 | 60.7 | 49 | up |  |
| 10-28 13:15 | 52551.2 | 52554.2 | 52527.2 | 52549.2 | 52500.9 | 60.3 | 51 | up |  |
| 10-28 13:30 | 52549.6 | 52564.2 | 52523.6 | 52525.2 | 52503.1 | 56.2 | 50 | up |  |
| 10-28 13:45 | 52525.6 | 52572.6 | 52522.2 | 52561.2 | 52508.4 | 60.5 | 48 | up |  |
| 10-28 14:00 | 52559.6 | 52607.6 | 52472.2 | 52499.6 | 52507.6 | 51.2 | 51 | up |  |
| 10-28 14:15 | 52498.2 | 52505.2 | 52445.6 | 52491.2 | 52506.1 | 50.0 | 50 | up |  |
| 10-28 14:30 | 52491.6 | 52645.2 | 52424.2 | 52551.2 | 52510.2 | 57.3 | 53 | up |  |
| 10-28 14:45 | 52551.6 | 52601.6 | 52406.6 | 52455.6 | 52505.2 | 45.9 | 55 | up |  |
| 10-28 15:00 | 52456.2 | 52562.6 | 52373.2 | 52436.6 | 52499.0 | 44.0 | 54 | up | **SIGNAL candle (closed → entry)** |
| 10-28 15:15 | 52436.2 | 52489.6 | 52380.6 | 52475.2 | 52496.8 | 48.6 | 56 | up | next candle (entry price) |
| 10-28 15:30 | 52475.6 | 52540.2 | 52462.2 | 52517.6 | 52498.7 | 53.2 | 57 | up | ← exit decided on this close |
| 10-28 15:45 | 52518.2 | 52578.2 | 52501.6 | 52568.6 | 52505.1 | 58.0 | 58 | up |  |
| 10-28 16:00 | 52568.2 | 52812.6 | 52568.1 | 52609.1 | 52514.5 | 61.4 | 49 | up |  |

## my_ema_rsi_15m · LONG · entered 10-28 16:00 → exited 10-28 16:15 · trail_through · R 0.171 (best 1.10)

Logged entry reason: `my_ema_rsi_15m: 15min close 52568.60 > EMA21 52505.07, RSI 58.0, CHOP 58, Supertrend up`

Signal candle: **10-28 15:45** (15min); the trade opened right after it closed at 16:00.

| Measure | Value |
|---|---|
| close | 52568.60 |
| ema21 | 52505.07 |
| beyond EMA21 (ATR) | 0.70 |
| candles on this side of EMA21 (1 = this one just crossed) | 2 |
| RSI | 57.99 |
| RSI before | 53.16 |
| CHOP | 57.54 |
| EMA21 side changes in last 12 candles | 4 |
| Supertrend | 1 |
| last 3 closes | ↑↑↑ |
| signal candle body / range | 0.66 |
| signal candle range (ATR) | 0.85 |
| move since the 20-candle extreme (ATR) | 2.16 |
| closed beyond the prior 10-candle extreme | False |
| ADX(14) | 36.88 |
| EMA9 beyond EMA21 in the trade direction (ATR) | 0.10 |
| EMA9/21 crossed this many candles ago | 2 |
| EMA9/21 crosses in the last 20 candles | 2 |
| EMA21 slope over 8 candles in the trade direction (ATR) | -0.04 |
| RSI change over 3 candles | 14.01 |

Higher timeframes at that moment: 1h: close above EMA21, EMA21 > EMA50, RSI 60, Supertrend up → **with the trade**; 4h: close above EMA21, EMA21 > EMA50, RSI 56, Supertrend up → **with the trade**

| Candle (opens, NY) | O | H | L | C | EMA21 | RSI | CHOP | ST | |
|---|---|---|---|---|---|---|---|---|---|
| 10-28 13:45 | 52525.6 | 52572.6 | 52522.2 | 52561.2 | 52508.4 | 60.5 | 48 | up |  |
| 10-28 14:00 | 52559.6 | 52607.6 | 52472.2 | 52499.6 | 52507.6 | 51.2 | 51 | up |  |
| 10-28 14:15 | 52498.2 | 52505.2 | 52445.6 | 52491.2 | 52506.1 | 50.0 | 50 | up |  |
| 10-28 14:30 | 52491.6 | 52645.2 | 52424.2 | 52551.2 | 52510.2 | 57.3 | 53 | up |  |
| 10-28 14:45 | 52551.6 | 52601.6 | 52406.6 | 52455.6 | 52505.2 | 45.9 | 55 | up |  |
| 10-28 15:00 | 52456.2 | 52562.6 | 52373.2 | 52436.6 | 52499.0 | 44.0 | 54 | up |  |
| 10-28 15:15 | 52436.2 | 52489.6 | 52380.6 | 52475.2 | 52496.8 | 48.6 | 56 | up |  |
| 10-28 15:30 | 52475.6 | 52540.2 | 52462.2 | 52517.6 | 52498.7 | 53.2 | 57 | up |  |
| 10-28 15:45 | 52518.2 | 52578.2 | 52501.6 | 52568.6 | 52505.1 | 58.0 | 58 | up | **SIGNAL candle (closed → entry)** |
| 10-28 16:00 | 52568.2 | 52812.6 | 52568.1 | 52609.1 | 52514.5 | 61.4 | 49 | up | ← exit decided on this close |
| 10-28 16:15 | 52607.6 | 52636.1 | 52588.1 | 52616.1 | 52523.8 | 62.0 | 47 | up |  |
| 10-28 16:30 | 52617.6 | 52647.1 | 52610.6 | 52637.6 | 52534.1 | 63.7 | 47 | up |  |

## my_ema_rsi_15m · LONG · entered 10-28 19:15 → exited 10-28 19:45 · close_past_ema21 · R -0.576 (best 0.16)

Logged entry reason: `my_ema_rsi_15m: 15min close 52586.60 > EMA21 52551.03, RSI 56.4, CHOP 41, Supertrend up`

Signal candle: **10-28 19:00** (15min); the trade opened right after it closed at 19:15.

| Measure | Value |
|---|---|
| close | 52586.60 |
| ema21 | 52551.03 |
| beyond EMA21 (ATR) | 0.45 |
| candles on this side of EMA21 (1 = this one just crossed) | 11 |
| RSI | 56.43 |
| RSI before | 54.17 |
| CHOP | 41.13 |
| EMA21 side changes in last 12 candles | 1 |
| Supertrend | 1 |
| last 3 closes | ↓↑↑ |
| signal candle body / range | 0.38 |
| signal candle range (ATR) | 0.63 |
| move since the 20-candle extreme (ATR) | 2.71 |
| closed beyond the prior 10-candle extreme | False |
| ADX(14) | 41.62 |
| EMA9 beyond EMA21 in the trade direction (ATR) | 0.25 |
| EMA9/21 crossed this many candles ago | 11 |
| EMA9/21 crosses in the last 20 candles | 2 |
| EMA21 slope over 8 candles in the trade direction (ATR) | 0.46 |
| RSI change over 3 candles | 3.95 |

Higher timeframes at that moment: 1h: close above EMA21, EMA21 > EMA50, RSI 58, Supertrend up → **with the trade**; 4h: close above EMA21, EMA21 > EMA50, RSI 57, Supertrend up → **with the trade**

| Candle (opens, NY) | O | H | L | C | EMA21 | RSI | CHOP | ST | |
|---|---|---|---|---|---|---|---|---|---|
| 10-28 16:00 | 52568.2 | 52812.6 | 52568.1 | 52609.1 | 52514.5 | 61.4 | 49 | up |  |
| 10-28 16:15 | 52607.6 | 52636.1 | 52588.1 | 52616.1 | 52523.8 | 62.0 | 47 | up |  |
| 10-28 16:30 | 52617.6 | 52647.1 | 52610.6 | 52637.6 | 52534.1 | 63.7 | 47 | up |  |
| 10-28 16:45 | 52639.1 | 52648.1 | 52596.1 | 52614.6 | 52541.4 | 60.5 | 47 | up |  |
| 10-28 18:00 | 52584.6 | 52624.1 | 52531.6 | 52573.6 | 52544.4 | 55.1 | 49 | up |  |
| 10-28 18:15 | 52573.1 | 52574.6 | 52516.6 | 52552.6 | 52545.1 | 52.5 | 49 | up |  |
| 10-28 18:30 | 52553.1 | 52570.1 | 52539.6 | 52549.6 | 52545.5 | 52.1 | 46 | up |  |
| 10-28 18:45 | 52550.1 | 52572.6 | 52531.1 | 52567.1 | 52547.5 | 54.2 | 46 | up |  |
| 10-28 19:00 | 52567.6 | 52599.6 | 52550.1 | 52586.6 | 52551.0 | 56.4 | 41 | up | **SIGNAL candle (closed → entry)** |
| 10-28 19:15 | 52585.1 | 52603.1 | 52574.1 | 52584.1 | 52554.0 | 56.0 | 36 | up | next candle (entry price) |
| 10-28 19:30 | 52584.6 | 52588.1 | 52510.6 | 52537.1 | 52552.5 | 49.3 | 33 | up | ← exit decided on this close |
| 10-28 19:45 | 52537.6 | 52588.1 | 52531.1 | 52570.1 | 52554.1 | 53.5 | 39 | up |  |
| 10-28 20:00 | 52571.6 | 52595.1 | 52539.1 | 52590.6 | 52557.4 | 56.0 | 42 | up |  |

## my_ema_rsi_15m · LONG · entered 10-28 20:15 → OPEN ·  · R - (best 1.87)

Logged entry reason: `my_ema_rsi_15m: 15min close 52590.60 > EMA21 52557.42, RSI 56.0, CHOP 42, Supertrend up`

Signal candle: **10-28 20:00** (15min); the trade opened right after it closed at 20:15.

| Measure | Value |
|---|---|
| close | 52590.60 |
| ema21 | 52557.42 |
| beyond EMA21 (ATR) | 0.46 |
| candles on this side of EMA21 (1 = this one just crossed) | 2 |
| RSI | 55.99 |
| RSI before | 53.53 |
| CHOP | 42.28 |
| EMA21 side changes in last 12 candles | 2 |
| Supertrend | 1 |
| last 3 closes | ↓↑↑ |
| signal candle body / range | 0.34 |
| signal candle range (ATR) | 0.77 |
| move since the 20-candle extreme (ATR) | 2.99 |
| closed beyond the prior 10-candle extreme | False |
| ADX(14) | 37.30 |
| EMA9 beyond EMA21 in the trade direction (ATR) | 0.20 |
| EMA9/21 crossed this many candles ago | 15 |
| EMA9/21 crosses in the last 20 candles | 2 |
| EMA21 slope over 8 candles in the trade direction (ATR) | 0.18 |
| RSI change over 3 candles | -0.06 |

Higher timeframes at that moment: 1h: close above EMA21, EMA21 > EMA50, RSI 58, Supertrend up → **with the trade**; 4h: close above EMA21, EMA21 > EMA50, RSI 57, Supertrend up → **with the trade**

| Candle (opens, NY) | O | H | L | C | EMA21 | RSI | CHOP | ST | |
|---|---|---|---|---|---|---|---|---|---|
| 10-28 18:00 | 52584.6 | 52624.1 | 52531.6 | 52573.6 | 52544.4 | 55.1 | 49 | up |  |
| 10-28 18:15 | 52573.1 | 52574.6 | 52516.6 | 52552.6 | 52545.1 | 52.5 | 49 | up |  |
| 10-28 18:30 | 52553.1 | 52570.1 | 52539.6 | 52549.6 | 52545.5 | 52.1 | 46 | up |  |
| 10-28 18:45 | 52550.1 | 52572.6 | 52531.1 | 52567.1 | 52547.5 | 54.2 | 46 | up |  |
| 10-28 19:00 | 52567.6 | 52599.6 | 52550.1 | 52586.6 | 52551.0 | 56.4 | 41 | up |  |
| 10-28 19:15 | 52585.1 | 52603.1 | 52574.1 | 52584.1 | 52554.0 | 56.0 | 36 | up |  |
| 10-28 19:30 | 52584.6 | 52588.1 | 52510.6 | 52537.1 | 52552.5 | 49.3 | 33 | up |  |
| 10-28 19:45 | 52537.6 | 52588.1 | 52531.1 | 52570.1 | 52554.1 | 53.5 | 39 | up |  |
| 10-28 20:00 | 52571.6 | 52595.1 | 52539.1 | 52590.6 | 52557.4 | 56.0 | 42 | up | **SIGNAL candle (closed → entry)** |
| 10-28 20:15 | 52590.1 | 52614.6 | 52559.6 | 52601.1 | 52561.4 | 57.2 | 43 | up | next candle (entry price) |
| 10-28 20:30 | 52600.6 | 52638.1 | 52590.1 | 52624.1 | 52567.1 | 59.9 | 63 | up |  |
| 10-28 20:45 | 52622.1 | 52624.1 | 52589.6 | 52603.1 | 52570.4 | 56.4 | 63 | up |  |
| 10-28 21:00 | 52603.6 | 52697.1 | 52603.1 | 52691.1 | 52581.3 | 65.5 | 54 | up |  |
| 10-28 21:15 | 52690.6 | 52714.1 | 52673.1 | 52694.1 | 52591.6 | 65.7 | 50 | up |  |
| 10-28 21:30 | 52694.6 | 52698.6 | 52656.6 | 52681.1 | 52599.7 | 63.5 | 48 | up |  |
| 10-28 21:45 | 52680.6 | 52778.6 | 52675.6 | 52742.1 | 52612.7 | 68.9 | 39 | up |  |
| 10-28 22:00 | 52741.6 | 52743.1 | 52700.6 | 52721.1 | 52622.5 | 65.3 | 40 | up |  |

## my_ema_rsi_1d · LONG · entered 10-28 17:00 → OPEN ·  · R - (best 0.00)

Logged entry reason: `my_ema_rsi_1d: 1D close 52614.60 > EMA21 52186.56, RSI 56.8, CHOP 59, Supertrend up`

Signal candle: **10-27 17:00** (1D); the trade opened right after it closed at 17:00.

| Measure | Value |
|---|---|
| close | 52614.60 |
| ema21 | 52186.43 |
| beyond EMA21 (ATR) | 0.74 |
| candles on this side of EMA21 (1 = this one just crossed) | 10 |
| RSI | 57.97 |
| RSI before | 55.57 |
| CHOP | 59.10 |
| EMA21 side changes in last 12 candles | 1 |
| Supertrend | 1 |
| last 3 closes | ↑↑↑ |
| signal candle body / range | 0.32 |
| signal candle range (ATR) | 0.98 |
| move since the 20-candle extreme (ATR) | 3.50 |
| closed beyond the prior 10-candle extreme | False |
| ADX(14) | 22.16 |
| EMA9 beyond EMA21 in the trade direction (ATR) | 0.37 |
| EMA9/21 crossed this many candles ago | 8 |
| EMA9/21 crosses in the last 20 candles | 1 |
| EMA21 slope over 8 candles in the trade direction (ATR) | 0.68 |
| RSI change over 3 candles | 4.16 |

Higher timeframes at that moment: 1h: close above EMA21, EMA21 > EMA50, RSI 62, Supertrend up → **with the trade**; 4h: close above EMA21, EMA21 > EMA50, RSI 57, Supertrend up → **with the trade**

| Candle (opens, NY) | O | H | L | C | EMA21 | RSI | CHOP | ST | |
|---|---|---|---|---|---|---|---|---|---|
| 10-15 17:00 | 52234.0 | 52622.0 | 51867.6 | 51999.6 | 51793.6 | 53.6 | 54 | dn |  |
| 10-18 17:00 | 52066.6 | 52308.1 | 51850.1 | 52046.4 | 51816.6 | 54.2 | 54 | dn |  |
| 10-19 17:00 | 52060.9 | 52742.0 | 51903.4 | 52655.0 | 51892.8 | 61.4 | 52 | up |  |
| 10-20 17:00 | 52636.0 | 52983.0 | 52425.6 | 52914.0 | 51985.6 | 64.0 | 49 | up |  |
| 10-21 17:00 | 52878.5 | 52965.0 | 52475.0 | 52916.4 | 52070.3 | 64.0 | 49 | up |  |
| 10-22 17:00 | 52926.4 | 52978.9 | 52063.0 | 52284.0 | 52089.7 | 53.8 | 50 | up |  |
| 10-25 17:00 | 52400.8 | 52643.4 | 52202.8 | 52371.5 | 52115.3 | 54.9 | 50 | up |  |
| 10-26 17:00 | 52370.5 | 52627.0 | 52261.6 | 52426.7 | 52143.6 | 55.6 | 49 | up |  |
| 10-27 17:00 | 52430.7 | 52812.6 | 52244.2 | 52614.6 | 52186.4 | 58.0 | 59 | up | **SIGNAL candle (closed → entry)** |
| 10-28 17:00 | 52584.6 | 52778.6 | 52510.6 | 52710.1 | 52234.0 | 59.2 | 61 | up |  |

## my_ema_rsi_1h · LONG · entered 10-22 12:00 → OPEN ·  · R - (best 0.00)

Logged entry reason: `my_ema_rsi_1h: 1h close 52863.60 > EMA21 52670.66, RSI 59.9, CHOP 57, Supertrend up`

Signal candle: **10-22 11:00** (1h); the trade opened right after it closed at 12:00.

| Measure | Value |
|---|---|
| close | 52863.60 |
| ema21 | 52670.66 |
| beyond EMA21 (ATR) | 1.36 |
| candles on this side of EMA21 (1 = this one just crossed) | 3 |
| RSI | 59.86 |
| RSI before | 52.43 |
| CHOP | 56.97 |
| EMA21 side changes in last 12 candles | 2 |
| Supertrend | 1 |
| last 3 closes | ↑↓↑ |
| signal candle body / range | 0.75 |
| signal candle range (ATR) | 1.66 |
| move since the 20-candle extreme (ATR) | 2.73 |
| closed beyond the prior 10-candle extreme | True |
| ADX(14) | 18.94 |
| EMA9 beyond EMA21 in the trade direction (ATR) | 0.18 |
| EMA9/21 crossed this many candles ago | 2 |
| EMA9/21 crosses in the last 20 candles | 2 |
| EMA21 slope over 8 candles in the trade direction (ATR) | -0.03 |
| RSI change over 3 candles | 12.30 |

Higher timeframes at that moment: 1h: close above EMA21, EMA21 > EMA50, RSI 60, Supertrend up → **with the trade**; 4h: close above EMA21, EMA21 > EMA50, RSI 56, Supertrend up → **with the trade**

| Candle (opens, NY) | O | H | L | C | EMA21 | RSI | CHOP | ST | |
|---|---|---|---|---|---|---|---|---|---|
| 10-22 03:00 | 52635.5 | 52672.5 | 52543.5 | 52557.0 | 52675.0 | 44.2 | 48 | up |  |
| 10-22 04:00 | 52557.5 | 52587.5 | 52500.0 | 52510.0 | 52660.0 | 41.8 | 44 | up |  |
| 10-22 05:00 | 52509.5 | 52571.0 | 52481.0 | 52540.0 | 52649.1 | 43.9 | 41 | up |  |
| 10-22 06:00 | 52540.5 | 52596.5 | 52475.0 | 52521.0 | 52637.5 | 42.8 | 37 | up |  |
| 10-22 07:00 | 52521.5 | 52616.5 | 52493.0 | 52592.5 | 52633.4 | 47.9 | 44 | up |  |
| 10-22 08:00 | 52593.0 | 52639.5 | 52569.0 | 52587.0 | 52629.2 | 47.6 | 52 | up |  |
| 10-22 09:00 | 52587.5 | 52852.0 | 52574.0 | 52834.6 | 52647.8 | 61.2 | 50 | up |  |
| 10-22 10:00 | 52832.6 | 52840.0 | 52533.0 | 52686.6 | 52651.4 | 52.4 | 57 | up |  |
| 10-22 11:00 | 52687.0 | 52879.6 | 52643.6 | 52863.6 | 52670.7 | 59.9 | 57 | up | **SIGNAL candle (closed → entry)** |
| 10-22 12:00 | 52864.0 | 52965.0 | 52761.0 | 52841.0 | 52686.1 | 58.6 | 52 | up | next candle (entry price) |
| 10-22 13:00 | 52841.4 | 52868.4 | 52745.4 | 52806.0 | 52697.0 | 56.6 | 53 | up |  |
| 10-22 14:00 | 52806.4 | 52885.4 | 52714.0 | 52771.0 | 52703.8 | 54.6 | 56 | up |  |
| 10-22 15:00 | 52770.4 | 52932.0 | 52741.0 | 52911.0 | 52722.6 | 60.6 | 58 | up |  |
| 10-22 16:00 | 52910.4 | 52960.9 | 52876.9 | 52916.4 | 52740.2 | 60.8 | 57 | up |  |
| 10-22 18:00 | 52926.4 | 52978.9 | 52917.9 | 52963.9 | 52760.6 | 62.7 | 55 | up |  |
| 10-22 19:00 | 52962.9 | 52975.9 | 52927.9 | 52969.9 | 52779.6 | 63.0 | 54 | up |  |
| 10-22 20:00 | 52969.4 | 52969.4 | 52870.9 | 52910.9 | 52791.5 | 58.9 | 54 | up |  |

## my_ema_rsi_1h · LONG · entered 10-28 16:00 → OPEN ·  · R - (best 0.00)

Logged entry reason: `my_ema_rsi_1h: 1h close 52568.60 > EMA21 52444.84, RSI 59.9, CHOP 53, Supertrend up`

Signal candle: **10-28 15:00** (1h); the trade opened right after it closed at 16:00.

| Measure | Value |
|---|---|
| close | 52568.60 |
| ema21 | 52444.84 |
| beyond EMA21 (ATR) | 1.05 |
| candles on this side of EMA21 (1 = this one just crossed) | 8 |
| RSI | 59.85 |
| RSI before | 52.41 |
| CHOP | 52.55 |
| EMA21 side changes in last 12 candles | 1 |
| Supertrend | 1 |
| last 3 closes | ↓↓↑ |
| signal candle body / range | 0.55 |
| signal candle range (ATR) | 1.74 |
| move since the 20-candle extreme (ATR) | 2.75 |
| closed beyond the prior 10-candle extreme | False |
| ADX(14) | 16.84 |
| EMA9 beyond EMA21 in the trade direction (ATR) | 0.42 |
| EMA9/21 crossed this many candles ago | 6 |
| EMA9/21 crosses in the last 20 candles | 1 |
| EMA21 slope over 8 candles in the trade direction (ATR) | 0.76 |
| RSI change over 3 candles | -5.24 |

Higher timeframes at that moment: 1h: close above EMA21, EMA21 > EMA50, RSI 60, Supertrend up → **with the trade**; 4h: close above EMA21, EMA21 > EMA50, RSI 56, Supertrend up → **with the trade**

| Candle (opens, NY) | O | H | L | C | EMA21 | RSI | CHOP | ST | |
|---|---|---|---|---|---|---|---|---|---|
| 10-28 07:00 | 52297.2 | 52362.7 | 52282.2 | 52289.2 | 52355.6 | 42.2 | 52 | dn |  |
| 10-28 08:00 | 52288.7 | 52465.2 | 52282.2 | 52442.2 | 52363.5 | 55.8 | 58 | dn |  |
| 10-28 09:00 | 52442.7 | 52526.8 | 52371.2 | 52477.8 | 52373.9 | 58.2 | 54 | dn |  |
| 10-28 10:00 | 52478.2 | 52566.8 | 52441.8 | 52480.8 | 52383.6 | 58.4 | 52 | dn |  |
| 10-28 11:00 | 52479.2 | 52586.8 | 52454.8 | 52566.8 | 52400.2 | 64.0 | 49 | up |  |
| 10-28 12:00 | 52566.2 | 52676.6 | 52512.6 | 52585.2 | 52417.0 | 65.1 | 42 | up |  |
| 10-28 13:00 | 52585.6 | 52587.2 | 52522.2 | 52561.2 | 52430.2 | 62.5 | 43 | up |  |
| 10-28 14:00 | 52559.6 | 52645.2 | 52406.6 | 52455.6 | 52432.5 | 52.4 | 48 | up |  |
| 10-28 15:00 | 52456.2 | 52578.2 | 52373.2 | 52568.6 | 52444.8 | 59.9 | 53 | up | **SIGNAL candle (closed → entry)** |
| 10-28 16:00 | 52568.2 | 52812.6 | 52568.1 | 52614.6 | 52460.3 | 62.4 | 47 | up | next candle (entry price) |
| 10-28 18:00 | 52584.6 | 52624.1 | 52516.6 | 52567.1 | 52470.0 | 58.3 | 47 | up |  |
| 10-28 19:00 | 52567.6 | 52603.1 | 52510.6 | 52570.1 | 52479.1 | 58.5 | 48 | up |  |
| 10-28 20:00 | 52571.6 | 52638.1 | 52539.1 | 52603.1 | 52490.4 | 60.6 | 48 | up |  |
| 10-28 21:00 | 52603.6 | 52778.6 | 52603.1 | 52742.1 | 52513.2 | 67.9 | 52 | up |  |
| 10-28 22:00 | 52741.6 | 52761.1 | 52700.6 | 52710.1 | 52531.1 | 64.9 | 51 | up |  |

## my_ema_rsi_4h · LONG · entered 10-22 09:00 → OPEN ·  · R - (best 1.69)

Logged entry reason: `my_ema_rsi_4h: 4h close 52587.00 > EMA21 52452.03, RSI 56.2, CHOP 46, Supertrend up`

Signal candle: **10-22 05:00** (4h); the trade opened right after it closed at 09:00.

| Measure | Value |
|---|---|
| close | 52587.00 |
| ema21 | 52452.03 |
| beyond EMA21 (ATR) | 0.56 |
| candles on this side of EMA21 (1 = this one just crossed) | 12 |
| RSI | 56.17 |
| RSI before | 54.21 |
| CHOP | 46.20 |
| EMA21 side changes in last 12 candles | 0 |
| Supertrend | 1 |
| last 3 closes | ↑↓↑ |
| signal candle body / range | 0.47 |
| signal candle range (ATR) | 0.68 |
| move since the 20-candle extreme (ATR) | 3.06 |
| closed beyond the prior 10-candle extreme | False |
| ADX(14) | 33.43 |
| EMA9 beyond EMA21 in the trade direction (ATR) | 0.65 |
| EMA9/21 crossed this many candles ago | >19 |
| EMA9/21 crosses in the last 20 candles | 0 |
| EMA21 slope over 8 candles in the trade direction (ATR) | 1.05 |
| RSI change over 3 candles | -4.62 |

Higher timeframes at that moment: 1h: close below EMA21, EMA21 > EMA50, RSI 48, Supertrend up → **AGAINST the trade**; 4h: close above EMA21, EMA21 > EMA50, RSI 56, Supertrend up → **with the trade**

| Candle (opens, NY) | O | H | L | C | EMA21 | RSI | CHOP | ST | |
|---|---|---|---|---|---|---|---|---|---|
| 10-20 21:00 | 52534.0 | 52598.5 | 52491.5 | 52574.5 | 52200.2 | 63.2 | 50 | up |  |
| 10-21 01:00 | 52574.0 | 52634.5 | 52471.0 | 52474.5 | 52225.1 | 59.5 | 49 | up |  |
| 10-21 05:00 | 52475.0 | 52774.5 | 52445.5 | 52769.5 | 52274.6 | 65.8 | 49 | up |  |
| 10-21 09:00 | 52769.0 | 52811.5 | 52425.6 | 52754.0 | 52318.2 | 65.2 | 49 | up |  |
| 10-21 13:00 | 52754.6 | 52983.0 | 52624.0 | 52914.0 | 52372.3 | 68.3 | 44 | up |  |
| 10-21 17:00 | 52878.5 | 52883.5 | 52687.5 | 52706.0 | 52402.7 | 60.8 | 45 | up |  |
| 10-21 21:00 | 52704.5 | 52797.5 | 52686.5 | 52718.5 | 52431.4 | 61.1 | 45 | up |  |
| 10-22 01:00 | 52718.0 | 52726.5 | 52500.0 | 52510.0 | 52438.5 | 54.2 | 46 | up |  |
| 10-22 05:00 | 52509.5 | 52639.5 | 52475.0 | 52587.0 | 52452.0 | 56.2 | 46 | up | **SIGNAL candle (closed → entry)** |
| 10-22 09:00 | 52587.5 | 52965.0 | 52533.0 | 52841.0 | 52487.4 | 61.9 | 49 | up | next candle (entry price) |
| 10-22 13:00 | 52841.4 | 52960.9 | 52714.0 | 52916.4 | 52526.4 | 63.5 | 51 | up |  |
| 10-22 17:00 | 52926.4 | 52978.9 | 52870.9 | 52910.9 | 52561.4 | 63.3 | 67 | up |  |
| 10-22 21:00 | 52911.4 | 52914.9 | 52734.9 | 52751.4 | 52578.6 | 57.6 | 66 | up |  |
| 10-23 01:00 | 52750.9 | 52809.4 | 52660.9 | 52669.9 | 52586.9 | 54.9 | 66 | up |  |
| 10-23 05:00 | 52669.4 | 52675.4 | 52387.9 | 52422.9 | 52572.0 | 47.6 | 66 | up |  |
| 10-23 09:00 | 52420.9 | 52478.9 | 52063.0 | 52334.6 | 52550.4 | 45.2 | 52 | up |  |
| 10-23 13:00 | 52334.0 | 52343.0 | 52215.0 | 52284.0 | 52526.2 | 43.9 | 50 | up |  |

## my_rsi_15m · LONG · entered 10-22 16:00 → OPEN ·  · R - (best 0.00)

Logged entry reason: `my_rsi_15m: 15min close 52911.00 > EMA21 52798.62, RSI 62.1, CHOP 61, Supertrend up`

Signal candle: **10-22 15:45** (15min); the trade opened right after it closed at 16:00.

| Measure | Value |
|---|---|
| close | 52911.00 |
| ema21 | 52798.62 |
| beyond EMA21 (ATR) | 1.31 |
| candles on this side of EMA21 (1 = this one just crossed) | 4 |
| RSI | 62.09 |
| RSI before | 57.44 |
| CHOP | 60.80 |
| EMA21 side changes in last 12 candles | 2 |
| Supertrend | 1 |
| last 3 closes | ↑↓↑ |
| signal candle body / range | 0.53 |
| signal candle range (ATR) | 1.40 |
| move since the 20-candle extreme (ATR) | 3.11 |
| closed beyond the prior 10-candle extreme | True |
| ADX(14) | 19.67 |
| EMA9 beyond EMA21 in the trade direction (ATR) | 0.43 |
| EMA9/21 crossed this many candles ago | >19 |
| EMA9/21 crosses in the last 20 candles | 0 |
| EMA21 slope over 8 candles in the trade direction (ATR) | 0.42 |
| RSI change over 3 candles | 8.15 |

Higher timeframes at that moment: 1h: close above EMA21, EMA21 > EMA50, RSI 61, Supertrend up → **with the trade**; 4h: close above EMA21, EMA21 > EMA50, RSI 62, Supertrend up → **with the trade**

| Candle (opens, NY) | O | H | L | C | EMA21 | RSI | CHOP | ST | |
|---|---|---|---|---|---|---|---|---|---|
| 10-22 13:45 | 52840.0 | 52841.0 | 52776.4 | 52806.0 | 52762.4 | 54.5 | 44 | up |  |
| 10-22 14:00 | 52806.4 | 52834.0 | 52714.0 | 52812.4 | 52767.0 | 54.9 | 47 | up |  |
| 10-22 14:15 | 52813.0 | 52885.4 | 52784.4 | 52802.0 | 52770.2 | 54.1 | 55 | up |  |
| 10-22 14:30 | 52800.0 | 52800.0 | 52757.4 | 52786.4 | 52771.6 | 52.7 | 58 | up |  |
| 10-22 14:45 | 52786.0 | 52811.0 | 52766.0 | 52771.0 | 52771.6 | 51.4 | 60 | up |  |
| 10-22 15:00 | 52770.4 | 52841.4 | 52741.0 | 52802.0 | 52774.4 | 53.9 | 61 | up |  |
| 10-22 15:15 | 52802.4 | 52860.0 | 52795.0 | 52851.0 | 52781.3 | 57.8 | 59 | up |  |
| 10-22 15:30 | 52849.0 | 52867.0 | 52823.4 | 52848.0 | 52787.4 | 57.4 | 59 | up |  |
| 10-22 15:45 | 52847.4 | 52932.0 | 52812.0 | 52911.0 | 52798.6 | 62.1 | 61 | up | **SIGNAL candle (closed → entry)** |
| 10-22 16:00 | 52910.4 | 52960.9 | 52887.9 | 52894.4 | 52807.3 | 60.2 | 57 | up | next candle (entry price) |
| 10-22 16:15 | 52894.9 | 52927.9 | 52876.9 | 52918.9 | 52817.5 | 62.0 | 56 | up |  |
| 10-22 16:30 | 52919.4 | 52923.9 | 52903.9 | 52919.9 | 52826.8 | 62.1 | 52 | up |  |
| 10-22 16:45 | 52921.4 | 52928.9 | 52909.9 | 52916.4 | 52834.9 | 61.7 | 50 | up |  |
| 10-22 18:00 | 52926.4 | 52946.9 | 52917.9 | 52937.4 | 52844.2 | 63.4 | 49 | up |  |
| 10-22 18:15 | 52936.9 | 52978.9 | 52930.4 | 52973.4 | 52856.0 | 66.3 | 46 | up |  |
| 10-22 18:30 | 52972.9 | 52976.9 | 52954.4 | 52962.4 | 52865.7 | 64.6 | 45 | up |  |
| 10-22 18:45 | 52961.9 | 52973.4 | 52954.9 | 52963.9 | 52874.6 | 64.8 | 41 | up |  |

## my_rsi_1h · LONG · entered 10-22 16:00 → OPEN ·  · R - (best 0.00)

Logged entry reason: `my_rsi_1h: 1h close 52911.00 > EMA21 52722.60, RSI 60.6, CHOP 58, Supertrend up`

Signal candle: **10-22 15:00** (1h); the trade opened right after it closed at 16:00.

| Measure | Value |
|---|---|
| close | 52911.00 |
| ema21 | 52722.60 |
| beyond EMA21 (ATR) | 1.26 |
| candles on this side of EMA21 (1 = this one just crossed) | 7 |
| RSI | 60.60 |
| RSI before | 54.62 |
| CHOP | 57.64 |
| EMA21 side changes in last 12 candles | 1 |
| Supertrend | 1 |
| last 3 closes | ↓↓↑ |
| signal candle body / range | 0.74 |
| signal candle range (ATR) | 1.27 |
| move since the 20-candle extreme (ATR) | 2.91 |
| closed beyond the prior 10-candle extreme | False |
| ADX(14) | 20.50 |
| EMA9 beyond EMA21 in the trade direction (ATR) | 0.38 |
| EMA9/21 crossed this many candles ago | 6 |
| EMA9/21 crosses in the last 20 candles | 2 |
| EMA21 slope over 8 candles in the trade direction (ATR) | 0.59 |
| RSI change over 3 candles | 2.00 |

Higher timeframes at that moment: 1h: close above EMA21, EMA21 > EMA50, RSI 61, Supertrend up → **with the trade**; 4h: close above EMA21, EMA21 > EMA50, RSI 62, Supertrend up → **with the trade**

| Candle (opens, NY) | O | H | L | C | EMA21 | RSI | CHOP | ST | |
|---|---|---|---|---|---|---|---|---|---|
| 10-22 07:00 | 52521.5 | 52616.5 | 52493.0 | 52592.5 | 52633.4 | 47.9 | 44 | up |  |
| 10-22 08:00 | 52593.0 | 52639.5 | 52569.0 | 52587.0 | 52629.2 | 47.6 | 52 | up |  |
| 10-22 09:00 | 52587.5 | 52852.0 | 52574.0 | 52834.6 | 52647.8 | 61.2 | 50 | up |  |
| 10-22 10:00 | 52832.6 | 52840.0 | 52533.0 | 52686.6 | 52651.4 | 52.4 | 57 | up |  |
| 10-22 11:00 | 52687.0 | 52879.6 | 52643.6 | 52863.6 | 52670.7 | 59.9 | 57 | up |  |
| 10-22 12:00 | 52864.0 | 52965.0 | 52761.0 | 52841.0 | 52686.1 | 58.6 | 52 | up |  |
| 10-22 13:00 | 52841.4 | 52868.4 | 52745.4 | 52806.0 | 52697.0 | 56.6 | 53 | up |  |
| 10-22 14:00 | 52806.4 | 52885.4 | 52714.0 | 52771.0 | 52703.8 | 54.6 | 56 | up |  |
| 10-22 15:00 | 52770.4 | 52932.0 | 52741.0 | 52911.0 | 52722.6 | 60.6 | 58 | up | **SIGNAL candle (closed → entry)** |
| 10-22 16:00 | 52910.4 | 52960.9 | 52876.9 | 52916.4 | 52740.2 | 60.8 | 57 | up | next candle (entry price) |
| 10-22 18:00 | 52926.4 | 52978.9 | 52917.9 | 52963.9 | 52760.6 | 62.7 | 55 | up |  |
| 10-22 19:00 | 52962.9 | 52975.9 | 52927.9 | 52969.9 | 52779.6 | 63.0 | 54 | up |  |
| 10-22 20:00 | 52969.4 | 52969.4 | 52870.9 | 52910.9 | 52791.5 | 58.9 | 54 | up |  |
| 10-22 21:00 | 52911.4 | 52914.9 | 52756.9 | 52771.9 | 52789.7 | 50.5 | 56 | up |  |
| 10-22 22:00 | 52771.4 | 52828.4 | 52735.4 | 52813.9 | 52791.9 | 52.7 | 59 | up |  |
| 10-22 23:00 | 52813.4 | 52824.4 | 52790.4 | 52802.9 | 52792.9 | 52.0 | 59 | up |  |
| 10-23 00:00 | 52804.9 | 52807.9 | 52734.9 | 52751.4 | 52789.2 | 49.0 | 55 | up |  |

## my_rsi_4h · LONG · entered 10-22 13:00 → OPEN ·  · R - (best 0.00)

Logged entry reason: `my_rsi_4h: 4h close 52841.00 > EMA21 52487.40, RSI 61.9, CHOP 49, Supertrend up`

Signal candle: **10-22 09:00** (4h); the trade opened right after it closed at 13:00.

| Measure | Value |
|---|---|
| close | 52841.00 |
| ema21 | 52487.40 |
| beyond EMA21 (ATR) | 1.39 |
| candles on this side of EMA21 (1 = this one just crossed) | 13 |
| RSI | 61.94 |
| RSI before | 56.17 |
| CHOP | 48.77 |
| EMA21 side changes in last 12 candles | 0 |
| Supertrend | 1 |
| last 3 closes | ↓↑↑ |
| signal candle body / range | 0.59 |
| signal candle range (ATR) | 1.70 |
| move since the 20-candle extreme (ATR) | 3.89 |
| closed beyond the prior 10-candle extreme | False |
| ADX(14) | 34.23 |
| EMA9 beyond EMA21 in the trade direction (ATR) | 0.66 |
| EMA9/21 crossed this many candles ago | >19 |
| EMA9/21 crosses in the last 20 candles | 0 |
| EMA21 slope over 8 candles in the trade direction (ATR) | 1.03 |
| RSI change over 3 candles | 0.88 |

Higher timeframes at that moment: 1h: close above EMA21, EMA21 > EMA50, RSI 59, Supertrend up → **with the trade**; 4h: close above EMA21, EMA21 > EMA50, RSI 62, Supertrend up → **with the trade**

| Candle (opens, NY) | O | H | L | C | EMA21 | RSI | CHOP | ST | |
|---|---|---|---|---|---|---|---|---|---|
| 10-21 01:00 | 52574.0 | 52634.5 | 52471.0 | 52474.5 | 52225.1 | 59.5 | 49 | up |  |
| 10-21 05:00 | 52475.0 | 52774.5 | 52445.5 | 52769.5 | 52274.6 | 65.8 | 49 | up |  |
| 10-21 09:00 | 52769.0 | 52811.5 | 52425.6 | 52754.0 | 52318.2 | 65.2 | 49 | up |  |
| 10-21 13:00 | 52754.6 | 52983.0 | 52624.0 | 52914.0 | 52372.3 | 68.3 | 44 | up |  |
| 10-21 17:00 | 52878.5 | 52883.5 | 52687.5 | 52706.0 | 52402.7 | 60.8 | 45 | up |  |
| 10-21 21:00 | 52704.5 | 52797.5 | 52686.5 | 52718.5 | 52431.4 | 61.1 | 45 | up |  |
| 10-22 01:00 | 52718.0 | 52726.5 | 52500.0 | 52510.0 | 52438.5 | 54.2 | 46 | up |  |
| 10-22 05:00 | 52509.5 | 52639.5 | 52475.0 | 52587.0 | 52452.0 | 56.2 | 46 | up |  |
| 10-22 09:00 | 52587.5 | 52965.0 | 52533.0 | 52841.0 | 52487.4 | 61.9 | 49 | up | **SIGNAL candle (closed → entry)** |
| 10-22 13:00 | 52841.4 | 52960.9 | 52714.0 | 52916.4 | 52526.4 | 63.5 | 51 | up | next candle (entry price) |
| 10-22 17:00 | 52926.4 | 52978.9 | 52870.9 | 52910.9 | 52561.4 | 63.3 | 67 | up |  |
| 10-22 21:00 | 52911.4 | 52914.9 | 52734.9 | 52751.4 | 52578.6 | 57.6 | 66 | up |  |
| 10-23 01:00 | 52750.9 | 52809.4 | 52660.9 | 52669.9 | 52586.9 | 54.9 | 66 | up |  |
| 10-23 05:00 | 52669.4 | 52675.4 | 52387.9 | 52422.9 | 52572.0 | 47.6 | 66 | up |  |
| 10-23 09:00 | 52420.9 | 52478.9 | 52063.0 | 52334.6 | 52550.4 | 45.2 | 52 | up |  |
| 10-23 13:00 | 52334.0 | 52343.0 | 52215.0 | 52284.0 | 52526.2 | 43.9 | 50 | up |  |
| 10-25 17:00 | 52400.8 | 52400.8 | 52215.8 | 52249.8 | 52501.1 | 43.0 | 47 | up |  |

## Every logged signal on US30 in the window (taken and skipped)

| Time (NY) | Book | What happened | Why |
|---|---|---|---|
| 10-28 04:15 | ema21_rsi55 | taken | qty 0.66, jev 0.3825 |
| 10-28 05:30 | my_ema_cross_15m | rejected | trading halted: daily loss limit hit ($-1,941) |
| 10-28 06:00 | my_ema_rsi_15m | rejected | choppy market (CHOP 63.6 ≥ 61.8) |
| 10-28 06:15 | ema21_rsi55 | rejected | choppy market (CHOP 71.8 ≥ 61.8) |
| 10-28 06:15 | my_ema_rsi_15m | rejected | choppy market (CHOP 71.8 ≥ 61.8) |
| 10-28 06:30 | my_ema_cross_15m | rejected | choppy market (CHOP 73.0 ≥ 61.8) |
| 10-28 07:45 | ema21_rsi55 | rejected | choppy market (CHOP 67.7 ≥ 61.8) |
| 10-28 07:45 | my_ema_cross_15m | rejected | choppy market (CHOP 67.7 ≥ 61.8) |
| 10-28 07:45 | my_ema_rsi_15m | rejected | choppy market (CHOP 67.7 ≥ 61.8) |
| 10-28 08:00 | my_ema_cross_15m | rejected | choppy market (CHOP 69.8 ≥ 61.8) |
| 10-28 08:15 | ema21_rsi55 | rejected | choppy market (CHOP 63.7 ≥ 61.8) |
| 10-28 08:15 | my_ema_cross_15m | rejected | choppy market (CHOP 63.7 ≥ 61.8) |
| 10-28 08:15 | my_ema_rsi_15m | rejected | choppy market (CHOP 63.7 ≥ 61.8) |
| 10-28 09:45 | my_ema_rsi_15m | rejected | stop too wide (3.1 ATR) |
| 10-28 11:00 | my_ema_cross_1h | taken | qty 1.39, jev 0.2625 |
| 10-28 13:00 | my_ema_rsi_4h | rejected | choppy market (CHOP 67.8 ≥ 61.8) |
| 10-28 14:45 | ema21_rsi55 | rejected | news blackout: FOMC Press Conference |
| 10-28 14:45 | my_ema_rsi_15m | rejected | news blackout: FOMC Press Conference |
| 10-28 15:15 | my_ema_rsi_15m | taken | qty 1.51, jev 0.305 |
| 10-28 15:30 | my_ema_cross_15m | rejected | trading halted: daily loss limit hit ($-1,941) |
| 10-28 15:45 | my_ema_cross_15m | rejected | trading halted: daily loss limit hit ($-1,941) |
| 10-28 16:00 | my_ema_rsi_15m | taken | qty 1.61, jev 0.5125 |
| 10-28 16:00 | my_ema_rsi_1h | taken | qty 1.09, jev 0.5025 |
| 10-28 17:00 | my_ema_cross_4h | taken | qty 0.81, jev 0.5 |
| 10-28 17:00 | my_ema_rsi_1d | taken | qty 0.38, jev 0.475 |
| 10-28 19:15 | my_ema_rsi_15m | taken | qty 3.84, jev 0.485 |
| 10-28 20:15 | my_ema_rsi_15m | taken | qty 3.5, jev 0.4775 |
