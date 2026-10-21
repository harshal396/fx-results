# Context for US30 - generated 2026-10-21 18:57 New York

Candles are labelled by their OPEN time, like TradingView. The **signal candle** is the one that closed when the bot entered; the trade opened at the open of the next candle. Prices are OANDA mid prices.


## ema21_rsi55 · LONG · entered 10-21 11:30 → exited 10-21 15:00 · close_below_ema21 · R 0.304 (best 0.96)

Logged entry reason: `EMA21+RSI55: 15m close 52652.00 > EMA21 52595.07, RSI 55.7`

Signal candle: **10-21 11:15** (15min); the trade opened right after it closed at 11:30.

| Measure | Value |
|---|---|
| close | 52652.00 |
| ema21 | 52595.07 |
| beyond EMA21 (ATR) | 0.74 |
| candles on this side of EMA21 (1 = this one just crossed) | 1 |
| RSI | 55.68 |
| RSI before | 48.44 |
| CHOP | 45.49 |
| EMA21 side changes in last 12 candles | 2 |
| Supertrend | -1 |
| last 3 closes | ↓↑↑ |
| signal candle body / range | 0.79 |
| signal candle range (ATR) | 1.30 |
| move since the 20-candle extreme (ATR) | 2.92 |
| closed beyond the prior 10-candle extreme | False |

Higher timeframes at that moment: 1h: close above EMA21, EMA21 > EMA50, RSI 52, Supertrend up → **with the trade**; 4h: close above EMA21, EMA21 > EMA50, RSI 66, Supertrend up → **with the trade**

| Candle (opens, NY) | O | H | L | C | EMA21 | RSI | CHOP | ST | |
|---|---|---|---|---|---|---|---|---|---|
| 10-21 09:15 | 52765.0 | 52805.0 | 52764.5 | 52799.5 | 52633.5 | 76.1 | 27 | up |  |
| 10-21 09:30 | 52799.6 | 52802.6 | 52474.0 | 52573.6 | 52628.0 | 46.2 | 39 | dn |  |
| 10-21 09:45 | 52573.0 | 52671.6 | 52573.0 | 52585.0 | 52624.1 | 47.3 | 43 | dn |  |
| 10-21 10:00 | 52584.6 | 52584.6 | 52425.6 | 52499.0 | 52612.7 | 40.4 | 41 | dn |  |
| 10-21 10:15 | 52497.6 | 52519.0 | 52446.6 | 52497.0 | 52602.2 | 40.3 | 42 | dn |  |
| 10-21 10:30 | 52497.6 | 52551.6 | 52487.6 | 52543.0 | 52596.8 | 45.2 | 43 | dn |  |
| 10-21 10:45 | 52542.6 | 52597.0 | 52534.0 | 52534.0 | 52591.1 | 44.4 | 43 | dn |  |
| 10-21 11:00 | 52535.6 | 52586.0 | 52515.6 | 52572.0 | 52589.4 | 48.4 | 44 | dn |  |
| 10-21 11:15 | 52572.6 | 52672.6 | 52572.0 | 52652.0 | 52595.1 | 55.7 | 45 | dn | **SIGNAL candle (closed → entry)** |
| 10-21 11:30 | 52652.6 | 52700.0 | 52630.6 | 52681.0 | 52602.9 | 58.0 | 46 | dn | next candle (entry price) |
| 10-21 11:45 | 52680.6 | 52699.0 | 52670.6 | 52681.6 | 52610.0 | 58.0 | 46 | dn |  |
| 10-21 12:00 | 52681.0 | 52702.0 | 52656.6 | 52676.6 | 52616.1 | 57.4 | 45 | dn |  |
| 10-21 12:15 | 52677.0 | 52707.0 | 52674.6 | 52697.6 | 52623.5 | 59.3 | 44 | dn |  |
| 10-21 12:30 | 52698.0 | 52798.6 | 52681.6 | 52738.0 | 52633.9 | 62.7 | 46 | dn |  |
| 10-21 12:45 | 52738.6 | 52761.0 | 52718.0 | 52754.0 | 52644.8 | 64.0 | 47 | up |  |
| 10-21 13:00 | 52754.6 | 52783.6 | 52740.0 | 52773.6 | 52656.5 | 65.6 | 38 | up |  |
| 10-21 13:15 | 52773.0 | 52786.6 | 52755.6 | 52764.6 | 52666.4 | 64.2 | 35 | up |  |
| 10-21 13:30 | 52766.0 | 52813.0 | 52750.0 | 52808.6 | 52679.3 | 67.8 | 32 | up |  |
| 10-21 13:45 | 52809.0 | 52838.6 | 52804.6 | 52827.6 | 52692.8 | 69.2 | 31 | up |  |
| 10-21 14:00 | 52828.0 | 52850.6 | 52818.0 | 52845.6 | 52706.7 | 70.6 | 32 | up |  |
| 10-21 14:15 | 52845.0 | 52867.0 | 52844.0 | 52857.6 | 52720.4 | 71.5 | 28 | up |  |
| 10-21 14:30 | 52857.0 | 52876.6 | 52849.6 | 52869.6 | 52734.0 | 72.4 | 31 | up |  |
| 10-21 14:45 | 52870.0 | 52876.6 | 52718.6 | 52725.6 | 52733.2 | 51.4 | 42 | up | ← exit decided on this close |
| 10-21 15:00 | 52727.0 | 52727.6 | 52624.0 | 52694.0 | 52729.6 | 48.1 | 43 | dn |  |
| 10-21 15:15 | 52693.6 | 52828.0 | 52688.6 | 52825.6 | 52738.4 | 59.7 | 48 | dn |  |

