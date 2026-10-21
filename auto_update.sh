#!/usr/bin/env bash
# Safe auto-update of ~/fx-agents from your friend's repo (git remote "upstream").
# Install OUTSIDE the repo (a script rewritten by its own update can misbehave while it runs):  ~/auto_update.sh
#
# It changes nothing unless ALL of these hold, in order:
#   1. upstream has new commits, you are on main with no uncommitted changes, and nothing else is updating
#   2. the merge has no conflicts, OR its only conflicts are in the three files where your books hook into his code
#      (config.yaml, setup_first.py, index.html) - those are fixed automatically by ~/apply_my_hooks.py;
#      any other conflict: merge undone, you get a phone alert, a human decides
#   3. the image builds and the FULL test suite passes in a throwaway container
#   4. the restarted bot answers /healthz and keeps answering 45 s later
# Any failure after the merge rolls the code and the running bot back to what it was. Only after a healthy
# restart is the result pushed to your GitHub. Alerts go to your ntfy topic (NTFY_TOPIC in .env).
#
# Run by hand:   ~/auto_update.sh            Check only (changes nothing):   DRY=1 ~/auto_update.sh
# Log:           ~/auto_update.log           (tail -30 ~/auto_update.log)
set -u
REPO="${REPO:-$HOME/fx-agents}"; UP="${UP:-upstream}"; BR="${BR:-main}"; ORIGIN="${ORIGIN:-origin}"
LOG="${LOG:-$HOME/auto_update.log}"; LOCK="${LOCK:-/tmp/fx-auto-update.lock}"; DRY="${DRY:-0}"
TEST_TIMEOUT="${TEST_TIMEOUT:-2400}"
HOOKS="${HOOKS:-$HOME/apply_my_hooks.py}"
HOOK_FILES="${HOOK_FILES:-config.yaml fxagents/agents/setup_first.py fxagents/dashboard/static/index.html}"
GIT_ID="-c user.name=auto-update -c user.email=auto-update@localhost"
exec >>"$LOG" 2>&1
exec 9>"$LOCK"; flock -n 9 || { echo "$(date '+%F %T') another update is running - skipped"; exit 0; }
cd "$REPO" || { echo "$(date '+%F %T') no such folder: $REPO"; exit 1; }
DC="docker compose"
say() { echo "$(date '+%F %T') $*"; }
notify() {
  local t; t=$(grep -E '^NTFY_TOPIC=' .env 2>/dev/null | tail -1 | cut -d= -f2- | tr -d "\"' ")
  [ -n "$t" ] && curl -fsS -m 15 -d "FX auto-update: $*" "https://ntfy.sh/$t" >/dev/null 2>&1
  say "ALERT: $*"; return 0
}
fail() { notify "$*"; exit 1; }
conflicted() { git diff --name-only --diff-filter=U; }
no_markers() { [ -z "$(git grep -n -E '^(<<<<<<<|>>>>>>>) ' 2>/dev/null)" ]; }
only_hook_conflicts() { local f; [ -f "$HOOKS" ] || return 1; [ -n "$(conflicted)" ] || return 1
  for f in $(conflicted); do case " $HOOK_FILES " in *" $f "*) ;; *) return 1;; esac; done; return 0; }
# take his version of the hook files, then put your book hooks back on top (idempotent script)
resolve_hooks() {
  only_hook_conflicts || return 1
  git checkout --theirs -- $(conflicted) >/dev/null 2>&1 || return 1
  python3 "$HOOKS" >/dev/null 2>&1 || return 1
  git add -- $HOOK_FILES >/dev/null 2>&1 || return 1
  [ -z "$(conflicted)" ] && no_markers || return 1
  git $GIT_ID commit --no-edit -q >/dev/null 2>&1
}
# after a clean merge: make sure the hooks are all still in place (a no-op when they are)
reapply_hooks() {
  [ -f "$HOOKS" ] || return 0
  python3 "$HOOKS" >/dev/null 2>&1 || return 1
  git add -- $HOOK_FILES >/dev/null 2>&1
  if ! git diff --cached --quiet; then git $GIT_ID commit -q -m "re-apply my book hooks" >/dev/null 2>&1 || return 1; fi
  no_markers
}
healthy() { local i; for i in $(seq 1 "${HEALTH_TRIES:-30}"); do curl -fsS -m 5 localhost:8088/healthz >/dev/null 2>&1 && return 0; sleep "${HEALTH_WAIT:-10}"; done; return 1; }
rollback() {
  say "rolling back to $OLD"
  git merge --abort >/dev/null 2>&1
  git reset --hard "$OLD" >/dev/null 2>&1
  $DC build fxagents >/dev/null 2>&1
  $DC up -d fxagents >/dev/null 2>&1
  healthy && say "rollback done, bot healthy" || notify "ROLLBACK DONE BUT THE BOT IS NOT ANSWERING - check the server"
}

