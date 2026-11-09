#!/usr/bin/env bash
# install_open_candle_off.sh (Nov 8 2026) - switches the market-open-candle block OFF in every one of your RSI/EMA books.
# Config only: one line `no_entry_open_candle: {}` is added to each my_* book in config.yaml (my_intraday_mom excluded) and a test that checks it.
# The feature stays in the code and can be turned back on per book. Nothing else changes: your books' code, rules and journals are untouched.
# Run:  bash ~/install_open_candle_off.sh        Check only (changes nothing):  DRY=1 bash ~/install_open_candle_off.sh
# It changes nothing unless ALL of these hold, in order:
#   1. you are on main with no uncommitted changes, no update is running, and the config looks as expected
#   2. the image builds and the FULL test suite passes in a throwaway container (the running bot is untouched until now)
#   3. the restarted bot answers /healthz and keeps answering 45 s later
# Any failure after step 1 puts the code back exactly as it was. Only after a healthy restart is it pushed to GitHub.
set -u
REPO="${REPO:-$HOME/fx-agents}"; BR="${BR:-main}"; ORIGIN="${ORIGIN:-origin}"; DRY="${DRY:-0}"
LOG="${LOG:-$HOME/install_open_candle_off.log}"; LOCK="${LOCK:-/tmp/fx-auto-update.lock}"; TEST_TIMEOUT="${TEST_TIMEOUT:-2400}"
DC="docker compose"
exec > >(tee -a "$LOG") 2>&1
say() { echo "$(date '+%F %T') $*"; }
notify() {
  local t; t=$(grep -E '^NTFY_TOPIC=' "$REPO/.env" 2>/dev/null | tail -1 | cut -d= -f2- | tr -d "\"' ")
  [ -n "$t" ] && curl -fsS -m 15 -d "FX open-candle-off install: $*" "https://ntfy.sh/$t" >/dev/null 2>&1
  say "$*"; return 0
}
die() { notify "STOPPED, nothing changed: $*"; exit 1; }
cd "$REPO" || { say "no such folder: $REPO"; exit 1; }
exec 9>"$LOCK"; flock -n 9 || die "an update is running - try again in 15 minutes"
[ "$(git rev-parse --abbrev-ref HEAD)" = "$BR" ] || die "the repo is not on $BR"
[ -z "$(git status --porcelain)" ] || die "the repo has uncommitted changes - commit or undo them first"
grep -q no_entry_open_candle fxagents/agents/my_books.py || die "the market-open block is not in your code, so there is nothing to switch off"
grep -q "no_entry_open_candle: {}" config.yaml && die "already installed (config.yaml already has no_entry_open_candle: {})"
[ ! -e tests/test_open_candle_off.py ] || die "tests/test_open_candle_off.py already exists"
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
base64 -d > "$T/test_open_candle_off.py" <<'B64'
IiIiVGhlIG1hcmtldC1vcGVuLWNhbmRsZSBibG9jayBpcyBzd2l0Y2hlZCBPRkYgaW4gZXZlcnkg
bXlfKiBib29rIChOb3YgOCAyMDI2KS4gVGhlIGZlYXR1cmUgc3RheXMgaW4gdGhlIGNvZGUgKGFn
ZW50cy9teV9ib29rcy5weSwKc2V0dGluZyBub19lbnRyeV9vcGVuX2NhbmRsZSkgc28gaXQgY2Fu
IGJlIHR1cm5lZCBiYWNrIG9uIHBlciBib29rOyBpdCBibG9ja2VkIGEgd2lubmluZyBORFEgc2hv
cnQgb24gTm92IDUgYW5kIHRoZSBiYWNrdGVzdCBkZWNpZGVzLiIiIgpmcm9tIGZ4YWdlbnRzLmNv
bmZpZyBpbXBvcnQgbG9hZF9jb25maWcKCkNGRyA9IGxvYWRfY29uZmlnKCJjb25maWcueWFtbCIp
Ck1JTkUgPSBbYiBmb3IgYiwgdiBpbiBDRkdbInNoYWRvdyJdLml0ZW1zKCkgaWYgYi5zdGFydHN3
aXRoKCJteV8iKSBhbmQgYiAhPSAibXlfaW50cmFkYXlfbW9tIiBhbmQgaXNpbnN0YW5jZSh2LCBk
aWN0KSBhbmQgInN5bWJvbHMiIGluIHZdCgoKZGVmIHRlc3RfZXZlcnlfbXlfcnNpX2VtYV9ib29r
X2hhc190aGVfb3Blbl9jYW5kbGVfYmxvY2tfb2ZmKCk6CiAgICBhc3NlcnQgTUlORQogICAgYXNz
ZXJ0IGFsbChDRkdbInNoYWRvdyJdW2JdLmdldCgibm9fZW50cnlfb3Blbl9jYW5kbGUiLCAibWlz
c2luZyIpID09IHt9IGZvciBiIGluIE1JTkUpLCBbYiBmb3IgYiBpbiBNSU5FIGlmIENGR1sic2hh
ZG93Il1bYl0uZ2V0KCJub19lbnRyeV9vcGVuX2NhbmRsZSIsICJtaXNzaW5nIikgIT0ge31dCgoK
ZGVmIHRlc3RfdGhlX2ZlYXR1cmVfaXRzZWxmX2lzX3N0aWxsX2luX3RoZV9jb2RlX2FuZF9kZWZh
dWx0c190b190aGVfb2xkX3ZhbHVlKCk6CiAgICBmcm9tIGZ4YWdlbnRzLmFnZW50cy5teV9ib29r
cyBpbXBvcnQgREVGQVVMVFMKICAgIGFzc2VydCBERUZBVUxUU1sibm9fZW50cnlfb3Blbl9jYW5k
bGUiXSA9PSB7Ik5EUSI6ICIwOTozMCIsICJVUzMwIjogIjA5OjMwIn0gYW5kIERFRkFVTFRTWyJv
cGVuX2NhbmRsZV90ZnMiXSA9PSBbIjE1bWluIiwgIjFoIl0K
B64
cat > "$T/edit.py" <<'PY'
import re, sys
p = "config.yaml"; s = open(p, encoding="utf-8").read()
out, cur, n = [], None, 0
for ln in s.split("\n"):
    m = re.match(r"^  (my_[a-z0-9_]+):", ln)
    if m:
        cur = m.group(1)
    elif re.match(r"^  \S", ln):
        cur = None
    out.append(ln)
    if cur and cur != "my_intraday_mom" and re.match(r"^    symbols: \[", ln):
        out.append("    no_entry_open_candle: {}          # OFF (Nov 8 2026): it blocked a winning NDQ short on Nov 5; the backtest decides")
        n += 1
