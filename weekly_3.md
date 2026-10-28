# Your weekly and daily rule books

Generated 2026-10-28 02:57 UTC. OANDA daily bid/ask, 5 years, markets XAUUSD,NDQ. Decisions on COMPLETED weeks / days only, executed at the next daily open (buy at the ask, sell at the bid). No stop, as specified. % = return on the price per trade, one unit, no leverage, no swap.

Reference, simply holding each market over the same period: XAUUSD +128%, NDQ +86%


## WEEKLY rule book, exit at the EMA21 (WK = your rule, WK0 = without the RSI condition, WK18 = reference with the old EMA exit)

### All markets together (% per trade)

| Variant | Trades | Win | Total % | Avg % per trade (95% interval) | PF | Deepest fall (%) |
|---|---|---|---|---|---|---|
| WK | 22 | 36% | +113.4 | +5.15 (-2.41..+16.96) | 2.96 | 16.7 |
| WK0 | 52 | 35% | +183.7 | +3.53 (-0.26..+8.94) | 3.36 | 20.2 |
| WK18 | 24 | 38% | +84.0 | +3.50 (-1.50..+10.28) | 2.47 | 15.9 |

### Markets we tuned other rules on (NDQ,US30,XAUUSD) versus markets we never looked at

| Variant | Tuned: trades | Tuned: total % | Tuned: avg | Untouched: trades | Untouched: total % | Untouched: avg (95% interval) |
|---|---|---|---|---|---|---|
| WK | 22 | +113.4 | +5.15 | 0 | +0.0 | +0.00 (+0.00..+0.00) |
| WK0 | 52 | +183.7 | +3.53 | 0 | +0.0 | +0.00 (+0.00..+0.00) |
| WK18 | 24 | +84.0 | +3.50 | 0 | +0.0 | +0.00 (+0.00..+0.00) |

### Build period versus holdout (entries after 2025-04-25)

| Variant | Build trades | Build total | Build avg | Holdout trades | Holdout total | Holdout avg |
|---|---|---|---|---|---|---|
| WK | 17 | +107.1 | +6.30 | 5 | +6.3 | +1.25 |
| WK0 | 37 | +150.1 | +4.06 | 15 | +33.5 | +2.24 |
| WK18 | 18 | +80.7 | +4.48 | 6 | +3.3 | +0.55 |

### Total % by market (trades)

| Variant | NDQ | XAUUSD |
|---|---|---|
| WK | +14.8 (13) | +98.6 (9) |
| WK0 | +57.5 (25) | +126.2 (27) |
| WK18 | +13.7 (14) | +70.3 (10) |

### Total % by year of entry

| Variant | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|
| WK | -9.0 | -9.7 | +133.6 | -2.9 | +4.7 | -3.4 |
| WK0 | -5.0 | +15.4 | +148.3 | -12.7 | +27.4 | +10.3 |
| WK18 | -9.0 | -7.0 | +39.6 | +62.0 | +6.2 | -7.9 |

### Long trades versus short trades

| Variant | Long trades | Long total % | Long avg | Short trades | Short total % | Short avg |
|---|---|---|---|---|---|---|
| WK | 13 | +143.9 | +11.07 | 9 | -30.6 | -3.40 |
| WK0 | 25 | +193.4 | +7.74 | 27 | -9.8 | -0.36 |
| WK18 | 15 | +113.8 | +7.59 | 9 | -29.8 | -3.31 |

### The same results in R (risk = distance from the entry to the exit EMA at entry; a stand-in, because these rules have no stop)

| Variant | Avg risk (% of price) | Total R | Avg R per trade (95% interval) | PF in R | Gold: total R | Silver: total R | NDQ: total R |
|---|---|---|---|---|---|---|---|
| WK | 6.3 | +31.0 | +1.41 (-0.40..+4.53) | 4.17 | +28.6 | +0.0 | +2.5 |
| WK0 | 1.5 | +154.8 | +2.98 (-0.51..+8.29) | 3.56 | +119.9 | +0.0 | +34.9 |
| WK18 | 5.9 | +20.4 | +0.85 (-0.26..+2.35) | 3.01 | +18.3 | +0.0 | +2.2 |

### How long, how much time in the market, and the worst dip inside a trade

| Variant | Avg days held | Time in the market | Avg worst dip inside a trade (%) | Worst dip of any trade (%) | Trades still open |
|---|---|---|---|---|---|
| WK | 85 | 72% | 4.2 | 10.6 | 1 |
| WK0 | 49 | 98% | 2.8 | 8.5 | 2 |
| WK18 | 76 | 70% | 4.2 | 10.6 | 1 |

## DAILY rule book, exit at the EMA21 (DY1 = your rule with the sell trigger at 42, DY3 = sell trigger at 40, DY18 = reference with the old EMA exit)

### All markets together (% per trade)

| Variant | Trades | Win | Total % | Avg % per trade (95% interval) | PF | Deepest fall (%) |
|---|---|---|---|---|---|---|
| DY1 | 56 | 29% | -0.8 | -0.01 (-1.18..+1.31) | 0.99 | 34.7 |
| DY3 | 53 | 32% | +14.3 | +0.27 (-1.00..+1.58) | 1.18 | 23.0 |
| DY18 | 59 | 31% | +2.1 | +0.03 (-0.93..+1.11) | 1.02 | 29.5 |

