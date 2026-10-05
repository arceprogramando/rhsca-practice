#!/usr/bin/env bash
# =============================================================================
# Lab guiado: hard links y symbolic links (estilo RHCSA / Lab 3.1)
# Uso:
#   bash lab-links-guiado.sh          # modo automatico
#   bash lab-links-guiado.sh --pausa  # espera Enter entre pasos
# =============================================================================

set -euo pipefail

PAUSA=0
[[ "${1:-}" == "--pausa" ]] && PAUSA=1

paso() {
  echo
  echo "================================================================"
  echo " PASO $1"
  echo "================================================================"
}

explica() {
  # Imprime lineas de explicacion
  while IFS= read -r line; do
    echo "# $line"
  done
}

espera() {
  if [[ "$PAUSA" -eq 1 ]]; then
    read -r -p "Enter para continuar... " _
  fi
}

LABDIR="$HOME/lab-links-practica"
rm -rf "$LABDIR"
mkdir -p "$LABDIR"
cd "$LABDIR"

explica <<'EOF'
Vamos a practicar en: ~/lab-links-practica
Idea clave:
  - Hard link  = OTRO NOMBRE del MISMO archivo (mismo inode)
  - Soft link  = ATAJO a una RUTA (inode distinto; se puede romper)
EOF
espera

# -----------------------------------------------------------------------------
paso "1 — Crear un archivo real"
explica <<'EOF'
Creamos un archivo normal. Este es el "contenido" en disco.
EOF
espera

echo "contenido del archivo original" > archivo.txt
echo "# Comando: echo ... > archivo.txt"
ls -l archivo.txt
echo "# OK: existe archivo.txt"

# -----------------------------------------------------------------------------
paso "2 — Crear un HARD LINK"
explica <<'EOF'
ln archivo.txt hard.txt
No copia datos: crea otro nombre que apunta al MISMO inode.
Si editas hard.txt, tambien cambia archivo.txt (es el mismo).
EOF
espera

ln archivo.txt hard.txt
echo "# Comando: ln archivo.txt hard.txt"
ls -li archivo.txt hard.txt
explica <<'EOF'
Mira la primera columna (inode): debe ser IGUAL en ambos.
Mira la columna de links (despues de permisos): suele decir 2.
EOF
espera

# -----------------------------------------------------------------------------
paso "3 — Crear un SYMBOLIC LINK (soft link)"
explica <<'EOF'
ln -s archivo.txt soft.txt
Esto NO comparte inode: soft.txt guarda la ruta "archivo.txt".
Es como un acceso directo.
EOF
espera

ln -s archivo.txt soft.txt
echo "# Comando: ln -s archivo.txt soft.txt"
ls -li archivo.txt hard.txt soft.txt
echo
ls -l soft.txt
explica <<'EOF'
En ls -l el soft se ve asi:  soft.txt -> archivo.txt
El inode de soft.txt es DISTINTO al de archivo.txt/hard.txt.
EOF
espera

# -----------------------------------------------------------------------------
paso "4 — Probar que hard = mismo contenido"
explica <<'EOF'
Editamos por el hard link y leemos por el nombre original.
EOF
espera

echo "modificado via hard link" >> hard.txt
echo "# Comando: echo ... >> hard.txt"
echo "# Contenido de archivo.txt:"
cat archivo.txt
explica <<'EOF'
Viste el cambio en archivo.txt: hard link = mismo archivo.
EOF
espera

# -----------------------------------------------------------------------------
paso "5 — Renombrar un hard link (como Lab 3.1 paso 3)"
explica <<'EOF'
mv hard.txt hard-renombrado.txt
Solo cambia UN nombre. El otro nombre (archivo.txt) sigue OK.
El soft link sigue apuntando a "archivo.txt" (ruta), asi que sigue OK.
EOF
espera

mv hard.txt hard-renombrado.txt
echo "# Comando: mv hard.txt hard-renombrado.txt"
ls -li archivo.txt hard-renombrado.txt soft.txt
espera

# -----------------------------------------------------------------------------
paso "6 — Borrar el archivo al que apunta el soft link"
explica <<'EOF'
Ahora borramos archivo.txt (la ruta del soft link).
- hard-renombrado.txt SIGUE VIVO (sigue siendo un hard link al inode)
- soft.txt queda ROTO (la ruta "archivo.txt" ya no existe)
EOF
espera

rm archivo.txt
echo "# Comando: rm archivo.txt"
echo
echo "# Soft link (deberia verse roto):"
ls -l soft.txt || true
echo
echo "# Leer soft (falla):"
cat soft.txt 2>&1 || true
echo
echo "# Hard link (sigue OK):"
cat hard-renombrado.txt
explica <<'EOF'
ESTA es la leccion del examen:
  Soft link se rompe si desaparece la RUTA.
  Hard link sobrevive mientras quede ALGUN nombre al inode.
EOF
espera

# -----------------------------------------------------------------------------
paso "7 — Soft link a un directorio (tambien cae en examen)"
explica <<'EOF'
Los hard links a directorios NO se usan en la practica normal.
Los soft links a directorios SI (muy comun).
EOF
espera

mkdir mi_dir
echo "hola" > mi_dir/dentro.txt
ln -s mi_dir atajo_dir
echo "# Comando: ln -s mi_dir atajo_dir"
ls -l atajo_dir
echo "# Listar por el atajo:"
ls atajo_dir
espera

# -----------------------------------------------------------------------------
paso "8 — Limpieza del soft link roto"
explica <<'EOF'
Para borrar un soft link se borra el link, NO el destino:
  rm soft.txt
Nunca uses rm -rf sobre un soft link a directorio sin cuidado:
  mejor: rm atajo_dir   (borra el link)
  no:    rm -rf atajo_dir/  (puede borrar contenido del destino)
EOF
espera

rm -f soft.txt
rm -f atajo_dir
echo "# Soft links removidos. Queda el hard link con el contenido."
ls -li
espera

# -----------------------------------------------------------------------------
paso "9 — Mini resumen tipo examen"
explica <<'EOF'
Comandos tipicos EX200:
  ln archivo destino          # hard link
  ln -s origen destino        # symbolic link
  ls -li archivo1 archivo2    # comparar inodes
  ls -l enlace                # ver -> destino
  stat archivo                # Links: N
  find /ruta -type l          # buscar symlinks
  find /ruta -xtype l         # buscar symlinks ROTOS

Reglas de oro:
  1) Hard = mismo inode, no cruza particiones
  2) Soft = atajo a ruta, puede cruzar particiones y puede romperse
  3) Soft SI puede apuntar a directorios
EOF

echo
echo "================================================================"
echo " Lab terminado. Carpeta: $LABDIR"
echo " Para repetir con pausas: bash $HOME/lab-links-guiado.sh --pausa"
echo "================================================================"
echo
explica <<'EOF'
OPCIONAL — Lab 3.1 del libro (necesita root / sudo), idea equivalente:
  1) tar -cvf /root/essentials.tar /home /etc
  2) cp /root/essentials.tar /tmp/
     ln /root/essentials.tar /essentials.tar
  3) mv /essentials.tar /archive.tar
  4) ln -s /archive.tar /root/link.tar
  5) rm /archive.tar   # link.tar queda roto; /root/essentials.tar sigue
     rm /root/link.tar
  6) gzip /root/essentials.tar
EOF
