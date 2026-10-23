# Context for NDQ - generated 2026-10-23 00:34 New York

Candles are labelled by their OPEN time, like TradingView. The **signal candle** is the one that closed when the bot entered; the trade opened at the open of the next candle. Prices are OANDA mid prices.


## my_ema_cross_15m · SHORT · entered 10-21 18:15 → exited 10-22 06:31 · stop · R 1.033 (best 2.78)

Logged entry reason: `my_ema_cross_15m: 15min close 29747.40 < EMA21 29838.56, RSI 40.8, CHOP 54, Supertrend down`

Signal candle: **10-21 18:00** (15min); the trade opened right after it closed at 18:15.

| Measure | Value |
|---|---|
| close | 29747.40 |
| ema21 | 29838.56 |
| beyond EMA21 (ATR) | 1.47 |
| candles on this side of EMA21 (1 = this one just crossed) | 1 |
| RSI | 40.85 |
| RSI before | 53.21 |
| CHOP | 54.18 |
| EMA21 side changes in last 12 candles | 5 |
| Supertrend | -1 |
| last 3 closes | ↑↓↓ |
| signal candle body / range | 0.73 |
| signal candle range (ATR) | 0.98 |
| move since the 20-candle extreme (ATR) | 3.41 |
| closed beyond the prior 10-candle extreme | False |
| ADX(14) | 17.16 |
| EMA9 beyond EMA21 in the trade direction (ATR) | 0.09 |
| EMA9/21 crossed this many candles ago | 1 |
| EMA9/21 crosses in the last 20 candles | 1 |
| EMA21 slope over 8 candles in the trade direction (ATR) | 0.09 |
| RSI change over 3 candles | -9.55 |

Higher timeframes at that moment: 1h: close above EMA21, EMA21 > EMA50, RSI 59, Supertrend up → **AGAINST the trade**; 4h: close above EMA21, EMA21 < EMA50, RSI 53, Supertrend down → **AGAINST the trade**

| Candle (opens, NY) | O | H | L | C | EMA21 | RSI | CHOP | ST | |
|---|---|---|---|---|---|---|---|---|---|
| 10-21 15:00 | 29811.3 | 29812.1 | 29732.1 | 29795.1 | 29844.1 | 45.6 | 42 | up |  |
| 10-21 15:15 | 29794.8 | 29880.2 | 29792.1 | 29878.8 | 29847.2 | 55.4 | 45 | up |  |
| 10-21 15:30 | 29878.3 | 29884.2 | 29844.0 | 29867.6 | 29849.1 | 54.0 | 45 | up |  |
| 10-21 15:45 | 29867.7 | 29904.8 | 29840.1 | 29842.6 | 29848.5 | 50.9 | 46 | up |  |
| 10-21 16:00 | 29843.2 | 29901.4 | 29807.8 | 29808.4 | 29844.9 | 46.9 | 45 | up |  |
| 10-21 16:15 | 29808.6 | 29850.1 | 29800.6 | 29837.0 | 29844.1 | 50.4 | 45 | up |  |
| 10-21 16:30 | 29837.1 | 29873.6 | 29824.1 | 29866.8 | 29846.2 | 53.8 | 46 | up |  |
| 10-21 16:45 | 29866.6 | 29882.7 | 29854.6 | 29862.4 | 29847.7 | 53.2 | 50 | up |  |
| 10-21 18:00 | 29791.6 | 29794.4 | 29734.0 | 29747.4 | 29838.6 | 40.8 | 54 | dn | **SIGNAL candle (closed → entry)** |
| 10-21 18:15 | 29747.2 | 29748.4 | 29677.8 | 29690.7 | 29825.1 | 36.4 | 47 | dn | next candle (entry price) |
| 10-21 18:30 | 29690.6 | 29708.6 | 29681.6 | 29685.2 | 29812.4 | 36.0 | 47 | dn |  |
| 10-21 18:45 | 29685.1 | 29707.4 | 29680.0 | 29693.0 | 29801.5 | 37.0 | 47 | dn |  |
| 10-21 19:00 | 29693.1 | 29700.8 | 29651.9 | 29674.4 | 29790.0 | 35.5 | 47 | dn |  |
| 10-21 19:15 | 29673.8 | 29676.4 | 29627.1 | 29635.8 | 29776.0 | 32.5 | 42 | dn |  |
| 10-21 19:30 | 29635.6 | 29647.6 | 29616.7 | 29636.4 | 29763.3 | 32.5 | 39 | dn |  |
| 10-21 19:45 | 29636.4 | 29638.4 | 29601.4 | 29608.4 | 29749.2 | 30.4 | 34 | dn |  |
| 10-21 20:00 | 29608.2 | 29699.1 | 29607.9 | 29682.4 | 29743.1 | 41.5 | 37 | dn |  |
| 10-21 20:15 | 29682.2 | 29683.4 | 29614.6 | 29634.7 | 29733.3 | 37.4 | 37 | dn |  |
| 10-21 20:30 | 29634.4 | 29652.6 | 29618.4 | 29650.6 | 29725.8 | 39.5 | 37 | dn |  |
| 10-21 20:45 | 29650.4 | 29671.6 | 29633.6 | 29638.9 | 29717.9 | 38.5 | 36 | dn |  |
| 10-21 21:00 | 29639.0 | 29655.0 | 29611.8 | 29630.8 | 29709.9 | 37.7 | 36 | dn |  |
| 10-21 21:15 | 29630.9 | 29656.8 | 29602.0 | 29630.2 | 29702.7 | 37.7 | 51 | dn |  |
| 10-21 21:30 | 29629.6 | 29643.6 | 29576.4 | 29603.4 | 29693.7 | 35.0 | 53 | dn |  |
| 10-21 21:45 | 29603.6 | 29613.0 | 29574.0 | 29598.4 | 29685.0 | 34.6 | 60 | dn |  |
| 10-21 22:00 | 29598.8 | 29604.4 | 29560.6 | 29563.6 | 29674.0 | 31.3 | 58 | dn |  |
| 10-21 22:15 | 29563.8 | 29565.0 | 29528.0 | 29543.0 | 29662.1 | 29.6 | 52 | dn |  |
| 10-21 22:30 | 29543.1 | 29557.1 | 29525.2 | 29529.8 | 29650.0 | 28.4 | 51 | dn |  |
| 10-21 22:45 | 29529.2 | 29543.8 | 29517.3 | 29533.4 | 29639.4 | 29.2 | 48 | dn |  |
| 10-21 23:00 | 29533.3 | 29535.8 | 29495.1 | 29501.8 | 29626.9 | 26.5 | 44 | dn |  |
| 10-21 23:15 | 29502.0 | 29536.8 | 29496.6 | 29516.4 | 29616.9 | 29.8 | 44 | dn |  |
| 10-21 23:30 | 29515.6 | 29515.6 | 29464.6 | 29491.2 | 29605.5 | 27.5 | 39 | dn |  |
| 10-21 23:45 | 29491.1 | 29498.4 | 29459.2 | 29476.2 | 29593.7 | 26.2 | 39 | dn |  |
| 10-22 00:00 | 29476.8 | 29478.6 | 29456.9 | 29465.2 | 29582.0 | 25.3 | 37 | dn |  |
| 10-22 00:15 | 29465.0 | 29474.4 | 29446.3 | 29452.2 | 29570.2 | 24.2 | 37 | dn |  |
| 10-22 00:30 | 29451.8 | 29459.6 | 29427.8 | 29441.0 | 29558.5 | 23.3 | 33 | dn |  |
| 10-22 00:45 | 29441.6 | 29469.0 | 29434.1 | 29465.6 | 29550.0 | 29.7 | 34 | dn |  |
| 10-22 01:00 | 29465.8 | 29472.3 | 29441.6 | 29443.4 | 29540.3 | 27.4 | 37 | dn |  |
| 10-22 01:15 | 29443.3 | 29447.8 | 29411.8 | 29421.0 | 29529.5 | 25.4 | 36 | dn |  |
| 10-22 01:30 | 29421.2 | 29422.6 | 29369.8 | 29371.8 | 29515.2 | 21.5 | 36 | dn |  |
| 10-22 01:45 | 29372.4 | 29394.0 | 29353.1 | 29389.6 | 29503.7 | 25.9 | 35 | dn |  |
| 10-22 02:00 | 29389.4 | 29413.0 | 29357.4 | 29390.2 | 29493.4 | 26.0 | 39 | dn |  |
| 10-22 02:15 | 29390.4 | 29405.6 | 29353.6 | 29369.2 | 29482.1 | 24.2 | 42 | dn |  |
| 10-22 02:30 | 29368.8 | 29397.0 | 29357.4 | 29368.0 | 29471.7 | 24.1 | 42 | dn |  |
| 10-22 02:45 | 29368.2 | 29393.4 | 29358.0 | 29381.6 | 29463.6 | 27.9 | 46 | dn |  |
| 10-22 03:00 | 29381.6 | 29395.6 | 29315.4 | 29342.2 | 29452.5 | 24.1 | 44 | dn |  |
| 10-22 03:15 | 29343.0 | 29379.2 | 29327.8 | 29336.8 | 29442.0 | 23.7 | 49 | dn |  |
| 10-22 03:30 | 29336.6 | 29363.6 | 29330.4 | 29343.0 | 29433.0 | 25.5 | 50 | dn |  |
| 10-22 03:45 | 29343.0 | 29348.8 | 29310.0 | 29326.8 | 29423.3 | 23.9 | 50 | dn |  |
| 10-22 04:00 | 29326.6 | 29345.8 | 29295.8 | 29318.4 | 29413.8 | 23.1 | 48 | dn |  |
| 10-22 04:15 | 29318.4 | 29329.4 | 29300.4 | 29318.1 | 29405.1 | 23.0 | 48 | dn |  |
| 10-22 04:30 | 29317.9 | 29352.4 | 29300.6 | 29349.2 | 29400.0 | 32.8 | 55 | dn |  |
| 10-22 04:45 | 29349.0 | 29354.4 | 29264.1 | 29269.0 | 29388.1 | 24.3 | 56 | dn |  |
| 10-22 05:00 | 29269.0 | 29328.7 | 29262.4 | 29325.0 | 29382.4 | 36.6 | 59 | dn |  |
| 10-22 05:15 | 29324.8 | 29330.2 | 29276.6 | 29287.6 | 29373.8 | 32.8 | 60 | dn |  |
| 10-22 05:30 | 29287.6 | 29300.2 | 29270.2 | 29271.6 | 29364.5 | 31.3 | 60 | dn |  |
| 10-22 05:45 | 29271.0 | 29314.2 | 29271.0 | 29313.0 | 29359.8 | 39.1 | 62 | dn |  |
| 10-22 06:00 | 29313.6 | 29336.4 | 29296.9 | 29302.6 | 29354.6 | 37.9 | 62 | dn |  |
| 10-22 06:15 | 29302.6 | 29353.9 | 29291.4 | 29351.8 | 29354.3 | 46.1 | 64 | dn | ← exit decided on this close |
| 10-22 06:30 | 29351.7 | 29388.7 | 29349.9 | 29375.0 | 29356.2 | 49.5 | 64 | dn |  |
| 10-22 06:45 | 29374.6 | 29390.6 | 29349.8 | 29359.2 | 29356.5 | 47.3 | 63 | dn |  |