## ema21_rsi55 · LONG · entered 10-21 15:30 → exited 10-21 15:50 · session_flat · R 0.135 (best 0.15)

Logged entry reason: `EMA21+RSI55: 15m close 52825.60 > EMA21 52738.35, RSI 59.7`

Signal candle: **10-21 15:15** (15min); the trade opened right after it closed at 15:30.

| Measure | Value |
|---|---|
| close | 52825.60 |
| ema21 | 52738.35 |
| beyond EMA21 (ATR) | 1.22 |
| candles on this side of EMA21 (1 = this one just crossed) | 1 |
| RSI | 59.69 |
| RSI before | 48.11 |
| CHOP | 47.85 |
| EMA21 side changes in last 12 candles | 2 |
| Supertrend | -1 |
| last 3 closes | ↓↓↑ |
| signal candle body / range | 0.95 |
| signal candle range (ATR) | 1.95 |
| move since the 20-candle extreme (ATR) | 4.74 |
| closed beyond the prior 10-candle extreme | False |

Higher timeframes at that moment: 1h: close above EMA21, EMA21 > EMA50, RSI 58, Supertrend up → **with the trade**; 4h: close above EMA21, EMA21 > EMA50, RSI 65, Supertrend up → **with the trade**

| Candle (opens, NY) | O | H | L | C | EMA21 | RSI | CHOP | ST | |
|---|---|---|---|---|---|---|---|---|---|
| 10-21 13:15 | 52773.0 | 52786.6 | 52755.6 | 52764.6 | 52666.4 | 64.2 | 35 | up |  |
| 10-21 13:30 | 52766.0 | 52813.0 | 52750.0 | 52808.6 | 52679.3 | 67.8 | 32 | up |  |
| 10-21 13:45 | 52809.0 | 52838.6 | 52804.6 | 52827.6 | 52692.8 | 69.2 | 31 | up |  |
| 10-21 14:00 | 52828.0 | 52850.6 | 52818.0 | 52845.6 | 52706.7 | 70.6 | 32 | up |  |
| 10-21 14:15 | 52845.0 | 52867.0 | 52844.0 | 52857.6 | 52720.4 | 71.5 | 28 | up |  |
| 10-21 14:30 | 52857.0 | 52876.6 | 52849.6 | 52869.6 | 52734.0 | 72.4 | 31 | up |  |
| 10-21 14:45 | 52870.0 | 52876.6 | 52718.6 | 52725.6 | 52733.2 | 51.4 | 42 | up |  |
| 10-21 15:00 | 52727.0 | 52727.6 | 52624.0 | 52694.0 | 52729.6 | 48.1 | 43 | dn |  |
| 10-21 15:15 | 52693.6 | 52828.0 | 52688.6 | 52825.6 | 52738.4 | 59.7 | 48 | dn | **SIGNAL candle (closed → entry)** |
| 10-21 15:30 | 52826.0 | 52830.0 | 52793.6 | 52822.6 | 52746.0 | 59.4 | 47 | dn | ← exit decided on this close |
| 10-21 15:45 | 52824.6 | 52902.0 | 52820.6 | 52890.0 | 52759.1 | 64.1 | 46 | up |  |
| 10-21 16:00 | 52889.0 | 52973.5 | 52842.5 | 52939.5 | 52775.5 | 67.1 | 38 | up |  |

