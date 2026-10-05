#!/usr/bin/env python3
"""
DOCX maestro editable del informe RHCSA.
Respeta el diseño del PDF (colores, secciones, KPIs, prioridades, links)
para editar en Word y exportar a PDF desde ahí.
"""

from __future__ import annotations

import zipfile
from datetime import date
from pathlib import Path
from xml.sax.saxutils import escape

DOCX_OUT = Path("/home/felipe/Informe-Progreso-RHCSA-Felipe.docx")

PLAN_START = date(2026, 8, 18)
PLAN_END = date(2026, 10, 30)
REPORT_AS_OF = date(2026, 9, 15)
BOOK_PAGE = 335
BOOK_TOTAL = 1593
BOOK_USEFUL = 1135


def plan_metrics(today: date | None = None) -> dict:
    today = today or REPORT_AS_OF
    elapsed = (today - PLAN_START).days
    left = (PLAN_END - today).days
    total = (PLAN_END - PLAN_START).days
    pct_cal = round(100 * elapsed / total) if total else 0
    book_left = BOOK_TOTAL - BOOK_PAGE
    useful_left = max(0, BOOK_USEFUL - BOOK_PAGE)
    avg = round(BOOK_PAGE / elapsed) if elapsed else 0
    need_pdf = round(book_left / left) if left else 0
    need_useful = round(useful_left / left) if left else 0
    return {
        "elapsed": elapsed,
        "left": left,
        "total": total,
        "pct_cal": pct_cal,
        "book_page": BOOK_PAGE,
        "book_total": BOOK_TOTAL,
        "book_left": book_left,
        "useful_left": useful_left,
        "avg": avg,
        "need_pdf": need_pdf,
        "need_useful": need_useful,
        "book_pct": round(100 * BOOK_PAGE / BOOK_TOTAL),
    }


URL_EX200 = "https://www.redhat.com/es/services/training/ex200-red-hat-certified-system-administrator-rhcsa-exam"
URL_EX294 = "https://www.redhat.com/es/services/training/ex294-red-hat-certified-engineer-rhce-exam-red-hat-enterprise-linux-9"
URL_RH124 = "https://www.credly.com/badges/b3bb2779-eefd-4646-813c-e142e5c9d219/linked_in_profile"
URL_RH134 = "https://www.credly.com/badges/a6a4a878-0fec-4a05-9c66-57cc1e6de2f6/linked_in?t=tioxto"
URL_RH199 = "https://rol.redhat.com/rol/app/courses/rh199-10.0/pages/pr01"
URL_YT_TIPS = "https://www.youtube.com/watch?v=QlAwLcLz8CM"
URL_YT_INSIDE = "https://www.youtube.com/watch?v=Me6Y12-sux8"
URL_YT_RUIN = "https://www.youtube.com/watch?v=-ZH4M-VShN8"
URL_YT_PREP = "https://www.youtube.com/watch?v=fkHWkjQD3N8"
URL_YT_NICODEMOS = (
    "https://www.youtube.com/watch?v=O7yPeKjyWO0&list=PLzwsIhHG_OdZiC6ugglW4TzjIM8wrJDrt"
)

NS_W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS_R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
NS_REL = "http://schemas.openxmlformats.org/package/2006/relationships"

NAVY, WHITE, DARK, GRAY = "151515", "FFFFFF", "151515", "5C6578"
RED, AMBER, BLUE, GREEN = "EE0000", "F5921B", "0066CC", "63993D"
LIGHT, LIGHT_BLUE, BAR_BG = "F2F2F2", "EEF6FB", "E6EAEF"


def rpr(*, bold=False, size=22, color=DARK, underline=False) -> str:
    parts = [
        f'<w:sz w:val="{size}"/>',
        f'<w:szCs w:val="{size}"/>',
        f'<w:color w:val="{color}"/>',
    ]
    if bold:
        parts.append("<w:b/>")
    if underline:
        parts.append('<w:u w:val="single"/>')
    return "<w:rPr>" + "".join(parts) + "</w:rPr>"


def run(text: str, **kw) -> str:
    return f'<w:r>{rpr(**kw)}<w:t xml:space="preserve">{escape(text)}</w:t></w:r>'


