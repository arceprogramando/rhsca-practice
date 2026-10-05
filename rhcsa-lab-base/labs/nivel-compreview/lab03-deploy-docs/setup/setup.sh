#!/bin/bash
set -euo pipefail
H="$HOME"
echo "==> Lab03 setup"

if ! getent group webadmins >/dev/null; then
  sudo groupadd webadmins
fi

rm -rf "$H/site-src" "$H/www" "$H/www-public.tar.xz" \
  "$H/www-public-list.txt" "$H/www-public-errors.txt" "$H/www_size.txt"
mkdir -p "$H/site-src"

echo '<h1>Home</h1>' > "$H/site-src/index.html"
echo '<h1>About</h1>' > "$H/site-src/about.html"
echo 'body{}' > "$H/site-src/style.css"
echo 'PNGFAKE' > "$H/site-src/logo.png"
echo 'borrador' > "$H/site-src/draft-intro.txt"
echo 'clave' > "$H/site-src/secret-token.txt"
echo 'viejo' > "$H/site-src/index-OLD.html"
echo 'cssviejo' > "$H/site-src/style-OLD.css"

echo "==> Setup listo."