## my_ema_rsi_15m · LONG · entered 10-21 00:15 → exited 10-21 02:15 · close_past_ema21 · R -0.314 (best 0.41)

Logged entry reason: `my_ema_rsi_15m: 15min close 52592.50 > EMA21 52547.42, RSI 61.6, CHOP 50, Supertrend up`

Signal candle: **10-21 00:00** (15min); the trade opened right after it closed at 00:15.

| Measure | Value |
|---|---|
| close | 52592.50 |
| ema21 | 52547.42 |
| beyond EMA21 (ATR) | 1.36 |
| candles on this side of EMA21 (1 = this one just crossed) | 6 |
| RSI | 61.64 |
| RSI before | 55.00 |
| CHOP | 49.95 |
| EMA21 side changes in last 12 candles | 1 |
| Supertrend | 1 |
| last 3 closes | ↓↓↑ |
| signal candle body / range | 0.67 |
| signal candle range (ATR) | 1.63 |
| move since the 20-candle extreme (ATR) | 3.05 |
| closed beyond the prior 10-candle extreme | True |

Higher timeframes at that moment: 1h: close above EMA21, EMA21 > EMA50, RSI 60, Supertrend up → **with the trade**; 4h: close above EMA21, EMA21 > EMA50, RSI 62, Supertrend up → **with the trade**