def para(*runs: str, before: int = 60, after: int = 60) -> str:
    return (
        f'<w:p><w:pPr><w:spacing w:before="{before}" w:after="{after}"/></w:pPr>'
        + "".join(runs)
        + "</w:p>"
    )


def heading(text: str, level: int = 2) -> str:
    size = {1: 36, 2: 28, 3: 24}.get(level, 24)
    return para(run(text, bold=True, size=size, color=NAVY), before=240, after=100)


def bullet(text: str, color: str = DARK) -> str:
    return (
        '<w:p><w:pPr><w:ind w:left="288"/><w:spacing w:after="40"/></w:pPr>'
        + run("• " + text, size=20, color=color)
        + "</w:p>"
    )


def spacer(n: int = 80) -> str:
    return f'<w:p><w:pPr><w:spacing w:before="{n}" w:after="0"/></w:pPr></w:p>'


def tc(
    text: str,
    *,
    bold: bool = False,
    fill: str | None = None,
    color: str = DARK,
    size: int = 18,
    width: int | None = None,
    center: bool = False,
) -> str:
    tcpr = ["<w:tcPr>"]
    if width:
        tcpr.append(f'<w:tcW w:w="{width}" w:type="dxa"/>')
    if fill:
        tcpr.append(f'<w:shd w:val="clear" w:color="auto" w:fill="{fill}"/>')
    tcpr.append("</w:tcPr>")
    jc = '<w:jc w:val="center"/>' if center else ""
    return (
        f"<w:tc>{''.join(tcpr)}<w:p><w:pPr>{jc}</w:pPr>"
        + run(text, bold=bold, size=size, color=color)
        + "</w:p></w:tc>"
    )


def tbl(rows_xml: str, borders: bool = True) -> str:
    b = ""
    if borders:
        b = (
            "<w:tblBorders>"
            f'<w:top w:val="single" w:sz="4" w:color="{BAR_BG}"/>'
            f'<w:left w:val="single" w:sz="4" w:color="{BAR_BG}"/>'
            f'<w:bottom w:val="single" w:sz="4" w:color="{BAR_BG}"/>'
            f'<w:right w:val="single" w:sz="4" w:color="{BAR_BG}"/>'
            f'<w:insideH w:val="single" w:sz="4" w:color="{BAR_BG}"/>'
            f'<w:insideV w:val="single" w:sz="4" w:color="{BAR_BG}"/>'
            "</w:tblBorders>"
        )
    return (
        f'<w:tbl><w:tblPr><w:tblW w:w="5000" w:type="pct"/>'
        f'<w:tblLayout w:type="fixed"/>{b}</w:tblPr>{rows_xml}</w:tbl>'
    )


def tr(*cells: str) -> str:
    return "<w:tr>" + "".join(cells) + "</w:tr>"


def header_banner() -> str:
    cell = f"""<w:tc>
      <w:tcPr><w:tcW w:w="9360" w:type="dxa"/><w:shd w:val="clear" w:fill="{NAVY}"/></w:tcPr>
      <w:p><w:pPr><w:spacing w:before="160" w:after="40"/></w:pPr>{run("Informe de Progreso", bold=True, size=36, color=WHITE)}</w:p>
      <w:p><w:pPr><w:spacing w:before="0" w:after="40"/></w:pPr>{run("Certificación RHCSA (EX200)", bold=True, size=24, color=WHITE)}</w:p>
      <w:p><w:pPr><w:spacing w:before="0" w:after="160"/></w:pPr>{run("Candidato: Felipe Antonio Aleman Arce", size=20, color=WHITE)}</w:p>
    </w:tc>"""
    return tbl(tr(cell), borders=False) + spacer(140)