## my_ema_cross_15m · LONG · entered 10-22 21:45 → exited 10-22 22:00 · close_past_ema21 · R -0.389 (best 0.08)

Logged entry reason: `my_ema_cross_15m: 15min close 29048.60 > EMA21 28995.71, RSI 54.3, CHOP 60, Supertrend down`

Signal candle: **10-22 21:30** (15min); the trade opened right after it closed at 21:45.

| Measure | Value |
|---|---|
| close | 29048.60 |
| ema21 | 28995.71 |
| beyond EMA21 (ATR) | 0.75 |
| candles on this side of EMA21 (1 = this one just crossed) | 2 |
| RSI | 54.33 |
| RSI before | 51.77 |
| CHOP | 60.26 |
| EMA21 side changes in last 12 candles | 3 |
| Supertrend | -1 |
| last 3 closes | ↓↑↑ |
| signal candle body / range | 0.34 |
| signal candle range (ATR) | 1.10 |
| move since the 20-candle extreme (ATR) | 2.44 |
| closed beyond the prior 10-candle extreme | False |
| ADX(14) | 24.04 |
| EMA9 beyond EMA21 in the trade direction (ATR) | 0.00 |
| EMA9/21 crossed this many candles ago | 1 |
| EMA9/21 crosses in the last 20 candles | 1 |
| EMA21 slope over 8 candles in the trade direction (ATR) | 0.00 |
| RSI change over 3 candles | 1.00 |

Higher timeframes at that moment: 1h: close below EMA21, EMA21 < EMA50, RSI 36, Supertrend down → **AGAINST the trade**; 4h: close below EMA21, EMA21 < EMA50, RSI 35, Supertrend down → **AGAINST the trade**

| Candle (opens, NY) | O | H | L | C | EMA21 | RSI | CHOP | ST | |
|---|---|---|---|---|---|---|---|---|---|
| 10-22 19:30 | 28930.8 | 28935.7 | 28895.4 | 28921.0 | 28995.5 | 36.1 | 55 | dn |  |
| 10-22 19:45 | 28921.2 | 28953.6 | 28899.2 | 28941.0 | 28990.5 | 39.5 | 55 | dn |  |
| 10-22 20:00 | 28940.9 | 28987.0 | 28876.0 | 28986.7 | 28990.2 | 46.5 | 53 | dn |  |
| 10-22 20:15 | 28985.4 | 28988.8 | 28922.2 | 28949.0 | 28986.4 | 42.2 | 50 | dn |  |
| 10-22 20:30 | 28949.2 | 28994.7 | 28944.6 | 28983.4 | 28986.1 | 47.1 | 58 | dn |  |
| 10-22 20:45 | 28983.2 | 29051.4 | 28972.8 | 29034.2 | 28990.5 | 53.3 | 53 | dn |  |
| 10-22 21:00 | 29034.2 | 29050.0 | 28949.2 | 28954.8 | 28987.3 | 44.5 | 57 | dn |  |
| 10-22 21:15 | 28954.6 | 29050.0 | 28909.3 | 29022.0 | 28990.4 | 51.8 | 61 | dn |  |
| 10-22 21:30 | 29021.8 | 29060.7 | 28982.7 | 29048.6 | 28995.7 | 54.3 | 60 | dn | **SIGNAL candle (closed → entry)** |
| 10-22 21:45 | 29049.0 | 29064.6 | 28958.7 | 28976.6 | 28994.0 | 47.0 | 62 | dn | ← exit decided on this close |
| 10-22 22:00 | 28976.6 | 28994.4 | 28942.2 | 28977.8 | 28992.5 | 47.2 | 63 | dn |  |
| 10-22 22:15 | 28977.2 | 29017.0 | 28961.5 | 29004.8 | 28993.6 | 50.1 | 63 | dn |  |

## my_ema_cross_4h · SHORT · entered 10-21 21:00 → OPEN ·  · R - (best 1.99)

Logged entry reason: `my_ema_cross_4h: 4h close 29638.90 < EMA21 29715.93, RSI 45.9, CHOP 55, Supertrend down`

Signal candle: **10-21 17:00** (4h); the trade opened right after it closed at 21:00.

| Measure | Value |
|---|---|
| close | 29638.90 |
| ema21 | 29715.93 |
| beyond EMA21 (ATR) | 0.34 |
| candles on this side of EMA21 (1 = this one just crossed) | 1 |
| RSI | 45.89 |
| RSI before | 53.34 |
| CHOP | 54.92 |
| EMA21 side changes in last 12 candles | 4 |
| Supertrend | -1 |
| last 3 closes | ↑↓↓ |
| signal candle body / range | 0.79 |
| signal candle range (ATR) | 0.86 |
| move since the 20-candle extreme (ATR) | 1.42 |
| closed beyond the prior 10-candle extreme | False |
| ADX(14) | 23.76 |
| EMA9 beyond EMA21 in the trade direction (ATR) | 0.03 |
| EMA9/21 crossed this many candles ago | 1 |
| EMA9/21 crosses in the last 20 candles | 2 |
| EMA21 slope over 8 candles in the trade direction (ATR) | -0.14 |
| RSI change over 3 candles | -2.17 |

Higher timeframes at that moment: 1h: close below EMA21, EMA21 > EMA50, RSI 45, Supertrend up → **with the trade**; 4h: close below EMA21, EMA21 < EMA50, RSI 46, Supertrend down → **with the trade**

| Candle (opens, NY) | O | H | L | C | EMA21 | RSI | CHOP | ST | |
|---|---|---|---|---|---|---|---|---|---|
| 10-20 09:00 | 29433.2 | 29742.6 | 29231.3 | 29553.6 | 29684.8 | 41.8 | 50 | dn |  |
| 10-20 13:00 | 29553.8 | 29729.5 | 29498.9 | 29726.4 | 29688.6 | 48.4 | 56 | dn |  |
| 10-20 17:00 | 29799.8 | 29852.4 | 29702.0 | 29757.4 | 29694.9 | 49.5 | 55 | dn |  |
| 10-20 21:00 | 29757.6 | 29844.8 | 29689.6 | 29732.0 | 29698.2 | 48.6 | 56 | dn |  |
| 10-21 01:00 | 29731.6 | 29762.0 | 29579.6 | 29588.0 | 29688.2 | 43.6 | 58 | dn |  |
| 10-21 05:00 | 29587.9 | 29743.6 | 29569.9 | 29700.2 | 29689.3 | 48.1 | 58 | dn |  |
| 10-21 09:00 | 29700.4 | 29951.0 | 29614.2 | 29914.3 | 29709.8 | 55.3 | 55 | dn |  |
| 10-21 13:00 | 29914.4 | 29958.2 | 29732.1 | 29862.4 | 29723.6 | 53.3 | 56 | dn |  |
| 10-21 17:00 | 29791.6 | 29794.4 | 29601.4 | 29638.9 | 29715.9 | 45.9 | 55 | dn | **SIGNAL candle (closed → entry)** |
| 10-21 21:00 | 29639.0 | 29656.8 | 29427.8 | 29465.6 | 29693.2 | 41.1 | 56 | dn | next candle (entry price) |
| 10-22 01:00 | 29465.8 | 29472.3 | 29264.1 | 29269.0 | 29654.6 | 36.5 | 56 | dn |  |
| 10-22 05:00 | 29269.0 | 29398.6 | 29262.4 | 29342.3 | 29626.2 | 39.2 | 55 | dn |  |
| 10-22 09:00 | 29342.2 | 29434.4 | 28988.4 | 29090.4 | 29577.5 | 33.8 | 48 | dn |  |
| 10-22 13:00 | 29090.7 | 29095.8 | 28886.9 | 28944.9 | 29520.0 | 31.1 | 44 | dn |  |
| 10-22 17:00 | 28980.8 | 29051.4 | 28876.0 | 29034.2 | 29475.8 | 34.5 | 40 | dn |  |
| 10-22 21:00 | 29034.2 | 29064.6 | 28909.3 | 29030.2 | 29435.3 | 34.4 | 39 | dn |  |

## my_ema_rsi_15m · SHORT · entered 10-21 01:45 → exited 10-21 03:30 · close_past_ema21 · R -0.563 (best 0.32)

