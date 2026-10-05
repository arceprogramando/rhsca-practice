# RH199 Rapid Track v10.0 — Índice del curso

Fuente: contenido del curso en ROL (RHCSA Rapid Track).  
Progreso actual: **24 / 154** pág (18 sep 2026) → zona temprana (archivos / usuarios).  
Lab: VirtualBox `student@workstation` + `student@servera` (idea del aula, no VMs oficiales).

Objetivos examen: `ex200-objetivos-oficiales.md`

Leyenda avance capítulo:
- `[x]` hecho
- `[~]` en curso / parcial
- `[ ]` pendiente

---

## Prefacio

| | Sección | Notas |
|---|---|---|
| [x] | A.1 RHCSA Rapid Track | Orientación del curso |
| [x] | A.2 Orientación entorno del aula | En ROL: workstation/servera; vos: VB |
| [x] | A.3 Realización de ejercicios de laboratorio | |

---

## Cap. 1 — Registro de sistemas (soporte Red Hat)

| | Sección | EX200 |
|---|---|---|
| [ ] | 1.1 Registro para Soporte Red Hat | Software / CDN (contexto; en examen a veces subscription-manager) |
| [ ] | 1.2 Cuestionario | |
| [ ] | 1.3 Resumen | |

*En lab casero Rocky a menudo no aplica igual que RHEL suscrito.*

---

## Cap. 2 — Administración de archivos (CLI)

| | Sección | EX200 |
|---|---|---|
| [~] | 2.1 Gestión de archivos CLI | Essential tools |
| [~] | 2.2 Ej. guiado archivos | |
| [~] | 2.3 Creación de enlaces | Hard/soft links |
| [~] | 2.4 Ej. guiado enlaces | (estabas en links ~pág 10) |
| [ ] | 2.5 Expansiones de shell (globs) | |
| [ ] | 2.6 Cuestionario globs | |
| [ ] | 2.7 Lab: gestionar archivos | |
| [ ] | 2.8 Resumen | |

---

## Cap. 3 — Edición de archivos de texto

| | Sección | EX200 |
|---|---|---|
| [ ] | 3.1 Edición CLI (`vim`) | Create and edit text files |
| [ ] | 3.2 Ej. guiado | |
| [ ] | 3.3 Resumen | |

---

## Cap. 4 — Usuarios y grupos locales  ← **zona actual (~24/154)**

| | Sección | EX200 |
|---|---|---|
| [~] | 4.1 Usuarios y grupos Linux | Manage users and groups |
| [~] | 4.2 Cuestionario | `getent`, passwd/shadow, GECOS |
| [~] | 4.3 Acceso superusuario | Privileged access / sudo |
| [ ] | 4.4 Ej. guiado sudo | |
| [~] | 4.5 Cuentas de usuarios locales | `useradd`/`usermod` + `/etc/login.defs` |
| [ ] | 4.6 Ej. guiado users | |
| [ ] | 4.7 Grupos locales | |
| [ ] | 4.8 Ej. guiado groups | |
| [ ] | 4.9 Contraseñas | aging / `chage` |
| [ ] | 4.10 Ej. guiado passwords | |
| [ ] | 4.11 Lab: users y groups | |
| [ ] | 4.12 Resumen | |

---

## Cap. 5 — Control de acceso a archivos

| | Sección | EX200 |
|---|---|---|
| [ ] | 5.1 Interpretar permisos | ugo/rwx |
| [ ] | 5.2 Cuestionario | |
| [ ] | 5.3 Gestionar permisos CLI | `chmod`/`chown` |
| [ ] | 5.4 Ej. guiado | |
| [ ] | 5.5 Defaults y especiales | umask, SUID/SGID/sticky |
| [ ] | 5.6 Ej. guiado | |
| [ ] | 5.7 Lab | |
| [ ] | 5.8 Resumen | |

*Refuerzo paralelo: libro Van Vugt Cap. 7 Permissions (pág ~338).*

---

## Cap. 6 — Software con RPM / DNF

| | Sección | EX200 |
|---|---|---|
| [ ] | 6.1 Investigar RPM | Manage software |
| [ ] | 6.2 Ej. guiado | |
| [ ] | 6.3 Instalar/actualizar con DNF | |
| [ ] | 6.4 Ej. guiado DNF | |
| [ ] | 6.5 Habilitar repos DNF | ← video Alta3 tema 2 |
| [ ] | 6.6 Ej. guiado repo | |
| [ ] | 6.7 Lab | |
| [ ] | 6.8 Resumen | |