### Markets we tuned other rules on (NDQ,US30,XAUUSD) versus markets we never looked at

| Variant | Tuned: trades | Tuned: total % | Tuned: avg | Untouched: trades | Untouched: total % | Untouched: avg (95% interval) |
|---|---|---|---|---|---|---|
| DY1 | 56 | -0.8 | -0.01 | 0 | +0.0 | +0.00 (+0.00..+0.00) |
| DY3 | 53 | +14.3 | +0.27 | 0 | +0.0 | +0.00 (+0.00..+0.00) |
| DY18 | 59 | +2.1 | +0.03 | 0 | +0.0 | +0.00 (+0.00..+0.00) |

### Build period versus holdout (entries after 2025-04-25)

| Variant | Build trades | Build total | Build avg | Holdout trades | Holdout total | Holdout avg |
|---|---|---|---|---|---|---|
| DY1 | 38 | -4.0 | -0.10 | 18 | +3.1 | +0.17 |
| DY3 | 35 | +11.1 | +0.32 | 18 | +3.1 | +0.17 |
| DY18 | 39 | +3.1 | +0.08 | 20 | -1.1 | -0.05 |

### Total % by market (trades)

| Variant | NDQ | XAUUSD |
|---|---|---|
| DY1 | -12.9 (28) | +12.0 (28) |
| DY3 | -1.1 (27) | +15.4 (26) |
| DY18 | -8.6 (29) | +10.6 (30) |

### Total % by year of entry

| Variant | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|
| DY1 | -8.1 | -20.1 | +14.3 | +5.2 | +24.9 | -17.1 |
| DY3 | -8.1 | -5.8 | +15.1 | +5.2 | +24.9 | -17.1 |
| DY18 | -5.1 | -17.8 | +13.2 | +6.5 | +16.1 | -10.8 |

### Long trades versus short trades

| Variant | Long trades | Long total % | Long avg | Short trades | Short total % | Short avg |
|---|---|---|---|---|---|---|
| DY1 | 44 | +26.4 | +0.60 | 12 | -27.2 | -2.27 |
| DY3 | 44 | +26.4 | +0.60 | 9 | -12.1 | -1.34 |
| DY18 | 47 | +27.8 | +0.59 | 12 | -25.8 | -2.15 |

### The same results in R (risk = distance from the entry to the exit EMA at entry; a stand-in, because these rules have no stop)

| Variant | Avg risk (% of price) | Total R | Avg R per trade (95% interval) | PF in R | Gold: total R | Silver: total R | NDQ: total R |
|---|---|---|---|---|---|---|---|
| DY1 | 2.3 | +19.8 | +0.35 (-0.35..+1.20) | 1.49 | +11.9 | +0.0 | +7.9 |
| DY3 | 2.3 | +24.8 | +0.47 (-0.30..+1.37) | 1.70 | +14.7 | +0.0 | +10.1 |
| DY18 | 2.1 | +22.2 | +0.38 (-0.35..+1.21) | 1.52 | +9.9 | +0.0 | +12.3 |

### How long, how much time in the market, and the worst dip inside a trade

| Variant | Avg days held | Time in the market | Avg worst dip inside a trade (%) | Worst dip of any trade (%) | Trades still open |
|---|---|---|---|---|---|
| DY1 | 13 | 28% | 2.7 | 8.5 | 0 |
| DY3 | 14 | 28% | 2.6 | 8.5 | 0 |
| DY18 | 12 | 27% | 2.5 | 8.5 | 0 |

## EVERY trade of WK (22 trades, chronological within each market)