Logged entry reason: `my_ema_rsi_15m: 15min close 29692.40 < EMA21 29747.98, RSI 42.1, CHOP 38, Supertrend up`

Signal candle: **10-21 01:30** (15min); the trade opened right after it closed at 01:45.

| Measure | Value |
|---|---|
| close | 29692.40 |
| ema21 | 29747.98 |
| beyond EMA21 (ATR) | 1.26 |
| candles on this side of EMA21 (1 = this one just crossed) | 8 |
| RSI | 42.09 |
| RSI before | 48.07 |
| CHOP | 38.48 |
| EMA21 side changes in last 12 candles | 1 |
| Supertrend | 1 |
| last 3 closes | ↓↑↓ |
| signal candle body / range | 0.57 |
| signal candle range (ATR) | 1.66 |
| move since the 20-candle extreme (ATR) | 3.45 |
| closed beyond the prior 10-candle extreme | True |
| ADX(14) | 15.74 |
| EMA9 beyond EMA21 in the trade direction (ATR) | 0.27 |
| EMA9/21 crossed this many candles ago | 3 |
| EMA9/21 crosses in the last 20 candles | 1 |
| EMA21 slope over 8 candles in the trade direction (ATR) | 0.52 |
| RSI change over 3 candles | -4.93 |

Higher timeframes at that moment: 1h: close above EMA21, EMA21 > EMA50, RSI 56, Supertrend up → **AGAINST the trade**; 4h: close above EMA21, EMA21 < EMA50, RSI 49, Supertrend down → **AGAINST the trade**

| Candle (opens, NY) | O | H | L | C | EMA21 | RSI | CHOP | ST | |
|---|---|---|---|---|---|---|---|---|---|
| 10-20 23:30 | 29796.9 | 29806.7 | 29784.0 | 29789.0 | 29770.9 | 55.3 | 54 | up |  |
| 10-20 23:45 | 29789.1 | 29806.2 | 29759.2 | 29764.8 | 29770.3 | 51.7 | 53 | up |  |
| 10-21 00:00 | 29764.6 | 29773.0 | 29740.4 | 29745.8 | 29768.1 | 49.0 | 54 | up |  |
| 10-21 00:15 | 29745.6 | 29759.2 | 29732.9 | 29736.2 | 29765.2 | 47.6 | 50 | up |  |
| 10-21 00:30 | 29736.4 | 29752.4 | 29727.2 | 29740.4 | 29763.0 | 48.3 | 51 | up |  |
| 10-21 00:45 | 29740.8 | 29744.9 | 29726.9 | 29732.0 | 29760.1 | 47.0 | 51 | up |  |
| 10-21 01:00 | 29731.6 | 29740.0 | 29706.4 | 29708.8 | 29755.5 | 43.5 | 43 | up |  |
| 10-21 01:15 | 29708.6 | 29741.7 | 29695.4 | 29734.2 | 29753.5 | 48.1 | 42 | up |  |
| 10-21 01:30 | 29734.0 | 29740.2 | 29666.8 | 29692.4 | 29748.0 | 42.1 | 38 | up | **SIGNAL candle (closed → entry)** |
| 10-21 01:45 | 29692.4 | 29700.9 | 29672.4 | 29674.8 | 29741.3 | 39.8 | 39 | up | next candle (entry price) |
| 10-21 02:00 | 29674.7 | 29712.0 | 29671.4 | 29686.4 | 29736.3 | 42.0 | 41 | up |  |
| 10-21 02:15 | 29686.4 | 29690.2 | 29655.0 | 29663.8 | 29729.7 | 39.0 | 40 | dn |  |
| 10-21 02:30 | 29664.8 | 29704.1 | 29659.2 | 29677.0 | 29724.9 | 41.7 | 41 | dn |  |
| 10-21 02:45 | 29677.2 | 29689.0 | 29654.8 | 29659.4 | 29719.0 | 39.2 | 46 | dn |  |
| 10-21 03:00 | 29658.9 | 29722.8 | 29650.8 | 29704.2 | 29717.6 | 47.6 | 48 | dn |  |
| 10-21 03:15 | 29704.2 | 29761.8 | 29699.4 | 29761.0 | 29721.6 | 55.8 | 59 | dn | ← exit decided on this close |
| 10-21 03:30 | 29760.6 | 29762.0 | 29716.8 | 29732.8 | 29722.6 | 51.5 | 63 | dn |  |
| 10-21 03:45 | 29732.5 | 29753.8 | 29722.6 | 29749.0 | 29725.0 | 53.7 | 63 | dn |  |

## my_ema_rsi_15m · SHORT · entered 10-21 06:00 → exited 10-21 07:15 · close_past_ema21 · R -0.365 (best 0.49)

Logged entry reason: `my_ema_rsi_15m: 15min close 29637.20 < EMA21 29688.52, RSI 42.5, CHOP 53, Supertrend down`

Signal candle: **10-21 05:45** (15min); the trade opened right after it closed at 06:00.

| Measure | Value |
|---|---|
| close | 29637.20 |
| ema21 | 29688.52 |
| beyond EMA21 (ATR) | 1.01 |
| candles on this side of EMA21 (1 = this one just crossed) | 6 |
| RSI | 42.47 |
| RSI before | 46.04 |
| CHOP | 53.45 |
| EMA21 side changes in last 12 candles | 2 |
| Supertrend | -1 |
| last 3 closes | ↑↑↓ |
| signal candle body / range | 0.64 |
| signal candle range (ATR) | 0.98 |
| move since the 20-candle extreme (ATR) | 2.45 |
| closed beyond the prior 10-candle extreme | False |
| ADX(14) | 18.03 |
| EMA9 beyond EMA21 in the trade direction (ATR) | 0.49 |
| EMA9/21 crossed this many candles ago | >19 |
| EMA9/21 crosses in the last 20 candles | 0 |
| EMA21 slope over 8 candles in the trade direction (ATR) | 0.72 |
| RSI change over 3 candles | 1.68 |

Higher timeframes at that moment: 1h: close below EMA21, EMA21 > EMA50, RSI 49, Supertrend up → **with the trade**; 4h: close below EMA21, EMA21 < EMA50, RSI 44, Supertrend down → **with the trade**

| Candle (opens, NY) | O | H | L | C | EMA21 | RSI | CHOP | ST | |
|---|---|---|---|---|---|---|---|---|---|
| 10-21 03:45 | 29732.5 | 29753.8 | 29722.6 | 29749.0 | 29725.0 | 53.7 | 63 | dn |  |
| 10-21 04:00 | 29748.6 | 29757.0 | 29701.0 | 29726.8 | 29725.2 | 50.3 | 65 | dn |  |
| 10-21 04:15 | 29726.6 | 29745.4 | 29698.0 | 29729.2 | 29725.5 | 50.7 | 67 | dn |  |
| 10-21 04:30 | 29729.0 | 29729.8 | 29636.4 | 29651.8 | 29718.8 | 40.4 | 66 | dn |  |
| 10-21 04:45 | 29651.7 | 29662.0 | 29579.6 | 29588.0 | 29706.9 | 34.2 | 53 | dn |  |
| 10-21 05:00 | 29587.9 | 29632.8 | 29574.2 | 29631.0 | 29700.0 | 40.8 | 52 | dn |  |
| 10-21 05:15 | 29631.4 | 29658.6 | 29611.8 | 29657.0 | 29696.1 | 44.4 | 52 | dn |  |
| 10-21 05:30 | 29656.8 | 29702.2 | 29656.6 | 29669.0 | 29693.7 | 46.0 | 53 | dn |  |
| 10-21 05:45 | 29668.9 | 29676.4 | 29626.8 | 29637.2 | 29688.5 | 42.5 | 53 | dn | **SIGNAL candle (closed → entry)** |
| 10-21 06:00 | 29637.0 | 29643.5 | 29584.2 | 29585.8 | 29679.2 | 37.4 | 54 | dn | next candle (entry price) |
| 10-21 06:15 | 29585.6 | 29627.4 | 29569.9 | 29621.5 | 29673.9 | 42.5 | 54 | dn |  |
| 10-21 06:30 | 29621.4 | 29669.9 | 29609.4 | 29668.2 | 29673.4 | 48.5 | 54 | dn |  |
| 10-21 06:45 | 29668.1 | 29670.0 | 29646.4 | 29663.2 | 29672.5 | 47.9 | 52 | dn |  |
| 10-21 07:00 | 29663.2 | 29715.8 | 29661.6 | 29683.6 | 29673.5 | 50.4 | 53 | dn | ← exit decided on this close |
| 10-21 07:15 | 29683.4 | 29717.4 | 29669.6 | 29716.8 | 29677.4 | 54.4 | 54 | dn |  |
| 10-21 07:30 | 29717.2 | 29743.6 | 29687.9 | 29709.7 | 29680.4 | 53.4 | 57 | dn |  |

## my_ema_rsi_15m · LONG · entered 10-21 08:30 → exited 10-21 08:45 · close_past_ema21 · R -0.363 (best 0.04)

Logged entry reason: `my_ema_rsi_15m: 15min close 29730.40 > EMA21 29688.10, RSI 55.8, CHOP 51, Supertrend down`

Signal candle: **10-21 08:15** (15min); the trade opened right after it closed at 08:30.

| Measure | Value |
|---|---|
| close | 29730.40 |
| ema21 | 29688.10 |
| beyond EMA21 (ATR) | 0.88 |
| candles on this side of EMA21 (1 = this one just crossed) | 6 |
| RSI | 55.78 |
| RSI before | 50.61 |
| CHOP | 51.33 |
| EMA21 side changes in last 12 candles | 1 |
| Supertrend | -1 |
| last 3 closes | ↑↓↑ |
| signal candle body / range | 0.82 |
| signal candle range (ATR) | 0.99 |
| move since the 20-candle extreme (ATR) | 3.32 |
| closed beyond the prior 10-candle extreme | False |
| ADX(14) | 14.61 |
| EMA9 beyond EMA21 in the trade direction (ATR) | 0.13 |
| EMA9/21 crossed this many candles ago | 3 |
| EMA9/21 crosses in the last 20 candles | 1 |
| EMA21 slope over 8 candles in the trade direction (ATR) | 0.29 |
| RSI change over 3 candles | 2.38 |