| Candle (opens, NY) | O | H | L | C | EMA21 | RSI | CHOP | ST | |
|---|---|---|---|---|---|---|---|---|---|
| 10-20 22:00 | 52505.5 | 52508.5 | 52491.5 | 52507.5 | 52535.8 | 45.6 | 51 | up |  |
| 10-20 22:15 | 52507.0 | 52528.5 | 52503.5 | 52513.0 | 52533.7 | 46.9 | 54 | up |  |
| 10-20 22:30 | 52512.5 | 52528.0 | 52511.0 | 52519.0 | 52532.4 | 48.3 | 54 | up |  |
| 10-20 22:45 | 52518.5 | 52546.5 | 52517.5 | 52543.0 | 52533.3 | 53.7 | 56 | up |  |
| 10-20 23:00 | 52542.5 | 52559.5 | 52541.0 | 52551.0 | 52534.9 | 55.3 | 60 | up |  |
| 10-20 23:15 | 52551.5 | 52580.0 | 52551.0 | 52577.0 | 52538.8 | 60.3 | 56 | up |  |
| 10-20 23:30 | 52577.5 | 52582.5 | 52560.5 | 52569.0 | 52541.5 | 58.2 | 53 | up |  |
| 10-20 23:45 | 52568.5 | 52569.0 | 52546.5 | 52557.0 | 52542.9 | 55.0 | 52 | up |  |
| 10-21 00:00 | 52556.5 | 52594.0 | 52540.0 | 52592.5 | 52547.4 | 61.6 | 50 | up | **SIGNAL candle (closed → entry)** |
| 10-21 00:15 | 52592.0 | 52598.5 | 52572.0 | 52572.0 | 52549.7 | 56.5 | 47 | up | next candle (entry price) |
| 10-21 00:30 | 52572.5 | 52590.5 | 52565.5 | 52573.0 | 52551.8 | 56.7 | 47 | up |  |
| 10-21 00:45 | 52572.5 | 52580.5 | 52569.5 | 52574.5 | 52553.8 | 57.0 | 44 | up |  |
| 10-21 01:00 | 52574.0 | 52615.5 | 52571.5 | 52611.5 | 52559.1 | 63.8 | 41 | up |  |
| 10-21 01:15 | 52611.0 | 52633.0 | 52600.0 | 52624.5 | 52565.0 | 65.8 | 37 | up |  |
| 10-21 01:30 | 52625.0 | 52634.5 | 52589.5 | 52604.5 | 52568.6 | 60.2 | 42 | up |  |
| 10-21 01:45 | 52604.0 | 52607.5 | 52579.5 | 52587.0 | 52570.3 | 55.7 | 45 | up |  |
| 10-21 02:00 | 52588.5 | 52594.5 | 52557.0 | 52564.5 | 52569.8 | 50.5 | 49 | up | ← exit decided on this close |
| 10-21 02:15 | 52565.0 | 52591.0 | 52561.5 | 52572.5 | 52570.0 | 52.2 | 57 | up |  |
| 10-21 02:30 | 52573.0 | 52582.0 | 52552.0 | 52569.5 | 52570.0 | 51.5 | 58 | up |  |

## my_ema_rsi_15m · SHORT · entered 10-21 04:45 → exited 10-21 05:45 · close_past_ema21 · R -0.752 (best 0.69)

Logged entry reason: `my_ema_rsi_15m: 15min close 52507.50 < EMA21 52555.01, RSI 40.9, CHOP 54, Supertrend down`

Signal candle: **10-21 04:30** (15min); the trade opened right after it closed at 04:45.

| Measure | Value |
|---|---|
| close | 52507.50 |
| ema21 | 52555.01 |
| beyond EMA21 (ATR) | 1.16 |
| candles on this side of EMA21 (1 = this one just crossed) | 2 |
| RSI | 40.87 |
| RSI before | 49.90 |
| CHOP | 54.13 |
| EMA21 side changes in last 12 candles | 7 |
| Supertrend | -1 |
| last 3 closes | ↑↓↓ |
| signal candle body / range | 0.69 |
| signal candle range (ATR) | 1.76 |
| move since the 20-candle extreme (ATR) | 3.11 |
| closed beyond the prior 10-candle extreme | False |

Higher timeframes at that moment: 1h: close above EMA21, EMA21 > EMA50, RSI 58, Supertrend up → **AGAINST the trade**; 4h: close above EMA21, EMA21 > EMA50, RSI 63, Supertrend up → **AGAINST the trade**