| Market | Side | Entry | Exit | Days | Result % | Risk % | R | Worst dip % | Ended |
|---|---|---|---|---|---|---|---|---|---|
| NDQ | long | 2021-12-12 | 2022-01-09 | 19 | -4.5 | 5.3 | -0.9 | 7.2 | EMA exit |
| NDQ | short | 2022-01-23 | 2022-04-03 | 50 | -3.0 | 7.8 | -0.4 | 5.9 | EMA exit |
| NDQ | short | 2022-04-24 | 2022-07-31 | 70 | +2.9 | 8.8 | +0.3 | 1.8 | EMA exit |
| NDQ | short | 2022-09-25 | 2022-12-04 | 50 | -6.1 | 11.5 | -0.5 | 7.2 | EMA exit |
| NDQ | long | 2023-04-02 | 2023-10-22 | 145 | +10.9 | 7.8 | +1.4 | 3.3 | EMA exit |
| NDQ | long | 2023-11-12 | 2024-04-21 | 112 | +10.1 | 4.8 | +2.1 | 0.8 | EMA exit |
| NDQ | long | 2024-05-12 | 2024-08-04 | 60 | +0.5 | 3.7 | +0.1 | 5.0 | EMA exit |
| NDQ | long | 2024-08-25 | 2024-09-08 | 10 | -6.8 | 4.2 | -1.6 | 7.2 | EMA exit |
| NDQ | long | 2024-10-13 | 2025-03-02 | 98 | +3.4 | 4.8 | +0.7 | 1.8 | EMA exit |
| NDQ | short | 2025-03-30 | 2025-05-04 | 24 | -5.0 | 7.6 | -0.7 | 5.5 | EMA exit |
| NDQ | long | 2025-06-29 | 2026-02-15 | 163 | +9.6 | 7.9 | +1.2 | 0.8 | EMA exit |
| NDQ | short | 2026-03-29 | 2026-04-12 | 10 | -7.9 | 7.0 | -1.1 | 10.6 | EMA exit |
| NDQ | long | 2026-04-19 | 2026-10-18 | 130 | +10.5 | 6.0 | +1.7 | 0.0 | EMA exit |
| XAUUSD | long | 2021-11-14 | 2021-11-28 | 10 | -4.5 | 3.8 | -1.2 | 5.4 | EMA exit |
| XAUUSD | long | 2022-02-20 | 2022-05-08 | 54 | -2.3 | 4.6 | -0.5 | 2.9 | EMA exit |
| XAUUSD | short | 2022-07-10 | 2022-11-13 | 90 | -1.3 | 6.4 | -0.2 | 3.9 | EMA exit |
| XAUUSD | long | 2023-01-08 | 2023-02-26 | 35 | -3.0 | 5.4 | -0.6 | 3.3 | EMA exit |
| XAUUSD | long | 2023-03-19 | 2023-06-25 | 69 | -3.2 | 7.4 | -0.4 | 3.9 | EMA exit |
| XAUUSD | short | 2023-10-01 | 2023-10-15 | 10 | -4.3 | 4.1 | -1.1 | 4.7 | EMA exit |
| XAUUSD | long | 2023-10-29 | 2026-03-22 | 617 | +123.1 | 3.7 | +33.2 | 3.6 | EMA exit |
| XAUUSD | short | 2026-06-21 | 2026-08-09 | 35 | -4.4 | 8.8 | -0.5 | 5.8 | EMA exit |
| XAUUSD | short | 2026-10-25 | 2026-10-26 | 1 | -1.6 | 7.2 | -0.2 | 1.7 | still open |

Worst 8: NDQ 2026-03-29 -7.9%; NDQ 2024-08-25 -6.8%; NDQ 2022-09-25 -6.1%; NDQ 2025-03-30 -5.0%; NDQ 2021-12-12 -4.5%; XAUUSD 2021-11-14 -4.5%; XAUUSD 2026-06-21 -4.4%; XAUUSD 2023-10-01 -4.3%

Best 8: XAUUSD 2023-10-29 +123.1%; NDQ 2023-04-02 +10.9%; NDQ 2026-04-19 +10.5%; NDQ 2023-11-12 +10.1%; NDQ 2025-06-29 +9.6%; NDQ 2024-10-13 +3.4%; NDQ 2022-04-24 +2.9%; NDQ 2024-05-12 +0.5%

## EVERY trade of WK0 (52 trades, chronological within each market)