Higher timeframes at that moment: 1h: close above EMA21, EMA21 > EMA50, RSI 54, Supertrend up → **with the trade**; 4h: close below EMA21, EMA21 < EMA50, RSI 44, Supertrend down → **AGAINST the trade**

| Candle (opens, NY) | O | H | L | C | EMA21 | RSI | CHOP | ST | |
|---|---|---|---|---|---|---|---|---|---|
| 10-21 06:15 | 29585.6 | 29627.4 | 29569.9 | 29621.5 | 29673.9 | 42.5 | 54 | dn |  |
| 10-21 06:30 | 29621.4 | 29669.9 | 29609.4 | 29668.2 | 29673.4 | 48.5 | 54 | dn |  |
| 10-21 06:45 | 29668.1 | 29670.0 | 29646.4 | 29663.2 | 29672.5 | 47.9 | 52 | dn |  |
| 10-21 07:00 | 29663.2 | 29715.8 | 29661.6 | 29683.6 | 29673.5 | 50.4 | 53 | dn |  |
| 10-21 07:15 | 29683.4 | 29717.4 | 29669.6 | 29716.8 | 29677.4 | 54.4 | 54 | dn |  |
| 10-21 07:30 | 29717.2 | 29743.6 | 29687.9 | 29709.7 | 29680.4 | 53.4 | 57 | dn |  |
| 10-21 07:45 | 29709.6 | 29734.4 | 29694.2 | 29711.0 | 29683.2 | 53.6 | 57 | dn |  |
| 10-21 08:00 | 29711.2 | 29714.8 | 29688.9 | 29691.0 | 29683.9 | 50.6 | 53 | dn |  |
| 10-21 08:15 | 29691.1 | 29736.8 | 29689.0 | 29730.4 | 29688.1 | 55.8 | 51 | dn | **SIGNAL candle (closed → entry)** |
| 10-21 08:30 | 29729.4 | 29730.0 | 29678.4 | 29683.9 | 29687.7 | 49.2 | 51 | dn | ← exit decided on this close |
| 10-21 08:45 | 29684.0 | 29708.2 | 29675.4 | 29700.2 | 29688.9 | 51.4 | 50 | dn |  |
| 10-21 09:00 | 29700.4 | 29729.9 | 29689.0 | 29695.9 | 29689.5 | 50.8 | 50 | dn |  |

## my_ema_rsi_15m · SHORT · entered 10-21 18:15 → exited 10-22 06:31 · stop · R 1.033 (best 2.78)

Logged entry reason: `my_ema_rsi_15m: 15min close 29747.40 < EMA21 29838.56, RSI 40.8, CHOP 54, Supertrend down`

Signal candle: **10-21 18:00** (15min); the trade opened right after it closed at 18:15.

| Measure | Value |
|---|---|
| close | 29747.40 |
| ema21 | 29838.56 |
| beyond EMA21 (ATR) | 1.47 |
| candles on this side of EMA21 (1 = this one just crossed) | 1 |
| RSI | 40.85 |
| RSI before | 53.21 |
| CHOP | 54.18 |
| EMA21 side changes in last 12 candles | 5 |
| Supertrend | -1 |
| last 3 closes | ↑↓↓ |
| signal candle body / range | 0.73 |
| signal candle range (ATR) | 0.98 |
| move since the 20-candle extreme (ATR) | 3.41 |
| closed beyond the prior 10-candle extreme | False |
| ADX(14) | 17.16 |
| EMA9 beyond EMA21 in the trade direction (ATR) | 0.09 |
| EMA9/21 crossed this many candles ago | 1 |
| EMA9/21 crosses in the last 20 candles | 1 |
| EMA21 slope over 8 candles in the trade direction (ATR) | 0.09 |
| RSI change over 3 candles | -9.55 |

Higher timeframes at that moment: 1h: close above EMA21, EMA21 > EMA50, RSI 59, Supertrend up → **AGAINST the trade**; 4h: close above EMA21, EMA21 < EMA50, RSI 53, Supertrend down → **AGAINST the trade**

| Candle (opens, NY) | O | H | L | C | EMA21 | RSI | CHOP | ST | |
|---|---|---|---|---|---|---|---|---|---|
| 10-21 15:00 | 29811.3 | 29812.1 | 29732.1 | 29795.1 | 29844.1 | 45.6 | 42 | up |  |
| 10-21 15:15 | 29794.8 | 29880.2 | 29792.1 | 29878.8 | 29847.2 | 55.4 | 45 | up |  |
| 10-21 15:30 | 29878.3 | 29884.2 | 29844.0 | 29867.6 | 29849.1 | 54.0 | 45 | up |  |
| 10-21 15:45 | 29867.7 | 29904.8 | 29840.1 | 29842.6 | 29848.5 | 50.9 | 46 | up |  |
| 10-21 16:00 | 29843.2 | 29901.4 | 29807.8 | 29808.4 | 29844.9 | 46.9 | 45 | up |  |
| 10-21 16:15 | 29808.6 | 29850.1 | 29800.6 | 29837.0 | 29844.1 | 50.4 | 45 | up |  |
| 10-21 16:30 | 29837.1 | 29873.6 | 29824.1 | 29866.8 | 29846.2 | 53.8 | 46 | up |  |
| 10-21 16:45 | 29866.6 | 29882.7 | 29854.6 | 29862.4 | 29847.7 | 53.2 | 50 | up |  |
| 10-21 18:00 | 29791.6 | 29794.4 | 29734.0 | 29747.4 | 29838.6 | 40.8 | 54 | dn | **SIGNAL candle (closed → entry)** |
| 10-21 18:15 | 29747.2 | 29748.4 | 29677.8 | 29690.7 | 29825.1 | 36.4 | 47 | dn | next candle (entry price) |
| 10-21 18:30 | 29690.6 | 29708.6 | 29681.6 | 29685.2 | 29812.4 | 36.0 | 47 | dn |  |
| 10-21 18:45 | 29685.1 | 29707.4 | 29680.0 | 29693.0 | 29801.5 | 37.0 | 47 | dn |  |
| 10-21 19:00 | 29693.1 | 29700.8 | 29651.9 | 29674.4 | 29790.0 | 35.5 | 47 | dn |  |
| 10-21 19:15 | 29673.8 | 29676.4 | 29627.1 | 29635.8 | 29776.0 | 32.5 | 42 | dn |  |
| 10-21 19:30 | 29635.6 | 29647.6 | 29616.7 | 29636.4 | 29763.3 | 32.5 | 39 | dn |  |
| 10-21 19:45 | 29636.4 | 29638.4 | 29601.4 | 29608.4 | 29749.2 | 30.4 | 34 | dn |  |
| 10-21 20:00 | 29608.2 | 29699.1 | 29607.9 | 29682.4 | 29743.1 | 41.5 | 37 | dn |  |
| 10-21 20:15 | 29682.2 | 29683.4 | 29614.6 | 29634.7 | 29733.3 | 37.4 | 37 | dn |  |
| 10-21 20:30 | 29634.4 | 29652.6 | 29618.4 | 29650.6 | 29725.8 | 39.5 | 37 | dn |  |
| 10-21 20:45 | 29650.4 | 29671.6 | 29633.6 | 29638.9 | 29717.9 | 38.5 | 36 | dn |  |
| 10-21 21:00 | 29639.0 | 29655.0 | 29611.8 | 29630.8 | 29709.9 | 37.7 | 36 | dn |  |
| 10-21 21:15 | 29630.9 | 29656.8 | 29602.0 | 29630.2 | 29702.7 | 37.7 | 51 | dn |  |
| 10-21 21:30 | 29629.6 | 29643.6 | 29576.4 | 29603.4 | 29693.7 | 35.0 | 53 | dn |  |
| 10-21 21:45 | 29603.6 | 29613.0 | 29574.0 | 29598.4 | 29685.0 | 34.6 | 60 | dn |  |
| 10-21 22:00 | 29598.8 | 29604.4 | 29560.6 | 29563.6 | 29674.0 | 31.3 | 58 | dn |  |
| 10-21 22:15 | 29563.8 | 29565.0 | 29528.0 | 29543.0 | 29662.1 | 29.6 | 52 | dn |  |
| 10-21 22:30 | 29543.1 | 29557.1 | 29525.2 | 29529.8 | 29650.0 | 28.4 | 51 | dn |  |
| 10-21 22:45 | 29529.2 | 29543.8 | 29517.3 | 29533.4 | 29639.4 | 29.2 | 48 | dn |  |
| 10-21 23:00 | 29533.3 | 29535.8 | 29495.1 | 29501.8 | 29626.9 | 26.5 | 44 | dn |  |
| 10-21 23:15 | 29502.0 | 29536.8 | 29496.6 | 29516.4 | 29616.9 | 29.8 | 44 | dn |  |
| 10-21 23:30 | 29515.6 | 29515.6 | 29464.6 | 29491.2 | 29605.5 | 27.5 | 39 | dn |  |
| 10-21 23:45 | 29491.1 | 29498.4 | 29459.2 | 29476.2 | 29593.7 | 26.2 | 39 | dn |  |
| 10-22 00:00 | 29476.8 | 29478.6 | 29456.9 | 29465.2 | 29582.0 | 25.3 | 37 | dn |  |
| 10-22 00:15 | 29465.0 | 29474.4 | 29446.3 | 29452.2 | 29570.2 | 24.2 | 37 | dn |  |
| 10-22 00:30 | 29451.8 | 29459.6 | 29427.8 | 29441.0 | 29558.5 | 23.3 | 33 | dn |  |
| 10-22 00:45 | 29441.6 | 29469.0 | 29434.1 | 29465.6 | 29550.0 | 29.7 | 34 | dn |  |
| 10-22 01:00 | 29465.8 | 29472.3 | 29441.6 | 29443.4 | 29540.3 | 27.4 | 37 | dn |  |
| 10-22 01:15 | 29443.3 | 29447.8 | 29411.8 | 29421.0 | 29529.5 | 25.4 | 36 | dn |  |
| 10-22 01:30 | 29421.2 | 29422.6 | 29369.8 | 29371.8 | 29515.2 | 21.5 | 36 | dn |  |
| 10-22 01:45 | 29372.4 | 29394.0 | 29353.1 | 29389.6 | 29503.7 | 25.9 | 35 | dn |  |
| 10-22 02:00 | 29389.4 | 29413.0 | 29357.4 | 29390.2 | 29493.4 | 26.0 | 39 | dn |  |
| 10-22 02:15 | 29390.4 | 29405.6 | 29353.6 | 29369.2 | 29482.1 | 24.2 | 42 | dn |  |
| 10-22 02:30 | 29368.8 | 29397.0 | 29357.4 | 29368.0 | 29471.7 | 24.1 | 42 | dn |  |
| 10-22 02:45 | 29368.2 | 29393.4 | 29358.0 | 29381.6 | 29463.6 | 27.9 | 46 | dn |  |
| 10-22 03:00 | 29381.6 | 29395.6 | 29315.4 | 29342.2 | 29452.5 | 24.1 | 44 | dn |  |
| 10-22 03:15 | 29343.0 | 29379.2 | 29327.8 | 29336.8 | 29442.0 | 23.7 | 49 | dn |  |
| 10-22 03:30 | 29336.6 | 29363.6 | 29330.4 | 29343.0 | 29433.0 | 25.5 | 50 | dn |  |
| 10-22 03:45 | 29343.0 | 29348.8 | 29310.0 | 29326.8 | 29423.3 | 23.9 | 50 | dn |  |
| 10-22 04:00 | 29326.6 | 29345.8 | 29295.8 | 29318.4 | 29413.8 | 23.1 | 48 | dn |  |
| 10-22 04:15 | 29318.4 | 29329.4 | 29300.4 | 29318.1 | 29405.1 | 23.0 | 48 | dn |  |
| 10-22 04:30 | 29317.9 | 29352.4 | 29300.6 | 29349.2 | 29400.0 | 32.8 | 55 | dn |  |
| 10-22 04:45 | 29349.0 | 29354.4 | 29264.1 | 29269.0 | 29388.1 | 24.3 | 56 | dn |  |
| 10-22 05:00 | 29269.0 | 29328.7 | 29262.4 | 29325.0 | 29382.4 | 36.6 | 59 | dn |  |
| 10-22 05:15 | 29324.8 | 29330.2 | 29276.6 | 29287.6 | 29373.8 | 32.8 | 60 | dn |  |
| 10-22 05:30 | 29287.6 | 29300.2 | 29270.2 | 29271.6 | 29364.5 | 31.3 | 60 | dn |  |
| 10-22 05:45 | 29271.0 | 29314.2 | 29271.0 | 29313.0 | 29359.8 | 39.1 | 62 | dn |  |
| 10-22 06:00 | 29313.6 | 29336.4 | 29296.9 | 29302.6 | 29354.6 | 37.9 | 62 | dn |  |
| 10-22 06:15 | 29302.6 | 29353.9 | 29291.4 | 29351.8 | 29354.3 | 46.1 | 64 | dn | ← exit decided on this close |
| 10-22 06:30 | 29351.7 | 29388.7 | 29349.9 | 29375.0 | 29356.2 | 49.5 | 64 | dn |  |
| 10-22 06:45 | 29374.6 | 29390.6 | 29349.8 | 29359.2 | 29356.5 | 47.3 | 63 | dn |  |

