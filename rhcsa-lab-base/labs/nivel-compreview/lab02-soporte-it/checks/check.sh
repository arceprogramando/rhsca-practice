#!/bin/bash
set -u
ok=0; fail=0
pass(){ echo "  OK  $*"; ok=$((ok+1)); }
bad(){ echo "  FAIL $*"; fail=$((fail+1)); }
echo "=== CHECK lab02-soporte-it ==="

[[ -d ~/tickets/open && -d ~/tickets/closed && -d ~/tickets/attachments ]] \
  && pass "dirs tickets" || bad "estructura tickets"
[[ -f ~/tickets/closed/INC-1002-DONE.txt ]] && pass "DONE en closed" || bad "DONE"
[[ -f ~/tickets/open/INC-1001.txt ]] && pass "open INC" || bad "open"
[[ -f ~/tickets/attachments/secure.log ]] && pass "log en attachments" || bad "logs"
[[ ! -e ~/tickets/attachments/app-TMP.log && ! -e ~/tickets/attachments/debug-tmp.log ]] \
  && pass "TMP/tmp borrados" || bad "quedan TMP/tmp"
[[ -s ~/tickets/inventory.txt ]] && pass "inventory" || bad "inventory"
[[ -s ~/tickets/attachments/auth-snippet.txt ]] && pass "auth-snippet" || bad "auth-snippet"
[[ -f ~/bash_users.txt ]] && pass "bash_users" || bad "bash_users"
[[ -f ~/client-pack.tar.xz ]] && pass "client-pack.tar.xz" || bad "tar.xz"
[[ -d ~/tickets/backup-open ]] && pass "backup-open" || bad "backup-open"
[[ "$(stat -c '%G' ~/tickets)" == "helpdesk" ]] && pass "grupo helpdesk" || bad "grupo"
[[ "$(stat -c '%a' ~/tickets)" == "770" ]] && pass "770" || bad "permisos"
[[ -L ~/mesa-ayuda ]] && pass "symlink mesa-ayuda" || bad "symlink"
[[ -s ~/tickets_size.txt ]] && pass "tickets_size" || bad "size"
echo "=== $ok OK, $fail FAIL ==="
[[ "$fail" -eq 0 ]]