| Market | Side | Entry | Exit | Days | Result % | Risk % | R | Worst dip % | Ended |
|---|---|---|---|---|---|---|---|---|---|
| NDQ | short | 2022-01-09 | 2022-04-03 | 60 | +4.8 | 1.0 | +4.8 | 2.7 | EMA exit |
| NDQ | long | 2022-04-03 | 2022-04-10 | 5 | -3.4 | 1.0 | -3.4 | 5.8 | EMA exit |
| NDQ | short | 2022-04-10 | 2022-07-31 | 79 | +9.7 | 2.6 | +3.7 | 0.2 | EMA exit |
| NDQ | long | 2022-07-31 | 2022-08-28 | 20 | -3.2 | 1.0 | -3.2 | 4.4 | EMA exit |
| NDQ | short | 2022-08-28 | 2022-12-04 | 70 | +4.4 | 3.0 | +1.5 | 2.7 | EMA exit |
| NDQ | long | 2022-12-04 | 2022-12-11 | 5 | -3.6 | 1.0 | -3.6 | 4.8 | EMA exit |
| NDQ | short | 2022-12-11 | 2023-01-22 | 28 | -0.4 | 2.7 | -0.2 | 5.8 | EMA exit |
| NDQ | long | 2023-01-22 | 2023-03-12 | 35 | +2.5 | 1.0 | +2.5 | 0.6 | EMA exit |
| NDQ | short | 2023-03-12 | 2023-03-19 | 5 | -6.0 | 1.0 | -6.0 | 6.6 | EMA exit |
| NDQ | long | 2023-03-19 | 2023-10-22 | 155 | +15.7 | 5.3 | +3.0 | 1.7 | EMA exit |
| NDQ | short | 2023-10-22 | 2023-11-05 | 10 | -3.7 | 1.0 | -3.7 | 4.1 | EMA exit |
| NDQ | long | 2023-11-05 | 2024-04-21 | 117 | +13.1 | 2.8 | +4.8 | 0.4 | EMA exit |
| NDQ | short | 2024-04-21 | 2024-04-28 | 5 | -3.8 | 1.2 | -3.2 | 4.3 | EMA exit |
| NDQ | long | 2024-04-28 | 2024-08-04 | 70 | +2.7 | 2.3 | +1.2 | 2.9 | EMA exit |
| NDQ | short | 2024-08-04 | 2024-08-18 | 10 | -7.1 | 2.9 | -2.5 | 8.5 | EMA exit |
| NDQ | long | 2024-08-18 | 2024-09-08 | 15 | -5.9 | 3.7 | -1.6 | 6.3 | EMA exit |
| NDQ | short | 2024-09-08 | 2024-09-15 | 5 | -6.1 | 2.8 | -2.2 | 6.4 | EMA exit |
| NDQ | long | 2024-09-15 | 2025-03-02 | 118 | +7.5 | 2.8 | +2.6 | 1.1 | EMA exit |
| NDQ | short | 2025-03-02 | 2025-05-04 | 44 | +4.1 | 1.0 | +4.1 | 0.6 | EMA exit |
| NDQ | long | 2025-05-04 | 2026-02-15 | 203 | +23.2 | 1.0 | +23.2 | 2.4 | EMA exit |
| NDQ | short | 2026-02-15 | 2026-02-22 | 5 | -1.0 | 1.0 | -1.0 | 1.3 | EMA exit |
| NDQ | long | 2026-02-22 | 2026-03-01 | 5 | -1.3 | 1.0 | -1.3 | 2.2 | EMA exit |
| NDQ | short | 2026-03-01 | 2026-04-12 | 30 | -0.6 | 1.1 | -0.6 | 3.2 | EMA exit |
| NDQ | long | 2026-04-12 | 2026-10-18 | 135 | +17.5 | 1.0 | +17.5 | 0.2 | EMA exit |
| NDQ | short | 2026-10-18 | 2026-10-26 | 6 | -1.7 | 1.0 | -1.7 | 2.7 | still open |
| XAUUSD | short | 2021-10-31 | 2021-11-07 | 5 | -2.0 | 1.0 | -2.0 | 2.5 | EMA exit |
| XAUUSD | long | 2021-11-07 | 2021-11-28 | 15 | -1.9 | 1.6 | -1.2 | 2.8 | EMA exit |
| XAUUSD | short | 2021-11-28 | 2021-12-19 | 15 | -0.9 | 1.0 | -0.9 | 1.7 | EMA exit |
| XAUUSD | long | 2021-12-19 | 2022-01-09 | 14 | -0.3 | 1.0 | -0.3 | 1.0 | EMA exit |
| XAUUSD | short | 2022-01-09 | 2022-01-16 | 5 | -1.3 | 1.0 | -1.3 | 1.9 | EMA exit |
| XAUUSD | long | 2022-01-16 | 2022-01-30 | 10 | -1.6 | 1.0 | -1.6 | 2.1 | EMA exit |
| XAUUSD | short | 2022-01-30 | 2022-02-06 | 5 | -1.1 | 1.0 | -1.1 | 1.9 | EMA exit |
| XAUUSD | long | 2022-02-06 | 2022-05-08 | 64 | +2.9 | 1.0 | +2.9 | 0.1 | EMA exit |
| XAUUSD | short | 2022-05-08 | 2022-11-13 | 135 | +5.4 | 1.5 | +3.5 | 1.1 | EMA exit |
| XAUUSD | long | 2022-11-13 | 2023-02-26 | 73 | +2.8 | 2.1 | +1.4 | 2.1 | EMA exit |
| XAUUSD | short | 2023-02-26 | 2023-03-05 | 5 | -2.3 | 1.0 | -2.3 | 2.6 | EMA exit |
| XAUUSD | long | 2023-03-05 | 2023-06-25 | 79 | +3.7 | 1.8 | +2.1 | 2.4 | EMA exit |
| XAUUSD | short | 2023-06-25 | 2023-07-16 | 15 | -1.7 | 1.0 | -1.7 | 2.1 | EMA exit |
| XAUUSD | long | 2023-07-16 | 2023-08-13 | 20 | -2.1 | 1.0 | -2.1 | 2.7 | EMA exit |
| XAUUSD | short | 2023-08-13 | 2023-09-03 | 15 | -1.4 | 1.3 | -1.1 | 2.1 | EMA exit |
| XAUUSD | long | 2023-09-03 | 2023-09-10 | 5 | -1.1 | 1.0 | -1.1 | 1.3 | EMA exit |
| XAUUSD | short | 2023-09-10 | 2023-10-15 | 25 | -0.4 | 1.0 | -0.4 | 1.5 | EMA exit |
| XAUUSD | long | 2023-10-15 | 2026-03-22 | 627 | +132.0 | 1.0 | +132.0 | 1.0 | EMA exit |
| XAUUSD | short | 2026-03-22 | 2026-04-05 | 9 | -3.8 | 3.1 | -1.2 | 7.4 | EMA exit |
| XAUUSD | long | 2026-04-05 | 2026-05-03 | 20 | -0.3 | 1.0 | -0.3 | 3.0 | EMA exit |
| XAUUSD | short | 2026-05-03 | 2026-05-10 | 5 | -1.4 | 1.0 | -1.4 | 3.0 | EMA exit |
| XAUUSD | long | 2026-05-10 | 2026-05-17 | 5 | -3.0 | 1.0 | -3.0 | 4.4 | EMA exit |
| XAUUSD | short | 2026-05-17 | 2026-08-09 | 60 | +4.5 | 2.1 | +2.2 | 1.1 | EMA exit |
| XAUUSD | long | 2026-08-09 | 2026-09-13 | 25 | -0.1 | 1.0 | -0.1 | 2.0 | EMA exit |
| XAUUSD | short | 2026-09-13 | 2026-09-20 | 5 | -1.0 | 1.0 | -1.0 | 1.4 | EMA exit |
| XAUUSD | long | 2026-09-20 | 2026-09-27 | 5 | -2.5 | 1.0 | -2.5 | 6.2 | EMA exit |
| XAUUSD | short | 2026-09-27 | 2026-10-26 | 21 | +4.9 | 2.1 | +2.3 | 0.1 | still open |