---

## Cap. 7 — Flatpak

| | Sección | EX200 |
|---|---|---|
| [ ] | 7.1 Configurar Flatpak | Flatpak repos (objetivo oficial) |
| [ ] | 7.2 Ej. guiado | |
| [ ] | 7.3 Gestionar apps Flatpak | |
| [ ] | 7.4 Ej. guiado | |
| [ ] | 7.5 Cuestionario | |
| [ ] | 7.6 Resumen | |

---

## Cap. 8 — Medios extraíbles

| | Sección | EX200 |
|---|---|---|
| [ ] | 8.1 FS y block devices | Local storage / filesystems |
| [ ] | 8.2 Cuestionario | |
| [ ] | 8.3 Montar/desmontar | |
| [ ] | 8.4 Ej. guiado | |
| [ ] | 8.5 Localizar archivos (`find`) | |
| [ ] | 8.6 Ej. guiado | |
| [ ] | 8.7 Lab | |
| [ ] | 8.8 Resumen | |

---

## Cap. 9 — Procesos

| | Sección | EX200 |
|---|---|---|
| [ ] | 9.1 Ciclo de vida | Operate running systems |
| [ ] | 9.2 Cuestionario | |
| [ ] | 9.3 Control de trabajos (jobs) | |
| [ ] | 9.4 Ej. guiado | |
| [ ] | 9.5 Señales | `kill` / `ps` |
| [ ] | 9.6 Ej. guiado | |
| [ ] | 9.7 Monitoreo | `top` / scheduling |
| [ ] | 9.8 Ej. guiado | |
| [ ] | 9.9 Lab | |
| [ ] | 9.10 Resumen | |

---

## Cap. 10 — Servicios y daemons

| | Sección | EX200 |
|---|---|---|
| [ ] | 10.1 Procesos auto-start | systemd |
| [ ] | 10.2 Ej. guiado | |
| [ ] | 10.3 Control de servicios | enable/start/status |
| [ ] | 10.4 Ej. guiado | |
| [ ] | 10.5 Lab | |
| [ ] | 10.6 Resumen | |

---

## Cap. 11 — Red

| | Sección | EX200 |
|---|---|---|
| [ ] | 11.1 Red CLI (`nmcli`) | Manage basic networking |
| [ ] | 11.2 Ej. guiado | |
| [ ] | 11.3 Archivos de config de red | |
| [ ] | 11.4 Ej. guiado | |
| [ ] | 11.5 Hostname y resolución | `/etc/hosts`, DNS |
| [ ] | 11.6 Ej. guiado | |
| [ ] | 11.7 Lab | |
| [ ] | 11.8 Resumen | |

---

## Cap. 12 — Programación de tareas

| | Sección | EX200 |
|---|---|---|
| [ ] | 12.1 Timers systemd | Schedule tasks |
| [ ] | 12.2 Ej. guiado | |
| [ ] | 12.3 Archivos temporales | `tmpfiles` |
| [ ] | 12.4 Ej. guiado | |
| [ ] | 12.5 Cron | |
| [ ] | 12.6 Ej. guiado cron | |
| [ ] | 12.7 Cuestionario tareas de usuario | `at` / user cron |
| [ ] | 12.8 Resumen | |

---

## Cap. 13 — Logs

| | Sección | EX200 |
|---|---|---|
| [ ] | 13.1 Arquitectura de logging | Journals / logs |
| [ ] | 13.2 Cuestionario | |
| [ ] | 13.3 Syslog | |
| [ ] | 13.4 Ej. guiado | |
| [ ] | 13.5 `journalctl` | |
| [ ] | 13.6 Ej. guiado | |
| [ ] | 13.7 Journal persistente | Preserve journals |
| [ ] | 13.8 Ej. guiado | |
| [ ] | 13.9 Hora (`chrony`) | Time service clients |
| [ ] | 13.10 Ej. guiado | |
| [ ] | 13.11 Lab | |
| [ ] | 13.12 Resumen | |

---

## Cap. 14 — SELinux

