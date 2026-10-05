#!/bin/bash
set -u
ok=0; fail=0
pass(){ echo "  OK  $*"; ok=$((ok+1)); }
bad(){ echo "  FAIL $*"; fail=$((fail+1)); }
echo "=== CHECK lab03-deploy-docs ==="

[[ -d ~/www/public/html && -d ~/www/public/assets ]] && pass "public tree" || bad "public"
[[ -d ~/www/private/drafts && -d ~/www/private/secrets ]] && pass "private tree" || bad "private"
[[ -f ~/www/public/html/index.html ]] && pass "html movido" || bad "html"
[[ -f ~/www/public/assets/style.css ]] && pass "assets" || bad "assets"
[[ -f ~/www/private/drafts/draft-intro.txt ]] && pass "drafts" || bad "drafts"
[[ -f ~/www/private/secrets/secret-token.txt ]] && pass "secrets" || bad "secrets"
if find ~/www ~/site-src -type f -name '*OLD*' 2>/dev/null | grep -q .; then
  bad "quedan OLD"
else
  pass "sin OLD"
fi
[[ -L ~/www/docs ]] && pass "symlink docs" || bad "symlink"
[[ -f ~/www-public.tar.xz ]] && pass "tar.xz" || bad "tar"
[[ -s ~/www-public-list.txt ]] && pass "list" || bad "list"
[[ "$(stat -c '%G' ~/www/private)" == "webadmins" ]] && pass "webadmins" || bad "grupo"
[[ "$(stat -c '%a' ~/www/private)" == "750" ]] && pass "private 750" || bad "750"
[[ "$(stat -c '%a' ~/www/public)" == "755" ]] && pass "public 755" || bad "755"
[[ -f ~/www/private/secrets/hosts.copy ]] && pass "hosts.copy" || bad "hosts.copy"
[[ -s ~/www_size.txt ]] && pass "www_size" || bad "size"
echo "=== $ok OK, $fail FAIL ==="
[[ "$fail" -eq 0 ]]
