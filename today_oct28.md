# RSI / EMA books report

Generated 2026-10-28 23:17 New York. Window: since 2026-10-28 00:00 (23 h). R = profit as a multiple of the risk at the first stop.

Books read: live, c10_afternoon, daily_rsi2_adx2, ema21_rsi55, h1_vol_trend, my_ema_cross_15m, my_ema_cross_1d, my_ema_cross_1h, my_ema_cross_4h, my_ema_rsi_15m, my_ema_rsi_1d, my_ema_rsi_1h, my_ema_rsi_4h, my_intraday_mom, my_rsi_15m, my_rsi_1h, my_rsi_4h, playbook_regime, shadow

## 1. Per book

| Book | Trades | Closed | Open | Wins | Total R | P&L | Avg best R | Avg hours held | Jev partials |
|---|---|---|---|---|---|---|---|---|---|
| live | 1 | 1 | 0 | 1 | +0.55 | +87.04 | 1.43 | 0.5 | 1 |
| c10_afternoon | 0 | 0 | 0 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 0 |
| daily_rsi2_adx2 | 0 | 0 | 0 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 0 |
| ema21_rsi55 | 4 | 4 | 0 | 1 | -0.92 | -64.11 | 0.28 | 0.8 | 0 |
| h1_vol_trend | 0 | 0 | 0 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 0 |
| my_ema_cross_15m | 3 | 2 | 1 | 0 | -0.60 | -211.07 | 0.41 | 0.7 | 0 |
| my_ema_cross_1d | 0 | 0 | 0 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 0 |
| my_ema_cross_1h | 3 | 3 | 0 | 1 | -0.90 | -311.56 | 0.68 | 53.4 | 0 |
| my_ema_cross_4h | 4 | 3 | 1 | 2 | +0.73 | +257.26 | 0.99 | 69.5 | 2 |
| my_ema_rsi_15m | 16 | 14 | 2 | 7 | +0.09 | +33.49 | 1.07 | 1.5 | 6 |
| my_ema_rsi_1d | 1 | 0 | 1 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 0 |
| my_ema_rsi_1h | 9 | 7 | 2 | 2 | -0.41 | -135.25 | 0.58 | 32.4 | 4 |
| my_ema_rsi_4h | 4 | 3 | 1 | 2 | +0.04 | +18.96 | 0.66 | 67.9 | 1 |
| my_intraday_mom | 2 | 2 | 0 | 2 | +0.85 | +293.59 | 0.47 | 0.5 | 0 |
| my_rsi_15m | 5 | 2 | 3 | 2 | +1.13 | +394.81 | 1.60 | 4.7 | 5 |
| my_rsi_1h | 1 | 0 | 1 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 0 |
| my_rsi_4h | 1 | 0 | 1 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 0 |
| playbook_regime | 1 | 0 | 1 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 0 |
| shadow | 4 | 2 | 2 | 2 | +1.33 | +227.49 | 1.26 | 3.3 | 1 |

All listed books: 43 closed trades, +1.89 R.

## 2. Why the losing trades lost

| Cause | Trades | R |
|---|---|---|
| closed on the EMA exit at a loss | 14 | -6.27 |
| stopped at the first stop | 5 | -3.35 |
| gave back: was +0.5R or better first | 1 | -0.30 |

## 3. Skipped signals (what the filters blocked)