| | Sección | EX200 |
|---|---|---|
| [ ] | 14.1 Funcionamiento SELinux | Manage security |
| [ ] | 14.2 Ej. guiado | |
| [ ] | 14.3 Contextos de archivo | `restorecon` |
| [ ] | 14.4 Ej. guiado | |
| [ ] | 14.5 Booleanos | |
| [ ] | 14.6 Ej. guiado | |
| [ ] | 14.7 Troubleshooting SELinux | |
| [ ] | 14.8 Ej. guiado | |
| [ ] | 14.9 Lab | |
| [ ] | 14.10 Resumen | |

---

## Cap. 15 — Almacenamiento básico

| | Sección | EX200 |
|---|---|---|
| [ ] | 15.1 FS en particiones | GPT / VFAT ext4 XFS |
| [ ] | 15.2 Ej. guiado | |
| [ ] | 15.3 Swap | |
| [ ] | 15.4 Ej. guiado | |
| [ ] | 15.5 Lab | |
| [ ] | 15.6 Resumen | |

---

## Cap. 16 — LVM

| | Sección | EX200 |
|---|---|---|
| [ ] | 16.1 Crear LVs | PV/VG/LV |
| [ ] | 16.2 Ej. guiado | |
| [ ] | 16.3 Ampliar LV | Extend LVs |
| [ ] | 16.4 Ej. guiado | |
| [ ] | 16.5 Reemplazar PVs / gestión | |
| [ ] | 16.6 Cuestionario | |
| [ ] | 16.7 Lab | |
| [ ] | 16.8 Resumen | |

*Bloque crítico del examen.*

---

## Cap. 17 — Boot y troubleshooting

| | Sección | EX200 |
|---|---|---|
| [ ] | 17.1 Bootloader / cmdline kernel | Modify bootloader |
| [ ] | 17.2 Ej. guiado | |
| [ ] | 17.3 Proceso de arranque / targets | Boot into targets |
| [ ] | 17.4 Ej. guiado | |
| [ ] | 17.5 Reparar FS dañados al boot | |
| [ ] | 17.6 Ej. guiado | |
| [ ] | 17.7 Lab | |
| [ ] | 17.8 Resumen | |

---

## Cap. 18 — Recuperar root  ← **mismo tema que Alta3 #1**

| | Sección | EX200 |
|---|---|---|
| [ ] | 18.1 Reset password root | Interrupt boot (`rd.break`) |
| [ ] | 18.2 Ej. guiado | Practica en **consola** VirtualBox |
| [ ] | 18.3 Resumen | |

---

## Cap. 19 — Seguridad de redes

| | Sección | EX200 |
|---|---|---|
| [ ] | 19.1 Firewalls (`firewalld`) | firewall-cmd |
| [ ] | 19.2 Ej. guiado | |
| [ ] | 19.3 Etiquetado puertos SELinux | SELinux port labels |
| [ ] | 19.4 Ej. guiado | |
| [ ] | 19.5 Lab | |
| [ ] | 19.6 Resumen | |

---

## Cap. 20 — NFS / autofs

| | Sección | EX200 |
|---|---|---|
| [ ] | 20.1 Montar NFS | Network file systems |
| [ ] | 20.2 Ej. guiado | |
| [ ] | 20.3 Automount | autofs |
| [ ] | 20.4 Ej. guiado | |
| [ ] | 20.5 Lab | |
| [ ] | 20.6 Resumen | |

---

## Cap. 21 — Revisión exhaustiva

| | Sección | Notas |
|---|---|---|
| [ ] | 21 Revisión | Simula examen: verificar + **reboot** + re-verificar |

---

## Orden práctico (no saltear a lo loco)

```
2–5 archivos/users/permisos  →  6–7 software
8–9 storage básico + procesos → 10 servicios → 11 red
12–13 cron/logs/hora → 14 SELinux
15–16 particiones + LVM (crítico)
17–18 boot + rd.break (músculo)
19 firewall + SELinux ports → 20 NFS/autofs → 21 review
```

## Nota sobre el aula vs tu VB

| ROL / enunciado | Tu lab |
|---|---|
| workstation / servera (classroom) | VMs propias con esos nombres/roles |
| Labs guiados del curso | Adaptá paths/IPs a tu Host-Only |
| Cap. 18 consola GRUB | Ventana VirtualBox, no solo SSH |
