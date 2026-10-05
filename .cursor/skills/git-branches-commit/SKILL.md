---
name: git-branches-commit
description: >-
  Guía nombres de rama y mensajes de commit (Conventional Commits) para
  rhsca-practice. Usar prefijo feat en ramas, no feature. Preguntar siempre si hay
  ticket Jira si no lo dieron. Incluir el ticket en el commit. Nunca agregar
  Co-authored-by de Cursor ni de ningún agente IA. Asunto máximo 50 caracteres;
  cuerpo con -m adicionales. Nunca ejecutar git commit: devolver siempre el
  comando para copiar. Usar al pedir rama, mensaje de commit, convención git,
  o al crear commits, push o PR en este proyecto.
---

# Ramas y commits – convenciones

Repo personal de notas Markdown (`README.md`, `daily/YYYY-MM-DD.md` y otras carpetas de memoria). Seguir estas reglas en **cada** rama, commit, push o PR de este proyecto.

## Cuándo usar este skill

- El usuario pide un **nombre de rama** o **mensaje de commit**.
- Pide sugerencias para hacer push, PR o documentar cambios en git.
- Se discute convención de ramas o commits en el proyecto.
- El agente va a **proponer** un commit o una rama. El commit no se ejecuta: se entrega el comando para copiar.

---

## Ticket Jira (obligatorio preguntar)

- **Antes** de sugerir rama/commit: si el usuario **no** indicó un ticket, preguntar:
  > ¿Tenés algún ticket? (ej. RRHH-498)
- Si responde un ticket (`RRHH-XXX`, etc.):
  - Incluirlo en la **rama**: `feat/RRHH-498-descripcion-corta`
  - Incluirlo en el **cuerpo del commit** con un `-m` dedicado, primera línea del cuerpo:
    ```bash
    git commit -m "tipo: descripción corta" -m "Ticket: RRHH-498."
    ```
  - Si cabe en el asunto (≤50 caracteres), también puede ir al inicio de la descripción:
    `feat: RRHH-498 descripción corta`
  - Preferir **Ticket: RRHH-XXX.** en el cuerpo para no comer espacio del asunto.
- Si **no** hay ticket: sugerir igual sin `Ticket:` en el cuerpo ni prefijo en la rama.

---

## Formato de salida (para copiar)

- **Rama:** darla siempre en forma de comando listo para copiar:
  ```bash
  git checkout -b feat/RRHH-498-descripcion-rama
  ```
- **Commits:** devolver **siempre** el comando `git commit` listo para copiar. **Nunca ejecutarlo.**
  - **No incluir `git add`** salvo que el usuario lo pida explícitamente.
- **Commits:** cuando hay cambios en backend **y** frontend, devolver **dos comandos de commit separados**, uno por capa:
  - Agregar encabezados `#backend` y `#frontend` arriba de cada bloque para identificar rápido cada commit.
  - Backend:
    ```text
    #backend
    ```
    ```bash
    git commit -m "tipo: descripción backend" -m "Ticket: RRHH-498."
    ```
  - Frontend:
    ```text
    #frontend
    ```
    ```bash
    git commit -m "tipo: descripción frontend" -m "Ticket: RRHH-498."
    ```
- **Asunto de cada commit:** ≤50 caracteres; si hace falta más detalle, usar segundo `-m` para el cuerpo:
  ```bash
  git commit -m "tipo: descripción corta" -m "Ticket: RRHH-498." -m "Detalle adicional aquí."
  ```

---

## Nombres de rama

- **Prefijo:** usar **`feat`**, no `feature`.
- **Formato:** `tipo/descripcion-corta-en-minusculas`.
- Con ticket: `tipo/RRHH-498-descripcion-corta`.
- Tipos habituales: `feat`, `fix`, `docs`, `refactor`, `chore`.

**Ejemplos:**

| Cambio | Rama |
|--------|------|
| Nueva funcionalidad con ticket | `feat/RRHH-498-goce-cumpleanos-mes` |
| Nueva funcionalidad sin ticket | `feat/vacaciones-30-dias-anticipacion` |
| Corrección de bug | `fix/RRHH-501-mensaje-fecha-valida` |
| Solo documentación | `docs/architectura-reglas-negocio` |

---

## Mensajes de commit (Conventional Commits)

- **Formato:** `tipo: descripción en minúsculas`.
- **Ticket:** siempre en el cuerpo como `Ticket: RRHH-XXX.` cuando exista.
- **Límite de caracteres en el asunto:** máximo **50 caracteres** en la primera línea (el asunto).
- **Límite de caracteres en el cuerpo:** cada línea del cuerpo ≤**120** caracteres.
- **Si hace falta más información:** ponerla en el cuerpo con **varios `-m` cortos**, cada uno ≤120 caracteres. Ejemplo:
  ```bash
  git commit -m "feat: goce cumpleaños solo en mes natalicio" \
    -m "Ticket: RRHH-498." \
    -m "Reemplaza ventana de 30 días corridos por el mes calendario del natalicio."
  ```
- **Sin paréntesis** en el mensaje: no usar scope entre paréntesis ni aclaraciones entre paréntesis.
- Tipos: `feat`, `fix`, `docs`, `refactor`, `chore`, `test`, `style`.

### Co-author — prohibido

- **Nunca** agregar `Co-authored-by:` al commit (ni en el mensaje sugerido, ni al ejecutar `git commit`).
- **Nunca** firmar como Cursor, Cursor Agent, ni ningún agente/modelo de IA.
- El autor del commit es solo el usuario / su `user.name` y `user.email` de git.
- Si el entorno o un hook intenta inyectar co-author, **omitirlo** y dejar el mensaje sin esa línea.

**Evitar:**

- `feat(licencias): ...` → preferir `feat: ...` sin scope entre paréntesis.
- `feat: algo (backend)` → no paréntesis en la descripción.
- `Co-authored-by: Cursor <cursoragent@cursor.com>` u otras variantes de co-author IA.

---

## Resumen rápido

| Qué | Regla |
|-----|--------|
| Ticket | Preguntar si no lo dieron. Incluir en rama y en cuerpo del commit |
| Rama | `feat/RRHH-498-descripcion` o `feat/descripcion`. Entregar como `git checkout -b ...` |
| Entrega de commits | Siempre el comando para copiar. Nunca ejecutar `git commit`. Sin `git add`, salvo pedido explícito |
| Etiquetas visuales | Si hay backend y frontend, usar `#backend` y `#frontend` |
| Commit asunto | Máximo 50 caracteres |
| Commit cuerpo | `Ticket: RRHH-XXX.` + detalle en `-m` adicionales ≤120 chars |
| Co-author | **Nunca** `Co-authored-by` de Cursor ni de agentes IA |
| Tipos | feat, fix, docs, refactor, chore, test, style |