## my_ema_rsi_15m · SHORT · entered 10-22 09:15 → exited 10-22 09:30 · close_past_ema21 · R -0.493 (best 0.12)

Logged entry reason: `my_ema_rsi_15m: 15min close 29316.30 < EMA21 29351.19, RSI 42.7, CHOP 59, Supertrend down`

Signal candle: **10-22 09:00** (15min); the trade opened right after it closed at 09:15.

| Measure | Value |
|---|---|
| close | 29316.30 |
| ema21 | 29351.19 |
| beyond EMA21 (ATR) | 0.78 |
| candles on this side of EMA21 (1 = this one just crossed) | 2 |
| RSI | 42.69 |
| RSI before | 46.23 |
| CHOP | 59.14 |
| EMA21 side changes in last 12 candles | 4 |
| Supertrend | -1 |
| last 3 closes | ↓↓↓ |
| signal candle body / range | 0.67 |
| signal candle range (ATR) | 0.87 |
| move since the 20-candle extreme (ATR) | 1.85 |
| closed beyond the prior 10-candle extreme | False |
| ADX(14) | 26.76 |
| EMA9 beyond EMA21 in the trade direction (ATR) | 0.13 |
| EMA9/21 crossed this many candles ago | >19 |
| EMA9/21 crosses in the last 20 candles | 0 |
| EMA21 slope over 8 candles in the trade direction (ATR) | 0.04 |
| RSI change over 3 candles | -9.98 |

Higher timeframes at that moment: 1h: close below EMA21, EMA21 < EMA50, RSI 35, Supertrend down → **with the trade**; 4h: close below EMA21, EMA21 < EMA50, RSI 39, Supertrend down → **with the trade**

| Candle (opens, NY) | O | H | L | C | EMA21 | RSI | CHOP | ST | |
|---|---|---|---|---|---|---|---|---|---|
| 10-22 07:00 | 29359.3 | 29363.1 | 29318.1 | 29318.8 | 29353.1 | 42.2 | 63 | dn |  |
| 10-22 07:15 | 29318.6 | 29339.6 | 29292.2 | 29300.2 | 29348.3 | 40.1 | 64 | dn |  |
| 10-22 07:30 | 29300.6 | 29365.1 | 29297.2 | 29351.4 | 29348.5 | 47.9 | 65 | dn |  |
| 10-22 07:45 | 29351.2 | 29367.6 | 29338.1 | 29359.4 | 29349.5 | 49.1 | 65 | dn |  |
| 10-22 08:00 | 29359.7 | 29392.1 | 29347.8 | 29368.3 | 29351.2 | 50.3 | 64 | dn |  |
| 10-22 08:15 | 29368.4 | 29388.0 | 29360.7 | 29384.4 | 29354.3 | 52.7 | 60 | dn |  |
| 10-22 08:30 | 29384.7 | 29398.6 | 29363.0 | 29372.6 | 29355.9 | 50.8 | 59 | dn |  |
| 10-22 08:45 | 29372.6 | 29387.8 | 29340.6 | 29342.3 | 29354.7 | 46.2 | 58 | dn |  |
| 10-22 09:00 | 29342.2 | 29354.1 | 29315.4 | 29316.3 | 29351.2 | 42.7 | 59 | dn | **SIGNAL candle (closed → entry)** |
| 10-22 09:15 | 29316.2 | 29369.4 | 29304.1 | 29360.6 | 29352.0 | 49.8 | 67 | dn | ← exit decided on this close |
| 10-22 09:30 | 29360.8 | 29405.2 | 29310.6 | 29365.6 | 29353.3 | 50.5 | 68 | dn |  |
| 10-22 09:45 | 29365.2 | 29414.6 | 29281.6 | 29387.4 | 29356.4 | 53.7 | 66 | dn |  |

## my_ema_rsi_15m · SHORT · entered 10-22 20:30 → exited 10-22 20:47 · stop · R -1.0 (best 0.09)

Logged entry reason: `my_ema_rsi_15m: 15min close 28949.00 < EMA21 28986.42, RSI 42.2, CHOP 50, Supertrend down`

Signal candle: **10-22 20:15** (15min); the trade opened right after it closed at 20:30.

| Measure | Value |
|---|---|
| close | 28949.00 |
| ema21 | 28986.42 |
| beyond EMA21 (ATR) | 0.61 |
| candles on this side of EMA21 (1 = this one just crossed) | 38 |
| RSI | 42.18 |
| RSI before | 46.55 |
| CHOP | 49.67 |
| EMA21 side changes in last 12 candles | 0 |
| Supertrend | -1 |
| last 3 closes | ↑↑↓ |
| signal candle body / range | 0.55 |
| signal candle range (ATR) | 1.09 |
| move since the 20-candle extreme (ATR) | 1.93 |
| closed beyond the prior 10-candle extreme | False |
| ADX(14) | 30.73 |
| EMA9 beyond EMA21 in the trade direction (ATR) | 0.47 |
| EMA9/21 crossed this many candles ago | >19 |
| EMA9/21 crosses in the last 20 candles | 0 |
| EMA21 slope over 8 candles in the trade direction (ATR) | 0.63 |
| RSI change over 3 candles | 6.11 |

Higher timeframes at that moment: 1h: close below EMA21, EMA21 < EMA50, RSI 29, Supertrend down → **with the trade**; 4h: close below EMA21, EMA21 < EMA50, RSI 31, Supertrend down → **with the trade**

