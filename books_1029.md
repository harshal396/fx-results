# RSI / EMA books report

Generated 2026-10-29 22:26 New York. Window: since 2026-10-29 00:00 (22 h). R = profit as a multiple of the risk at the first stop.

Books read: live, c10_afternoon, daily_rsi2_adx2, ema21_rsi55, h1_vol_trend, my_ema_cross_15m, my_ema_cross_1d, my_ema_cross_1h, my_ema_cross_4h, my_ema_rsi_15m, my_ema_rsi_1d, my_ema_rsi_1h, my_ema_rsi_4h, my_intraday_mom, my_rsi_15m, my_rsi_1h, my_rsi_4h, playbook_regime, shadow

## 1. Per book

| Book | Trades | Closed | Open | Wins | Total R | P&L | Avg best R | Avg hours held | Jev partials |
|---|---|---|---|---|---|---|---|---|---|
| live | 1 | 1 | 0 | 1 | +0.55 | +86.13 | 1.75 | 0.3 | 1 |
| c10_afternoon | 0 | 0 | 0 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 0 |
| daily_rsi2_adx2 | 0 | 0 | 0 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 0 |
| ema21_rsi55 | 1 | 1 | 0 | 1 | +0.10 | +7.00 | 0.57 | 2.3 | 0 |
| h1_vol_trend | 0 | 0 | 0 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 0 |
| my_ema_cross_15m | 2 | 2 | 0 | 2 | +0.73 | +255.02 | 1.08 | 4.7 | 2 |
| my_ema_cross_1d | 0 | 0 | 0 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 0 |
| my_ema_cross_1h | 0 | 0 | 0 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 0 |
| my_ema_cross_4h | 3 | 2 | 1 | 0 | -0.52 | -180.03 | 0.49 | 9.4 | 0 |
| my_ema_rsi_15m | 4 | 3 | 1 | 2 | +1.14 | +397.58 | 1.88 | 4.9 | 3 |
| my_ema_rsi_1d | 2 | 1 | 1 | 0 | -0.24 | -83.60 | 0.41 | 15.4 | 0 |
| my_ema_rsi_1h | 2 | 2 | 0 | 1 | -0.14 | -51.98 | 0.82 | 88.8 | 2 |
| my_ema_rsi_4h | 3 | 1 | 2 | 0 | +0.00 | +0.00 | 1.81 | 165.6 | 0 |
| my_intraday_mom | 2 | 2 | 0 | 0 | -0.72 | -251.73 | 0.15 | 0.5 | 0 |
| my_rsi_15m | 3 | 0 | 3 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 2 |
| my_rsi_1h | 1 | 1 | 0 | 0 | -1.00 | -350.36 | 0.19 | 158.7 | 0 |
| my_rsi_4h | 2 | 1 | 1 | 0 | -1.00 | -350.84 | 0.31 | 163.1 | 0 |
| playbook_regime | 2 | 1 | 1 | 0 | -1.00 | -174.34 | 0.07 | 1.0 | 0 |
| shadow | 6 | 4 | 2 | 0 | -3.31 | -578.13 | 0.29 | 1.3 | 0 |

All listed books: 22 closed trades, -5.42 R.

## 2. Why the losing trades lost

| Cause | Trades | R |
|---|---|---|
| stopped at the first stop | 10 | -6.69 |
| gave back: was +0.5R or better first | 3 | -1.48 |
| closed on the EMA exit at a loss | 1 | -0.80 |

## 3. Skipped signals (what the filters blocked)

