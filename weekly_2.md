# Your weekly and daily rule books

Generated 2026-10-28 02:50 UTC. OANDA daily bid/ask, 5 years, markets XAUUSD,NDQ. Decisions on COMPLETED weeks / days only, executed at the next daily open (buy at the ask, sell at the bid). No stop, as specified. % = return on the price per trade, one unit, no leverage, no swap.

Reference, simply holding each market over the same period: XAUUSD +128%, NDQ +86%


## WEEKLY rule book (WK = your rule, WK0 = the same without the RSI condition)

### All markets together (% per trade)

| Variant | Trades | Win | Total % | Avg % per trade (95% interval) | PF | Deepest fall (%) |
|---|---|---|---|---|---|---|
| WK | 24 | 38% | +84.0 | +3.50 (-1.50..+10.28) | 2.47 | 15.9 |
| WK0 | 50 | 38% | +92.5 | +1.85 (-0.17..+4.08) | 2.26 | 20.2 |

### Markets we tuned other rules on (NDQ,US30,XAUUSD) versus markets we never looked at

| Variant | Tuned: trades | Tuned: total % | Tuned: avg | Untouched: trades | Untouched: total % | Untouched: avg (95% interval) |
|---|---|---|---|---|---|---|
| WK | 24 | +84.0 | +3.50 | 0 | +0.0 | +0.00 (+0.00..+0.00) |
| WK0 | 50 | +92.5 | +1.85 | 0 | +0.0 | +0.00 (+0.00..+0.00) |

### Build period versus holdout (entries after 2025-04-25)

| Variant | Build trades | Build total | Build avg | Holdout trades | Holdout total | Holdout avg |
|---|---|---|---|---|---|---|
| WK | 18 | +80.7 | +4.48 | 6 | +3.3 | +0.55 |
| WK0 | 37 | +57.2 | +1.55 | 13 | +35.3 | +2.72 |

### Total % by market (trades)

| Variant | NDQ | XAUUSD |
|---|---|---|
| WK | +13.7 (14) | +70.3 (10) |
| WK0 | +61.7 (23) | +30.8 (27) |

### Total % by year of entry

| Variant | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|
| WK | -9.0 | -7.0 | +39.6 | +62.0 | +6.2 | -7.9 |
| WK0 | -5.0 | +18.7 | +52.0 | -12.7 | +29.1 | +10.3 |

### Long trades versus short trades

| Variant | Long trades | Long total % | Long avg | Short trades | Short total % | Short avg |
|---|---|---|---|---|---|---|
| WK | 15 | +113.8 | +7.59 | 9 | -29.8 | -3.31 |
| WK0 | 24 | +99.5 | +4.15 | 26 | -7.1 | -0.27 |

### How long, how much time in the market, and the worst dip inside a trade

| Variant | Avg days held | Time in the market | Avg worst dip inside a trade (%) | Worst dip of any trade (%) | Trades still open |
|---|---|---|---|---|---|
| WK | 76 | 70% | 4.2 | 10.6 | 1 |
| WK0 | 42 | 81% | 2.8 | 8.5 | 2 |

## DAILY rule book (DY1 = your rule with the sell trigger at 42, DY2 = plus EMA21 side at entry, DY3 = sell trigger at 40)

### All markets together (% per trade)

| Variant | Trades | Win | Total % | Avg % per trade (95% interval) | PF | Deepest fall (%) |
|---|---|---|---|---|---|---|
| DY1 | 59 | 31% | +2.1 | +0.03 (-0.93..+1.11) | 1.02 | 29.5 |
| DY2 | 59 | 31% | +2.1 | +0.03 (-0.93..+1.11) | 1.02 | 29.5 |
| DY3 | 56 | 34% | +16.5 | +0.29 (-0.77..+1.33) | 1.23 | 18.5 |

### Markets we tuned other rules on (NDQ,US30,XAUUSD) versus markets we never looked at

| Variant | Tuned: trades | Tuned: total % | Tuned: avg | Untouched: trades | Untouched: total % | Untouched: avg (95% interval) |
|---|---|---|---|---|---|---|
| DY1 | 59 | +2.1 | +0.03 | 0 | +0.0 | +0.00 (+0.00..+0.00) |
| DY2 | 59 | +2.1 | +0.03 | 0 | +0.0 | +0.00 (+0.00..+0.00) |
| DY3 | 56 | +16.5 | +0.29 | 0 | +0.0 | +0.00 (+0.00..+0.00) |

### Build period versus holdout (entries after 2025-04-25)

| Variant | Build trades | Build total | Build avg | Holdout trades | Holdout total | Holdout avg |
|---|---|---|---|---|---|---|
| DY1 | 39 | +3.1 | +0.08 | 20 | -1.1 | -0.05 |
| DY2 | 39 | +3.1 | +0.08 | 20 | -1.1 | -0.05 |
| DY3 | 36 | +17.5 | +0.49 | 20 | -1.1 | -0.05 |

### Total % by market (trades)

| Variant | NDQ | XAUUSD |
|---|---|---|
| DY1 | -8.6 (29) | +10.6 (30) |
| DY2 | -8.6 (29) | +10.6 (30) |
| DY3 | +2.4 (28) | +14.0 (28) |

### Total % by year of entry

| Variant | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|
| DY1 | -5.1 | -17.8 | +13.2 | +6.5 | +16.1 | -10.8 |
| DY2 | -5.1 | -17.8 | +13.2 | +6.5 | +16.1 | -10.8 |
| DY3 | -5.1 | -4.2 | +14.0 | +6.5 | +16.1 | -10.8 |

### Long trades versus short trades

| Variant | Long trades | Long total % | Long avg | Short trades | Short total % | Short avg |
|---|---|---|---|---|---|---|
| DY1 | 47 | +27.8 | +0.59 | 12 | -25.8 | -2.15 |
| DY2 | 47 | +27.8 | +0.59 | 12 | -25.8 | -2.15 |
| DY3 | 47 | +27.8 | +0.59 | 9 | -11.4 | -1.26 |

### How long, how much time in the market, and the worst dip inside a trade

| Variant | Avg days held | Time in the market | Avg worst dip inside a trade (%) | Worst dip of any trade (%) | Trades still open |
|---|---|---|---|---|---|
| DY1 | 12 | 27% | 2.5 | 8.5 | 0 |
| DY2 | 12 | 27% | 2.5 | 8.5 | 0 |
| DY3 | 12 | 27% | 2.4 | 8.5 | 0 |

## EVERY trade of W1 (0 trades, chronological within each market)

| Market | Side | Entry | Exit | Days | Result % | Worst dip % | Ended |
|---|---|---|---|---|---|---|---|

Worst 8: 

Best 8: 

## EVERY trade of W3 (0 trades, chronological within each market)

| Market | Side | Entry | Exit | Days | Result % | Worst dip % | Ended |
|---|---|---|---|---|---|---|---|

Worst 8: 

Best 8: 

## EVERY trade of X1 (0 trades, chronological within each market)

| Market | Side | Entry | Exit | Days | Result % | Worst dip % | Ended |
|---|---|---|---|---|---|---|---|

Worst 8: 

Best 8: 

## EVERY trade of X3 (0 trades, chronological within each market)

| Market | Side | Entry | Exit | Days | Result % | Worst dip % | Ended |
|---|---|---|---|---|---|---|---|

Worst 8: 

Best 8: 
