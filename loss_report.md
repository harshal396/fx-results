# RSI / EMA books report

Generated 2026-10-23 22:11 New York. Window: since 2026-10-22 18:00 (28 h). R = profit as a multiple of the risk at the first stop.

Books read: live, c10_afternoon, daily_rsi2_adx2, ema21_rsi55, h1_vol_trend, my_ema_cross_15m, my_ema_cross_1d, my_ema_cross_1h, my_ema_cross_4h, my_ema_rsi_15m, my_ema_rsi_1d, my_ema_rsi_1h, my_ema_rsi_4h, my_intraday_mom, my_rsi_15m, my_rsi_1h, my_rsi_4h, playbook_regime, shadow

## 1. Per book

| Book | Trades | Closed | Open | Wins | Total R | P&L | Avg best R | Avg hours held | Jev partials |
|---|---|---|---|---|---|---|---|---|---|
| live | 4 | 4 | 0 | 1 | -2.49 | -246.31 | 0.58 | 0.1 | 1 |
| c10_afternoon | 0 | 0 | 0 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 0 |
| daily_rsi2_adx2 | 0 | 0 | 0 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 0 |
| ema21_rsi55 | 1 | 1 | 0 | 1 | +0.20 | +13.65 | 0.38 | 2.8 | 0 |
| h1_vol_trend | 0 | 0 | 0 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 0 |
| my_ema_cross_15m | 4 | 4 | 0 | 2 | -0.14 | -50.84 | 0.61 | 2.8 | 2 |
| my_ema_cross_1d | 0 | 0 | 0 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 0 |
| my_ema_cross_1h | 2 | 1 | 1 | 1 | +0.96 | +339.43 | 1.90 | 7.0 | 0 |
| my_ema_cross_4h | 1 | 0 | 1 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 2 |
| my_ema_rsi_15m | 14 | 13 | 1 | 6 | -1.75 | -619.62 | 0.60 | 1.5 | 9 |
| my_ema_rsi_1d | 0 | 0 | 0 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 0 |
| my_ema_rsi_1h | 4 | 1 | 3 | 1 | +0.84 | +297.73 | 1.88 | 5.0 | 3 |
| my_ema_rsi_4h | 2 | 0 | 2 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 1 |
| my_intraday_mom | 2 | 2 | 0 | 1 | +0.16 | +57.89 | 0.22 | 0.5 | 0 |
| my_rsi_15m | 7 | 4 | 3 | 1 | -1.36 | -480.45 | 0.66 | 1.7 | 4 |
| my_rsi_1h | 2 | 0 | 2 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 1 |
| my_rsi_4h | 1 | 0 | 1 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 0 |
| playbook_regime | 3 | 2 | 1 | 1 | -0.50 | -148.16 | 0.83 | 0.5 | 1 |
| shadow | 7 | 5 | 2 | 0 | -4.27 | -890.24 | 0.31 | 0.9 | 0 |

All listed books: 37 closed trades, -8.34 R.

## 2. Why the losing trades lost

| Cause | Trades | R |
|---|---|---|
| stopped at the first stop | 11 | -8.86 |
| closed on the EMA exit at a loss | 8 | -4.11 |
| gave back: was +0.5R or better first | 3 | -3.01 |

## 3. Skipped signals (what the filters blocked)

