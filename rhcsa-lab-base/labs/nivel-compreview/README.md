# Labs nivel Comprehensive Review (estilo RH104 Cap. 8)

## Importante: entorno

El PDF `ejercicio final.pdf` es del curso **RH104-9.1** en el laboratorio Red Hat:

- usuarios `student` / máquinas del **ROL** (`lab start compreview-review1`)
- grading con `lab grade ...`

**Estos labs NO usan eso.** Están pensados para **tus VMs**:

| Máquina     | Rol típico                          |
|-------------|--------------------------------------|
| `workstation` | donde trabajás / donde bajás archivos |
| `servera`     | donde resolvés la mayoría de tareas   |

Usuario sugerido: `felipe` (o el que uses con `sudo`).

## Complejidad (igual que el PDF)

Cada lab combina, en un solo escenario:

- redirección (`>`, `2>`, `&>`)
- organizar archivos/dirs (`mkdir`, `mv`, `cp -r`)
- editor / filtrar contenido
- `tar` comprimido
- `sudo` + `chown` / `chmod` / grupos
- enlaces simbólicos
- `find`, `du`, a veces `scp` entre VMs

## Cómo usar cada lab

```bash
# en servera (o la VM que indique el enunciado)
cd ~/labs/nivel-compreview/lab01-biblioteca
bash setup/setup.sh          # deja el estado inicial
# ... resolvés el ENUNCIADO.md sin mirar pistas ...
bash checks/check.sh         # autocorrección local
```

Orden recomendado: **lab01 → lab02 → lab03** (misma dificultad; cambia el “cuento”).

## Origen

Basado en: RH104 Cap. 8 — *Lab: Manipulating Files and Directories* (`compreview-review1`).
