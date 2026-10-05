# EX200 — Objetivos oficiales RHCSA

Fuente: [EX200 Red Hat](https://www.redhat.com/en/services/training/ex200-red-hat-certified-system-administrator-rhcsa-exam)  
Examen basado en **RHEL 10**. Hands-on: sin internet, sin apuntes externos; sí man/docs del sistema.  
**Regla de oro:** todo debe **persistir tras reboot** sin intervención.

Tu camino: RH104 + RH124 + RH134 (hechos) → **RH199** en curso → EX200.  
Lab práctica: VirtualBox `student@workstation` + `student@servera`.

Leyenda de avance (ajustá vos):
- `[x]` sólido / practicado
- `[~]` visto / a reforzar
- `[ ]` pendiente fuerte

---

## 1. Essential tools

- [x] Shell con sintaxis correcta
- [x] Redirecciones `>`, `>>`, `|`, `2>`, etc.
- [~] `grep` + regex
- [x] SSH a sistemas remotos
- [x] Login / cambiar usuarios (multi-user)
- [x] `tar` / gzip / bzip2
- [x] Crear/editar texto (`vim`)
- [x] Crear/borrar/copiar/mover archivos y dirs
- [x] Hard y soft links
- [~] Permisos ugo/rwx (`chmod`/`chown`; ACL más adelante)
- [x] Docs: `man`, `info`, `/usr/share/doc`

## 2. Manage software

- [ ] Repos RPM (`dnf` / `.repo`) — video Alta3 tema 2
- [ ] Instalar/quitar RPM
- [ ] Repos Flatpak (**nuevo en objetivos recientes / RHEL 10**)
- [ ] Instalar/quitar Flatpak

## 3. Simple shell scripts

- [ ] `if` / `test` / `[]`
- [ ] Loops (`for`, etc.)
- [ ] Args `$1`, `$2`, …
- [ ] Capturar salida de comandos en el script

## 4. Operate running systems

- [x] Boot / reboot / shutdown normal
- [ ] Targets manuales (`rescue`, `multi-user`, etc.)
- [~] Interrumpir boot (`rd.break` / root reset) — **practicar en consola VB**
- [~] Procesos intensivos + `kill` (`ps`/`top`)
- [ ] Scheduling de procesos (`nice`/`renice`)
- [ ] Tuning profiles (`tuned`)
- [ ] Logs / journals (`journalctl`)
- [ ] Preservar journals
- [ ] Servicios de red: start/stop/status
- [x] Transferir archivos seguro (`scp`/`sftp`)

## 5. Configure local storage

- [ ] Particiones GPT (crear/listar/borrar)
- [ ] PV (crear/quitar)
- [ ] VG (asignar PVs)
- [ ] LV (crear/borrar)
- [ ] Mount al boot por UUID o label (`fstab`)
- [ ] Agregar particiones/LV/swap **sin destruir** datos

## 6. Create and configure file systems

- [ ] VFAT, ext4, XFS (crear/montar/desmontar)
- [ ] NFS (montar/desmontar)
- [ ] `autofs`
- [ ] Extender LVs existentes
- [~] Diagnosticar/corregir permisos

## 7. Deploy, configure, and maintain systems

- [ ] `at`, `cron`, timers systemd
- [ ] Services enable/start (persisten boot)
- [ ] Target por defecto al boot
- [ ] Cliente de hora (`chrony`)
- [ ] Paquetes: CDN / repo remoto / local
- [ ] Modificar bootloader (`grubby`/GRUB)

## 8. Manage basic networking

- [~] IPv4 / IPv6 (`nmcli`)
- [~] Resolución de nombres (`/etc/hosts`, DNS)
- [ ] Servicios de red enable al boot
- [ ] `firewalld` / `firewall-cmd`

## 9. Manage users and groups

- [x] Crear/borrar/modificar users (`useradd`/`usermod`/`userdel`)
- [~] Passwords + aging (`passwd`, `chage`)
- [x] Grupos y memberships
- [~] Acceso privilegiado (`wheel` / sudo)

## 10. Manage security

- [ ] Firewall (`firewall-cmd`)
- [ ] Umask / permisos por defecto
- [x] SSH por claves
- [ ] SELinux enforcing/permissive
- [ ] Contextos de archivo/proceso
- [ ] `restorecon` (default contexts)
- [ ] Port labels SELinux
- [ ] Booleans SELinux

---

## Mapa rápido: video Alta3 ↔ objetivos

| Tema video | Objetivo oficial |
|---|---|
| Reset root (`rd.break`) | Interrupt the boot process… |
| Add yum/dnf repo | Configure access to RPM repositories |
| Podman build/run/systemd | *Containers no están listados tal cual en este texto*; DevOps/path RHCE los menciona en audiencia. Priorizá lo listado arriba; si el blueprint de tu fecha incluye containers, practicá Podman aparte. |

> Revisá siempre la página oficial por si Red Hat actualiza el blueprint (sobre todo RHEL 10 / Flatpak / containers).

## Prioridad sugerida (vos ahora)

1. Cerrar **users/permisos/links** (RH199 temprano) hasta músculo.  
2. Clavar **`rd.break`** en VirtualBox (consola + GRUB_TIMEOUT).  
3. **Repos + dnf** y **nmcli** básico.  
4. **Storage LVM + fstab UUID** (bloque crítico examen).  
5. **SELinux + firewalld** (último tramo, alto impacto).  
6. Scripts, cron/timers, Flatpak, tuned — no dejarlos para el final absoluto.

## Checklist de cada tarea en el examen

```text
1. Hacer el cambio
2. Verificar (comando + salida esperada)
3. Reboot (si aplica)
4. Verificar de nuevo  ← sin esto, a menudo = 0 puntos
```
