# RSI / EMA books report

Generated 2026-10-30 22:40 New York. Window: since 2026-10-30 00:00 (23 h). R = profit as a multiple of the risk at the first stop.

Books read: live, c10_afternoon, daily_rsi2_adx2, ema21_rsi55, h1_vol_trend, my_ema_cross_15m, my_ema_cross_1d, my_ema_cross_1h, my_ema_cross_4h, my_ema_rsi_15m, my_ema_rsi_1d, my_ema_rsi_1h, my_ema_rsi_4h, my_intraday_mom, my_rsi_15m, my_rsi_1h, my_rsi_4h, playbook_allhours, playbook_nobias, playbook_regime, shadow

## 1. Per book

| Book | Trades | Closed | Open | Wins | Total R | P&L | Avg best R | Avg hours held | Jev partials |
|---|---|---|---|---|---|---|---|---|---|
| live | 1 | 1 | 0 | 1 | +2.00 | +351.20 | 2.95 | 2.6 | 0 |
| c10_afternoon | 1 | 1 | 0 | 1 | +1.93 | +134.05 | 1.77 | 1.3 | 0 |
| daily_rsi2_adx2 | 0 | 0 | 0 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 0 |
| ema21_rsi55 | 2 | 2 | 0 | 1 | +4.22 | +291.17 | 2.88 | 6.3 | 0 |
| h1_vol_trend | 1 | 1 | 0 | 1 | +2.38 | +164.48 | 2.55 | 6.8 | 0 |
| my_ema_cross_15m | 0 | 0 | 0 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 0 |
| my_ema_cross_1d | 0 | 0 | 0 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 0 |
| my_ema_cross_1h | 0 | 0 | 0 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 0 |
| my_ema_cross_4h | 1 | 0 | 1 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 1 |
| my_ema_rsi_15m | 4 | 4 | 0 | 3 | +2.02 | +710.62 | 2.17 | 2.8 | 5 |
| my_ema_rsi_1d | 1 | 0 | 1 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 1 |
| my_ema_rsi_1h | 1 | 1 | 0 | 0 | -0.33 | -114.00 | 0.16 | 3.0 | 0 |
| my_ema_rsi_4h | 2 | 0 | 2 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 3 |
| my_intraday_mom | 2 | 2 | 0 | 0 | -1.01 | -354.90 | 0.10 | 0.5 | 0 |
| my_rsi_15m | 0 | 0 | 0 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 0 |
| my_rsi_1h | 0 | 0 | 0 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 0 |
| my_rsi_4h | 1 | 0 | 1 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 2 |
| playbook_allhours | 9 | 9 | 0 | 6 | +4.01 | +1287.10 | 1.60 | 2.1 | 6 |
| playbook_nobias | 6 | 6 | 0 | 5 | +5.54 | +1619.42 | 2.29 | 1.8 | 5 |
| playbook_regime | 3 | 3 | 0 | 2 | +2.60 | +905.70 | 2.75 | 1.4 | 2 |
| shadow | 1 | 1 | 0 | 1 | +1.04 | +365.76 | 1.13 | 4.0 | 1 |

All listed books: 31 closed trades, +24.42 R.

## 2. Why the losing trades lost

| Cause | Trades | R |
|---|---|---|
| stopped at the first stop | 6 | -5.01 |
| gave back: was +0.5R or better first | 2 | -1.26 |
| closed on the EMA exit at a loss | 2 | -1.04 |

## 3. Skipped signals (what the filters blocked)

