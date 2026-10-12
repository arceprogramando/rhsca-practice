RHCSA / RH104 — pack de estudio (workstation.lab.example.com)
Generado: 2026-09-18
Usuario: felipe

Vault Obsidian
==============
La raíz del repo (/home/felipe/dev/rhsca-practice) es el vault.
Abrir esa carpeta en Obsidian. Mapa: tableros/inicio.md
Diario de estudio: diario/YYYY/YYYY-MM-DD.md
Este pack (rhcsa-lab-base/) es el material de labs e informes.

Qué hay adentro
===============

cheatsheets/
  rhcsa-comandos-principales.md
    Glosario / cheat sheet: lab workstation+servera (student),
    apropos, teclado vs LANG, users, GECOS, getent, login.defs,
    sudoers (%grupo ALL=(ALL) ALL), rd.break (reset root),
    usermod -aG (grupos complementarios; NUNCA -G solo),
    umask vs chmod; setuid/setgid/sticky (3770 techdocs),
    PASS_MAX_DAYS / chage (aging: -M vs -E account expire; date +%F),
    día EX200 (UI Red Hat / proctor), awk/passwd, tar, find,
    redirecciones, ritual EX200.
  ex200-objetivos-oficiales.md
    Objetivos EX200 (página Red Hat) en checklist + tu avance.
  rh199-indice-curso.md
    Índice RH199 Rapid Track (caps 1–21) mapeado a EX200.

labs/
  simulacros/
    exam-simulation-openddemonicos.pdf
    README-evaluacion-vs-informe.md   # qué labs podés hacer ahora vs RH199 38/154
  ejercicios-rh104/
    ejercicio_final_rh104.pdf
    ejercicio_final_rh104_resultados.pdf
  nivel-compreview/
    README.md + lab01-biblioteca, lab02-soporte-it, lab03-deploy-docs
    (enunciado + setup.sh + check.sh, estilo RH104 Cap. 8)
  labs6/lab-6-1
  lab-permisos/          práctica chmod/chown
  lab-links/             hard/soft links
  lab-links-practica/
  lab-links-guiado.sh
  rhcsa_lab-nbaud/       guía de https://github.com/nbaud/rhcsa_lab.git

rhcsa-lab/
  Lab multi-host estilo RH199/EX200 (server1+server2)
  exercises/01-ssh-y-consolas.md
  exercises/02-systemd-reboot.md
  scripts/setup-server1.sh, setup-server2.sh
  configs/hosts.lab

Guía tomada de nbaud/rhcsa_lab
==============================
Origen: https://github.com/nbaud/rhcsa_lab.git (Nico)
Copia local: labs/rhcsa_lab-nbaud/
Los archivos están en este repo. Esa carpeta ya no tiene un .git propio.

Me guío de ese repo en esto:
  - Lab de dos VMs con Vagrant (Rocky Linux 10, VirtualBox):
    server 172.16.1.13 y client 172.16.1.12, red host-only.
    En server: httpd, firewalld, el boolean de SELinux
    httpd_can_network_connect y un disco extra.
    En client: curl, lynx, firewalld y ssh.
  - Gaps de práctica que trae el repo:
    gap-q01  scripting (find de *.txt)
    gap-q02  systemd timers (servicio cleanup a los :30)
    gap-q05  SELinux en enforcing con vsftpd
             (anon descarga en pub y sube en incoming;
              sin setenforce 0, sin chmod 777, sin mover a /var/ftp)

pdfs-curso/
  ejercicio final.pdf          (RH104 compreview)
  rhcsa9-cert-guide.pdf        (libro Cert Guide, ~21 MB)

informes/
  Informe-Progreso-RHCSA-Felipe.pdf
  generar-informe-rhcsa.py
  GUIA-agente-descarga-informe.md

scripts-practica/
  Scripts bash de práctica (arrays, loops, validar dirs, etc.)

capturas/
  Capturas de checks RH y assets Red Hat

canvas/
  rhcsa-progreso.canvas.tsx (tablero de avance en Cursor)

NO incluido (a propósito)
  .ssh, user_passwords.txt, CV, configs de Cursor/IDE

Cómo descomprimir en Windows (PowerShell)
  tar -xzf "$env:USERPROFILE\Downloads\rhcsa-estudio-pack.tar.gz" -C "$env:USERPROFILE\Downloads\"