| Candle (opens, NY) | O | H | L | C | EMA21 | RSI | CHOP | ST | |
|---|---|---|---|---|---|---|---|---|---|
| 10-21 02:30 | 52573.0 | 52582.0 | 52552.0 | 52569.5 | 52570.0 | 51.5 | 58 | up |  |
| 10-21 02:45 | 52569.0 | 52573.5 | 52517.5 | 52525.5 | 52565.9 | 42.3 | 52 | dn |  |
| 10-21 03:00 | 52526.0 | 52548.5 | 52500.5 | 52527.0 | 52562.4 | 42.7 | 49 | dn |  |
| 10-21 03:15 | 52527.5 | 52583.5 | 52505.0 | 52567.0 | 52562.8 | 51.7 | 53 | dn |  |
| 10-21 03:30 | 52567.5 | 52570.0 | 52529.0 | 52535.5 | 52560.3 | 45.6 | 52 | dn |  |
| 10-21 03:45 | 52535.0 | 52576.0 | 52531.0 | 52555.5 | 52559.9 | 49.7 | 54 | dn |  |
| 10-21 04:00 | 52555.0 | 52570.0 | 52533.5 | 52561.5 | 52560.0 | 50.8 | 54 | dn |  |
| 10-21 04:15 | 52562.0 | 52566.5 | 52529.0 | 52557.0 | 52559.8 | 49.9 | 56 | dn |  |
| 10-21 04:30 | 52557.5 | 52558.5 | 52486.5 | 52507.5 | 52555.0 | 40.9 | 54 | dn | **SIGNAL candle (closed → entry)** |
| 10-21 04:45 | 52507.0 | 52516.5 | 52471.0 | 52474.5 | 52547.7 | 36.2 | 51 | dn | next candle (entry price) |
| 10-21 05:00 | 52475.0 | 52497.5 | 52445.5 | 52496.0 | 52543.0 | 40.9 | 52 | dn |  |
| 10-21 05:15 | 52495.5 | 52532.0 | 52474.5 | 52528.5 | 52541.7 | 47.3 | 57 | dn |  |
| 10-21 05:30 | 52528.0 | 52586.0 | 52523.0 | 52570.5 | 52544.3 | 54.2 | 59 | dn | ← exit decided on this close |
| 10-21 05:45 | 52571.0 | 52585.5 | 52502.5 | 52505.5 | 52540.8 | 44.5 | 63 | dn |  |
| 10-21 06:00 | 52507.5 | 52527.5 | 52463.5 | 52471.5 | 52534.5 | 40.4 | 65 | dn |  |

## my_ema_rsi_1h · LONG · entered 10-21 07:00 → exited 10-21 09:32 · stop · R 0.972 (best 2.20)

Logged entry reason: `my_ema_rsi_1h: 1h close 52540.50 > EMA21 52477.95, RSI 56.6, CHOP 61, Supertrend up`

Signal candle: **10-21 06:00** (1h); the trade opened right after it closed at 07:00.

| Measure | Value |
|---|---|
| close | 52540.50 |
| ema21 | 52477.95 |
| beyond EMA21 (ATR) | 0.60 |
| candles on this side of EMA21 (1 = this one just crossed) | 21 |
| RSI | 56.63 |
| RSI before | 54.58 |
| CHOP | 60.60 |
| EMA21 side changes in last 12 candles | 0 |
| Supertrend | 1 |
| last 3 closes | ↓↑↑ |
| signal candle body / range | 0.35 |
| signal candle range (ATR) | 0.91 |
| move since the 20-candle extreme (ATR) | 1.73 |
| closed beyond the prior 10-candle extreme | False |

Higher timeframes at that moment: 1h: close above EMA21, EMA21 > EMA50, RSI 57, Supertrend up → **with the trade**; 4h: close above EMA21, EMA21 > EMA50, RSI 60, Supertrend up → **with the trade**

