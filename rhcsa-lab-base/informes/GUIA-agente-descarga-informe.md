# Guía para el otro agente — bajar informe RHCSA a Descargas (Windows)

## Objetivo
Copiar a `C:\Users\User0085\Downloads\` el PDF que genera `generar-informe-rhcsa.py`:

**`/home/felipe/Informe-Progreso-RHCSA-Felipe.pdf`**

## Cómo bajar (PowerShell)

Si hay port-forward SSH `127.0.0.1:2222` → guest 22:

```powershell
scp -P 2222 felipe@127.0.0.1:/home/felipe/Informe-Progreso-RHCSA-Felipe.pdf "$env:USERPROFILE\Downloads\"
```

## Verificar

```powershell
Get-ChildItem "$env:USERPROFILE\Downloads\Informe-RHCSA*"
```

## Nota red
IP interna VM `10.0.2.15` (NAT) no sirve desde Windows sin port-forward o Bridged.
