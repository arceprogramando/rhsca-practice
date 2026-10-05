# Lab 02 — systemd y reinicio (Cap. 5)

**Solo en VM de lab** — no en VPS de producción sin aviso.

## Ejercicios

1. Estado del sistema:
   ```bash
   systemctl status sshd
   systemctl is-enabled sshd
   ```

2. Reinicio recomendado (examen):
   ```bash
   sudo systemctl reboot
   ```

3. Apagado:
   ```bash
   sudo systemctl poweroff
   ```
   Volver a encender: panel VirtualBox → **Start**.

4. Comparar (no ejecutar en VPS crítico):
   - `sudo systemctl halt` vs `poweroff` — leer `man systemd-halt`.

5. SysRq (solo lectura en lab):
   ```bash
   cat /proc/sys/kernel/sysrq
   # echo b > /proc/sysrq-trigger  → NO en VM con trabajo sin guardar
   ```

## Pregunta

¿Por qué en el examen preferís `sudo systemctl reboot` en lugar de `su -` + `reboot`?