**live**: 3x filtered: counter to BEARISH bias; 3x filtered: bias neutral (#); 2x filtered: counter to BULLISH bias; 2x skipped: Jev quality # < #; 1x rejected: cost #R of the stop (spread # vs stop #) > cap #R; 1x taken: qty #, risk $#, cost #R; 1x skipped: Jev quality # < # and confidence # < #
**ema21_rsi55**: 1x taken: qty #, jev #
**my_ema_cross_15m**: 3x rejected: not a fresh cross (the price has been above the EMA# for # candles, limit #; 2x rejected: not a fresh cross (the price has been below the EMA# for # candles, limit #; 1x rejected: against the #h trend (bearish) - no buy; 1x rejected: RSI not falling (RSI #, # three candles ago) - no sell; 1x taken: qty #, jev #
**my_ema_cross_1h**: 2x rejected: not a fresh cross (the price has been below the EMA# for # candles, limit #
**my_ema_cross_4h**: 2x taken: qty #, jev #; 1x rejected: against the #D trend (bullish) - no sell
**my_ema_rsi_15m**: 15x rejected: not a fresh cross (the price has been below the EMA# for # candles, limit #; 5x rejected: not a fresh cross (the price has been above the EMA# for # candles, limit #; 2x rejected: choppy market (CHOP # ≥ #); 2x taken: qty #, jev #; 1x rejected: against the #h trend (bearish) - no buy; 1x rejected: stop too wide (# ATR)
**my_ema_rsi_1d**: 1x taken: qty #, jev #
**my_ema_rsi_1h**: 11x rejected: not a fresh cross (the price has been below the EMA# for # candles, limit #; 1x rejected: against the #h trend (bullish) - no sell
**my_ema_rsi_4h**: 2x taken: qty #, jev #
**my_intraday_mom**: 2x taken: qty #, jev None
**my_rsi_1h**: 1x rejected: not a fresh cross (the price has been below the EMA# for # candles, limit #
**my_rsi_4h**: 1x taken: qty #, jev #; 1x rejected: choppy market (CHOP # ≥ #)
**playbook_regime**: 18x skipped: regime chop (Jev chop #, CHOP #): scalps only; 13x filtered: bias neutral (#); 8x filtered: counter to BEARISH bias; 2x filtered: counter to BULLISH bias; 1x taken: qty #, risk $#, cost #R; 1x rejected: outside entry windows; 1x skipped: Jev quality # < #
**shadow**: 13x filtered: bias neutral (#); 8x filtered: counter to BEARISH bias; 6x skipped: Jev quality # < #; 4x taken: qty #, risk $#, cost #R; 4x filtered: bias suspended; 2x filtered: counter to BULLISH bias; 2x skipped: a higher-expectancy playbook cell fired on this bar; 2x skipped: Jev quality # < # and confidence # < #

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
| ema21_rsi55 | any_exit | 11 | -0.11 | 7 |
| ema21_rsi55 | giveback | 1 | -0.05 | 0 |
| ema21_rsi55 | h1_against | 10 | -0.20 | 6 |
| ema21_rsi55 | news_soon | 1 | +0.34 | 1 |
| ema21_rsi55 | stall | 8 | -0.21 | 6 |
| ema21_rsi55 | structure_break | 10 | +0.06 | 5 |
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
| my_ema_rsi_15m | any_exit | 39 | -0.02 | 23 |
| my_ema_rsi_15m | giveback | 12 | +0.05 | 11 |
| my_ema_rsi_15m | h1_against | 33 | +0.09 | 20 |
| my_ema_rsi_15m | news_soon | 1 | +0.11 | 1 |
| my_ema_rsi_15m | stall | 17 | -0.01 | 9 |
| my_ema_rsi_15m | structure_break | 35 | -0.00 | 18 |
| my_ema_rsi_15m | trend_flip | 9 | +0.15 | 7 |
| my_ema_rsi_1d | any_exit | 1 | +0.19 | 1 |
| my_ema_rsi_1d | h1_against | 1 | +0.14 | 1 |
| my_ema_rsi_1d | news_soon | 1 | -0.04 | 0 |
| my_ema_rsi_1d | stall | 1 | +0.20 | 1 |
| my_ema_rsi_1d | structure_break | 1 | +0.19 | 1 |
| my_ema_rsi_1d | trend_flip | 1 | +0.30 | 1 |
| my_ema_rsi_1h | any_exit | 23 | +0.16 | 16 |
| my_ema_rsi_1h | giveback | 1 | +0.07 | 1 |
| my_ema_rsi_1h | h1_against | 3 | +0.50 | 3 |
| my_ema_rsi_1h | news_soon | 1 | -0.20 | 0 |
| my_ema_rsi_1h | stall | 15 | +0.24 | 12 |
| my_ema_rsi_1h | structure_break | 23 | +0.13 | 16 |
| my_ema_rsi_1h | trend_flip | 20 | +0.10 | 14 |
| my_ema_rsi_4h | any_exit | 4 | +0.26 | 3 |
| my_ema_rsi_4h | giveback | 1 | +0.43 | 1 |
| my_ema_rsi_4h | h1_against | 1 | +0.12 | 1 |
| my_ema_rsi_4h | news_soon | 1 | +0.28 | 1 |
| my_ema_rsi_4h | stall | 4 | +0.31 | 3 |
| my_ema_rsi_4h | structure_break | 4 | +0.14 | 2 |
| my_ema_rsi_4h | trend_flip | 4 | +0.23 | 4 |
| my_intraday_mom | any_exit | 8 | +0.10 | 5 |
| my_intraday_mom | h1_against | 3 | +0.07 | 2 |
| my_intraday_mom | structure_break | 8 | +0.10 | 5 |
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
| playbook_regime | any_exit | 2 | -0.02 | 1 |
| playbook_regime | giveback | 3 | -0.04 | 2 |
| playbook_regime | stall | 1 | -0.19 | 0 |
| playbook_regime | structure_break | 2 | -0.02 | 1 |
| shadow | any_exit | 22 | +0.13 | 14 |
| shadow | giveback | 7 | +0.05 | 6 |
| shadow | h1_against | 8 | -0.10 | 3 |
| shadow | stall | 13 | +0.14 | 8 |
| shadow | structure_break | 20 | +0.11 | 13 |
| shadow | trend_flip | 5 | +0.27 | 5 |

## 5. Every trade in the window

| Book | Id | Market | Side | Opened (NY) | Closed (NY) | Entry | Exit | First stop | Stop at end | Qty | P&L | R | Best R | Worst R | How it ended |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ema21_rsi55 | 75e8b85f | US30 | SHORT | 10-29 06:45 | 10-29 09:01 | 52503.60 | 52471.80 | 52821.30 | 52471.80 | 0.22 | 7.00 | 0.10 | 0.57 | -0.30 | stop |
| live | 20ab619a | NDQ | SHORT | 10-29 04:40 | 10-29 04:55 | 29475.20 | 29472.54 | 29506.80 | 29472.00 | 4.95 | 86.13 | 0.55 | 1.75 | -0.25 | breakeven_plus_stop |
| my_ema_cross_15m | 758f2ac8 | XAUUSD | SHORT | 10-28 22:45 | 10-29 06:15 | 4042.97 | 4033.59 | 4071.51 | 4071.51 | 12.20 | 177.09 | 0.51 | 0.95 | -0.26 | close_past_ema21 |
| my_ema_cross_15m | 39d652eb | XAUUSD | SHORT | 10-29 19:30 | 10-29 21:29 | 4015.05 | 4011.65 | 4030.37 | 4011.65 | 22.90 | 77.93 | 0.22 | 1.21 | -0.26 | stop |
| my_ema_cross_4h | dd479e2f | US30 | LONG | 10-28 17:00 | 10-29 08:25 | 52616.10 | 52396.10 | 52189.60 | 52189.60 | 0.81 | -178.20 | -0.52 | 0.88 | -0.64 | pre-news: Advance GDP q/q |
| my_ema_cross_4h | 8776906e | XAUUSD | SHORT | 10-29 05:00 | 10-29 08:25 | 4023.94 | 4024.28 | 4089.95 | 4089.95 | 5.30 | -1.83 | -0.01 | 0.10 | -0.23 | pre-news: Advance GDP q/q |
| my_ema_cross_4h | 59f05cdd | NDQ | SHORT | 10-29 17:00 | open | 29086.80 |  | 29795.40 | 29795.40 | 0.49 | 0.00 |  | 0.00 | 0.00 | OPEN |
| my_ema_rsi_15m | c94efac9 | US30 | LONG | 10-22 15:30 | open | 52852.50 |  | 52692.40 | 52692.40 | 2.21 | 0.00 |  | 0.00 | 0.00 | OPEN |
| my_ema_rsi_15m | 7d727584 | US30 | LONG | 10-28 20:15 | 10-29 06:34 | 52592.10 | 52656.90 | 52492.40 | 52656.90 | 3.50 | 343.53 | 0.98 | 4.01 | -0.33 | stop |
| my_ema_rsi_15m | beb4935c | NDQ | SHORT | 10-29 09:45 | 10-29 11:15 | 29417.10 | 29482.20 | 29592.10 | 29592.10 | 2.00 | -130.20 | -0.37 | 0.61 | -0.46 | close_past_ema21 |
| my_ema_rsi_15m | 22506910 | XAUUSD | SHORT | 10-29 19:15 | 10-29 22:17 | 4013.47 | 4013.47 | 4030.41 | 4013.47 | 20.60 | 184.25 | 0.53 | 1.01 | -0.33 | stop |
| my_ema_rsi_1d | 4e7ae8d4 | US30 | LONG | 10-28 17:00 | 10-29 08:25 | 52616.10 | 52396.10 | 51704.30 | 51704.30 | 0.38 | -83.60 | -0.24 | 0.41 | -0.30 | pre-news: Advance GDP q/q |
| my_ema_rsi_1d | 039ebc8c | NDQ | SHORT | 10-29 17:00 | open | 29086.80 |  | 30180.10 | 30180.10 | 0.32 | 0.00 |  | 0.00 | 0.00 | OPEN |
| my_ema_rsi_1h | 216b658a | US30 | LONG | 10-22 12:00 | 10-29 07:00 | 52865.10 | 52525.60 | 52439.40 | 52439.40 | 0.82 | -278.39 | -0.80 | 0.30 | -0.95 | close_past_ema21 |
| my_ema_rsi_1h | ee5142d6 | US30 | LONG | 10-28 16:00 | 10-29 06:34 | 52570.10 | 52663.20 | 52252.70 | 52663.20 | 1.09 | 226.41 | 0.65 | 1.33 | -0.21 | stop |
| my_ema_rsi_4h | c0daa33b | US30 | LONG | 10-22 09:00 | 10-29 06:34 | 52588.50 | 52588.50 | 52365.40 | 52588.50 | 1.58 | 0.00 | 0.00 | 1.81 | -0.25 | stop |
| my_ema_rsi_4h | 4fe39add | XAUUSD | SHORT | 10-29 09:00 | open | 4020.48 |  | 4089.85 | 4089.85 | 5.00 | 0.00 |  | 0.00 | 0.00 | OPEN |
| my_ema_rsi_4h | a24a45d7 | NDQ | SHORT | 10-29 17:00 | open | 29086.80 |  | 29795.40 | 29795.40 | 0.49 | 0.00 |  | 0.00 | 0.00 | OPEN |
| my_intraday_mom | d908a0b6 | NDQ | SHORT | 10-29 15:30 | 10-29 16:00 | 29366.30 | 29440.60 | 29564.80 | 29564.80 | 1.76 | -130.77 | -0.37 | 0.20 | -0.40 | session_close |
| my_intraday_mom | cbcc18a1 | US30 | SHORT | 10-29 15:30 | 10-29 16:00 | 52308.30 | 52380.30 | 52516.60 | 52516.60 | 1.68 | -120.96 | -0.35 | 0.11 | -0.36 | session_close |
| my_rsi_15m | d5f69550 | XAUUSD | SHORT | 10-22 11:15 | open | 4054.70 |  | 4084.20 | 4034.91 | 11.90 | 159.92 |  | 1.14 | -0.22 | OPEN |
| my_rsi_15m | fcd1d2ed | US30 | LONG | 10-22 16:00 | open | 52912.50 |  | 52692.50 | 52692.50 | 1.61 | 0.00 |  | 0.00 | 0.00 | OPEN |
| my_rsi_15m | 9971e243 | NDQ | SHORT | 10-22 16:45 | open | 28967.40 |  | 29085.60 | 29085.60 | 3.00 | 0.00 |  | 0.00 | 0.00 | OPEN |
| my_rsi_1h | af640ece | US30 | LONG | 10-22 16:00 | 10-29 06:40 | 52912.50 | 52495.40 | 52495.40 | 52495.40 | 0.84 | -350.36 | -1.00 | 0.19 | -0.92 | stop |
| my_rsi_4h | 3750c941 | US30 | LONG | 10-22 13:00 | 10-29 08:04 | 52842.50 | 52361.90 | 52361.90 | 52361.90 | 0.73 | -350.84 | -1.00 | 0.31 | -0.99 | stop |
| my_rsi_4h | 446c4319 | NDQ | SHORT | 10-29 17:00 | open | 29086.80 |  | 29795.40 | 29795.40 | 0.49 | 0.00 |  | 0.00 | 0.00 | OPEN |
| playbook_regime | 05bac06e | US30 | LONG | 10-20 20:30 | open | 52554.50 |  | 52437.60 | 52437.60 | 2.78 | 0.00 |  | 0.00 | 0.00 | OPEN |
| playbook_regime | 58829378 | XAUUSD | SHORT | 10-29 14:30 | 10-29 15:31 | 4006.27 | 4018.72 | 4018.72 | 4018.72 | 14.00 | -174.34 | -1.00 | 0.07 | -0.92 | stop |
| shadow | ebcda2f4 | NDQ | SHORT | 10-19 22:15 | open | 29545.40 |  | 29647.70 | 29647.70 | 3.34 | 0.00 |  | 0.00 | 0.00 | OPEN |
| shadow | 4dfb39be | US30 | LONG | 10-20 20:30 | open | 52554.50 |  | 52437.60 | 52437.60 | 2.73 | 0.00 |  | 0.00 | 0.00 | OPEN |
| shadow | 108eb1fc | US30 | LONG | 10-29 03:00 | 10-29 03:59 | 52771.10 | 52659.60 | 52659.60 | 52659.60 | 1.57 | -175.06 | -1.00 | 0.44 | -0.97 | stop |
| shadow | 35af8281 | XAUUSD | SHORT | 10-29 04:55 | 10-29 05:09 | 4018.89 | 4035.66 | 4035.66 | 4035.66 | 10.40 | -174.51 | -1.00 | 0.00 | -0.81 | stop |
| shadow | 56aa92a6 | XAUUSD | SHORT | 10-29 13:45 | 10-29 15:50 | 4013.19 | 4020.69 | 4025.90 | 4025.90 | 13.70 | -102.75 | -0.59 | 0.62 | -0.61 | session_flat |
| shadow | eedc7368 | XAUUSD | SHORT | 10-29 14:00 | 10-29 15:50 | 4006.86 | 4020.69 | 4026.00 | 4026.00 | 9.10 | -125.81 | -0.72 | 0.08 | -0.73 | session_flat |

## 6. Timelines of the losing and the open trades

- **my_ema_cross_4h** US30 LONG dd479e2f → pre-news: Advance GDP q/q (-0.52R, best 0.88R): 17:00 entry (52189.600000000006); 17:00 analyst (trade on track); 17:00 readopted (app restarted; position restored from the shadow); 18:05 analyst (5m structure broke); 18:25 analyst (trade on track); 19:05 analyst (stalled: no new best for 60 min and under +0.5R); 20:45 analyst (trade on track); 23:00 analyst (stalled: no new best for 60 min and under +0.5R); 23:06 readopted (app restarted; position restored from the shadow); 01:05 analyst (trade on track); 02:20 analyst (stalled: no new best for 60 min and under +0.5R); 04:00 analyst (15m trend flipped against the trade; 5m structur); 04:30 analyst (trade on track); 04:40 analyst (stalled: no new best for 60 min and under +0.5R)
- **my_ema_cross_4h** XAUUSD SHORT 8776906e → pre-news: Advance GDP q/q (-0.01R, best 0.10R): 05:00 entry (4089.951); 05:00 analyst (trade on track); 05:10 analyst (5m structure broke); 05:15 analyst (trade on track); 06:05 analyst (stalled: no new best for 60 min and under +0.5R); 08:00 analyst (trade on track); 08:10 analyst (high-impact news within 20 min); 08:25 exit
- **my_ema_cross_4h** NDQ SHORT 59f05cdd → OPEN (R, best 0.00R): 17:00 entry (29795.4)
- **my_ema_rsi_15m** US30 LONG c94efac9 → OPEN (R, best 0.00R): 15:30 entry (52692.4)
- **my_ema_rsi_15m** NDQ SHORT beb4935c → close_past_ema21 (-0.37R, best 0.61R): 09:45 entry (29592.100000000002); 09:45 analyst (trade on track); 10:05 analyst (5m structure broke); 10:10 analyst (trade on track); 10:55 analyst (stalled: no new best for 60 min and under +0.5R); 11:15 exit_signal; 11:15 exit
- **my_ema_rsi_1d** US30 LONG 4e7ae8d4 → pre-news: Advance GDP q/q (-0.24R, best 0.41R): 17:00 entry (51704.3); 17:00 analyst (trade on track); 17:00 readopted (app restarted; position restored from the shadow); 18:05 analyst (5m structure broke); 18:25 analyst (trade on track); 19:05 analyst (stalled: no new best for 60 min and under +0.5R); 20:45 analyst (trade on track); 23:00 analyst (stalled: no new best for 60 min and under +0.5R); 23:06 readopted (app restarted; position restored from the shadow); 01:05 analyst (trade on track); 02:20 analyst (stalled: no new best for 60 min and under +0.5R); 04:00 analyst (15m trend flipped against the trade; 5m structur); 05:10 analyst (trade on track); 06:35 analyst (5m structure broke)
- **my_ema_rsi_1d** NDQ SHORT 039ebc8c → OPEN (R, best 0.00R): 17:00 entry (30180.100000000002)
- **my_ema_rsi_1h** US30 LONG 216b658a → close_past_ema21 (-0.80R, best 0.30R): 12:00 entry (52439.4); 23:06 readopted (bot restarted; trade restored from the journal); 23:10 analyst (5m structure broke); 23:45 analyst (trade on track); 00:10 analyst (stalled: no new best for 60 min and under +0.5R); 01:15 analyst (trade on track); 02:20 analyst (stalled: no new best for 60 min and under +0.5R); 04:00 analyst (15m trend flipped against the trade; 5m structur); 05:10 analyst (trade on track); 06:35 analyst (5m structure broke); 07:00 exit_signal; 07:00 exit
- **my_ema_rsi_4h** XAUUSD SHORT 4fe39add → OPEN (R, best 0.00R): 09:00 entry (4089.847)
- **my_ema_rsi_4h** NDQ SHORT a24a45d7 → OPEN (R, best 0.00R): 17:00 entry (29795.4)
- **my_intraday_mom** NDQ SHORT d908a0b6 → session_close (-0.37R, best 0.20R): 15:30 entry (29564.800000000003); 15:30 analyst (5m structure broke); 15:40 analyst (trade on track); 15:55 analyst (5m structure broke); 16:00 exit_signal (end of the 15:30-16:00 window); 16:00 exit
- **my_intraday_mom** US30 SHORT cbcc18a1 → session_close (-0.35R, best 0.11R): 15:30 entry (52516.600000000006); 15:30 analyst (5m structure broke); 15:50 analyst (trade on track); 16:00 exit_signal (end of the 15:30-16:00 window); 16:00 exit
- **my_rsi_15m** XAUUSD SHORT d5f69550 → OPEN (R, best 1.14R): 11:15 entry (4084.205); 11:15 analyst (trade on track); 13:00 agent_check (continuation 0.47 ≥ 0.45); 14:00 analyst (stalled: no new best for 60 min and under +0.5R); 14:10 analyst (trade on track); 14:15 partial (Jev: continuation 0.40 < 0.45); 14:20 analyst (stalled: no new best for 60 min and under +0.5R); 14:25 analyst (trade on track); 14:30 partial (Jev: continuation 0.43 < 0.45); 15:45 stop_moved (breakeven / 2×ATR trail after +1R); 16:00 stop_moved (breakeven / 2×ATR trail after +1R); 16:15 stop_moved (breakeven / 2×ATR trail after +1R); 16:30 stop_moved (breakeven / 2×ATR trail after +1R); 16:45 stop_moved (breakeven / 2×ATR trail after +1R)
- **my_rsi_15m** US30 LONG fcd1d2ed → OPEN (R, best 0.00R): 16:00 entry (52692.5)
- **my_rsi_15m** NDQ SHORT 9971e243 → OPEN (R, best 0.00R): 16:45 entry (29085.600000000002)
- **my_rsi_1h** US30 LONG af640ece → stop (-1.00R, best 0.19R): 16:00 entry (52495.4); 23:06 readopted (bot restarted; trade restored from the journal); 23:10 analyst (5m structure broke); 23:45 analyst (trade on track); 00:10 analyst (stalled: no new best for 60 min and under +0.5R); 04:00 analyst (15m trend flipped against the trade; 5m structur); 06:40 exit
- **my_rsi_4h** US30 LONG 3750c941 → stop (-1.00R, best 0.31R): 13:00 entry (52361.9); 23:06 readopted (bot restarted; trade restored from the journal); 23:10 analyst (5m structure broke); 23:45 analyst (trade on track); 00:10 analyst (stalled: no new best for 60 min and under +0.5R); 01:15 analyst (trade on track); 02:20 analyst (stalled: no new best for 60 min and under +0.5R); 04:00 analyst (15m trend flipped against the trade; 5m structur); 05:10 analyst (trade on track); 06:35 analyst (5m structure broke); 07:10 analyst (1H trend is against the trade); 07:35 analyst (stalled: no new best for 60 min and under +0.5R;); 08:04 exit
- **my_rsi_4h** NDQ SHORT 446c4319 → OPEN (R, best 0.00R): 17:00 entry (29795.4)
- **playbook_regime** US30 LONG 05bac06e → OPEN (R, best 0.00R): 20:30 entry (52437.6)
- **playbook_regime** XAUUSD SHORT 58829378 → stop (-1.00R, best 0.07R): 14:30 entry (4018.723); 14:35 analyst (trade on track); 15:00 analyst (5m structure broke); 15:15 analyst (trade on track); 15:20 analyst (5m structure broke); 15:25 analyst (trade on track); 15:30 analyst (5m structure broke); 15:31 exit
- **shadow** NDQ SHORT ebcda2f4 → OPEN (R, best 0.00R): 22:15 entry (29647.7)
- **shadow** US30 LONG 4dfb39be → OPEN (R, best 0.00R): 20:30 entry (52437.6)
- **shadow** US30 LONG 108eb1fc → stop (-1.00R, best 0.44R): 03:00 entry (52659.6); 03:05 analyst (trade on track); 03:35 analyst (5m structure broke); 03:59 exit
- **shadow** XAUUSD SHORT 35af8281 → stop (-1.00R, best 0.00R): 04:55 entry (4035.665); 05:00 analyst (trade on track); 05:09 exit
- **shadow** XAUUSD SHORT 56aa92a6 → session_flat (-0.59R, best 0.62R): 13:45 entry (4025.896); 13:50 analyst (trade on track); 15:00 analyst (5m structure broke); 15:15 analyst (trade on track); 15:20 analyst (5m structure broke); 15:25 analyst (trade on track); 15:30 analyst (5m structure broke); 15:35 analyst (5m structure broke; stalled: no new best for 60 ); 15:50 exit
- **shadow** XAUUSD SHORT eedc7368 → session_flat (-0.72R, best 0.08R): 14:00 entry (4026.001); 14:05 analyst (trade on track); 15:00 analyst (5m structure broke); 15:15 analyst (trade on track); 15:20 analyst (5m structure broke); 15:25 analyst (trade on track); 15:30 analyst (5m structure broke); 15:35 analyst (5m structure broke; stalled: no new best for 60 ); 15:50 exit

## 7. Entry reasons of every trade

- ema21_rsi55 75e8b85f US30 SHORT: EMA21+RSI45 short: 15m close 52505.10 < EMA21 52770.80, RSI 33.6
- live 20ab619a NDQ SHORT: Resistance rejection @ 29482.87
- my_ema_cross_15m 758f2ac8 XAUUSD SHORT: my_ema_cross_15m: 15min close 4043.28 < EMA21 4051.49, RSI 45.1, CHOP 56, Supertrend up
- my_ema_cross_15m 39d652eb XAUUSD SHORT: my_ema_cross_15m: 15min close 4015.36 < EMA21 4018.83, RSI 45.4, CHOP 49, Supertrend down
- my_ema_cross_4h dd479e2f US30 LONG: my_ema_cross_4h: 4h close 52614.60 > EMA21 52460.36, RSI 57.5, CHOP 62, Supertrend up
- my_ema_cross_4h 8776906e XAUUSD SHORT: my_ema_cross_4h: 4h close 4024.25 < EMA21 4041.22, RSI 44.1, CHOP 55, Supertrend down
- my_ema_cross_4h 59f05cdd NDQ SHORT: my_ema_cross_4h: 4h close 29088.00 < EMA21 29475.53, RSI 34.0, CHOP 42, Supertrend down
- my_ema_rsi_15m c94efac9 US30 LONG: my_ema_rsi_15m: 15min close 52851.00 > EMA21 52781.32, RSI 57.8, CHOP 59, Supertrend up
- my_ema_rsi_15m 7d727584 US30 LONG: my_ema_rsi_15m: 15min close 52590.60 > EMA21 52557.42, RSI 56.0, CHOP 42, Supertrend up
- my_ema_rsi_15m beb4935c NDQ SHORT: my_ema_rsi_15m: 15min close 29418.30 < EMA21 29509.15, RSI 39.7, CHOP 41, Supertrend down
- my_ema_rsi_15m 22506910 XAUUSD SHORT: my_ema_rsi_15m: 15min close 4013.78 < EMA21 4019.18, RSI 43.4, CHOP 47, Supertrend down
- my_ema_rsi_1d 4e7ae8d4 US30 LONG: my_ema_rsi_1d: 1D close 52614.60 > EMA21 52186.56, RSI 56.8, CHOP 59, Supertrend up
- my_ema_rsi_1d 039ebc8c NDQ SHORT: my_ema_rsi_1d: 1D close 29088.00 < EMA21 29776.40, RSI 39.9, CHOP 49, Supertrend down
- my_ema_rsi_1h 216b658a US30 LONG: my_ema_rsi_1h: 1h close 52863.60 > EMA21 52670.66, RSI 59.9, CHOP 57, Supertrend up
- my_ema_rsi_1h ee5142d6 US30 LONG: my_ema_rsi_1h: 1h close 52568.60 > EMA21 52444.84, RSI 59.9, CHOP 53, Supertrend up
- my_ema_rsi_4h c0daa33b US30 LONG: my_ema_rsi_4h: 4h close 52587.00 > EMA21 52452.03, RSI 56.2, CHOP 46, Supertrend up
- my_ema_rsi_4h 4fe39add XAUUSD SHORT: my_ema_rsi_4h: 4h close 4020.79 < EMA21 4039.36, RSI 43.2, CHOP 55, Supertrend down
- my_ema_rsi_4h a24a45d7 NDQ SHORT: my_ema_rsi_4h: 4h close 29088.00 < EMA21 29475.53, RSI 34.0, CHOP 42, Supertrend down
- my_intraday_mom d908a0b6 NDQ SHORT: my_intraday_mom: first half-hour -1.489% (16:00 close 29859.50 -> 10:00 29414.80) -> short 15:30-16:00
- my_intraday_mom cbcc18a1 US30 SHORT: my_intraday_mom: first half-hour -0.428% (16:00 close 52568.60 -> 10:00 52343.60) -> short 15:30-16:00
- my_rsi_15m d5f69550 XAUUSD SHORT: my_rsi_15m: 15min close 4055.01 < EMA21 4068.51, RSI 38.3, CHOP 49, Supertrend down
- my_rsi_15m fcd1d2ed US30 LONG: my_rsi_15m: 15min close 52911.00 > EMA21 52798.62, RSI 62.1, CHOP 61, Supertrend up
- my_rsi_15m 9971e243 NDQ SHORT: my_rsi_15m: 15min close 28968.60 < EMA21 29041.31, RSI 38.9, CHOP 59, Supertrend down
- my_rsi_1h af640ece US30 LONG: my_rsi_1h: 1h close 52911.00 > EMA21 52722.60, RSI 60.6, CHOP 58, Supertrend up
- my_rsi_4h 3750c941 US30 LONG: my_rsi_4h: 4h close 52841.00 > EMA21 52487.40, RSI 61.9, CHOP 49, Supertrend up
- my_rsi_4h 446c4319 NDQ SHORT: my_rsi_4h: 4h close 29088.00 < EMA21 29475.53, RSI 34.0, CHOP 42, Supertrend down
- playbook_regime 05bac06e US30 LONG: DTFX close_fib BOS → 50-70% zone rejection · playbook level=50-70/trend p=0.47
- playbook_regime 58829378 XAUUSD SHORT: BOS → retest of the broken level · playbook stop=level/std p=0.52
- shadow ebcda2f4 NDQ SHORT: DTFX wick_fib BOS → 50-70% zone rejection · playbook level=50-70/std p=0.55
- shadow 4dfb39be US30 LONG: DTFX close_fib BOS → 50-70% zone rejection · playbook level=50-70/trend p=0.47
- shadow 108eb1fc US30 LONG: DTFX close_fib BOS → 50-70% zone rejection · playbook level=50-70/trend p=0.51
- shadow 35af8281 XAUUSD SHORT: BOS → retest of the broken level · playbook tol_atr=0.3/std p=0.54
- shadow 56aa92a6 XAUUSD SHORT: BOS → retest of the broken level · playbook stop=level/std p=0.52
- shadow eedc7368 XAUUSD SHORT: BOS → retest of the broken level · playbook tol_atr=0.3/std p=0.54
