# Lab 02 — Mesa de ayuda IT (mismo nivel, otro escenario)

**Dónde:** **servera** (usuario con `sudo`).  
**Setup:** `bash setup/setup.sh`  
No uses el `lab` de Red Hat ROL: esto es para tus VMs.

---

## Parte A — Incidentes y evidencia

1. Creá `~/tickets/` y dentro los dirs `open/`, `closed/`, `attachments/`.
2. El setup deja `~/tickets/inbox/` con archivos `INC-*.txt` y algunos `.log`.
   - Mové los `INC-*.txt` cuyo nombre termine en `-DONE.txt` a `closed/`.
   - El resto de `INC-*.txt` a `open/`.
   - Todos los `.log` a `attachments/`.
3. Generá `~/tickets/inventory.txt` con la lista recursiva de `~/tickets` (`find` o `ls -R`), solo stdout.
4. Con `sudo`, copiá las últimas **20** líneas de `/var/log/messages` o `/var/log/secure` (el que exista) a `~/tickets/attachments/auth-snippet.txt`. Si ninguno existe, usá `journalctl -n 20` redirigido a ese archivo (puede pedir sudo).

## Parte B — Paquete para el cliente

1. Filtrá `/etc/passwd` dejando solo usuarios con shell `/bin/bash` → `~/bash_users.txt`.
2. Creá `~/client-pack.tar.xz` con:
   - `bash_users.txt`
   - todo `~/tickets/open/`
   - todo `~/tickets/attachments/`
3. Desde el home, el tar debe poder listarse con `tar -tJf ~/client-pack.tar.xz`.

## Parte C — ACL-style con permisos clásicos

1. Grupo `helpdesk` (setup lo crea). Poné `~/tickets` con dueño tu usuario y grupo `helpdesk`.
2. Permisos `~/tickets`: **770** (otros sin acceso).
3. Enlace simbólico `~/mesa-ayuda` → `~/tickets`.
4. Guardá `du -sh ~/tickets` en `~/tickets_size.txt`.

## Parte D — Limpieza selectiva

1. Dentro de `attachments/`, borrá cualquier archivo cuyo nombre contenga `TMP` o `tmp`.
2. Copiá recursivamente `open/` a `~/tickets/backup-open/`.

## Check

```bash
bash checks/check.sh
```
