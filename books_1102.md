# RSI / EMA books report

Generated 2026-11-02 22:30 New York. Window: since 2026-11-01 18:00 (29 h). R = profit as a multiple of the risk at the first stop.

Books read: live, c10_afternoon, daily_rsi2_adx2, ema21_rsi55, h1_vol_trend, my_ema_cross_15m, my_ema_cross_1d, my_ema_cross_1h, my_ema_cross_4h, my_ema_rsi_15m, my_ema_rsi_1d, my_ema_rsi_1h, my_ema_rsi_4h, my_intraday_mom, my_rsi_15m, my_rsi_1h, my_rsi_4h, playbook_allhours, playbook_nobias, playbook_regime, shadow

## 1. Per book

| Book | Trades | Closed | Open | Wins | Total R | P&L | Avg best R | Avg hours held | Jev partials |
|---|---|---|---|---|---|---|---|---|---|
| live | 0 | 0 | 0 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 0 |
| c10_afternoon | 0 | 0 | 0 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 0 |
| daily_rsi2_adx2 | 0 | 0 | 0 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 0 |
| ema21_rsi55 | 0 | 0 | 0 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 0 |
| h1_vol_trend | 0 | 0 | 0 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 0 |
| my_ema_cross_15m | 0 | 0 | 0 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 0 |
| my_ema_cross_1d | 0 | 0 | 0 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 0 |
| my_ema_cross_1h | 0 | 0 | 0 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 0 |
| my_ema_cross_4h | 1 | 1 | 0 | 1 | +0.62 | +214.61 | 1.38 | 92.8 | 1 |
| my_ema_rsi_15m | 0 | 0 | 0 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 0 |
| my_ema_rsi_1d | 1 | 0 | 1 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 2 |
| my_ema_rsi_1h | 0 | 0 | 0 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 0 |
| my_ema_rsi_4h | 3 | 2 | 1 | 2 | +1.78 | +618.06 | 1.77 | 96.8 | 3 |
| my_intraday_mom | 2 | 2 | 0 | 0 | -0.96 | -337.21 | 0.02 | 0.5 | 0 |
| my_rsi_15m | 0 | 0 | 0 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 0 |
| my_rsi_1h | 0 | 0 | 0 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 0 |
| my_rsi_4h | 1 | 1 | 0 | 1 | +0.69 | +239.57 | 1.38 | 92.8 | 2 |
| playbook_allhours | 1 | 1 | 0 | 1 | +0.11 | +37.96 | 0.39 | 0.6 | 0 |
| playbook_nobias | 1 | 1 | 0 | 1 | +0.11 | +37.96 | 0.39 | 0.6 | 0 |
| playbook_regime | 0 | 0 | 0 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 0 |
| shadow | 1 | 1 | 0 | 1 | +0.11 | +37.96 | 0.39 | 0.6 | 0 |

All listed books: 9 closed trades, +2.46 R.

## 2. Why the losing trades lost

| Cause | Trades | R |
|---|---|---|
| stopped at the first stop | 2 | -0.96 |

## 3. Skipped signals (what the filters blocked)

