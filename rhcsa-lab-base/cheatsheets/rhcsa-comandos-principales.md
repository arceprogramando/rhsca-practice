# RHCSA — Comandos principales (para recordar)

Actualizado: 2026-09-21
Usuario a veces: normal ($) | a veces: root/sudo (#)

---

## Tu lab (2 VMs VirtualBox) — cómo trabajás hoy

Lab **propio** (VirtualBox), no las VMs oficiales del classroom de Red Hat.  
Las armaste vos para **imitar** la idea del curso: dos máquinas + usuario `student` + SSH entre ellas.

| Host (tuyas) | Login típico | Rol (idea del curso) |
|---|---|---|
| **workstation** | `student@workstation` | Desde donde estudiás / SSH / scp |
| **servera** | `student@servera` | Donde resolvés la mayoría de labs |

```bash
ssh student@workstation
ssh student@servera
# Desde workstation → servera
ssh student@servera
scp archivo.txt student@servera:~/
```

Password que uses en **tus** VMs (a menudo `student` en labs RH; confirmá en la tuya).  
IPs: las que configuraste en Host-Only (ej. `192.168.56.10` / `.11`) o `/etc/hosts`.

### Cursos cuyos labs seguís (misma *idea* de topología)

| Curso | Qué es | Nota |
|---|---|---|
| **RH104** | Fundamentals | Enunciados hablan de workstation/servera |
| **RH124** | Sysadmin I | Idem |
| **RH134** | Sysadmin II | Idem |
| **RH199** | Rapid Track | Idem (prep EX200) |

En ROL el lab real es otro entorno; vos practicás **el mismo esquema** en VirtualBox.  
Si un lab pide `serverb` u otro host, o lo agregás o adaptás a lo que tengas.

**Nota:** `rhcsa-lab/` en este repo (server1/server2/felipe) es **otro** lab local distinto.  
Tu setup actual de práctica = **tus** VMs workstation + servera.

---

## Ideas clave (no confundir)

### 1) ¿No me acuerdo del comando? → `apropos`
```bash
apropos user
man -k user
apropos user | grep -i add
```
En RHEL/Rocky el correcto es **`useradd`** (no `adduser`).

| Si dudás entre... | Hacé esto |
|---|---|
| useradd / adduser | `apropos user` → usá **useradd** |
| cualquier comando | `apropos TEMA` o `man -k TEMA` |

Si dice "nada apropiado":
```bash
sudo mandb
```

### 2) Idioma vs teclado (son cosas distintas)
| Qué | Variable/comando | Ejemplo |
|---|---|---|
| **Idioma** de man/mensajes | `$LANG` | `es_AR.UTF-8` |
| **Teclado** (dónde está @ \| ñ) | keymap | `latam` |

```bash
echo $LANG
# → idioma (man, helps, errores)

localectl status
# → mirar "VC Keymap" = teclado
```

**Al empezar el examen:** si @ \| / salen mal, NO toques `$LANG`.
Cambiá el **teclado**:
```bash
localectl status
sudo localectl set-keymap latam
# España: sudo localectl set-keymap es
# US:     sudo localectl set-keymap us
```

**Consola / minimal:** `localectl` / `loadkeys` (arriba).

**Con escritorio GNOME** (si la VM tiene GUI), Felipe lo resolvió así — layout Argentina/Latam en la sesión gráfica:
```bash
gsettings set org.gnome.desktop.input-sources sources "[('xkb', 'latam')]"
```
Eso cambia el teclado de **GNOME**; no reemplaza del todo al keymap de consola (`localectl`). En lab con GUI, a veces hace falta **los dos** (o al menos el de GNOME para la terminal gráfica).

Ver idiomas disponibles (locale, no teclado):
```bash
locale -a | grep '^es_'
```

Probar idioma temporal (ejercicio del libro):
```bash
LANG=es_ES.UTF-8 ls --help
```

### 3) `sudoers` — quién puede hacer `sudo` (MEMORIZAR · te cuesta)
No confundir:
- `/etc/group` → **quién está** en el grupo (`admin:x:30001:sysadmin1,...`)
- `/etc/sudoers` + `/etc/sudoers.d/*` → **qué puede hacer** ese grupo/usuario con `sudo`

**Línea del lab (MEMORIZAR ESTA):**
```text
%admin ALL=(ALL) ALL
```

| Pieza | Significa |
|---|---|
| `%admin` | grupo `admin` (`%` = grupo; sin `%` = un usuario) |
| `ALL` (1º) | desde cualquier máquina |
| `(ALL)` | puede actuar como cualquier user (incl. root) |
| `ALL` (último) | puede correr **cualquier** comando |

Ritual examen / lab `users-group`:
```bash
# 1) miembros del grupo
getent group admin
# 2) regla sudo (archivo dedicado; permisos con visudo)
echo '%admin ALL=(ALL) ALL' | sudo tee /etc/sudoers.d/admin
sudo chmod 440 /etc/sudoers.d/admin
# mejor: sudo visudo -f /etc/sudoers.d/admin

# 3) probar
su - sysadmin1
tail /var/log/messages          # FALLA (sin permiso)
sudo tail /var/log/messages     # OK (pide pass de sysadmin1, no de root)
```

En RHEL lo habitual es el grupo **`wheel`** (a menudo ya tiene regla en sudoers):
```bash
sudo usermod -aG wheel USUARIO
```

### 4) Reset password de root — **DOS métodos** (MEMORIZAR · músculo)
**Objetivo EX200:** *Interrupt the boot process in order to gain access to a system*  
(RH199 Cap. 18). En el examen real a veces **falla uno** (pide root pw o no entra) → tenés que saber el otro.

**Solo en la consola de la VM** (ventana VirtualBox), **no por SSH**.

#### Antes (lab casero): que GRUB se vea
Si al rebootear “pasa de una” sin menú:
```bash
sudo vim /etc/default/grub
# GRUB_TIMEOUT=5
# GRUB_TIMEOUT_STYLE=menu
sudo grub2-mkconfig -o /boot/grub2/grub.cfg   # BIOS (VirtualBox típico)
# UEFI: grub.cfg bajo /boot/efi/EFI/rocky/ o redhat/
```
Al reiniciar: click en la ventana VM → **Shift** o **Esc** si hace falta.

---

#### Método A — `rd.break` (el clásico del curso)
1. Reboot → menú **GRUB** → kernel → tecla **`e`**
2. Línea **`linux`** → al **final** → agregar: ` rd.break`
3. Arrancar: **Ctrl+X**
4. En el prompt de emergencia:
```bash
mount -o remount,rw /sysroot
chroot /sysroot
passwd                    # nueva pass de root (la que diga el examen)
touch /.autorelabel       # OBLIGATORIO (SELinux)
exit                      # sale del chroot
exit                      # / reboot — a veces hace falta el 2º exit
# o: reboot
```
5. Login root → verificar.

**Frase A:** `e` → `rd.break` → Ctrl+X → remount **/sysroot** → **chroot** → passwd → **touch /.autorelabel** → exit → exit/reboot

**Si pide password de root acá** → este método falló en tu VM → pasá al Método B.

---

#### Método B — `init=/bin/bash` (plan B del examen)
Misma entrada a GRUB; **cambia solo** lo que agregás en la línea `linux` y los comandos (acá **no** hay `/sysroot` ni `chroot`).

1. Reboot → GRUB → **`e`**
2. Línea **`linux`** → al final → agregar: ` init=/bin/bash`  
   (opcional: borrar `rhgb quiet` para ver más mensajes)
3. **Ctrl+X**
4. Shell como PID 1 (ya estás en el root real `/`):
```bash
mount -o remount,rw /
passwd                    # nueva pass de root
touch /.autorelabel       # OBLIGATORIO (SELinux) — igual que en A
exec /sbin/init           # continuar el boot normal
# si se cuelga: sync ; reboot -f
```
5. Login root → verificar.

**Frase B:** `e` → `init=/bin/bash` → Ctrl+X → remount **`/`** → passwd → **touch /.autorelabel** → **exec /sbin/init**

---

#### A vs B — no mezclar
| | Método A `rd.break` | Método B `init=/bin/bash` |
|---|---|---|
| Dónde caés | initramfs / emergencia | bash como init (PID 1) |
| Remount | `/sysroot` | `/` |
| ¿chroot? | **Sí** `chroot /sysroot` | **No** |
| Salida | `exit` (+ a veces otro) / `reboot` | `exec /sbin/init` |
| SELinux | `touch /.autorelabel` en ambos | igual |

**Regla de oro examen:** probar A; si pide root pw o no entra → **mismo reboot, Método B**. Nunca olvidar `/.autorelabel`.

---

## Documentación
| Comando | Para qué |
|---|---|
| `apropos PALABRA` | Buscar man por tema |
| `man -k PALABRA` | Igual que apropos |
| `whatis COMANDO` | Descripción corta |
| `man COMANDO` | Manual completo |
| `man 5 ARCHIVO` | Formato de config (`man 5 passwd`) |
| `sudo mandb` | Rebuild índice de man |

---

## Usuarios
| Correcto RHEL/Rocky | Nota |
|---|---|
| `useradd` | crear usuario (lee defaults de `/etc/login.defs`) |
| `usermod` | modificar |
| `userdel` | borrar |
| `passwd` | contraseña |
| `chage` | aging de password / cuenta (users **ya** existentes) |
| `id USUARIO` | ver uid/grupos |
| `usermod -aG wheel USUARIO` | meter en wheel → sudo (si wheel está en sudoers) |
| `usermod -aG admin USUARIO` | member de grupo `admin` (hace falta regla en sudoers) |
| `usermod -aG GRUPO USUARIO` | **grupo complementario** (MEMORIZAR `-a`) |
| `usermod -g GRUPO USUARIO` | cambiar **grupo primario** |
| `usermod -c "Texto" USUARIO` | poner **comentario** (campo GECOS) |
| `groupadd` / `groupdel` / `groupmod` | grupos (hace falta root/sudo) |
| `getent passwd USUARIO` | ver ficha del usuario (mejor que `cat`) |
| `getent group NOMBRE` | ver GID + miembros |

### `/etc/login.defs` — DEFINICIÓN (MEMORIZAR)

**Qué es:** archivo de **políticas / valores por defecto** para la creación y el aging de cuentas  
(lo lee `useradd`, y también alimenta defaults de password aging).

**Qué NO es:** no es la lista de usuarios (`/etc/passwd`) ni de passwords (`/etc/shadow`).

**Idea en una frase:**  
`useradd` **crea** la cuenta; `/etc/login.defs` dice **con qué reglas por defecto** la crea  
(UID range, si crea home, vigencia de password, umask, grupo privado, etc.).

```bash
# Ver lo importante
grep -E '^(UID_|GID_|PASS_|CREATE_HOME|UMASK|USERGROUPS)' /etc/login.defs
```

| Zona típica | Controla |
|---|---|
| `UID_MIN` / `UID_MAX` | rango de UIDs de users normales |
| `GID_MIN` / `GID_MAX` | rango de GIDs |
| `CREATE_HOME` | si `useradd` crea home solo |
| `UMASK` | permisos base del home nuevo |
| `USERGROUPS_ENAB` | grupo privado con el mismo nombre del user |
| `PASS_MAX_DAYS` / `PASS_MIN_DAYS` / `PASS_WARN_AGE` | aging **por defecto** de la password |

Otra capa de defaults: `/etc/default/useradd` (shell, `HOME=/home`, …).  
Plantilla del home nuevo: `/etc/skel/`.

**Clave aging:** cambios en `PASS_*` de `login.defs` → solo users **creados después**.  
Users ya existentes → `chage` (ver bloque siguiente).

### Vigencia de contraseña (MEMORIZAR · `login.defs` + `chage`)

En `/etc/login.defs` (defaults para users **nuevos**):

| Opción | Qué hace |
|---|---|
| `PASS_MAX_DAYS` | máxima vigencia de la password (días) |
| `PASS_MIN_DAYS` | mínima: cuántos días hay que esperar para **cambiarla** de nuevo |
| `PASS_WARN_AGE` | días de **aviso** antes de que expire |

```bash
sudo vim /etc/login.defs
# ej. PASS_MAX_DAYS 90
#     PASS_MIN_DAYS 0
#     PASS_WARN_AGE 7
```

**Clave (no confundir):**  
cambiar `login.defs` **solo afecta a usuarios creados DESPUÉS**.  
Los que ya existen **siguen** con la política vieja → **`chage`**.

### `chage` — MEMORIZAR (users ya existentes)

Herramienta del examen para aging. Ver siempre antes/después:

```bash
sudo chage -l usuario          # --list
```

| Corta | Larga | Qué hace |
|---|---|---|
| `-l` | `--list` | ver política actual |
| `-M N` | `--maxdays N` | password vale máx. N días |
| `-m N` | `--mindays N` | mín. N días entre cambios de pass |
| `-W N` | `--warndays N` | avisar N días antes de expirar |
| `-d 0` | `--lastday 0` | “último cambio = hoy/época 0” → **obligar a cambiar pass en el próximo login** |
| `-E FECHA` | `--expiredate` | caduca la **cuenta** (no solo la pass) ← distinto de `-M` |
| `-I N` | `--inactive N` | días inactiva tras expirar la pass |

```bash
# Ejemplos típicos de lab
sudo chage -M 90 usuario
sudo chage -m 0 usuario
sudo chage -W 7 usuario
sudo chage -d 0 usuario              # debe cambiar pass al entrar
sudo chage -E 2026-11-10 usuario     # cuenta vence esa fecha
```

Fecha “dentro de 180 días” (formato `%F` = `YYYY-MM-DD`). **Sin espacio** tras el `+`:

```bash
date -d "+180 days" +%F
# MAL:  date -d "+180 days" + %F   ← espacio → error "extra operand"
sudo chage -E "$(date -d '+180 days' +%F)" usuario
```

#### Password expire vs Account expire (MEMORIZAR · te confunden)

| Qué pide el lab | Comando | En `chage -l` |
|---|---|---|
| Vigencia / max de la **password** | `chage -M N` | Password expires / Max days |
| Vencimiento de la **cuenta** | `chage -E YYYY-MM-DD` | **Account expires** |
| Bloqueo ya | `usermod -L` | lock; no es una fecha |

Si el grade dice algo como:  
`Verify the account expiration … is not specified`  
→ falta **`chage -E`**. Si `Account expires: never` → todavía no está.

```bash
# Ver
sudo chage -l usuario | grep -i expire

# Todos los members de un grupo (ej. consultants del lab)
getent group consultants
for u in $(getent group consultants | cut -d: -f4 | tr ',' ' '); do
  sudo chage -E "$(date -d '+180 days' +%F)" "$u"
  sudo chage -l "$u" | grep -i 'Account expires'
done
```

También relacionado (bloqueo de login, no es `chage`):
```bash
sudo usermod -L usuario    # --lock
sudo usermod -U usuario    # --unlock
```

Ritual mental examen:
1. ¿Política **por defecto** users nuevos? → `/etc/login.defs` (`PASS_*`)
2. ¿User **ya creado**? → `chage` (+ verificar `chage -l`)
3. ¿Vence la **pass**? → `-M` / `-m` / `-W` (y a veces `-d 0`)
4. ¿Vence la **cuenta**? → `-E` + fecha (`date … +%F`)
5. Persiste en `/etc/shadow`

Si `man -k chage` dice *nothing appropriate* → `sudo mandb` (el índice man vacío).

### GID automático (`groupadd` sin `-g`)

```bash
groupadd -g 30000 operators   # GID fijo 30000
groupadd admin                # sin -g → suele tomar el siguiente libre (30001)
```

Si “salta” a 30000, el próximo automático suele ser **30001**.  
Forzá número: `groupadd -g 40000 admin`.

### Grupos complementarios — `usermod -aG` (MEMORIZAR)

**Grupo primario** = el de `/etc/passwd` (campo GID).  
**Grupos complementarios** = lista extra en `/etc/group` (el user aparece al final de la línea).

```bash
# Agregar a un grupo SIN sacar los demás  →  -a = append
sudo usermod -aG operators operator1

# Verificar
id operator1
getent group operators
# operators:x:30000:operator1,operator2,...
```

| Comando | Efecto |
|---|---|
| `usermod -aG g1 user` | **suma** `g1` a los complementarios |
| `usermod -G g1 user` | **reemplaza** todos los complementarios por solo `g1` (peligroso) |
| `usermod -g g1 user` | cambia el **primario** |

**Frase:** `-aG` = agregar grupo complementario; sin `-a` te podés cargar los otros grupos.

### umask + SGID + sticky — REPASO PENDIENTE (22 sep)

Lab `perms-review`: **GRADE PASS**, pero **repasar** hasta hacerlo sin dudar.

Checklist de práctica (en **serverb**):
```bash
ls -ld /home/techdocs          # ¿drwxrws--T. … techdocs?
ls -l /home/techdocs/dev1/     # ¿grupo techdocs (no dev1)?
id                             # ¿techdocs en grupos?
umask                          # lab: 007
echo "Logging started" >> /home/techdocs/dev1/dev1.log   # debe andar entre miembros
rm -rf /home/techdocs/dev1     # otro user: Operation not permitted (sticky)
```

Si `Permission denied` al editar archivo ajeno → casi seguro **falta SGID** o el archivo nació con grupo privado.

### umask vs chmod (MEMORIZAR · te confunden)

| | `umask` | `chmod` |
|---|---|---|
| ¿Cuándo? | al **crear** archivos/dirs nuevos | sobre algo que **ya existe** |
| ¿Dónde? | en la **sesión** (no se pega a una carpeta) | en ese archivo/dir |
| Ejemplo | `umask 0022` | `chmod 3770 /home/techdocs` |

Base al crear: archivo `666` · directorio `777`. El umask **resta** bits.

| umask | Archivo nuevo | Dir nuevo |
|---|---|---|
| `0022` / `022` | `644` | `755` |
| `0002` / `002` | `664` | `775` |
| `0000` / `000` | `666` (sin x) | **`777`** |

```bash
umask           # ver
umask 0022      # típico RHEL (volver a “normal”)
# no hay “exit umask”: se pone de nuevo el valor o se cierra la sesión
```

**Frase:** umask = filtro al crear; chmod = cambio a lo ya creado.

### Permisos especiales: setuid · setgid · sticky (MEMORIZAR)

| Nombre | Octal | En `ls` | Efecto |
|---|---:|---|---|
| **setuid** | **4**000 | `s`/`S` en dueño | el binario corre como el **dueño** (ej. `passwd`) |
| **setgid** | **2**000 | `s`/`S` en grupo | en **dir**: lo nuevo hereda el **grupo** del dir |
| **sticky** | **1**000 | `t`/`T` en others | en **dir**: solo dueño del archivo (o root) lo **borra** |

Primer dígito = suma `0–7` (ej. `3` = setgid+sticky).

```bash
chmod g+s /home/techdocs     # SGID
chmod o+t /home/techdocs     # sticky  (la t no es rwx; es sticky)
chmod 3770 /home/techdocs    # setgid + sticky + rwxrwx---
ls -ld /home/techdocs        # drwxrws--T. …
```

Lab colaborativo (`techdocs`): grupo escribe, others nada, SGID + sticky → **`3770`**.

### GECOS — el “comentario” del usuario

**GECOS** = 5º campo de `/etc/passwd`: texto libre (nombre, rol, descripción).  
No da permisos ni cambia el login; solo describe la cuenta.

```bash
sudo usermod -c "Operator One" operator1   # comentario → operator1 (no a otro user)
getent passwd erik                          # ver ficha
getent passwd erik | cut -d: -f5            # solo el comentario
```

Ejemplo de línea:
```text
erik:x:1005:1008:Erik-Workstation:/home/erik:/bin/bash
#                   ↑ GECOS (comentario)
```

### `getent` vs `cat /etc/passwd`

| | `cat /etc/passwd` | `getent passwd` |
|---|---|---|
| Archivo local | sí | sí |
| Usuarios de red (LDAP/SSSD) | no | **sí** |
| Un usuario | `grep erik /etc/passwd` | `getent passwd erik` |

En lab local suelen verse iguales. En examen preferí **`getent`**.

```bash
getent passwd              # todos
getent passwd student      # uno
getent group sales         # un grupo + miembros
sudo getent shadow student # shadow (hace falta privilegio)
```

Campos de `getent passwd`:
`nombre:x:UID:GID:GECOS:home:shell`

### passwd vs shadow + `awk` (lab compreview / filtrar cuentas)

| Archivo | Qué tiene | ¿sudo para leer? |
|---|---|---|
| `/etc/passwd` | usuario, **UID**, home, shell, **GECOS** | no |
| `/etc/shadow` | hash de password | **sí** (solo root) |

Cuentas **regulares** ≈ UID **≥ 1000**. Sistema ≈ UID &lt; 1000 (`root`, `bin`, `sshd`…).

**Memorizar este patrón:**

```bash
# 1) Solo NOMBRES de usuarios regulares (campo 1; UID es campo 3)
awk -F: '$3 >= 1000 {print $1}' /etc/passwd

# 2) Líneas COMPLETAS de passwd solo regulares → user_info.txt
awk -F: '$3 >= 1000 {print}' /etc/passwd > ~/user_info.txt

# 3) Mismos usuarios en shadow → user_passwords.txt
awk -F: '$3 >= 1000 {print $1}' /etc/passwd > /tmp/regulares.txt
sudo grep -F -f /tmp/regulares.txt /etc/shadow | sudo tee ~/user_passwords.txt > /dev/null
sudo chown "$USER:$USER" ~/user_passwords.txt
```

Piezas de `awk -F: '$3 >= 1000 {print $1}' /etc/passwd`:
- `-F:` → separar campos por `:`
- `$3` → UID; `$1` → nombre de usuario
- `$3 >= 1000` → solo regulares
- `{print $1}` → imprimir solo el nombre (sin `{print $1}` / con solo `{print}` = línea entera)
- `/etc/passwd` → archivo de entrada

**Ojo `sudo` + `>`:** el `>` lo hace tu usuario, no root. Si el archivo es de root → `Permission denied`. Usá `tee` o `sudo bash -c '...'` o `chown` antes.

### `tar` — meter 2 (o más) archivos en un `.tar.gz` (como RH104)

Orden mental: **crear + gzip + archivo-salida + lo-que-va-adentro**

```bash
# Forma del libro / solución oficial (estás en ~)
tar --create --gzip --file user_backup.tar.gz user_info.txt user_passwords.txt

# Misma cosa, corto (MEMORIZAR ESTE)
tar -czf user_backup.tar.gz user_info.txt user_passwords.txt
#    │││  ^^^^^^^^^^^^^^^^^^  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#    │││  nombre del PAQUETE   archivos que ENTRAN (cuantos quieras)
#    ││└─ f = file (el .tar.gz)
#    │└── z = gzip → .tar.gz
#    └─── c = create
```

Truco: **`-f` va pegado al nombre del .tar.gz**; después van los contenidos.  
Listar / comprobar: `tar -tzf user_backup.tar.gz`

xz en vez de gzip → `-cJf archivo.tar.xz ...` (`J` = xz).

---

## Storage — `mount` / `umount` / `fstab` (Idea clave)

### Qué es
Un disco o partición (ej. `/dev/sdb1`) **no se usa solo por existir**.  
`mount` = **enganchar** ese dispositivo a una carpeta (punto de montaje).  
Desde ahí lo ves como archivos normales.

```
/dev/sdb1  ──mount──►  /mnt/datos
                       (vacía al principio; después de mount “aparece” el contenido)
```

`umount` = desenganchar (antes de sacar el disco / tocar particiones).

### Comandos del día a día
```bash
lsblk -f                    # discos, FS, UUID, dónde está montado
findmnt                     # árbol de lo montado ahora
mount                       # lista (más ruidosa)
df -hT                      # espacio + tipo de FS de lo montado

# Montar YA (solo hasta reboot, si no está en fstab)
sudo mkdir -p /mnt/datos
sudo mount /dev/sdb1 /mnt/datos
# o por UUID (más seguro que /dev/sdX que cambia):
sudo mount UUID=xxxx-xxxx /mnt/datos

sudo umount /mnt/datos      # o: umount /dev/sdb1
```

### Que sobreviva al reboot → `/etc/fstab`
`mount` a mano = temporal. Persistente = línea en **`/etc/fstab`**:

```
UUID=xxxx-xxxx   /mnt/datos   xfs   defaults   0 0
# 1 dispositivo    2 punto     3 FS  4 opciones  5  6
```

Después:
```bash
sudo mount -a               # monta todo lo de fstab (probar sin reboot)
findmnt /mnt/datos          # verificar
```

**Examen:** siempre preferí **UUID** o **LABEL** (de `lsblk -f` / `blkid`), no `/dev/sdb1` a ciegas.

### Remount (el del reset de root)
Ya está montado, pero **solo lectura** → lo reabrís lectura/escritura **sin** desmontar:

```bash
mount -o remount,rw /sysroot   # método rd.break
mount -o remount,rw /          # método init=/bin/bash
```

`-o` = opciones. `remount` = cambiar opciones del mount actual. `rw` = read-write.

### Tipos que vas a ver
| Tipo | Uso típico |
|---|---|
| `xfs` | default RHEL/Rocky en muchos discos |
| `ext4` | también común |
| `vfat` | a veces USB / EFI |
| `swap` | no se “monta” con carpetas; `swapon` |
| `nfs` | red: `mount server:/export /mnt/nfs` |

### Errores típicos
| Síntoma | Causa típica |
|---|---|
| `target is busy` al umount | algo usa esa carpeta (`cd` fuera, cerrar archivos) |
| Montás y al reboot “desaparece” | faltó `/etc/fstab` |
| `wrong fs type` | tipo mal en fstab o sin formatear (`mkfs.xfs` etc.) |

---

## Shell / archivos
| Comando | Para qué |
|---|---|
| `pwd` | dónde estoy |
| `ls -lah` | permisos + tamaño |
| `vim` | editar |
| `chmod` / `chown` | permisos / dueño |
| `find` | buscar (también por size) |
| `echo $PATH` / `env` | PATH / todas las variables |

### `find` + `-iname` (lab mutt / buscar por nombre)

```bash
find / -iname 'mutt' 2>/dev/null
#  │         │              └─ stderr a /dev/null (tirar errores)
#  │         └─ -iname = nombre "mutt" SIN importar Mayúsc/minúsc
#  └─ / = empezar a buscar DESDE la raíz del sistema (todo el disco)
```

El **`/`** no es parte de `-iname`: es el **directorio desde donde arranca** la búsqueda.

| Empezás en | Comando | Alcance |
|---|---|---|
| Raíz | `find / -iname 'mutt'` | **todo** el sistema (`/usr`, `/etc`, `/home`…) |
| Solo etc | `find /etc ...` | solo bajo `/etc` |
| Tu home | `find ~ -iname 'mutt'` o `find /home/student ...` | solo tu carpeta |
| Acá | `find . -name '*.rc'` | solo el directorio actual |

Sin esa ruta, `find` no sabe **dónde** mirar (o usa `.` según versión/uso). En el lab mutt usás `/` porque la doc puede estar en `/usr/share/doc/...`, no en tu home.

| Opción | Significado |
|---|---|
| `-name 'mutt'` | nombre exacto (sí distingue mayúsculas) |
| `-iname 'mutt'` | igual, **case-insensitive** (Mutt, MUTT, mutt) |
| `find /etc` | solo bajo `/etc` |
| `find / -iname 'mutt'` | en todo el sistema (desde `/`) |

Docs de mutt suelen estar en `/usr/share/doc/mutt` → `mkdir ~/mutt-rc` y `cp /usr/share/doc/mutt/*.rc ~/mutt-rc`.

---

## Historial / redirecciones
| Comando / símbolo | Para qué |
|---|---|
| `history` / `history -d N` | ver / borrar entrada |
| `Ctrl-r` / `!N` | buscar / repetir |
| `>` `>>` `2>` `2>&1` `\|` | redirect y pipes |
| `/dev/null` | “tacho”: todo lo escrito **desaparece** |

### `2> archivo` vs `2>/dev/null` (importante)

| Forma | Efecto |
|---|---|
| `find /etc > etc_success.txt 2> etc_errors.txt` | stdout → success; **stderr se GUARDA** en `etc_errors.txt` |
| `find / -iname 'mutt' 2>/dev/null` | stderr → **/dev/null**; errores **no se ven ni se guardan** |
| `>` / `1>` | solo salida normal (stdout) |
| `2>` | solo errores (stderr) |
| `2>&1` | errores al mismo lugar que stdout |

Inventario `/etc` del lab → usá **dos archivos** (`>` y `2>`).  
Búsqueda ruidosa en `/` → usá **`2>/dev/null`** para limpiar la pantalla.

---

## Ritual inicio examen
1. Probar teclado: `@ | / -`
2. Si está mal → `sudo localectl set-keymap latam` (no $LANG)
3. Leer todo el examen
4. Si olvidás un comando → `apropos` / `man -k` (si vacío → `sudo mandb`)
5. Fáciles primero (users/permisos/red)
6. Si una máquina pide root y no entra → **`rd.break`** o plan B **`init=/bin/bash`** (Idea clave 4)
7. Verificar + reboot + re-verificar (sin persistir = 0 puntos)

---

## Día del EX200 — UI Red Hat (MEMORIZAR · entorno)

Fuente: video oficial *How to take a Red Hat exam*  
(`https://www.youtube.com/watch?v=Me6Y12-sux8`).

**No instalás ISO en casa:** el día D te dan un lab ya armado (VMs + browser del examen + proctor).

### Timer / idioma / teclado
- El **timer arranca** con el examen; miralo en el browser del exam (cada examen tiene su límite).
- Podés cambiar idioma de **enunciados**; terminales/SO siguen en **inglés**.
- VMs en inglés por defecto. Layout puede no coincidir con tu setup → Red Hat recomienda **dejar teclado en inglés** en el exam para no pelear.

### Tareas en el browser
- **Revisit / Done** = solo para vos; **no cuentan** para la nota.
- Links de tareas → al volver usá **Back**.
- **Feedback** ≠ calificación.

### Terminales y VMs
```text
Activities → Terminal          (varios OK)
Activities → VM Manager        (nodos / status)
```
- Entrar a un nodo: **SSH** (`ssh root@IP` — IP y pass en las instrucciones) **o** **Console** en VM control.
- **Shutdown VM** desde el control (confirma); el SSH se cierra.
- **Rebuild node** = **borra y resetea** esa VM (Yes → escribir `CONFIRM` en mayúsculas → esperar).  
  Perdés todo lo hecho ahí. Solo si realmente hace falta.

### Copy / paste / zoom
- Fuente terminal: **Ctrl+Shift++**
- Zoom browser exam: menú ☰ → **+**
- **No uses** Ctrl+C / Ctrl+X / Ctrl+V (pueden colgar terminal/consola).  
  Copiá con **mouse → clic derecho → Copy / Paste**.  
  En consola VM a veces: “Open text dialog” → pegar → **Send**.

### Documentación (sin internet libre)
- Sección **Available documentation** → URL / PDFs del exam.
- Guardá PDF al disco; abrí con el **visor PDF del SO** (menos RAM).
- No abras mil pestañas (puede romper Back / colgar).
- En las VMs: **`man` / `apropos` / `sudo mandb`**. No Google/YouTube.

### Break / proctor / red
- Chat (abajo derecha) → **Break** → avisás al proctor.
- Ícono de **taza de café** = estás en break; **el timer sigue corriendo**.
- Nada de celular/tablet (sesión grabada; puede anular el examen).
- Para volver: chat al proctor (puede pedir otro room scan).
- Problemas de conexión: **avisá al proctor al toque** (pueden pedir reboot PC/router).

### Encaje rápido
| Idea | Para vos |
|---|---|
| Lab lo dan ellos | Tu VirtualBox es solo práctica |
| SSH + Console | Misma idea que workstation/servera |
| Rebuild = wipe | No lo toques salvo desastre |
| Doc = man + PDFs del exam | No Firefox a internet |

