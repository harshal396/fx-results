#!/usr/bin/env bash
# share_check.sh - audit a git repo for secrets, then build a clean copy (no history) that is safe to hand over.
#
# Usage (run inside the repo):   bash share_check.sh
# Output: a report in the terminal, and a clean copy in ~/fx-share (plus ~/fx-share.zip if zip is installed).
# It never prints a full secret: matches are masked to their first 4 characters.
# It only reads your repo. It changes nothing in it.

set -u
REPO="$(git rev-parse --show-toplevel 2>/dev/null)" || { echo "Run this inside the git repo."; exit 1; }
cd "$REPO"
OUT="${OUT:-$HOME/fx-share}"
bad=0

# Patterns that look like secrets (extended regex)
PATTERNS='[0-9a-f]{32}-[0-9a-f]{32}'                      # OANDA API token
PATTERNS+='|\b[0-9]{3}-[0-9]{3}-[0-9]{6,8}-[0-9]{3}\b'     # OANDA account id
PATTERNS+='|[0-9]{8,10}:[A-Za-z0-9_-]{35}'                 # Telegram bot token
PATTERNS+='|AKIA[0-9A-Z]{16}'                              # AWS access key
PATTERNS+='|gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,}'   # GitHub tokens
PATTERNS+='|-----BEGIN [A-Z ]*PRIVATE KEY-----'            # private keys
PATTERNS+='|eyJhIjoi[A-Za-z0-9_=-]{40,}'                   # Cloudflare tunnel token
PATTERNS+='|(TOKEN|SECRET|PASSWORD|PASSWD|API_?KEY|NTFY_TOPIC|ACCOUNT_?ID)[A-Z_]*[[:space:]]*[=:][[:space:]]*["'"'"']?[A-Za-z0-9._/+-]{8,}'

mask() { sed -E 's/(.{4}).*/\1***/'; }

echo "== 1. Sensitive-looking files that are tracked by git"
files=$(git ls-files | grep -iE '(^|/)\.env($|\.)|\.pem$|\.key$|id_rsa|\.p12$|\.pfx$|credentials|secrets?\.|\.sqlite3?$|\.db$|\.log$|(^|/)data/|\.csv$' | grep -viE '\.example$|\.sample$')
if [ -n "$files" ]; then echo "$files" | sed 's/^/   FOUND: /'; bad=1; else echo "   none"; fi

echo; echo "== 2. Secret-looking text in the CURRENT files"
hits=$(git grep -nIE "$PATTERNS" -- . ':!share_check.sh' 2>/dev/null | grep -vE '\.example:|\.sample:' || true)
if [ -n "$hits" ]; then
  echo "$hits" | while IFS= read -r l; do f=${l%%:*}; rest=${l#*:}; n=${rest%%:*}; echo "   $f line $n: $(echo "${rest#*:}" | grep -oE "$PATTERNS" | head -1 | mask)"; done
  bad=1
else echo "   none"; fi

echo; echo "== 3. Secret-looking text anywhere in the HISTORY (deleted files count)"
hist=$(git log --all -p --no-color 2>/dev/null | grep -E '^(\+\+\+ |\+)' | grep -E "$PATTERNS" | grep -vE '\.example|\.sample' | grep -oE "$PATTERNS" | sort -u | mask)
if [ -n "$hist" ]; then echo "$hist" | sed 's/^/   in history: /'; echo "   -> Revoke these secrets. History keeps them even if the file is deleted."; bad=1; else echo "   none"; fi

echo; echo "== 4. .gitignore covers the usual leaks?"
for p in ".env" "*.pem" "*.csv" "*.log" "data/"; do
  if git check-ignore -q "$p" 2>/dev/null || grep -qxF "$p" .gitignore 2>/dev/null; then echo "   ok:      $p"; else echo "   MISSING: $p"; bad=1; fi
done

echo; echo "== 5. Remotes and identity that would be visible"
git remote -v | sed 's/^/   /'
echo "   commit authors: $(git log --all --format='%an <%ae>' | sort -u | tr '\n' ';')"

echo; echo "== 6. Building a clean copy in $OUT (no history, no ignored or sensitive files)"
rm -rf "$OUT"; mkdir -p "$OUT"
git archive HEAD | tar -x -C "$OUT"
cd "$OUT"
find . \( -iname '.env' -o -iname '.env.*' -o -iname '*.pem' -o -iname '*.key' -o -iname 'id_rsa*' -o -iname '*.log' -o -iname '*.db' -o -iname '*.sqlite*' \) \
     ! -iname '*.example' ! -iname '*.sample' -print -delete 2>/dev/null | sed 's/^/   removed: /'
find . -iname '*.csv' -print -delete 2>/dev/null | sed 's/^/   removed: /'
rm -rf ./data ./.git
[ -f .env.example ] || printf '# Copy to .env and fill in your OWN values. Never commit .env.\nOANDA_TOKEN=\nOANDA_ACCOUNT_ID=\nNTFY_TOPIC=\n' > .env.example
printf '.env\n*.pem\n*.key\n*.csv\n*.log\ndata/\n' >> .gitignore
# the same pattern check on the clean copy
left=$(grep -rIlE "$PATTERNS" . 2>/dev/null | grep -vE '\.example$|\.sample$' || true)
if [ -n "$left" ]; then echo "   STILL contains secret-like text (edit these before sharing):"; echo "$left" | sed 's/^/     /'; bad=1; else echo "   clean copy: no secret-like text found"; fi
git init -q && git add -A && git -c user.name="share" -c user.email="share@localhost" commit -qm "clean copy" && echo "   fresh git history: 1 commit"
cd "$HOME" && command -v zip >/dev/null && zip -qr fx-share.zip "$(basename "$OUT")" && echo "   zip: $HOME/fx-share.zip"

echo
if [ $bad -eq 0 ]; then echo "RESULT: nothing risky found. Still read the clean copy once before sending."
else echo "RESULT: problems found above. Fix or revoke them first. Do NOT send the original repo; the clean copy is safer."; fi
echo "Reminder: change the OANDA token before you share, and tell your friend to use their own account and token."