| Candle (opens, NY) | O | H | L | C | EMA21 | RSI | CHOP | ST | |
|---|---|---|---|---|---|---|---|---|---|
| 10-20 22:00 | 52505.5 | 52546.5 | 52491.5 | 52543.0 | 52412.0 | 59.4 | 36 | up |  |
| 10-20 23:00 | 52542.5 | 52582.5 | 52541.0 | 52557.0 | 52425.2 | 60.0 | 37 | up |  |
| 10-21 00:00 | 52556.5 | 52598.5 | 52540.0 | 52574.5 | 52438.8 | 60.8 | 55 | up |  |
| 10-21 01:00 | 52574.0 | 52634.5 | 52571.5 | 52587.0 | 52452.3 | 61.4 | 58 | up |  |
| 10-21 02:00 | 52588.5 | 52594.5 | 52517.5 | 52525.5 | 52458.9 | 56.9 | 60 | up |  |
| 10-21 03:00 | 52526.0 | 52583.5 | 52500.5 | 52555.5 | 52467.7 | 58.5 | 60 | up |  |
| 10-21 04:00 | 52555.0 | 52570.0 | 52471.0 | 52474.5 | 52468.3 | 52.7 | 60 | up |  |
| 10-21 05:00 | 52475.0 | 52586.0 | 52445.5 | 52505.5 | 52471.7 | 54.6 | 61 | up |  |
| 10-21 06:00 | 52507.5 | 52551.5 | 52457.0 | 52540.5 | 52477.9 | 56.6 | 61 | up | **SIGNAL candle (closed → entry)** |
| 10-21 07:00 | 52541.0 | 52640.0 | 52538.5 | 52617.0 | 52490.6 | 60.8 | 63 | up | next candle (entry price) |
| 10-21 08:00 | 52616.5 | 52774.5 | 52609.0 | 52769.5 | 52515.9 | 67.5 | 47 | up | ← exit decided on this close |
| 10-21 09:00 | 52769.0 | 52811.5 | 52474.0 | 52585.0 | 52522.2 | 55.2 | 52 | up |  |
| 10-21 10:00 | 52584.6 | 52597.0 | 52425.6 | 52534.0 | 52523.3 | 52.4 | 53 | up |  |

## my_ema_rsi_1h · LONG · entered 10-21 12:00 → OPEN ·  · R - (best 1.03)

Logged entry reason: `my_ema_rsi_1h: 1h close 52681.60 > EMA21 52537.68, RSI 58.9, CHOP 56, Supertrend up`

Signal candle: **10-21 11:00** (1h); the trade opened right after it closed at 12:00.

| Measure | Value |
|---|---|
| close | 52681.60 |
| ema21 | 52537.68 |
| beyond EMA21 (ATR) | 1.09 |
| candles on this side of EMA21 (1 = this one just crossed) | 26 |
| RSI | 58.94 |
| RSI before | 52.36 |
| CHOP | 55.56 |
| EMA21 side changes in last 12 candles | 0 |
| Supertrend | 1 |
| last 3 closes | ↓↓↑ |
| signal candle body / range | 0.79 |
| signal candle range (ATR) | 1.40 |
| move since the 20-candle extreme (ATR) | 1.94 |
| closed beyond the prior 10-candle extreme | False |

Higher timeframes at that moment: 1h: close above EMA21, EMA21 > EMA50, RSI 59, Supertrend up → **with the trade**; 4h: close above EMA21, EMA21 > EMA50, RSI 66, Supertrend up → **with the trade**

| Candle (opens, NY) | O | H | L | C | EMA21 | RSI | CHOP | ST | |
|---|---|---|---|---|---|---|---|---|---|
| 10-21 03:00 | 52526.0 | 52583.5 | 52500.5 | 52555.5 | 52467.7 | 58.5 | 60 | up |  |
| 10-21 04:00 | 52555.0 | 52570.0 | 52471.0 | 52474.5 | 52468.3 | 52.7 | 60 | up |  |
| 10-21 05:00 | 52475.0 | 52586.0 | 52445.5 | 52505.5 | 52471.7 | 54.6 | 61 | up |  |
| 10-21 06:00 | 52507.5 | 52551.5 | 52457.0 | 52540.5 | 52477.9 | 56.6 | 61 | up |  |
| 10-21 07:00 | 52541.0 | 52640.0 | 52538.5 | 52617.0 | 52490.6 | 60.8 | 63 | up |  |
| 10-21 08:00 | 52616.5 | 52774.5 | 52609.0 | 52769.5 | 52515.9 | 67.5 | 47 | up |  |
| 10-21 09:00 | 52769.0 | 52811.5 | 52474.0 | 52585.0 | 52522.2 | 55.2 | 52 | up |  |
| 10-21 10:00 | 52584.6 | 52597.0 | 52425.6 | 52534.0 | 52523.3 | 52.4 | 53 | up |  |
| 10-21 11:00 | 52535.6 | 52700.0 | 52515.6 | 52681.6 | 52537.7 | 58.9 | 56 | up | **SIGNAL candle (closed → entry)** |
| 10-21 12:00 | 52681.0 | 52798.6 | 52656.6 | 52754.0 | 52557.3 | 61.7 | 57 | up | next candle (entry price) |
| 10-21 13:00 | 52754.6 | 52838.6 | 52740.0 | 52827.6 | 52581.9 | 64.4 | 56 | up |  |
| 10-21 14:00 | 52828.0 | 52876.6 | 52718.6 | 52725.6 | 52595.0 | 58.4 | 55 | up |  |
| 10-21 15:00 | 52727.0 | 52902.0 | 52624.0 | 52890.0 | 52621.8 | 64.2 | 57 | up |  |
| 10-21 16:00 | 52889.0 | 52983.0 | 52842.5 | 52914.0 | 52648.4 | 65.0 | 52 | up |  |

