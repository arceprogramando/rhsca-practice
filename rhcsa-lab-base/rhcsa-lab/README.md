# Lab RHCSA — server1 + server2 (estilo Red Hat)

Lab de práctica multi-host inspirado en **RH199** (workstation + servers) y objetivos **EX200**.

## Qué podés hacer desde acá

| Desde Cursor / server1 | Necesitás vos |
|------------------------|---------------|
| Leer guías y ejercicios | Segunda VM (`server2`) en VirtualBox/VMware |
| Correr `setup-server1.sh` | Red **Host-Only** o **Internal** entre VMs |
| Practicar SSH a `localhost` (pts) | Clonar VM o instalar Rocky otra vez |
| Editar `/etc/hosts` cuando exista server2 | Misma red: ej. `192.168.122.10` / `.11` |

**No se puede** simular dos servidores reales con solo aliases en `/etc/hosts` en la misma IP: SSH, firewall y servicios necesitan **dos máquinas** (o dos VMs).

---

## Topología recomendada (simple)

```
                    Red Host-Only 192.168.122.0/24
                    ───────────────────────────────

   ┌─────────────────────┐       ┌─────────────────────┐
   │ server1             │       │ server2             │
   │ 192.168.122.10      │◄─────►│ 192.168.122.11      │
   │ felipe + wheel      │  SSH  │ felipe + wheel      │
   │ (tu VM actual)      │       │ (clon o nueva VM)   │
   └─────────────────────┘       └─────────────────────┘

   Dominio lab (opcional): lab.example.com
   server1.lab.example.com / server2.lab.example.com
```

### Estilo RH199 (cuando tengas 3 VMs)

| Host | IP sugerida | Rol |
|------|-------------|-----|
| workstation | 192.168.122.9 | Entrada del estudiante |
| servera | 192.168.122.10 | Objetivos de examen |
| serverb | 192.168.122.11 | Segundo objetivo |
| serverc | 192.168.122.12 | Tercer objetivo |

Para empezar alcanza **server1 + server2**.

---

## VirtualBox — pasos rápidos

1. **Adaptador 2** en `server1`: Host-Only Adapter → `vboxnet0`.
2. En la VM, IP estática (ej. `nmcli`):
   ```bash
   sudo nmcli con add type ethernet con-name lab ifname enp0s8 \
     ipv4.method manual ipv4.addresses 192.168.122.10/24
   sudo nmcli con up lab
   ```
3. **Clonar** `server1` → `server2` (regenerar MAC) o instalar Rocky de cero.
4. En `server2`: IP `192.168.122.11/24`, hostname `server2.lab.example.com`.
5. En **ambos**: copiar `configs/hosts.lab` a `/etc/hosts` (ver abajo).
6. Ejecutar en cada uno: `sudo bash scripts/setup-server1.sh` o `setup-server2.sh`.

---

## Archivos de este lab

| Archivo | Uso |
|---------|-----|
| `configs/hosts.lab` | Nombres server1/server2 |
| `scripts/setup-server1.sh` | Usuarios de práctica, SSH, sudo |
| `scripts/setup-server2.sh` | Igual en la segunda VM |
| `exercises/01-ssh-y-consolas.md` | Cap. 5 — SSH, tty, pts, claves |
| `exercises/02-systemd-reboot.md` | systemd, reboot, apagado |

---

## Práctica en UNA sola VM (mientras tanto)

En `server1` sin `server2`:

```bash
# Pseudo multi-sesión (pts, no dos hosts)
ssh felipe@localhost
ssh student@localhost   # después de crear student con setup-server1.sh

# Consolas virtuales
Alt+F2 … Alt+F6   → tty distintas, usuarios distintos
```

Eso cubre **Exercise 5-2 parcial** (pts) y **tty**, no routing ni firewall entre hosts.

---

## Comandos de verificación (estilo examen)

```bash
# En server1
ping -c2 server2
ssh felipe@server2 hostname
ssh-copy-id felipe@server2

# En ambos
w
tty
ss -tlnp | grep 22
systemctl status sshd
```

---

## Usuarios de práctica (creados por los scripts)

| Usuario | Uso |
|---------|-----|
| `felipe` | Tu usuario principal (wheel) |
| `student` | Segundo usuario, SSH entre hosts |
| `erik` | Ejercicios permisos/grupos (libro) |

Contraseñas: las definís al correr el script o en clase; **no uses contraseñas reales en producción**.