Worst 8: NDQ 2024-08-04 -7.1%; NDQ 2024-09-08 -6.1%; NDQ 2023-03-12 -6.0%; NDQ 2024-08-18 -5.9%; NDQ 2024-04-21 -3.8%; XAUUSD 2026-03-22 -3.8%; NDQ 2023-10-22 -3.7%; NDQ 2022-12-04 -3.6%

Best 8: XAUUSD 2023-10-15 +132.0%; NDQ 2025-05-04 +23.2%; NDQ 2026-04-12 +17.5%; NDQ 2023-03-19 +15.7%; NDQ 2023-11-05 +13.1%; NDQ 2022-04-10 +9.7%; NDQ 2024-09-15 +7.5%; XAUUSD 2022-05-08 +5.4%

## EVERY trade of DY1 (56 trades, chronological within each market)

| Market | Side | Entry | Exit | Days | Result % | Risk % | R | Worst dip % | Ended |
|---|---|---|---|---|---|---|---|---|---|
| NDQ | long | 2021-11-29 | 2021-12-01 | 2 | -3.2 | 1.5 | -2.1 | 4.0 | EMA exit |
| NDQ | long | 2021-12-27 | 2022-01-05 | 7 | -4.9 | 2.8 | -1.8 | 5.9 | EMA exit |
| NDQ | short | 2022-02-13 | 2022-03-16 | 23 | +1.9 | 4.3 | +0.4 | 3.0 | EMA exit |
| NDQ | short | 2022-05-18 | 2022-05-29 | 7 | -6.9 | 7.4 | -0.9 | 8.3 | EMA exit |
| NDQ | short | 2022-06-12 | 2022-06-26 | 10 | -3.4 | 6.5 | -0.5 | 4.4 | EMA exit |
| NDQ | short | 2022-06-30 | 2022-07-06 | 4 | -3.5 | 3.1 | -1.1 | 5.8 | EMA exit |
| NDQ | short | 2022-10-09 | 2022-10-23 | 10 | -3.3 | 5.6 | -0.6 | 4.5 | EMA exit |
| NDQ | long | 2023-04-13 | 2023-04-25 | 8 | -1.6 | 1.9 | -0.9 | 2.8 | EMA exit |
| NDQ | long | 2023-05-07 | 2023-08-02 | 63 | +16.0 | 1.7 | +9.5 | 0.8 | EMA exit |
| NDQ | long | 2023-12-05 | 2024-01-03 | 19 | +3.3 | 0.9 | +3.7 | 0.7 | EMA exit |
| NDQ | long | 2024-01-09 | 2024-02-20 | 30 | +4.9 | 1.1 | +4.5 | 0.7 | EMA exit |
| NDQ | long | 2024-02-22 | 2024-03-17 | 16 | -0.7 | 2.1 | -0.3 | 1.1 | EMA exit |
| NDQ | long | 2024-03-20 | 2024-04-04 | 10 | -2.2 | 1.8 | -1.2 | 2.5 | EMA exit |
| NDQ | long | 2024-05-13 | 2024-07-17 | 47 | +9.3 | 1.7 | +5.6 | 0.6 | EMA exit |
| NDQ | long | 2024-10-17 | 2024-10-31 | 10 | -1.3 | 1.2 | -1.1 | 1.7 | EMA exit |
| NDQ | long | 2024-11-26 | 2024-12-18 | 16 | +1.5 | 1.1 | +1.3 | 1.4 | EMA exit |
| NDQ | long | 2024-12-25 | 2024-12-30 | 3 | -3.0 | 2.1 | -1.4 | 3.9 | EMA exit |
| NDQ | long | 2025-01-22 | 2025-01-27 | 3 | -2.9 | 2.4 | -1.2 | 5.5 | EMA exit |
| NDQ | short | 2025-03-30 | 2025-04-09 | 8 | -0.1 | 4.8 | -0.0 | 4.0 | EMA exit |
| NDQ | short | 2025-04-21 | 2025-04-23 | 2 | -5.0 | 5.5 | -0.9 | 8.5 | EMA exit |
| NDQ | long | 2025-08-07 | 2025-08-20 | 9 | -0.7 | 1.5 | -0.5 | 2.0 | EMA exit |
| NDQ | long | 2025-08-28 | 2025-08-31 | 1 | -1.2 | 1.1 | -1.1 | 1.6 | EMA exit |
| NDQ | long | 2025-09-08 | 2025-10-12 | 24 | +3.3 | 1.2 | +2.8 | 0.3 | EMA exit |
| NDQ | long | 2025-10-20 | 2025-11-06 | 13 | +0.0 | 2.0 | +0.0 | 2.3 | EMA exit |
| NDQ | long | 2025-12-07 | 2025-12-14 | 5 | -1.9 | 1.7 | -1.1 | 2.7 | EMA exit |
| NDQ | long | 2026-01-11 | 2026-01-14 | 3 | -1.2 | 1.1 | -1.1 | 1.8 | EMA exit |
| NDQ | long | 2026-06-15 | 2026-06-23 | 6 | -3.3 | 3.5 | -0.9 | 5.0 | EMA exit |
| NDQ | long | 2026-08-13 | 2026-08-20 | 5 | -2.8 | 2.9 | -1.0 | 3.2 | EMA exit |
| XAUUSD | long | 2022-04-12 | 2022-04-24 | 7 | -1.8 | 1.5 | -1.2 | 3.9 | EMA exit |
| XAUUSD | short | 2022-09-08 | 2022-10-03 | 17 | +0.6 | 1.4 | +0.4 | 1.6 | EMA exit |
| XAUUSD | short | 2022-10-16 | 2022-10-26 | 8 | -1.1 | 2.1 | -0.6 | 1.8 | EMA exit |
| XAUUSD | short | 2022-10-31 | 2022-11-06 | 4 | -2.6 | 1.6 | -1.6 | 3.0 | EMA exit |
| XAUUSD | long | 2023-05-02 | 2023-05-16 | 10 | -1.4 | 1.3 | -1.0 | 2.1 | EMA exit |
| XAUUSD | short | 2023-10-10 | 2023-10-11 | 1 | -0.8 | 0.7 | -1.2 | 1.4 | EMA exit |
| XAUUSD | long | 2023-12-07 | 2023-12-10 | 1 | -1.2 | 1.0 | -1.2 | 2.6 | EMA exit |
| XAUUSD | long | 2024-04-28 | 2024-04-30 | 2 | -2.0 | 0.9 | -2.3 | 2.3 | EMA exit |
| XAUUSD | long | 2024-05-09 | 2024-05-23 | 10 | -0.7 | 1.3 | -0.6 | 0.9 | EMA exit |
| XAUUSD | long | 2024-07-07 | 2024-07-25 | 14 | -1.1 | 2.1 | -0.5 | 1.7 | EMA exit |
| XAUUSD | long | 2024-07-31 | 2024-08-06 | 4 | -2.4 | 2.1 | -1.1 | 3.4 | EMA exit |
| XAUUSD | long | 2024-08-12 | 2024-10-09 | 42 | +5.5 | 2.4 | +2.3 | 1.6 | EMA exit |
| XAUUSD | long | 2024-10-13 | 2024-11-06 | 18 | +0.5 | 1.2 | +0.4 | 0.4 | EMA exit |
| XAUUSD | long | 2024-11-24 | 2024-11-25 | 1 | -3.1 | 1.9 | -1.6 | 3.9 | EMA exit |
| XAUUSD | long | 2025-01-12 | 2025-02-27 | 34 | +6.9 | 1.6 | +4.3 | 1.2 | EMA exit |
| XAUUSD | long | 2025-03-04 | 2025-03-10 | 4 | -1.0 | 1.2 | -0.8 | 1.3 | EMA exit |
| XAUUSD | long | 2025-03-12 | 2025-04-07 | 18 | +1.6 | 1.3 | +1.2 | 0.1 | EMA exit |
| XAUUSD | long | 2025-04-09 | 2025-05-01 | 15 | +5.1 | 1.7 | +3.0 | 0.3 | EMA exit |
| XAUUSD | long | 2025-05-05 | 2025-05-12 | 5 | -2.9 | 2.6 | -1.1 | 3.8 | EMA exit |
| XAUUSD | long | 2025-05-25 | 2025-06-08 | 10 | -1.0 | 2.3 | -0.4 | 3.2 | EMA exit |
| XAUUSD | long | 2025-06-12 | 2025-06-24 | 8 | -1.8 | 1.8 | -1.0 | 2.6 | EMA exit |
| XAUUSD | long | 2025-07-21 | 2025-07-27 | 4 | -2.1 | 1.7 | -1.2 | 2.9 | EMA exit |
| XAUUSD | long | 2025-08-27 | 2025-10-27 | 43 | +17.4 | 1.2 | +14.5 | 0.4 | EMA exit |
| XAUUSD | long | 2025-11-10 | 2025-11-17 | 5 | -1.6 | 2.5 | -0.7 | 2.9 | EMA exit |
| XAUUSD | long | 2025-11-26 | 2026-02-02 | 46 | +12.9 | 2.0 | +6.3 | 0.6 | EMA exit |
| XAUUSD | long | 2026-02-09 | 2026-02-17 | 6 | -3.7 | 3.9 | -1.0 | 4.3 | EMA exit |
| XAUUSD | long | 2026-02-23 | 2026-03-12 | 13 | -3.1 | 5.3 | -0.6 | 4.8 | EMA exit |
| XAUUSD | short | 2026-07-13 | 2026-07-22 | 7 | -3.0 | 3.5 | -0.8 | 4.1 | EMA exit |