def kpi_block(m: dict | None = None) -> str:
    m = m or plan_metrics()
    items = [
        (str(m["elapsed"]), ("Días desde el", "comienzo del plan"), GREEN),
        (str(m["left"]), ("Días a finalizar la", "Práctica pre-examen"), AMBER),
        ("2/3", "Cursos base", GREEN),
    ]
    accents = tr(*[tc(" ", fill=c, size=4, width=3120, center=True) for _, _, c in items])
    cells = []
    for val, label, col in items:
        if isinstance(label, tuple):
            label_xml = "".join(
                f'<w:p><w:pPr><w:jc w:val="center"/><w:spacing w:before="0" w:after="20"/></w:pPr>{run(line, size=15, color=GRAY)}</w:p>'
                for line in label
            )
        else:
            label_xml = f'<w:p><w:pPr><w:jc w:val="center"/><w:spacing w:before="0" w:after="100"/></w:pPr>{run(label, size=16, color=GRAY)}</w:p>'
        cells.append(
            f"""<w:tc>
  <w:tcPr><w:tcW w:w="3120" w:type="dxa"/><w:shd w:val="clear" w:fill="{LIGHT}"/></w:tcPr>
  <w:p><w:pPr><w:jc w:val="center"/><w:spacing w:before="100" w:after="40"/></w:pPr>{run(val, bold=True, size=40, color=col)}</w:p>
  {label_xml}
</w:tc>"""
        )
    return tbl(accents + tr(*cells), borders=False) + spacer(140)


def pipeline_block() -> str:
    steps = [
        ("RH024", "Video·OK", GREEN),
        ("RH104", "43/56", AMBER),
        ("RH124", "Hecho", GREEN),
        ("RH134", "Hecho", GREEN),
        ("Libro", "335/1593", BLUE),
        ("RH199", "10/154", AMBER),
        ("EX200", "Obj.", AMBER),
        ("EX294", "Ruta", BLUE),
    ]
    cells = []
    for name, sub, col in steps:
        cells.append(
            f"""<w:tc>
  <w:tcPr><w:tcW w:w="1170" w:type="dxa"/><w:shd w:val="clear" w:fill="{col}"/></w:tcPr>
  <w:p><w:pPr><w:jc w:val="center"/><w:spacing w:before="60" w:after="10"/></w:pPr>{run(name, bold=True, size=14, color=WHITE)}</w:p>
  <w:p><w:pPr><w:jc w:val="center"/><w:spacing w:before="0" w:after="60"/></w:pPr>{run(sub, size=10, color=WHITE)}</w:p>
</w:tc>"""
        )
    return tbl(tr(*cells), borders=False) + spacer(120)


def callout(title: str, lines: list[str]) -> str:
    inner = [
        f'<w:p><w:pPr><w:spacing w:before="100" w:after="60"/></w:pPr>{run(title, bold=True, size=22)}</w:p>'
    ]
    for line in lines:
        inner.append(
            f'<w:p><w:pPr><w:spacing w:before="0" w:after="40"/></w:pPr>{run(line, size=20)}</w:p>'
        )
    left = tc(" ", fill=BLUE, width=140)
    right = (
        f'<w:tc><w:tcPr><w:tcW w:w="9220" w:type="dxa"/>'
        f'<w:shd w:val="clear" w:fill="{LIGHT_BLUE}"/></w:tcPr>'
        + "".join(inner)
        + "<w:p/></w:tc>"
    )
    return tbl(tr(left, right), borders=False) + spacer(100)


def prio_color(score: int) -> str:
    if score >= 10:
        return RED
    if score >= 9:
        return AMBER
    if score >= 7:
        return BLUE
    return GREEN


def bar_cell(score: int) -> str:
    bar = ("█" * score) + ("░" * (10 - score))
    col = prio_color(score)
    return f"""<w:tc>
  <w:tcPr><w:tcW w:w="4680" w:type="dxa"/><w:shd w:val="clear" w:fill="{BAR_BG}"/></w:tcPr>
  <w:p><w:pPr><w:spacing w:before="40" w:after="40"/></w:pPr>{run(bar, size=16, color=col)}</w:p>
</w:tc>"""


def priority_table() -> str:
    prios = [
        ("Reset root / rd.break", 10),
        ("Persistencia al reboot", 10),
        ("Storage + LVM + fstab", 10),
        ("SELinux", 10),
        ("Red + firewall (nmcli/nmtui)", 9),
        ("Boot / troubleshoot", 9),
        ("systemd + cron", 7),
        ("DNF + Flatpak", 5),
        ("Users / grupos", 4),
        ("Permisos + ACL", 3),  # chmod OK (11 sep); afianzar chown/ACL
        ("SSH", 3),
        ("Hard/soft links", 3),
        ("Comprimir/extraer (tar)", 2),
        ("Shell / archivos", 1),
    ]
    rows = tr(
        tc("Tema", bold=True, fill=LIGHT, width=3600, size=16),
        tc("Nivel", bold=True, fill=LIGHT, width=4680, size=16, center=True),
        tc("#", bold=True, fill=LIGHT, width=1080, size=16, center=True),
    )
    for name, score in prios:
        col = prio_color(score)
        rows += tr(
            tc(name, width=3600, size=18),
            bar_cell(score),
            tc(str(score), bold=True, color=col, width=1080, size=20, center=True),
        )
    note = para(
        run(
            "Reset root / rd.break: GRUB → rd.break → remount → chroot → passwd → /.autorelabel. "
            "Persistencia al reboot: fstab, systemctl enable, red/firewall permanentes.",
            size=18,
            color=GRAY,
        ),
        before=80,
        after=40,
    )
    return tbl(rows) + note + spacer(60)


