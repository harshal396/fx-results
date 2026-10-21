# RSI / EMA books report

Generated 2026-10-21 13:09 New York. Window: since 2026-10-20 07:09 (30 h). R = profit as a multiple of the risk at the first stop.

Books read: ema21_rsi55, my_ema_cross_15m, my_ema_cross_1d, my_ema_cross_1h, my_ema_cross_4h, my_ema_rsi_15m, my_ema_rsi_1d, my_ema_rsi_1h, my_ema_rsi_4h, my_rsi_15m, my_rsi_1h, my_rsi_4h

## 1. Per book

| Book | Trades | Closed | Open | Wins | Total R | P&L | Avg best R | Avg hours held | Jev partials |
|---|---|---|---|---|---|---|---|---|---|
| ema21_rsi55 | 5 | 4 | 1 | 2 | +0.39 | +26.72 | 0.73 | 2.9 | 0 |
| my_ema_cross_15m | 1 | 1 | 0 | 0 | -0.75 | -262.10 | 0.23 | 0.2 | 0 |
| my_ema_cross_1d | 0 | 0 | 0 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 0 |
| my_ema_cross_1h | 1 | 0 | 1 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 0 |
| my_ema_cross_4h | 0 | 0 | 0 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 0 |
| my_ema_rsi_15m | 10 | 10 | 0 | 1 | -4.24 | -1478.50 | 0.34 | 1.0 | 1 |
| my_ema_rsi_1d | 0 | 0 | 0 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 0 |
| my_ema_rsi_1h | 4 | 2 | 2 | 1 | -0.03 | -12.73 | 1.12 | 1.7 | 1 |
| my_ema_rsi_4h | 1 | 1 | 0 | 0 | -0.36 | -126.06 | 0.05 | 4.0 | 0 |
| my_rsi_15m | 1 | 1 | 0 | 0 | -0.31 | -110.36 | 0.41 | 2.0 | 0 |
| my_rsi_1h | 0 | 0 | 0 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 0 |
| my_rsi_4h | 0 | 0 | 0 | 0 | +0.00 | +0.00 | 0.00 | 0.0 | 0 |

All listed books: 19 closed trades, -5.30 R.

## 2. Why the losing trades lost

| Cause | Trades | R |
|---|---|---|
| closed on the EMA exit at a loss | 12 | -5.35 |
| stopped at the first stop | 2 | -1.54 |
| gave back: was +0.5R or better first | 1 | -0.75 |

## 3. Skipped signals (what the filters blocked)

