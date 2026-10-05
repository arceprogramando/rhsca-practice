#!/bin/bash

suffix=BACKUP--`date +%Y%m%d-%H%M`

for script in *.sh; do
    newname="$script.$suffix"

    if [ -e "$newname" ]; then
        echo "Ya existe: $newname (no se copia)"
        continue
    fi

    echo "Copying $script to $newname"
    cp "$script" "$newname"
done
