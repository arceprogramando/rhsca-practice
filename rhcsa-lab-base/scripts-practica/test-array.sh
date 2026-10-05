#!/bin/bash

example=(aa 'bb cc' dd)
example[3]=ee

echo -n "example[@] = ${example[@]}"
echo -e "example array contains ${#example[@]} elements"

for elt in "${example[@]}"; do
    echo " Element = $elt"
done

