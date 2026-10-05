# Guía para el otro agente — bajar informe RHCSA a Descargas (Windows)

## Objetivo
Copiar a `C:\Users\User0085\Downloads\` estos archivos de la VM Rocky:

1. **`/home/felipe/Informe-RHCSA-Gerencia.html`** ← **preferido para gerencia** (look marketing, gráficos, KPIs)
2. **`/home/felipe/dev/rhsca-practice/rhcsa-lab-base/informes/Informe-Progreso-RHCSA-Felipe.pdf`** ← PDF visual (copia canónica en el vault)

## Cómo bajar (PowerShell)

Si hay port-forward SSH `127.0.0.1:2222` → guest 22:

```powershell
scp -P 2222 felipe@127.0.0.1:/home/felipe/Informe-RHCSA-Gerencia.html "$env:USERPROFILE\Downloads\"
scp -P 2222 felipe@127.0.0.1:/home/felipe/dev/rhsca-practice/rhcsa-lab-base/informes/Informe-Progreso-RHCSA-Felipe.pdf "$env:USERPROFILE\Downloads\"
```

## PDF “bonito” desde el HTML (recomendado)

El HTML se ve mejor. En Windows:

1. Abrir `Informe-RHCSA-Gerencia.html` con Chrome/Edge  
2. `Ctrl+P` → Destino: **Microsoft Print to PDF** / Guardar como PDF  
3. Márgenes: mínimos · Gráficos de fondo: **activado**  
4. Guardar en Descargas como `Informe-RHCSA-Gerencia.pdf`

## Verificar

```powershell
Get-ChildItem "$env:USERPROFILE\Downloads\Informe-RHCSA*"
```

## Nota red
IP interna VM `10.0.2.15` (NAT) no sirve desde Windows sin port-forward o Bridged.