say "=== auto-update start (DRY=$DRY) ==="
git fetch -q "$UP" "$BR" || fail "could not fetch $UP (network or remote name?)"
N=$(git rev-list --count "HEAD..$UP/$BR")
[ "$N" -gt 0 ] || { say "up to date"; exit 0; }
[ "$(git rev-parse --abbrev-ref HEAD)" = "$BR" ] || fail "$N new commits waiting, but the repo is not on $BR - not touching it"
[ -z "$(git status --porcelain --untracked-files=no)" ] || fail "$N new commits waiting, but tracked files have uncommitted changes ($(git status --porcelain --untracked-files=no | awk '{print $2}' | head -3 | tr '\n' ' ')) - commit or undo them first"
# the new backtest worker defaults to a 2000 MB cap = the whole RAM of a 2 GB server: demand a smaller cap first
if git show "$UP/$BR:docker-compose.yml" 2>/dev/null | grep -q "FX_BT_MEM" && ! grep -q '^FX_BT_MEM=' .env 2>/dev/null; then
  fail "$N new commits waiting, but .env has no FX_BT_MEM. Add the line FX_BT_MEM=500m (the backtest worker would otherwise be allowed 2000 MB) and run again"
fi
OLD=$(git rev-parse HEAD)
say "$N new commits from $UP/$BR; currently at $(git rev-parse --short HEAD)"
git log --format='   %h %s' "HEAD..$UP/$BR" | head -15 | cut -c1-150

# ── 1. merge ──
if [ "$DRY" = "1" ]; then
  if git $GIT_ID merge --no-commit --no-ff "$UP/$BR" >/dev/null 2>&1; then
    git merge --abort >/dev/null 2>&1; notify "DRY RUN: $N new commits would merge cleanly (nothing was changed)"
  else
    F=$(conflicted | tr '\n' ' '); AUTO="needs a human"; only_hook_conflicts && AUTO="only your hook files - the real run fixes these automatically"
    git merge --abort >/dev/null 2>&1; notify "DRY RUN: $N new commits conflict in: ${F:-(no file list - maybe a file in the way)}($AUTO; nothing was changed)"
  fi
  exit 0
fi
MERGE_OUT=$(git $GIT_ID merge --no-edit "$UP/$BR" 2>&1); MRC=$?
if [ "$MRC" -ne 0 ]; then
  if resolve_hooks; then
    say "conflicts only in your hook files - resolved automatically"
  else
    F=$(conflicted | tr '\n' ' '); git merge --abort >/dev/null 2>&1
    echo "$MERGE_OUT" | tail -5 | sed 's/^/   merge: /'
    fail "$N new commits CONFLICT with your changes in: ${F:-(no file list - maybe an untracked file is in the way; see the log)}- nothing changed, a human has to merge"
  fi
fi
reapply_hooks || { rollback; fail "merged, but your book hooks could not be re-applied cleanly - rolled back"; }
no_markers || { rollback; fail "merged, but conflict markers were found in the code - rolled back"; }
NEW=$(git rev-parse --short HEAD)

# ── 2. build and test in a throwaway container (the running bot is untouched until step 3) ──
$DC build fxagents >/dev/null 2>&1 || { rollback; fail "merge of $N commits ok, but the image did not BUILD - rolled back"; }
OUT=$(timeout "$TEST_TIMEOUT" $DC run --rm --no-deps -T -e FX_NO_LOCAL_CONFIG=1 fxagents python -m pytest -q -p no:cacheprovider tests 2>&1); RC=$?
say "tests exit code $RC: $(echo "$OUT" | tail -2 | tr '\n' ' ')"
[ "$RC" -eq 0 ] || { rollback; fail "merge ok, but the TESTS FAILED ($(echo "$OUT" | tail -1 | cut -c1-80)) - rolled back"; }

# ── 3. restart and watch ──
SERVICES="fxagents"; $DC config --services 2>/dev/null | grep -qx fxbt && SERVICES="fxagents fxbt"
$DC up -d $SERVICES >/dev/null 2>&1 || { rollback; fail "could not restart the bot - rolled back"; }
healthy || { rollback; fail "the new version did not answer /healthz - rolled back"; }
sleep "${SETTLE:-45}"
healthy || { rollback; fail "the new version crashed after starting - rolled back"; }

# ── 4. keep your GitHub in sync ──
if git push -q "$ORIGIN" "$BR" >/dev/null 2>&1; then
  notify "updated OK: $N commits merged, tests passed, bot healthy, saved to GitHub ($NEW)"
else
  notify "updated OK and running ($NEW), but the push to your GitHub failed - run: cd ~/fx-agents && git push origin $BR"
fi
exit 0
