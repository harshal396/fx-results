#!/usr/bin/env python3
"""Read-only: which instruments can your OANDA account trade?  Places NO orders.
Run it INSIDE the bot's container (the token is in its environment):
  docker compose exec -T fxagents python - < ~/check_instruments.py
  docker compose exec -T fxagents python - BTC US2000 < ~/check_instruments.py      # your own search words
With no words it looks for the ones you asked about: BTC, US2000 (Russell 2000), plus the three the bot trades now.
Prints the OANDA name, type, price precision, minimum size and margin rate of every match, or says it found none."""
import asyncio
import os
import sys

from fxagents.oanda import OandaClient, OandaError

WORDS = [w.upper() for w in sys.argv[1:]] or ["BTC", "XBT", "US2000", "RUSSELL", "XAU_USD", "NAS100", "US30"]


async def main() -> int:
    token, acct = os.environ.get("OANDA_API_TOKEN", ""), os.environ.get("OANDA_ACCOUNT_ID", "")
    if not token or not acct:
        print("OANDA_API_TOKEN / OANDA_ACCOUNT_ID are not set in this container.")
        return 2
    env = os.environ.get("OANDA_ENV", "practice")
    c = OandaClient(token, acct, env)
    try:
        try:
            ins = (await c.req("GET", c.acct("/instruments")))["instruments"]
        except OandaError as e:
            print(f"OANDA refused the request: {e}")
            return 1
    finally:
        await c.aclose()
    print(f"{len(ins)} instruments tradeable on this {env} account. Matches for {', '.join(WORDS)}:\n")
    print(f"{'name':<14}{'type':<8}{'prec':<6}{'min size':<10}{'margin':<8}display")
    n = 0
    for i in sorted(ins, key=lambda x: x["name"]):
        hay = (i["name"] + " " + str(i.get("displayName", ""))).upper()
        if any(w in hay for w in WORDS):
            n += 1
            print(f"{i['name']:<14}{i.get('type', ''):<8}{str(i.get('displayPrecision', '')):<6}{str(i.get('minimumTradeSize', '')):<10}"
                  f"{float(i.get('marginRate', 0)) * 100:>5.1f}%  {i.get('displayName', '')}")
    if not n:
        print("(none found: this account cannot trade any of them)")
    return 0


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
