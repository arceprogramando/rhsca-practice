#!/usr/bin/env bash
# setup-server1.sh — preparar server1 para lab RHCSA (ejecutar con sudo)
set -euo pipefail

HOST_SHORT="${1:-server1}"
LAB_DOMAIN="${2:-lab.example.com}"

echo "==> Hostname: ${HOST_SHORT}.${LAB_DOMAIN}"
hostnamectl set-hostname "${HOST_SHORT}.${LAB_DOMAIN}"

echo "==> Paquetes SSH"
dnf install -y openssh-server openssh-clients 2>/dev/null || true
systemctl enable --now sshd

echo "==> Usuario student (si no existe)"
if ! id student &>/dev/null; then
  useradd -m student
  echo "student:student" | chpasswd
  usermod -aG wheel student 2>/dev/null || true
fi

echo "==> Usuario erik (ejercicios passwd/grupos)"
if ! id erik &>/dev/null; then
  useradd -m erik
  echo "erik:erik" | chpasswd
fi

echo "==> Directorio SSH para root (referencia)"
install -d -m 700 /root/.ssh

echo "==> Firewall: permitir SSH (si firewalld activo)"
if systemctl is-active firewalld &>/dev/null; then
  firewall-cmd --permanent --add-service=ssh
  firewall-cmd --reload
fi

echo "==> Listo. Verificar:"
echo "    hostnamectl"
echo "    systemctl status sshd"
echo "    getent passwd student erik"
