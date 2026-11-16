---
tipo: tema
nombre: Posibles errores en el examen
aliases:
  - errores examen
  - nmtui 0
tags:
  - tema
  - examen
  - EX200
---

# Posibles errores en el examen

Espacio para juntar relatos de gente que sacó **0** (u otro fallo raro) y **no queda claro por qué**. Red Hat no explica el detalle del score. Acá se anota la fuente, el minuto y qué se puede comparar después.

Volver a [[temas/_indice|Temas]] · [[tableros/inicio|Inicio]].

## Cómo usar esta nota

1. Agregá un caso nuevo debajo (video, post, chat).
2. Poné **minuto** o timestamp si hay.
3. Separá lo que la persona **cree** que falló de lo que **puede** haber fallado de verdad.
4. Cuando aparezca otro caso parecido, enlazalo en la misma fila o sección.

---

## Caso: red con `nmtui` → 0%

| Campo | Valor |
| ----- | ----- |
| Fuente | [YouTube — tips RHCSA / EX200 2025](https://www.youtube.com/watch?v=em2bZj8_ZKY&t=231s) |
| Minuto | **3:51** (empieza a hablar del error) · link con tiempo: `t=231` |
| Qué dice | Usó **nmtui** (en el audio se oye “NM2E” / “NM2”) para armar la red. La IP “estaba como pedía el enunciado”. Igual sacó **0 puntos / 0%** en network management. Aprobó igual. |
| Qué recomienda él | La próxima vez hacerlo solo con **`nmcli`**, sin nmtui. |
| Minutos útiles | **3:51** error con nmtui · **4:26** “zero points” · **4:31** “0% on network management” · **~4:58** “use NMCLI… not use NM2 at all” |
| Comparar con | Caso Reddit más abajo (mismo archivo) |

### Por qué “no tiene sentido” si `nmtui` y `nmcli` son lo mismo

En el blueprint los dos son NetworkManager. No hay evidencia pública de que nmtui esté prohibido.

Lo que sí cuadra con un 0 aunque “la IP se veía bien”:

- Interfaz equivocada (NAT del lab vs la NIC del enunciado)
- Conexión no activada / sin `autoconnect` / no persistió al **reboot**
- Faltó gateway, DNS o hostname
- El corrector mira un perfil o archivo concreto y nmtui dejó otro nombre/ruta
- Chequeo por `nmcli` / keyfiles y el estado real no matchea lo que vos miraste en la GUI

**Hipótesis de trabajo:** el 0 no prueba “nmtui baneado”; prueba “algo del objetivo de red no pasó el auto-check”. Como Red Hat no dice cuál, la gente culpa a la herramienta.

**Práctica acá:** preferir `nmcli`, verificar, y **reboot**. No porque nmtui esté mal en teoría, sino para reducir esa duda en el examen.

---

## Caso Reddit — nmtui + reboot + SSH OK → 0%

| Campo | Valor |
| ----- | ----- |
| Fuente | [r/redhat_certification — Just Passed my RHCSA, but I am contesting my results](https://www.reddit.com/r/redhat_certification/comments/1xgpk2s/just_passed_my_rhcsa_but_i_am_contesting_my/) |
| Fecha post | ~19 días antes de leerlo (nov 2026) |
| Examen | EX200 v10; aprobó; está contestando un resultado con Red Hat |
| Qué dice | En el lab casero `nmcli connection modify` le anda. **En el examen `nmcli` le fallaba** (“interface didn’t exist” con device name y con connection name). Perdió ~30 min. Por un tip de Reddit probó **`nmtui`** (primera vez). Pasó la conexión de automática a manual, cargó la IP, **reinició**, la config quedó, pudo **SSH a la IP nueva**, siguió el resto. Score: **0%** en esa pregunta. Pidió review a Red Hat. |
| Qué cree / pide | Que revisen: él verificó persistencia y SSH. |
| Qué podría haber fallado igual | Hostname, DNS, gateway, interfaz “correcta” vs la que chequean, perfil/nombre de conexión, otro criterio del auto-grader que no se ve en `ip a` + SSH. |
| Notas al comparar con el video | **Al revés del YouTube:** allá culpa a nmtui y pide nmcli; acá nmcli no le anduvo en el examen, nmtui sí “funcionó” a ojo, y **igual 0%**. Refuerza: no se sabe el porqué real; no alcanza con “usé la herramienta X”. |

---

## Caso Reddit — aprobó con 253 y 0% en shell script “simple”

| Campo | Valor |
| ----- | ----- |
| Fuente | [r/redhat_certification — RHCSA v10-200k DONE](https://www.reddit.com/r/redhat_certification/comments/1xq14d1/rhcsa_v10200k_done/) |
| Resultado | PASS · score **253** (mínimo 210) · 2 nov 2026 |
| Qué dice el OP | Aprobó. En comentarios admite **0% en “create simple shell script”** y no sabe por qué; “era simple” y no era su foco de estudio. |
| Comentarios útiles | Otro también pasó con 0% en scripts. Tips: `shellcheck`; en el examen hay **repo full** (no solo ISO). Estudio del OP: ~1 mes de simuladores en el laburo. |
| Lectura | Otra vez: estado final / detalle del script (shebang, `chmod +x`, path exacto, salida esperada) puede tumbar el % aunque “casi” ande. No es el caso nmtui, pero el mismo patrón de opacidad. |

---

## Otros 0% del mismo video (para no mezclar)

Mismo autor, mismo video: [em2bZj8_ZKY](https://www.youtube.com/watch?v=em2bZj8_ZKY).

| Tema | Minuto aprox. | Qué pasó |
| ---- | ------------- | -------- |
| Containers / Podman + systemd usuario | ~9:03 y ~10:40 | 0% en la pregunta de container. Creó como root; el servicio para el user (ej. “Valhalla”) no arrancaba persistente al reboot. |

Eso es otro objetivo. No confundirlo con el caso nmtui.
