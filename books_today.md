# RSI / EMA books report

Generated 2026-10-26 22:00 New York. Window: since 2026-10-26 00:00 (22 h). R = profit as a multiple of the risk at the first stop.

Books read: live, c10_afternoon, daily_rsi2_adx2, ema21_rsi55, h1_vol_trend, my_ema_cross_15m, my_ema_cross_1d, my_ema_cross_1h, my_ema_cross_4h, my_ema_rsi_15m, my_ema_rsi_1d, my_ema_rsi_1h, my_ema_rsi_4h, my_intraday_mom, my_rsi_15m, my_rsi_1h, my_rsi_4h, playbook_regime, shadow

## 1. Per book

| Book | Trades | Closed | Open | Wins | Total R | P&L | Avg best R | Avg hours held | Jev partials |
|---|---|---|---|---|---|---|---|---|---|
| live | 4 | 4 | 0 | 2 | -0.27 | -174.91 | 1.06 | 0.9 | 1 |
| c10_afternoon | 1 | 1 | 0 | 1 | +0.15 | +10.87 | 0.82 | 2.7 | 0 |
| daily_rsi2_adx2 | 0 | 0 | 0 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 0 |
| ema21_rsi55 | 3 | 3 | 0 | 0 | -1.30 | -91.02 | 0.26 | 1.8 | 0 |
| h1_vol_trend | 0 | 0 | 0 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 0 |
| my_ema_cross_15m | 6 | 5 | 1 | 0 | -2.04 | -709.37 | 0.24 | 1.5 | 0 |
| my_ema_cross_1d | 0 | 0 | 0 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 0 |
| my_ema_cross_1h | 6 | 3 | 3 | 0 | -1.77 | -621.43 | 0.19 | 3.0 | 0 |
| my_ema_cross_4h | 1 | 0 | 1 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 2 |
| my_ema_rsi_15m | 14 | 11 | 3 | 2 | -4.33 | -1517.69 | 0.61 | 1.8 | 2 |
| my_ema_rsi_1d | 0 | 0 | 0 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 0 |
| my_ema_rsi_1h | 7 | 4 | 3 | 0 | -1.72 | -599.28 | 0.17 | 3.8 | 2 |
| my_ema_rsi_4h | 2 | 0 | 2 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 1 |
| my_intraday_mom | 2 | 2 | 0 | 1 | -0.10 | -35.74 | 0.22 | 0.5 | 0 |
| my_rsi_15m | 3 | 0 | 3 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 2 |
| my_rsi_1h | 2 | 1 | 1 | 0 | -0.85 | -300.71 | 0.09 | 1.0 | 0 |
| my_rsi_4h | 1 | 0 | 1 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 0 |
| playbook_regime | 1 | 0 | 1 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 0 |
| shadow | 7 | 5 | 2 | 2 | -1.21 | -331.44 | 1.09 | 0.7 | 2 |

All listed books: 39 closed trades, -13.44 R.

## 2. Why the losing trades lost

| Cause | Trades | R |
|---|---|---|
| closed on the EMA exit at a loss | 22 | -10.71 |
| stopped at the first stop | 6 | -5.24 |
| gave back: was +0.5R or better first | 3 | -2.39 |

## 3. Skipped signals (what the filters blocked)

