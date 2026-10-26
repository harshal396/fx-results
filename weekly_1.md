# Weekly-RSI strategies

Generated 2026-10-26 03:13 UTC. OANDA daily bid/ask, 5 years, markets XAUUSD,NDQ,US30,EURUSD,GBPUSD,USDJPY,AUDUSD,USDCAD,XAGUSD,SPX500,DE30,UK100,WTI. Decisions on COMPLETED weeks / days only, executed at the next daily open (buy at the ask, sell at the bid). % = return on the price per trade, one unit, no leverage, no swap.

Reference, the market itself over the same period (buy and hold, % change, mid prices): XAUUSD +122%, NDQ +86%, US30 +47%, EURUSD -3%, GBPUSD -3%, USDJPY +38%, AUDUSD -6%, USDCAD +13%, XAGUSD +124%, SPX500 +68%, DE30 +60%, UK100 +47%, WTI +27%


## STRATEGY 1: the weekly RSI alone (W1 long>60 / short<40 / flat between, W2 always in the market, W3 long-only)


### All markets together (%)

| Variant | Trades | Win | Total % | Avg % per trade (95% interval) | PF | Deepest fall (%) |
|---|---|---|---|---|---|---|
| W1 | 314 | 26% | -98.7 | -0.31 (-1.10..+0.59) | 0.83 | 172.8 |
| W2 | 101 | 33% | -57.5 | -0.57 (-4.45..+4.65) | 0.90 | 233.1 |
| W3 | 191 | 32% | +150.9 | +0.79 (-0.41..+2.43) | 1.57 | 76.4 |

### Markets we tuned other rules on (NDQ,US30,XAUUSD) versus markets we never looked at

| Variant | Tuned: trades | Tuned: total % | Tuned: avg | Untouched: trades | Untouched: total % | Untouched: avg (95% interval) |
|---|---|---|---|---|---|---|
| W1 | 74 | +15.0 | +0.20 | 240 | -113.6 | -0.47 (-1.35..+0.83) |
| W2 | 22 | +47.8 | +2.17 | 79 | -105.3 | -1.33 (-4.89..+4.75) |
| W3 | 51 | +74.3 | +1.46 | 140 | +76.6 | +0.55 (-0.91..+2.76) |

### Build period versus holdout (everything after 2025-04-18): total % and average per trade

| Variant | Build trades | Build total | Build avg | Holdout trades | Holdout total | Holdout avg |
|---|---|---|---|---|---|---|
| W1 | 228 | -189.1 | -0.83 | 86 | +90.5 | +1.05 |
| W2 | 77 | -52.0 | -0.68 | 24 | -5.5 | -0.23 |
| W3 | 131 | +2.1 | +0.02 | 60 | +148.8 | +2.48 |

### Total % by market (trades)

| Variant | AUDUSD | DE30 | EURUSD | GBPUSD | NDQ | SPX500 | UK100 | US30 | USDCAD | USDJPY | WTI | XAGUSD | XAUUSD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| W1 | -27.1 (25) | -23.2 (27) | +0.7 (27) | +6.8 (15) | +1.8 (28) | -1.7 (27) | -13.0 (21) | -35.3 (25) | -13.9 (26) | -2.5 (23) | -89.6 (26) | +49.9 (23) | +48.5 (21) |
| W2 | -28.7 (8) | +15.8 (6) | -3.1 (9) | -3.0 (6) | +23.9 (7) | -12.9 (9) | -39.8 (8) | -63.6 (9) | -10.7 (7) | -24.3 (10) | -118.9 (11) | +120.4 (5) | +87.5 (6) |
| W3 | -10.4 (10) | -13.1 (18) | +3.6 (13) | +1.1 (8) | +14.6 (20) | +20.4 (18) | +7.6 (14) | -2.1 (16) | -9.3 (18) | +10.1 (16) | -5.6 (11) | +72.1 (14) | +61.8 (15) |

### Total % by year of entry

| Variant | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|
| W1 | -32.1 | -45.9 | -46.7 | -35.5 | +108.1 | -46.6 |
| W2 | -62.7 | +98.2 | +62.7 | -85.3 | -86.6 | +16.1 |
| W3 | -15.7 | +26.1 | +1.4 | -8.8 | +157.5 | -9.6 |

### Long trades versus short trades

| Variant | Long trades | Long total % | Long avg | Short trades | Short total % | Short avg |
|---|---|---|---|---|---|---|
| W1 | 191 | +150.9 | +0.79 | 123 | -249.6 | -2.03 |
| W2 | 52 | +283.9 | +5.46 | 49 | -341.4 | -6.97 |
| W3 | 191 | +150.9 | +0.79 | 0 | +0.0 | +0.00 |

### Average days held, and how trades ended

| Variant | Avg days held | signal | still open |
|---|---|---|---|
| W1 | 22 | 99% | 1% |
| W2 | 164 | 87% | 13% |
| W3 | 28 | 100% | 0% |

## STRATEGY 2: weekly RSI regime + daily RSI crossing 60 / 40 (X1-X4 = the four exits)


### All markets together (%)

