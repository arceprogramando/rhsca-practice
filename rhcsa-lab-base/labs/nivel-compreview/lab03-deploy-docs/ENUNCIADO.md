# Lab 03 — Deploy de documentación interna (mismo nivel)

**Dónde:** trabajo principal en **servera**; al final **scp** a **workstation** (si tenés las dos).  
**Setup en servera:** `bash setup/setup.sh`

---

## Parte A — Árbol de publicación

El setup deja `~/site-src/` con HTML/TXT desordenados.

1. Creá `~/www/`:
   - `www/public/html/`
   - `www/public/assets/`
   - `www/private/drafts/`
   - `www/private/secrets/`
2. Reglas de movimiento desde `site-src/`:
   - `*.html` → `www/public/html/`
   - `*.css` / `*.png` / `*.jpg` → `www/public/assets/`
   - `draft-*.txt` → `www/private/drafts/`
   - `secret-*.txt` → `www/private/secrets/`
3. Borrá de `site-src` (y de www si se colaron) cualquier archivo con `OLD` en el nombre.
4. Enlace: `~/www/docs` → `~/www/public/html`.

## Parte B — Empaquetado y redirección

1. `find ~/www/public` exitosos → `~/www-public-list.txt`; errores → `~/www-public-errors.txt`.
2. Archivo `~/www-public.tar.xz` con el contenido de `www/public` (que al listar se vean `html/` y `assets/`).
3. `du -sh ~/www` → `~/www_size.txt`.

## Parte C — Seguridad básica de dirs

1. Grupo `webadmins` (setup).
2. `chown`/`chgrp` para que `~/www/private` sea tu usuario:`webadmins` y modo **750**.
3. `~/www/public` modo **755**.
4. Copiá `/etc/hosts` a `~/www/private/secrets/hosts.copy` (lectura normal; no hace falta shadow).

## Parte D — Cruce de VMs (opcional pero cuenta en el check si existe workstation)

Desde **workstation**:

```bash
scp felipe@servera:~/www-public.tar.xz ~/recibido-www-public.tar.xz
```

El check en servera solo valida A–C; en workstation podés verificar a mano con `ls ~/recibido-www-public.tar.xz`.

## Check (servera)

```bash
bash checks/check.sh
```
