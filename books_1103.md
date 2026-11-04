# RSI / EMA books report

Generated 2026-11-03 23:00 New York. Window: since 2026-11-02 17:00 (30 h). R = profit as a multiple of the risk at the first stop.

Books read: live, c10_afternoon, daily_rsi2_adx2, ema21_rsi55, h1_vol_trend, my_ema_cross_15m, my_ema_cross_1d, my_ema_cross_1h, my_ema_cross_4h, my_ema_rsi_15m, my_ema_rsi_1d, my_ema_rsi_1h, my_ema_rsi_4h, my_intraday_mom, my_rsi_15m, my_rsi_1h, my_rsi_4h, playbook_allhours, playbook_nobias, playbook_regime, shadow

## 1. Per book

| Book | Trades | Closed | Open | Wins | Total R | P&L | Avg best R | Avg hours held | Jev partials |
|---|---|---|---|---|---|---|---|---|---|
| live | 1 | 1 | 0 | 0 | -1.00 | -321.76 | 0.22 | 0.4 | 0 |
| c10_afternoon | 0 | 0 | 0 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 0 |
| daily_rsi2_adx2 | 0 | 0 | 0 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 0 |
| ema21_rsi55 | 1 | 1 | 0 | 0 | -0.66 | -45.73 | 0.66 | 1.2 | 0 |
| h1_vol_trend | 0 | 0 | 0 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 0 |
| my_ema_cross_15m | 1 | 1 | 0 | 0 | -0.41 | -143.46 | 0.75 | 1.2 | 0 |
| my_ema_cross_1d | 0 | 0 | 0 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 0 |
| my_ema_cross_1h | 2 | 1 | 1 | 0 | -0.75 | -264.86 | 0.05 | 2.0 | 0 |
| my_ema_cross_4h | 0 | 0 | 0 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 0 |
| my_ema_rsi_15m | 2 | 2 | 0 | 0 | -0.64 | -220.67 | 0.35 | 1.0 | 0 |
| my_ema_rsi_1d | 1 | 0 | 1 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 2 |
| my_ema_rsi_1h | 2 | 1 | 1 | 0 | -0.21 | -75.35 | 0.62 | 8.0 | 1 |
| my_ema_rsi_4h | 2 | 1 | 1 | 0 | +0.00 | +0.00 | 1.58 | 15.5 | 0 |
| my_intraday_mom | 2 | 2 | 0 | 0 | -0.16 | -57.20 | 0.27 | 0.5 | 0 |
| my_rsi_15m | 0 | 0 | 0 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 0 |
| my_rsi_1h | 0 | 0 | 0 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 0 |
| my_rsi_4h | 1 | 1 | 0 | 0 | -0.71 | -248.65 | 0.38 | 8.0 | 0 |
| playbook_allhours | 6 | 6 | 0 | 4 | -0.21 | -281.26 | 1.11 | 0.5 | 4 |
| playbook_nobias | 5 | 5 | 0 | 2 | -2.12 | -724.63 | 0.76 | 1.0 | 2 |
| playbook_regime | 3 | 3 | 0 | 1 | -1.51 | -557.33 | 0.83 | 0.6 | 1 |
| shadow | 6 | 6 | 0 | 2 | -1.87 | -658.73 | 0.79 | 0.7 | 2 |

All listed books: 31 closed trades, -10.26 R.

## 2. Why the losing trades lost

| Cause | Trades | R |
|---|---|---|
| gave back: was +0.5R or better first | 13 | -9.75 |
| stopped at the first stop | 6 | -3.09 |
| closed on the EMA exit at a loss | 2 | -1.46 |

## 3. Skipped signals (what the filters blocked)