def progress_row(label: str, blocks: int, detail: str, color: str) -> str:
    filled = "█" * blocks
    empty = "░" * (20 - blocks)
    return (
        para(run(label, bold=True, size=20), before=80, after=20)
        + para(run(f"{filled}{empty}  {detail}", size=18, color=color), before=0, after=40)
    )


def link_bullet(label: str, rid: str) -> str:
    return f"""<w:p>
  <w:pPr><w:ind w:left="288"/><w:spacing w:after="40"/></w:pPr>
  {run("• ", size=20)}
  <w:hyperlink r:id="{rid}" w:history="1">
    {run(label, size=20, color=BLUE, underline=True)}
  </w:hyperlink>
</w:p>"""


def simple_table(headers: list[str], rows: list[list[str]], widths: list[int]) -> str:
    head = tr(*[tc(h, bold=True, fill=LIGHT, width=w, size=16) for h, w in zip(headers, widths)])
    body = ""
    for row in rows:
        body += tr(*[tc(c, width=w, size=18) for c, w in zip(row, widths)])
    return tbl(head + body) + spacer(100)


def build_document_xml() -> tuple[str, list[tuple[str, str]]]:
    rels: list[tuple[str, str]] = []

    def add_url(url: str) -> str:
        rid = f"rId{len(rels) + 1}"
        rels.append((rid, url))
        return rid

    r124, r134 = add_url(URL_RH124), add_url(URL_RH134)
    r199, rex200, rex294 = add_url(URL_RH199), add_url(URL_EX200), add_url(URL_EX294)
    ryt1, ryt2 = add_url(URL_YT_TIPS), add_url(URL_YT_INSIDE)
    ryt3, ryt4 = add_url(URL_YT_RUIN), add_url(URL_YT_PREP)
    ryt5 = add_url(URL_YT_NICODEMOS)

    parts: list[str] = []
    parts.append(header_banner())
    parts.append(para(run("Aproximado Finalización Práctica: 30 de octubre de 2026", size=22, color=GRAY)))
    parts.append(
        para(
            run(
                "Examen objetivo: RHCSA (EX200) — Requerido para Ruta RHCE (EX294)",
                size=20,
                color=GRAY,
            )
        )
    )
    parts.append(spacer(60))
    m = plan_metrics()
    parts.append(kpi_block(m))

    parts.append(heading("Pipeline de estudio", 2))
    parts.append(pipeline_block())

    parts.append(heading("Resumen", 2))
    for line in [
        "RH124 y RH134 acreditados (completados previamente).",
        "Examen objetivo: RHCSA (EX200) — requerido para ruta RHCE (EX294).",
        "Refuerzo actual: libro Red Hat RHCSA 9 Cert Guide (Sander van Vugt) + labs.",
        "Cap. 7 Permissions (pág 335) + lab-permisos: chmod OK; afianzar chown (11 sep).",
        "RH199 Rapid Track v10.0 en curso (10/154 pág · Cap. 2 ch02s03 Links · 27 ago).",
        "Path RHCSA: RH024 completado; RH104 Fundamentals v9.1 en curso (43/56 · Cap. 4 · 15 sep).",
        "Fortaleza: chmod/modos octal-simbólico. Refuerzo: chown/ownership, ACL, nmcli, systemd.",
        "Más adelante: storage/LVM, SELinux, firewall y boot.",
    ]:
        parts.append(bullet(line, GRAY))

    parts.append(spacer(40))
    parts.append(
        callout(
            "Problemáticas encontradas",
            [
                "8 sep 2026 — Path RHCSA / cursos fundamentals",
                "Encontré el path correcto para anotarme a rendir el RHCSA en ROL. "
                "Además de RH124 y RH134, el plan exige cursos previos de fundamentals.",
                "RH024 (video Getting Started): COMPLETADO.",
                "RH104 Fundamentals v9.1 EN CURSO (43/56 · Cap. 4 ch04); practica en GNOME via VNC.",
                "Impacto: suma carga al plan (libro + RH199 + RH104) hasta el EX200.",
                "",
                "31 ago 2026 — Lab SSH / VirtualBox",
                "Para practicar Cap. 5 (SSH) de la forma más real posible, monté dos VMs Rocky en VirtualBox "
                "(servidor + cliente). Consumió gran parte de las horas de estudio del día (infraestructura vs páginas del libro).",
                "Trabas: clon con hostname/Machine ID/MAC duplicados; puertos SSH 2200/2222 mezclados.",
                "Segundo disco LVM duplicado trabó el boot; red host-only con IP DHCP (.102) vs plan estático (.10/.11).",
                "nmcli: nombre exacto del perfil (Conexión cableada 1). Resuelto: lab 2 VMs (servera .10 + workstation .11); SSH, scp, sftp y claves (Ex 5-5).",
                "Nota examen: VirtualBox/clonado no entra; sí puede pedirse IP estática con nmcli en una interfaz.",
            ],
        )
    )
    parts.append(spacer(40))
    parts.append(
        callout(
            "Perfil y contexto",
            [
                "Me desenvuelvo como desarrollador FullStack. Al no haber trabajado antes "
                "en el área de sysadmin, algunos conceptos me son nuevos y otros ya los uso "
                "de alguna forma en el día a día.",
            ],
        )
    )
    parts.append(para(run("Disponibilidad", bold=True, size=22), before=160, after=60))
    parts.append(bullet("2 hs de estudio por día en el trabajo + días/horarios disponibles fuera de eso"))
    parts.append(bullet("Extra: martes, jueves y sábado 20 a 22 hs"))
    parts.append(bullet("domingo todo el día"))
    parts.append(para(run("Días ocupados", bold=True, size=22), before=160, after=60))
    parts.append(bullet("Lunes y miércoles: 19 a 22 hs inglés en el CUI"))
    parts.append(bullet("Sábados: universidad de 8 a 15 hs (+ 1 hs de viaje a la universidad)"))
    parts.append(para(run("Otras Obligaciones", bold=True, size=22), before=160, after=60))
    parts.append(bullet("Rendir Matemática Universidad 14 de septiembre"))

    parts.append(heading("Avance cuantitativo y ritmo de estudio", 2))
    parts.append(
        progress_row(
            "Calendario total del plan (18 ago → 30 oct)",
            m["pct_cal"],
            f"{m['elapsed']} transcurridos + {m['left']} restantes = {m['total']} (~{m['pct_cal']}%)",
            BLUE,
        )
    )
    parts.append(
        progress_row(
            "Libro Red Hat RHCSA 9 Cert Guide (Sander van Vugt)",
            m["book_pct"],
            f"{m['book_page']} / {m['book_total']} (~{m['book_pct']}%) · Cap. 7 Permissions Management",
            GREEN,
        )
    )
    parts.append(
        para(
            run(
                f"Libro (PDF {m['book_total']}): faltan {m['book_left']} | 15/día → ~nov | meta 30 oct ({m['left']} d) → ~{m['need_pdf']}/día",
                bold=True,
                size=18,
                color=RED,
            ),
            before=60,
            after=20,
        )
    )
    parts.append(
        para(
            run(
                f"Libro (contenido útil ~{BOOK_USEFUL}): faltan ~{m['useful_left']} | 15/día → ~fin oct | meta 30 oct → ~{m['need_useful']}/día",
                bold=True,
                size=18,
                color=BLUE,
            ),
            before=20,
            after=20,
        )
    )
    parts.append(
        para(
            run(
                f"Promedio hasta hoy: ~{m['avg']} pág/día ({m['book_page']} en {m['elapsed']} d) | para meta: ~{m['need_pdf']} PDF o ~{m['need_useful']} útil",
                bold=True,
                size=18,
                color=GREEN,
            ),
            before=20,
            after=80,
        )
    )
    parts.append(
        progress_row(
            "RH104 Getting Started with Linux Fundamentals v9.1 (ROL)",
            round(100 * 43 / 56),
            "43 / 56 (~77%) · Cap. 4 ch04 · path RHCSA · 15 sep",
            AMBER,
        )
    )
    parts.append(
        para(
            run(
                "RH104: labs en GUI GNOME via VNC (no solo CLI); faltan 13 unidades. Cap. 4 (ch04).",
                bold=True,
                size=18,
                color=GREEN,
            ),
            before=40,
            after=60,
        )
    )
    parts.append(
        progress_row(
            "RH199 Rapid Track v10.0 (ROL)",
            1,
            "10 / 154 (~6%) · Cap. 2 ch02s03 Links · 27 ago",
            AMBER,
        )
    )
    parts.append(
        para(
            run(
                "RH199: Cap. 2 ch02s03 Links / enlaces simbólicos (10/154).",
                bold=True,
                size=18,
                color=GREEN,
            ),
            before=60,
            after=120,
        )
    )

    parts.append(
        heading("Prioridad de estudio (importancia + comodidad · 1 menor · 10 mayor)", 2)
    )
    parts.append(
        para(
            run(
                "Combina lo crítico para el examen con cómo nos sentimos hoy en cada tema.",
                size=18,
                color=GRAY,
            )
        )
    )
    parts.append(priority_table())

    parts.append(heading("Ritmo libro Van Vugt (335 / 1593 pág)", 2))
    parts.append(
        para(
            run(
                "Páginas acumuladas del PDF del libro. Actual: 335 / 1593 · puntos mostrados: 18 ago, 1 sep, 2 sep, 3 sep, 4 sep.",
                size=20,
                color=GRAY,
            )
        )
    )
    parts.append(
        simple_table(
            ["Fecha", "Página del libro"],
            [
                ["18 ago", "80"],
                ["1 sep", "298"],
                ["2 sep", "309"],
                ["3 sep", "321"],
                ["4 sep", "335"],
            ],
            [4680, 4680],
        )
    )

    parts.append(heading("Ritmo RH199 Rapid Track (10 / 154 pág)", 2))
    parts.append(
        para(
            run(
                "Páginas acumuladas del curso en ROL. Actual: 10 / 154 · Cap. 2 ch02s03 Links · 27 ago.",
                size=20,
                color=GRAY,
            )
        )
    )
    parts.append(
        simple_table(
            ["Fecha", "Página RH199"],
            [
                ["27 ago", "10"],
            ],
            [4680, 4680],
        )
    )

    parts.append(heading("Credenciales y horizonte (orden de plan)", 2))
    parts.append(
        simple_table(
            ["Ítem", "Estado"],
            [
                ["RH199 Rapid Track (v10.0)", "En curso · 10/154 pág · Cap. 2 ch02s03 Links (27 ago)"],
                ["RH104 Linux Fundamentals v9.1", "En curso · 43/56 · Cap. 4 (path RHCSA · 15 sep)"],
                ["RH024 Getting Started (video)", "COMPLETADO (8 sep)"],
                ["RH124 Sysadmin I", "OBTENIDO — ver certificado"],
                ["RH134 Sysadmin II", "OBTENIDO — ver certificado"],
                ["EX200 RHCSA / ruta EX294 RHCE", "Objetivo; requerido para RHCE"],
            ],
            [5200, 4160],
        )
    )
    parts.append(link_bullet("Ver certificado RH124", r124))
    parts.append(link_bullet("Ver certificado RH134", r134))

    parts.append(heading("Fases de estudio RHCSA 10 (finalización ~30 oct 2026)", 2))
    parts.append(
        simple_table(
            ["Fase", "Foco"],
            [
                ["Hecho", "Cap. 1-6: install, tools, files, SSH, users/groups"],
                ["Ahora", "Cap. 7: chmod OK; afianzar chown/ownership + ACL (pág 335 · 15 sep)"],
                ["Bloque B", "Red nmcli (Cap. 8) — SSH ya hecho"],
                ["Bloque C", "DNF + Flatpak + systemd/cron"],
                ["Crítico", "Storage LVM/fstab (+ NFS/autofs)"],
                ["Seguridad", "SELinux + firewall + boot"],
                ["Cierre", "Repaso / practice exams (EX200 RHEL 10)"],
            ],
            [2400, 6960],
        )
    )

    parts.append(heading("Plan de estudio", 2))
    parts.append(bullet("Continuar labs en Rocky 10 según las fases anteriores."))
    parts.append(bullet("RH199 Rapid Track en curso (10/154 pág · Cap. 2 ch02s03 Links · 27 ago); EX200 como objetivo."))
    parts.append(
        bullet("Hito actual: Cap. 7 pág 335 · chmod más sólido; pendiente chown/ownership + ACL · lab-permisos (11 sep).")
    )

    parts.append(spacer(120))
    parts.append(heading("Bibliografía y enlaces", 2))
    parts.append(para(run("Bibliografía", bold=True, size=22), before=80, after=60))
    parts.append(bullet("van Vugt, S. — Red Hat RHCSA 9 Cert Guide (Pearson; libro principal)"))
    parts.append(bullet("Red Hat — RH124 System Administration I"))
    parts.append(bullet("Red Hat — RH134 System Administration II"))
    parts.append(bullet("Red Hat — RH199 RHCSA Rapid Track (v10.0)"))

    parts.append(heading("Videos", 2))
    parts.append(para(run("Vistos", bold=True, size=22), before=80, after=60))
    parts.append(
        link_bullet(
            "How I Scored 300/300 on the RHCSA Exam – 8 Tips You Need to Know!",
            ryt1,
        )
    )
    parts.append(
        link_bullet(
            "Inside a Red Hat Certification Exam: What you need to know",
            ryt2,
        )
    )
    parts.append(
        para(run("Por ver (importante)", bold=True, size=22, color=AMBER), before=160, after=60)
    )
    parts.append(
        link_bullet(
            "[pendiente] 3 RHCSA Exam Tasks That Will RUIN Your Score!",
            ryt3,
        )
    )
    parts.append(
        link_bullet(
            "[pendiente] RHCSA 9/10 Exam Prep: Real EX200 Questions & Step-by-Step Solutions",
            ryt4,
        )
    )
    parts.append(
        link_bullet(
            "[pendiente] Playlist RHCSA exam prep series — NicoDemos",
            ryt5,
        )
    )

    parts.append(spacer(40))
    parts.append(heading("Enlaces (hipervínculos)", 2))
    parts.append(link_bullet("RH124 — certificado", r124))
    parts.append(link_bullet("RH134 — certificado", r134))
    parts.append(link_bullet("RH199 — Rapid Track v10.0 (ROL)", r199))
    parts.append(link_bullet("EX200 — examen RHCSA oficial", rex200))
    parts.append(link_bullet("EX294 — examen RHCE", rex294))

    parts.append(spacer(80))
    parts.append(
        para(
            run(
                f"Generado {REPORT_AS_OF.strftime('%d/%m/%Y')}  ·  Documento maestro editable  ·  Exportar a PDF desde Word",
                size=16,
                color=GRAY,
            )
        )
    )

    body = "\n".join(parts)
    doc = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="{NS_W}" xmlns:r="{NS_R}">
  <w:body>
{body}
    <w:sectPr>
      <w:pgSz w:w="12240" w:h="15840"/>
      <w:pgMar w:top="720" w:right="720" w:bottom="720" w:left="720"/>
    </w:sectPr>
  </w:body>
</w:document>"""
    return doc, rels


def build_docx(path: Path) -> None:
    document_xml, rels = build_document_xml()
    content_types = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
</Types>"""
    root_rels = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="{NS_REL}">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>"""
    rel_items = "\n".join(
        f'  <Relationship Id="{rid}" '
        f'Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink" '
        f'Target="{escape(url)}" TargetMode="External"/>'
        for rid, url in rels
    )
    doc_rels = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="{NS_REL}">
{rel_items}
</Relationships>"""
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", content_types)
        z.writestr("_rels/.rels", root_rels)
        z.writestr("word/document.xml", document_xml.encode("utf-8"))
        z.writestr("word/_rels/document.xml.rels", doc_rels.encode("utf-8"))


def main() -> None:
    build_docx(DOCX_OUT)
    print(f"OK DOCX maestro editable: {DOCX_OUT} ({DOCX_OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
