#!/bin/bash
# Prepara lab01 en la VM local (NO es el lab ROL de Red Hat).
set -euo pipefail
HOME_DIR="${HOME}"
BOOKS="${HOME_DIR}/books"

echo "==> Lab01 setup en ${HOME_DIR}"

# Grupo librarians
if ! getent group librarians >/dev/null; then
  sudo groupadd librarians
  echo "    grupo librarians creado"
else
  echo "    grupo librarians ya existe"
fi

# Limpieza suave de restos previos del lab
rm -rf "${BOOKS}" "${HOME_DIR}/mutt-rc" \
  "${HOME_DIR}/user_info.txt" "${HOME_DIR}/user_passwords.txt" \
  "${HOME_DIR}/user_backup.tar.gz" "${HOME_DIR}/etc_success.txt" \
  "${HOME_DIR}/etc_errors.txt" "${HOME_DIR}/books_size.txt" \
  "${HOME_DIR}/mutt-rc-SOURCE.txt"
mkdir -p "${BOOKS}/unsorted"

# Libros de ejemplo (nombre indica categoría + número)
cat > "${BOOKS}/unsorted/fiction-children-story1.txt" <<<'kids book 1'
cat > "${BOOKS}/unsorted/fiction-children-story4.txt" <<<'kids book 4 DELETE'
cat > "${BOOKS}/unsorted/fiction-mystery-case2.txt" <<<'mystery 2'
cat > "${BOOKS}/unsorted/fiction-mystery-case5.txt" <<<'mystery 5 DELETE'
cat > "${BOOKS}/unsorted/fiction-romance-love3.txt" <<<'romance 3'
cat > "${BOOKS}/unsorted/nonfiction-dictionary-oxford1.txt" <<<'dict 1'
cat > "${BOOKS}/unsorted/nonfiction-history-rome2.txt" <<<'history 2'
cat > "${BOOKS}/unsorted/nonfiction-travel-peru3.txt" <<<'travel 3'
cat > "${BOOKS}/unsorted/nonfiction-travel-chile6.txt" <<<'travel 6 DELETE'

# Árbol falso estilo docs de mutt (por si no está instalado mutt)
FAKE="/tmp/fake-mutt-doc"
sudo rm -rf "${FAKE}"
sudo mkdir -p "${FAKE}/usr/share/doc/mutt"
echo 'set from=lab' | sudo tee "${FAKE}/usr/share/doc/mutt/sample.rc" >/dev/null
echo 'set spoolfile=' | sudo tee "${FAKE}/usr/share/doc/mutt/muttrc.rc" >/dev/null
echo "    docs falsos mutt en ${FAKE}/usr/share/doc/mutt (*.rc)"

echo "==> Setup listo. Leé ENUNCIADO.md y resolvé sin mirar checks/."
echo "    Luego: bash checks/check.sh"