## my_rsi_15m · LONG · entered 10-21 00:15 → exited 10-21 02:15 · close_past_ema21 · R -0.314 (best 0.41)

Logged entry reason: `my_rsi_15m: 15min close 52592.50 > EMA21 52547.42, RSI 61.6, CHOP 50, Supertrend up`

Signal candle: **10-21 00:00** (15min); the trade opened right after it closed at 00:15.

| Measure | Value |
|---|---|
| close | 52592.50 |
| ema21 | 52547.42 |
| beyond EMA21 (ATR) | 1.36 |
| candles on this side of EMA21 (1 = this one just crossed) | 6 |
| RSI | 61.64 |
| RSI before | 55.00 |
| CHOP | 49.95 |
| EMA21 side changes in last 12 candles | 1 |
| Supertrend | 1 |
| last 3 closes | ↓↓↑ |
| signal candle body / range | 0.67 |
| signal candle range (ATR) | 1.63 |
| move since the 20-candle extreme (ATR) | 3.05 |
| closed beyond the prior 10-candle extreme | True |

Higher timeframes at that moment: 1h: close above EMA21, EMA21 > EMA50, RSI 60, Supertrend up → **with the trade**; 4h: close above EMA21, EMA21 > EMA50, RSI 62, Supertrend up → **with the trade**

