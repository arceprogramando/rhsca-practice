# Lab 01 — SSH, tty y pseudo terminals (Cap. 5)

**Objetivo:** Replicar ideas del libro y Exercise 5-2 con server1 (+ server2 si existe).

---

## Parte A — Una sola VM (server1)

### A1. Consolas virtuales (tty)

1. En `tty1`, logueate como `felipe`. `tty` → `/dev/tty1`.
2. `Alt+F3` → login `felipe` otra vez. `tty` → `/dev/tty3`.
3. En tty1: `w` → deben aparecer **dos** sesiones de felipe (tty1 y tty3).
4. En tty3: `exit` → vuelve `login:`.
5. En tty1: `w` → tty3 ya no debe listar sesión activa.

**Pregunta:** ¿Por qué `exit` en tty3 no cerró tty1?

### A2. Pseudo terminal (pts) con SSH local

1. En tty1: `ssh felipe@localhost` (aceptar clave si pregunta).
2. `tty` → `/dev/pts/0` (o pts/1).
3. Otra terminal: `ssh felipe@localhost` en segundo intento paralelo (otra tty o mismo).
4. `w` → ver líneas `pts/X` además de `ttyY`.

**Pregunta:** ¿pts es lo mismo que tty6?

### A3. su - no crea otra tty

1. En una sesión: `su -` (root).
2. `w` → mismo TTY/pts, usuario root en esa sesión.

---

## Parte B — Dos VMs (server1 + server2)

Requisito: ping entre `192.168.122.10` y `.11`, `/etc/hosts` configurado.

### B1. Primera conexión SSH

```bash
# Desde server1
ssh felipe@server2
hostname    # debe decir server2.lab.example.com
exit
```

### B2. known_hosts

```bash
cat ~/.ssh/known_hosts
ssh-keygen -F server2
```

**Pregunta:** ¿Dónde se guarda la huella del servidor?

### B3. Clave pública (key-based auth)

```bash
ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519 -N ""
ssh-copy-id felipe@server2
ssh felipe@server2    # no debe pedir contraseña
```

### B4. root por SSH (solo lab)

En **server2** (examen a veces pide permitir root o usuario específico):

```bash
# En server2 como root — solo práctica, no producción
grep -E '^PermitRootLogin|^#PermitRootLogin' /etc/ssh/sshd_config
```

Documentar valor por defecto en Rocky 10.

### B5. X11 forwarding (si hay GUI)

```bash
ssh -X felipe@server2
# En server2 con GUI: xclock &
```

En cliente: `ForwardX11 yes` en `/etc/ssh/ssh_config`.

---

## Parte C — Preguntas tipo examen

1. ¿Qué dispositivo corresponde a Alt+F6 sin GUI?
2. ¿`chvt 4` hace qué?
3. ¿Diferencia entre `sudo reboot` y `echo b > /proc/sysrq-trigger`?
4. ¿Puerto por defecto de SSH?
5. ¿Comando para copiar clave pública al servidor?

**Respuestas:** tty6 · cambia a consola 4 · reboot limpio vs reset brusco · 22 · `ssh-copy-id`

---

## Limpieza

```bash
w
# exit en cada sesión que sobre
sudo loginctl list-sessions
```