**live**: 8x skipped: Jev quality # < #; 6x filtered: counter to BEARISH bias; 4x skipped: Jev confidence # < #; 4x filtered: bias neutral (#); 3x taken: qty #, risk $#, cost #R; 2x filtered: counter to BULLISH bias; 1x taken: qty #; 1x rejected: index group full (one index position per direction at a time)
**c10_afternoon**: 1x taken: qty #
**ema21_rsi55**: 3x taken: qty #, jev #; 1x rejected: choppy market (CHOP # ≥ #)
**my_ema_cross_15m**: 5x taken: qty #, jev #; 5x rejected: stop too wide (# ATR); 1x rejected: choppy market (CHOP # ≥ #)
**my_ema_cross_1h**: 5x taken: qty #, jev #; 1x rejected: choppy market (CHOP # ≥ #)
**my_ema_rsi_15m**: 11x taken: qty #, jev #; 8x rejected: choppy market (CHOP # ≥ #); 7x rejected: stop too wide (# ATR)
**my_ema_rsi_1h**: 4x taken: qty #, jev #; 2x rejected: choppy market (CHOP # ≥ #); 1x rejected: stop too wide (# ATR)
**my_intraday_mom**: 2x taken: qty #, jev None
**my_rsi_1h**: 1x taken: qty #, jev #
**playbook_regime**: 29x skipped: regime chop (Jev chop #, CHOP #): scalps only; 6x filtered: bias neutral (#); 5x skipped: Jev quality # < #; 3x filtered: counter to BEARISH bias
**shadow**: 20x skipped: Jev quality # < #; 6x filtered: bias neutral (#); 3x taken: qty #, risk $#, cost #R; 3x filtered: counter to BEARISH bias; 3x rejected: outside entry windows; 2x skipped: a higher-expectancy playbook cell fired on this bar; 2x skipped: playbook: XAUUSD has an opposite position (OANDA nets positions per instrum; 2x taken: qty #, risk $#, cost #R (over the #R cap — log only)

## 4. Trade analyst (shadow) - how its advice scored

| Book | Check | Times | Avg value in R (positive = its advice would have helped) | Helpful |
|---|---|---|---|---|
| live | any_exit | 6 | +0.17 | 4 |
| live | giveback | 4 | +0.04 | 3 |
| live | h1_against | 3 | -0.48 | 1 |
| live | stall | 2 | +0.30 | 1 |
| live | structure_break | 5 | +0.12 | 3 |
| live | trend_flip | 4 | +0.03 | 3 |
| c10_afternoon | any_exit | 2 | -0.33 | 0 |
| c10_afternoon | giveback | 1 | -1.33 | 0 |
| c10_afternoon | stall | 1 | -0.00 | 0 |
| c10_afternoon | structure_break | 2 | -0.46 | 0 |
| ema21_rsi55 | any_exit | 6 | +0.05 | 3 |
| ema21_rsi55 | giveback | 1 | -0.05 | 0 |
| ema21_rsi55 | h1_against | 6 | +0.17 | 5 |
| ema21_rsi55 | stall | 5 | +0.05 | 4 |
| ema21_rsi55 | structure_break | 5 | +0.07 | 2 |
| h1_vol_trend | any_exit | 1 | -0.90 | 0 |
| h1_vol_trend | stall | 1 | -0.96 | 0 |
| h1_vol_trend | structure_break | 1 | -0.90 | 0 |
| my_ema_cross_15m | any_exit | 7 | +0.04 | 5 |
| my_ema_cross_15m | giveback | 1 | +0.03 | 1 |
| my_ema_cross_15m | h1_against | 10 | +0.19 | 7 |
| my_ema_cross_15m | stall | 4 | +0.06 | 2 |
| my_ema_cross_15m | structure_break | 7 | +0.09 | 5 |
| my_ema_cross_15m | trend_flip | 3 | -0.09 | 1 |
| my_ema_cross_1h | any_exit | 6 | +0.34 | 5 |
| my_ema_cross_1h | h1_against | 4 | +0.55 | 4 |
| my_ema_cross_1h | stall | 4 | +0.58 | 4 |
| my_ema_cross_1h | structure_break | 6 | +0.27 | 5 |
| my_ema_cross_1h | trend_flip | 4 | +0.36 | 4 |
| my_ema_rsi_15m | any_exit | 25 | +0.11 | 16 |
| my_ema_rsi_15m | giveback | 3 | +0.18 | 3 |
| my_ema_rsi_15m | h1_against | 22 | +0.19 | 15 |
| my_ema_rsi_15m | stall | 11 | +0.12 | 7 |
| my_ema_rsi_15m | structure_break | 23 | +0.08 | 13 |
| my_ema_rsi_15m | trend_flip | 6 | +0.30 | 5 |
| my_ema_rsi_1h | any_exit | 10 | +0.25 | 8 |
| my_ema_rsi_1h | giveback | 1 | +0.07 | 1 |
| my_ema_rsi_1h | h1_against | 2 | +0.62 | 2 |
| my_ema_rsi_1h | stall | 6 | +0.38 | 5 |
| my_ema_rsi_1h | structure_break | 10 | +0.22 | 8 |
| my_ema_rsi_1h | trend_flip | 8 | +0.21 | 6 |
| my_ema_rsi_4h | any_exit | 1 | +0.25 | 1 |
| my_ema_rsi_4h | h1_against | 1 | +0.12 | 1 |
| my_ema_rsi_4h | stall | 1 | +0.25 | 1 |
| my_ema_rsi_4h | structure_break | 1 | -0.02 | 0 |
| my_ema_rsi_4h | trend_flip | 1 | +0.05 | 1 |
| my_intraday_mom | any_exit | 4 | +0.07 | 3 |
| my_intraday_mom | h1_against | 3 | +0.07 | 2 |
| my_intraday_mom | structure_break | 4 | +0.07 | 3 |
| my_rsi_15m | any_exit | 4 | +0.14 | 3 |
| my_rsi_15m | giveback | 1 | +0.05 | 1 |
| my_rsi_15m | stall | 3 | +0.03 | 2 |
| my_rsi_15m | structure_break | 4 | +0.18 | 3 |
| my_rsi_1h | any_exit | 2 | -0.28 | 1 |
| my_rsi_1h | giveback | 1 | +0.29 | 1 |
| my_rsi_1h | stall | 1 | -1.01 | 0 |
| my_rsi_1h | structure_break | 2 | -0.28 | 1 |
| my_rsi_1h | trend_flip | 2 | -0.42 | 1 |
| playbook_regime | any_exit | 1 | -0.54 | 0 |
| playbook_regime | giveback | 3 | -0.04 | 2 |
| playbook_regime | stall | 1 | -0.19 | 0 |
| playbook_regime | structure_break | 1 | -0.54 | 0 |
| shadow | any_exit | 16 | +0.02 | 9 |
| shadow | giveback | 6 | +0.05 | 5 |
| shadow | h1_against | 5 | -0.11 | 2 |
| shadow | stall | 9 | +0.08 | 5 |
| shadow | structure_break | 14 | -0.03 | 8 |
| shadow | trend_flip | 4 | +0.27 | 4 |

## 5. Every trade in the window

| Book | Id | Market | Side | Opened (NY) | Closed (NY) | Entry | Exit | First stop | Stop at end | Qty | P&L | R | Best R | Worst R | How it ended |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| c10_afternoon | cf213cd1 | NDQ | LONG | 10-26 13:00 | 10-26 15:45 | 29343.00 | 29357.30 | 29250.50 | 29250.50 | 0.76 | 10.87 | 0.15 | 0.82 | -0.47 | time_1545 |
| ema21_rsi55 | 11f85acb | XAUUSD | LONG | 10-26 07:00 | 10-26 07:15 | 4015.51 | 4011.27 | 4000.01 | 4000.01 | 4.50 | -19.08 | -0.27 | 0.07 | -0.30 | close_below_ema21 |
| ema21_rsi55 | 874563ec | US30 | LONG | 10-26 10:15 | 10-26 11:30 | 52552.90 | 52399.30 | 52325.50 | 52325.50 | 0.31 | -47.62 | -0.68 | 0.40 | -0.69 | close_below_ema21 |
| ema21_rsi55 | 835908fe | XAUUSD | LONG | 10-26 10:45 | 10-26 14:45 | 4022.47 | 4014.09 | 3998.42 | 3998.42 | 2.90 | -24.32 | -0.35 | 0.32 | -0.35 | close_below_ema21 |
| live | 5f6a64cb | NDQ | SHORT | 10-26 03:45 | 10-26 04:14 | 28966.40 | 28911.95 | 28992.80 | 28911.00 | 5.07 | 205.84 | 1.54 | 3.30 | -0.27 | trail_stop |
| live | 139ba435 | US30 | LONG | 10-26 11:25 | 10-26 11:32 | 52444.60 | 52383.10 | 52383.30 | 52383.30 | 2.80 | -172.20 | -1.00 | 0.00 | -0.96 | stop |
| live | 3cc62c71 | NDQ | LONG | 10-26 13:00 | 10-26 15:45 | 29340.70 | 29359.40 | 29250.50 | 29250.50 | 1.96 | 36.65 | 0.21 | 0.87 | -0.46 | time_1545 |
| live | 70326449 | XAUUSD | SHORT | 10-26 21:25 | 10-26 21:35 | 4004.68 | 4016.94 | 4016.74 | 4016.74 | 20.00 | -245.20 | -1.02 | 0.06 | -0.92 | stop |
| my_ema_cross_15m | f854a81b | US30 | LONG | 10-25 22:30 | 10-26 02:30 | 52343.80 | 52343.30 | 52188.00 | 52188.00 | 2.24 | -1.12 | -0.00 | 0.44 | -0.19 | close_past_ema21 |
| my_ema_cross_15m | cda682ac | NDQ | LONG | 10-26 01:00 | 10-26 02:30 | 29036.00 | 28926.00 | 28904.40 | 28904.40 | 2.66 | -292.60 | -0.84 | 0.20 | -0.88 | close_past_ema21 |
| my_ema_cross_15m | 958d6b8c | NDQ | SHORT | 10-26 02:45 | 10-26 03:15 | 28915.40 | 28989.20 | 29075.80 | 29075.80 | 2.17 | -160.15 | -0.46 | 0.04 | -0.52 | close_past_ema21 |
| my_ema_cross_15m | e74b6331 | NDQ | LONG | 10-26 05:00 | 10-26 06:30 | 29026.40 | 28989.00 | 28865.80 | 28865.80 | 2.16 | -80.78 | -0.23 | 0.38 | -0.26 | close_past_ema21 |
| my_ema_cross_15m | ff83b3b3 | NDQ | SHORT | 10-26 07:15 | 10-26 07:30 | 28975.00 | 29037.40 | 29099.00 | 29099.00 | 2.80 | -174.72 | -0.50 | 0.12 | -0.51 | close_past_ema21 |
| my_ema_cross_15m | df38203d | US30 | LONG | 10-26 20:15 | open | 52407.50 |  | 52285.80 | 52285.80 | 2.90 | 0.00 |  | 0.00 | 0.00 | OPEN |
| my_ema_cross_1h | 1311e5cd | US30 | LONG | 10-22 11:00 | open | 52688.10 |  | 52441.20 | 52688.10 | 1.42 | 0.00 |  | 1.12 | -0.18 | OPEN |
| my_ema_cross_1h | c709fa59 | XAUUSD | LONG | 10-26 06:00 | 10-26 10:00 | 4018.01 | 3992.86 | 3983.28 | 3983.28 | 10.10 | -253.96 | -0.72 | 0.21 | -0.84 | close_past_ema21 |
| my_ema_cross_1h | 3944eb23 | XAUUSD | LONG | 10-26 11:00 | 10-26 15:00 | 4023.55 | 4012.38 | 3985.05 | 3985.05 | 9.10 | -101.69 | -0.29 | 0.17 | -0.29 | close_past_ema21 |
| my_ema_cross_1h | 4de8ae50 | US30 | LONG | 10-26 11:00 | 10-26 12:00 | 52490.30 | 52332.10 | 52282.00 | 52282.00 | 1.68 | -265.78 | -0.76 | 0.18 | -0.81 | close_past_ema21 |
| my_ema_cross_1h | 5bb1bd2b | XAUUSD | SHORT | 10-26 21:00 | open | 4009.26 |  | 4033.13 | 4033.13 | 14.70 | 0.00 |  | 0.00 | 0.00 | OPEN |
| my_ema_cross_1h | 21b09a0d | US30 | LONG | 10-26 22:00 | open | 52478.50 |  | 52264.70 | 52264.70 | 1.65 | 0.00 |  | 0.00 | 0.00 | OPEN |
| my_ema_cross_4h | f1537166 | NDQ | SHORT | 10-21 21:00 | open | 29637.80 |  | 30014.40 | 29351.10 | 0.93 | 236.81 |  | 1.99 | -0.05 | OPEN |
| my_ema_rsi_15m | c94efac9 | US30 | LONG | 10-22 15:30 | open | 52852.50 |  | 52692.40 | 52692.40 | 2.21 | 0.00 |  | 0.00 | 0.00 | OPEN |
| my_ema_rsi_15m | c6c3b4f1 | NDQ | SHORT | 10-25 21:45 | 10-26 00:15 | 28917.60 | 28980.40 | 29116.30 | 29116.30 | 1.76 | -110.53 | -0.32 | 0.12 | -0.66 | close_past_ema21 |
| my_ema_rsi_15m | f22f9f0e | US30 | LONG | 10-25 22:30 | 10-26 02:30 | 52343.80 | 52343.30 | 52188.00 | 52188.00 | 2.24 | -1.12 | -0.00 | 0.44 | -0.19 | close_past_ema21 |
| my_ema_rsi_15m | 5d8ce702 | NDQ | LONG | 10-26 01:00 | 10-26 02:30 | 29036.00 | 28926.00 | 28904.40 | 28904.40 | 2.66 | -292.60 | -0.84 | 0.20 | -0.88 | close_past_ema21 |
| my_ema_rsi_15m | 7bd66d5a | XAUUSD | LONG | 10-26 04:00 | 10-26 06:44 | 4010.07 | 4011.97 | 4001.88 | 4011.97 | 42.40 | 80.22 | 0.23 | 1.50 | -0.11 | stop |
| my_ema_rsi_15m | e6afdc13 | NDQ | SHORT | 10-26 04:00 | 10-26 04:45 | 28936.20 | 29037.20 | 29053.70 | 29053.70 | 2.96 | -298.96 | -0.86 | 0.48 | -0.90 | close_past_ema21 |
| my_ema_rsi_15m | 95a73e13 | XAUUSD | LONG | 10-26 07:00 | 10-26 07:15 | 4015.51 | 4011.27 | 4009.51 | 4009.51 | 57.80 | -245.07 | -0.71 | 0.18 | -0.78 | close_past_ema21 |
| my_ema_rsi_15m | 66294d3d | NDQ | LONG | 10-26 10:15 | 10-26 12:44 | 29161.40 | 29282.40 | 29004.20 | 29282.40 | 2.20 | 301.51 | 0.87 | 1.69 | -0.09 | stop |
| my_ema_rsi_15m | b30e14cf | XAUUSD | LONG | 10-26 12:30 | 10-26 14:45 | 4019.30 | 4014.09 | 4006.08 | 4006.08 | 26.30 | -136.89 | -0.39 | 0.82 | -0.39 | close_past_ema21 |
| my_ema_rsi_15m | 242cb99e | US30 | SHORT | 10-26 12:45 | 10-26 14:30 | 52349.10 | 52416.10 | 52562.40 | 52562.40 | 1.62 | -108.54 | -0.31 | 0.27 | -0.37 | close_past_ema21 |
| my_ema_rsi_15m | f9c61cc0 | XAUUSD | SHORT | 10-26 19:15 | 10-26 20:12 | 4011.01 | 4018.68 | 4018.68 | 4018.68 | 46.00 | -352.87 | -1.00 | 0.89 | -0.92 | stop |
| my_ema_rsi_15m | ce856337 | US30 | SHORT | 10-26 19:15 | 10-26 19:41 | 52306.50 | 52411.20 | 52411.20 | 52411.20 | 3.37 | -352.84 | -1.00 | 0.07 | -0.96 | stop |
| my_ema_rsi_15m | 53d77db4 | US30 | LONG | 10-26 20:30 | open | 52419.50 |  | 52285.90 | 52285.90 | 2.61 | 0.00 |  | 0.00 | 0.00 | OPEN |
| my_ema_rsi_15m | e041b1c3 | NDQ | LONG | 10-26 21:45 | open | 29400.20 |  | 29311.90 | 29311.90 | 3.96 | 0.00 |  | 0.00 | 0.00 | OPEN |
| my_ema_rsi_1h | c33f7974 | US30 | LONG | 10-21 12:00 | open | 52683.10 |  | 52392.50 | 52697.70 | 1.21 | 192.06 |  | 1.03 | -0.20 | OPEN |
| my_ema_rsi_1h | 216b658a | US30 | LONG | 10-22 12:00 | open | 52865.10 |  | 52439.40 | 52439.40 | 0.82 | 0.00 |  | 0.00 | 0.00 | OPEN |
| my_ema_rsi_1h | 709409e3 | NDQ | SHORT | 10-25 21:00 | 10-26 01:00 | 28951.20 | 29036.00 | 29230.60 | 29230.60 | 1.25 | -106.00 | -0.30 | 0.24 | -0.35 | close_past_ema21 |
| my_ema_rsi_1h | 50bb300c | NDQ | SHORT | 10-26 03:00 | 10-26 05:00 | 28937.80 | 29026.40 | 29195.10 | 29195.10 | 1.36 | -120.50 | -0.34 | 0.23 | -0.47 | close_past_ema21 |
| my_ema_rsi_1h | 74231b50 | XAUUSD | SHORT | 10-26 10:00 | 10-26 11:00 | 3992.86 | 4023.55 | 4028.83 | 4028.83 | 9.70 | -297.64 | -0.85 | 0.09 | -0.94 | close_past_ema21 |
| my_ema_rsi_1h | 2cfac4f4 | US30 | SHORT | 10-26 12:00 | 10-26 20:00 | 52332.10 | 52406.50 | 52675.30 | 52675.30 | 1.01 | -75.14 | -0.22 | 0.12 | -0.28 | close_past_ema21 |
| my_ema_rsi_1h | 11bb8774 | US30 | LONG | 10-26 22:00 | open | 52478.50 |  | 52264.70 | 52264.70 | 1.64 | 0.00 |  | 0.00 | 0.00 | OPEN |
| my_ema_rsi_4h | 632887d2 | NDQ | SHORT | 10-22 01:00 | open | 29464.40 |  | 30014.50 | 29351.10 | 0.64 | 165.89 |  | 1.05 | -0.01 | OPEN |
| my_ema_rsi_4h | c0daa33b | US30 | LONG | 10-22 09:00 | open | 52588.50 |  | 52365.40 | 52588.50 | 1.58 | 0.00 |  | 1.69 | -0.25 | OPEN |
| my_intraday_mom | 5b04f4c6 | NDQ | LONG | 10-26 15:30 | 10-26 16:00 | 29343.60 | 29301.80 | 29158.20 | 29158.20 | 1.90 | -79.42 | -0.23 | 0.21 | -0.29 | session_close |
| my_intraday_mom | 85cf3db3 | US30 | LONG | 10-26 15:30 | 10-26 16:00 | 52363.10 | 52387.50 | 52166.60 | 52166.60 | 1.79 | 43.68 | 0.12 | 0.24 | -0.12 | session_close |
| my_rsi_15m | d5f69550 | XAUUSD | SHORT | 10-22 11:15 | open | 4054.70 |  | 4084.20 | 4034.91 | 11.90 | 159.92 |  | 1.14 | -0.22 | OPEN |
| my_rsi_15m | fcd1d2ed | US30 | LONG | 10-22 16:00 | open | 52912.50 |  | 52692.50 | 52692.50 | 1.61 | 0.00 |  | 0.00 | 0.00 | OPEN |
| my_rsi_15m | 9971e243 | NDQ | SHORT | 10-22 16:45 | open | 28967.40 |  | 29085.60 | 29085.60 | 3.00 | 0.00 |  | 0.00 | 0.00 | OPEN |
| my_rsi_1h | af640ece | US30 | LONG | 10-22 16:00 | open | 52912.50 |  | 52495.40 | 52495.40 | 0.84 | 0.00 |  | 0.00 | 0.00 | OPEN |
| my_rsi_1h | 35e267e6 | XAUUSD | SHORT | 10-26 10:00 | 10-26 11:00 | 3992.86 | 4023.55 | 4028.83 | 4028.83 | 9.80 | -300.71 | -0.85 | 0.09 | -0.94 | close_past_ema21 |
| my_rsi_4h | 3750c941 | US30 | LONG | 10-22 13:00 | open | 52842.50 |  | 52361.90 | 52361.90 | 0.73 | 0.00 |  | 0.00 | 0.00 | OPEN |
| playbook_regime | 05bac06e | US30 | LONG | 10-20 20:30 | open | 52554.50 |  | 52437.60 | 52437.60 | 2.78 | 0.00 |  | 0.00 | 0.00 | OPEN |
| shadow | ebcda2f4 | NDQ | SHORT | 10-19 22:15 | open | 29545.40 |  | 29647.70 | 29647.70 | 3.34 | 0.00 |  | 0.00 | 0.00 | OPEN |
| shadow | 4dfb39be | US30 | LONG | 10-20 20:30 | open | 52554.50 |  | 52437.60 | 52437.60 | 2.73 | 0.00 |  | 0.00 | 0.00 | OPEN |
| shadow | 13b7e8a3 | XAUUSD | SHORT | 10-26 02:54 | 10-26 04:07 | 4008.26 | 4015.68 | 4015.68 | 4015.68 | 20.00 | -148.44 | -1.00 | 0.66 | -0.80 | stop |
| shadow | 1de38240 | XAUUSD | SHORT | 10-26 03:54 | 10-26 04:01 | 4006.50 | 4011.69 | 4011.69 | 4011.69 | 20.00 | -103.72 | -1.00 | 0.06 | -0.84 | stop |
| shadow | 7c197d46 | XAUUSD | SHORT | 10-26 09:00 | 10-26 10:14 | 4015.49 | 4004.29 | 4025.68 | 4004.29 | 19.90 | 172.86 | 0.85 | 2.62 | -0.29 | trail_stop |
| shadow | 2a409407 | XAUUSD | SHORT | 10-26 09:06 | 10-26 09:32 | 4016.55 | 4010.54 | 4022.01 | 4010.54 | 19.90 | 101.67 | 0.94 | 2.07 | -0.26 | trail_stop |
| shadow | 07ed9921 | US30 | LONG | 10-26 11:15 | 10-26 11:51 | 52494.90 | 52331.10 | 52331.10 | 52331.10 | 2.16 | -353.81 | -1.00 | 0.06 | -0.88 | stop |

## 6. Timelines of the losing and the open trades

- **live** US30 LONG 139ba435 → stop (-1.00R, best 0.00R): 11:25 entry (52383.3); 11:25 target_placed; 11:30 analyst (15m trend flipped against the trade; 5m structur); 11:32 exit
- **live** XAUUSD SHORT 70326449 → stop (-1.02R, best 0.06R): 21:25 entry (4016.74); 21:25 target_placed; 21:30 analyst (15m trend flipped against the trade); 21:35 exit
- **ema21_rsi55** XAUUSD LONG 11f85acb → close_below_ema21 (-0.27R, best 0.07R): 07:00 entry (4000.007); 07:00 analyst (1H trend is against the trade); 07:15 exit_signal; 07:15 exit
- **ema21_rsi55** US30 LONG 874563ec → close_below_ema21 (-0.68R, best 0.40R): 10:15 entry (52325.5); 10:15 analyst (1H trend is against the trade); 10:50 analyst (5m structure broke; 1H trend is against the trad); 10:55 analyst (1H trend is against the trade); 11:00 analyst (5m structure broke); 11:05 analyst (trade on track); 11:25 analyst (5m structure broke; stalled: no new best for 60 ); 11:30 exit_signal; 11:30 exit
- **ema21_rsi55** XAUUSD LONG 835908fe → close_below_ema21 (-0.35R, best 0.32R): 10:45 entry (3998.424); 10:45 analyst (1H trend is against the trade); 12:00 analyst (stalled: no new best for 60 min and under +0.5R;); 13:10 analyst (1H trend is against the trade); 14:15 analyst (stalled: no new best for 60 min and under +0.5R;); 14:35 analyst (5m structure broke; stalled: no new best for 60 ); 14:45 exit_signal; 14:45 exit
- **my_ema_cross_15m** US30 LONG f854a81b → close_past_ema21 (-0.00R, best 0.44R): 22:30 entry (52188.0); 22:30 analyst (1H trend is against the trade); 23:30 analyst (15m trend flipped against the trade; 1H trend is); 23:45 analyst (1H trend is against the trade); 00:10 analyst (5m structure broke; stalled: no new best for 60 ); 01:00 analyst (1H trend is against the trade); 02:10 analyst (stalled: no new best for 60 min and under +0.5R;); 02:30 exit_signal; 02:30 exit
- **my_ema_cross_15m** NDQ LONG cda682ac → close_past_ema21 (-0.84R, best 0.20R): 01:00 entry (28904.4); 01:00 analyst (1H trend is against the trade); 02:05 analyst (stalled: no new best for 60 min and under +0.5R;); 02:15 analyst (15m trend flipped against the trade; stalled: no); 02:20 analyst (15m trend flipped against the trade; 5m structur); 02:30 exit_signal; 02:30 exit
- **my_ema_cross_15m** NDQ SHORT 958d6b8c → close_past_ema21 (-0.46R, best 0.04R): 02:45 entry (29075.800000000003); 02:45 analyst (trade on track); 03:15 exit_signal; 03:15 exit
- **my_ema_cross_15m** NDQ LONG e74b6331 → close_past_ema21 (-0.23R, best 0.38R): 05:00 entry (28865.800000000003); 05:00 analyst (1H trend is against the trade); 06:20 analyst (5m structure broke; 1H trend is against the trad); 06:30 exit_signal; 06:30 exit
- **my_ema_cross_15m** NDQ SHORT ff83b3b3 → close_past_ema21 (-0.50R, best 0.12R): 07:15 entry (29099.0); 07:15 analyst (trade on track); 07:30 exit_signal; 07:30 exit
- **my_ema_cross_15m** US30 LONG df38203d → OPEN (R, best 0.00R): 20:15 entry (52285.8)
- **my_ema_cross_1h** US30 LONG 1311e5cd → OPEN (R, best 1.12R): 11:00 entry (52441.200000000004); 11:00 analyst (trade on track); 12:00 agent_check (continuation 0.50 ≥ 0.45); 12:45 analyst (gave back half of a ≥1R open profit); 12:55 analyst (trade on track); 13:00 agent_check (continuation 0.50 ≥ 0.45); 13:00 stop_moved (breakeven / 2×ATR trail after +1R)
- **my_ema_cross_1h** XAUUSD LONG c709fa59 → close_past_ema21 (-0.72R, best 0.21R): 06:00 entry (3983.2780000000002); 06:00 analyst (1H trend is against the trade); 06:30 analyst (5m structure broke; 1H trend is against the trad); 07:00 analyst (1H trend is against the trade); 07:15 analyst (stalled: no new best for 60 min and under +0.5R;); 07:55 analyst (1H trend is against the trade); 09:00 analyst (5m structure broke; 1H trend is against the trad); 09:15 analyst (15m trend flipped against the trade; 5m structur); 10:00 exit_signal; 10:00 exit
- **my_ema_cross_1h** XAUUSD LONG 3944eb23 → close_past_ema21 (-0.29R, best 0.17R): 11:00 entry (3985.053); 11:00 analyst (1H trend is against the trade); 12:10 analyst (stalled: no new best for 60 min and under +0.5R;); 13:10 analyst (1H trend is against the trade); 14:15 analyst (stalled: no new best for 60 min and under +0.5R;); 14:35 analyst (5m structure broke; stalled: no new best for 60 ); 14:45 analyst (15m trend flipped against the trade; 5m structur); 15:00 exit_signal; 15:00 exit
- **my_ema_cross_1h** US30 LONG 4de8ae50 → close_past_ema21 (-0.76R, best 0.18R): 11:00 entry (52282.0); 11:00 analyst (5m structure broke); 11:05 analyst (trade on track); 11:25 analyst (5m structure broke); 11:30 analyst (15m trend flipped against the trade; 5m structur); 12:00 exit_signal; 12:00 exit
- **my_ema_cross_1h** XAUUSD SHORT 5bb1bd2b → OPEN (R, best 0.00R): 21:00 entry (4033.131)
- **my_ema_cross_1h** US30 LONG 21b09a0d → OPEN (R, best 0.00R): 22:00 entry (52264.700000000004)
- **my_ema_cross_4h** NDQ SHORT f1537166 → OPEN (R, best 1.99R): 21:00 entry (30014.4); 21:00 analyst (trade on track); 04:45 analyst (5m structure broke); 04:50 analyst (trade on track); 05:00 partial (Jev: continuation 0.43 < 0.45); 06:30 analyst (5m structure broke); 06:50 analyst (trade on track); 08:05 analyst (5m structure broke); 08:10 analyst (trade on track); 08:15 analyst (5m structure broke); 08:30 analyst (trade on track); 09:00 partial (Jev: continuation 0.42 < 0.45); 09:30 analyst (5m structure broke); 09:50 analyst (trade on track)
- **my_ema_rsi_15m** US30 LONG c94efac9 → OPEN (R, best 0.00R): 15:30 entry (52692.4)
- **my_ema_rsi_15m** NDQ SHORT c6c3b4f1 → close_past_ema21 (-0.32R, best 0.12R): 21:45 entry (29116.300000000003); 21:45 analyst (trade on track); 22:05 analyst (5m structure broke); 22:10 analyst (trade on track); 22:50 analyst (stalled: no new best for 60 min and under +0.5R); 00:15 exit_signal; 00:15 exit
- **my_ema_rsi_15m** US30 LONG f22f9f0e → close_past_ema21 (-0.00R, best 0.44R): 22:30 entry (52188.0); 22:30 analyst (1H trend is against the trade); 23:30 analyst (15m trend flipped against the trade; 1H trend is); 23:45 analyst (1H trend is against the trade); 00:10 analyst (5m structure broke; stalled: no new best for 60 ); 01:00 analyst (1H trend is against the trade); 02:10 analyst (stalled: no new best for 60 min and under +0.5R;); 02:30 exit_signal; 02:30 exit
- **my_ema_rsi_15m** NDQ LONG 5d8ce702 → close_past_ema21 (-0.84R, best 0.20R): 01:00 entry (28904.4); 01:00 analyst (1H trend is against the trade); 02:05 analyst (stalled: no new best for 60 min and under +0.5R;); 02:15 analyst (15m trend flipped against the trade; stalled: no); 02:20 analyst (15m trend flipped against the trade; 5m structur); 02:30 exit_signal; 02:30 exit
- **my_ema_rsi_15m** NDQ SHORT e6afdc13 → close_past_ema21 (-0.86R, best 0.48R): 04:00 entry (29053.7); 04:00 analyst (trade on track); 04:35 analyst (5m structure broke); 04:45 exit_signal; 04:45 exit
- **my_ema_rsi_15m** XAUUSD LONG 95a73e13 → close_past_ema21 (-0.71R, best 0.18R): 07:00 entry (4009.513); 07:00 analyst (1H trend is against the trade); 07:15 exit_signal; 07:15 exit
- **my_ema_rsi_15m** XAUUSD LONG b30e14cf → close_past_ema21 (-0.39R, best 0.82R): 12:30 entry (4006.0840000000003); 12:30 analyst (1H trend is against the trade); 13:15 agent_check (continuation 0.50 ≥ 0.45); 14:15 analyst (stalled: no new best for 60 min and under +0.5R;); 14:35 analyst (5m structure broke; stalled: no new best for 60 ); 14:45 exit_signal; 14:45 exit
- **my_ema_rsi_15m** US30 SHORT 242cb99e → close_past_ema21 (-0.31R, best 0.27R): 12:45 entry (52562.4); 12:45 analyst (trade on track); 13:20 analyst (5m structure broke); 13:25 analyst (trade on track); 14:30 exit_signal; 14:30 exit
- **my_ema_rsi_15m** XAUUSD SHORT f9c61cc0 → stop (-1.00R, best 0.89R): 19:15 entry (4018.676); 19:15 analyst (trade on track); 20:00 agent_check (continuation 0.46 ≥ 0.45); 20:10 analyst (5m structure broke); 20:12 exit
- **my_ema_rsi_15m** US30 SHORT ce856337 → stop (-1.00R, best 0.07R): 19:15 entry (52411.200000000004); 19:15 analyst (trade on track); 19:40 analyst (5m structure broke); 19:41 exit
- **my_ema_rsi_15m** US30 LONG 53d77db4 → OPEN (R, best 0.00R): 20:30 entry (52285.9)
- **my_ema_rsi_15m** NDQ LONG e041b1c3 → OPEN (R, best 0.00R): 21:45 entry (29311.9)
- **my_ema_rsi_1h** US30 LONG c33f7974 → OPEN (R, best 1.03R): 12:00 entry (52392.5); 12:00 analyst (trade on track); 15:00 analyst (5m structure broke); 15:20 analyst (trade on track); 16:00 partial (Jev: continuation 0.43 < 0.45); 17:00 partial (Jev: continuation 0.43 < 0.45); 17:00 stop_moved (breakeven / 2×ATR trail after +1R)
- **my_ema_rsi_1h** US30 LONG 216b658a → OPEN (R, best 0.00R): 12:00 entry (52439.4)
- **my_ema_rsi_1h** NDQ SHORT 709409e3 → close_past_ema21 (-0.30R, best 0.24R): 21:00 entry (29230.600000000002); 21:00 analyst (trade on track); 22:05 analyst (5m structure broke); 22:10 analyst (trade on track); 22:20 analyst (stalled: no new best for 60 min and under +0.5R); 00:45 analyst (15m trend flipped against the trade; 5m structur); 01:00 exit_signal; 01:00 exit
- **my_ema_rsi_1h** NDQ SHORT 50bb300c → close_past_ema21 (-0.34R, best 0.23R): 03:00 entry (29195.100000000002); 03:00 analyst (trade on track); 04:35 analyst (5m structure broke); 04:45 analyst (15m trend flipped against the trade; 5m structur); 05:00 exit_signal; 05:00 exit
- **my_ema_rsi_1h** XAUUSD SHORT 74231b50 → close_past_ema21 (-0.85R, best 0.09R): 10:00 entry (4028.8340000000003); 10:00 analyst (trade on track); 10:40 analyst (5m structure broke); 10:45 analyst (15m trend flipped against the trade; 5m structur); 11:00 exit_signal; 11:00 exit
- **my_ema_rsi_1h** US30 SHORT 2cfac4f4 → close_past_ema21 (-0.22R, best 0.12R): 12:00 entry (52675.3); 12:00 analyst (trade on track); 13:20 analyst (5m structure broke); 13:25 analyst (trade on track); 14:30 analyst (15m trend flipped against the trade); 14:45 analyst (trade on track); 14:50 analyst (stalled: no new best for 60 min and under +0.5R); 17:00 readopted (app restarted; position restored from the shadow); 20:00 exit_signal; 20:00 exit
- **my_ema_rsi_1h** US30 LONG 11bb8774 → OPEN (R, best 0.00R): 22:00 entry (52264.700000000004)
- **my_ema_rsi_4h** NDQ SHORT 632887d2 → OPEN (R, best 1.05R): 01:00 entry (30014.5); 01:00 analyst (trade on track); 02:55 analyst (stalled: no new best for 60 min and under +0.5R); 03:10 analyst (trade on track); 04:45 analyst (5m structure broke); 04:50 analyst (trade on track); 06:05 analyst (stalled: no new best for 60 min and under +0.5R); 10:25 analyst (trade on track); 11:25 analyst (5m structure broke); 11:30 analyst (trade on track); 12:15 analyst (stalled: no new best for 60 min and under +0.5R); 12:30 analyst (trade on track); 13:00 agent_check (continuation 0.45 ≥ 0.45); 15:25 analyst (5m structure broke)
- **my_ema_rsi_4h** US30 LONG c0daa33b → OPEN (R, best 1.69R): 09:00 entry (52365.4); 09:00 analyst (trade on track); 10:25 analyst (5m structure broke; gave back half of a ≥1R open); 10:30 analyst (15m trend flipped against the trade; 5m structur); 10:55 analyst (gave back half of a ≥1R open profit); 11:00 analyst (stalled: no new best for 60 min and under +0.5R;); 11:20 analyst (trade on track); 13:00 agent_check (continuation 0.48 ≥ 0.45); 13:00 stop_moved (breakeven / 2×ATR trail after +1R)
- **my_intraday_mom** NDQ LONG 5b04f4c6 → session_close (-0.23R, best 0.21R): 15:30 entry (29158.2); 15:30 analyst (trade on track); 15:55 analyst (5m structure broke); 16:00 exit_signal (end of the 15:30-16:00 window); 16:00 exit
- **my_rsi_15m** XAUUSD SHORT d5f69550 → OPEN (R, best 1.14R): 11:15 entry (4084.205); 11:15 analyst (trade on track); 13:00 agent_check (continuation 0.47 ≥ 0.45); 14:00 analyst (stalled: no new best for 60 min and under +0.5R); 14:10 analyst (trade on track); 14:15 partial (Jev: continuation 0.40 < 0.45); 14:20 analyst (stalled: no new best for 60 min and under +0.5R); 14:25 analyst (trade on track); 14:30 partial (Jev: continuation 0.43 < 0.45); 15:45 stop_moved (breakeven / 2×ATR trail after +1R); 16:00 stop_moved (breakeven / 2×ATR trail after +1R); 16:15 stop_moved (breakeven / 2×ATR trail after +1R); 16:30 stop_moved (breakeven / 2×ATR trail after +1R); 16:45 stop_moved (breakeven / 2×ATR trail after +1R)
- **my_rsi_15m** US30 LONG fcd1d2ed → OPEN (R, best 0.00R): 16:00 entry (52692.5)
- **my_rsi_15m** NDQ SHORT 9971e243 → OPEN (R, best 0.00R): 16:45 entry (29085.600000000002)
- **my_rsi_1h** US30 LONG af640ece → OPEN (R, best 0.00R): 16:00 entry (52495.4)
- **my_rsi_1h** XAUUSD SHORT 35e267e6 → close_past_ema21 (-0.85R, best 0.09R): 10:00 entry (4028.8340000000003); 10:00 analyst (trade on track); 10:40 analyst (5m structure broke); 10:45 analyst (15m trend flipped against the trade; 5m structur); 11:00 exit_signal; 11:00 exit
- **my_rsi_4h** US30 LONG 3750c941 → OPEN (R, best 0.00R): 13:00 entry (52361.9)
- **playbook_regime** US30 LONG 05bac06e → OPEN (R, best 0.00R): 20:30 entry (52437.6)
- **shadow** NDQ SHORT ebcda2f4 → OPEN (R, best 0.00R): 22:15 entry (29647.7)
- **shadow** US30 LONG 4dfb39be → OPEN (R, best 0.00R): 20:30 entry (52437.6)
- **shadow** XAUUSD SHORT 13b7e8a3 → stop (-1.00R, best 0.66R): 02:54 entry (4015.677); 02:55 analyst (trade on track); 03:35 analyst (5m structure broke); 03:40 analyst (trade on track); 03:45 analyst (5m structure broke); 03:50 analyst (trade on track); 04:05 analyst (5m structure broke); 04:07 exit
- **shadow** XAUUSD SHORT 1de38240 → stop (-1.00R, best 0.06R): 03:54 entry (4011.686); 03:55 analyst (trade on track); 04:01 exit
- **shadow** US30 LONG 07ed9921 → stop (-1.00R, best 0.06R): 11:15 entry (52331.1); 11:20 analyst (trade on track); 11:25 analyst (5m structure broke); 11:30 analyst (15m trend flipped against the trade; 5m structur); 11:51 exit

## 7. Entry reasons of every trade

- c10_afternoon cf213cd1 NDQ LONG: morning up held to 13:00: 29341.8 vs prior close 28978.7, 3.5 ATR from 09:30, ER 0.53
- ema21_rsi55 11f85acb XAUUSD LONG: EMA21+RSI55: 15m close 4015.20 > EMA21 4012.95, RSI 55.7
- ema21_rsi55 874563ec US30 LONG: EMA21+RSI55: 15m close 52551.40 > EMA21 52422.84, RSI 62.2
- ema21_rsi55 835908fe XAUUSD LONG: EMA21+RSI55: 15m close 4022.16 > EMA21 4011.41, RSI 59.2
- live 5f6a64cb NDQ SHORT: Resistance rejection @ 28979.95
- live 139ba435 US30 LONG: Sweep → MSS → breaker retest
- live 3cc62c71 NDQ LONG: morning up held to 13:00: 29341.8 vs prior close 28978.7, 3.5 ATR from 09:30, ER 0.53
- live 70326449 XAUUSD SHORT: Inverse FVG retest
- my_ema_cross_15m f854a81b US30 LONG: my_ema_cross_15m: 15min close 52342.30 > EMA21 52295.36, RSI 55.4, CHOP 57, Supertrend down
- my_ema_cross_15m cda682ac NDQ LONG: my_ema_cross_15m: 15min close 29034.80 > EMA21 28986.32, RSI 56.3, CHOP 60, Supertrend down
- my_ema_cross_15m 958d6b8c NDQ SHORT: my_ema_cross_15m: 15min close 28916.60 < EMA21 28988.00, RSI 38.7, CHOP 55, Supertrend down
- my_ema_cross_15m e74b6331 NDQ LONG: my_ema_cross_15m: 15min close 29025.20 > EMA21 28980.19, RSI 55.8, CHOP 54, Supertrend down
- my_ema_cross_15m ff83b3b3 NDQ SHORT: my_ema_cross_15m: 15min close 28976.20 < EMA21 28998.23, RSI 47.0, CHOP 43, Supertrend up
- my_ema_cross_15m df38203d US30 LONG: my_ema_cross_15m: 15min close 52406.00 > EMA21 52381.48, RSI 53.8, CHOP 51, Supertrend down
- my_ema_cross_1h 1311e5cd US30 LONG: my_ema_cross_1h: 1h close 52686.60 > EMA21 52651.37, RSI 52.4, CHOP 57, Supertrend up
- my_ema_cross_1h c709fa59 XAUUSD LONG: my_ema_cross_1h: 1h close 4017.70 > EMA21 4010.16, RSI 52.9, CHOP 51, Supertrend down
- my_ema_cross_1h 3944eb23 XAUUSD LONG: my_ema_cross_1h: 1h close 4023.24 > EMA21 4011.12, RSI 54.9, CHOP 55, Supertrend down
- my_ema_cross_1h 4de8ae50 US30 LONG: my_ema_cross_1h: 1h close 52488.80 > EMA21 52416.61, RSI 54.8, CHOP 47, Supertrend down
- my_ema_cross_1h 5bb1bd2b XAUUSD SHORT: my_ema_cross_1h: 1h close 4009.57 < EMA21 4012.46, RSI 47.7, CHOP 55, Supertrend down
- my_ema_cross_1h 21b09a0d US30 LONG: my_ema_cross_1h: 1h close 52477.00 > EMA21 52406.15, RSI 56.0, CHOP 57, Supertrend down
- my_ema_cross_4h f1537166 NDQ SHORT: my_ema_cross_4h: 4h close 29638.90 < EMA21 29715.93, RSI 45.9, CHOP 55, Supertrend down
- my_ema_rsi_15m c94efac9 US30 LONG: my_ema_rsi_15m: 15min close 52851.00 > EMA21 52781.32, RSI 57.8, CHOP 59, Supertrend up
- my_ema_rsi_15m c6c3b4f1 NDQ SHORT: my_ema_rsi_15m: 15min close 28918.80 < EMA21 29011.85, RSI 40.3, CHOP 47, Supertrend down
- my_ema_rsi_15m f22f9f0e US30 LONG: my_ema_rsi_15m: 15min close 52342.30 > EMA21 52295.36, RSI 55.4, CHOP 57, Supertrend down
- my_ema_rsi_15m 5d8ce702 NDQ LONG: my_ema_rsi_15m: 15min close 29034.80 > EMA21 28986.32, RSI 56.3, CHOP 60, Supertrend down
- my_ema_rsi_15m 7bd66d5a XAUUSD LONG: my_ema_rsi_15m: 15min close 4009.76 > EMA21 4007.16, RSI 55.2, CHOP 57, Supertrend up
- my_ema_rsi_15m e6afdc13 NDQ SHORT: my_ema_rsi_15m: 15min close 28937.40 < EMA21 28977.08, RSI 43.2, CHOP 54, Supertrend down
- my_ema_rsi_15m 95a73e13 XAUUSD LONG: my_ema_rsi_15m: 15min close 4015.20 > EMA21 4012.95, RSI 55.7, CHOP 53, Supertrend up
- my_ema_rsi_15m 66294d3d NDQ LONG: my_ema_rsi_15m: 15min close 29160.20 > EMA21 29078.43, RSI 60.9, CHOP 53, Supertrend up
- my_ema_rsi_15m b30e14cf XAUUSD LONG: my_ema_rsi_15m: 15min close 4018.99 > EMA21 4014.89, RSI 55.3, CHOP 43, Supertrend up
- my_ema_rsi_15m 242cb99e US30 SHORT: my_ema_rsi_15m: 15min close 52350.60 < EMA21 52417.46, RSI 43.3, CHOP 54, Supertrend down
- my_ema_rsi_15m f9c61cc0 XAUUSD SHORT: my_ema_rsi_15m: 15min close 4011.32 < EMA21 4014.74, RSI 42.7, CHOP 59, Supertrend up
- my_ema_rsi_15m ce856337 US30 SHORT: my_ema_rsi_15m: 15min close 52308.00 < EMA21 52374.32, RSI 38.3, CHOP 54, Supertrend down
- my_ema_rsi_15m 53d77db4 US30 LONG: my_ema_rsi_15m: 15min close 52418.00 > EMA21 52384.80, RSI 55.6, CHOP 50, Supertrend down
- my_ema_rsi_15m e041b1c3 NDQ LONG: my_ema_rsi_15m: 15min close 29399.00 > EMA21 29368.60, RSI 56.8, CHOP 51, Supertrend up
- my_ema_rsi_1h c33f7974 US30 LONG: my_ema_rsi_1h: 1h close 52681.60 > EMA21 52537.68, RSI 58.9, CHOP 56, Supertrend up
- my_ema_rsi_1h 216b658a US30 LONG: my_ema_rsi_1h: 1h close 52863.60 > EMA21 52670.66, RSI 59.9, CHOP 57, Supertrend up
- my_ema_rsi_1h 709409e3 NDQ SHORT: my_ema_rsi_1h: 1h close 28952.40 < EMA21 29044.12, RSI 43.0, CHOP 60, Supertrend down
- my_ema_rsi_1h 50bb300c NDQ SHORT: my_ema_rsi_1h: 1h close 28939.00 < EMA21 29018.41, RSI 43.7, CHOP 61, Supertrend down
- my_ema_rsi_1h 74231b50 XAUUSD SHORT: my_ema_rsi_1h: 1h close 3993.18 < EMA21 4009.90, RSI 38.4, CHOP 52, Supertrend down
- my_ema_rsi_1h 2cfac4f4 US30 SHORT: my_ema_rsi_1h: 1h close 52333.60 < EMA21 52409.07, RSI 43.4, CHOP 59, Supertrend down
- my_ema_rsi_1h 11bb8774 US30 LONG: my_ema_rsi_1h: 1h close 52477.00 > EMA21 52406.15, RSI 56.0, CHOP 57, Supertrend down
- my_ema_rsi_4h 632887d2 NDQ SHORT: my_ema_rsi_4h: 4h close 29465.60 < EMA21 29693.18, RSI 41.1, CHOP 56, Supertrend down
- my_ema_rsi_4h c0daa33b US30 LONG: my_ema_rsi_4h: 4h close 52587.00 > EMA21 52452.03, RSI 56.2, CHOP 46, Supertrend up
- my_intraday_mom 5b04f4c6 NDQ LONG: my_intraday_mom: first half-hour +0.292% (16:00 close 28978.70 -> 10:00 29063.20) -> long 15:30-16:00
- my_intraday_mom 85cf3db3 US30 LONG: my_intraday_mom: first half-hour +0.303% (16:00 close 52235.00 -> 10:00 52393.40) -> long 15:30-16:00
- my_rsi_15m d5f69550 XAUUSD SHORT: my_rsi_15m: 15min close 4055.01 < EMA21 4068.51, RSI 38.3, CHOP 49, Supertrend down
- my_rsi_15m fcd1d2ed US30 LONG: my_rsi_15m: 15min close 52911.00 > EMA21 52798.62, RSI 62.1, CHOP 61, Supertrend up
- my_rsi_15m 9971e243 NDQ SHORT: my_rsi_15m: 15min close 28968.60 < EMA21 29041.31, RSI 38.9, CHOP 59, Supertrend down
- my_rsi_1h af640ece US30 LONG: my_rsi_1h: 1h close 52911.00 > EMA21 52722.60, RSI 60.6, CHOP 58, Supertrend up
- my_rsi_1h 35e267e6 XAUUSD SHORT: my_rsi_1h: 1h close 3993.18 < EMA21 4009.90, RSI 38.4, CHOP 52, Supertrend down
- my_rsi_4h 3750c941 US30 LONG: my_rsi_4h: 4h close 52841.00 > EMA21 52487.40, RSI 61.9, CHOP 49, Supertrend up
- playbook_regime 05bac06e US30 LONG: DTFX close_fib BOS → 50-70% zone rejection · playbook level=50-70/trend p=0.47
- shadow ebcda2f4 NDQ SHORT: DTFX wick_fib BOS → 50-70% zone rejection · playbook level=50-70/std p=0.55
- shadow 4dfb39be US30 LONG: DTFX close_fib BOS → 50-70% zone rejection · playbook level=50-70/trend p=0.47
- shadow 13b7e8a3 XAUUSD SHORT: DTFX wick_fib BOS → 50% rejection · playbook sessions=killzones/std p=0.59
- shadow 1de38240 XAUUSD SHORT: Sweep → MSS (displacement CHoCH) · playbook default/std p=0.61
- shadow 7c197d46 XAUUSD SHORT: Sweep → MSS (displacement CHoCH) · playbook default/std p=0.61
- shadow 2a409407 XAUUSD SHORT: DTFX wick_fib flip → 50% rejection · playbook sessions=killzones/std p=0.59
- shadow 07ed9921 US30 LONG: DTFX close_fib flip → 50-70% zone rejection · playbook level=50-70/std p=0.62
