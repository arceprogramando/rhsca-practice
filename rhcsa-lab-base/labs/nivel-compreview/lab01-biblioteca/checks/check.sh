#!/bin/bash
# Autocheck lab01 — no es el grader de Red Hat; solo ayuda local.
set -u
ok=0; fail=0
pass(){ echo "  OK  $*"; ok=$((ok+1)); }
bad(){ echo "  FAIL $*"; fail=$((fail+1)); }

echo "=== CHECK lab01-biblioteca ==="

[[ -f ~/user_backup.tar.gz ]] && pass "user_backup.tar.gz existe" || bad "falta user_backup.tar.gz"
if [[ -f ~/user_backup.tar.gz ]]; then
  tar -tzf ~/user_backup.tar.gz 2>/dev/null | grep -q 'user_info.txt' \
    && pass "tar contiene user_info.txt" || bad "tar sin user_info.txt"
  tar -tzf ~/user_backup.tar.gz 2>/dev/null | grep -q 'user_passwords.txt' \
    && pass "tar contiene user_passwords.txt" || bad "tar sin user_passwords.txt"
fi

[[ -s ~/etc_success.txt ]] && pass "etc_success.txt no vacío" || bad "etc_success.txt"
[[ -f ~/etc_errors.txt ]] && pass "etc_errors.txt existe" || bad "etc_errors.txt"

[[ -d ~/mutt-rc ]] && pass "mutt-rc/" || bad "falta mutt-rc/"
compgen -G ~/mutt-rc/*.rc >/dev/null && pass "hay *.rc en mutt-rc" || bad "sin *.rc en mutt-rc"

[[ -d ~/books/fiction/mystery ]] && pass "estructura fiction/mystery" || bad "estructura books"
[[ -L ~/books/fiction/crime ]] && pass "symlink crime" || bad "falta symlink crime"
target=$(readlink -f ~/books/fiction/crime 2>/dev/null || true)
[[ "$target" == "$(readlink -f ~/books/fiction/mystery)" ]] && pass "crime → mystery" || bad "crime no apunta a mystery"

# no deben quedar archivos con dígito >=4 en el nombre bajo books (excepto dirs)
if find ~/books -type f -name '*[4-9]*' 2>/dev/null | grep -q .; then
  bad "quedan archivos con dígito >=4: $(find ~/books -type f -name '*[4-9]*' | tr '\n' ' ')"
else
  pass "sin archivos con dígito >=4"
fi

compgen -G ~/books/nonfiction/travel/*.pdf >/dev/null && pass "travel/*.pdf" || bad "travel sin .pdf"

[[ -d ~/books/nonfiction/children ]] && pass "children copiado a nonfiction" || bad "falta nonfiction/children"

grp=$(stat -c '%G' ~/books 2>/dev/null || echo '')
[[ "$grp" == "librarians" ]] && pass "grupo librarians" || bad "grupo books=$grp (esperaba librarians)"
mode=$(stat -c '%a' ~/books 2>/dev/null || echo '')
[[ "$mode" == "775" ]] && pass "permisos 775" || bad "permisos books=$mode (esperaba 775)"

[[ -s ~/books_size.txt ]] && pass "books_size.txt" || bad "falta books_size.txt"

echo "=== Resultado: $ok OK, $fail FAIL ==="
[[ "$fail" -eq 0 ]]