| Candle (opens, NY) | O | H | L | C | EMA21 | RSI | CHOP | ST | |
|---|---|---|---|---|---|---|---|---|---|
| 10-22 18:15 | 28989.6 | 29018.4 | 28971.0 | 28990.0 | 29025.1 | 42.7 | 62 | dn |  |
| 10-22 18:30 | 28990.2 | 28990.2 | 28956.9 | 28973.5 | 29020.5 | 41.2 | 60 | dn |  |
| 10-22 18:45 | 28974.0 | 28992.2 | 28959.9 | 28976.2 | 29016.4 | 41.5 | 57 | dn |  |
| 10-22 19:00 | 28976.0 | 28982.7 | 28936.0 | 28947.2 | 29010.1 | 38.6 | 58 | dn |  |
| 10-22 19:15 | 28947.0 | 28951.3 | 28925.4 | 28930.6 | 29002.9 | 37.0 | 56 | dn |  |
| 10-22 19:30 | 28930.8 | 28935.7 | 28895.4 | 28921.0 | 28995.5 | 36.1 | 55 | dn |  |
| 10-22 19:45 | 28921.2 | 28953.6 | 28899.2 | 28941.0 | 28990.5 | 39.5 | 55 | dn |  |
| 10-22 20:00 | 28940.9 | 28987.0 | 28876.0 | 28986.7 | 28990.2 | 46.5 | 53 | dn |  |
| 10-22 20:15 | 28985.4 | 28988.8 | 28922.2 | 28949.0 | 28986.4 | 42.2 | 50 | dn | **SIGNAL candle (closed → entry)** |
| 10-22 20:30 | 28949.2 | 28994.7 | 28944.6 | 28983.4 | 28986.1 | 47.1 | 58 | dn | ← exit decided on this close |
| 10-22 20:45 | 28983.2 | 29051.4 | 28972.8 | 29034.2 | 28990.5 | 53.3 | 53 | dn |  |
| 10-22 21:00 | 29034.2 | 29050.0 | 28949.2 | 28954.8 | 28987.3 | 44.5 | 57 | dn |  |

## my_ema_rsi_1h · LONG · entered 10-21 04:00 → exited 10-21 04:53 · stop · R -1.0 (best 0.05)

Logged entry reason: `my_ema_rsi_1h: 1h close 29749.00 > EMA21 29669.82, RSI 56.6, CHOP 51, Supertrend up`

Signal candle: **10-21 03:00** (1h); the trade opened right after it closed at 04:00.

| Measure | Value |
|---|---|
| close | 29749.00 |
| ema21 | 29669.82 |
| beyond EMA21 (ATR) | 0.75 |
| candles on this side of EMA21 (1 = this one just crossed) | 1 |
| RSI | 56.58 |
| RSI before | 50.91 |
| CHOP | 50.77 |
| EMA21 side changes in last 12 candles | 3 |
| Supertrend | 1 |
| last 3 closes | ↓↓↑ |
| signal candle body / range | 0.81 |
| signal candle range (ATR) | 1.06 |
| move since the 20-candle extreme (ATR) | 4.91 |
| closed beyond the prior 10-candle extreme | False |
| ADX(14) | 17.67 |
| EMA9 beyond EMA21 in the trade direction (ATR) | 0.43 |
| EMA9/21 crossed this many candles ago | 16 |
| EMA9/21 crosses in the last 20 candles | 1 |
| EMA21 slope over 8 candles in the trade direction (ATR) | 0.75 |
| RSI change over 3 candles | 0.47 |

Higher timeframes at that moment: 1h: close above EMA21, EMA21 > EMA50, RSI 57, Supertrend up → **with the trade**; 4h: close above EMA21, EMA21 < EMA50, RSI 49, Supertrend down → **with the trade**

| Candle (opens, NY) | O | H | L | C | EMA21 | RSI | CHOP | ST | |
|---|---|---|---|---|---|---|---|---|---|
| 10-20 19:00 | 29758.2 | 29766.4 | 29702.0 | 29747.0 | 29590.9 | 59.6 | 44 | up |  |
| 10-20 20:00 | 29746.8 | 29852.4 | 29706.1 | 29757.4 | 29606.0 | 60.1 | 42 | up |  |
| 10-20 21:00 | 29757.6 | 29844.8 | 29689.6 | 29822.8 | 29625.7 | 63.1 | 44 | up |  |
| 10-20 22:00 | 29822.9 | 29840.4 | 29791.2 | 29812.2 | 29642.7 | 62.3 | 44 | up |  |
| 10-20 23:00 | 29812.6 | 29831.4 | 29759.2 | 29764.8 | 29653.8 | 58.6 | 42 | up |  |
| 10-21 00:00 | 29764.6 | 29773.0 | 29726.9 | 29732.0 | 29660.9 | 56.1 | 54 | up |  |
| 10-21 01:00 | 29731.6 | 29741.7 | 29666.8 | 29674.8 | 29662.1 | 52.0 | 54 | up |  |
| 10-21 02:00 | 29674.7 | 29712.0 | 29654.8 | 29659.4 | 29661.9 | 50.9 | 51 | up |  |
| 10-21 03:00 | 29658.9 | 29762.0 | 29650.8 | 29749.0 | 29669.8 | 56.6 | 51 | up | ← exit decided on this close |
| 10-21 04:00 | 29748.6 | 29757.0 | 29579.6 | 29588.0 | 29662.4 | 46.2 | 53 | up |  |
| 10-21 05:00 | 29587.9 | 29702.2 | 29574.2 | 29637.2 | 29660.1 | 49.3 | 54 | up |  |

## my_ema_rsi_4h · SHORT · entered 10-21 05:00 → exited 10-21 09:00 · close_past_ema21 · R -0.359 (best 0.05)

Logged entry reason: `my_ema_rsi_4h: 4h close 29588.00 < EMA21 29688.22, RSI 43.6, CHOP 58, Supertrend down`

Signal candle: **10-21 01:00** (4h); the trade opened right after it closed at 05:00.

| Measure | Value |
|---|---|
| close | 29588.00 |
| ema21 | 29688.22 |
| beyond EMA21 (ATR) | 0.46 |
| candles on this side of EMA21 (1 = this one just crossed) | 1 |
| RSI | 43.64 |
| RSI before | 48.57 |
| CHOP | 57.63 |
| EMA21 side changes in last 12 candles | 2 |
| Supertrend | -1 |
| last 3 closes | ↑↓↓ |
| signal candle body / range | 0.79 |
| signal candle range (ATR) | 0.85 |
| move since the 20-candle extreme (ATR) | 2.14 |
| closed beyond the prior 10-candle extreme | False |
| ADX(14) | 29.62 |
| EMA9 beyond EMA21 in the trade direction (ATR) | 0.30 |
| EMA9/21 crossed this many candles ago | >19 |
| EMA9/21 crosses in the last 20 candles | 0 |
| EMA21 slope over 8 candles in the trade direction (ATR) | 0.41 |
| RSI change over 3 candles | -4.74 |

Higher timeframes at that moment: 1h: close below EMA21, EMA21 > EMA50, RSI 46, Supertrend up → **with the trade**; 4h: close below EMA21, EMA21 < EMA50, RSI 44, Supertrend down → **with the trade**

| Candle (opens, NY) | O | H | L | C | EMA21 | RSI | CHOP | ST | |
|---|---|---|---|---|---|---|---|---|---|
| 10-19 17:00 | 29606.8 | 29642.4 | 29444.2 | 29484.0 | 29777.4 | 37.6 | 44 | dn |  |
| 10-19 21:00 | 29484.1 | 29623.8 | 29415.5 | 29499.8 | 29752.2 | 38.2 | 44 | dn |  |
| 10-20 01:00 | 29500.0 | 29576.3 | 29422.0 | 29446.9 | 29724.4 | 36.9 | 44 | dn |  |
| 10-20 05:00 | 29446.8 | 29485.4 | 29318.1 | 29433.5 | 29698.0 | 36.6 | 44 | dn |  |
| 10-20 09:00 | 29433.2 | 29742.6 | 29231.3 | 29553.6 | 29684.8 | 41.8 | 50 | dn |  |
| 10-20 13:00 | 29553.8 | 29729.5 | 29498.9 | 29726.4 | 29688.6 | 48.4 | 56 | dn |  |
| 10-20 17:00 | 29799.8 | 29852.4 | 29702.0 | 29757.4 | 29694.9 | 49.5 | 55 | dn |  |
| 10-20 21:00 | 29757.6 | 29844.8 | 29689.6 | 29732.0 | 29698.2 | 48.6 | 56 | dn |  |
| 10-21 01:00 | 29731.6 | 29762.0 | 29579.6 | 29588.0 | 29688.2 | 43.6 | 58 | dn | **SIGNAL candle (closed → entry)** |
| 10-21 05:00 | 29587.9 | 29743.6 | 29569.9 | 29700.2 | 29689.3 | 48.1 | 58 | dn | ← exit decided on this close |
| 10-21 09:00 | 29700.4 | 29951.0 | 29614.2 | 29914.3 | 29709.8 | 55.3 | 55 | dn |  |
| 10-21 13:00 | 29914.4 | 29958.2 | 29732.1 | 29862.4 | 29723.6 | 53.3 | 56 | dn |  |

## my_ema_rsi_4h · SHORT · entered 10-22 01:00 → OPEN ·  · R - (best 1.05)

Logged entry reason: `my_ema_rsi_4h: 4h close 29465.60 < EMA21 29693.18, RSI 41.1, CHOP 56, Supertrend down`

Signal candle: **10-21 21:00** (4h); the trade opened right after it closed at 01:00.