| Variant | Trades | Win | Total % | Avg % per trade (95% interval) | PF | Deepest fall (%) |
|---|---|---|---|---|---|---|
| X1 | 214 | 36% | +37.6 | +0.18 (-0.51..+0.99) | 1.13 | 76.0 |
| X2 | 168 | 30% | +74.6 | +0.44 (-0.86..+2.35) | 1.26 | 70.9 |
| X3 | 240 | 37% | +53.6 | +0.22 (-0.47..+0.97) | 1.18 | 63.4 |
| X4 | 204 | 37% | -69.4 | -0.34 (-1.09..+0.49) | 0.83 | 127.7 |

### Markets we tuned other rules on (NDQ,US30,XAUUSD) versus markets we never looked at

| Variant | Tuned: trades | Tuned: total % | Tuned: avg | Untouched: trades | Untouched: total % | Untouched: avg (95% interval) |
|---|---|---|---|---|---|---|
| X1 | 61 | +17.8 | +0.29 | 153 | +19.8 | +0.13 (-0.73..+1.16) |
| X2 | 45 | +29.0 | +0.64 | 123 | +45.6 | +0.37 (-1.15..+3.08) |
| X3 | 70 | +6.1 | +0.09 | 170 | +47.5 | +0.28 (-0.54..+1.30) |
| X4 | 58 | +3.2 | +0.05 | 146 | -72.6 | -0.50 (-1.40..+0.47) |

### Build period versus holdout (everything after 2025-04-18): total % and average per trade

| Variant | Build trades | Build total | Build avg | Holdout trades | Holdout total | Holdout avg |
|---|---|---|---|---|---|---|
| X1 | 149 | -33.4 | -0.22 | 65 | +71.1 | +1.09 |
| X2 | 122 | -38.7 | -0.32 | 46 | +113.2 | +2.46 |
| X3 | 165 | -17.7 | -0.11 | 75 | +71.3 | +0.95 |
| X4 | 140 | -67.6 | -0.48 | 64 | -1.8 | -0.03 |

### Total % by market (trades)

| Variant | AUDUSD | DE30 | EURUSD | GBPUSD | NDQ | SPX500 | UK100 | US30 | USDCAD | USDJPY | WTI | XAGUSD | XAUUSD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X1 | -6.5 (11) | +3.6 (20) | -2.6 (18) | +2.0 (16) | +5.4 (23) | +0.3 (19) | -9.0 (15) | -19.8 (18) | -5.6 (11) | +5.4 (19) | -25.4 (12) | +57.5 (12) | +32.2 (20) |
| X2 | -13.0 (10) | -13.3 (17) | +7.7 (12) | +13.9 (9) | -6.2 (18) | -11.1 (16) | -5.5 (12) | -17.9 (15) | -5.0 (11) | -0.2 (15) | -24.1 (11) | +96.2 (10) | +53.1 (12) |
| X3 | -5.3 (11) | +3.5 (22) | -1.7 (19) | +4.5 (18) | -1.1 (25) | -6.5 (23) | -9.2 (17) | -14.1 (21) | -5.5 (12) | +5.7 (23) | -5.8 (12) | +67.8 (13) | +21.3 (24) |
| X4 | -7.8 (9) | -10.5 (21) | -1.8 (16) | +6.8 (13) | -8.6 (22) | -10.5 (18) | -11.7 (14) | -21.0 (16) | -9.2 (11) | +6.6 (19) | -71.0 (13) | +36.5 (12) | +32.8 (20) |

### Total % by year of entry

| Variant | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|
| X1 | -17.3 | -35.9 | +0.1 | +9.4 | +105.3 | -23.8 |
| X2 | -21.0 | -20.0 | -10.3 | -6.5 | +149.1 | -16.7 |
| X3 | -17.5 | -14.8 | -3.7 | +10.3 | +95.3 | -15.9 |
| X4 | -24.6 | -53.2 | -9.3 | +6.3 | +51.9 | -40.5 |

### Long trades versus short trades

| Variant | Long trades | Long total % | Long avg | Short trades | Short total % | Short avg |
|---|---|---|---|---|---|---|
| X1 | 150 | +121.7 | +0.81 | 64 | -84.1 | -1.31 |
| X2 | 109 | +175.7 | +1.61 | 59 | -101.1 | -1.71 |
| X3 | 171 | +133.1 | +0.78 | 69 | -79.5 | -1.15 |
| X4 | 142 | +62.7 | +0.44 | 62 | -132.2 | -2.13 |

### Average days held, and how trades ended

| Variant | Avg days held | EMA21 break | daily RSI through 50 | stop | weekly regime ended |
|---|---|---|---|---|---|
| X1 | 18 | 0% | 89% | 11% | 0% |
| X2 | 28 | 0% | 0% | 25% | 75% |
| X3 | 15 | 92% | 0% | 8% | 0% |
| X4 | 21 | 0% | 0% | 100% | 0% |

### Strategy 2 in R (risk = distance to the initial stop)

| Variant | Trades | Win | Total R | Avg R per trade (95% interval) | PF | Deepest fall (R) |
|---|---|---|---|---|---|---|
| X1 | 214 | 36% | +11.6 | +0.05 (-0.09..+0.20) | 1.15 | 18.9 |
| X2 | 168 | 30% | +40.1 | +0.24 (-0.15..+0.82) | 1.54 | 16.7 |
| X3 | 240 | 37% | +16.3 | +0.07 (-0.07..+0.21) | 1.20 | 14.1 |
| X4 | 204 | 37% | +0.4 | +0.00 (-0.16..+0.17) | 1.00 | 19.0 |
