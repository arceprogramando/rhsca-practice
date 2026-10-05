---
tipo: tablero
tags:
  - tablero
  - progreso
---

# Progreso

Informe actual (PDF):

`rhcsa-lab-base/informes/Informe-Progreso-RHCSA-Felipe.pdf`

Generadores y guía de descarga: carpeta `rhcsa-lab-base/informes/`.

Checklist oficial: [[rhcsa-lab-base/cheatsheets/ex200-objetivos-oficiales|Objetivos EX200]].

Evaluación vs labs: [[rhcsa-lab-base/labs/simulacros/README-evaluacion-vs-informe|Simulacros]].

## Camino

RH104 + RH124 + RH134 → **RH199** → EX200.

## Días recientes

```dataview
TABLE lab, horas, temas, animo
FROM "diario"
WHERE tipo = "diario"
SORT fecha DESC
LIMIT 14
```

## Temas tocados

```dataview
TABLE length(file.inlinks) as menciones
FROM "temas"
SORT menciones DESC
```
