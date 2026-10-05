#!/usr/bin/env bash
# setup-server2.sh — igual que server1 pero hostname server2
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
exec bash "${SCRIPT_DIR}/setup-server1.sh" server2 lab.example.com