**live**: 1x skipped: Jev quality # < #
**my_ema_cross_15m**: 2x rejected: not a fresh cross (the price has been below the EMA# for # candles, limit #; 1x rejected: not a fresh cross (the price has been above the EMA# for # candles, limit #
**my_ema_rsi_15m**: 2x rejected: not a fresh cross (the price has been above the EMA# for # candles, limit #; 2x rejected: not a fresh cross (the price has been below the EMA# for # candles, limit #; 1x rejected: choppy market (CHOP # ≥ #)
**my_ema_rsi_4h**: 1x taken: qty #, jev #
**my_intraday_mom**: 2x taken: qty #, jev None
**playbook_allhours**: 3x skipped: Jev quality # < #; 2x skipped: a higher-expectancy playbook cell fired on this bar; 2x filtered: counter to BEARISH bias; 2x rejected: outside entry windows; 1x taken: qty #, risk $#, cost #R; 1x skipped: playbook: US# already has # position(s); 1x rejected: cost #R of the stop (spread # vs stop #) > cap #R
**playbook_nobias**: 5x skipped: Jev quality # < #; 2x skipped: a higher-expectancy playbook cell fired on this bar; 1x taken: qty #, risk $#, cost #R; 1x skipped: playbook: US# already has # position(s); 1x skipped: Jev confidence # < #; 1x rejected: outside entry windows; 1x rejected: cost #R of the stop (spread # vs stop #) > cap #R
**playbook_regime**: 10x skipped: regime chop (Jev chop #, CHOP #): scalps only; 2x filtered: counter to BEARISH bias
**shadow**: 3x skipped: Jev quality # < #; 2x skipped: a higher-expectancy playbook cell fired on this bar; 2x filtered: counter to BEARISH bias; 2x rejected: outside entry windows; 1x taken: qty #, risk $#, cost #R; 1x skipped: playbook: US# already has # position(s); 1x rejected: cost #R of the stop (spread # vs stop #) > cap #R

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
| my_ema_cross_4h | any_exit | 5 | -0.05 | 2 |
| my_ema_cross_4h | h1_against | 1 | +0.30 | 1 |
| my_ema_cross_4h | news_soon | 4 | +0.04 | 1 |
| my_ema_cross_4h | stall | 5 | -0.01 | 2 |
| my_ema_cross_4h | structure_break | 5 | +0.00 | 2 |
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
| my_ema_rsi_4h | any_exit | 6 | -0.12 | 3 |
| my_ema_rsi_4h | giveback | 1 | +0.43 | 1 |
| my_ema_rsi_4h | h1_against | 1 | +0.12 | 1 |
| my_ema_rsi_4h | news_soon | 1 | +0.28 | 1 |
| my_ema_rsi_4h | stall | 6 | -0.08 | 3 |
| my_ema_rsi_4h | structure_break | 6 | -0.15 | 2 |
| my_ema_rsi_4h | trend_flip | 5 | -0.08 | 4 |
| my_intraday_mom | any_exit | 12 | +0.16 | 8 |
| my_intraday_mom | h1_against | 5 | +0.23 | 4 |
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
| my_rsi_4h | any_exit | 2 | +0.09 | 1 |
| my_rsi_4h | h1_against | 1 | +0.34 | 1 |
| my_rsi_4h | stall | 2 | +0.10 | 1 |
| my_rsi_4h | structure_break | 2 | +0.23 | 1 |
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
| my_ema_cross_4h | 59f05cdd | NDQ | SHORT | 10-29 17:00 | 11-02 13:50 | 29086.80 | 28611.80 | 29795.40 | 28611.80 | 0.49 | 214.61 | 0.62 | 1.38 | -0.01 | stop |
| my_ema_rsi_1d | 039ebc8c | NDQ | SHORT | 10-29 17:00 | open | 29086.80 |  | 30180.10 | 29086.80 | 0.32 | 186.26 |  | 1.00 | -0.01 | OPEN |
| my_ema_rsi_4h | 4fe39add | XAUUSD | SHORT | 10-29 09:00 | 11-02 13:50 | 4020.48 | 3934.47 | 4089.85 | 3934.47 | 5.00 | 379.33 | 1.09 | 2.16 | -0.25 | stop |
| my_ema_rsi_4h | a24a45d7 | NDQ | SHORT | 10-29 17:00 | 11-02 13:50 | 29086.80 | 28611.80 | 29795.40 | 28611.80 | 0.49 | 238.73 | 0.69 | 1.38 | -0.01 | stop |
| my_ema_rsi_4h | 905fa495 | XAUUSD | SHORT | 11-02 17:00 | open | 3946.43 |  | 3978.62 | 3978.62 | 11.00 | 0.00 |  | 0.00 | 0.00 | OPEN |
| my_intraday_mom | 94dc55f5 | NDQ | LONG | 11-02 15:30 | 11-02 16:00 | 28152.80 | 28025.20 | 27899.50 | 27899.50 | 1.39 | -177.36 | -0.50 | 0.03 | -0.64 | session_close |
| my_intraday_mom | d1d909e1 | US30 | LONG | 11-02 15:30 | 11-02 16:00 | 52141.50 | 52026.50 | 51888.80 | 51888.80 | 1.39 | -159.85 | -0.46 | 0.01 | -0.51 | session_close |
| my_rsi_4h | 446c4319 | NDQ | SHORT | 10-29 17:00 | 11-02 13:50 | 29086.80 | 28611.80 | 29795.40 | 28611.80 | 0.49 | 239.57 | 0.69 | 1.38 | -0.01 | stop |
| playbook_allhours | 11917e56 | US30 | SHORT | 11-02 15:15 | 11-02 15:50 | 52145.10 | 52119.10 | 52386.00 | 52386.00 | 1.46 | 37.96 | 0.11 | 0.39 | -0.27 | session_flat |
| playbook_nobias | 904d3462 | US30 | SHORT | 11-02 15:15 | 11-02 15:50 | 52145.10 | 52119.10 | 52386.00 | 52386.00 | 1.46 | 37.96 | 0.11 | 0.39 | -0.27 | session_flat |
| shadow | 4ec419e9 | US30 | SHORT | 11-02 15:15 | 11-02 15:50 | 52145.10 | 52119.10 | 52386.00 | 52386.00 | 1.46 | 37.96 | 0.11 | 0.39 | -0.27 | session_flat |

## 6. Timelines of the losing and the open trades

- **my_ema_rsi_1d** NDQ SHORT 039ebc8c → OPEN (R, best 1.00R): 17:00 entry (30180.100000000002); 17:00 analyst (trade on track); 20:10 analyst (stalled: no new best for 60 min and under +0.5R); 20:45 analyst (trade on track); 22:15 analyst (5m structure broke); 22:20 analyst (trade on track); 22:25 analyst (5m structure broke); 00:07 readopted (app restarted; position restored from the shadow); 07:05 analyst (trade on track); 09:00 analyst (5m structure broke); 09:05 analyst (trade on track); 10:00 analyst (5m structure broke); 10:05 analyst (trade on track); 11:30 analyst (stalled: no new best for 60 min and under +0.5R)
- **my_ema_rsi_4h** XAUUSD SHORT 905fa495 → OPEN (R, best 0.00R): 17:00 entry (3978.62); 17:00 mode (trend mode: CHOP 41.3 at entry)
- **my_intraday_mom** NDQ LONG 94dc55f5 → session_close (-0.50R, best 0.03R): 15:30 entry (27899.5); 15:30 analyst (1H trend is against the trade); 15:35 analyst (5m structure broke; 1H trend is against the trad); 16:00 exit_signal (end of the 15:30-16:00 window); 16:00 exit
- **my_intraday_mom** US30 LONG d1d909e1 → session_close (-0.46R, best 0.01R): 15:30 entry (51888.8); 15:30 analyst (5m structure broke; 1H trend is against the trad); 16:00 exit_signal (end of the 15:30-16:00 window); 16:00 exit

## 7. Entry reasons of every trade

- my_ema_cross_4h 59f05cdd NDQ SHORT: my_ema_cross_4h: 4h close 29088.00 < EMA21 29475.53, RSI 34.0, CHOP 42, Supertrend down
- my_ema_rsi_1d 039ebc8c NDQ SHORT: my_ema_rsi_1d: 1D close 29088.00 < EMA21 29776.40, RSI 39.9, CHOP 49, Supertrend down
- my_ema_rsi_4h 4fe39add XAUUSD SHORT: my_ema_rsi_4h: 4h close 4020.79 < EMA21 4039.36, RSI 43.2, CHOP 55, Supertrend down
- my_ema_rsi_4h a24a45d7 NDQ SHORT: my_ema_rsi_4h: 4h close 29088.00 < EMA21 29475.53, RSI 34.0, CHOP 42, Supertrend down
- my_ema_rsi_4h 905fa495 XAUUSD SHORT: my_ema_rsi_4h: 4h close 3946.74 < EMA21 3967.76, RSI 43.0, CHOP 41, Supertrend down
- my_intraday_mom 94dc55f5 NDQ LONG: my_intraday_mom: first half-hour +0.583% (16:00 close 28407.40 -> 10:00 28573.00) -> long 15:30-16:00
- my_intraday_mom d1d909e1 US30 LONG: my_intraday_mom: first half-hour +1.114% (16:00 close 51778.00 -> 10:00 52355.00) -> long 15:30-16:00
- my_rsi_4h 446c4319 NDQ SHORT: my_rsi_4h: 4h close 29088.00 < EMA21 29475.53, RSI 34.0, CHOP 42, Supertrend down
- playbook_allhours 11917e56 US30 SHORT: DTFX close_fib BOS → 50-70% zone rejection · playbook level=50-70/trend p=0.51
- playbook_nobias 904d3462 US30 SHORT: DTFX close_fib BOS → 50-70% zone rejection · playbook level=50-70/trend p=0.51
- shadow 4ec419e9 US30 SHORT: DTFX close_fib BOS → 50-70% zone rejection · playbook level=50-70/trend p=0.51
