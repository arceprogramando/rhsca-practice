#!/bin/bash

shopt -s nullglob
files=( * )

if [ ${#files[@]} -eq 0 ]; then
    echo 'No hay archivos aca'
    exit 0
fi

tmp=$(mktemp)
for f in "${files[@]}"; do
    [ -f "$f" ] || continue
    sha256sum -- "$f"
done > "$tmp"

echo 'Archivos repetidos encontrados'
echo

cut -d' ' -f1 "$tmp" | sort | uniq -d | while read -r hash; do
    echo "==Duplicados por hash ${hash:0:12}"
    grep "^$hash" "$tmp" | while read -r _h file; do
    echo " $file"
    done
    echo
done

echo 'Se conservara el primero de cada grupo y se borraran los demas.'
read -r -p "Confirmar borrado de repetidos?(s/N):" ans
if [ "$ans" != "s" ] && [ "$ans" != "S" ]; then
    echo "Cancelado"
    rm -f "$tmp"
    exit 1
fi

cut -d' ' -f1 "$tmp" | sort | uniq -d | while read -r hash; do
    first=1
    grep "^$hash" "$tmp" | while read -r _h file; do
        if [ "$first" -eq 1 ]; then
             echo "Conservo: $file"
             first=0
        else
            rm -v -- "$file"
        fi
    done
done

rm -f "$tmp"
echo "Listo"


