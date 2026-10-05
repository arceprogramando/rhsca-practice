# Lab 01 — Biblioteca (nivel compreview RH104)

**Dónde:** resolvé en **servera** como tu usuario (ej. `felipe`).  
**Estilo:** enunciado corto tipo examen (sin pasos).  
**Setup previo:** `bash setup/setup.sh`

---

## Objetivos

Organizar archivos, redirección, filtrado, `tar`, enlaces, ownership y permisos.

---

## Parte A — Soporte / auditoría

1. Copiá `/etc/passwd` a `~/user_info.txt` y `/etc/shadow` a `~/user_passwords.txt` (shadow requiere `sudo`).
2. Editá ambos para dejar **solo cuentas humanas** (UID ≥ 1000, y sin `nfsnobody`/`nobody` si aparece). Sacá cuentas de sistema.
3. Creá el archivo comprimido `~/user_backup.tar.gz` que contenga **solo** `user_info.txt` y `user_passwords.txt` (desde tu home).
4. Inventario de `/etc`:
   - lista exitosa → `~/etc_success.txt` (stdout)
   - errores → `~/etc_errors.txt` (stderr)  
   Usá un `find` sobre `/etc` (va a haber denegados: eso va a stderr).
5. Buscá documentación de `mutt` bajo `/usr` cuyo path contenga `doc`. Copiá todos los `*.rc` de ese árbol a `~/mutt-rc/` (creá el dir).  
   Si no hay `mutt` instalado, el setup deja un árbol falso en `/tmp/fake-mutt-doc` — usalo como fuente y documentalo creando también `~/mutt-rc-SOURCE.txt` con una línea: la ruta que usaste.

## Parte B — Libros del cliente

Estado inicial (lo crea el setup): `~/books/unsorted/` con varios “libros”.

1. Creá esta estructura (si falta alguna carpeta):

```text
books/
  fiction/children/
  fiction/mystery/
  fiction/romance/
  nonfiction/dictionary/
  nonfiction/history/
  nonfiction/travel/
  unsorted/
```

2. Mové cada archivo de `unsorted` a la categoría que indique su **nombre** (ej. `fiction-mystery-...` → `fiction/mystery/`).
3. Borrá cualquier libro cuyo nombre contenga un dígito **≥ 4** (4, 5, 6…).
4. En `~/books/nonfiction/travel/`, renombrá todos los archivos para que terminen en `.pdf` (cambiá la extensión).
5. Creá el enlace simbólico `~/books/fiction/crime` → `~/books/fiction/mystery`.

## Parte C — Permisos y tamaño

1. Copiá recursivamente `~/books/fiction/children` dentro de `~/books/nonfiction/`.
2. Grupo dueño de `~/books`: `librarians` (el setup crea el grupo; usá `sudo`).
3. Permisos de `~/books` (dir): dueño y grupo `rwx`, otros `r-x` → típico **775**.
4. Guardá el tamaño human-readable de `~/books` en `~/books_size.txt` (una línea, estilo `du -sh`, ej. `13M` o el valor que salga).

## Entrega / check

```bash
bash checks/check.sh
```

Opcional: desde **workstation**, bajá el backup:

```bash
scp felipe@servera:~/user_backup.tar.gz ~/
```