| Measure | Value |
|---|---|
| close | 29465.60 |
| ema21 | 29693.18 |
| beyond EMA21 (ATR) | 1.01 |
| candles on this side of EMA21 (1 = this one just crossed) | 2 |
| RSI | 41.10 |
| RSI before | 45.89 |
| CHOP | 55.98 |
| EMA21 side changes in last 12 candles | 4 |
| Supertrend | -1 |
| last 3 closes | ↓↓↓ |
| signal candle body / range | 0.76 |
| signal candle range (ATR) | 1.02 |
| move since the 20-candle extreme (ATR) | 2.19 |
| closed beyond the prior 10-candle extreme | False |
| ADX(14) | 23.27 |
| EMA9 beyond EMA21 in the trade direction (ATR) | 0.14 |
| EMA9/21 crossed this many candles ago | 2 |
| EMA9/21 crosses in the last 20 candles | 2 |
| EMA21 slope over 8 candles in the trade direction (ATR) | -0.02 |
| RSI change over 3 candles | -14.18 |

Higher timeframes at that moment: 1h: close below EMA21, EMA21 < EMA50, RSI 36, Supertrend down → **with the trade**; 4h: close below EMA21, EMA21 < EMA50, RSI 41, Supertrend down → **with the trade**

| Candle (opens, NY) | O | H | L | C | EMA21 | RSI | CHOP | ST | |
|---|---|---|---|---|---|---|---|---|---|
| 10-20 13:00 | 29553.8 | 29729.5 | 29498.9 | 29726.4 | 29688.6 | 48.4 | 56 | dn |  |
| 10-20 17:00 | 29799.8 | 29852.4 | 29702.0 | 29757.4 | 29694.9 | 49.5 | 55 | dn |  |
| 10-20 21:00 | 29757.6 | 29844.8 | 29689.6 | 29732.0 | 29698.2 | 48.6 | 56 | dn |  |
| 10-21 01:00 | 29731.6 | 29762.0 | 29579.6 | 29588.0 | 29688.2 | 43.6 | 58 | dn |  |
| 10-21 05:00 | 29587.9 | 29743.6 | 29569.9 | 29700.2 | 29689.3 | 48.1 | 58 | dn |  |
| 10-21 09:00 | 29700.4 | 29951.0 | 29614.2 | 29914.3 | 29709.8 | 55.3 | 55 | dn |  |
| 10-21 13:00 | 29914.4 | 29958.2 | 29732.1 | 29862.4 | 29723.6 | 53.3 | 56 | dn |  |
| 10-21 17:00 | 29791.6 | 29794.4 | 29601.4 | 29638.9 | 29715.9 | 45.9 | 55 | dn |  |
| 10-21 21:00 | 29639.0 | 29656.8 | 29427.8 | 29465.6 | 29693.2 | 41.1 | 56 | dn | **SIGNAL candle (closed → entry)** |
| 10-22 01:00 | 29465.8 | 29472.3 | 29264.1 | 29269.0 | 29654.6 | 36.5 | 56 | dn | next candle (entry price) |
| 10-22 05:00 | 29269.0 | 29398.6 | 29262.4 | 29342.3 | 29626.2 | 39.2 | 55 | dn |  |
| 10-22 09:00 | 29342.2 | 29434.4 | 28988.4 | 29090.4 | 29577.5 | 33.8 | 48 | dn |  |
| 10-22 13:00 | 29090.7 | 29095.8 | 28886.9 | 28944.9 | 29520.0 | 31.1 | 44 | dn |  |
| 10-22 17:00 | 28980.8 | 29051.4 | 28876.0 | 29034.2 | 29475.8 | 34.5 | 40 | dn |  |
| 10-22 21:00 | 29034.2 | 29064.6 | 28909.3 | 29030.2 | 29435.3 | 34.4 | 39 | dn |  |

## my_rsi_15m · SHORT · entered 10-22 12:45 → exited 10-22 16:02 · stop · R 0.465 (best 1.07)

Logged entry reason: `my_rsi_15m: 15min close 29073.90 < EMA21 29226.84, RSI 33.0, CHOP 49, Supertrend down`

Signal candle: **10-22 12:30** (15min); the trade opened right after it closed at 12:45.

| Measure | Value |
|---|---|
| close | 29073.90 |
| ema21 | 29226.84 |
| beyond EMA21 (ATR) | 2.03 |
| candles on this side of EMA21 (1 = this one just crossed) | 11 |
| RSI | 32.97 |
| RSI before | 41.58 |
| CHOP | 48.93 |
| EMA21 side changes in last 12 candles | 1 |
| Supertrend | -1 |
| last 3 closes | ↑↓↓ |
| signal candle body / range | 0.96 |
| signal candle range (ATR) | 1.60 |
| move since the 20-candle extreme (ATR) | 4.78 |
| closed beyond the prior 10-candle extreme | False |
| ADX(14) | 25.07 |
| EMA9 beyond EMA21 in the trade direction (ATR) | 0.78 |
| EMA9/21 crossed this many candles ago | 11 |
| EMA9/21 crosses in the last 20 candles | 2 |
| EMA21 slope over 8 candles in the trade direction (ATR) | 1.24 |
| RSI change over 3 candles | -8.48 |

Higher timeframes at that moment: 1h: close below EMA21, EMA21 < EMA50, RSI 32, Supertrend down → **with the trade**; 4h: close below EMA21, EMA21 < EMA50, RSI 39, Supertrend down → **with the trade**

| Candle (opens, NY) | O | H | L | C | EMA21 | RSI | CHOP | ST | |
|---|---|---|---|---|---|---|---|---|---|
| 10-22 10:30 | 29204.4 | 29215.8 | 29125.8 | 29142.4 | 29320.5 | 29.2 | 44 | dn |  |
| 10-22 10:45 | 29142.0 | 29162.4 | 29095.6 | 29153.0 | 29305.3 | 30.8 | 41 | dn |  |
| 10-22 11:00 | 29152.8 | 29169.0 | 29073.6 | 29088.6 | 29285.6 | 26.8 | 40 | dn |  |
| 10-22 11:15 | 29088.0 | 29208.1 | 29080.8 | 29133.4 | 29271.7 | 33.2 | 43 | dn |  |
| 10-22 11:30 | 29133.6 | 29157.3 | 29082.6 | 29121.2 | 29258.0 | 32.4 | 44 | dn |  |
| 10-22 11:45 | 29120.4 | 29193.6 | 29107.1 | 29191.0 | 29251.9 | 41.5 | 46 | dn |  |
| 10-22 12:00 | 29191.3 | 29224.3 | 29156.8 | 29202.6 | 29247.5 | 42.8 | 47 | dn |  |
| 10-22 12:15 | 29203.0 | 29227.1 | 29183.7 | 29188.9 | 29242.1 | 41.6 | 47 | dn |  |
| 10-22 12:30 | 29189.0 | 29189.6 | 29069.2 | 29073.9 | 29226.8 | 33.0 | 49 | dn | **SIGNAL candle (closed → entry)** |
| 10-22 12:45 | 29074.2 | 29097.2 | 28988.4 | 29090.4 | 29214.4 | 35.1 | 43 | dn | next candle (entry price) |
| 10-22 13:00 | 29090.7 | 29095.8 | 29019.2 | 29053.9 | 29199.8 | 32.6 | 42 | dn |  |
| 10-22 13:15 | 29054.2 | 29087.2 | 29031.9 | 29061.7 | 29187.3 | 33.7 | 40 | dn |  |
| 10-22 13:30 | 29062.2 | 29090.4 | 29049.2 | 29080.9 | 29177.6 | 36.3 | 48 | dn |  |
| 10-22 13:45 | 29080.8 | 29084.2 | 29005.2 | 29010.2 | 29162.4 | 31.4 | 59 | dn |  |
| 10-22 14:00 | 29011.0 | 29024.4 | 28946.9 | 28994.8 | 29147.2 | 30.4 | 53 | dn |  |
| 10-22 14:15 | 28994.9 | 29062.2 | 28970.9 | 28974.2 | 29131.4 | 29.1 | 53 | dn |  |
| 10-22 14:30 | 28974.0 | 28979.6 | 28940.6 | 28975.9 | 29117.3 | 29.4 | 51 | dn |  |
| 10-22 14:45 | 28975.8 | 28979.8 | 28927.0 | 28933.2 | 29100.6 | 26.7 | 46 | dn |  |
| 10-22 15:00 | 28932.8 | 28974.6 | 28905.3 | 28953.6 | 29087.2 | 30.0 | 43 | dn |  |
| 10-22 15:15 | 28953.4 | 29007.8 | 28947.4 | 29005.0 | 29079.7 | 37.7 | 42 | dn |  |
| 10-22 15:30 | 29004.9 | 29007.7 | 28899.8 | 28916.2 | 29064.9 | 31.3 | 43 | dn |  |
| 10-22 15:45 | 28916.2 | 29011.8 | 28886.9 | 28999.2 | 29058.9 | 41.3 | 49 | dn | ← exit decided on this close |
| 10-22 16:00 | 28998.4 | 29067.6 | 28967.6 | 29003.8 | 29053.9 | 41.8 | 62 | dn |  |
| 10-22 16:15 | 29003.6 | 29007.0 | 28982.2 | 28995.6 | 29048.6 | 41.1 | 59 | dn |  |

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

## my_rsi_15m · SHORT · entered 10-22 19:15 → exited 10-22 20:48 · stop · R -1.0 (best 0.80)

Logged entry reason: `my_rsi_15m: 15min close 28947.20 < EMA21 29010.14, RSI 38.6, CHOP 58, Supertrend down`

Signal candle: **10-22 19:00** (15min); the trade opened right after it closed at 19:15.

| Measure | Value |
|---|---|
| close | 28947.20 |
| ema21 | 29010.14 |
| beyond EMA21 (ATR) | 1.03 |
| candles on this side of EMA21 (1 = this one just crossed) | 33 |
| RSI | 38.62 |
| RSI before | 41.54 |
| CHOP | 57.67 |
| EMA21 side changes in last 12 candles | 0 |
| Supertrend | -1 |
| last 3 closes | ↓↑↓ |
| signal candle body / range | 0.62 |
| signal candle range (ATR) | 0.76 |
| move since the 20-candle extreme (ATR) | 2.34 |
| closed beyond the prior 10-candle extreme | False |
| ADX(14) | 33.01 |
| EMA9 beyond EMA21 in the trade direction (ATR) | 0.60 |
| EMA9/21 crossed this many candles ago | >19 |
| EMA9/21 crosses in the last 20 candles | 0 |
| EMA21 slope over 8 candles in the trade direction (ATR) | 0.72 |
| RSI change over 3 candles | -4.13 |