**live**: 8x skipped: Jev quality # < #; 2x filtered: counter to BEARISH bias; 2x skipped: Jev quality # < # and confidence # < #; 1x taken: qty #, risk $#, cost #R; 1x skipped: Jev confidence # < #
**ema21_rsi55**: 1x rejected: choppy market (CHOP # ≥ #); 1x taken: qty #, jev #
**my_ema_cross_15m**: 2x rejected: not a fresh cross (the price has been above the EMA# for # candles, limit #; 2x rejected: not a fresh cross (the price has been below the EMA# for # candles, limit #; 2x rejected: stop too wide (# ATR); 2x rejected: choppy market (CHOP # ≥ #); 1x taken: qty #, jev #
**my_ema_cross_1h**: 3x rejected: stop too wide (# ATR); 2x taken: qty #, jev #; 1x rejected: not a fresh cross (the price has been above the EMA# for # candles, limit #; 1x rejected: against the #h trend (bearish) - no buy
**my_ema_rsi_15m**: 5x rejected: not a fresh cross (the price has been above the EMA# for # candles, limit #; 5x rejected: not a fresh cross (the price has been below the EMA# for # candles, limit #; 4x rejected: against the #h trend (bearish) - no buy; 3x rejected: choppy market (CHOP # ≥ #); 2x rejected: stop too wide (# ATR); 2x taken: qty #, jev #
**my_ema_rsi_1h**: 2x taken: qty #, jev #; 2x rejected: against the #h trend (bearish) - no buy; 1x rejected: stop too wide (# ATR)
**my_ema_rsi_4h**: 2x taken: qty #, jev #
**my_intraday_mom**: 2x taken: qty #, jev None
**my_rsi_1h**: 2x rejected: stop too wide (# ATR); 1x rejected: RSI not falling (RSI #, # three candles ago) - no sell
**my_rsi_4h**: 1x taken: qty #, jev #
**playbook_allhours**: 20x skipped: Jev quality # < #; 9x filtered: counter to BEARISH bias; 6x taken: qty #, risk $#, cost #R; 5x rejected: outside entry windows; 5x rejected: cost #R of the stop (spread # vs stop #) > cap #R; 5x skipped: Jev confidence # < #; 2x skipped: Jev quality # < # and confidence # < #; 1x rejected: news blackout: Congressional Elections (high, before)
**playbook_nobias**: 28x skipped: Jev quality # < #; 9x rejected: outside entry windows; 5x skipped: Jev confidence # < #; 5x taken: qty #, risk $#, cost #R; 3x rejected: cost #R of the stop (spread # vs stop #) > cap #R; 2x skipped: playbook: XAUUSD has an opposite position (OANDA nets positions per instrum; 1x skipped: Jev quality # < # and confidence # < #
**playbook_regime**: 27x skipped: regime chop (Jev chop #, CHOP #): scalps only; 9x filtered: counter to BEARISH bias; 5x skipped: Jev quality # < #; 4x rejected: outside entry windows; 3x taken: qty #, risk $#, cost #R; 2x skipped: Jev confidence # < #; 2x skipped: Jev quality # < # and confidence # < #; 1x skipped: regime trend (Jev chop #, CHOP #): no scalps in a trend
**shadow**: 16x skipped: Jev quality # < #; 9x filtered: counter to BEARISH bias; 9x rejected: outside entry windows; 6x taken: qty #, risk $#, cost #R; 4x skipped: Jev confidence # < #; 3x rejected: cost #R of the stop (spread # vs stop #) > cap #R; 3x filtered: bias suspended; 2x skipped: Jev quality # < # and confidence # < #

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
| ema21_rsi55 | any_exit | 13 | -0.04 | 9 |
| ema21_rsi55 | giveback | 2 | +0.23 | 1 |
| ema21_rsi55 | h1_against | 11 | -0.12 | 7 |
| ema21_rsi55 | news_soon | 1 | +0.34 | 1 |
| ema21_rsi55 | stall | 10 | -0.15 | 7 |
| ema21_rsi55 | structure_break | 12 | +0.09 | 7 |
| ema21_rsi55 | trend_flip | 1 | +0.45 | 1 |
| h1_vol_trend | any_exit | 1 | -0.90 | 0 |
| h1_vol_trend | stall | 1 | -0.96 | 0 |
| h1_vol_trend | structure_break | 1 | -0.90 | 0 |
| my_ema_cross_15m | any_exit | 13 | +0.03 | 9 |
| my_ema_cross_15m | giveback | 2 | +0.19 | 2 |
| my_ema_cross_15m | h1_against | 17 | -0.02 | 11 |
| my_ema_cross_15m | stall | 5 | -0.07 | 2 |
| my_ema_cross_15m | structure_break | 13 | +0.06 | 9 |
| my_ema_cross_15m | trend_flip | 3 | -0.09 | 1 |
| my_ema_cross_1h | any_exit | 15 | +0.28 | 13 |
| my_ema_cross_1h | giveback | 1 | +0.12 | 1 |
| my_ema_cross_1h | h1_against | 5 | +0.50 | 5 |
| my_ema_cross_1h | news_soon | 1 | +0.16 | 1 |
| my_ema_cross_1h | stall | 10 | +0.38 | 10 |
| my_ema_cross_1h | structure_break | 15 | +0.24 | 12 |
| my_ema_cross_1h | trend_flip | 11 | +0.28 | 11 |
| my_ema_cross_4h | any_exit | 5 | -0.05 | 2 |
| my_ema_cross_4h | h1_against | 1 | +0.30 | 1 |
| my_ema_cross_4h | news_soon | 4 | +0.04 | 1 |
| my_ema_cross_4h | stall | 5 | -0.01 | 2 |
| my_ema_cross_4h | structure_break | 5 | +0.00 | 2 |
| my_ema_cross_4h | trend_flip | 3 | +0.37 | 3 |
| my_ema_rsi_15m | any_exit | 41 | -0.03 | 23 |
| my_ema_rsi_15m | giveback | 13 | +0.04 | 11 |
| my_ema_rsi_15m | h1_against | 35 | +0.10 | 22 |
| my_ema_rsi_15m | news_soon | 1 | +0.11 | 1 |
| my_ema_rsi_15m | stall | 17 | -0.01 | 9 |
| my_ema_rsi_15m | structure_break | 37 | -0.01 | 18 |
| my_ema_rsi_15m | trend_flip | 9 | +0.15 | 7 |
| my_ema_rsi_1d | any_exit | 1 | +0.19 | 1 |
| my_ema_rsi_1d | h1_against | 1 | +0.14 | 1 |
| my_ema_rsi_1d | news_soon | 1 | -0.04 | 0 |
| my_ema_rsi_1d | stall | 1 | +0.20 | 1 |
| my_ema_rsi_1d | structure_break | 1 | +0.19 | 1 |
| my_ema_rsi_1d | trend_flip | 1 | +0.30 | 1 |
| my_ema_rsi_1h | any_exit | 25 | +0.16 | 18 |
| my_ema_rsi_1h | giveback | 1 | +0.07 | 1 |
| my_ema_rsi_1h | h1_against | 4 | +0.39 | 4 |
| my_ema_rsi_1h | news_soon | 1 | -0.20 | 0 |
| my_ema_rsi_1h | stall | 17 | +0.25 | 13 |
| my_ema_rsi_1h | structure_break | 25 | +0.13 | 18 |
| my_ema_rsi_1h | trend_flip | 21 | +0.09 | 14 |
| my_ema_rsi_4h | any_exit | 7 | -0.11 | 3 |
| my_ema_rsi_4h | giveback | 2 | +0.55 | 2 |
| my_ema_rsi_4h | h1_against | 2 | -0.13 | 1 |
| my_ema_rsi_4h | news_soon | 1 | +0.28 | 1 |
| my_ema_rsi_4h | stall | 7 | -0.07 | 3 |
| my_ema_rsi_4h | structure_break | 7 | -0.14 | 2 |
| my_ema_rsi_4h | trend_flip | 6 | +0.00 | 5 |
| my_intraday_mom | any_exit | 12 | +0.16 | 8 |
| my_intraday_mom | h1_against | 6 | +0.20 | 5 |
| my_intraday_mom | structure_break | 12 | +0.16 | 8 |
| my_rsi_15m | any_exit | 7 | -0.07 | 4 |
| my_rsi_15m | giveback | 3 | -0.02 | 2 |
| my_rsi_15m | stall | 4 | -0.05 | 2 |
| my_rsi_15m | structure_break | 7 | -0.04 | 4 |
| my_rsi_1h | any_exit | 4 | +0.03 | 3 |
| my_rsi_1h | giveback | 1 | +0.29 | 1 |
| my_rsi_1h | stall | 3 | -0.10 | 2 |
| my_rsi_1h | structure_break | 4 | +0.03 | 3 |
| my_rsi_1h | trend_flip | 4 | -0.10 | 3 |
| my_rsi_4h | any_exit | 3 | +0.25 | 2 |
| my_rsi_4h | h1_against | 1 | +0.34 | 1 |
| my_rsi_4h | stall | 3 | +0.36 | 2 |
| my_rsi_4h | structure_break | 3 | +0.35 | 2 |
| my_rsi_4h | trend_flip | 2 | +0.55 | 2 |
| playbook_allhours | any_exit | 3 | +0.04 | 2 |
| playbook_allhours | giveback | 3 | +0.24 | 3 |
| playbook_allhours | h1_against | 1 | +0.86 | 1 |
| playbook_allhours | stall | 2 | -0.17 | 1 |
| playbook_allhours | structure_break | 3 | +0.04 | 2 |
| playbook_allhours | trend_flip | 1 | +0.47 | 1 |
| playbook_nobias | any_exit | 2 | -0.38 | 1 |
| playbook_nobias | giveback | 4 | -0.14 | 3 |
| playbook_nobias | stall | 2 | -0.24 | 1 |
| playbook_nobias | structure_break | 1 | -1.25 | 0 |
| playbook_regime | any_exit | 2 | -0.02 | 1 |
| playbook_regime | giveback | 5 | -0.24 | 3 |
| playbook_regime | stall | 1 | -0.19 | 0 |
| playbook_regime | structure_break | 2 | -0.02 | 1 |
| shadow | any_exit | 24 | +0.08 | 15 |
| shadow | giveback | 9 | +0.08 | 8 |
| shadow | h1_against | 8 | -0.10 | 3 |
| shadow | stall | 14 | +0.06 | 8 |
| shadow | structure_break | 21 | +0.05 | 13 |
| shadow | trend_flip | 6 | +0.27 | 6 |

## 5. Every trade in the window

| Book | Id | Market | Side | Opened (NY) | Closed (NY) | Entry | Exit | First stop | Stop at end | Qty | P&L | R | Best R | Worst R | How it ended |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ema21_rsi55 | 23206262 | US30 | LONG | 11-03 08:30 | 11-03 09:45 | 51833.00 | 51690.10 | 51617.60 | 51617.60 | 0.32 | -45.73 | -0.66 | 0.66 | -0.92 | close_below_ema21 |
| live | 98980c45 | NDQ | SHORT | 11-03 02:05 | 11-03 02:29 | 27942.20 | 28008.00 | 28007.80 | 28007.80 | 4.89 | -321.76 | -1.00 | 0.22 | -0.71 | stop |
| my_ema_cross_15m | 55326160 | XAUUSD | LONG | 11-03 18:30 | 11-03 19:45 | 3931.01 | 3925.76 | 3918.13 | 3918.13 | 27.30 | -143.46 | -0.41 | 0.75 | -0.86 | close_past_ema21 |
| my_ema_cross_1h | 5ef199ec | NDQ | SHORT | 11-03 15:00 | 11-03 17:00 | 28154.60 | 28310.40 | 28361.70 | 28361.70 | 1.70 | -264.86 | -0.75 | 0.05 | -0.91 | close_past_ema21 |
| my_ema_cross_1h | be9b1346 | NDQ | SHORT | 11-03 20:00 | open | 28041.80 |  | 28441.20 | 27855.00 | 0.86 | 0.00 |  | 1.32 | -0.08 | OPEN |
| my_ema_rsi_15m | 9e0a5457 | NDQ | LONG | 11-03 09:45 | 11-03 10:14 | 28260.60 | 28215.00 | 28069.20 | 28069.20 | 1.84 | -83.90 | -0.24 | 0.07 | -0.65 | pre-news: Congressional Elections |
| my_ema_rsi_15m | ead5901e | XAUUSD | LONG | 11-03 18:15 | 11-03 19:45 | 3931.58 | 3925.76 | 3917.14 | 3917.14 | 23.50 | -136.77 | -0.40 | 0.63 | -0.81 | close_past_ema21 |
| my_ema_rsi_1d | 039ebc8c | NDQ | SHORT | 10-29 17:00 | open | 29086.80 |  | 30180.10 | 28977.50 | 0.32 | 186.26 |  | 1.06 | -0.01 | OPEN |
| my_ema_rsi_1h | aab3ff99 | XAUUSD | SHORT | 11-03 00:00 | 11-03 08:00 | 3923.33 | 3932.99 | 3968.40 | 3968.40 | 7.80 | -75.35 | -0.21 | 0.62 | -0.23 | close_past_ema21 |
| my_ema_rsi_1h | 77c8372b | NDQ | SHORT | 11-03 20:00 | open | 28041.80 |  | 28441.20 | 27855.00 | 0.85 | 118.52 |  | 1.32 | -0.08 | OPEN |
| my_ema_rsi_4h | 905fa495 | XAUUSD | SHORT | 11-02 17:00 | 11-03 08:30 | 3946.43 | 3946.43 | 3978.62 | 3946.43 | 11.00 | 0.00 | 0.00 | 1.58 | -0.57 | stop |
| my_ema_rsi_4h | 2dd4a33e | XAUUSD | SHORT | 11-03 13:00 | open | 3932.47 |  | 3980.25 | 3980.25 | 7.30 | 0.00 |  | 0.00 | 0.00 | OPEN |
| my_intraday_mom | 2bdbca2c | NDQ | LONG | 11-03 15:30 | 11-03 16:00 | 28208.20 | 28194.40 | 28012.60 | 28012.60 | 1.80 | -24.84 | -0.07 | 0.21 | -0.17 | session_close |
| my_intraday_mom | e88ef742 | US30 | SHORT | 11-03 15:30 | 11-03 16:00 | 51771.50 | 51790.10 | 51973.60 | 51973.60 | 1.74 | -32.36 | -0.09 | 0.32 | -0.14 | session_close |
| my_rsi_4h | 5f2228bf | XAUUSD | SHORT | 11-03 01:00 | 11-03 09:00 | 3918.28 | 3961.14 | 3978.43 | 3978.43 | 5.80 | -248.65 | -0.71 | 0.38 | -0.88 | close_past_ema21 |
| playbook_allhours | 73fff62a | NDQ | SHORT | 11-03 00:20 | 11-03 00:43 | 28029.80 | 28023.90 | 28088.80 | 28023.90 | 5.24 | 153.27 | 0.50 | 1.02 | -0.11 | breakeven_plus_stop |
| playbook_allhours | 085187a1 | NDQ | SHORT | 11-03 00:45 | 11-03 01:32 | 28009.00 | 28006.00 | 28038.90 | 28006.00 | 5.25 | 65.01 | 0.41 | 1.97 | -0.62 | breakeven_plus_stop |
| playbook_allhours | d89758d5 | NDQ | SHORT | 11-03 02:30 | 11-03 02:46 | 27999.20 | 27996.10 | 28029.90 | 27996.10 | 5.26 | 63.38 | 0.39 | 1.19 | -0.05 | breakeven_plus_stop |
| playbook_allhours | 57cc4dbe | XAUUSD | SHORT | 11-03 03:10 | 11-03 04:11 | 3905.41 | 3904.63 | 3913.27 | 3904.63 | 20.60 | 79.58 | 0.49 | 1.25 | -0.73 | breakeven_plus_stop |
| playbook_allhours | de392769 | NDQ | SHORT | 11-03 09:30 | 11-03 09:43 | 28153.80 | 28228.00 | 28228.00 | 28228.00 | 4.78 | -354.68 | -1.00 | 0.67 | -0.91 | stop |
| playbook_allhours | 6f56204a | NDQ | SHORT | 11-03 22:20 | 11-03 22:58 | 27609.00 | 27662.30 | 27662.30 | 27662.30 | 5.40 | -287.82 | -1.00 | 0.58 | -0.77 | stop |
| playbook_nobias | caf9966e | NDQ | SHORT | 11-03 02:30 | 11-03 02:46 | 27999.20 | 27996.10 | 28029.90 | 27996.10 | 5.24 | 63.14 | 0.39 | 1.19 | -0.05 | breakeven_plus_stop |
| playbook_nobias | 2b43b090 | XAUUSD | SHORT | 11-03 03:10 | 11-03 04:11 | 3905.41 | 3904.63 | 3913.27 | 3904.63 | 20.50 | 78.88 | 0.49 | 1.25 | -0.73 | breakeven_plus_stop |
| playbook_nobias | 1f6cace9 | XAUUSD | SHORT | 11-03 04:15 | 11-03 07:19 | 3900.41 | 3911.48 | 3911.48 | 3911.48 | 20.50 | -226.91 | -1.00 | 0.13 | -0.92 | stop |
| playbook_nobias | b50eb5aa | NDQ | SHORT | 11-03 09:30 | 11-03 09:43 | 28153.80 | 28228.00 | 28228.00 | 28228.00 | 4.75 | -352.45 | -1.00 | 0.67 | -0.91 | stop |
| playbook_nobias | 603f7e8e | NDQ | SHORT | 11-03 22:20 | 11-03 22:58 | 27609.00 | 27662.30 | 27662.30 | 27662.30 | 5.39 | -287.29 | -1.00 | 0.58 | -0.77 | stop |
| playbook_regime | e93156a6 | XAUUSD | SHORT | 11-03 03:10 | 11-03 04:11 | 3905.41 | 3904.63 | 3913.27 | 3904.63 | 20.50 | 78.88 | 0.49 | 1.25 | -0.73 | breakeven_plus_stop |
| playbook_regime | 9ab3d6f3 | NDQ | SHORT | 11-03 09:30 | 11-03 09:43 | 28153.80 | 28228.00 | 28228.00 | 28228.00 | 4.76 | -353.19 | -1.00 | 0.67 | -0.91 | stop |
| playbook_regime | 31900dd8 | NDQ | SHORT | 11-03 22:20 | 11-03 22:58 | 27609.00 | 27662.30 | 27662.30 | 27662.30 | 5.31 | -283.02 | -1.00 | 0.58 | -0.77 | stop |
| shadow | 05834e61 | NDQ | SHORT | 11-03 02:30 | 11-03 02:46 | 27999.20 | 27996.10 | 28029.90 | 27996.10 | 5.24 | 63.14 | 0.39 | 1.19 | -0.05 | breakeven_plus_stop |
| shadow | 9af84527 | XAUUSD | SHORT | 11-03 03:10 | 11-03 04:11 | 3905.41 | 3904.63 | 3913.27 | 3904.63 | 20.50 | 78.88 | 0.49 | 1.25 | -0.73 | breakeven_plus_stop |
| shadow | d079af5f | XAUUSD | SHORT | 11-03 04:15 | 11-03 04:46 | 3900.41 | 3908.04 | 3911.48 | 3911.48 | 20.50 | -156.31 | -0.69 | 0.12 | -0.87 | max_hold |
| shadow | c0938768 | NDQ | SHORT | 11-03 09:30 | 11-03 09:43 | 28153.80 | 28228.00 | 28228.00 | 28228.00 | 4.75 | -352.45 | -1.00 | 0.67 | -0.91 | stop |
| shadow | 3319e164 | NDQ | SHORT | 11-03 14:25 | 11-03 15:50 | 28225.60 | 28232.00 | 28328.80 | 28328.80 | 3.40 | -21.76 | -0.06 | 0.91 | -0.22 | session_flat |
| shadow | 75f552ed | NDQ | SHORT | 11-03 22:20 | 11-03 22:58 | 27609.00 | 27662.30 | 27662.30 | 27662.30 | 5.07 | -270.23 | -1.00 | 0.58 | -0.77 | stop |

## 6. Timelines of the losing and the open trades

- **live** NDQ SHORT 98980c45 → stop (-1.00R, best 0.22R): 02:05 entry (28007.8); 02:05 target_placed; 02:10 analyst (trade on track); 02:29 exit
- **ema21_rsi55** US30 LONG 23206262 → close_below_ema21 (-0.66R, best 0.66R): 08:30 entry (51617.600000000006); 08:30 analyst (1H trend is against the trade); 09:30 analyst (15m trend flipped against the trade; 1H trend is); 09:35 analyst (15m trend flipped against the trade; 5m structur); 09:45 exit_signal; 09:45 exit
- **my_ema_cross_15m** XAUUSD LONG 55326160 → close_past_ema21 (-0.41R, best 0.75R): 18:30 entry (3918.129); 18:30 mode (trend mode: CHOP 47.5 at entry); 18:30 analyst (1H trend is against the trade); 18:45 liq_line (liquidity lines fixed at entry); 19:00 analyst (trade on track); 19:35 analyst (5m structure broke); 19:45 exit_signal; 19:45 exit
- **my_ema_cross_1h** NDQ SHORT 5ef199ec → close_past_ema21 (-0.75R, best 0.05R): 15:00 entry (28361.7); 15:00 mode (range mode: CHOP 53.9 at entry); 15:00 analyst (trade on track); 15:30 analyst (15m trend flipped against the trade); 15:45 analyst (trade on track); 15:50 analyst (5m structure broke); 15:55 analyst (trade on track); 16:00 liq_line (liquidity lines fixed at entry); 16:10 analyst (stalled: no new best for 60 min and under +0.5R); 17:00 exit_signal; 17:00 exit
- **my_ema_cross_1h** NDQ SHORT be9b1346 → OPEN (R, best 1.32R): 20:00 entry (28441.2); 20:00 mode (range mode: CHOP 57.7 at entry); 20:00 analyst (trade on track); 21:00 liq_line (no liquidity line beyond 1R: book rules apply); 21:00 agent_check (continuation 0.47 ≥ 0.45); 21:00 stop_moved (breakeven / 2×ATR trail after +1R); 22:00 agent_check (continuation 0.47 ≥ 0.45); 22:00 stop_moved (breakeven / 2×ATR trail after +1R); 23:00 agent_check (continuation 0.48 ≥ 0.45); 23:00 stop_moved (breakeven / 2×ATR trail after +1R)
- **my_ema_rsi_15m** NDQ LONG 9e0a5457 → pre-news: Congressional Elections (-0.24R, best 0.07R): 09:45 entry (28069.2); 09:45 mode (trend mode: CHOP 42.9 at entry); 09:45 analyst (1H trend is against the trade); 10:00 liq_line (liquidity lines fixed at entry); 10:14 exit
- **my_ema_rsi_15m** XAUUSD LONG ead5901e → close_past_ema21 (-0.40R, best 0.63R): 18:15 entry (3917.136); 18:15 mode (trend mode: CHOP 45.8 at entry); 18:15 analyst (1H trend is against the trade); 18:30 liq_line (liquidity lines fixed at entry); 19:00 analyst (trade on track); 19:35 analyst (5m structure broke); 19:45 exit_signal; 19:45 exit
- **my_ema_rsi_1d** NDQ SHORT 039ebc8c → OPEN (R, best 1.06R): 17:00 entry (30180.100000000002); 17:00 analyst (trade on track); 20:10 analyst (stalled: no new best for 60 min and under +0.5R); 20:45 analyst (trade on track); 22:15 analyst (5m structure broke); 22:20 analyst (trade on track); 22:25 analyst (5m structure broke); 00:07 readopted (app restarted; position restored from the shadow); 07:05 analyst (trade on track); 09:00 analyst (5m structure broke); 09:05 analyst (trade on track); 10:00 analyst (5m structure broke); 10:05 analyst (trade on track); 11:30 analyst (stalled: no new best for 60 min and under +0.5R)
- **my_ema_rsi_1h** XAUUSD SHORT aab3ff99 → close_past_ema21 (-0.21R, best 0.62R): 00:00 entry (3968.399); 00:00 mode (range mode: CHOP 54.0 at entry); 00:00 analyst (trade on track); 01:00 liq_line (liquidity lines fixed at entry); 01:35 analyst (5m structure broke); 01:45 analyst (trade on track); 04:00 agent_check (continuation 0.45 ≥ 0.45); 05:10 analyst (stalled: no new best for 60 min and under +0.5R); 08:00 exit_signal; 08:00 exit
- **my_ema_rsi_1h** NDQ SHORT 77c8372b → OPEN (R, best 1.32R): 20:00 entry (28441.2); 20:00 mode (range mode: CHOP 57.7 at entry); 20:00 analyst (trade on track); 21:00 liq_line (no liquidity line beyond 1R: book rules apply); 21:00 partial (Jev: continuation 0.41 < 0.45); 21:00 stop_moved (breakeven / 2×ATR trail after +1R); 22:00 agent_check (continuation 0.45 ≥ 0.45); 22:00 stop_moved (breakeven / 2×ATR trail after +1R); 23:00 agent_check (continuation 0.47 ≥ 0.45); 23:00 stop_moved (breakeven / 2×ATR trail after +1R)
- **my_ema_rsi_4h** XAUUSD SHORT 2dd4a33e → OPEN (R, best 0.00R): 13:00 entry (3980.251); 13:00 mode (range mode: CHOP 54.9 at entry)
- **my_intraday_mom** NDQ LONG 2bdbca2c → session_close (-0.07R, best 0.21R): 15:30 entry (28012.600000000002); 15:30 analyst (1H trend is against the trade); 16:00 exit_signal (end of the 15:30-16:00 window); 16:00 exit
- **my_intraday_mom** US30 SHORT e88ef742 → session_close (-0.09R, best 0.32R): 15:30 entry (51973.600000000006); 15:30 analyst (trade on track); 16:00 exit_signal (end of the 15:30-16:00 window); 16:00 exit
- **my_rsi_4h** XAUUSD SHORT 5f2228bf → close_past_ema21 (-0.71R, best 0.38R): 01:00 entry (3978.434); 01:00 mode (trend mode: CHOP 44.0 at entry); 01:00 analyst (trade on track); 01:35 analyst (5m structure broke); 01:45 analyst (trade on track); 05:00 liq_line (no liquidity line beyond 1R: book rules apply); 05:10 analyst (stalled: no new best for 60 min and under +0.5R); 08:00 analyst (15m trend flipped against the trade; 5m structur); 09:00 exit_signal; 09:00 exit
- **playbook_allhours** NDQ SHORT de392769 → stop (-1.00R, best 0.67R): 09:30 entry (28228.0); 09:35 analyst (trade on track); 09:43 exit
- **playbook_allhours** NDQ SHORT 6f56204a → stop (-1.00R, best 0.58R): 22:20 entry (27662.3); 22:25 analyst (trade on track); 22:58 exit
- **playbook_nobias** XAUUSD SHORT 1f6cace9 → stop (-1.00R, best 0.13R): 04:15 entry (3911.484); 04:20 analyst (trade on track); 05:20 analyst (stalled: no new best for 60 min and under +0.5R); 07:10 analyst (trade on track); 07:19 exit
- **playbook_nobias** NDQ SHORT b50eb5aa → stop (-1.00R, best 0.67R): 09:30 entry (28228.0); 09:35 analyst (trade on track); 09:43 exit
- **playbook_nobias** NDQ SHORT 603f7e8e → stop (-1.00R, best 0.58R): 22:20 entry (27662.3); 22:25 analyst (trade on track); 22:58 exit
- **playbook_regime** NDQ SHORT 9ab3d6f3 → stop (-1.00R, best 0.67R): 09:30 entry (28228.0); 09:35 analyst (trade on track); 09:43 exit
- **playbook_regime** NDQ SHORT 31900dd8 → stop (-1.00R, best 0.58R): 22:20 entry (27662.3); 22:25 analyst (trade on track); 22:58 exit
- **shadow** XAUUSD SHORT d079af5f → max_hold (-0.69R, best 0.12R): 04:15 entry (3911.484); 04:20 analyst (trade on track); 04:46 exit
- **shadow** NDQ SHORT c0938768 → stop (-1.00R, best 0.67R): 09:30 entry (28228.0); 09:35 analyst (trade on track); 09:43 exit
- **shadow** NDQ SHORT 3319e164 → session_flat (-0.06R, best 0.91R): 14:25 entry (28328.8); 14:30 analyst (trade on track); 15:30 analyst (15m trend flipped against the trade); 15:45 analyst (trade on track); 15:50 exit
- **shadow** NDQ SHORT 75f552ed → stop (-1.00R, best 0.58R): 22:20 entry (27662.3); 22:25 analyst (trade on track); 22:58 exit

## 7. Entry reasons of every trade

- ema21_rsi55 23206262 US30 LONG: EMA21+RSI55: 15m close 51831.50 > EMA21 51708.35, RSI 59.2
- live 98980c45 NDQ SHORT: Inverse FVG retest
- my_ema_cross_15m 55326160 XAUUSD LONG: my_ema_cross_15m: 15min close 3930.70 > EMA21 3927.54, RSI 54.9, CHOP 47, Supertrend down
- my_ema_cross_1h 5ef199ec NDQ SHORT: my_ema_cross_1h: 1h close 28155.80 < EMA21 28205.32, RSI 44.7, CHOP 54, Supertrend down
- my_ema_cross_1h be9b1346 NDQ SHORT: my_ema_cross_1h: 1h close 28043.00 < EMA21 28198.79, RSI 40.1, CHOP 58, Supertrend down
- my_ema_rsi_15m 9e0a5457 NDQ LONG: my_ema_rsi_15m: 15min close 28259.40 > EMA21 28143.06, RSI 64.7, CHOP 43, Supertrend up
- my_ema_rsi_15m ead5901e XAUUSD LONG: my_ema_rsi_15m: 15min close 3931.27 > EMA21 3927.23, RSI 55.9, CHOP 46, Supertrend down
- my_ema_rsi_1d 039ebc8c NDQ SHORT: my_ema_rsi_1d: 1D close 29088.00 < EMA21 29776.40, RSI 39.9, CHOP 49, Supertrend down
- my_ema_rsi_1h aab3ff99 XAUUSD SHORT: my_ema_rsi_1h: 1h close 3923.64 < EMA21 3937.41, RSI 43.3, CHOP 54, Supertrend up
- my_ema_rsi_1h 77c8372b NDQ SHORT: my_ema_rsi_1h: 1h close 28043.00 < EMA21 28198.79, RSI 40.1, CHOP 58, Supertrend down
- my_ema_rsi_4h 905fa495 XAUUSD SHORT: my_ema_rsi_4h: 4h close 3946.74 < EMA21 3967.76, RSI 43.0, CHOP 41, Supertrend down
- my_ema_rsi_4h 2dd4a33e XAUUSD SHORT: my_ema_rsi_4h: 4h close 3932.78 < EMA21 3955.23, RSI 43.9, CHOP 55, Supertrend down
- my_intraday_mom 2bdbca2c NDQ LONG: my_intraday_mom: first half-hour +0.533% (16:00 close 28026.40 -> 10:00 28175.80) -> long 15:30-16:00
- my_intraday_mom e88ef742 US30 SHORT: my_intraday_mom: first half-hour -0.631% (16:00 close 52028.00 -> 10:00 51699.60) -> short 15:30-16:00
- my_rsi_4h 5f2228bf XAUUSD SHORT: my_rsi_4h: 4h close 3918.59 < EMA21 3961.89, RSI 38.4, CHOP 44, Supertrend down
- playbook_allhours 73fff62a NDQ SHORT: DTFX close_origin BOS → origin zone touch · playbook confirm=touch/std p=0.53
- playbook_allhours 085187a1 NDQ SHORT: DTFX close_origin BOS → origin zone touch · playbook confirm=touch/std p=0.53
- playbook_allhours d89758d5 NDQ SHORT: DTFX close_origin BOS → origin zone touch · playbook confirm=touch/std p=0.53
- playbook_allhours 57cc4dbe XAUUSD SHORT: Silver Bullet (all): displacement FVG retrace · playbook require_sweep=False/std p=0.55
- playbook_allhours de392769 NDQ SHORT: DTFX close_origin flip → origin zone touch · playbook confirm=touch/std p=0.53
- playbook_allhours 6f56204a NDQ SHORT: DTFX close_origin BOS → origin zone touch · playbook confirm=touch/std p=0.53
- playbook_nobias caf9966e NDQ SHORT: DTFX close_origin BOS → origin zone touch · playbook confirm=touch/std p=0.53
- playbook_nobias 2b43b090 XAUUSD SHORT: Silver Bullet (all): displacement FVG retrace · playbook require_sweep=False/std p=0.55
- playbook_nobias 1f6cace9 XAUUSD SHORT: DTFX wick_fib BOS → 50% rejection · playbook default/std p=0.56
- playbook_nobias b50eb5aa NDQ SHORT: DTFX close_origin flip → origin zone touch · playbook confirm=touch/std p=0.53
- playbook_nobias 603f7e8e NDQ SHORT: DTFX close_origin BOS → origin zone touch · playbook confirm=touch/std p=0.53
- playbook_regime e93156a6 XAUUSD SHORT: Silver Bullet (all): displacement FVG retrace · playbook require_sweep=False/std p=0.55
- playbook_regime 9ab3d6f3 NDQ SHORT: DTFX close_origin flip → origin zone touch · playbook confirm=touch/std p=0.53
- playbook_regime 31900dd8 NDQ SHORT: DTFX close_origin BOS → origin zone touch · playbook confirm=touch/std p=0.53
- shadow 05834e61 NDQ SHORT: DTFX close_origin BOS → origin zone touch · playbook confirm=touch/std p=0.53
- shadow 9af84527 XAUUSD SHORT: Silver Bullet (all): displacement FVG retrace · playbook require_sweep=False/std p=0.55
- shadow d079af5f XAUUSD SHORT: DTFX wick_fib BOS → 50% rejection · playbook default/scalp p=0.51
- shadow c0938768 NDQ SHORT: DTFX close_origin flip → origin zone touch · playbook confirm=touch/std p=0.53
- shadow 3319e164 NDQ SHORT: DTFX close_origin flip → origin zone touch · playbook confirm=touch/std p=0.53
- shadow 75f552ed NDQ SHORT: DTFX close_origin BOS → origin zone touch · playbook confirm=touch/std p=0.53
