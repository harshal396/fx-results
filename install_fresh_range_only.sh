#!/usr/bin/env bash
# install_fresh_range_only.sh - the fresh-cross rule applies in range mode only (Nov 2 2026).
# Trend mode (CHOP under 50): a signal a few candles after the EMA cross is taken. Range mode (CHOP 50 to 58): unchanged.
# Run:  bash ~/install_fresh_range_only.sh        Check only (changes nothing):  DRY=1 bash ~/install_fresh_range_only.sh
# It changes nothing unless ALL of these hold, in order:
#   1. you are on main with no uncommitted changes, no update is running, and my_books.py / test_liquidity_line.py accept the
#      patch (checked with `git apply --check` first)
#   2. the image builds and the FULL test suite passes in a throwaway container (the running bot is untouched until now)
#   3. the restarted bot answers /healthz and keeps answering 45 s later
# Any failure after step 1 puts the code back exactly as it was. Only after a healthy restart is it pushed to GitHub.
set -u
REPO="${REPO:-$HOME/fx-agents}"; BR="${BR:-main}"; ORIGIN="${ORIGIN:-origin}"; DRY="${DRY:-0}"
LOG="${LOG:-$HOME/install_fresh_range_only.log}"; LOCK="${LOCK:-/tmp/fx-auto-update.lock}"; TEST_TIMEOUT="${TEST_TIMEOUT:-2400}"
DC="docker compose"
exec > >(tee -a "$LOG") 2>&1
say() { echo "$(date '+%F %T') $*"; }
notify() {
  local t; t=$(grep -E '^NTFY_TOPIC=' "$REPO/.env" 2>/dev/null | tail -1 | cut -d= -f2- | tr -d "\"' ")
  [ -n "$t" ] && curl -fsS -m 15 -d "FX fresh-cross install: $*" "https://ntfy.sh/$t" >/dev/null 2>&1
  say "$*"; return 0
}
die() { notify "STOPPED, nothing changed: $*"; exit 1; }
cd "$REPO" || { say "no such folder: $REPO"; exit 1; }
exec 9>"$LOCK"; flock -n 9 || die "an update is running - try again in 15 minutes"
[ "$(git rev-parse --abbrev-ref HEAD)" = "$BR" ] || die "the repo is not on $BR"
[ -z "$(git status --porcelain)" ] || die "the repo has uncommitted changes - commit or undo them first"
grep -q trend_chop_max fxagents/agents/my_books.py || die "the trend-mode install (b59a675) is not here - run that one first"
grep -q fresh_range_only fxagents/agents/my_books.py && die "already installed (my_books.py has fresh_range_only)"
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
base64 -d > "$T/fresh.patch" <<'B64'
ZGlmZiAtLWdpdCBhL2Z4YWdlbnRzL2FnZW50cy9teV9ib29rcy5weSBiL2Z4YWdlbnRzL2FnZW50
cy9teV9ib29rcy5weQppbmRleCBjY2E2ZDVmLi5kNGVlZTdkIDEwMDY0NAotLS0gYS9meGFnZW50
cy9hZ2VudHMvbXlfYm9va3MucHkKKysrIGIvZnhhZ2VudHMvYWdlbnRzL215X2Jvb2tzLnB5CkBA
IC0yNiw2ICsyNiw4IEBAIE1vZGVzIChmaXhlZCBhdCBlbnRyeSBmcm9tIENIT1AoMTQpIG9mIHRo
ZSBib29rJ3Mgb3duIHRpbWVmcmFtZTsgbG9nZ2VkIG9uIHRoZSB0CiAgICAgICAgICAgICAgIChK
ZXYgb25seSBmcm9tICsyUiksIHdoaWNoZXZlciBjb21lcyBmaXJzdC4KICAgcmFuZ2UgbW9kZSAg
Q0hPUCA1MCAuLiBjaG9wX21heCAoNTgpOiBhcyBiZWZvcmU6IEpldiBwYXJ0aWFscyBmcm9tICsw
LjVSIChoYWxmIG9mIHdoYXQgaXMgb3BlbiwgYXQgbW9zdCBtYXhfcGFydGlhbHMgPSAyLCB0aGUK
ICAgICAgICAgICAgICAgbGlxdWlkaXR5LWxpbmUgcGFydGlhbCBjb3VudHMgYXMgb25lIG9mIHRo
ZW0pIGFuZCB0aGUgMiB4IEFUUiB0cmFpbCBhZnRlciArMVIuCitUaGUgZnJlc2gtY3Jvc3MgZ2F0
ZSAoZnJlc2gsIDE1bSAvIDFoIGJvb2tzKSBhcHBsaWVzIGluIHJhbmdlIG1vZGUgb25seTogaW4g
dHJlbmQgbW9kZSAoQ0hPUCA8IDUwKSBhbiBlbnRyeSB0aGF0IGZpcmVzIGEgZmV3IGNhbmRsZXMK
K2FmdGVyIHRoZSBjcm9zcyBpcyB0YWtlbiwgYXMgbG9uZyBhcyB0aGUgUlNJIHRyaWdnZXIgYW5k
IHRoZSBvdGhlciBnYXRlcyBwYXNzIChmcmVzaF9yYW5nZV9vbmx5LCBOb3YgMiAyMDI2KS4KIE5v
IG5ldyBlbnRyaWVzIGluIHRoZSBub19lbnRyeV9zeW1ib2xzIChVUzMwKTsgYSBVUzMwIHRyYWRl
IHRoYXQgaXMgYWxyZWFkeSBvcGVuIGlzIG1hbmFnZWQgdG8gaXRzIGVuZC4KIEV4aXQ6IHRoZSBm
aXJzdCBjb21wbGV0ZWQgY2FuZGxlIHRoYXQgY2xvc2VzIGJhY2sgYWNyb3NzIEVNQTIxICh0aGUg
cG9zaXRpb24gbWFuYWdlciBjbG9zZXMgaXQgb24gdGhlIG5leHQKIGJhcikgb3IgdGhlIGR5bmFt
aWMgc3RvcCwgd2hpY2hldmVyIGNvbWVzIGZpcnN0LiBQYXJ0aWFsIHByb2ZpdDogb25jZSBhIHRy
YWRlIGlzICswLjVSIG9yIGJldHRlciwgSmV2IGlzIGFza2VkIGF0IGV2ZXJ5CkBAIC03NCw2ICs3
Niw3IEBAIERFRkFVTFRTID0geyJzeW1ib2xzIjogWyJYQVVVU0QiLCAiTkRRIiwgIlVTMzAiXSwg
InJpc2tfcGN0IjogMC4wMDUsICJzdG9wX2xvb2tiCiAgICAgICAgICAgICAidXNlX3BhcnRpYWxz
IjogVHJ1ZSwgInBhcnRpYWxfbWluX3IiOiAwLjUsICJwYXJ0aWFsX2JlbG93IjogMC40NSwgInBh
cnRpYWxfZnJhY3Rpb24iOiAwLjUsICJtYXhfcGFydGlhbHMiOiAyLAogICAgICAgICAgICAgIm5v
X2VudHJ5X3N5bWJvbHMiOiBbIlVTMzAiXSwgICAgICAgICAgICAgICAgICAgICMgb3BlbiBVUzMw
IHRyYWRlcyBhcmUgc3RpbGwgbWFuYWdlZDsgbm8gbmV3IG9uZXMgKE9jdCAzMCAyMDI2KQogICAg
ICAgICAgICAgInRyZW5kX21vZGUiOiBUcnVlLCAidHJlbmRfY2hvcF9tYXgiOiA1MC4wLCAgICAg
ICMgQ0hPUCgxNCkgYXQgZW50cnkgYmVsb3cgdGhpcyA9IHRyZW5kIG1vZGUsIGVsc2UgcmFuZ2Ug
bW9kZQorICAgICAgICAgICAgImZyZXNoX3JhbmdlX29ubHkiOiBUcnVlLCAgICAgICAgICAgICAg
ICAgICAgICAgICMgdGhlIGZyZXNoLWNyb3NzIGdhdGUgYXBwbGllcyBpbiByYW5nZSBtb2RlIG9u
bHkgKE5vdiAyIDIwMjYpCiAgICAgICAgICAgICAidHJlbmRfamV2X21pbl9yIjogMi4wLCAidHJl
bmRfcGFydGlhbF9mcmFjdGlvbiI6IDEgLyAzfSAgICMgdHJlbmQgbW9kZTogb25lIHBhcnRpYWwg
b2YgMS8zLCBKZXYgb25seSBmcm9tICsyUgogREVGQVVMVFMudXBkYXRlKExJUV9ERUZBVUxUUykg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAjIGxpcXVpZGl0eS1saW5lIHBh
cnRpYWwgKGFnZW50cy9saXF1aWRpdHlfbGluZS5weSksIG9uIGZvciBldmVyeSBib29rCiBINF9I
T1VSUyA9ICgxLCA1LCA5LCAxMywgMTcsIDIxKSAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICMgNGggY2FuZGxlcyBlbmQgYXQgdGhlc2UgTmV3IFlvcmsgaG91cnMKQEAgLTQ1
Myw3ICs0NTYsMTAgQEAgY2xhc3MgTXlCb29rVHJhZGVyKExpcXVpZGl0eU1peGluLCBfQmFzZSk6
CiAgICAgICAgICAgICBybmcgPSBmbG9hdChiLmguaWxvY1stMV0gLSBiLmwuaWxvY1stMV0pIC8g
YQogICAgICAgICAgICAgaWYgcm5nID4gc2VsZi5za2lwX2JpZzoKICAgICAgICAgICAgICAgICBy
ZXR1cm4gc2VsZi5fcmVqZWN0KHJlYywgZiJvdmVyc2l6ZWQgc2lnbmFsIGNhbmRsZSAoe3JuZzou
MWZ9IEFUUiwgbGltaXQge3NlbGYuc2tpcF9iaWc6Z30pIikKLSAgICAgICAgaWYgc2VsZi5mcmVz
aDoKKyAgICAgICAgY2hvcDAgPSBmbG9hdChiLmNob3AuaWxvY1stMV0pCisgICAgICAgIHRyZW5k
X2VudHJ5ID0gYm9vbChzZWxmLmNbInRyZW5kX21vZGUiXSkgYW5kIGJvb2woc2VsZi5jWyJmcmVz
aF9yYW5nZV9vbmx5Il0pIGFuZCBucC5pc2Zpbml0ZShjaG9wMCkgXAorICAgICAgICAgICAgYW5k
IGNob3AwIDwgZmxvYXQoc2VsZi5jWyJ0cmVuZF9jaG9wX21heCJdKSAgICAgICAgICAgICAgICMg
dHJlbmQgbW9kZTogYSBzaWduYWwgbGF0ZSBpbiB0aGUgbW92ZSBpcyB3ZWxjb21lCisgICAgICAg
IGlmIHNlbGYuZnJlc2ggYW5kIG5vdCB0cmVuZF9lbnRyeToKICAgICAgICAgICAgIHNnID0gbnAu
c2lnbihiLmMudG9fbnVtcHkoKSAtIGIuZW1hMjEudG9fbnVtcHkoKSkKICAgICAgICAgICAgIGkg
PSBsZW4oc2cpIC0gMQogICAgICAgICAgICAgcnVuID0gMQpkaWZmIC0tZ2l0IGEvdGVzdHMvdGVz
dF9saXF1aWRpdHlfbGluZS5weSBiL3Rlc3RzL3Rlc3RfbGlxdWlkaXR5X2xpbmUucHkKaW5kZXgg
NmY1MTJiYy4uNDdlYjIyOCAxMDA2NDQKLS0tIGEvdGVzdHMvdGVzdF9saXF1aWRpdHlfbGluZS5w
eQorKysgYi90ZXN0cy90ZXN0X2xpcXVpZGl0eV9saW5lLnB5CkBAIC00MTgsMyArNDE4LDcyIEBA
IGRlZiB0ZXN0X2Fkb3B0X3Jlc3RvcmVzX3RoZV9tb2RlX2FuZF90aGVfYm9va2VkX3BhcnRpYWxf
YW5kX29sZF90cmFkZXNfY291bnRfYXNfCiAgICAgYSwgYjIgPSBoLnN0YXRlLnBvc2l0aW9uc1si
YTEiXSwgaC5zdGF0ZS5wb3NpdGlvbnNbImIyIl0KICAgICBhc3NlcnQgYS5tZXRhWyJtb2RlIl0g
PT0gInRyZW5kIiBhbmQgYS5vcGVuX3F0eSA9PSA2LjAgYW5kIGEucGFydGlhbF9kb25lCiAgICAg
YXNzZXJ0IGIyLm1ldGFbIm1vZGUiXSA9PSAicmFuZ2UiCisKKworIyDilIDilIAgdGhlIGZyZXNo
LWNyb3NzIGdhdGUgYXBwbGllcyBpbiByYW5nZSBtb2RlIG9ubHkg4pSA4pSACitkZWYgX2VudGVy
KGNob3AsIHJ1biwgb3Zlcj1Ob25lLCBmcmVzaD0yKToKKyAgICAiIiJPbmUgMTVtIHNob3J0IHNp
Z25hbCB3aG9zZSBwcmljZSBoYXMgYmVlbiBiZWxvdyB0aGUgRU1BMjEgZm9yIGBydW5gIGNhbmRs
ZXMsIENIT1AgPSBgY2hvcGAuIFJldHVybnMgd2hhdCBvcGVuX3ZpcnR1YWwgc2F3LiIiIgorICAg
IG1iID0gX21iKCkKKyAgICBzZWVuID0gW10KKworICAgIGNsYXNzIFByb2JlKG1iLk15Qm9va1Ry
YWRlcik6CisgICAgICAgIGFzeW5jIGRlZiBvcGVuX3ZpcnR1YWwoc2VsZiwgc3ltLCBzaWRlLCBt
aWQsIGUwLCBzdG9wLCBkaXN0LCBhLCByZWMsIHdoeSwgbWV0YSwgZyk6CisgICAgICAgICAgICBz
ZWVuLmFwcGVuZCgobWV0YS5nZXQoIm1vZGUiKSwgbWV0YS5nZXQoImNob3AiKSkpOyByZXR1cm4g
VHJ1ZQorCisgICAgICAgIGFzeW5jIGRlZiBqZXZfZ3JhZGUoc2VsZiwgKmEsICoqayk6CisgICAg
ICAgICAgICByZXR1cm4gTm9uZQorCisgICAgICAgIGRlZiBlbnRyeV9hbGxvd2VkKHNlbGYsICph
LCAqKmspOgorICAgICAgICAgICAgcmV0dXJuIFRydWUKKworICAgICAgICBkZWYgX3JlamVjdChz
ZWxmLCByZWMsIHdoeSk6CisgICAgICAgICAgICBzZWVuLmFwcGVuZCgoInJlamVjdGVkIiwgd2h5
WzoyNF0pKQorCisgICAgbiA9IDYwCisgICAgaWR4ID0gcGQuZGF0ZV9yYW5nZShUMCwgcGVyaW9k
cz1uLCBmcmVxPSIxNW1pbiIpCisgICAgcCA9IDEwMC4wICsgbnAuemVyb3MobikKKyAgICBlbWEg
PSBucC53aGVyZShucC5hcmFuZ2UobikgPCBuIC0gcnVuLCBwIC0gMS4wLCBwICsgMS4wKSAgICAg
ICAgICAgICMgcHJpY2UgYWJvdmUgdGhlIEVNQTIxLCB0aGVuIGJlbG93IGl0IGZvciB0aGUgbGFz
dCBgcnVuYAorICAgIGIgPSBwZC5EYXRhRnJhbWUoeyJvIjogcCwgImgiOiBwICsgMSwgImwiOiBw
IC0gMSwgImMiOiBwLCAiYXRyIjogMS4wLCAiZW1hMjEiOiBlbWEsICJyc2kiOiA0MC4wLCAic3Qi
OiAtMSwKKyAgICAgICAgICAgICAgICAgICAgICAiY2hvcCI6IGZsb2F0KGNob3ApLCAicmF3Ijog
LTF9LCBpbmRleD1pZHgpCisgICAgaCA9IF90cmFkZXIoW10sIG92ZXI9b3ZlcikKKyAgICBoLl9f
Y2xhc3NfXyA9IFByb2JlCisgICAgaC51c2VfY2hvcCwgaC51c2Vfc3VwZXJ0cmVuZCwgaC5jaG9w
X21heCwgaC5mcmVzaCA9IFRydWUsIEZhbHNlLCA1OC4wLCBmcmVzaAorICAgIGgudHJlbmRfZ2F0
ZSwgaC5yc2lfbW9tZW50dW0sIGguc2tpcF9iaWcsIGguc3RvcF9jYXAsIGgudXNlX2hvdXJzID0g
RmFsc2UsIEZhbHNlLCAwLjAsIEZhbHNlLCBGYWxzZQorICAgIGguY2ZnWyJpbnN0cnVtZW50cyJd
WyJYQVVVU0QiXSA9IHsidGlja19zaXplIjogMC4wMSwgInF0eV9zdGVwIjogMC4wMSwgIm1pbl91
bml0cyI6IDAuMDEsICJzcHJlYWQiOiAwLjAsICJtdWx0aXBsaWVyIjogMS4wLCAibWF4X3VuaXRz
IjogMTAwfQorICAgIGguY2ZnWyJzcHJlYWRfcGlwcyJdID0ge30KKyAgICBoLndpbmRvd3MsIGgu
c3BlYywgaC5ydWxlID0gRmFsc2UsIG1iLlNQRUNTWyJteV9lbWFfcnNpXzE1bSJdLCAiZW1hX3Jz
aSIKKyAgICBoLnN0YXRlLmxhc3RfcHJpY2VzWyJYQVVVU0QiXSA9IDEwMC4wCisgICAgaC5jdHgu
am91cm5hbCA9IFNpbXBsZU5hbWVzcGFjZShhZGRfc2lnbmFsPWxhbWJkYSAqYSwgKiprOiBOb25l
KQorICAgIGFzeW5jaW8ucnVuKGgubWF5YmVfZW50ZXIoIlhBVVVTRCIsIGIsIGIuaW5kZXhbLTFd
ICsgcGQuVGltZWRlbHRhKCIxNW1pbiIpLCBTaW1wbGVOYW1lc3BhY2UoY2xvc2U9MTAwLjApLCAw
KSkKKyAgICByZXR1cm4gc2VlbgorCisKK2RlZiB0ZXN0X3RyZW5kX21vZGVfdGFrZXNfYV9zaWdu
YWxfbGF0ZV9pbl90aGVfbW92ZSgpOgorICAgIGFzc2VydCBfZW50ZXIoNDUsIHJ1bj01KSA9PSBb
KCJ0cmVuZCIsIDQ1LjApXQorICAgIGFzc2VydCBfZW50ZXIoNDUsIHJ1bj0zOSkgPT0gWygidHJl
bmQiLCA0NS4wKV0KKworCitkZWYgdGVzdF9yYW5nZV9tb2RlX3N0aWxsX3dhbnRzX2FfZnJlc2hf
Y3Jvc3MoKToKKyAgICBhc3NlcnQgX2VudGVyKDU1LCBydW49NSlbMF1bMF0gPT0gInJlamVjdGVk
IiBhbmQgX2VudGVyKDU1LCBydW49NSlbMF1bMV0uc3RhcnRzd2l0aCgibm90IGEgZnJlc2ggY3Jv
c3MiKQorICAgIGFzc2VydCBfZW50ZXIoNTUsIHJ1bj0yKSA9PSBbKCJyYW5nZSIsIDU1LjApXQor
ICAgIGFzc2VydCBfZW50ZXIoNTUsIHJ1bj0xKSA9PSBbKCJyYW5nZSIsIDU1LjApXQorCisKK2Rl
ZiB0ZXN0X3RoZV90cmVuZF9ib3VuZGFyeV9pc19jaG9wXzUwKCk6CisgICAgYXNzZXJ0IF9lbnRl
cig0OS45LCBydW49NSkgPT0gWygidHJlbmQiLCA0OS45KV0KKyAgICBhc3NlcnQgX2VudGVyKDUw
LjAsIHJ1bj01KVswXVswXSA9PSAicmVqZWN0ZWQiCisKKworZGVmIHRlc3RfdGhlX2dhdGVfc3Rh
eXNfb25fd2hlbl90cmVuZF9tb2RlX29yX3RoZV9yYW5nZV9vbmx5X3N3aXRjaF9pc19vZmYoKToK
KyAgICBhc3NlcnQgX2VudGVyKDQ1LCBydW49NSwgb3Zlcj17InRyZW5kX21vZGUiOiBGYWxzZX0p
WzBdWzBdID09ICJyZWplY3RlZCIKKyAgICBhc3NlcnQgX2VudGVyKDQ1LCBydW49NSwgb3Zlcj17
ImZyZXNoX3JhbmdlX29ubHkiOiBGYWxzZX0pWzBdWzBdID09ICJyZWplY3RlZCIKKyAgICBhc3Nl
cnQgX2VudGVyKDQ1LCBydW49Miwgb3Zlcj17ImZyZXNoX3JhbmdlX29ubHkiOiBGYWxzZX0pID09
IFsoInRyZW5kIiwgNDUuMCldICAgICAgICMgYSBmcmVzaCBjcm9zcyBwYXNzZXMgZWl0aGVyIHdh
eQorCisKK2RlZiB0ZXN0X3RoZV9jaG9wX2N1dG9mZl9zdGlsbF9hcHBsaWVzX2luX2JvdGhfbW9k
ZXMoKToKKyAgICByID0gX2VudGVyKDYwLCBydW49MSkKKyAgICBhc3NlcnQgciBhbmQgclswXVsw
XSA9PSAicmVqZWN0ZWQiIGFuZCByWzBdWzFdLnN0YXJ0c3dpdGgoImNob3BweSIpCisKKworZGVm
IHRlc3RfYV9taXNzaW5nX2Nob3BfcmVhZGluZ19kb2VzX25vdF9vcGVuX3RoZV9nYXRlKCk6Cisg
ICAgYXNzZXJ0IF9lbnRlcihmbG9hdCgibmFuIiksIHJ1bj01KVswXVswXSA9PSAicmVqZWN0ZWQi
Cg==
B64
git apply --check "$T/fresh.patch" 2>/dev/null || die "fxagents/agents/my_books.py or tests/test_liquidity_line.py differ from what I expect - tell me"
[ "$DRY" = "1" ] && { notify "DRY RUN OK: the patch fits; nothing was changed"; exit 0; }

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

git apply "$T/fresh.patch" || die "the patch did not apply"
git add -A && git -c user.name="${GIT_NAME:-fx}" -c user.email="${GIT_EMAIL:-fx@localhost}" commit -qm "Fresh-cross rule applies in range mode only" || fail "could not commit"
NEW=$(git rev-parse --short HEAD)
say "committed $NEW; building and running the full tests (about 12 minutes) ..."
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
  notify "installed OK ($NEW): tests passed, bot healthy, saved to GitHub"
else
  notify "installed OK and running ($NEW), but the push to your GitHub failed - run: cd ~/fx-agents && git push $ORIGIN $BR"
fi
