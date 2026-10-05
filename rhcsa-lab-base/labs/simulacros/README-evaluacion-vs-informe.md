# Simulacro EX200 — OpenDDemonicos

Archivo: `exam-simulation-openddemonicos.pdf`  
Fuente: Downloads → copiado acá.  
Evaluado vs informe Felipe: **RH199 38/154** (~25%, ~22 sep) · libro Cap. 7 · labs users/permisos recientes.

Leyenda:
- **Sí** — podés intentarlo ahora (viste el tema + lab o muy cercano)
- **A medias** — algo de base, pero te va a costar / incompleto
- **No aún** — RH199/blueprint todavía no lo cubriste bien

---

## Resumen rápido

| | Cantidad | Labs |
|--|----------|------|
| **Sí** | ~6 | 5, 6, 9, 12, 13?, 14 |
| **A medias** | ~5 | 1, 2, 7?, 10, 19 |
| **No aún** | ~11 | 3, 4, 8, 11, 15–18, 20–22 |

**Conclusión:** todavía **no** es momento de un simulacro completo. Sí podés hacer un **mini-simulacro** solo de labs 5–6–9–12–14 (users/permisos/tar/find/UID).

---

## Lab por lab

### Lab 1 — Networking (nmcli/nmtui)
**A medias.** Montaste VMs y tocaste nmcli, pero RH199 Cap. 11 aún no. Hostname + IP/DNS/gateway persistente: practicá antes.

### Lab 2 — Root recovery (`rd.break`) + networking
**A medias.** Teoría en glosario; en VB el GRUB te costó. Networking = igual que Lab 1. **Repetir rd.break en consola** antes de simular.

### Lab 3 — Repos YUM/DNF
**No aún.** Cap. 6 RH199 pendiente. Alta3 lo mencionó; no lo clavaste en lab.

### Lab 4 — SELinux puerto custom (httpd :82)
**No aún.** Caps 14/19. Prioridad 10 en el informe — ni empezar.

### Lab 5 — Users, groups, sudo
**Sí (con detalle).** Es tu zona fuerte ahora (`useradd`, `-aG`, `passwd`, sudoers).  
Ojo examen: sudo **solo** para `useradd` (sysadm) y `passwd` **NOPASSWD** solo para harry — no copiar `%sysadm ALL=(ALL) ALL` sin leer.

### Lab 6 — Shared dir + setgid
**Sí / repaso.** Lab `techdocs` PASS, pero marcado **REPASO**. Hacé uno limpio: `3770` o `2770` + grupo, verificar `ls -l` con grupo heredado.

### Lab 7 — Cron (natasha cada 1 min + logger)
**No aún / casi no.** Cap. 12 no visto. Comando fácil de memorizar, pero sin práctica = frágil.

### Lab 8 — Autofs + NFS
**No aún.** Cap. 20. Dos máquinas server/client.

### Lab 9 — Tar bzip2 de `/etc`
**Sí.** RH104/`tar -cjf`. Casi regalado.

### Lab 10 — ACL (`setfacl`)
**A medias.** Libro Cap. 7 ACL pendiente; en RH199 aún temprano. Sabés ugo; ACL es el siguiente escalón.

### Lab 11 — Chrony
**No aún.** Cap. 13.

### Lab 12 — Find (natasha, 24h → copiar con estructura)
**Sí / a medias.** Usaste `find`; `-user`, `-mtime`, `-exec`/`cp --parents` hay que afilar.

### Lab 13 — Grep → `/root/lines`
**Sí / a medias.** Básico; si el dict existe en la VM.

### Lab 14 — User UID fijo 1111
**Sí.** `useradd -u 1111 …` + `passwd`.

### Lab 15 — LVM (VG/LV/ext4/fstab)
**No aún.** Cap. 15–16. Prioridad 10.

### Lab 16 — Swap 400 MB persistente
**No aún.** Cap. 15.

### Lab 17 — Resize LV
**No aún.** Cap. 16 (`lvextend`/`lvreduce` + FS).

### Lab 18 — Tuned profile
**No aún.** No figura fuerte en tu avance.

### Lab 19 — Mensaje al login (`.bashrc` / `/etc/profile.d`)
**A medias.** Bash lo manejás; es más “saber dónde pegar el script” que un capítulo largo.

### Labs 20–22 — Podman (build/run/systemd linger)
**No aún.** Video Alta3 visto a alto nivel; RH199 no te llevó ahí. Dejar para después (o si el blueprint de tu fecha no incluye containers, priorizar menos).

---

## Qué practicar esta semana (según este PDF)

1. **Mini-exam (sí):** Labs **5, 6, 9, 14** (+ 12/13 si hay tiempo) en servera/serverb.  
2. **Repaso obligatorio:** umask + SGID + sticky (Lab 6) hasta que `ls -l` muestre grupo correcto.  
3. **Siguiente bloque del curso** antes del simulacro full: Cap. 6 DNF → Cap. 11 red → Cap. 18 `rd.break` en consola.  
4. **No gastar horas aún** en LVM/SELinux/Podman de este PDF hasta que RH199 los toque.

---

## Nota sobre el PDF

- Habla de **servera/serverb** + Vagrant; tus VMs son **workstation/servera** (misma idea).  
- URLs tipo `choubidoubidouuu.lab` son del autor del simulacro: en tu lab casero adaptá repos/NFS o saltá labs que dependan de ese mirror.  
- Siempre: **persistir + reboot + verificar**.