**live**: 10x filtered: bias neutral (#); 5x filtered: counter to BEARISH bias; 1x taken: qty #, risk $#, cost #R; 1x skipped: Jev quality # < #; 1x filtered: counter to BULLISH bias
**ema21_rsi55**: 4x taken: qty #, jev #; 3x rejected: choppy market (CHOP # ≥ #); 2x rejected: news blackout: FOMC Press Conference
**my_ema_cross_15m**: 5x rejected: trading halted: daily loss limit hit ($#,#); 5x rejected: choppy market (CHOP # ≥ #); 3x rejected: stop too wide (# ATR); 3x taken: qty #, jev #
**my_ema_cross_1h**: 2x taken: qty #, jev #; 2x rejected: stop too wide (# ATR)
**my_ema_cross_4h**: 2x taken: qty #, jev #
**my_ema_rsi_15m**: 13x taken: qty #, jev #; 8x rejected: stop too wide (# ATR); 6x rejected: choppy market (CHOP # ≥ #); 2x rejected: news blackout: Federal Funds Rate; 2x rejected: news blackout: FOMC Press Conference; 1x rejected: not a fresh cross (the price has been below the EMA# for # candles, limit #
**my_ema_rsi_1d**: 1x taken: qty #, jev #
**my_ema_rsi_1h**: 5x taken: qty #, jev #; 2x rejected: stop too wide (# ATR)
**my_ema_rsi_4h**: 1x rejected: choppy market (CHOP # ≥ #); 1x taken: qty #, jev #
**my_intraday_mom**: 2x taken: qty #, jev None
**my_rsi_15m**: 1x taken: qty #, jev #; 1x rejected: choppy market (CHOP # ≥ #)
**playbook_regime**: 20x filtered: bias neutral (#); 15x filtered: counter to BEARISH bias; 12x skipped: regime chop (Jev chop #, CHOP #): scalps only; 2x rejected: outside entry windows; 2x filtered: counter to BULLISH bias; 1x rejected: cost #R of the stop (spread # vs stop #) > cap #R; 1x skipped: Jev quality # < #
**shadow**: 20x filtered: bias neutral (#); 15x filtered: counter to BEARISH bias; 7x skipped: Jev quality # < #; 2x rejected: outside entry windows; 2x taken: qty #, risk $#, cost #R; 2x skipped: playbook: XAUUSD already has # position(s); 2x filtered: counter to BULLISH bias; 1x rejected: cost #R of the stop (spread # vs stop #) > cap #R

## 4. Trade analyst (shadow) - how its advice scored

| Book | Check | Times | Avg value in R (positive = its advice would have helped) | Helpful |
|---|---|---|---|---|
| live | any_exit | 9 | +0.18 | 6 |
| live | giveback | 4 | +0.04 | 3 |
| live | h1_against | 5 | -0.22 | 2 |
| live | stall | 3 | -0.19 | 1 |
| live | structure_break | 7 | +0.34 | 5 |
| live | trend_flip | 6 | +0.24 | 5 |
| c10_afternoon | any_exit | 3 | -0.43 | 0 |
| c10_afternoon | giveback | 1 | -1.33 | 0 |
| c10_afternoon | stall | 2 | -0.47 | 0 |
| c10_afternoon | structure_break | 3 | -0.52 | 0 |
| ema21_rsi55 | any_exit | 10 | -0.13 | 6 |
| ema21_rsi55 | giveback | 1 | -0.05 | 0 |
| ema21_rsi55 | h1_against | 9 | -0.21 | 6 |
| ema21_rsi55 | stall | 8 | -0.21 | 6 |
| ema21_rsi55 | structure_break | 9 | +0.06 | 4 |
| h1_vol_trend | any_exit | 1 | -0.90 | 0 |
| h1_vol_trend | stall | 1 | -0.96 | 0 |
| h1_vol_trend | structure_break | 1 | -0.90 | 0 |
| my_ema_cross_15m | any_exit | 11 | +0.11 | 9 |
| my_ema_cross_15m | giveback | 1 | +0.03 | 1 |
| my_ema_cross_15m | h1_against | 15 | -0.02 | 10 |
| my_ema_cross_15m | stall | 4 | +0.06 | 2 |
| my_ema_cross_15m | structure_break | 11 | +0.14 | 9 |
| my_ema_cross_15m | trend_flip | 3 | -0.09 | 1 |
| my_ema_cross_1h | any_exit | 14 | +0.26 | 12 |
| my_ema_cross_1h | giveback | 1 | +0.12 | 1 |
| my_ema_cross_1h | h1_against | 5 | +0.50 | 5 |
| my_ema_cross_1h | news_soon | 1 | +0.16 | 1 |
| my_ema_cross_1h | stall | 9 | +0.36 | 9 |
| my_ema_cross_1h | structure_break | 14 | +0.23 | 11 |
| my_ema_cross_1h | trend_flip | 10 | +0.25 | 10 |
| my_ema_cross_4h | any_exit | 2 | -0.04 | 1 |
| my_ema_cross_4h | news_soon | 2 | +0.14 | 1 |
| my_ema_cross_4h | stall | 2 | +0.03 | 1 |
| my_ema_cross_4h | structure_break | 2 | -0.04 | 1 |
| my_ema_cross_4h | trend_flip | 2 | +0.24 | 2 |
| my_ema_rsi_15m | any_exit | 37 | -0.03 | 22 |
| my_ema_rsi_15m | giveback | 10 | +0.04 | 9 |
| my_ema_rsi_15m | h1_against | 33 | +0.09 | 20 |
| my_ema_rsi_15m | news_soon | 1 | +0.11 | 1 |
| my_ema_rsi_15m | stall | 16 | -0.05 | 8 |
| my_ema_rsi_15m | structure_break | 33 | -0.01 | 17 |
| my_ema_rsi_15m | trend_flip | 8 | +0.17 | 6 |
| my_ema_rsi_1h | any_exit | 21 | +0.19 | 15 |
| my_ema_rsi_1h | giveback | 1 | +0.07 | 1 |
| my_ema_rsi_1h | h1_against | 3 | +0.50 | 3 |
| my_ema_rsi_1h | news_soon | 1 | -0.20 | 0 |
| my_ema_rsi_1h | stall | 13 | +0.30 | 11 |
| my_ema_rsi_1h | structure_break | 21 | +0.16 | 15 |
| my_ema_rsi_1h | trend_flip | 18 | +0.11 | 13 |
| my_ema_rsi_4h | any_exit | 3 | +0.20 | 2 |
| my_ema_rsi_4h | h1_against | 1 | +0.12 | 1 |
| my_ema_rsi_4h | news_soon | 1 | +0.28 | 1 |
| my_ema_rsi_4h | stall | 3 | +0.24 | 2 |
| my_ema_rsi_4h | structure_break | 3 | +0.04 | 1 |
| my_ema_rsi_4h | trend_flip | 3 | +0.19 | 3 |
| my_intraday_mom | any_exit | 6 | +0.02 | 3 |
| my_intraday_mom | h1_against | 3 | +0.07 | 2 |
| my_intraday_mom | structure_break | 6 | +0.02 | 3 |
| my_rsi_15m | any_exit | 7 | -0.07 | 4 |
| my_rsi_15m | giveback | 3 | -0.02 | 2 |
| my_rsi_15m | stall | 4 | -0.05 | 2 |
| my_rsi_15m | structure_break | 7 | -0.04 | 4 |
| my_rsi_1h | any_exit | 3 | -0.12 | 2 |
| my_rsi_1h | giveback | 1 | +0.29 | 1 |
| my_rsi_1h | stall | 2 | -0.40 | 1 |
| my_rsi_1h | structure_break | 3 | -0.12 | 2 |
| my_rsi_1h | trend_flip | 3 | -0.27 | 2 |
| playbook_regime | any_exit | 1 | -0.54 | 0 |
| playbook_regime | giveback | 3 | -0.04 | 2 |
| playbook_regime | stall | 1 | -0.19 | 0 |
| playbook_regime | structure_break | 1 | -0.54 | 0 |
| shadow | any_exit | 19 | +0.06 | 11 |
| shadow | giveback | 7 | +0.05 | 6 |
| shadow | h1_against | 8 | -0.10 | 3 |
| shadow | stall | 11 | +0.12 | 6 |
| shadow | structure_break | 17 | +0.03 | 10 |
| shadow | trend_flip | 5 | +0.27 | 5 |

## 5. Every trade in the window

| Book | Id | Market | Side | Opened (NY) | Closed (NY) | Entry | Exit | First stop | Stop at end | Qty | P&L | R | Best R | Worst R | How it ended |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ema21_rsi55 | 92a06f11 | US30 | SHORT | 10-28 04:15 | 10-28 04:45 | 52290.20 | 52328.70 | 52395.60 | 52395.60 | 0.66 | -25.41 | -0.36 | 0.12 | -0.36 | close_above_ema21 |
| ema21_rsi55 | 6af0aef8 | XAUUSD | LONG | 10-28 08:15 | 10-28 10:00 | 4052.96 | 4049.64 | 4038.38 | 4038.38 | 4.70 | -15.60 | -0.23 | 0.49 | -0.49 | close_below_ema21 |
| ema21_rsi55 | dc93b775 | XAUUSD | SHORT | 10-28 15:00 | 10-28 15:15 | 4032.84 | 4051.93 | 4062.76 | 4062.76 | 2.30 | -43.91 | -0.64 | 0.19 | -0.73 | close_above_ema21 |
| ema21_rsi55 | 5f3cc758 | XAUUSD | LONG | 10-28 15:15 | 10-28 15:50 | 4051.93 | 4062.34 | 4018.26 | 4018.26 | 2.00 | 20.81 | 0.31 | 0.33 | -0.34 | session_flat |
| live | 878bf5b0 | NDQ | SHORT | 10-28 10:35 | 10-28 11:03 | 29699.40 | 29695.93 | 29734.50 | 29695.90 | 4.51 | 87.04 | 0.55 | 1.43 | -0.25 | breakeven_plus_stop |
| my_ema_cross_15m | d83bc33d | XAUUSD | SHORT | 10-28 20:15 | 10-28 21:15 | 4044.35 | 4054.01 | 4066.36 | 4066.36 | 15.90 | -153.51 | -0.44 | 0.37 | -0.53 | close_past_ema21 |
| my_ema_cross_15m | 35371060 | XAUUSD | LONG | 10-28 21:45 | 10-28 22:15 | 4056.05 | 4052.36 | 4033.68 | 4033.68 | 15.60 | -57.56 | -0.17 | 0.45 | -0.30 | close_past_ema21 |
| my_ema_cross_15m | 758f2ac8 | XAUUSD | SHORT | 10-28 22:45 | open | 4042.97 |  | 4071.51 | 4071.51 | 12.20 | 0.00 |  | 0.00 | 0.00 | OPEN |
| my_ema_cross_1h | 1311e5cd | US30 | LONG | 10-22 11:00 | 10-28 23:09 | 52688.10 | 52688.10 | 52441.20 | 52688.10 | 1.42 | 0.00 | 0.00 | 1.12 | -0.18 | stop |
| my_ema_cross_1h | 9c681328 | US30 | LONG | 10-28 11:00 | 10-28 14:01 | 52482.30 | 52507.30 | 52232.40 | 52507.30 | 1.39 | 34.75 | 0.10 | 0.78 | -0.11 | stop |
| my_ema_cross_1h | f990a79c | XAUUSD | SHORT | 10-28 15:00 | 10-28 15:59 | 4032.84 | 4070.90 | 4070.90 | 4070.90 | 9.10 | -346.31 | -1.00 | 0.15 | -0.92 | stop |
| my_ema_cross_4h | f1537166 | NDQ | SHORT | 10-21 21:00 | 10-28 23:07 | 29637.80 | 29415.20 | 30014.40 | 29351.10 | 0.93 | 290.23 | 0.83 | 1.99 | -0.05 | stop |
| my_ema_cross_4h | 74f738ac | NDQ | LONG | 10-27 09:00 | 10-28 18:26 | 29463.60 | 29527.40 | 28825.10 | 29527.40 | 0.55 | 35.09 | 0.10 | 0.91 | -0.16 | stop |
| my_ema_cross_4h | e4d32e5d | XAUUSD | LONG | 10-28 09:00 | 10-28 13:55 | 4053.72 | 4039.82 | 3982.76 | 3982.76 | 4.90 | -68.06 | -0.20 | 0.06 | -0.25 | pre-news: Federal Funds Rate |
| my_ema_cross_4h | dd479e2f | US30 | LONG | 10-28 17:00 | open | 52616.10 |  | 52189.60 | 52189.60 | 0.81 | 0.00 |  | 0.00 | 0.00 | OPEN |
| my_ema_rsi_15m | c94efac9 | US30 | LONG | 10-22 15:30 | open | 52852.50 |  | 52692.40 | 52692.40 | 2.21 | 0.00 |  | 0.00 | 0.00 | OPEN |
| my_ema_rsi_15m | f94b2d73 | NDQ | LONG | 10-27 17:00 | 10-28 00:39 | 29664.80 | 29759.00 | 29635.40 | 29759.00 | 11.96 | 728.36 | 2.07 | 5.48 | -0.57 | stop |
| my_ema_rsi_15m | 46a11632 | US30 | SHORT | 10-27 23:30 | 10-28 03:11 | 52335.20 | 52298.80 | 52379.10 | 52298.80 | 8.07 | 236.90 | 0.67 | 2.07 | -0.27 | stop |
| my_ema_rsi_15m | edeb373f | NDQ | LONG | 10-28 06:00 | 10-28 06:15 | 29816.20 | 29784.20 | 29747.60 | 29747.60 | 5.17 | -165.44 | -0.47 | 0.06 | -0.86 | close_past_ema21 |
| my_ema_rsi_15m | cca066e1 | XAUUSD | LONG | 10-28 08:15 | 10-28 10:00 | 4052.96 | 4049.64 | 4041.87 | 4041.87 | 31.90 | -105.91 | -0.30 | 0.65 | -0.65 | close_past_ema21 |
| my_ema_rsi_15m | fcd306e4 | NDQ | SHORT | 10-28 09:45 | 10-28 10:05 | 29742.20 | 29725.50 | 29843.50 | 29725.50 | 3.49 | 58.28 | 0.17 | 1.05 | -0.04 | stop |
| my_ema_rsi_15m | 0f879900 | XAUUSD | SHORT | 10-28 11:30 | 10-28 14:01 | 4043.18 | 4042.09 | 4054.04 | 4042.09 | 32.60 | 101.73 | 0.29 | 0.65 | -0.48 | stop |
| my_ema_rsi_15m | 52de5818 | NDQ | SHORT | 10-28 12:00 | 10-28 12:55 | 29711.60 | 29750.50 | 29750.50 | 29750.50 | 9.11 | -354.38 | -1.00 | 0.42 | -0.49 | stop |
| my_ema_rsi_15m | 42dec4c9 | XAUUSD | LONG | 10-28 15:15 | 10-28 16:29 | 4051.93 | 4058.33 | 4021.86 | 4058.33 | 11.70 | 74.83 | 0.21 | 1.03 | -0.38 | stop |
| my_ema_rsi_15m | d12ce22e | US30 | SHORT | 10-28 15:15 | 10-28 15:45 | 52435.10 | 52519.10 | 52668.00 | 52668.00 | 1.51 | -126.84 | -0.36 | 0.23 | -0.45 | close_past_ema21 |
| my_ema_rsi_15m | 0a1a3ce4 | NDQ | LONG | 10-28 15:45 | 10-28 16:15 | 29784.20 | 29773.80 | 29635.50 | 29635.50 | 2.37 | 75.06 | 0.21 | 1.75 | -0.07 | trail_through |
| my_ema_rsi_15m | 01f8ad26 | US30 | LONG | 10-28 16:00 | 10-28 16:15 | 52570.10 | 52607.60 | 52350.60 | 52350.60 | 1.61 | 60.38 | 0.17 | 1.10 | -0.30 | trail_through |
| my_ema_rsi_15m | 2a3ee83e | US30 | LONG | 10-28 19:15 | 10-28 19:45 | 52588.10 | 52535.60 | 52496.90 | 52496.90 | 3.84 | -201.60 | -0.58 | 0.16 | -0.85 | close_past_ema21 |
| my_ema_rsi_15m | 7d727584 | US30 | LONG | 10-28 20:15 | open | 52592.10 |  | 52492.40 | 52656.90 | 3.50 | 230.12 |  | 1.87 | -0.33 | OPEN |
| my_ema_rsi_15m | 0fcb2a23 | XAUUSD | SHORT | 10-28 20:30 | 10-28 21:15 | 4042.06 | 4054.01 | 4060.76 | 4060.76 | 18.60 | -222.18 | -0.64 | 0.31 | -0.74 | close_past_ema21 |
| my_ema_rsi_15m | 74a3c3e0 | XAUUSD | LONG | 10-28 22:00 | 10-28 22:15 | 4062.84 | 4052.36 | 4033.59 | 4033.59 | 12.00 | -125.70 | -0.36 | 0.07 | -0.46 | close_past_ema21 |
| my_ema_rsi_1d | 4e7ae8d4 | US30 | LONG | 10-28 17:00 | open | 52616.10 |  | 51704.30 | 51704.30 | 0.38 | 0.00 |  | 0.00 | 0.00 | OPEN |
| my_ema_rsi_1h | c33f7974 | US30 | LONG | 10-21 12:00 | 10-28 23:07 | 52683.10 | 52697.70 | 52392.50 | 52697.70 | 1.21 | 196.59 | 0.56 | 1.03 | -0.20 | stop |
| my_ema_rsi_1h | 216b658a | US30 | LONG | 10-22 12:00 | open | 52865.10 |  | 52439.40 | 52439.40 | 0.82 | 0.00 |  | 0.00 | 0.00 | OPEN |
| my_ema_rsi_1h | 0636d104 | NDQ | LONG | 10-27 06:00 | 10-28 09:48 | 29342.80 | 29697.20 | 29126.80 | 29697.20 | 1.62 | 573.66 | 1.64 | 2.37 | -0.40 | stop |
| my_ema_rsi_1h | 2704ca3a | US30 | SHORT | 10-27 22:00 | 10-28 09:00 | 52283.20 | 52443.70 | 52523.00 | 52523.00 | 1.45 | -232.72 | -0.67 | 0.16 | -0.76 | close_past_ema21 |
| my_ema_rsi_1h | e1c9c2d6 | XAUUSD | LONG | 10-28 05:00 | 10-28 11:00 | 4053.28 | 4041.45 | 4025.45 | 4025.45 | 12.50 | -147.94 | -0.42 | 0.25 | -0.59 | close_past_ema21 |
| my_ema_rsi_1h | be6b6d0a | NDQ | LONG | 10-28 13:00 | 10-28 13:55 | 29754.40 | 29733.30 | 29614.20 | 29614.20 | 2.48 | -52.33 | -0.15 | 0.04 | -0.54 | pre-news: Federal Funds Rate |
| my_ema_rsi_1h | 876a89d0 | XAUUSD | SHORT | 10-28 15:00 | 10-28 15:59 | 4032.84 | 4070.90 | 4070.90 | 4070.90 | 9.10 | -346.31 | -1.00 | 0.15 | -0.92 | stop |
| my_ema_rsi_1h | ee5142d6 | US30 | LONG | 10-28 16:00 | open | 52570.10 |  | 52252.70 | 52252.70 | 1.09 | 0.00 |  | 0.00 | 0.00 | OPEN |
| my_ema_rsi_1h | 42926942 | XAUUSD | LONG | 10-28 22:00 | 10-28 23:00 | 4062.84 | 4047.45 | 4020.40 | 4020.40 | 8.20 | -126.20 | -0.36 | 0.05 | -0.54 | close_past_ema21 |
| my_ema_rsi_4h | 632887d2 | NDQ | SHORT | 10-22 01:00 | 10-28 23:07 | 29464.40 | 29415.20 | 30014.50 | 29351.10 | 0.64 | 181.63 | 0.52 | 1.05 | -0.01 | stop |
| my_ema_rsi_4h | c0daa33b | US30 | LONG | 10-22 09:00 | open | 52588.50 |  | 52365.40 | 52588.50 | 1.58 | 0.00 |  | 1.69 | -0.25 | OPEN |
| my_ema_rsi_4h | 6bc1d4a3 | NDQ | LONG | 10-27 09:00 | 10-28 18:26 | 29463.60 | 29527.40 | 28825.10 | 29527.40 | 0.55 | 35.09 | 0.10 | 0.91 | -0.16 | stop |
| my_ema_rsi_4h | 6a42dbd0 | XAUUSD | LONG | 10-28 17:00 | 10-28 21:00 | 4067.60 | 4036.70 | 4013.69 | 4013.69 | 6.40 | -197.76 | -0.57 | 0.01 | -0.58 | close_past_ema21 |
| my_intraday_mom | f4187774 | NDQ | LONG | 10-28 15:30 | 10-28 16:00 | 29744.00 | 29858.30 | 29524.20 | 29524.20 | 1.58 | 180.59 | 0.52 | 0.57 | -0.11 | session_close |
| my_intraday_mom | bdfd7a1d | US30 | LONG | 10-28 15:30 | 10-28 16:00 | 52476.70 | 52567.10 | 52199.30 | 52199.30 | 1.25 | 113.00 | 0.33 | 0.37 | -0.11 | session_close |
| my_rsi_15m | d5f69550 | XAUUSD | SHORT | 10-22 11:15 | open | 4054.70 |  | 4084.20 | 4034.91 | 11.90 | 159.92 |  | 1.14 | -0.22 | OPEN |
| my_rsi_15m | fcd1d2ed | US30 | LONG | 10-22 16:00 | open | 52912.50 |  | 52692.50 | 52692.50 | 1.61 | 0.00 |  | 0.00 | 0.00 | OPEN |
| my_rsi_15m | 9971e243 | NDQ | SHORT | 10-22 16:45 | open | 28967.40 |  | 29085.60 | 29085.60 | 3.00 | 0.00 |  | 0.00 | 0.00 | OPEN |
| my_rsi_15m | 2cc2354d | NDQ | LONG | 10-27 18:30 | 10-28 00:39 | 29694.80 | 29759.00 | 29635.60 | 29759.00 | 5.89 | 259.36 | 0.74 | 2.22 | -0.45 | stop |
| my_rsi_15m | f540ce43 | NDQ | LONG | 10-28 01:30 | 10-28 04:45 | 29796.80 | 29793.80 | 29738.30 | 29738.30 | 5.98 | 135.45 | 0.39 | 0.98 | -0.52 | close_past_ema21 |
| my_rsi_1h | af640ece | US30 | LONG | 10-22 16:00 | open | 52912.50 |  | 52495.40 | 52495.40 | 0.84 | 0.00 |  | 0.00 | 0.00 | OPEN |
| my_rsi_4h | 3750c941 | US30 | LONG | 10-22 13:00 | open | 52842.50 |  | 52361.90 | 52361.90 | 0.73 | 0.00 |  | 0.00 | 0.00 | OPEN |
| playbook_regime | 05bac06e | US30 | LONG | 10-20 20:30 | open | 52554.50 |  | 52437.60 | 52437.60 | 2.78 | 0.00 |  | 0.00 | 0.00 | OPEN |
| shadow | ebcda2f4 | NDQ | SHORT | 10-19 22:15 | open | 29545.40 |  | 29647.70 | 29647.70 | 3.34 | 0.00 |  | 0.00 | 0.00 | OPEN |
| shadow | 4dfb39be | US30 | LONG | 10-20 20:30 | open | 52554.50 |  | 52437.60 | 52437.60 | 2.73 | 0.00 |  | 0.00 | 0.00 | OPEN |
| shadow | 8ad91af1 | XAUUSD | SHORT | 10-28 08:48 | 10-28 11:22 | 4051.74 | 4045.68 | 4060.42 | 4050.87 | 19.50 | 150.86 | 0.89 | 1.71 | -0.71 | trail_stop |
| shadow | 2fddf60b | XAUUSD | SHORT | 10-28 09:35 | 10-28 13:36 | 4047.00 | 4041.06 | 4060.51 | 4060.51 | 12.90 | 76.63 | 0.44 | 0.81 | -0.37 | max_hold |

## 6. Timelines of the losing and the open trades

- **ema21_rsi55** US30 SHORT 92a06f11 → close_above_ema21 (-0.36R, best 0.12R): 04:15 entry (52395.600000000006); 04:15 analyst (trade on track); 04:45 exit_signal; 04:45 exit
- **ema21_rsi55** XAUUSD LONG 6af0aef8 → close_below_ema21 (-0.23R, best 0.49R): 08:15 entry (4038.378); 08:15 analyst (trade on track); 09:25 analyst (stalled: no new best for 60 min and under +0.5R); 09:35 analyst (5m structure broke; stalled: no new best for 60 ); 10:00 exit_signal; 10:00 exit
- **ema21_rsi55** XAUUSD SHORT dc93b775 → close_above_ema21 (-0.64R, best 0.19R): 15:00 entry (4062.756); 15:00 analyst (trade on track); 15:15 exit_signal; 15:15 exit
- **my_ema_cross_15m** XAUUSD SHORT d83bc33d → close_past_ema21 (-0.44R, best 0.37R): 20:15 entry (4066.359); 20:15 analyst (1H trend is against the trade); 21:00 analyst (trade on track); 21:15 exit_signal; 21:15 exit
- **my_ema_cross_15m** XAUUSD LONG 35371060 → close_past_ema21 (-0.17R, best 0.45R): 21:45 entry (4033.677); 21:45 analyst (1H trend is against the trade); 22:00 analyst (trade on track); 22:15 exit_signal; 22:15 exit
- **my_ema_cross_15m** XAUUSD SHORT 758f2ac8 → OPEN (R, best 0.00R): 22:45 entry (4071.506)
- **my_ema_cross_1h** XAUUSD SHORT f990a79c → stop (-1.00R, best 0.15R): 15:00 entry (4070.9010000000003); 15:00 analyst (trade on track); 15:15 analyst (15m trend flipped against the trade); 15:30 analyst (5m structure broke); 15:40 analyst (trade on track); 15:45 analyst (5m structure broke); 15:59 exit
- **my_ema_cross_4h** XAUUSD LONG e4d32e5d → pre-news: Federal Funds Rate (-0.20R, best 0.06R): 09:00 entry (3982.757); 09:00 analyst (trade on track); 09:35 analyst (5m structure broke); 09:50 analyst (trade on track); 10:05 analyst (stalled: no new best for 60 min and under +0.5R); 10:15 analyst (15m trend flipped against the trade; stalled: no); 13:55 exit
- **my_ema_cross_4h** US30 LONG dd479e2f → OPEN (R, best 0.00R): 17:00 entry (52189.600000000006)
- **my_ema_rsi_15m** US30 LONG c94efac9 → OPEN (R, best 0.00R): 15:30 entry (52692.4)
- **my_ema_rsi_15m** NDQ LONG edeb373f → close_past_ema21 (-0.47R, best 0.06R): 06:00 entry (29747.600000000002); 06:00 analyst (trade on track); 06:15 exit_signal; 06:15 exit
- **my_ema_rsi_15m** XAUUSD LONG cca066e1 → close_past_ema21 (-0.30R, best 0.65R): 08:15 entry (4041.869); 08:15 analyst (trade on track); 09:25 analyst (stalled: no new best for 60 min and under +0.5R); 09:35 analyst (5m structure broke; stalled: no new best for 60 ); 10:00 exit_signal; 10:00 exit
- **my_ema_rsi_15m** NDQ SHORT 52de5818 → stop (-1.00R, best 0.42R): 12:00 entry (29750.5); 12:00 analyst (1H trend is against the trade); 12:55 exit
- **my_ema_rsi_15m** US30 SHORT d12ce22e → close_past_ema21 (-0.36R, best 0.23R): 15:15 entry (52668.0); 15:15 analyst (1H trend is against the trade); 15:30 analyst (15m trend flipped against the trade; 1H trend is); 15:45 exit_signal; 15:45 exit
- **my_ema_rsi_15m** US30 LONG 2a3ee83e → close_past_ema21 (-0.58R, best 0.16R): 19:15 entry (52496.9); 19:15 analyst (trade on track); 19:40 analyst (5m structure broke); 19:45 exit_signal; 19:45 exit
- **my_ema_rsi_15m** US30 LONG 7d727584 → OPEN (R, best 1.87R): 20:15 entry (52492.4); 20:15 analyst (trade on track); 21:15 agent_check (continuation 0.46 ≥ 0.45); 21:15 stop_moved (breakeven / 2×ATR trail after +1R); 21:30 agent_check (continuation 0.46 ≥ 0.45); 21:45 agent_check (continuation 0.46 ≥ 0.45); 22:00 agent_check (continuation 0.49 ≥ 0.45); 22:00 stop_moved (breakeven / 2×ATR trail after +1R); 22:15 agent_check (continuation 0.47 ≥ 0.45); 22:15 stop_moved (breakeven / 2×ATR trail after +1R); 22:30 agent_check (continuation 0.47 ≥ 0.45); 22:30 stop_moved (breakeven / 2×ATR trail after +1R); 22:45 partial (Jev: continuation 0.44 < 0.45); 22:45 stop_moved (breakeven / 2×ATR trail after +1R)
- **my_ema_rsi_15m** XAUUSD SHORT 0fcb2a23 → close_past_ema21 (-0.64R, best 0.31R): 20:30 entry (4060.762); 20:30 analyst (1H trend is against the trade); 21:00 analyst (trade on track); 21:15 exit_signal; 21:15 exit
- **my_ema_rsi_15m** XAUUSD LONG 74a3c3e0 → close_past_ema21 (-0.36R, best 0.07R): 22:00 entry (4033.587); 22:00 analyst (trade on track); 22:15 exit_signal; 22:15 exit
- **my_ema_rsi_1d** US30 LONG 4e7ae8d4 → OPEN (R, best 0.00R): 17:00 entry (51704.3)
- **my_ema_rsi_1h** US30 LONG 216b658a → OPEN (R, best 0.00R): 12:00 entry (52439.4)
- **my_ema_rsi_1h** US30 SHORT 2704ca3a → close_past_ema21 (-0.67R, best 0.16R): 22:00 entry (52523.0); 22:00 analyst (trade on track); 22:40 analyst (5m structure broke); 23:10 analyst (5m structure broke; stalled: no new best for 60 ); 02:25 analyst (trade on track); 03:10 analyst (5m structure broke); 03:30 analyst (trade on track); 03:40 analyst (stalled: no new best for 60 min and under +0.5R); 06:00 analyst (15m trend flipped against the trade; 5m structur); 09:00 exit_signal; 09:00 exit
- **my_ema_rsi_1h** XAUUSD LONG e1c9c2d6 → close_past_ema21 (-0.42R, best 0.25R): 05:00 entry (4025.446); 05:00 analyst (trade on track); 06:10 analyst (5m structure broke); 06:25 analyst (5m structure broke; stalled: no new best for 60 ); 07:00 analyst (15m trend flipped against the trade; stalled: no); 08:20 analyst (trade on track); 09:25 analyst (stalled: no new best for 60 min and under +0.5R); 11:00 exit_signal; 11:00 exit
- **my_ema_rsi_1h** NDQ LONG be6b6d0a → pre-news: Federal Funds Rate (-0.15R, best 0.04R): 13:00 entry (29614.2); 13:00 analyst (trade on track); 13:15 analyst (15m trend flipped against the trade); 13:30 analyst (5m structure broke); 13:35 analyst (trade on track); 13:40 analyst (high-impact news within 20 min); 13:55 exit
- **my_ema_rsi_1h** XAUUSD SHORT 876a89d0 → stop (-1.00R, best 0.15R): 15:00 entry (4070.9010000000003); 15:00 analyst (trade on track); 15:15 analyst (15m trend flipped against the trade); 15:30 analyst (5m structure broke); 15:40 analyst (trade on track); 15:45 analyst (5m structure broke); 15:59 exit
- **my_ema_rsi_1h** US30 LONG ee5142d6 → OPEN (R, best 0.00R): 16:00 entry (52252.700000000004)
- **my_ema_rsi_1h** XAUUSD LONG 42926942 → close_past_ema21 (-0.36R, best 0.05R): 22:00 entry (4020.397); 22:00 analyst (trade on track); 22:30 analyst (15m trend flipped against the trade; 5m structur); 22:55 analyst (trade on track); 23:00 exit_signal; 23:00 exit
- **my_ema_rsi_4h** US30 LONG c0daa33b → OPEN (R, best 1.69R): 09:00 entry (52365.4); 09:00 analyst (trade on track); 10:25 analyst (5m structure broke; gave back half of a ≥1R open); 10:30 analyst (15m trend flipped against the trade; 5m structur); 10:55 analyst (gave back half of a ≥1R open profit); 11:00 analyst (stalled: no new best for 60 min and under +0.5R;); 11:20 analyst (trade on track); 13:00 agent_check (continuation 0.48 ≥ 0.45); 13:00 stop_moved (breakeven / 2×ATR trail after +1R)
- **my_ema_rsi_4h** XAUUSD LONG 6a42dbd0 → close_past_ema21 (-0.57R, best 0.01R): 17:00 entry (4013.6890000000003); 17:00 analyst (trade on track); 17:00 readopted (app restarted; position restored from the shadow); 18:05 analyst (stalled: no new best for 60 min and under +0.5R); 18:10 analyst (trade on track); 18:30 analyst (5m structure broke); 20:15 analyst (15m trend flipped against the trade; 5m structur); 21:00 exit_signal; 21:00 exit
- **my_rsi_15m** XAUUSD SHORT d5f69550 → OPEN (R, best 1.14R): 11:15 entry (4084.205); 11:15 analyst (trade on track); 13:00 agent_check (continuation 0.47 ≥ 0.45); 14:00 analyst (stalled: no new best for 60 min and under +0.5R); 14:10 analyst (trade on track); 14:15 partial (Jev: continuation 0.40 < 0.45); 14:20 analyst (stalled: no new best for 60 min and under +0.5R); 14:25 analyst (trade on track); 14:30 partial (Jev: continuation 0.43 < 0.45); 15:45 stop_moved (breakeven / 2×ATR trail after +1R); 16:00 stop_moved (breakeven / 2×ATR trail after +1R); 16:15 stop_moved (breakeven / 2×ATR trail after +1R); 16:30 stop_moved (breakeven / 2×ATR trail after +1R); 16:45 stop_moved (breakeven / 2×ATR trail after +1R)
- **my_rsi_15m** US30 LONG fcd1d2ed → OPEN (R, best 0.00R): 16:00 entry (52692.5)
- **my_rsi_15m** NDQ SHORT 9971e243 → OPEN (R, best 0.00R): 16:45 entry (29085.600000000002)
- **my_rsi_1h** US30 LONG af640ece → OPEN (R, best 0.00R): 16:00 entry (52495.4)
- **my_rsi_4h** US30 LONG 3750c941 → OPEN (R, best 0.00R): 13:00 entry (52361.9)
- **playbook_regime** US30 LONG 05bac06e → OPEN (R, best 0.00R): 20:30 entry (52437.6)
- **shadow** NDQ SHORT ebcda2f4 → OPEN (R, best 0.00R): 22:15 entry (29647.7)
- **shadow** US30 LONG 4dfb39be → OPEN (R, best 0.00R): 20:30 entry (52437.6)

## 7. Entry reasons of every trade

- ema21_rsi55 92a06f11 US30 SHORT: EMA21+RSI45 short: 15m close 52291.70 < EMA21 52312.67, RSI 44.4
- ema21_rsi55 6af0aef8 XAUUSD LONG: EMA21+RSI55: 15m close 4052.65 > EMA21 4047.39, RSI 57.9
- ema21_rsi55 dc93b775 XAUUSD SHORT: EMA21+RSI45 short: 15m close 4033.16 < EMA21 4041.94, RSI 42.4
- ema21_rsi55 5f3cc758 XAUUSD LONG: EMA21+RSI55: 15m close 4051.62 > EMA21 4042.82, RSI 55.5
- live 878bf5b0 NDQ SHORT: Resistance rejection @ 29706.10
- my_ema_cross_15m d83bc33d XAUUSD SHORT: my_ema_cross_15m: 15min close 4044.66 < EMA21 4053.31, RSI 44.2, CHOP 43, Supertrend up
- my_ema_cross_15m 35371060 XAUUSD LONG: my_ema_cross_15m: 15min close 4055.74 > EMA21 4052.03, RSI 52.4, CHOP 49, Supertrend up
- my_ema_cross_15m 758f2ac8 XAUUSD SHORT: my_ema_cross_15m: 15min close 4043.28 < EMA21 4051.49, RSI 45.1, CHOP 56, Supertrend up
- my_ema_cross_1h 1311e5cd US30 LONG: my_ema_cross_1h: 1h close 52686.60 > EMA21 52651.37, RSI 52.4, CHOP 57, Supertrend up
- my_ema_cross_1h 9c681328 US30 LONG: my_ema_cross_1h: 1h close 52480.80 > EMA21 52383.58, RSI 58.4, CHOP 52, Supertrend down
- my_ema_cross_1h f990a79c XAUUSD SHORT: my_ema_cross_1h: 1h close 4033.16 < EMA21 4042.80, RSI 43.5, CHOP 54, Supertrend down
- my_ema_cross_4h f1537166 NDQ SHORT: my_ema_cross_4h: 4h close 29638.90 < EMA21 29715.93, RSI 45.9, CHOP 55, Supertrend down
- my_ema_cross_4h 74f738ac NDQ LONG: my_ema_cross_4h: 4h close 29462.50 > EMA21 29278.06, RSI 55.5, CHOP 59, Supertrend down
- my_ema_cross_4h e4d32e5d XAUUSD LONG: my_ema_cross_4h: 4h close 4053.41 > EMA21 4041.62, RSI 52.0, CHOP 53, Supertrend down
- my_ema_cross_4h dd479e2f US30 LONG: my_ema_cross_4h: 4h close 52614.60 > EMA21 52460.36, RSI 57.5, CHOP 62, Supertrend up
- my_ema_rsi_15m c94efac9 US30 LONG: my_ema_rsi_15m: 15min close 52851.00 > EMA21 52781.32, RSI 57.8, CHOP 59, Supertrend up
- my_ema_rsi_15m f94b2d73 NDQ LONG: my_ema_rsi_15m: 15min close 29663.60 > EMA21 29645.55, RSI 56.3, CHOP 50, Supertrend up
- my_ema_rsi_15m 46a11632 US30 SHORT: my_ema_rsi_15m: 15min close 52336.70 < EMA21 52367.39, RSI 42.8, CHOP 41, Supertrend down
- my_ema_rsi_15m edeb373f NDQ LONG: my_ema_rsi_15m: 15min close 29815.10 > EMA21 29795.11, RSI 56.1, CHOP 62, Supertrend up
- my_ema_rsi_15m cca066e1 XAUUSD LONG: my_ema_rsi_15m: 15min close 4052.65 > EMA21 4047.39, RSI 57.9, CHOP 56, Supertrend up
- my_ema_rsi_15m fcd306e4 NDQ SHORT: my_ema_rsi_15m: 15min close 29743.40 < EMA21 29789.37, RSI 41.5, CHOP 60, Supertrend down
- my_ema_rsi_15m 0f879900 XAUUSD SHORT: my_ema_rsi_15m: 15min close 4043.49 < EMA21 4047.00, RSI 43.7, CHOP 45, Supertrend down
- my_ema_rsi_15m 52de5818 NDQ SHORT: my_ema_rsi_15m: 15min close 29712.80 < EMA21 29740.75, RSI 43.7, CHOP 54, Supertrend down
- my_ema_rsi_15m 42dec4c9 XAUUSD LONG: my_ema_rsi_15m: 15min close 4051.62 > EMA21 4042.82, RSI 55.5, CHOP 51, Supertrend up
- my_ema_rsi_15m d12ce22e US30 SHORT: my_ema_rsi_15m: 15min close 52436.60 < EMA21 52498.99, RSI 44.0, CHOP 54, Supertrend up
- my_ema_rsi_15m 0a1a3ce4 NDQ LONG: my_ema_rsi_15m: 15min close 29783.00 > EMA21 29742.32, RSI 55.4, CHOP 61, Supertrend down
- my_ema_rsi_15m 01f8ad26 US30 LONG: my_ema_rsi_15m: 15min close 52568.60 > EMA21 52505.07, RSI 58.0, CHOP 58, Supertrend up
- my_ema_rsi_15m 2a3ee83e US30 LONG: my_ema_rsi_15m: 15min close 52586.60 > EMA21 52551.03, RSI 56.4, CHOP 41, Supertrend up
- my_ema_rsi_15m 7d727584 US30 LONG: my_ema_rsi_15m: 15min close 52590.60 > EMA21 52557.42, RSI 56.0, CHOP 42, Supertrend up
- my_ema_rsi_15m 0fcb2a23 XAUUSD SHORT: my_ema_rsi_15m: 15min close 4042.37 < EMA21 4052.31, RSI 42.7, CHOP 36, Supertrend up
- my_ema_rsi_15m 74a3c3e0 XAUUSD LONG: my_ema_rsi_15m: 15min close 4062.53 > EMA21 4052.99, RSI 56.0, CHOP 51, Supertrend up
- my_ema_rsi_1d 4e7ae8d4 US30 LONG: my_ema_rsi_1d: 1D close 52614.60 > EMA21 52186.56, RSI 56.8, CHOP 59, Supertrend up
- my_ema_rsi_1h c33f7974 US30 LONG: my_ema_rsi_1h: 1h close 52681.60 > EMA21 52537.68, RSI 58.9, CHOP 56, Supertrend up
- my_ema_rsi_1h 216b658a US30 LONG: my_ema_rsi_1h: 1h close 52863.60 > EMA21 52670.66, RSI 59.9, CHOP 57, Supertrend up
- my_ema_rsi_1h 0636d104 NDQ LONG: my_ema_rsi_1h: 1h close 29341.60 > EMA21 29257.28, RSI 57.1, CHOP 52, Supertrend up
- my_ema_rsi_1h 2704ca3a US30 SHORT: my_ema_rsi_1h: 1h close 52284.70 < EMA21 52420.17, RSI 39.4, CHOP 55, Supertrend down
- my_ema_rsi_1h e1c9c2d6 XAUUSD LONG: my_ema_rsi_1h: 1h close 4052.97 > EMA21 4041.68, RSI 59.0, CHOP 41, Supertrend down
- my_ema_rsi_1h be6b6d0a NDQ LONG: my_ema_rsi_1h: 1h close 29753.30 > EMA21 29712.37, RSI 57.7, CHOP 61, Supertrend up
- my_ema_rsi_1h 876a89d0 XAUUSD SHORT: my_ema_rsi_1h: 1h close 4033.16 < EMA21 4042.80, RSI 43.5, CHOP 54, Supertrend down
- my_ema_rsi_1h ee5142d6 US30 LONG: my_ema_rsi_1h: 1h close 52568.60 > EMA21 52444.84, RSI 59.9, CHOP 53, Supertrend up
- my_ema_rsi_1h 42926942 XAUUSD LONG: my_ema_rsi_1h: 1h close 4062.53 > EMA21 4048.96, RSI 56.1, CHOP 58, Supertrend up
- my_ema_rsi_4h 632887d2 NDQ SHORT: my_ema_rsi_4h: 4h close 29465.60 < EMA21 29693.18, RSI 41.1, CHOP 56, Supertrend down
- my_ema_rsi_4h c0daa33b US30 LONG: my_ema_rsi_4h: 4h close 52587.00 > EMA21 52452.03, RSI 56.2, CHOP 46, Supertrend up
- my_ema_rsi_4h 6bc1d4a3 NDQ LONG: my_ema_rsi_4h: 4h close 29462.50 > EMA21 29278.06, RSI 55.5, CHOP 59, Supertrend down
- my_ema_rsi_4h 6a42dbd0 XAUUSD LONG: my_ema_rsi_4h: 4h close 4067.29 > EMA21 4044.02, RSI 55.6, CHOP 53, Supertrend down
- my_intraday_mom f4187774 NDQ LONG: my_intraday_mom: first half-hour +0.152% (16:00 close 29678.80 -> 10:00 29723.80) -> long 15:30-16:00
- my_intraday_mom bdfd7a1d US30 LONG: my_intraday_mom: first half-hour +0.100% (16:00 close 52425.20 -> 10:00 52477.80) -> long 15:30-16:00
- my_rsi_15m d5f69550 XAUUSD SHORT: my_rsi_15m: 15min close 4055.01 < EMA21 4068.51, RSI 38.3, CHOP 49, Supertrend down
- my_rsi_15m fcd1d2ed US30 LONG: my_rsi_15m: 15min close 52911.00 > EMA21 52798.62, RSI 62.1, CHOP 61, Supertrend up
- my_rsi_15m 9971e243 NDQ SHORT: my_rsi_15m: 15min close 28968.60 < EMA21 29041.31, RSI 38.9, CHOP 59, Supertrend down
- my_rsi_15m 2cc2354d NDQ LONG: my_rsi_15m: 15min close 29693.60 > EMA21 29652.03, RSI 60.4, CHOP 51, Supertrend up
- my_rsi_15m f540ce43 NDQ LONG: my_rsi_15m: 15min close 29795.60 > EMA21 29753.03, RSI 63.2, CHOP 46, Supertrend up
- my_rsi_1h af640ece US30 LONG: my_rsi_1h: 1h close 52911.00 > EMA21 52722.60, RSI 60.6, CHOP 58, Supertrend up
- my_rsi_4h 3750c941 US30 LONG: my_rsi_4h: 4h close 52841.00 > EMA21 52487.40, RSI 61.9, CHOP 49, Supertrend up
- playbook_regime 05bac06e US30 LONG: DTFX close_fib BOS → 50-70% zone rejection · playbook level=50-70/trend p=0.47
- shadow ebcda2f4 NDQ SHORT: DTFX wick_fib BOS → 50-70% zone rejection · playbook level=50-70/std p=0.55
- shadow 4dfb39be US30 LONG: DTFX close_fib BOS → 50-70% zone rejection · playbook level=50-70/trend p=0.47
- shadow 8ad91af1 XAUUSD SHORT: Sweep → MSS (displacement CHoCH) · playbook default/std p=0.57
- shadow 2fddf60b XAUUSD SHORT: Sweep → MSS (displacement CHoCH) · playbook disp_k=0.8/std p=0.58