Higher timeframes at that moment: 1h: close below EMA21, EMA21 < EMA50, RSI 30, Supertrend down → **with the trade**; 4h: close below EMA21, EMA21 < EMA50, RSI 31, Supertrend down → **with the trade**

| Candle (opens, NY) | O | H | L | C | EMA21 | RSI | CHOP | ST | |
|---|---|---|---|---|---|---|---|---|---|
| 10-22 16:00 | 28998.4 | 29067.6 | 28967.6 | 29003.8 | 29053.9 | 41.8 | 62 | dn |  |
| 10-22 16:15 | 29003.6 | 29007.0 | 28982.2 | 28995.6 | 29048.6 | 41.1 | 59 | dn |  |
| 10-22 16:30 | 28995.7 | 28996.0 | 28963.9 | 28968.6 | 29041.3 | 38.9 | 59 | dn |  |
| 10-22 16:45 | 28969.0 | 28969.2 | 28930.2 | 28944.9 | 29032.5 | 37.0 | 58 | dn |  |
| 10-22 18:00 | 28980.8 | 29001.7 | 28967.2 | 28989.8 | 29028.7 | 42.7 | 60 | dn |  |
| 10-22 18:15 | 28989.6 | 29018.4 | 28971.0 | 28990.0 | 29025.1 | 42.7 | 62 | dn |  |
| 10-22 18:30 | 28990.2 | 28990.2 | 28956.9 | 28973.5 | 29020.5 | 41.2 | 60 | dn |  |
| 10-22 18:45 | 28974.0 | 28992.2 | 28959.9 | 28976.2 | 29016.4 | 41.5 | 57 | dn |  |
| 10-22 19:00 | 28976.0 | 28982.7 | 28936.0 | 28947.2 | 29010.1 | 38.6 | 58 | dn | **SIGNAL candle (closed → entry)** |
| 10-22 19:15 | 28947.0 | 28951.3 | 28925.4 | 28930.6 | 29002.9 | 37.0 | 56 | dn | next candle (entry price) |
| 10-22 19:30 | 28930.8 | 28935.7 | 28895.4 | 28921.0 | 28995.5 | 36.1 | 55 | dn |  |
| 10-22 19:45 | 28921.2 | 28953.6 | 28899.2 | 28941.0 | 28990.5 | 39.5 | 55 | dn |  |
| 10-22 20:00 | 28940.9 | 28987.0 | 28876.0 | 28986.7 | 28990.2 | 46.5 | 53 | dn |  |
| 10-22 20:15 | 28985.4 | 28988.8 | 28922.2 | 28949.0 | 28986.4 | 42.2 | 50 | dn |  |
| 10-22 20:30 | 28949.2 | 28994.7 | 28944.6 | 28983.4 | 28986.1 | 47.1 | 58 | dn | ← exit decided on this close |
| 10-22 20:45 | 28983.2 | 29051.4 | 28972.8 | 29034.2 | 28990.5 | 53.3 | 53 | dn |  |
| 10-22 21:00 | 29034.2 | 29050.0 | 28949.2 | 28954.8 | 28987.3 | 44.5 | 57 | dn |  |

## Scan 10-21 17:00 → 10-21 20:00 on 15min: every candle, with the books' signals

| Candle (opens) | Close | EMA21 | RSI (before) | CHOP | ADX | EMA9-EMA21 (ATR) | ST | EMA+RSI rule | EMA9/21 rule | RSI60/40 rule | candles on this side | note |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 10-21 16:45 | 29862.4 | 29847.7 | 53.2 (53.8) | 50 | 17 | +0.12 | up |  |  |  | 2 ↑ |  |
| 10-21 18:00 | 29747.4 | 29838.6 | 40.8 (53.2) | 54 | 17 | -0.09 | dn | SELL | SELL |  | 1 ↓ |  |
| 10-21 18:15 | 29690.7 | 29825.1 | 36.4 (40.8) | 47 | 18 | -0.33 | dn |  |  |  | 2 ↓ | below EMA21 and RSI<44, but RSI did not CROSS 44 on this candle |
| 10-21 18:30 | 29685.2 | 29812.4 | 36.0 (36.4) | 47 | 19 | -0.53 | dn |  |  |  | 3 ↓ | below EMA21 and RSI<44, but RSI did not CROSS 44 on this candle |
| 10-21 18:45 | 29693.0 | 29801.5 | 37.0 (36.0) | 47 | 20 | -0.66 | dn |  |  |  | 4 ↓ | below EMA21 and RSI<44, but RSI did not CROSS 44 on this candle |
| 10-21 19:00 | 29674.4 | 29790.0 | 35.5 (37.0) | 47 | 22 | -0.78 | dn |  |  |  | 5 ↓ | below EMA21 and RSI<44, but RSI did not CROSS 44 on this candle |
| 10-21 19:15 | 29635.8 | 29776.0 | 32.5 (35.5) | 42 | 23 | -0.93 | dn |  |  |  | 6 ↓ | below EMA21 and RSI<44, but RSI did not CROSS 44 on this candle |
| 10-21 19:30 | 29636.4 | 29763.3 | 32.5 (32.5) | 39 | 25 | -1.05 | dn |  |  |  | 7 ↓ | below EMA21 and RSI<44, but RSI did not CROSS 44 on this candle |
| 10-21 19:45 | 29608.4 | 29749.2 | 30.4 (32.5) | 34 | 26 | -1.17 | dn |  |  |  | 8 ↓ | below EMA21 and RSI<44, but RSI did not CROSS 44 on this candle |

## Every logged signal on NDQ in the window (taken and skipped)

| Time (NY) | Book | What happened | Why |
|---|---|---|---|
| 10-21 01:15 | my_ema_cross_15m | rejected | stop too wide (3.2 ATR) |
| 10-21 01:15 | my_ema_rsi_15m | rejected | stop too wide (3.2 ATR) |
| 10-21 01:45 | my_ema_rsi_15m | taken | qty 2.78, jev 0.405 |
| 10-21 04:00 | my_ema_rsi_1h | taken | qty 2.8, jev 0.235 |
| 10-21 04:45 | my_ema_rsi_15m | rejected | choppy market (CHOP 65.7 ≥ 61.8) |
| 10-21 05:00 | my_ema_rsi_4h | taken | qty 1.1, jev 0.385 |
| 10-21 06:00 | my_ema_rsi_15m | taken | qty 2.59, jev 0.405 |
| 10-21 08:00 | my_ema_cross_15m | rejected | stop too wide (3.1 ATR) |
| 10-21 08:30 | my_ema_rsi_15m | taken | qty 2.58, jev 0.2325 |
| 10-21 11:00 | my_ema_rsi_15m | rejected | choppy market (CHOP 66.2 ≥ 61.8) |
| 10-21 11:00 | my_ema_rsi_1h | rejected | choppy market (CHOP 62.1 ≥ 61.8) |
| 10-21 13:00 | my_ema_rsi_4h | rejected | stop too wide (3.3 ATR) |
| 10-21 15:30 | my_ema_rsi_15m | rejected | trading halted: daily loss limit hit ($-1,471) |
| 10-21 17:00 | my_ema_cross_4h | rejected | stop too wide (3.1 ATR) |
| 10-21 18:15 | my_ema_cross_15m | taken | qty 2.02, jev 0.3775 |
| 10-21 18:15 | my_ema_rsi_15m | taken | qty 2.02, jev 0.3575 |
| 10-21 20:00 | my_ema_rsi_1h | rejected | stop too wide (3.2 ATR) |
| 10-21 21:00 | my_ema_cross_4h | taken | qty 0.93, jev 0.3725 |
| 10-21 22:00 | my_ema_cross_1h | rejected | stop too wide (3.4 ATR) |
| 10-21 22:00 | my_ema_rsi_1h | rejected | stop too wide (3.4 ATR) |
| 10-22 01:00 | my_ema_rsi_4h | taken | qty 0.64, jev 0.4425 |
| 10-22 07:15 | my_ema_rsi_15m | rejected | choppy market (CHOP 63.2 ≥ 61.8) |
| 10-22 09:15 | my_ema_rsi_15m | taken | qty 3.74, jev 0.4125 |
| 10-22 10:00 | my_ema_cross_15m | rejected | choppy market (CHOP 65.8 ≥ 61.8) |
| 10-22 10:15 | my_ema_cross_15m | rejected | choppy market (CHOP 65.1 ≥ 61.8) |
| 10-22 10:15 | my_ema_rsi_15m | rejected | choppy market (CHOP 65.1 ≥ 61.8) |
| 10-22 10:30 | my_rsi_15m | rejected | stop too wide (3.8 ATR) |
| 10-22 12:45 | my_rsi_15m | taken | qty 2.03, jev 0.4375 |
| 10-22 16:45 | my_rsi_15m | taken | qty 3.0, jev 0.435 |
| 10-22 17:00 | my_ema_rsi_1d | rejected | stop too wide (3.5 ATR) |
| 10-22 19:15 | my_rsi_15m | taken | qty 4.05, jev 0.4275 |
| 10-22 20:30 | my_ema_rsi_15m | taken | qty 5.94, jev 0.4275 |
| 10-22 21:45 | my_ema_cross_15m | taken | qty 1.85, jev 0.27 |
| 10-22 22:45 | my_ema_cross_15m | rejected | choppy market (CHOP 63.7 ≥ 61.8) |
