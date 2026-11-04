# Harshal's strategy notes (kept Nov 3 2026)

How to use this file: tell Claude **"check PULLBACK-ENTRY"** (or any ID below). Claude then looks this file up (if it is in
`fx-results`, or pasted) and in the old chats of the project, and works from it. Nothing in this file is built unless it says BUILT.

---

## PULLBACK-ENTRY — NOT BUILT, waiting for Harshal's example chart

**Harshal's words (Nov 3):** "only entry I want is if the market is going down one way fall and then if it pulls back to 21 we
can take the trade near the 21 EMA and stop above the 24 EMA (make sure it is going down crazy for this entry)".
He will send a chart when it happens. Do not build until he does.

**Claude's draft reading (NOT agreed, parameters are guesses):**
- Short side; longs are the mirror image.
- Strong one-way fall: EMA21 below EMA24 and both falling, CHOP(14) < 40, price down at least 3 ATR over the last 10 candles.
- Pullback: a candle rises to within 1/4 ATR of the EMA21, or touches it, and CLOSES back below it. Entry at that candle close.
- Stop: above the EMA24 plus 1/4 ATR, never tighter than 1/2 ATR.
- Exit: a close above the EMA24 (an exit at the EMA21 would trigger at once). Breakeven at +1R, one partial of 1/3 at the
  liquidity line or by Jev from +2R (the trend-mode exits).
- Not the same as today's entries: the bot enters on "close beyond EMA21 + RSI crosses 44/55", never on a touch of the EMA.

**Open questions:** Is the blue line the EMA24 and the green line the EMA21? Should this replace the RSI-trigger entries or sit
beside them? What counts as "going down crazy" (his chart will show)?

---

## Requested Nov 3, BUILT in `install_entry_blocks.sh` (Nov 3; installed once the file's "installed OK" line appears in ~/install_entry_blocks.log)
1. No entries on the candle that contains the 09:30 New York cash open: NDQ and US30, 15m and 1h books (the 15m 09:30 candle, the 1h
   09:00 candle). Gold has no open time set (waiting for Harshal: which time?). Settings: `no_entry_open_candle`, `open_candle_tfs`.
2. The EMA-cross strategy: the four `my_ema_cross` books take no new entries; open trades are managed to their end.
   Setting: `no_entry_rules: [ema_cross]`.
3. "A few more things we are not taking trades at": Harshal to list them (not yet given).

## Proposed, undecided
3. Liquidity-line minimum distance: today 1R; options 0.5R or 1 ATR (so the 1h and 4h books get lines).
4. Pre-news exit: keep for every book, or only for big events (GDP, CPI, Fed, elections), per book.
5. Fresh-cross gate on `my_rsi_1h` (an RSI-only book that still gets an EMA test): turn off after a week of data.
6. CHOP 50 trend / range line: review after about 30 trades per mode (5 trend trades so far, 4 lost on the EMA21 exit).
7. A "Close now" button for a single trade in the app (paper books only), through the hook script.
8. Signals list with what price did after each blocked signal.

## What is installed (as of Nov 3 2026)
- ba5a56b liquidity-line partial. b59a675 trend / range modes, no new US30 in the RSI/EMA books, chop cutoff 58, liquidity lines
  v2 (lowest of a group, 10 days back, 1h levels for 15m books). b807231 merge of the friend's daylight-saving fix.
- `install_fresh_range_only.sh` (fresh-cross only in range mode) was built Nov 2; check it is installed with
  `grep -c fresh_range_only ~/fx-agents/fxagents/agents/my_books.py` (3 or more = installed).
- Rules in force: gold and NDQ only (US30 managed to the end if open); CHOP >= 58 = no entry; CHOP < 50 at entry = trend mode
  (breakeven after +1R, no trailing stop, exit on a close past the EMA21, ONE partial of 1/3: liquidity line or Jev from +2R);
  CHOP 50..58 = range mode (Jev partials from +0.5R half of what is open, max 2, plus the 2xATR trail after +1R); decisions on closed
  candles, stops are live orders; fresh-cross gate (15m, 1h books) in range mode only; trend gate on the 15m, 1h and 4h books.
- Paper trading to collect data: no per-market risk cap on purpose; rules frozen for 2 to 4 weeks between big changes (advice).