Worst 8: NDQ 2022-05-18 -6.9%; NDQ 2025-04-21 -5.0%; NDQ 2021-12-27 -4.9%; XAUUSD 2026-02-09 -3.7%; NDQ 2022-06-30 -3.5%; NDQ 2022-06-12 -3.4%; NDQ 2022-10-09 -3.3%; NDQ 2026-06-15 -3.3%

Best 8: XAUUSD 2025-08-27 +17.4%; NDQ 2023-05-07 +16.0%; XAUUSD 2025-11-26 +12.9%; NDQ 2024-05-13 +9.3%; XAUUSD 2025-01-12 +6.9%; XAUUSD 2024-08-12 +5.5%; XAUUSD 2025-04-09 +5.1%; NDQ 2024-01-09 +4.9%

## EVERY trade of DY3 (53 trades, chronological within each market)

| Market | Side | Entry | Exit | Days | Result % | Risk % | R | Worst dip % | Ended |
|---|---|---|---|---|---|---|---|---|---|
| NDQ | long | 2021-11-29 | 2021-12-01 | 2 | -3.2 | 1.5 | -2.1 | 4.0 | EMA exit |
| NDQ | long | 2021-12-27 | 2022-01-05 | 7 | -4.9 | 2.8 | -1.8 | 5.9 | EMA exit |
| NDQ | short | 2022-02-13 | 2022-03-16 | 23 | +1.9 | 4.3 | +0.4 | 3.0 | EMA exit |
| NDQ | short | 2022-05-01 | 2022-05-29 | 20 | +1.3 | 6.9 | +0.2 | 5.2 | EMA exit |
| NDQ | short | 2022-06-12 | 2022-06-26 | 10 | -3.4 | 6.5 | -0.5 | 4.4 | EMA exit |
| NDQ | short | 2022-10-09 | 2022-10-23 | 10 | -3.3 | 5.6 | -0.6 | 4.5 | EMA exit |
| NDQ | long | 2023-04-13 | 2023-04-25 | 8 | -1.6 | 1.9 | -0.9 | 2.8 | EMA exit |
| NDQ | long | 2023-05-07 | 2023-08-02 | 63 | +16.0 | 1.7 | +9.5 | 0.8 | EMA exit |
| NDQ | long | 2023-12-05 | 2024-01-03 | 19 | +3.3 | 0.9 | +3.7 | 0.7 | EMA exit |
| NDQ | long | 2024-01-09 | 2024-02-20 | 30 | +4.9 | 1.1 | +4.5 | 0.7 | EMA exit |
| NDQ | long | 2024-02-22 | 2024-03-17 | 16 | -0.7 | 2.1 | -0.3 | 1.1 | EMA exit |
| NDQ | long | 2024-03-20 | 2024-04-04 | 10 | -2.2 | 1.8 | -1.2 | 2.5 | EMA exit |
| NDQ | long | 2024-05-13 | 2024-07-17 | 47 | +9.3 | 1.7 | +5.6 | 0.6 | EMA exit |
| NDQ | long | 2024-10-17 | 2024-10-31 | 10 | -1.3 | 1.2 | -1.1 | 1.7 | EMA exit |
| NDQ | long | 2024-11-26 | 2024-12-18 | 16 | +1.5 | 1.1 | +1.3 | 1.4 | EMA exit |
| NDQ | long | 2024-12-25 | 2024-12-30 | 3 | -3.0 | 2.1 | -1.4 | 3.9 | EMA exit |
| NDQ | long | 2025-01-22 | 2025-01-27 | 3 | -2.9 | 2.4 | -1.2 | 5.5 | EMA exit |
| NDQ | short | 2025-03-30 | 2025-04-09 | 8 | -0.1 | 4.8 | -0.0 | 4.0 | EMA exit |
| NDQ | short | 2025-04-21 | 2025-04-23 | 2 | -5.0 | 5.5 | -0.9 | 8.5 | EMA exit |
| NDQ | long | 2025-08-07 | 2025-08-20 | 9 | -0.7 | 1.5 | -0.5 | 2.0 | EMA exit |
| NDQ | long | 2025-08-28 | 2025-08-31 | 1 | -1.2 | 1.1 | -1.1 | 1.6 | EMA exit |
| NDQ | long | 2025-09-08 | 2025-10-12 | 24 | +3.3 | 1.2 | +2.8 | 0.3 | EMA exit |
| NDQ | long | 2025-10-20 | 2025-11-06 | 13 | +0.0 | 2.0 | +0.0 | 2.3 | EMA exit |
| NDQ | long | 2025-12-07 | 2025-12-14 | 5 | -1.9 | 1.7 | -1.1 | 2.7 | EMA exit |
| NDQ | long | 2026-01-11 | 2026-01-14 | 3 | -1.2 | 1.1 | -1.1 | 1.8 | EMA exit |
| NDQ | long | 2026-06-15 | 2026-06-23 | 6 | -3.3 | 3.5 | -0.9 | 5.0 | EMA exit |
| NDQ | long | 2026-08-13 | 2026-08-20 | 5 | -2.8 | 2.9 | -1.0 | 3.2 | EMA exit |
| XAUUSD | long | 2022-04-12 | 2022-04-24 | 7 | -1.8 | 1.5 | -1.2 | 3.9 | EMA exit |
| XAUUSD | short | 2022-09-08 | 2022-10-03 | 17 | +0.6 | 1.4 | +0.4 | 1.6 | EMA exit |
| XAUUSD | short | 2022-10-16 | 2022-10-26 | 8 | -1.1 | 2.1 | -0.6 | 1.8 | EMA exit |
| XAUUSD | long | 2023-05-02 | 2023-05-16 | 10 | -1.4 | 1.3 | -1.0 | 2.1 | EMA exit |
| XAUUSD | long | 2023-12-07 | 2023-12-10 | 1 | -1.2 | 1.0 | -1.2 | 2.6 | EMA exit |
| XAUUSD | long | 2024-04-28 | 2024-04-30 | 2 | -2.0 | 0.9 | -2.3 | 2.3 | EMA exit |
| XAUUSD | long | 2024-05-09 | 2024-05-23 | 10 | -0.7 | 1.3 | -0.6 | 0.9 | EMA exit |
| XAUUSD | long | 2024-07-07 | 2024-07-25 | 14 | -1.1 | 2.1 | -0.5 | 1.7 | EMA exit |
| XAUUSD | long | 2024-07-31 | 2024-08-06 | 4 | -2.4 | 2.1 | -1.1 | 3.4 | EMA exit |
| XAUUSD | long | 2024-08-12 | 2024-10-09 | 42 | +5.5 | 2.4 | +2.3 | 1.6 | EMA exit |
| XAUUSD | long | 2024-10-13 | 2024-11-06 | 18 | +0.5 | 1.2 | +0.4 | 0.4 | EMA exit |
| XAUUSD | long | 2024-11-24 | 2024-11-25 | 1 | -3.1 | 1.9 | -1.6 | 3.9 | EMA exit |
| XAUUSD | long | 2025-01-12 | 2025-02-27 | 34 | +6.9 | 1.6 | +4.3 | 1.2 | EMA exit |
| XAUUSD | long | 2025-03-04 | 2025-03-10 | 4 | -1.0 | 1.2 | -0.8 | 1.3 | EMA exit |
| XAUUSD | long | 2025-03-12 | 2025-04-07 | 18 | +1.6 | 1.3 | +1.2 | 0.1 | EMA exit |
| XAUUSD | long | 2025-04-09 | 2025-05-01 | 15 | +5.1 | 1.7 | +3.0 | 0.3 | EMA exit |
| XAUUSD | long | 2025-05-05 | 2025-05-12 | 5 | -2.9 | 2.6 | -1.1 | 3.8 | EMA exit |
| XAUUSD | long | 2025-05-25 | 2025-06-08 | 10 | -1.0 | 2.3 | -0.4 | 3.2 | EMA exit |
| XAUUSD | long | 2025-06-12 | 2025-06-24 | 8 | -1.8 | 1.8 | -1.0 | 2.6 | EMA exit |
| XAUUSD | long | 2025-07-21 | 2025-07-27 | 4 | -2.1 | 1.7 | -1.2 | 2.9 | EMA exit |
| XAUUSD | long | 2025-08-27 | 2025-10-27 | 43 | +17.4 | 1.2 | +14.5 | 0.4 | EMA exit |
| XAUUSD | long | 2025-11-10 | 2025-11-17 | 5 | -1.6 | 2.5 | -0.7 | 2.9 | EMA exit |
| XAUUSD | long | 2025-11-26 | 2026-02-02 | 46 | +12.9 | 2.0 | +6.3 | 0.6 | EMA exit |
| XAUUSD | long | 2026-02-09 | 2026-02-17 | 6 | -3.7 | 3.9 | -1.0 | 4.3 | EMA exit |
| XAUUSD | long | 2026-02-23 | 2026-03-12 | 13 | -3.1 | 5.3 | -0.6 | 4.8 | EMA exit |
| XAUUSD | short | 2026-07-13 | 2026-07-22 | 7 | -3.0 | 3.5 | -0.8 | 4.1 | EMA exit |

Worst 8: NDQ 2025-04-21 -5.0%; NDQ 2021-12-27 -4.9%; XAUUSD 2026-02-09 -3.7%; NDQ 2022-06-12 -3.4%; NDQ 2022-10-09 -3.3%; NDQ 2026-06-15 -3.3%; NDQ 2021-11-29 -3.2%; XAUUSD 2024-11-24 -3.1%

Best 8: XAUUSD 2025-08-27 +17.4%; NDQ 2023-05-07 +16.0%; XAUUSD 2025-11-26 +12.9%; NDQ 2024-05-13 +9.3%; XAUUSD 2025-01-12 +6.9%; XAUUSD 2024-08-12 +5.5%; XAUUSD 2025-04-09 +5.1%; NDQ 2024-01-09 +4.9%