| Candle (opens, NY) | O | H | L | C | EMA21 | RSI | CHOP | ST | |
|---|---|---|---|---|---|---|---|---|---|
| 10-20 22:00 | 52505.5 | 52508.5 | 52491.5 | 52507.5 | 52535.8 | 45.6 | 51 | up |  |
| 10-20 22:15 | 52507.0 | 52528.5 | 52503.5 | 52513.0 | 52533.7 | 46.9 | 54 | up |  |
| 10-20 22:30 | 52512.5 | 52528.0 | 52511.0 | 52519.0 | 52532.4 | 48.3 | 54 | up |  |
| 10-20 22:45 | 52518.5 | 52546.5 | 52517.5 | 52543.0 | 52533.3 | 53.7 | 56 | up |  |
| 10-20 23:00 | 52542.5 | 52559.5 | 52541.0 | 52551.0 | 52534.9 | 55.3 | 60 | up |  |
| 10-20 23:15 | 52551.5 | 52580.0 | 52551.0 | 52577.0 | 52538.8 | 60.3 | 56 | up |  |
| 10-20 23:30 | 52577.5 | 52582.5 | 52560.5 | 52569.0 | 52541.5 | 58.2 | 53 | up |  |
| 10-20 23:45 | 52568.5 | 52569.0 | 52546.5 | 52557.0 | 52542.9 | 55.0 | 52 | up |  |
| 10-21 00:00 | 52556.5 | 52594.0 | 52540.0 | 52592.5 | 52547.4 | 61.6 | 50 | up | **SIGNAL candle (closed → entry)** |
| 10-21 00:15 | 52592.0 | 52598.5 | 52572.0 | 52572.0 | 52549.7 | 56.5 | 47 | up | next candle (entry price) |
| 10-21 00:30 | 52572.5 | 52590.5 | 52565.5 | 52573.0 | 52551.8 | 56.7 | 47 | up |  |
| 10-21 00:45 | 52572.5 | 52580.5 | 52569.5 | 52574.5 | 52553.8 | 57.0 | 44 | up |  |
| 10-21 01:00 | 52574.0 | 52615.5 | 52571.5 | 52611.5 | 52559.1 | 63.8 | 41 | up |  |
| 10-21 01:15 | 52611.0 | 52633.0 | 52600.0 | 52624.5 | 52565.0 | 65.8 | 37 | up |  |
| 10-21 01:30 | 52625.0 | 52634.5 | 52589.5 | 52604.5 | 52568.6 | 60.2 | 42 | up |  |
| 10-21 01:45 | 52604.0 | 52607.5 | 52579.5 | 52587.0 | 52570.3 | 55.7 | 45 | up |  |
| 10-21 02:00 | 52588.5 | 52594.5 | 52557.0 | 52564.5 | 52569.8 | 50.5 | 49 | up | ← exit decided on this close |
| 10-21 02:15 | 52565.0 | 52591.0 | 52561.5 | 52572.5 | 52570.0 | 52.2 | 57 | up |  |
| 10-21 02:30 | 52573.0 | 52582.0 | 52552.0 | 52569.5 | 52570.0 | 51.5 | 58 | up |  |

## Every logged signal on US30 in the window (taken and skipped)

| Time (NY) | Book | What happened | Why |
|---|---|---|---|
| 10-21 00:15 | my_ema_rsi_15m | taken | qty 3.56, jev 0.505 |
| 10-21 00:15 | my_rsi_15m | taken | qty 3.56, jev 0.475 |
| 10-21 03:00 | my_ema_rsi_15m | rejected | stop too wide (3.5 ATR) |
| 10-21 03:15 | my_ema_cross_15m | rejected | stop too wide (3.4 ATR) |
| 10-21 04:45 | my_ema_rsi_15m | taken | qty 3.97, jev 0.3175 |
| 10-21 06:00 | ema21_rsi55 | rejected | choppy market (CHOP 63.2 ≥ 61.8) |
| 10-21 06:15 | my_ema_rsi_15m | rejected | choppy market (CHOP 64.9 ≥ 61.8) |
| 10-21 07:00 | my_ema_rsi_1h | taken | qty 2.85, jev 0.475 |
| 10-21 07:15 | my_ema_rsi_15m | rejected | choppy market (CHOP 62.9 ≥ 61.8) |
| 10-21 07:30 | my_ema_cross_15m | rejected | stop too wide (3.2 ATR) |
| 10-21 10:15 | my_ema_rsi_15m | rejected | stop too wide (4.3 ATR) |
| 10-21 10:30 | my_ema_cross_15m | rejected | stop too wide (4.3 ATR) |
| 10-21 11:30 | ema21_rsi55 | taken | qty 0.3, jev 0.695 |
| 10-21 11:30 | my_ema_rsi_15m | rejected | stop too wide (3.2 ATR) |
| 10-21 11:45 | my_ema_cross_15m | rejected | stop too wide (3.6 ATR) |
| 10-21 12:00 | my_ema_rsi_1h | taken | qty 1.21, jev 0.49 |
| 10-21 15:30 | ema21_rsi55 | taken | qty 0.32, jev 0.7125 |
| 10-21 15:30 | my_ema_rsi_15m | rejected | stop too wide (3.1 ATR) |
| 10-21 16:00 | my_rsi_15m | rejected | stop too wide (4.1 ATR) |