**ema21_rsi55**: 4x taken: qty #, jev #; 4x rejected: choppy market (CHOP # ≥ #)
**my_ema_cross_15m**: 6x rejected: stop too wide (# ATR); 3x rejected: choppy market (CHOP # ≥ #); 1x taken: qty #, jev #
**my_ema_cross_1h**: 1x taken: qty #, jev #
**my_ema_rsi_15m**: 10x taken: qty #, jev #; 9x rejected: choppy market (CHOP # ≥ #); 4x rejected: stop too wide (# ATR); 1x rejected: trading halted: daily loss limit hit ($#,#)
**my_ema_rsi_1h**: 4x taken: qty #, jev #; 2x rejected: choppy market (CHOP # ≥ #)
**my_ema_rsi_4h**: 1x taken: qty #, jev #; 1x rejected: stop too wide (# ATR)
**my_rsi_15m**: 1x taken: qty #, jev #

## 4. Trade analyst (shadow) - how its advice scored

| Book | Check | Times | Avg value in R (positive = its advice would have helped) | Helpful |
|---|---|---|---|---|
| ema21_rsi55 | any_exit | 2 | -0.05 | 0 |
| ema21_rsi55 | giveback | 1 | -0.05 | 0 |
| ema21_rsi55 | h1_against | 3 | -0.07 | 2 |
| ema21_rsi55 | stall | 1 | +0.09 | 1 |
| ema21_rsi55 | structure_break | 2 | -0.05 | 0 |
| my_ema_cross_15m | h1_against | 1 | +0.69 | 1 |
| my_ema_rsi_15m | any_exit | 4 | +0.19 | 2 |
| my_ema_rsi_15m | h1_against | 7 | +0.38 | 6 |
| my_ema_rsi_15m | structure_break | 4 | +0.04 | 1 |
| my_ema_rsi_15m | trend_flip | 2 | +0.46 | 2 |
| my_ema_rsi_1h | any_exit | 1 | +0.63 | 1 |
| my_ema_rsi_1h | structure_break | 1 | +0.63 | 1 |
| my_ema_rsi_1h | trend_flip | 1 | +0.21 | 1 |
| my_ema_rsi_4h | any_exit | 1 | +0.25 | 1 |
| my_ema_rsi_4h | h1_against | 1 | +0.12 | 1 |
| my_ema_rsi_4h | stall | 1 | +0.25 | 1 |
| my_ema_rsi_4h | structure_break | 1 | -0.02 | 0 |
| my_ema_rsi_4h | trend_flip | 1 | +0.05 | 1 |

## 5. Every trade in the window

| Book | Id | Market | Side | Opened (NY) | Closed (NY) | Entry | Exit | First stop | Stop at end | Qty | P&L | R | Best R | Worst R | How it ended |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ema21_rsi55 | b160b78d | XAUUSD | SHORT | 10-20 03:15 | 10-20 08:00 | 4128.85 | 4124.66 | 4148.94 | 4148.94 | 3.40 | 14.25 | 0.21 | 0.86 | -0.31 | close_above_ema21 |
| ema21_rsi55 | 34fad936 | XAUUSD | SHORT | 10-20 08:15 | 10-20 08:45 | 4114.57 | 4124.02 | 4133.69 | 4133.69 | 3.60 | -34.00 | -0.49 | 0.10 | -0.67 | close_above_ema21 |
| ema21_rsi55 | 47e4a5fe | US30 | LONG | 10-20 09:45 | 10-20 15:50 | 52259.50 | 52497.50 | 52005.10 | 52005.10 | 0.27 | 64.26 | 0.94 | 1.90 | -0.17 | session_flat |
| ema21_rsi55 | 360d73d9 | XAUUSD | LONG | 10-21 10:30 | 10-21 10:45 | 4133.75 | 4128.36 | 4112.97 | 4112.97 | 3.30 | -17.79 | -0.26 | 0.08 | -0.28 | close_below_ema21 |
| ema21_rsi55 | 06f5c168 | US30 | LONG | 10-21 11:30 | open | 52653.50 |  | 52421.20 | 52421.20 | 0.30 | 0.00 |  | 0.00 | 0.00 | OPEN |
| my_ema_cross_15m | 329cfa75 | XAUUSD | LONG | 10-21 00:15 | 10-21 00:30 | 4123.52 | 4114.69 | 4111.69 | 4111.69 | 29.70 | -262.10 | -0.75 | 0.23 | -0.72 | close_past_ema21 |
| my_ema_cross_1h | 51b67f4a | XAUUSD | LONG | 10-21 08:00 | open | 4140.24 |  | 4107.77 | 4107.77 | 10.80 | 0.00 |  | 0.00 | 0.00 | OPEN |
| my_ema_rsi_15m | 04035270 | XAUUSD | LONG | 10-21 00:15 | 10-21 00:30 | 4123.52 | 4114.69 | 4111.69 | 4111.69 | 29.70 | -262.10 | -0.75 | 0.23 | -0.72 | close_past_ema21 |
| my_ema_rsi_15m | 808ad62e | US30 | LONG | 10-21 00:15 | 10-21 02:15 | 52594.00 | 52563.00 | 52495.20 | 52495.20 | 3.56 | -110.36 | -0.31 | 0.41 | -0.37 | close_past_ema21 |
| my_ema_rsi_15m | 55bafc24 | NDQ | SHORT | 10-21 01:45 | 10-21 03:30 | 29691.20 | 29762.20 | 29817.30 | 29817.30 | 2.78 | -197.38 | -0.56 | 0.32 | -0.56 | close_past_ema21 |
| my_ema_rsi_15m | d06c07f7 | XAUUSD | LONG | 10-21 04:00 | 10-21 05:00 | 4124.39 | 4119.27 | 4109.19 | 4109.19 | 22.90 | -117.36 | -0.34 | 0.04 | -0.44 | close_past_ema21 |
| my_ema_rsi_15m | 4d2e09aa | US30 | SHORT | 10-21 04:45 | 10-21 05:45 | 52506.00 | 52572.00 | 52593.80 | 52593.80 | 3.97 | -262.02 | -0.75 | 0.69 | -0.91 | close_past_ema21 |
| my_ema_rsi_15m | 44a047a0 | NDQ | SHORT | 10-21 06:00 | 10-21 07:15 | 29636.00 | 29684.80 | 29769.80 | 29769.80 | 2.59 | -126.39 | -0.36 | 0.49 | -0.60 | close_past_ema21 |
| my_ema_rsi_15m | 811a7272 | XAUUSD | SHORT | 10-21 06:15 | 10-21 06:30 | 4114.60 | 4120.84 | 4127.36 | 4127.36 | 27.20 | -169.59 | -0.49 | 0.22 | -0.51 | close_past_ema21 |
| my_ema_rsi_15m | 9789444a | XAUUSD | LONG | 10-21 06:45 | 10-21 08:45 | 4128.82 | 4126.60 | 4110.28 | 4110.28 | 18.60 | 79.70 | 0.23 | 0.71 | -0.24 | close_past_ema21 |
| my_ema_rsi_15m | eec6c18c | NDQ | LONG | 10-21 08:30 | 10-21 08:45 | 29731.60 | 29682.80 | 29597.30 | 29597.30 | 2.58 | -125.90 | -0.36 | 0.04 | -0.40 | close_past_ema21 |
| my_ema_rsi_15m | 54bd333c | XAUUSD | LONG | 10-21 09:15 | 10-21 09:59 | 4136.73 | 4129.16 | 4122.77 | 4122.77 | 24.70 | -187.10 | -0.54 | 0.29 | -0.55 | flatten: daily loss limit hit ($-1,471) |
| my_ema_rsi_1h | b3c8df3d | NDQ | LONG | 10-21 04:00 | 10-21 04:53 | 29750.20 | 29624.40 | 29624.40 | 29624.40 | 2.80 | -352.24 | -1.00 | 0.05 | -0.97 | stop |
| my_ema_rsi_1h | 34bcbd4d | US30 | LONG | 10-21 07:00 | 10-21 09:32 | 52542.00 | 52555.00 | 52419.40 | 52555.00 | 2.85 | 339.51 | 0.97 | 2.20 | -0.03 | stop |
| my_ema_rsi_1h | af5bfde1 | XAUUSD | LONG | 10-21 08:00 | open | 4140.24 |  | 4107.77 | 4107.77 | 10.80 | 0.00 |  | 0.00 | 0.00 | OPEN |
| my_ema_rsi_1h | c33f7974 | US30 | LONG | 10-21 12:00 | open | 52683.10 |  | 52392.50 | 52392.50 | 1.21 | 0.00 |  | 0.00 | 0.00 | OPEN |
| my_ema_rsi_4h | 1d0da771 | NDQ | SHORT | 10-21 05:00 | 10-21 09:00 | 29586.80 | 29701.40 | 29906.40 | 29906.40 | 1.10 | -126.06 | -0.36 | 0.05 | -0.49 | close_past_ema21 |
| my_rsi_15m | 20a09f69 | US30 | LONG | 10-21 00:15 | 10-21 02:15 | 52594.00 | 52563.00 | 52495.20 | 52495.20 | 3.56 | -110.36 | -0.31 | 0.41 | -0.37 | close_past_ema21 |

## 6. Timelines of the losing and the open trades

- **ema21_rsi55** XAUUSD SHORT 34fad936 → close_above_ema21 (-0.49R, best 0.10R): 08:15 entry (4133.691); 08:15 analyst (trade on track); 08:45 exit_signal; 08:45 exit
- **ema21_rsi55** XAUUSD LONG 360d73d9 → close_below_ema21 (-0.26R, best 0.08R): 10:30 entry (4112.97); 10:30 analyst (1H trend is against the trade); 10:45 exit_signal; 10:45 exit
- **ema21_rsi55** US30 LONG 06f5c168 → OPEN (R, best 0.00R): 11:30 entry (52421.200000000004)
- **my_ema_cross_15m** XAUUSD LONG 329cfa75 → close_past_ema21 (-0.75R, best 0.23R): 00:15 entry (4111.694); 00:15 analyst (1H trend is against the trade); 00:30 exit_signal; 00:30 exit
- **my_ema_cross_1h** XAUUSD LONG 51b67f4a → OPEN (R, best 0.00R): 08:00 entry (4107.773)
- **my_ema_rsi_15m** XAUUSD LONG 04035270 → close_past_ema21 (-0.75R, best 0.23R): 00:15 entry (4111.694); 00:15 analyst (1H trend is against the trade); 00:30 exit_signal; 00:30 exit
- **my_ema_rsi_15m** US30 LONG 808ad62e → close_past_ema21 (-0.31R, best 0.41R): 00:15 entry (52495.200000000004); 00:15 analyst (trade on track); 02:15 exit_signal; 02:15 exit
- **my_ema_rsi_15m** NDQ SHORT 55bafc24 → close_past_ema21 (-0.56R, best 0.32R): 01:45 entry (29817.300000000003); 01:45 analyst (1H trend is against the trade); 03:15 analyst (15m trend flipped against the trade; 5m structur); 03:30 exit_signal; 03:30 exit
- **my_ema_rsi_15m** XAUUSD LONG d06c07f7 → close_past_ema21 (-0.34R, best 0.04R): 04:00 entry (4109.195); 04:00 analyst (1H trend is against the trade); 04:25 analyst (5m structure broke; 1H trend is against the trad); 04:30 analyst (1H trend is against the trade); 05:00 exit_signal; 05:00 exit
- **my_ema_rsi_15m** US30 SHORT 4d2e09aa → close_past_ema21 (-0.75R, best 0.69R): 04:45 entry (52593.8); 04:45 analyst (1H trend is against the trade); 05:30 analyst (15m trend flipped against the trade; 1H trend is); 05:35 analyst (15m trend flipped against the trade; 5m structur); 05:45 exit_signal; 05:45 exit
- **my_ema_rsi_15m** NDQ SHORT 44a047a0 → close_past_ema21 (-0.36R, best 0.49R): 06:00 entry (29769.800000000003); 06:00 analyst (trade on track); 07:00 analyst (1H trend is against the trade); 07:05 analyst (5m structure broke; 1H trend is against the trad); 07:15 exit_signal; 07:15 exit
- **my_ema_rsi_15m** XAUUSD SHORT 811a7272 → close_past_ema21 (-0.49R, best 0.22R): 06:15 entry (4127.356); 06:15 analyst (trade on track); 06:30 exit_signal; 06:30 exit
- **my_ema_rsi_15m** NDQ LONG eec6c18c → close_past_ema21 (-0.36R, best 0.04R): 08:30 entry (29597.300000000003); 08:30 analyst (trade on track); 08:45 exit_signal; 08:45 exit
- **my_ema_rsi_15m** XAUUSD LONG 54bd333c → flatten: daily loss limit hit ($-1,471) (-0.54R, best 0.29R): 09:15 entry (4122.765); 09:15 analyst (1H trend is against the trade); 09:59 exit
- **my_ema_rsi_1h** NDQ LONG b3c8df3d → stop (-1.00R, best 0.05R): 04:00 entry (29624.4); 04:00 analyst (trade on track); 04:10 analyst (5m structure broke); 04:15 analyst (trade on track); 04:20 analyst (5m structure broke); 04:25 analyst (trade on track); 04:35 analyst (5m structure broke); 04:45 analyst (15m trend flipped against the trade; 5m structur); 04:53 exit
- **my_ema_rsi_1h** XAUUSD LONG af5bfde1 → OPEN (R, best 0.00R): 08:00 entry (4107.773)
- **my_ema_rsi_1h** US30 LONG c33f7974 → OPEN (R, best 0.00R): 12:00 entry (52392.5)
- **my_ema_rsi_4h** NDQ SHORT 1d0da771 → close_past_ema21 (-0.36R, best 0.05R): 05:00 entry (29906.4); 05:00 analyst (trade on track); 06:05 analyst (stalled: no new best for 60 min and under +0.5R); 06:20 analyst (trade on track); 07:00 analyst (1H trend is against the trade); 07:05 analyst (5m structure broke; 1H trend is against the trad); 07:15 analyst (15m trend flipped against the trade; 5m structur); 09:00 exit_signal; 09:00 exit
- **my_rsi_15m** US30 LONG 20a09f69 → close_past_ema21 (-0.31R, best 0.41R): 00:15 entry (52495.200000000004); 00:15 analyst (trade on track); 02:15 exit_signal; 02:15 exit

## 7. Entry reasons of every trade

- ema21_rsi55 b160b78d XAUUSD SHORT: EMA21+RSI45 short: 15m close 4129.16 < EMA21 4133.96, RSI 44.5
- ema21_rsi55 34fad936 XAUUSD SHORT: EMA21+RSI45 short: 15m close 4114.88 < EMA21 4122.61, RSI 39.4
- ema21_rsi55 47e4a5fe US30 LONG: EMA21+RSI55: 15m close 52258.00 > EMA21 52072.53, RSI 65.2
- ema21_rsi55 360d73d9 XAUUSD LONG: EMA21+RSI55: 15m close 4133.44 > EMA21 4129.89, RSI 55.0
- ema21_rsi55 06f5c168 US30 LONG: EMA21+RSI55: 15m close 52652.00 > EMA21 52595.07, RSI 55.7
- my_ema_cross_15m 329cfa75 XAUUSD LONG: my_ema_cross_15m: 15min close 4123.20 > EMA21 4119.24, RSI 55.2, CHOP 61, Supertrend down
- my_ema_cross_1h 51b67f4a XAUUSD LONG: my_ema_cross_1h: 1h close 4139.93 > EMA21 4123.87, RSI 59.6, CHOP 59, Supertrend down
- my_ema_rsi_15m 04035270 XAUUSD LONG: my_ema_rsi_15m: 15min close 4123.20 > EMA21 4119.24, RSI 55.2, CHOP 61, Supertrend down
- my_ema_rsi_15m 808ad62e US30 LONG: my_ema_rsi_15m: 15min close 52592.50 > EMA21 52547.42, RSI 61.6, CHOP 50, Supertrend up
- my_ema_rsi_15m 55bafc24 NDQ SHORT: my_ema_rsi_15m: 15min close 29692.40 < EMA21 29747.98, RSI 42.1, CHOP 38, Supertrend up
- my_ema_rsi_15m d06c07f7 XAUUSD LONG: my_ema_rsi_15m: 15min close 4124.08 > EMA21 4118.87, RSI 55.6, CHOP 61, Supertrend up
- my_ema_rsi_15m 4d2e09aa US30 SHORT: my_ema_rsi_15m: 15min close 52507.50 < EMA21 52555.01, RSI 40.9, CHOP 54, Supertrend down
- my_ema_rsi_15m 44a047a0 NDQ SHORT: my_ema_rsi_15m: 15min close 29637.20 < EMA21 29688.52, RSI 42.5, CHOP 53, Supertrend down
- my_ema_rsi_15m 811a7272 XAUUSD SHORT: my_ema_rsi_15m: 15min close 4114.91 < EMA21 4119.89, RSI 43.6, CHOP 60, Supertrend up
- my_ema_rsi_15m 9789444a XAUUSD LONG: my_ema_rsi_15m: 15min close 4128.52 > EMA21 4120.72, RSI 58.8, CHOP 60, Supertrend up
- my_ema_rsi_15m eec6c18c NDQ LONG: my_ema_rsi_15m: 15min close 29730.40 > EMA21 29688.10, RSI 55.8, CHOP 51, Supertrend down
- my_ema_rsi_15m 54bd333c XAUUSD LONG: my_ema_rsi_15m: 15min close 4136.43 > EMA21 4128.13, RSI 59.9, CHOP 44, Supertrend up
- my_ema_rsi_1h b3c8df3d NDQ LONG: my_ema_rsi_1h: 1h close 29749.00 > EMA21 29669.82, RSI 56.6, CHOP 51, Supertrend up
- my_ema_rsi_1h 34bcbd4d US30 LONG: my_ema_rsi_1h: 1h close 52540.50 > EMA21 52477.95, RSI 56.6, CHOP 61, Supertrend up
- my_ema_rsi_1h af5bfde1 XAUUSD LONG: my_ema_rsi_1h: 1h close 4139.93 > EMA21 4123.87, RSI 59.6, CHOP 59, Supertrend down
- my_ema_rsi_1h c33f7974 US30 LONG: my_ema_rsi_1h: 1h close 52681.60 > EMA21 52537.68, RSI 58.9, CHOP 56, Supertrend up
- my_ema_rsi_4h 1d0da771 NDQ SHORT: my_ema_rsi_4h: 4h close 29588.00 < EMA21 29688.22, RSI 43.6, CHOP 58, Supertrend down
- my_rsi_15m 20a09f69 US30 LONG: my_rsi_15m: 15min close 52592.50 > EMA21 52547.42, RSI 61.6, CHOP 50, Supertrend up
