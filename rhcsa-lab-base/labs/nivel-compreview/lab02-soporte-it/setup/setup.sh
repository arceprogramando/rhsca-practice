#!/bin/bash
set -euo pipefail
H="$HOME"
echo "==> Lab02 setup"

if ! getent group helpdesk >/dev/null; then
  sudo groupadd helpdesk
fi

rm -rf "$H/tickets" "$H/mesa-ayuda" "$H/bash_users.txt" \
  "$H/client-pack.tar.xz" "$H/tickets_size.txt"
mkdir -p "$H/tickets/inbox"

echo 'falla vpn' > "$H/tickets/inbox/INC-1001.txt"
echo 'resuelto' > "$H/tickets/inbox/INC-1002-DONE.txt"
echo 'disco' > "$H/tickets/inbox/INC-1003.txt"
echo 'ok' > "$H/tickets/inbox/INC-1004-DONE.txt"
echo 'logA' > "$H/tickets/inbox/app-TMP.log"
echo 'logB' > "$H/tickets/inbox/secure.log"
echo 'tmpfile' > "$H/tickets/inbox/debug-tmp.log"

echo "==> Setup listo. ENUNCIADO.md → luego checks/check.sh"