if not 1 <= n <= 20:
    sys.exit(f"expected 1 to 20 my_* books with a symbols line, found {n}")
if sys.argv[1:] == ["write"]:
    open(p, "w", encoding="utf-8").write("\n".join(out))
print(n)
PY
N=$(python3 "$T/edit.py") || die "config.yaml is not laid out as I expect (no my_* books with a symbols line, or too many)"
[ "$DRY" = "1" ] && { notify "DRY RUN OK: $N books would get the line; nothing was changed"; exit 0; }

OLD=$(git rev-parse HEAD)
healthy() { local i; for i in $(seq 1 "${HEALTH_TRIES:-30}"); do curl -fsS -m 5 localhost:8088/healthz >/dev/null 2>&1 && return 0; sleep "${HEALTH_WAIT:-10}"; done; return 1; }
rollback() {
  say "rolling back to $OLD"
  git reset --hard "$OLD" >/dev/null 2>&1
  $DC build fxagents >/dev/null 2>&1
  $DC up -d fxagents >/dev/null 2>&1
  healthy && say "rollback done, bot healthy" || notify "ROLLBACK DONE BUT THE BOT IS NOT ANSWERING - check the server"
}
fail() { rollback; notify "FAILED and rolled back: $*"; exit 1; }

python3 "$T/edit.py" write >/dev/null || fail "the config edit failed"
cp "$T/test_open_candle_off.py" tests/test_open_candle_off.py
[ "$(grep -c 'no_entry_open_candle: {}' config.yaml)" = "$N" ] || fail "the config edit did not add $N lines"
git add -A && git -c user.name="${GIT_NAME:-fx}" -c user.email="${GIT_EMAIL:-fx@localhost}" commit -qm "Market-open-candle block off in the my_* books" || fail "could not commit"
NEW=$(git rev-parse --short HEAD)
say "committed $NEW ($N books); building and running the full tests (about 12 minutes) ..."
$DC build fxagents >/dev/null 2>&1 || fail "the image did not BUILD"
OUT=$(timeout "$TEST_TIMEOUT" $DC run --rm --no-deps -T -e FX_NO_LOCAL_CONFIG=1 fxagents python -m pytest -q -p no:cacheprovider tests 2>&1); RC=$?
say "tests exit code $RC: $(echo "$OUT" | tail -2 | tr '\n' ' ')"
if [ "$RC" -ne 0 ]; then echo "$OUT" | grep -E "^(FAILED|ERROR)" | head -15; fail "the TESTS FAILED ($(echo "$OUT" | tail -1 | cut -c1-80))"; fi
SERVICES="fxagents"; $DC config --services 2>/dev/null | grep -qx fxbt && SERVICES="fxagents fxbt"
$DC up -d $SERVICES >/dev/null 2>&1 || fail "could not restart the bot"
healthy || fail "the new version did not answer /healthz"
sleep "${SETTLE:-45}"
healthy || fail "the new version crashed after starting"
if git push -q "$ORIGIN" "$BR" >/dev/null 2>&1; then
  notify "installed OK ($NEW): tests passed, bot healthy, saved to GitHub. The 09:30 candle is no longer blocked"
else
  notify "installed OK and running ($NEW), but the push to your GitHub failed - run: cd ~/fx-agents && git push $ORIGIN $BR"
fi