**live**: 4x filtered: counter to BEARISH bias; 4x filtered: counter to BULLISH bias; 3x skipped: Jev confidence # < #; 1x skipped: Jev quality # < # and confidence # < #; 1x taken: qty #
**c10_afternoon**: 1x taken: qty #
**ema21_rsi55**: 2x taken: qty #, jev #
**h1_vol_trend**: 1x taken: qty #, risk $#
**my_ema_rsi_15m**: 4x taken: qty #, jev #; 2x rejected: not a fresh cross (the price has been below the EMA# for # candles, limit #; 1x rejected: choppy market (CHOP # ≥ #)
**my_ema_rsi_1h**: 1x taken: qty #, jev #; 1x rejected: not a fresh cross (the price has been below the EMA# for # candles, limit #
**my_ema_rsi_4h**: 2x rejected: against the #D trend (bullish) - no sell
**my_intraday_mom**: 2x taken: qty #, jev None
**my_rsi_1h**: 1x rejected: not a fresh cross (the price has been below the EMA# for # candles, limit #
**playbook_allhours**: 12x filtered: counter to BEARISH bias; 9x taken: qty #, risk $#, cost #R; 8x skipped: playbook: XAUUSD already has # position(s); 4x filtered: bias neutral (#); 4x filtered: counter to BULLISH bias; 3x skipped: Jev confidence # < #; 3x skipped: a higher-expectancy playbook cell fired on this bar; 1x skipped: playbook: NDQ already has # position(s)
**playbook_nobias**: 14x skipped: Jev quality # < #; 7x rejected: outside entry windows; 6x skipped: Jev confidence # < #; 6x taken: qty #, risk $#, cost #R; 6x skipped: playbook: XAUUSD already has # position(s); 5x skipped: playbook: XAUUSD has an opposite position (OANDA nets positions per instrum; 2x skipped: playbook: NDQ already has # position(s); 1x skipped: playbook: one index position per direction at a time
**playbook_regime**: 12x skipped: regime chop (Jev chop #, CHOP #): scalps only; 12x filtered: counter to BEARISH bias; 6x rejected: outside entry windows; 4x filtered: bias neutral (#); 4x filtered: counter to BULLISH bias; 3x taken: qty #, risk $#, cost #R; 3x skipped: playbook: XAUUSD already has # position(s); 2x skipped: Jev confidence # < #
**shadow**: 31x filtered: bias suspended; 4x filtered: bias neutral (#); 4x filtered: counter to BULLISH bias; 3x rejected: outside entry windows; 2x skipped: Jev confidence # < #; 1x taken: qty #, risk $#, cost #R; 1x filtered: counter to BEARISH bias; 1x skipped: playbook: NDQ already has # position(s)

## 4. Trade analyst (shadow) - how its advice scored

| Book | Check | Times | Avg value in R (positive = its advice would have helped) | Helpful |
|---|---|---|---|---|
| live | any_exit | 10 | +0.16 | 7 |
| live | giveback | 5 | -0.10 | 3 |
| live | h1_against | 5 | -0.22 | 2 |
| live | stall | 3 | -0.19 | 1 |
| live | structure_break | 8 | +0.30 | 6 |
| live | trend_flip | 6 | +0.24 | 5 |
| c10_afternoon | any_exit | 3 | -0.43 | 0 |
| c10_afternoon | giveback | 1 | -1.33 | 0 |
| c10_afternoon | stall | 2 | -0.47 | 0 |
| c10_afternoon | structure_break | 3 | -0.52 | 0 |
| ema21_rsi55 | any_exit | 12 | -0.08 | 8 |
| ema21_rsi55 | giveback | 2 | +0.23 | 1 |
| ema21_rsi55 | h1_against | 10 | -0.20 | 6 |
| ema21_rsi55 | news_soon | 1 | +0.34 | 1 |
| ema21_rsi55 | stall | 9 | -0.19 | 6 |
| ema21_rsi55 | structure_break | 11 | +0.08 | 6 |
| h1_vol_trend | any_exit | 1 | -0.90 | 0 |
| h1_vol_trend | stall | 1 | -0.96 | 0 |
| h1_vol_trend | structure_break | 1 | -0.90 | 0 |
| my_ema_cross_15m | any_exit | 12 | +0.06 | 9 |
| my_ema_cross_15m | giveback | 2 | +0.19 | 2 |
| my_ema_cross_15m | h1_against | 16 | -0.05 | 10 |
| my_ema_cross_15m | stall | 5 | -0.07 | 2 |
| my_ema_cross_15m | structure_break | 12 | +0.09 | 9 |
| my_ema_cross_15m | trend_flip | 3 | -0.09 | 1 |
| my_ema_cross_1h | any_exit | 14 | +0.26 | 12 |
| my_ema_cross_1h | giveback | 1 | +0.12 | 1 |
| my_ema_cross_1h | h1_against | 5 | +0.50 | 5 |
| my_ema_cross_1h | news_soon | 1 | +0.16 | 1 |
| my_ema_cross_1h | stall | 9 | +0.36 | 9 |
| my_ema_cross_1h | structure_break | 14 | +0.23 | 11 |
| my_ema_cross_1h | trend_flip | 10 | +0.25 | 10 |
| my_ema_cross_4h | any_exit | 4 | +0.04 | 2 |
| my_ema_cross_4h | h1_against | 1 | +0.30 | 1 |
| my_ema_cross_4h | news_soon | 4 | +0.04 | 1 |
| my_ema_cross_4h | stall | 4 | +0.09 | 2 |
| my_ema_cross_4h | structure_break | 4 | +0.04 | 2 |
| my_ema_cross_4h | trend_flip | 3 | +0.37 | 3 |
| my_ema_rsi_15m | any_exit | 40 | -0.02 | 23 |
| my_ema_rsi_15m | giveback | 13 | +0.04 | 11 |
| my_ema_rsi_15m | h1_against | 33 | +0.09 | 20 |
| my_ema_rsi_15m | news_soon | 1 | +0.11 | 1 |
| my_ema_rsi_15m | stall | 17 | -0.01 | 9 |
| my_ema_rsi_15m | structure_break | 36 | -0.01 | 18 |
| my_ema_rsi_15m | trend_flip | 9 | +0.15 | 7 |
| my_ema_rsi_1d | any_exit | 1 | +0.19 | 1 |
| my_ema_rsi_1d | h1_against | 1 | +0.14 | 1 |
| my_ema_rsi_1d | news_soon | 1 | -0.04 | 0 |
| my_ema_rsi_1d | stall | 1 | +0.20 | 1 |
| my_ema_rsi_1d | structure_break | 1 | +0.19 | 1 |
| my_ema_rsi_1d | trend_flip | 1 | +0.30 | 1 |
| my_ema_rsi_1h | any_exit | 24 | +0.16 | 17 |
| my_ema_rsi_1h | giveback | 1 | +0.07 | 1 |
| my_ema_rsi_1h | h1_against | 4 | +0.39 | 4 |
| my_ema_rsi_1h | news_soon | 1 | -0.20 | 0 |
| my_ema_rsi_1h | stall | 16 | +0.23 | 12 |
| my_ema_rsi_1h | structure_break | 24 | +0.13 | 17 |
| my_ema_rsi_1h | trend_flip | 21 | +0.09 | 14 |
| my_ema_rsi_4h | any_exit | 4 | +0.26 | 3 |
| my_ema_rsi_4h | giveback | 1 | +0.43 | 1 |
| my_ema_rsi_4h | h1_against | 1 | +0.12 | 1 |
| my_ema_rsi_4h | news_soon | 1 | +0.28 | 1 |
| my_ema_rsi_4h | stall | 4 | +0.31 | 3 |
| my_ema_rsi_4h | structure_break | 4 | +0.14 | 2 |
| my_ema_rsi_4h | trend_flip | 4 | +0.23 | 4 |
| my_intraday_mom | any_exit | 10 | +0.13 | 6 |
| my_intraday_mom | h1_against | 3 | +0.07 | 2 |
| my_intraday_mom | structure_break | 10 | +0.13 | 6 |
| my_rsi_15m | any_exit | 7 | -0.07 | 4 |
| my_rsi_15m | giveback | 3 | -0.02 | 2 |
| my_rsi_15m | stall | 4 | -0.05 | 2 |
| my_rsi_15m | structure_break | 7 | -0.04 | 4 |
| my_rsi_1h | any_exit | 4 | +0.03 | 3 |
| my_rsi_1h | giveback | 1 | +0.29 | 1 |
| my_rsi_1h | stall | 3 | -0.10 | 2 |
| my_rsi_1h | structure_break | 4 | +0.03 | 3 |
| my_rsi_1h | trend_flip | 4 | -0.10 | 3 |
| my_rsi_4h | any_exit | 1 | +0.67 | 1 |
| my_rsi_4h | h1_against | 1 | +0.34 | 1 |
| my_rsi_4h | stall | 1 | +0.70 | 1 |
| my_rsi_4h | structure_break | 1 | +0.67 | 1 |
| my_rsi_4h | trend_flip | 1 | +0.64 | 1 |
| playbook_allhours | any_exit | 3 | +0.04 | 2 |
| playbook_allhours | h1_against | 1 | +0.86 | 1 |
| playbook_allhours | stall | 2 | -0.17 | 1 |
| playbook_allhours | structure_break | 3 | +0.04 | 2 |
| playbook_allhours | trend_flip | 1 | +0.47 | 1 |
| playbook_nobias | any_exit | 1 | -1.25 | 0 |
| playbook_nobias | giveback | 2 | -0.46 | 1 |
| playbook_nobias | stall | 1 | -0.97 | 0 |
| playbook_nobias | structure_break | 1 | -1.25 | 0 |
| playbook_regime | any_exit | 2 | -0.02 | 1 |
| playbook_regime | giveback | 4 | -0.35 | 2 |
| playbook_regime | stall | 1 | -0.19 | 0 |
| playbook_regime | structure_break | 2 | -0.02 | 1 |
| shadow | any_exit | 23 | +0.07 | 14 |
| shadow | giveback | 7 | +0.05 | 6 |
| shadow | h1_against | 8 | -0.10 | 3 |
| shadow | stall | 14 | +0.06 | 8 |
| shadow | structure_break | 21 | +0.05 | 13 |
| shadow | trend_flip | 5 | +0.27 | 5 |

## 5. Every trade in the window

| Book | Id | Market | Side | Opened (NY) | Closed (NY) | Entry | Exit | First stop | Stop at end | Qty | P&L | R | Best R | Worst R | How it ended |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| c10_afternoon | 1142945a | NDQ | SHORT | 10-30 13:00 | 10-30 14:18 | 28401.40 | 28212.60 | 28499.20 | 28499.20 | 0.71 | 134.05 | 1.93 | 1.77 | -0.14 | target |
| ema21_rsi55 | d925f0de | XAUUSD | SHORT | 10-30 02:00 | 10-30 05:00 | 3991.22 | 3997.59 | 4015.78 | 4015.78 | 2.80 | -17.82 | -0.26 | 1.06 | -0.33 | close_above_ema21 |
| ema21_rsi55 | 6b559030 | XAUUSD | SHORT | 10-30 06:15 | 10-30 15:50 | 3982.36 | 3875.82 | 4006.15 | 4006.15 | 2.90 | 308.99 | 4.48 | 4.71 | -0.19 | session_flat |
| h1_vol_trend | de2fdaa1 | XAUUSD | SHORT | 10-30 09:00 | 10-30 15:50 | 3954.14 | 3875.82 | 3987.02 | 3916.17 | 2.10 | 164.48 | 2.38 | 2.55 | -0.05 | session_flat |
| live | 74ae19f3 | NDQ | SHORT | 10-30 13:00 | 10-30 15:36 | 28401.10 | 28204.90 | 28499.20 | 28499.20 | 1.79 | 351.20 | 2.00 | 2.95 | -0.11 | stop |
| my_ema_cross_4h | 59f05cdd | NDQ | SHORT | 10-29 17:00 | open | 29086.80 |  | 29795.40 | 28611.80 | 0.49 | 95.86 |  | 1.38 | -0.01 | OPEN |
| my_ema_rsi_15m | 928f03d6 | XAUUSD | SHORT | 10-30 02:00 | 10-30 04:03 | 3991.22 | 3981.71 | 4013.68 | 3981.71 | 15.60 | 197.09 | 0.56 | 1.16 | -0.13 | stop |
| my_ema_rsi_15m | e933b036 | NDQ | SHORT | 10-30 02:00 | 10-30 02:30 | 28850.00 | 28903.40 | 28925.00 | 28925.00 | 4.68 | -249.91 | -0.71 | 0.33 | -0.75 | close_past_ema21 |
| my_ema_rsi_15m | 21dacf55 | NDQ | SHORT | 10-30 05:30 | 10-30 09:48 | 28788.40 | 28646.80 | 28891.00 | 28646.80 | 3.42 | 271.81 | 0.78 | 2.43 | -0.21 | stop |
| my_ema_rsi_15m | 0584f536 | XAUUSD | SHORT | 10-30 06:15 | 10-30 10:41 | 3982.36 | 3914.01 | 4001.37 | 3914.01 | 18.50 | 491.63 | 1.40 | 4.77 | -0.24 | stop |
| my_ema_rsi_1d | 039ebc8c | NDQ | SHORT | 10-29 17:00 | open | 29086.80 |  | 30180.10 | 30180.10 | 0.32 | 108.16 |  | 0.89 | -0.01 | OPEN |
| my_ema_rsi_1h | 46f6a31a | US30 | LONG | 10-30 05:00 | 10-30 08:00 | 52475.70 | 52375.70 | 52169.40 | 52169.40 | 1.14 | -114.00 | -0.33 | 0.16 | -0.44 | close_past_ema21 |
| my_ema_rsi_4h | 4fe39add | XAUUSD | SHORT | 10-29 09:00 | open | 4020.48 |  | 4089.85 | 3934.47 | 5.00 | 164.30 |  | 2.16 | -0.25 | OPEN |
| my_ema_rsi_4h | a24a45d7 | NDQ | SHORT | 10-29 17:00 | open | 29086.80 |  | 29795.40 | 28611.80 | 0.49 | 176.98 |  | 1.38 | -0.01 | OPEN |
| my_intraday_mom | 7c0b4a39 | NDQ | SHORT | 10-30 15:30 | 10-30 16:00 | 28268.60 | 28408.60 | 28511.80 | 28511.80 | 1.44 | -201.60 | -0.58 | 0.12 | -0.75 | session_close |
| my_intraday_mom | e4cdb439 | US30 | SHORT | 10-30 15:30 | 10-30 16:00 | 51674.50 | 51779.50 | 51914.90 | 51914.90 | 1.46 | -153.30 | -0.44 | 0.09 | -0.63 | session_close |
| my_rsi_4h | 446c4319 | NDQ | SHORT | 10-29 17:00 | open | 29086.80 |  | 29795.40 | 28611.80 | 0.49 | 177.82 |  | 1.38 | -0.01 | OPEN |
| playbook_allhours | a7bf6fe7 | XAUUSD | SHORT | 10-30 00:45 | 10-30 01:27 | 3990.92 | 4004.72 | 4004.72 | 4004.72 | 20.00 | -276.08 | -1.00 | 0.02 | -0.87 | stop |
| playbook_allhours | 7c5a6513 | XAUUSD | SHORT | 10-30 02:05 | 10-30 04:04 | 3988.34 | 3986.38 | 4007.96 | 3986.38 | 17.80 | 199.07 | 0.57 | 1.18 | -0.29 | breakeven_plus_stop |
| playbook_allhours | 4c64eb28 | XAUUSD | SHORT | 10-30 02:45 | 10-30 04:02 | 3986.39 | 3977.49 | 3994.47 | 3977.49 | 19.90 | 219.13 | 1.36 | 2.62 | -0.24 | trail_stop |
| playbook_allhours | be6f5df6 | NDQ | SHORT | 10-30 03:50 | 10-30 07:50 | 28795.60 | 28645.00 | 28935.30 | 28781.60 | 2.51 | 365.76 | 1.04 | 1.13 | -0.59 | max_hold |
| playbook_allhours | 98609f78 | XAUUSD | SHORT | 10-30 04:10 | 10-30 04:20 | 3976.66 | 3988.93 | 3988.93 | 3988.93 | 20.10 | -246.51 | -1.00 | 0.08 | -0.96 | stop |
| playbook_allhours | 3ea27ebd | US30 | LONG | 10-30 05:45 | 10-30 08:44 | 52411.20 | 52297.30 | 52297.30 | 52297.30 | 2.78 | -316.64 | -1.00 | 0.57 | -0.92 | stop |
| playbook_allhours | f9decaaa | XAUUSD | SHORT | 10-30 08:15 | 10-30 11:01 | 3960.70 | 3920.39 | 3979.90 | 3920.39 | 18.30 | 551.05 | 1.57 | 3.60 | -0.53 | trail_stop |
| playbook_allhours | d654bc45 | XAUUSD | SHORT | 10-30 08:45 | 10-30 11:01 | 3957.31 | 3921.68 | 3974.28 | 3921.68 | 20.10 | 523.88 | 1.54 | 3.87 | -0.14 | trail_stop |
| playbook_allhours | dbd4db6a | XAUUSD | SHORT | 10-30 13:10 | 10-30 15:50 | 3888.89 | 3875.82 | 3902.62 | 3887.51 | 20.80 | 267.44 | 0.94 | 1.35 | -0.37 | session_flat |
| playbook_nobias | c975c56c | XAUUSD | SHORT | 10-30 02:45 | 10-30 04:02 | 3986.39 | 3977.49 | 3994.47 | 3977.49 | 20.00 | 220.44 | 1.36 | 2.62 | -0.24 | trail_stop |
| playbook_nobias | 513a6130 | XAUUSD | SHORT | 10-30 02:50 | 10-30 04:03 | 3983.75 | 3982.67 | 3994.57 | 3982.67 | 20.00 | 115.92 | 0.54 | 1.72 | -0.42 | breakeven_plus_stop |
| playbook_nobias | d21302c0 | NDQ | SHORT | 10-30 03:50 | 10-30 07:50 | 28795.60 | 28645.00 | 28935.30 | 28781.60 | 2.52 | 367.16 | 1.04 | 1.13 | -0.59 | max_hold |
| playbook_nobias | dfeff454 | XAUUSD | SHORT | 10-30 04:10 | 10-30 04:20 | 3976.66 | 3988.93 | 3988.93 | 3988.93 | 20.10 | -246.51 | -1.00 | 0.08 | -0.96 | stop |
| playbook_nobias | deb2789a | XAUUSD | SHORT | 10-30 08:45 | 10-30 11:01 | 3957.31 | 3921.68 | 3974.28 | 3921.68 | 20.30 | 529.09 | 1.54 | 3.87 | -0.14 | trail_stop |
| playbook_nobias | 01cab92f | XAUUSD | SHORT | 10-30 08:50 | 10-30 10:31 | 3956.38 | 3909.61 | 3971.47 | 3909.61 | 20.30 | 633.32 | 2.07 | 4.29 | -0.13 | trail_stop |
| playbook_regime | 451af5f5 | XAUUSD | SHORT | 10-30 04:10 | 10-30 04:20 | 3976.66 | 3988.93 | 3988.93 | 3988.93 | 20.00 | -245.28 | -1.00 | 0.08 | -0.96 | stop |
| playbook_regime | 28071d8f | XAUUSD | SHORT | 10-30 08:45 | 10-30 11:01 | 3957.31 | 3921.68 | 3974.28 | 3921.68 | 20.10 | 523.88 | 1.54 | 3.87 | -0.14 | trail_stop |
| playbook_regime | 1aa1599d | XAUUSD | SHORT | 10-30 08:50 | 10-30 10:31 | 3956.38 | 3909.61 | 3971.47 | 3909.61 | 20.10 | 627.10 | 2.07 | 4.29 | -0.13 | trail_stop |
| shadow | 7ea35235 | NDQ | SHORT | 10-30 03:50 | 10-30 07:50 | 28795.60 | 28645.00 | 28935.30 | 28781.60 | 2.51 | 365.76 | 1.04 | 1.13 | -0.59 | max_hold |

## 6. Timelines of the losing and the open trades

- **ema21_rsi55** XAUUSD SHORT d925f0de → close_above_ema21 (-0.26R, best 1.06R): 02:00 entry (4015.783); 02:00 analyst (trade on track); 04:05 analyst (gave back half of a ≥1R open profit); 04:10 analyst (trade on track); 04:15 analyst (gave back half of a ≥1R open profit); 04:20 analyst (5m structure broke; gave back half of a ≥1R open); 04:30 analyst (gave back half of a ≥1R open profit); 04:50 analyst (5m structure broke; gave back half of a ≥1R open); 04:55 analyst (5m structure broke; stalled: no new best for 60 ); 05:00 exit_signal; 05:00 exit
- **my_ema_cross_4h** NDQ SHORT 59f05cdd → OPEN (R, best 1.38R): 17:00 entry (29795.4); 17:00 analyst (trade on track); 20:10 analyst (stalled: no new best for 60 min and under +0.5R); 20:45 analyst (trade on track); 22:15 analyst (5m structure broke); 22:20 analyst (trade on track); 22:25 analyst (5m structure broke); 00:07 readopted (app restarted; position restored from the shadow); 01:00 liq_line (no liquidity line beyond 1R: book rules apply); 06:15 analyst (trade on track); 06:25 analyst (stalled: no new best for 60 min and under +0.5R); 06:30 analyst (trade on track); 06:35 analyst (stalled: no new best for 60 min and under +0.5R); 06:45 analyst (trade on track)
- **my_ema_rsi_15m** NDQ SHORT e933b036 → close_past_ema21 (-0.71R, best 0.33R): 02:00 entry (28925.0); 02:00 analyst (trade on track); 02:15 liq_line (liquidity lines fixed at entry); 02:30 exit_signal; 02:30 exit
- **my_ema_rsi_1d** NDQ SHORT 039ebc8c → OPEN (R, best 0.89R): 17:00 entry (30180.100000000002); 17:00 analyst (trade on track); 20:10 analyst (stalled: no new best for 60 min and under +0.5R); 20:45 analyst (trade on track); 22:15 analyst (5m structure broke); 22:20 analyst (trade on track); 22:25 analyst (5m structure broke); 00:07 readopted (app restarted; position restored from the shadow); 07:05 analyst (trade on track); 09:00 analyst (5m structure broke); 09:05 analyst (trade on track); 10:00 analyst (5m structure broke); 10:05 analyst (trade on track); 11:30 analyst (stalled: no new best for 60 min and under +0.5R)
- **my_ema_rsi_1h** US30 LONG 46f6a31a → close_past_ema21 (-0.33R, best 0.16R): 05:00 entry (52169.4); 05:00 analyst (trade on track); 05:55 analyst (5m structure broke); 06:00 liq_line (liquidity lines fixed at entry); 06:00 analyst (1H trend is against the trade); 06:05 analyst (5m structure broke; stalled: no new best for 60 ); 06:30 analyst (15m trend flipped against the trade; stalled: no); 08:00 exit_signal; 08:00 exit
- **my_ema_rsi_4h** XAUUSD SHORT 4fe39add → OPEN (R, best 2.16R): 09:00 entry (4089.847); 09:00 analyst (trade on track); 09:35 analyst (5m structure broke); 09:45 analyst (trade on track); 10:05 analyst (stalled: no new best for 60 min and under +0.5R); 10:15 analyst (trade on track); 10:40 analyst (5m structure broke); 10:45 analyst (15m trend flipped against the trade; 5m structur); 11:00 analyst (trade on track); 11:15 analyst (stalled: no new best for 60 min and under +0.5R); 12:10 analyst (trade on track); 13:00 analyst (5m structure broke); 13:05 analyst (trade on track); 13:10 analyst (5m structure broke)
- **my_ema_rsi_4h** NDQ SHORT a24a45d7 → OPEN (R, best 1.38R): 17:00 entry (29795.4); 17:00 analyst (trade on track); 20:10 analyst (stalled: no new best for 60 min and under +0.5R); 20:45 analyst (trade on track); 22:15 analyst (5m structure broke); 22:20 analyst (trade on track); 22:25 analyst (5m structure broke); 00:07 readopted (app restarted; position restored from the shadow); 01:00 liq_line (no liquidity line beyond 1R: book rules apply); 06:15 analyst (trade on track); 06:25 analyst (stalled: no new best for 60 min and under +0.5R); 06:30 analyst (trade on track); 06:35 analyst (stalled: no new best for 60 min and under +0.5R); 06:45 analyst (trade on track)
- **my_intraday_mom** NDQ SHORT 7c0b4a39 → session_close (-0.58R, best 0.12R): 15:30 entry (28511.800000000003); 15:30 analyst (5m structure broke); 16:00 exit_signal (end of the 15:30-16:00 window); 16:00 exit
- **my_intraday_mom** US30 SHORT e4cdb439 → session_close (-0.44R, best 0.09R): 15:30 entry (51914.9); 15:30 analyst (trade on track); 15:55 analyst (5m structure broke); 16:00 exit_signal (end of the 15:30-16:00 window); 16:00 exit
- **my_rsi_4h** NDQ SHORT 446c4319 → OPEN (R, best 1.38R): 17:00 entry (29795.4); 17:00 analyst (trade on track); 20:10 analyst (stalled: no new best for 60 min and under +0.5R); 20:45 analyst (trade on track); 22:15 analyst (5m structure broke); 22:20 analyst (trade on track); 22:25 analyst (5m structure broke); 00:07 readopted (app restarted; position restored from the shadow); 01:00 liq_line (no liquidity line beyond 1R: book rules apply); 06:15 analyst (trade on track); 06:25 analyst (stalled: no new best for 60 min and under +0.5R); 06:30 analyst (trade on track); 06:35 analyst (stalled: no new best for 60 min and under +0.5R); 06:45 analyst (trade on track)
- **playbook_allhours** XAUUSD SHORT a7bf6fe7 → stop (-1.00R, best 0.02R): 00:45 entry (4004.724); 00:50 analyst (trade on track); 01:00 analyst (5m structure broke); 01:27 exit
- **playbook_allhours** XAUUSD SHORT 98609f78 → stop (-1.00R, best 0.08R): 04:10 entry (3988.929); 04:15 analyst (trade on track); 04:20 exit
- **playbook_allhours** US30 LONG 3ea27ebd → stop (-1.00R, best 0.57R): 05:45 entry (52297.3); 05:50 analyst (trade on track); 05:55 analyst (5m structure broke); 06:00 analyst (1H trend is against the trade); 06:05 analyst (5m structure broke; 1H trend is against the trad); 06:20 analyst (1H trend is against the trade); 06:30 analyst (15m trend flipped against the trade; 1H trend is); 06:45 analyst (1H trend is against the trade); 06:50 analyst (stalled: no new best for 60 min and under +0.5R;); 07:00 analyst (1H trend is against the trade); 08:15 analyst (15m trend flipped against the trade; 5m structur); 08:44 exit
- **playbook_nobias** XAUUSD SHORT dfeff454 → stop (-1.00R, best 0.08R): 04:10 entry (3988.929); 04:15 analyst (trade on track); 04:20 exit
- **playbook_regime** XAUUSD SHORT 451af5f5 → stop (-1.00R, best 0.08R): 04:10 entry (3988.929); 04:15 analyst (trade on track); 04:20 exit

## 7. Entry reasons of every trade

- c10_afternoon 1142945a NDQ SHORT: morning down held to 13:00: 28402.6 vs prior close 29439.4, 3.5 ATR from 09:30, ER 0.46
- ema21_rsi55 d925f0de XAUUSD SHORT: EMA21+RSI45 short: 15m close 3991.53 < EMA21 4000.72, RSI 41.0
- ema21_rsi55 6b559030 XAUUSD SHORT: EMA21+RSI45 short: 15m close 3982.68 < EMA21 3990.18, RSI 42.0
- h1_vol_trend de2fdaa1 XAUUSD SHORT: H1-VOL-TREND short: 12-bar breakout, EMA32/128 trend, ER24 ≥ 0.30, normal ATR
- live 74ae19f3 NDQ SHORT: morning down held to 13:00: 28402.6 vs prior close 29439.4, 3.5 ATR from 09:30, ER 0.46
- my_ema_cross_4h 59f05cdd NDQ SHORT: my_ema_cross_4h: 4h close 29088.00 < EMA21 29475.53, RSI 34.0, CHOP 42, Supertrend down
- my_ema_rsi_15m 928f03d6 XAUUSD SHORT: my_ema_rsi_15m: 15min close 3991.53 < EMA21 4000.72, RSI 41.0, CHOP 55, Supertrend down
- my_ema_rsi_15m e933b036 NDQ SHORT: my_ema_rsi_15m: 15min close 28851.20 < EMA21 28868.82, RSI 43.0, CHOP 45, Supertrend down
- my_ema_rsi_15m 21dacf55 NDQ SHORT: my_ema_rsi_15m: 15min close 28789.60 < EMA21 28836.58, RSI 41.0, CHOP 51, Supertrend down
- my_ema_rsi_15m 0584f536 XAUUSD SHORT: my_ema_rsi_15m: 15min close 3982.68 < EMA21 3990.18, RSI 42.0, CHOP 45, Supertrend down
- my_ema_rsi_1d 039ebc8c NDQ SHORT: my_ema_rsi_1d: 1D close 29088.00 < EMA21 29776.40, RSI 39.9, CHOP 49, Supertrend down
- my_ema_rsi_1h 46f6a31a US30 LONG: my_ema_rsi_1h: 1h close 52474.20 > EMA21 52382.71, RSI 55.2, CHOP 57, Supertrend down
- my_ema_rsi_4h 4fe39add XAUUSD SHORT: my_ema_rsi_4h: 4h close 4020.79 < EMA21 4039.36, RSI 43.2, CHOP 55, Supertrend down
- my_ema_rsi_4h a24a45d7 NDQ SHORT: my_ema_rsi_4h: 4h close 29088.00 < EMA21 29475.53, RSI 34.0, CHOP 42, Supertrend down
- my_intraday_mom 7c0b4a39 NDQ SHORT: my_intraday_mom: first half-hour -2.467% (16:00 close 29439.40 -> 10:00 28713.00) -> short 15:30-16:00
- my_intraday_mom e4cdb439 US30 SHORT: my_intraday_mom: first half-hour -0.379% (16:00 close 52378.80 -> 10:00 52180.20) -> short 15:30-16:00
- my_rsi_4h 446c4319 NDQ SHORT: my_rsi_4h: 4h close 29088.00 < EMA21 29475.53, RSI 34.0, CHOP 42, Supertrend down
- playbook_allhours a7bf6fe7 XAUUSD SHORT: BOS → retest of the broken level · playbook stop=level/std p=0.52
- playbook_allhours 7c5a6513 XAUUSD SHORT: Turtle Soup (n20, choch) · playbook confirm=choch/std p=0.57
- playbook_allhours 4c64eb28 XAUUSD SHORT: DTFX wick_fib BOS → 50% rejection · playbook sessions=killzones/std p=0.57
- playbook_allhours be6f5df6 NDQ SHORT: AMD (midnight): manipulation → distribution · playbook model=midnight/std p=0.50
- playbook_allhours 98609f78 XAUUSD SHORT: BOS → retest of the broken level · playbook tol_atr=0.3/std p=0.54
- playbook_allhours 3ea27ebd US30 LONG: DTFX close_fib BOS → 50-70% zone rejection · playbook level=50-70/trend p=0.51
- playbook_allhours f9decaaa XAUUSD SHORT: BOS → retest of the broken level · playbook tol_atr=0.3/std p=0.54
- playbook_allhours d654bc45 XAUUSD SHORT: BOS → retest of the broken level · playbook stop=level/std p=0.52
- playbook_allhours dbd4db6a XAUUSD SHORT: BOS → retest of the broken level · playbook tol_atr=0.3/std p=0.54
- playbook_nobias c975c56c XAUUSD SHORT: DTFX wick_fib BOS → 50% rejection · playbook sessions=killzones/std p=0.57
- playbook_nobias 513a6130 XAUUSD SHORT: BOS → retest of the broken level · playbook tol_atr=0.3/std p=0.54
- playbook_nobias d21302c0 NDQ SHORT: AMD (midnight): manipulation → distribution · playbook model=midnight/std p=0.50
- playbook_nobias dfeff454 XAUUSD SHORT: BOS → retest of the broken level · playbook tol_atr=0.3/std p=0.54
- playbook_nobias deb2789a XAUUSD SHORT: BOS → retest of the broken level · playbook stop=level/std p=0.52
- playbook_nobias 01cab92f XAUUSD SHORT: BOS → retest of the broken level · playbook tol_atr=0.3/std p=0.54
- playbook_regime 451af5f5 XAUUSD SHORT: BOS → retest of the broken level · playbook tol_atr=0.3/std p=0.54
- playbook_regime 28071d8f XAUUSD SHORT: BOS → retest of the broken level · playbook stop=level/std p=0.52
- playbook_regime 1aa1599d XAUUSD SHORT: BOS → retest of the broken level · playbook tol_atr=0.3/std p=0.54
- shadow 7ea35235 NDQ SHORT: AMD (midnight): manipulation → distribution · playbook model=midnight/std p=0.50
