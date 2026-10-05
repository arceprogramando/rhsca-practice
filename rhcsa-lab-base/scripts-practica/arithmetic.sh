#!/bin/bash

a=1
b=$((2))

c="$a + $b"
d=$(($a+$b))

echo -e "$a + $b = $c \t(plus sign as string literal)"
echo -e "$a + $b = $d \t(plus sign as arithmetic addtion)"