**live**: 8x filtered: counter to BEARISH bias; 5x skipped: Jev quality # < #; 2x taken: qty #, risk $#, cost #R; 2x skipped: Jev confidence # < #; 2x taken: qty #, risk $#, cost #R (over the #R cap — log only); 2x skipped: Jev quality # < # and confidence # < #
**ema21_rsi55**: 2x rejected: choppy market (CHOP # ≥ #); 1x taken: qty #, jev #
**my_ema_cross_15m**: 4x taken: qty #, jev #; 4x rejected: choppy market (CHOP # ≥ #); 3x rejected: stop too wide (# ATR)
**my_ema_cross_1h**: 1x taken: qty #, jev #
**my_ema_rsi_15m**: 13x taken: qty #, jev #; 6x rejected: stop too wide (# ATR); 6x rejected: choppy market (CHOP # ≥ #); 1x rejected: market closed (weekend / flat before the weekend)
**my_ema_rsi_1h**: 2x taken: qty #, jev #; 1x rejected: news blackout: Revised UoM Consumer Sentiment
**my_intraday_mom**: 2x taken: qty #, jev None
**my_rsi_15m**: 4x taken: qty #, jev #; 3x rejected: stop too wide (# ATR)
**my_rsi_1h**: 3x rejected: choppy market (CHOP # ≥ #); 1x taken: qty #, jev #
**playbook_regime**: 18x skipped: regime chop (Jev chop #, CHOP #): scalps only; 13x filtered: counter to BEARISH bias; 3x skipped: Jev quality # < #; 3x filtered: bias neutral (#); 2x taken: qty #, risk $#, cost #R; 2x filtered: counter to BULLISH bias; 2x rejected: outside entry windows; 1x skipped: Jev confidence # < #
**shadow**: 13x filtered: counter to BEARISH bias; 12x skipped: Jev quality # < #; 5x taken: qty #, risk $#, cost #R; 4x rejected: outside entry windows; 3x filtered: bias neutral (#); 2x skipped: Jev confidence # < #; 2x filtered: counter to BULLISH bias; 2x skipped: Jev quality # < # and confidence # < #

## 4. Trade analyst (shadow) - how its advice scored

| Book | Check | Times | Avg value in R (positive = its advice would have helped) | Helpful |
|---|---|---|---|---|
| live | any_exit | 3 | +0.22 | 2 |
| live | giveback | 4 | +0.04 | 3 |
| live | h1_against | 3 | -0.48 | 1 |
| live | stall | 1 | +0.63 | 1 |
| live | structure_break | 3 | +0.22 | 2 |
| live | trend_flip | 2 | -0.14 | 1 |
| c10_afternoon | any_exit | 1 | -0.65 | 0 |
| c10_afternoon | giveback | 1 | -1.33 | 0 |
| c10_afternoon | structure_break | 1 | -0.65 | 0 |
| ema21_rsi55 | any_exit | 4 | -0.04 | 1 |
| ema21_rsi55 | giveback | 1 | -0.05 | 0 |
| ema21_rsi55 | h1_against | 3 | -0.07 | 2 |
| ema21_rsi55 | stall | 3 | +0.01 | 2 |
| ema21_rsi55 | structure_break | 3 | -0.04 | 0 |
| h1_vol_trend | any_exit | 1 | -0.90 | 0 |
| h1_vol_trend | stall | 1 | -0.96 | 0 |
| h1_vol_trend | structure_break | 1 | -0.90 | 0 |
| my_ema_cross_15m | any_exit | 3 | -0.26 | 2 |
| my_ema_cross_15m | giveback | 1 | +0.03 | 1 |
| my_ema_cross_15m | h1_against | 5 | -0.00 | 3 |
| my_ema_cross_15m | stall | 1 | -0.68 | 0 |
| my_ema_cross_15m | structure_break | 3 | -0.16 | 2 |
| my_ema_cross_15m | trend_flip | 1 | -0.81 | 0 |
| my_ema_cross_1h | any_exit | 3 | +0.16 | 2 |
| my_ema_cross_1h | h1_against | 2 | +0.62 | 2 |
| my_ema_cross_1h | stall | 2 | +0.81 | 2 |
| my_ema_cross_1h | structure_break | 3 | +0.07 | 2 |
| my_ema_cross_1h | trend_flip | 1 | +0.55 | 1 |
| my_ema_rsi_15m | any_exit | 14 | +0.04 | 8 |
| my_ema_rsi_15m | giveback | 2 | +0.10 | 2 |
| my_ema_rsi_15m | h1_against | 15 | +0.21 | 11 |
| my_ema_rsi_15m | stall | 5 | -0.08 | 2 |
| my_ema_rsi_15m | structure_break | 12 | -0.01 | 5 |
| my_ema_rsi_15m | trend_flip | 4 | +0.32 | 4 |
| my_ema_rsi_1h | any_exit | 5 | +0.32 | 4 |
| my_ema_rsi_1h | giveback | 1 | +0.07 | 1 |
| my_ema_rsi_1h | h1_against | 2 | +0.62 | 2 |
| my_ema_rsi_1h | stall | 3 | +0.68 | 3 |
| my_ema_rsi_1h | structure_break | 5 | +0.27 | 4 |
| my_ema_rsi_1h | trend_flip | 3 | +0.36 | 3 |
| my_ema_rsi_4h | any_exit | 1 | +0.25 | 1 |
| my_ema_rsi_4h | h1_against | 1 | +0.12 | 1 |
| my_ema_rsi_4h | stall | 1 | +0.25 | 1 |
| my_ema_rsi_4h | structure_break | 1 | -0.02 | 0 |
| my_ema_rsi_4h | trend_flip | 1 | +0.05 | 1 |
| my_intraday_mom | any_exit | 3 | +0.08 | 2 |
| my_intraday_mom | h1_against | 2 | +0.17 | 2 |
| my_intraday_mom | structure_break | 3 | +0.08 | 2 |
| my_rsi_15m | any_exit | 4 | +0.14 | 3 |
| my_rsi_15m | giveback | 1 | +0.05 | 1 |
| my_rsi_15m | stall | 3 | +0.03 | 2 |
| my_rsi_15m | structure_break | 4 | +0.18 | 3 |
| playbook_regime | any_exit | 1 | -0.54 | 0 |
| playbook_regime | giveback | 3 | -0.04 | 2 |
| playbook_regime | stall | 1 | -0.19 | 0 |
| playbook_regime | structure_break | 1 | -0.54 | 0 |
| shadow | any_exit | 14 | -0.08 | 7 |
| shadow | giveback | 5 | +0.03 | 4 |
| shadow | h1_against | 5 | -0.11 | 2 |
| shadow | stall | 9 | +0.08 | 5 |
| shadow | structure_break | 12 | -0.15 | 6 |
| shadow | trend_flip | 3 | +0.22 | 3 |

## 5. Every trade in the window

| Book | Id | Market | Side | Opened (NY) | Closed (NY) | Entry | Exit | First stop | Stop at end | Qty | P&L | R | Best R | Worst R | How it ended |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ema21_rsi55 | a13aebfa | US30 | SHORT | 10-23 13:00 | 10-23 15:50 | 52333.10 | 52278.50 | 52613.60 | 52613.60 | 0.25 | 13.65 | 0.20 | 0.38 | -0.04 | session_flat |
| live | b871757d | US30 | LONG | 10-22 20:40 | 10-22 21:03 | 52908.90 | 52866.90 | 52867.50 | 52867.50 | 2.79 | -117.18 | -1.01 | 0.52 | -0.82 | stop |
| live | 3850d8cc | US30 | LONG | 10-23 02:55 | 10-23 02:56 | 52776.90 | 52763.90 | 52764.00 | 52764.00 | 2.79 | -36.27 | -1.01 | 0.31 | -0.35 | stop |
| live | 9d73f905 | NDQ | SHORT | 10-23 03:05 | 10-23 03:06 | 29034.90 | 29058.70 | 29058.60 | 29058.60 | 5.08 | -120.90 | -1.00 | 0.28 | -0.09 | stop |
| live | 207db6a7 | XAUUSD | SHORT | 10-23 08:30 | 10-23 08:32 | 4028.95 | 4028.75 | 4031.55 | 4028.69 | 19.90 | 28.04 | 0.54 | 1.21 | -0.40 | breakeven_plus_stop |
| my_ema_cross_15m | 582cf1cd | US30 | SHORT | 10-22 21:30 | 10-23 07:02 | 52821.40 | 52642.50 | 52990.20 | 52642.50 | 2.10 | 283.10 | 0.80 | 1.67 | -0.06 | stop |
| my_ema_cross_15m | d25abfa4 | NDQ | LONG | 10-22 21:45 | 10-22 22:00 | 29049.80 | 28975.40 | 28858.30 | 28858.30 | 1.85 | -137.64 | -0.39 | 0.08 | -0.48 | close_past_ema21 |
| my_ema_cross_15m | c23166cb | XAUUSD | LONG | 10-23 03:45 | 10-23 04:00 | 4019.83 | 4011.26 | 4009.77 | 4009.77 | 35.30 | -302.70 | -0.85 | 0.16 | -0.88 | close_past_ema21 |
| my_ema_cross_15m | fb02ed70 | NDQ | SHORT | 10-23 15:00 | 10-23 16:00 | 29006.40 | 28979.80 | 29094.80 | 29094.80 | 4.00 | 106.40 | 0.30 | 0.55 | -0.14 | weekend_close |
| my_ema_cross_1h | 1311e5cd | US30 | LONG | 10-22 11:00 | open | 52688.10 |  | 52441.20 | 52688.10 | 1.42 | 0.00 |  | 1.12 | -0.18 | OPEN |
| my_ema_cross_1h | 1ad10fff | US30 | SHORT | 10-23 04:00 | 10-23 11:00 | 52674.90 | 52363.50 | 52997.80 | 52490.80 | 1.09 | 339.43 | 0.96 | 1.90 | -0.24 | trail_through |
| my_ema_cross_4h | f1537166 | NDQ | SHORT | 10-21 21:00 | open | 29637.80 |  | 30014.40 | 29351.10 | 0.93 | 236.81 |  | 1.99 | -0.05 | OPEN |
| my_ema_rsi_15m | c94efac9 | US30 | LONG | 10-22 15:30 | open | 52852.50 |  | 52692.40 | 52692.40 | 2.21 | 0.00 |  | 0.00 | 0.00 | OPEN |
| my_ema_rsi_15m | c3beb17d | NDQ | SHORT | 10-22 20:30 | 10-22 20:47 | 28947.80 | 29007.60 | 29007.60 | 29007.60 | 5.94 | -355.21 | -1.00 | 0.09 | -0.78 | stop |
| my_ema_rsi_15m | e65e56f9 | XAUUSD | SHORT | 10-23 00:15 | 10-23 01:15 | 4009.78 | 4015.48 | 4026.72 | 4026.72 | 20.80 | -118.66 | -0.34 | 0.45 | -0.40 | close_past_ema21 |
| my_ema_rsi_15m | 432fdb56 | US30 | SHORT | 10-23 00:15 | 10-23 04:34 | 52770.40 | 52752.30 | 52839.70 | 52752.30 | 5.09 | 191.44 | 0.54 | 1.58 | -0.56 | stop |
| my_ema_rsi_15m | f5f3f978 | NDQ | LONG | 10-23 03:15 | 10-23 03:45 | 29062.40 | 29018.30 | 28944.80 | 28944.80 | 3.00 | -132.30 | -0.38 | 0.07 | -0.40 | close_past_ema21 |
| my_ema_rsi_15m | bc90b02c | NDQ | LONG | 10-23 04:15 | 10-23 05:15 | 29094.80 | 29041.00 | 28994.70 | 28994.70 | 3.53 | -189.91 | -0.54 | 0.37 | -0.59 | close_past_ema21 |
| my_ema_rsi_15m | 31438490 | US30 | SHORT | 10-23 04:45 | 10-23 07:02 | 52696.40 | 52642.50 | 52821.50 | 52642.50 | 2.81 | 200.67 | 0.57 | 1.26 | -0.10 | stop |
| my_ema_rsi_15m | e49250ba | NDQ | SHORT | 10-23 06:45 | 10-23 09:45 | 28966.40 | 28979.40 | 29108.20 | 29108.20 | 2.49 | 140.49 | 0.40 | 0.88 | -0.22 | close_past_ema21 |
| my_ema_rsi_15m | 6131dc53 | XAUUSD | LONG | 10-23 07:15 | 10-23 08:15 | 4028.89 | 4022.02 | 4018.55 | 4018.55 | 34.10 | -234.44 | -0.67 | 0.21 | -0.70 | close_past_ema21 |
| my_ema_rsi_15m | d21c15b9 | US30 | SHORT | 10-23 11:45 | 10-23 12:00 | 52336.10 | 52407.50 | 52483.10 | 52483.10 | 2.39 | -170.65 | -0.49 | 0.11 | -0.58 | close_past_ema21 |
| my_ema_rsi_15m | 7d1f4801 | XAUUSD | SHORT | 10-23 12:30 | 10-23 14:26 | 4001.28 | 4001.28 | 4008.39 | 4001.28 | 49.40 | 182.80 | 0.52 | 1.44 | -0.74 | stop |
| my_ema_rsi_15m | 21739a3a | NDQ | LONG | 10-23 12:45 | 10-23 13:09 | 29110.60 | 29043.70 | 29043.70 | 29043.70 | 5.25 | -351.22 | -1.00 | 0.28 | -0.91 | stop |
| my_ema_rsi_15m | 9e47835a | US30 | SHORT | 10-23 13:00 | 10-23 16:00 | 52333.10 | 52236.50 | 52481.80 | 52481.80 | 2.35 | 205.25 | 0.59 | 0.79 | -0.07 | weekend_close |
| my_ema_rsi_15m | 946b389f | NDQ | SHORT | 10-23 15:45 | 10-23 16:00 | 28983.60 | 28979.80 | 29093.50 | 29093.50 | 3.19 | 12.12 | 0.04 | 0.24 | -0.13 | weekend_close |
| my_ema_rsi_1h | c33f7974 | US30 | LONG | 10-21 12:00 | open | 52683.10 |  | 52392.50 | 52697.70 | 1.21 | 192.06 |  | 1.03 | -0.20 | OPEN |
| my_ema_rsi_1h | 216b658a | US30 | LONG | 10-22 12:00 | open | 52865.10 |  | 52439.40 | 52439.40 | 0.82 | 0.00 |  | 0.00 | 0.00 | OPEN |
| my_ema_rsi_1h | 799e7790 | US30 | SHORT | 10-23 06:00 | 10-23 11:00 | 52581.40 | 52363.50 | 52856.50 | 52490.80 | 1.29 | 297.73 | 0.84 | 1.88 | -0.22 | trail_through |
| my_ema_rsi_1h | a93c25b2 | NDQ | SHORT | 10-23 16:00 | open | 28977.60 |  | 29205.50 | 29205.50 | 1.56 | 0.00 |  | 0.00 | 0.00 | OPEN |
| my_ema_rsi_4h | 632887d2 | NDQ | SHORT | 10-22 01:00 | open | 29464.40 |  | 30014.50 | 29351.10 | 0.64 | 165.89 |  | 1.05 | -0.01 | OPEN |
| my_ema_rsi_4h | c0daa33b | US30 | LONG | 10-22 09:00 | open | 52588.50 |  | 52365.40 | 52588.50 | 1.58 | 0.00 |  | 1.69 | -0.25 | OPEN |
| my_intraday_mom | e97a9539 | NDQ | LONG | 10-23 15:30 | 10-23 16:00 | 28998.80 | 28977.60 | 28835.00 | 28835.00 | 2.16 | -45.79 | -0.13 | 0.05 | -0.25 | session_close |
| my_intraday_mom | 0e0a3f01 | US30 | SHORT | 10-23 15:30 | 10-23 16:00 | 52300.50 | 52236.50 | 52518.50 | 52518.50 | 1.62 | 103.68 | 0.29 | 0.39 | -0.01 | session_close |
| my_rsi_15m | d5f69550 | XAUUSD | SHORT | 10-22 11:15 | open | 4054.70 |  | 4084.20 | 4034.91 | 11.90 | 159.92 |  | 1.14 | -0.22 | OPEN |
| my_rsi_15m | fcd1d2ed | US30 | LONG | 10-22 16:00 | open | 52912.50 |  | 52692.50 | 52692.50 | 1.61 | 0.00 |  | 0.00 | 0.00 | OPEN |
| my_rsi_15m | 9971e243 | NDQ | SHORT | 10-22 16:45 | open | 28967.40 |  | 29085.60 | 29085.60 | 3.00 | 0.00 |  | 0.00 | 0.00 | OPEN |
| my_rsi_15m | 95bbb3aa | XAUUSD | SHORT | 10-22 19:00 | 10-22 20:49 | 4027.39 | 4027.39 | 4034.36 | 4027.39 | 50.90 | 194.37 | 0.55 | 1.52 | -0.26 | stop |
| my_rsi_15m | ba5a4ccd | NDQ | SHORT | 10-22 19:15 | 10-22 20:48 | 28946.00 | 29033.70 | 29033.70 | 29033.70 | 4.05 | -355.19 | -1.00 | 0.80 | -0.74 | stop |
| my_rsi_15m | a3960d9b | XAUUSD | SHORT | 10-23 00:30 | 10-23 01:15 | 4005.84 | 4015.48 | 4026.64 | 4026.64 | 17.00 | -163.96 | -0.46 | 0.17 | -0.51 | close_past_ema21 |
| my_rsi_15m | 95337acf | XAUUSD | SHORT | 10-23 13:30 | 10-23 16:00 | 3993.55 | 4000.26 | 4008.72 | 4008.72 | 23.20 | -155.67 | -0.44 | 0.16 | -0.57 | weekend_close |
| my_rsi_1h | af640ece | US30 | LONG | 10-22 16:00 | open | 52912.50 |  | 52495.40 | 52495.40 | 0.84 | 0.00 |  | 0.00 | 0.00 | OPEN |
| my_rsi_1h | 4f472e7e | XAUUSD | SHORT | 10-23 03:00 | open | 4012.62 |  | 4036.67 | 4004.19 | 14.70 | 89.42 |  | 1.54 | -0.89 | OPEN |
| my_rsi_4h | 3750c941 | US30 | LONG | 10-22 13:00 | open | 52842.50 |  | 52361.90 | 52361.90 | 0.73 | 0.00 |  | 0.00 | 0.00 | OPEN |
| playbook_regime | 05bac06e | US30 | LONG | 10-20 20:30 | open | 52554.50 |  | 52437.60 | 52437.60 | 2.78 | 0.00 |  | 0.00 | 0.00 | OPEN |
| playbook_regime | ac77a940 | NDQ | SHORT | 10-22 20:10 | 10-22 20:13 | 28895.10 | 28956.90 | 28956.90 | 28956.90 | 5.11 | -315.80 | -1.00 | 0.31 | -0.75 | stop |
| playbook_regime | b5a1d520 | NDQ | SHORT | 10-23 08:30 | 10-23 09:32 | 28936.40 | 28929.80 | 29001.90 | 28929.80 | 5.08 | 167.64 | 0.50 | 1.34 | -0.17 | breakeven_plus_stop |
| shadow | ebcda2f4 | NDQ | SHORT | 10-19 22:15 | open | 29545.40 |  | 29647.70 | 29647.70 | 3.34 | 0.00 |  | 0.00 | 0.00 | OPEN |
| shadow | 4dfb39be | US30 | LONG | 10-20 20:30 | open | 52554.50 |  | 52437.60 | 52437.60 | 2.73 | 0.00 |  | 0.00 | 0.00 | OPEN |
| shadow | 3ca3d2af | NDQ | SHORT | 10-22 20:10 | 10-22 20:13 | 28895.10 | 28956.90 | 28956.90 | 28956.90 | 5.11 | -315.80 | -1.00 | 0.31 | -0.75 | stop |
| shadow | c540b744 | XAUUSD | SHORT | 10-22 22:09 | 10-22 22:18 | 4006.34 | 4015.62 | 4015.62 | 4015.62 | 20.00 | -185.52 | -1.00 | 0.08 | -0.94 | stop |
| shadow | fd268000 | XAUUSD | SHORT | 10-23 03:51 | 10-23 04:45 | 4015.28 | 4022.31 | 4022.31 | 4022.31 | 19.90 | -139.76 | -1.00 | 0.80 | -0.67 | stop |
| shadow | 549a7441 | XAUUSD | SHORT | 10-23 13:30 | 10-23 15:50 | 3993.55 | 4000.63 | 4006.95 | 4006.95 | 20.00 | -141.60 | -0.53 | 0.19 | -0.65 | session_flat |
| shadow | d0e533d2 | XAUUSD | SHORT | 10-23 14:42 | 10-23 15:50 | 3995.22 | 4000.63 | 4002.49 | 4002.49 | 19.90 | -107.56 | -0.74 | 0.18 | -0.80 | session_flat |

## 6. Timelines of the losing and the open trades

- **live** US30 LONG b871757d → stop (-1.01R, best 0.52R): 20:40 entry (52867.5); 20:40 target_placed; 20:45 analyst (5m structure broke); 20:50 analyst (trade on track); 21:03 exit
- **live** US30 LONG 3850d8cc → stop (-1.01R, best 0.31R): 02:55 entry (52764.0); 02:55 target_placed; 02:56 exit
- **live** NDQ SHORT 9d73f905 → stop (-1.00R, best 0.28R): 03:05 entry (29058.6); 03:05 target_placed; 03:06 exit
- **my_ema_cross_15m** NDQ LONG d25abfa4 → close_past_ema21 (-0.39R, best 0.08R): 21:45 entry (28858.300000000003); 21:45 analyst (1H trend is against the trade); 22:00 exit_signal; 22:00 exit
- **my_ema_cross_15m** XAUUSD LONG c23166cb → close_past_ema21 (-0.85R, best 0.16R): 03:45 entry (4009.766); 03:45 analyst (1H trend is against the trade); 04:00 exit_signal; 04:00 exit
- **my_ema_cross_1h** US30 LONG 1311e5cd → OPEN (R, best 1.12R): 11:00 entry (52441.200000000004); 11:00 analyst (trade on track); 12:00 agent_check (continuation 0.50 ≥ 0.45); 12:45 analyst (gave back half of a ≥1R open profit); 12:55 analyst (trade on track); 13:00 agent_check (continuation 0.50 ≥ 0.45); 13:00 stop_moved (breakeven / 2×ATR trail after +1R)
- **my_ema_cross_4h** NDQ SHORT f1537166 → OPEN (R, best 1.99R): 21:00 entry (30014.4); 21:00 analyst (trade on track); 04:45 analyst (5m structure broke); 04:50 analyst (trade on track); 05:00 partial (Jev: continuation 0.43 < 0.45); 06:30 analyst (5m structure broke); 06:50 analyst (trade on track); 08:05 analyst (5m structure broke); 08:10 analyst (trade on track); 08:15 analyst (5m structure broke); 08:30 analyst (trade on track); 09:00 partial (Jev: continuation 0.42 < 0.45); 09:30 analyst (5m structure broke); 09:50 analyst (trade on track)
- **my_ema_rsi_15m** US30 LONG c94efac9 → OPEN (R, best 0.00R): 15:30 entry (52692.4)
- **my_ema_rsi_15m** NDQ SHORT c3beb17d → stop (-1.00R, best 0.09R): 20:30 entry (29007.600000000002); 20:30 analyst (trade on track); 20:47 exit
- **my_ema_rsi_15m** XAUUSD SHORT e65e56f9 → close_past_ema21 (-0.34R, best 0.45R): 00:15 entry (4026.716); 00:15 analyst (trade on track); 01:15 exit_signal; 01:15 exit
- **my_ema_rsi_15m** NDQ LONG f5f3f978 → close_past_ema21 (-0.38R, best 0.07R): 03:15 entry (28944.800000000003); 03:15 analyst (1H trend is against the trade); 03:30 analyst (15m trend flipped against the trade; 1H trend is); 03:45 exit_signal; 03:45 exit
- **my_ema_rsi_15m** NDQ LONG bc90b02c → close_past_ema21 (-0.54R, best 0.37R): 04:15 entry (28994.7); 04:15 analyst (1H trend is against the trade); 05:15 exit_signal; 05:15 exit
- **my_ema_rsi_15m** XAUUSD LONG 6131dc53 → close_past_ema21 (-0.67R, best 0.21R): 07:15 entry (4018.552); 07:15 analyst (1H trend is against the trade); 08:15 exit_signal; 08:15 exit
- **my_ema_rsi_15m** US30 SHORT d21c15b9 → close_past_ema21 (-0.49R, best 0.11R): 11:45 entry (52483.100000000006); 11:45 analyst (trade on track); 12:00 exit_signal; 12:00 exit
- **my_ema_rsi_15m** NDQ LONG 21739a3a → stop (-1.00R, best 0.28R): 12:45 entry (29043.7); 12:45 analyst (1H trend is against the trade); 13:00 analyst (5m structure broke; 1H trend is against the trad); 13:09 exit
- **my_ema_rsi_1h** US30 LONG c33f7974 → OPEN (R, best 1.03R): 12:00 entry (52392.5); 12:00 analyst (trade on track); 15:00 analyst (5m structure broke); 15:20 analyst (trade on track); 16:00 partial (Jev: continuation 0.43 < 0.45); 17:00 partial (Jev: continuation 0.43 < 0.45); 17:00 stop_moved (breakeven / 2×ATR trail after +1R)
- **my_ema_rsi_1h** US30 LONG 216b658a → OPEN (R, best 0.00R): 12:00 entry (52439.4)
- **my_ema_rsi_1h** NDQ SHORT a93c25b2 → OPEN (R, best 0.00R): 16:00 entry (29205.5)
- **my_ema_rsi_4h** NDQ SHORT 632887d2 → OPEN (R, best 1.05R): 01:00 entry (30014.5); 01:00 analyst (trade on track); 02:55 analyst (stalled: no new best for 60 min and under +0.5R); 03:10 analyst (trade on track); 04:45 analyst (5m structure broke); 04:50 analyst (trade on track); 06:05 analyst (stalled: no new best for 60 min and under +0.5R); 10:25 analyst (trade on track); 11:25 analyst (5m structure broke); 11:30 analyst (trade on track); 12:15 analyst (stalled: no new best for 60 min and under +0.5R); 12:30 analyst (trade on track); 13:00 agent_check (continuation 0.45 ≥ 0.45); 15:25 analyst (5m structure broke)
- **my_ema_rsi_4h** US30 LONG c0daa33b → OPEN (R, best 1.69R): 09:00 entry (52365.4); 09:00 analyst (trade on track); 10:25 analyst (5m structure broke; gave back half of a ≥1R open); 10:30 analyst (15m trend flipped against the trade; 5m structur); 10:55 analyst (gave back half of a ≥1R open profit); 11:00 analyst (stalled: no new best for 60 min and under +0.5R;); 11:20 analyst (trade on track); 13:00 agent_check (continuation 0.48 ≥ 0.45); 13:00 stop_moved (breakeven / 2×ATR trail after +1R)
- **my_intraday_mom** NDQ LONG e97a9539 → session_close (-0.13R, best 0.05R): 15:30 entry (28835.0); 15:30 analyst (1H trend is against the trade); 15:40 analyst (5m structure broke; 1H trend is against the trad); 16:00 exit_signal (end of the 15:30-16:00 window); 16:00 exit
- **my_rsi_15m** XAUUSD SHORT d5f69550 → OPEN (R, best 1.14R): 11:15 entry (4084.205); 11:15 analyst (trade on track); 13:00 agent_check (continuation 0.47 ≥ 0.45); 14:00 analyst (stalled: no new best for 60 min and under +0.5R); 14:10 analyst (trade on track); 14:15 partial (Jev: continuation 0.40 < 0.45); 14:20 analyst (stalled: no new best for 60 min and under +0.5R); 14:25 analyst (trade on track); 14:30 partial (Jev: continuation 0.43 < 0.45); 15:45 stop_moved (breakeven / 2×ATR trail after +1R); 16:00 stop_moved (breakeven / 2×ATR trail after +1R); 16:15 stop_moved (breakeven / 2×ATR trail after +1R); 16:30 stop_moved (breakeven / 2×ATR trail after +1R); 16:45 stop_moved (breakeven / 2×ATR trail after +1R)
- **my_rsi_15m** US30 LONG fcd1d2ed → OPEN (R, best 0.00R): 16:00 entry (52692.5)
- **my_rsi_15m** NDQ SHORT 9971e243 → OPEN (R, best 0.00R): 16:45 entry (29085.600000000002)
- **my_rsi_15m** NDQ SHORT ba5a4ccd → stop (-1.00R, best 0.80R): 19:15 entry (29033.7); 19:15 analyst (trade on track); 20:15 analyst (5m structure broke); 20:20 analyst (trade on track); 20:48 exit
- **my_rsi_15m** XAUUSD SHORT a3960d9b → close_past_ema21 (-0.46R, best 0.17R): 00:30 entry (4026.638); 00:30 analyst (trade on track); 01:15 exit_signal; 01:15 exit
- **my_rsi_15m** XAUUSD SHORT 95337acf → weekend_close (-0.44R, best 0.16R): 13:30 entry (4008.715); 13:30 analyst (trade on track); 13:55 analyst (5m structure broke); 14:15 analyst (trade on track); 14:30 analyst (5m structure broke); 14:40 analyst (trade on track); 14:45 analyst (stalled: no new best for 60 min and under +0.5R); 16:00 exit_signal (flat before the weekend); 16:00 exit
- **my_rsi_1h** US30 LONG af640ece → OPEN (R, best 0.00R): 16:00 entry (52495.4)
- **my_rsi_1h** XAUUSD SHORT 4f472e7e → OPEN (R, best 1.54R): 03:00 entry (4036.6710000000003); 03:00 analyst (trade on track); 03:35 analyst (5m structure broke); 03:50 analyst (trade on track); 04:45 analyst (5m structure broke); 05:00 analyst (15m trend flipped against the trade; 5m structur); 05:15 analyst (5m structure broke; stalled: no new best for 60 ); 10:15 analyst (trade on track); 10:40 analyst (gave back half of a ≥1R open profit); 11:00 agent_check (continuation 0.47 ≥ 0.45); 11:00 stop_moved (breakeven / 2×ATR trail after +1R); 11:10 analyst (trade on track); 11:15 analyst (gave back half of a ≥1R open profit); 11:55 analyst (stalled: no new best for 60 min and under +0.5R;)
- **my_rsi_4h** US30 LONG 3750c941 → OPEN (R, best 0.00R): 13:00 entry (52361.9)
- **playbook_regime** US30 LONG 05bac06e → OPEN (R, best 0.00R): 20:30 entry (52437.6)
- **playbook_regime** NDQ SHORT ac77a940 → stop (-1.00R, best 0.31R): 20:10 entry (28956.9); 20:13 exit
- **shadow** NDQ SHORT ebcda2f4 → OPEN (R, best 0.00R): 22:15 entry (29647.7)
- **shadow** US30 LONG 4dfb39be → OPEN (R, best 0.00R): 20:30 entry (52437.6)
- **shadow** NDQ SHORT 3ca3d2af → stop (-1.00R, best 0.31R): 20:10 entry (28956.9); 20:13 exit
- **shadow** XAUUSD SHORT c540b744 → stop (-1.00R, best 0.08R): 22:09 entry (4015.616); 22:10 analyst (trade on track); 22:18 exit
- **shadow** XAUUSD SHORT fd268000 → stop (-1.00R, best 0.80R): 03:51 entry (4022.308); 03:55 analyst (trade on track); 04:45 exit
- **shadow** XAUUSD SHORT 549a7441 → session_flat (-0.53R, best 0.19R): 13:30 entry (4006.952); 13:35 analyst (trade on track); 13:55 analyst (5m structure broke); 14:15 analyst (trade on track); 14:30 analyst (5m structure broke); 14:40 analyst (trade on track); 14:45 analyst (stalled: no new best for 60 min and under +0.5R); 15:50 exit
- **shadow** XAUUSD SHORT d0e533d2 → session_flat (-0.74R, best 0.18R): 14:42 entry (4002.49); 14:45 analyst (trade on track); 15:40 analyst (5m structure broke); 15:50 exit

## 7. Entry reasons of every trade

- ema21_rsi55 a13aebfa US30 SHORT: EMA21+RSI45 short: 15m close 52334.60 < EMA21 52392.58, RSI 43.7
- live b871757d US30 LONG: RSI recovered above 35
- live 3850d8cc US30 LONG: Sweep → MSS → breaker retest
- live 9d73f905 NDQ SHORT: Resistance rejection @ 29047.07
- live 207db6a7 XAUUSD SHORT: MSS → OTE retrace
- my_ema_cross_15m 582cf1cd US30 SHORT: my_ema_cross_15m: 15min close 52822.90 < EMA21 52887.67, RSI 42.8, CHOP 40, Supertrend down
- my_ema_cross_15m d25abfa4 NDQ LONG: my_ema_cross_15m: 15min close 29048.60 > EMA21 28995.71, RSI 54.3, CHOP 60, Supertrend down
- my_ema_cross_15m c23166cb XAUUSD LONG: my_ema_cross_15m: 15min close 4019.52 > EMA21 4016.06, RSI 52.5, CHOP 50, Supertrend down
- my_ema_cross_15m fb02ed70 NDQ SHORT: my_ema_cross_15m: 15min close 29007.60 < EMA21 29038.71, RSI 46.3, CHOP 58, Supertrend up
- my_ema_cross_1h 1311e5cd US30 LONG: my_ema_cross_1h: 1h close 52686.60 > EMA21 52651.37, RSI 52.4, CHOP 57, Supertrend up
- my_ema_cross_1h 1ad10fff US30 SHORT: my_ema_cross_1h: 1h close 52676.40 < EMA21 52774.01, RSI 44.4, CHOP 56, Supertrend up
- my_ema_cross_4h f1537166 NDQ SHORT: my_ema_cross_4h: 4h close 29638.90 < EMA21 29715.93, RSI 45.9, CHOP 55, Supertrend down
- my_ema_rsi_15m c94efac9 US30 LONG: my_ema_rsi_15m: 15min close 52851.00 > EMA21 52781.32, RSI 57.8, CHOP 59, Supertrend up
- my_ema_rsi_15m c3beb17d NDQ SHORT: my_ema_rsi_15m: 15min close 28949.00 < EMA21 28986.42, RSI 42.2, CHOP 50, Supertrend down
- my_ema_rsi_15m e65e56f9 XAUUSD SHORT: my_ema_rsi_15m: 15min close 4010.09 < EMA21 4018.10, RSI 42.0, CHOP 48, Supertrend down
- my_ema_rsi_15m 432fdb56 US30 SHORT: my_ema_rsi_15m: 15min close 52771.90 < EMA21 52828.60, RSI 40.1, CHOP 44, Supertrend down
- my_ema_rsi_15m f5f3f978 NDQ LONG: my_ema_rsi_15m: 15min close 29061.20 > EMA21 29022.93, RSI 56.1, CHOP 59, Supertrend down
- my_ema_rsi_15m bc90b02c NDQ LONG: my_ema_rsi_15m: 15min close 29093.60 > EMA21 29029.27, RSI 59.7, CHOP 58, Supertrend up
- my_ema_rsi_15m 31438490 US30 SHORT: my_ema_rsi_15m: 15min close 52697.90 < EMA21 52739.83, RSI 40.4, CHOP 59, Supertrend down
- my_ema_rsi_15m e49250ba NDQ SHORT: my_ema_rsi_15m: 15min close 28967.60 < EMA21 29018.26, RSI 41.7, CHOP 46, Supertrend up
- my_ema_rsi_15m 6131dc53 XAUUSD LONG: my_ema_rsi_15m: 15min close 4028.59 > EMA21 4021.59, RSI 60.1, CHOP 53, Supertrend up
- my_ema_rsi_15m d21c15b9 US30 SHORT: my_ema_rsi_15m: 15min close 52337.60 < EMA21 52404.82, RSI 42.6, CHOP 47, Supertrend down
- my_ema_rsi_15m 7d1f4801 XAUUSD SHORT: my_ema_rsi_15m: 15min close 4001.59 < EMA21 4008.97, RSI 43.1, CHOP 39, Supertrend down
- my_ema_rsi_15m 21739a3a NDQ LONG: my_ema_rsi_15m: 15min close 29109.40 > EMA21 29050.01, RSI 57.4, CHOP 47, Supertrend up
- my_ema_rsi_15m 9e47835a US30 SHORT: my_ema_rsi_15m: 15min close 52334.60 < EMA21 52392.58, RSI 43.7, CHOP 55, Supertrend down
- my_ema_rsi_15m 946b389f NDQ SHORT: my_ema_rsi_15m: 15min close 28984.70 < EMA21 29027.70, RSI 43.4, CHOP 55, Supertrend up
- my_ema_rsi_1h c33f7974 US30 LONG: my_ema_rsi_1h: 1h close 52681.60 > EMA21 52537.68, RSI 58.9, CHOP 56, Supertrend up
- my_ema_rsi_1h 216b658a US30 LONG: my_ema_rsi_1h: 1h close 52863.60 > EMA21 52670.66, RSI 59.9, CHOP 57, Supertrend up
- my_ema_rsi_1h 799e7790 US30 SHORT: my_ema_rsi_1h: 1h close 52582.90 < EMA21 52748.03, RSI 39.2, CHOP 43, Supertrend up
- my_ema_rsi_1h a93c25b2 NDQ SHORT: my_ema_rsi_1h: 1h close 28978.70 < EMA21 29054.19, RSI 42.7, CHOP 57, Supertrend down
- my_ema_rsi_4h 632887d2 NDQ SHORT: my_ema_rsi_4h: 4h close 29465.60 < EMA21 29693.18, RSI 41.1, CHOP 56, Supertrend down
- my_ema_rsi_4h c0daa33b US30 LONG: my_ema_rsi_4h: 4h close 52587.00 > EMA21 52452.03, RSI 56.2, CHOP 46, Supertrend up
- my_intraday_mom e97a9539 NDQ LONG: my_intraday_mom: first half-hour +0.081% (16:00 close 28999.20 -> 10:00 29022.60) -> long 15:30-16:00
- my_intraday_mom 0e0a3f01 US30 SHORT: my_intraday_mom: first half-hour -1.087% (16:00 close 52911.00 -> 10:00 52336.00) -> short 15:30-16:00
- my_rsi_15m d5f69550 XAUUSD SHORT: my_rsi_15m: 15min close 4055.01 < EMA21 4068.51, RSI 38.3, CHOP 49, Supertrend down
- my_rsi_15m fcd1d2ed US30 LONG: my_rsi_15m: 15min close 52911.00 > EMA21 52798.62, RSI 62.1, CHOP 61, Supertrend up
- my_rsi_15m 9971e243 NDQ SHORT: my_rsi_15m: 15min close 28968.60 < EMA21 29041.31, RSI 38.9, CHOP 59, Supertrend down
- my_rsi_15m 95bbb3aa XAUUSD SHORT: my_rsi_15m: 15min close 4027.70 < EMA21 4033.56, RSI 39.7, CHOP 52, Supertrend down
- my_rsi_15m ba5a4ccd NDQ SHORT: my_rsi_15m: 15min close 28947.20 < EMA21 29010.14, RSI 38.6, CHOP 58, Supertrend down
- my_rsi_15m a3960d9b XAUUSD SHORT: my_rsi_15m: 15min close 4006.14 < EMA21 4017.01, RSI 39.5, CHOP 47, Supertrend down
- my_rsi_15m 95337acf XAUUSD SHORT: my_rsi_15m: 15min close 3993.86 < EMA21 4005.57, RSI 38.1, CHOP 44, Supertrend down
- my_rsi_1h af640ece US30 LONG: my_rsi_1h: 1h close 52911.00 > EMA21 52722.60, RSI 60.6, CHOP 58, Supertrend up
- my_rsi_1h 4f472e7e XAUUSD SHORT: my_rsi_1h: 1h close 4012.93 < EMA21 4037.48, RSI 38.5, CHOP 47, Supertrend down
- my_rsi_4h 3750c941 US30 LONG: my_rsi_4h: 4h close 52841.00 > EMA21 52487.40, RSI 61.9, CHOP 49, Supertrend up
- playbook_regime 05bac06e US30 LONG: DTFX close_fib BOS → 50-70% zone rejection · playbook level=50-70/trend p=0.47
- playbook_regime ac77a940 NDQ SHORT: DTFX wick_fib BOS → 50% rejection · playbook swing=pb/scalp p=0.55
- playbook_regime b5a1d520 NDQ SHORT: DTFX wick_fib BOS → 50-70% zone rejection · playbook level=50-70/std p=0.55
- shadow ebcda2f4 NDQ SHORT: DTFX wick_fib BOS → 50-70% zone rejection · playbook level=50-70/std p=0.55
- shadow 4dfb39be US30 LONG: DTFX close_fib BOS → 50-70% zone rejection · playbook level=50-70/trend p=0.47
- shadow 3ca3d2af NDQ SHORT: DTFX wick_fib BOS → 50% rejection · playbook swing=pb/scalp p=0.55
- shadow c540b744 XAUUSD SHORT: Displacement BOS → FVG ce · playbook default/std p=0.61
- shadow fd268000 XAUUSD SHORT: Sweep → MSS (displacement CHoCH) · playbook default/std p=0.61
- shadow 549a7441 XAUUSD SHORT: Turtle Soup (n20, choch) · playbook confirm=choch/std p=0.53
- shadow d0e533d2 XAUUSD SHORT: Sweep → MSS (displacement CHoCH) · playbook default/std p=0.61
