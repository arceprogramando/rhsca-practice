#!/usr/bin/env python3
"""PDF visual gerencial RHCSA - tono de estudio, sin pedir inscripción."""

from datetime import date
from pathlib import Path

PDF_OUT = Path("/home/felipe/Informe-Progreso-RHCSA-Felipe.pdf")
HTML_OUT = Path("/home/felipe/Informe-RHCSA-Gerencia.html")

# Calendario del plan: (fin - inicio) = total; elapsed + left = total
PLAN_START = date(2026, 8, 18)
PLAN_END = date(2026, 10, 30)
# Fecha del informe (la VM a veces tiene reloj desfasado; ajustar al día real)
REPORT_AS_OF = date(2026, 9, 15)
BOOK_PAGE = 335
BOOK_TOTAL = 1593
BOOK_USEFUL = 1135
RH104_PAGE = 43
RH104_TOTAL = 56
RH199_PAGE = 10
RH199_TOTAL = 154


def plan_metrics(today: date | None = None) -> dict:
    """Días del plan siempre suman: elapsed + left == total (73)."""
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
        "today": today,
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
        "rh104_page": RH104_PAGE,
        "rh104_total": RH104_TOTAL,
        "rh104_pct": round(100 * RH104_PAGE / RH104_TOTAL),
        "rh104_left": RH104_TOTAL - RH104_PAGE,
        "rh199_page": RH199_PAGE,
        "rh199_total": RH199_TOTAL,
        "rh199_pct": round(100 * RH199_PAGE / RH199_TOTAL),
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


def esc(s: str) -> str:
    return s.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def rect(x, y, w, h, r, g, b):
    return [f"{r:.3f} {g:.3f} {b:.3f} rg", f"{x:.1f} {y:.1f} {w:.1f} {h:.1f} re", "f"]


def txt(x, y, size, s, bold=False, color=(0.1, 0.12, 0.16)):
    font = "/F2" if bold else "/F1"
    r, g, b = color
    return [
        f"{r:.3f} {g:.3f} {b:.3f} rg",
        "BT",
        f"{font} {size} Tf",
        f"1 0 0 1 {x:.1f} {y:.1f} Tm",
        f"({esc(s)}) Tj",
        "ET",
    ]


# Anchos Helvetica (AFM / 1000) aprox. para centrado visual fiable
_HELV_W = {
    " ": 278, "!": 278, '"': 355, "#": 556, "$": 556, "%": 889, "&": 667, "'": 191,
    "(": 333, ")": 333, "*": 389, "+": 584, ",": 278, "-": 333, ".": 278, "/": 278,
    "0": 556, "1": 556, "2": 556, "3": 556, "4": 556, "5": 556, "6": 556, "7": 556,
    "8": 556, "9": 556, ":": 278, ";": 278, "<": 584, "=": 584, ">": 584, "?": 556,
    "@": 1015, "A": 667, "B": 667, "C": 722, "D": 722, "E": 667, "F": 611, "G": 778,
    "H": 722, "I": 278, "J": 500, "K": 667, "L": 556, "M": 833, "N": 722, "O": 778,
    "P": 667, "Q": 778, "R": 722, "S": 667, "T": 611, "U": 722, "V": 667, "W": 944,
    "X": 667, "Y": 667, "Z": 611, "[": 278, "\\": 278, "]": 278, "^": 469, "_": 556,
    "`": 333, "a": 556, "b": 556, "c": 500, "d": 556, "e": 556, "f": 278, "g": 556,
    "h": 556, "i": 222, "j": 222, "k": 500, "l": 222, "m": 833, "n": 556, "o": 556,
    "p": 556, "q": 556, "r": 333, "s": 500, "t": 278, "u": 556, "v": 500, "w": 722,
    "x": 500, "y": 500, "z": 500, "{": 334, "|": 260, "}": 334, "~": 584,
}


def text_width(s: str, size: float, bold: bool = False) -> float:
    scale = 1.0 if not bold else 1.04
    total = 0.0
    for ch in s:
        total += _HELV_W.get(ch, 556)
    return total * size * scale / 1000.0


def txt_centered(cx, y, size, s, bold=False, color=(0.1, 0.12, 0.16)):
    """Centra texto con anchos Helvetica (no factor fijo)."""
    w = text_width(s, size, bold)
    return txt(cx - w / 2, y, size, s, bold, color)


def stream(ops: list[str]) -> bytes:
    return "\n".join(ops).encode("latin-1", errors="replace")


def uri_annot(x1, y1, x2, y2, url: str) -> bytes:
    # Escape parentheses in URI for PDF string
    u = url.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")
    # NewWindow: hint para lectores (Acrobat/etc.) de abrir el URI sin reemplazar el PDF
    return (
        f"<< /Type /Annot /Subtype /Link "
        f"/Rect [{x1:.1f} {y1:.1f} {x2:.1f} {y2:.1f}] "
        f"/Border [0 0 0] "
        f"/A << /S /URI /URI ({u}) /NewWindow true >> >>"
    ).encode("latin-1")


# Fedora Red Hat (SVG paths) - rojo arriba, blanco abajo
PATH_HAT_RED = (
    "m 128,84 c 12.5,0 30.6,-2.6 30.6,-17.5 a 19.53,19.53 0 0 0 -0.3,-3.4 "
    "L 150.9,30.7 C 149.2,23.6 147.7,20.3 135.2,14.1 125.5,9.1 104.4,1 98.1,1 "
    "92.2,1 90.5,8.5 83.6,8.5 76.9,8.5 72,2.9 65.7,2.9 c -6,0 -9.9,4.1 -12.9,12.5 "
    "0,0 -8.4,23.7 -9.5,27.2 a 6.15,6.15 0 0 0 -0.2,1.9 C 43,53.7 79.3,83.9 128,84 "
    "m 32.5,-11.4 c 1.7,8.2 1.7,9.1 1.7,10.1 0,14 -15.7,21.8 -36.4,21.8 "
    "C 79,104.5 38.1,77.1 38.1,59 a 18.35,18.35 0 0 1 1.5,-7.3 "
    "C 22.8,52.5 1,55.5 1,74.7 1,106.2 75.6,145 134.6,145 c 45.3,0 56.7,-20.5 "
    "56.7,-36.7 0,-12.7 -11,-27.1 -30.8,-35.7"
)
PATH_HAT_WHITE = (
    "m 160.5,72.6 c 1.7,8.2 1.7,9.1 1.7,10.1 0,14 -15.7,21.8 -36.4,21.8 "
    "C 79,104.5 38.1,77.1 38.1,59 a 18.35,18.35 0 0 1 1.5,-7.3 l 3.7,-9.1 "
    "a 6.15,6.15 0 0 0 -0.2,1.9 c 0,9.2 36.3,39.4 84.9,39.4 12.5,0 30.6,-2.6 "
    "30.6,-17.5 A 19.53,19.53 0 0 0 158.3,63 Z"
)

_TOKEN = __import__("re").compile(
    r"([MmLlHhVvCcSsQqTtAaZz])|([+-]?(?:\d+\.?\d*|\.\d+)(?:[eE][+-]?\d+)?)"
)


def _tokenize_svg(d: str):
    for m in _TOKEN.finditer(d.replace(",", " ")):
        if m.group(1):
            yield ("cmd", m.group(1))
        else:
            yield ("num", float(m.group(2)))


def _arc_to_curves(x1, y1, rx, ry, phi, fa, fs, x2, y2):
    import math

    if rx == 0 or ry == 0:
        return [(x2, y2, x2, y2, x2, y2)]
    phi = math.radians(phi)
    cos_phi, sin_phi = math.cos(phi), math.sin(phi)
    dx, dy = (x1 - x2) / 2, (y1 - y2) / 2
    x1p = cos_phi * dx + sin_phi * dy
    y1p = -sin_phi * dx + cos_phi * dy
    rx, ry = abs(rx), abs(ry)
    lam = (x1p / rx) ** 2 + (y1p / ry) ** 2
    if lam > 1:
        s = math.sqrt(lam)
        rx, ry = rx * s, ry * s
    num = rx**2 * ry**2 - rx**2 * y1p**2 - ry**2 * x1p**2
    den = rx**2 * y1p**2 + ry**2 * x1p**2
    c = math.sqrt(max(0, num / den)) if den else 0
    if fa == fs:
        c = -c
    cxp = c * (rx * y1p / ry)
    cyp = c * (-ry * x1p / rx)
    cx = cos_phi * cxp - sin_phi * cyp + (x1 + x2) / 2
    cy = sin_phi * cxp + cos_phi * cyp + (y1 + y2) / 2

    def angle(u, v):
        ur = math.hypot(*u)
        vr = math.hypot(*v)
        if ur == 0 or vr == 0:
            return 0
        sign = 1 if u[0] * v[1] - u[1] * v[0] >= 0 else -1
        return sign * math.acos(max(-1, min(1, (u[0] * v[0] + u[1] * v[1]) / (ur * vr))))

    th1 = angle((1, 0), ((x1p - cxp) / rx, (y1p - cyp) / ry))
    dth = angle(
        ((x1p - cxp) / rx, (y1p - cyp) / ry),
        ((-x1p - cxp) / rx, (-y1p - cyp) / ry),
    )
    if not fs and dth > 0:
        dth -= 2 * math.pi
    if fs and dth < 0:
        dth += 2 * math.pi
    segments = max(1, int(math.ceil(abs(dth) / (math.pi / 2))))
    dth /= segments
    t = 4 / 3 * math.tan(dth / 4)
    out = []
    for i in range(segments):
        th = th1 + i * dth
        th2 = th + dth
        cos1, sin1 = math.cos(th), math.sin(th)
        cos2, sin2 = math.cos(th2), math.sin(th2)
        ep1 = (
            cx + rx * cos_phi * cos1 - ry * sin_phi * sin1,
            cy + rx * sin_phi * cos1 + ry * cos_phi * sin1,
        )
        ep2 = (
            cx + rx * cos_phi * cos2 - ry * sin_phi * sin2,
            cy + rx * sin_phi * cos2 + ry * cos_phi * sin2,
        )
        dx1 = -rx * cos_phi * sin1 - ry * sin_phi * cos1
        dy1 = -rx * sin_phi * sin1 + ry * cos_phi * cos1
        dx2 = -rx * cos_phi * sin2 - ry * sin_phi * cos2
        dy2 = -rx * sin_phi * sin2 + ry * cos_phi * cos2
        c1 = (ep1[0] + t * dx1, ep1[1] + t * dy1)
        c2 = (ep2[0] - t * dx2, ep2[1] - t * dy2)
        out.append((c1[0], c1[1], c2[0], c2[1], ep2[0], ep2[1]))
    return out


def svg_path_to_pdf_ops(d: str, ox: float, oy: float, scale: float, vb_h: float = 146.0):
    def tx(x, y):
        return ox + x * scale, oy + (vb_h - y) * scale

    ops = []
    nums = []
    cmd = None
    cx = cy = 0.0
    sx = sy = 0.0
    arity = {
        "M": 2, "m": 2, "L": 2, "l": 2, "H": 1, "h": 1, "V": 1, "v": 1,
        "C": 6, "c": 6, "S": 4, "s": 4, "Q": 4, "q": 4, "T": 2, "t": 2,
        "A": 7, "a": 7, "Z": 0, "z": 0,
    }
    for kind, val in _tokenize_svg(d):
        if kind == "cmd":
            if val in ("Z", "z"):
                ops.append("h")
                cx, cy = sx, sy
                cmd = None
                nums = []
                continue
            cmd = val
            nums = []
            continue
        nums.append(val)
        need = arity.get(cmd)
        if need is None or need == 0 or len(nums) < need:
            continue
        while len(nums) >= need:
            a = nums[:need]
            nums = nums[need:]
            if cmd == "M":
                cx, cy = a
                sx, sy = cx, cy
                x, y = tx(cx, cy)
                ops.append(f"{x:.2f} {y:.2f} m")
                cmd = "L"
            elif cmd == "m":
                cx += a[0]
                cy += a[1]
                sx, sy = cx, cy
                x, y = tx(cx, cy)
                ops.append(f"{x:.2f} {y:.2f} m")
                cmd = "l"
            elif cmd == "L":
                cx, cy = a
                x, y = tx(cx, cy)
                ops.append(f"{x:.2f} {y:.2f} l")
            elif cmd == "l":
                cx += a[0]
                cy += a[1]
                x, y = tx(cx, cy)
                ops.append(f"{x:.2f} {y:.2f} l")
            elif cmd == "C":
                x1, y1, x2, y2, x, y = a
                p1, p2, p3 = tx(x1, y1), tx(x2, y2), tx(x, y)
                cx, cy = x, y
                ops.append(
                    f"{p1[0]:.2f} {p1[1]:.2f} {p2[0]:.2f} {p2[1]:.2f} {p3[0]:.2f} {p3[1]:.2f} c"
                )
            elif cmd == "c":
                x1, y1 = cx + a[0], cy + a[1]
                x2, y2 = cx + a[2], cy + a[3]
                x, y = cx + a[4], cy + a[5]
                p1, p2, p3 = tx(x1, y1), tx(x2, y2), tx(x, y)
                cx, cy = x, y
                ops.append(
                    f"{p1[0]:.2f} {p1[1]:.2f} {p2[0]:.2f} {p2[1]:.2f} {p3[0]:.2f} {p3[1]:.2f} c"
                )
            elif cmd in ("A", "a"):
                rx, ry, phi, fa, fs, x, y = a
                if cmd == "a":
                    x, y = cx + x, cy + y
                for c1x, c1y, c2x, c2y, ex, ey in _arc_to_curves(
                    cx, cy, rx, ry, phi, int(fa), int(fs), x, y
                ):
                    p1, p2, p3 = tx(c1x, c1y), tx(c2x, c2y), tx(ex, ey)
                    ops.append(
                        f"{p1[0]:.2f} {p1[1]:.2f} {p2[0]:.2f} {p2[1]:.2f} {p3[0]:.2f} {p3[1]:.2f} c"
                    )
                cx, cy = x, y
    return ops


def draw_redhat_hat(ox: float, oy: float, scale: float = 0.38) -> list[str]:
    """Dibuja fedora Red Hat: cuerpo rojo + banda negra al medio (sobre placa blanca)."""
    ops: list[str] = []
    w = 192.3 * scale
    h = 146.0 * scale
    pad = 4
    # Placa blanca para que el rojo se vea sobre el header rojo
    ops += rect(ox - pad, oy - pad, w + 2 * pad, h + 2 * pad, 1, 1, 1)
    red_ops = svg_path_to_pdf_ops(PATH_HAT_RED, ox, oy, scale)
    band_ops = svg_path_to_pdf_ops(PATH_HAT_WHITE, ox, oy, scale)  # path de la banda
    ops += ["0.933 0 0 rg"]  # rojo
    ops += red_ops
    ops += ["f"]
    ops += ["0 0 0 rg"]  # banda negra
    ops += band_ops
    ops += ["f"]
    return ops



def load_hat_rgb(path: Path = Path("/home/felipe/redhat-hat.png")):
    """Decode PNG (RGB8/RGBA8) to (w, h, rgb_bytes), applying scanline filters."""
    import struct, zlib

    data = path.read_bytes()
    assert data[:8] == b"\x89PNG\r\n\x1a\n"
    i = 8
    w = h = ct = None
    idats: list[bytes] = []
    while i < len(data):
        ln = struct.unpack(">I", data[i : i + 4])[0]
        typ = data[i + 4 : i + 8]
        chunk = data[i + 8 : i + 8 + ln]
        i = i + 12 + ln
        if typ == b"IHDR":
            w, h, bit, ct, comp, filt, inter = struct.unpack(">IIBBBBB", chunk)
            assert bit == 8 and inter == 0 and comp == 0 and filt == 0
        elif typ == b"IDAT":
            idats.append(chunk)
        elif typ == b"IEND":
            break
    assert w and h and ct in (2, 6)
    bpp = 3 if ct == 2 else 4
    stride = w * bpp
    raw = zlib.decompress(b"".join(idats))

    def paeth(a: int, b: int, c: int) -> int:
        p = a + b - c
        pa, pb, pc = abs(p - a), abs(p - b), abs(p - c)
        if pa <= pb and pa <= pc:
            return a
        if pb <= pc:
            return b
        return c

    prev = bytearray(stride)
    out = bytearray()
    pos = 0
    for _ in range(h):
        ft = raw[pos]
        pos += 1
        row = bytearray(raw[pos : pos + stride])
        pos += stride
        if ft == 1:  # Sub
            for x in range(bpp, stride):
                row[x] = (row[x] + row[x - bpp]) & 255
        elif ft == 2:  # Up
            for x in range(stride):
                row[x] = (row[x] + prev[x]) & 255
        elif ft == 3:  # Average
            for x in range(stride):
                left = row[x - bpp] if x >= bpp else 0
                row[x] = (row[x] + ((left + prev[x]) // 2)) & 255
        elif ft == 4:  # Paeth
            for x in range(stride):
                left = row[x - bpp] if x >= bpp else 0
                up = prev[x]
                ul = prev[x - bpp] if x >= bpp else 0
                row[x] = (row[x] + paeth(left, up, ul)) & 255
        elif ft != 0:
            raise ValueError(f"PNG filter no soportado: {ft}")
        prev = row
        if ct == 6:
            for x in range(w):
                r, g, b, a = row[x * 4 : (x + 1) * 4]
                af = a / 255.0
                out += bytes(
                    [
                        int(r * af + 255 * (1 - af)),
                        int(g * af + 255 * (1 - af)),
                        int(b * af + 255 * (1 - af)),
                    ]
                )
        else:
            out += row
    # Fondo blanco del PNG → negro (header), para que el gorrito rojo destaque
    bg = (0x15, 0x15, 0x15)
    rgb = bytearray(out)
    for i in range(0, len(rgb), 3):
        if rgb[i] > 240 and rgb[i + 1] > 240 and rgb[i + 2] > 240:
            rgb[i], rgb[i + 1], rgb[i + 2] = bg
    return w, h, bytes(rgb)


def encode_png_rgb(w: int, h: int, rgb: bytes) -> bytes:
    """PNG RGB8 mínimo (sin dependencia externa)."""
    import struct, zlib

    def chunk(tag: bytes, data: bytes) -> bytes:
        return (
            struct.pack(">I", len(data))
            + tag
            + data
            + struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF)
        )

    raw = bytearray()
    stride = w * 3
    for y in range(h):
        raw.append(0)
        raw += rgb[y * stride : (y + 1) * stride]
    return (
        b"\x89PNG\r\n\x1a\n"
        + chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 2, 0, 0, 0))
        + chunk(b"IDAT", zlib.compress(bytes(raw), 9))
        + chunk(b"IEND", b"")
    )


def pdf_draw_image(name: str, x: float, y: float, w: float, h: float) -> list[str]:
    """Place XObject image; y is bottom of image in PDF coords."""
    return [
        "q",
        f"{w:.2f} 0 0 {h:.2f} {x:.2f} {y:.2f} cm",
        f"/{name} Do",
        "Q",
    ]


def build_pdf() -> bytes:
    m = plan_metrics()
    # Red Hat Brand Standards: red-50 #ee0000, gray-95 #151515
    NAVY = (0.082, 0.082, 0.082)      # gray-95 / black header
    ACCENT = (0.933, 0.0, 0.0)        # red-50 #ee0000
    GREEN = (0.388, 0.600, 0.239)     # success-green-50 #63993d
    AMBER = (0.961, 0.573, 0.106)     # orange-40 #f5921b
    RED = (0.933, 0.0, 0.0)           # red-50 (priority)
    LIGHT = (0.949, 0.949, 0.949)     # gray-10 #f2f2f2
    WHITE = (1, 1, 1)
    DARK = (0.082, 0.082, 0.082)
    MUTED = (0.702, 0.702, 0.702)     # gray-40-ish
    GRAY = (0.439, 0.439, 0.439)      # gray-50
    LINK = (0.0, 0.4, 0.8)            # interaction-blue-50
    CHART = (0.0, 0.4, 0.8)           # charts (no red=peligro)
    BAR = (0.878, 0.878, 0.878)       # gray-20

    pages_content: list[bytes] = []

    # PAGE 1 - solo header negro; cuerpo blanco
    o = []
    o += rect(0, 0, 612, 792, *WHITE)
    o += rect(0, 668, 612, 124, *NAVY)  # header con candidato
    o += txt(40, 760, 18, "Informe de Progreso", True, WHITE)
    o += txt(40, 732, 13, "Certificacion RHCSA (EX200)", True, WHITE)
    o += txt(40, 706, 11, "Candidato: Felipe Antonio Aleman Arce", False, WHITE)
    o += pdf_draw_image("ImHat", 518, 710, 72, 48)

    o += txt(40, 642, 11, "Aproximado Finalizacion Practica: 30 de octubre de 2026", False, GRAY)
    o += txt(
        40,
        624,
        11,
        "Examen objetivo: RHCSA (EX200) - Requerido para Ruta RHCE (EX294)",
        False,
        GRAY,
    )

    # KPIs mas arriba (aprovechar espacio libre bajo el header)
    for x, val, label, col in [
        (60, str(m["elapsed"]), ("Dias desde el", "comienzo del plan"), GREEN),
        (230, str(m["left"]), ("Dias a finalizar la", "Practica pre-examen"), AMBER),
        (400, "2/3", "Cursos base", GREEN),
    ]:
        o += rect(x, 505, 140, 82, *LIGHT)
        o += rect(x, 579, 140, 8, *col)
        cx = x + 70
        o += txt_centered(cx, 552, 20, val, True, col)
        if isinstance(label, tuple):
            # dos lineas centradas, dentro de la card
            o += txt_centered(cx, 528, 7, label[0], False, DARK)
            o += txt_centered(cx, 514, 7, label[1], False, DARK)
        else:
            o += txt_centered(cx, 520, 9, label, False, DARK)

    # Pipeline (1 fila, cajas chicas para que entren 8)
    o += txt(40, 488, 13, "Pipeline de estudio", True, DARK)
    steps = [
        ("RH024", ("Video", "OK"), GREEN),
        ("RH104", ("33", "/56"), AMBER),
        ("RH124", ("Hecho", ""), GREEN),
        ("RH134", ("Hecho", ""), GREEN),
        ("Libro", ("335", "/1593"), CHART),
        ("RH199", ("10", "/154"), AMBER),
        ("EX200", ("Obj.", ""), AMBER),
        ("EX294", ("Ruta", ""), CHART),
    ]
    box_w, gap, y_box = 64, 6, 442
    x0 = 28
    for i, (label, sub, col) in enumerate(steps):
        x = x0 + i * (box_w + gap)
        o += rect(x, y_box, box_w, 30, *col)
        o += txt_centered(x + box_w / 2, y_box + 12, 8, label, True, WHITE)
        cx = x + box_w / 2
        if isinstance(sub, tuple):
            o += txt_centered(cx, y_box - 12, 6, sub[0], False, GRAY)
            if sub[1]:
                o += txt_centered(cx, y_box - 22, 6, sub[1], False, GRAY)
        else:
            o += txt_centered(cx, y_box - 14, 6, sub, False, GRAY)

    # Resumen
    o += txt(40, 395, 13, "Resumen", True, DARK)
    for i, b in enumerate(
        [
            "RH024 terminado; RH104 Fundamentals v9.1 en curso (43/56 · Cap. 4 · 15 sep).",
            "RH124 y RH134 acreditados (completados previamente).",
            "Examen objetivo: RHCSA (EX200) - requerido para ruta RHCE (EX294).",
            "Libro Cap. 7 Permissions (pag 335) + lab-permisos + RH199/RH104.",
            "Fortaleza: chmod/modos; falta afianzar chown. Luego ACL, nmcli, systemd.",
            "Mas adelante: storage/LVM, SELinux, firewall y boot.",
        ]
    ):
        o += txt(48, 378 - i * 11, 9, "- " + b, False, GRAY)

    # Card Perfil
    o += rect(32, 55, 548, 240, *LIGHT)
    o += rect(32, 55, 6, 240, *CHART)
    o += txt(50, 277, 10, "Perfil y contexto", True, DARK)
    o += txt(
        50,
        261,
        8,
        "Me desenvuelvo como desarrollador FullStack. Al no haber trabajado antes en el area de sysadmin,",
        False,
        DARK,
    )
    o += txt(
        50,
        247,
        8,
        "algunos conceptos me son nuevos y otros ya los uso de alguna forma en el dia a dia.",
        False,
        DARK,
    )
    o += txt(50, 229, 9, "Disponibilidad", True, DARK)
    o += txt(
        50,
        213,
        8,
        "- 2 hs de estudio por dia en el trabajo + dias/horarios disponibles fuera de eso",
        False,
        DARK,
    )
    o += txt(
        50,
        199,
        8,
        "- Extra: martes, jueves y sabado 20 a 22 hs",
        False,
        DARK,
    )
    o += txt(
        50,
        185,
        8,
        "- domingo todo el dia",
        False,
        DARK,
    )
    o += txt(50, 167, 9, "Dias ocupados", True, DARK)
    o += txt(
        50,
        151,
        8,
        "- Lunes y miercoles: 19 a 22 hs ingles CUI",
        False,
        DARK,
    )
    o += txt(
        50,
        137,
        8,
        "- Sabados: universidad 8 a 15 hs (+ 1 hs de viaje a la un)",
        False,
        DARK,
    )
    o += txt(50, 119, 9, "Otras Obligaciones", True, DARK)
    o += txt(
        50,
        103,
        8,
        "- Rendir Matematica Universidad 14 de septiembre",
        False,
        DARK,
    )
    pages_content.append(stream(o))

    # PAGE 2
    o = []
    o += rect(0, 0, 612, 792, *WHITE)
    o += rect(0, 728, 612, 64, *NAVY)
    o += txt(40, 756, 14, "Avance cuantitativo y ritmo de estudio", True, WHITE)
    o += pdf_draw_image("ImHat", 538, 742, 44, 30)
    o += txt(
        40,
        710,
        11,
        f"Plazo total del plan: {m['total']} dias (18 ago -> 30 oct)  |  quedan {m['left']} dias",
        True,
        DARK,
    )
    o += rect(40, 685, 520, 16, *BAR)
    o += rect(40, 685, 520 * m["elapsed"] / m["total"], 16, *CHART)
    o += txt(
        40,
        668,
        9,
        f"Transcurridos {m['elapsed']} / {m['total']} (~{m['pct_cal']}%)  |  quedan {m['left']} dias  |  18 ago -> 30 oct",
        False,
        GRAY,
    )

    # Libro + notas debajo
    o += txt(40, 644, 11, "Avance del libro Red Hat RHCSA 9 Cert Guide - Sander van Vugt", True, DARK)
    o += rect(40, 622, 520, 14, *BAR)
    o += rect(40, 622, 520 * m["book_page"] / m["book_total"], 14, *CHART)
    o += txt(40, 608, 8, f"{m['book_page']} / {m['book_total']} (~{m['book_pct']}%)  |  Cap. 7 Permissions Management", False, GRAY)
    o += txt(
        40,
        594,
        8,
        f"Libro (PDF {m['book_total']}): faltan {m['book_left']} | 15/dia -> ~nov | meta 30 oct ({m['left']} d) -> ~{m['need_pdf']}/dia",
        True,
        RED,
    )
    o += txt(
        40,
        582,
        8,
        f"Libro (contenido util ~{BOOK_USEFUL}): faltan ~{m['useful_left']} | 15/dia -> ~fin oct | meta 30 oct -> ~{m['need_useful']}/dia",
        True,
        CHART,
    )
    o += txt(
        40,
        570,
        8,
        f"Promedio hasta hoy: ~{m['avg']} pag/dia ({m['book_page']} en {m['elapsed']} d) | para meta: subir a ~{m['need_pdf']} PDF o ~{m['need_useful']} util",
        True,
        GREEN,
    )

    # RH104 (entre libro y RH199)
    o += txt(40, 548, 11, "Avance RH104 Getting Started with Linux Fundamentals (v9.1) - ROL", True, DARK)
    o += rect(40, 526, 520, 14, *BAR)
    o += rect(40, 526, max(4, 520 * m["rh104_page"] / m["rh104_total"]), 14, *AMBER)
    o += txt(
        40,
        512,
        8,
        f"{m['rh104_page']} / {m['rh104_total']} (~{m['rh104_pct']}%)  |  Cap. 4 ch04  |  15 sep 2026",
        False,
        GRAY,
    )
    o += txt(
        40,
        498,
        8,
        f"RH104: labs en GUI GNOME via VNC (no solo CLI); faltan {m['rh104_left']} unidades.",
        True,
        GREEN,
    )

    # RH199 + nota debajo
    o += txt(40, 476, 11, "Avance RH199 Rapid Track (v10.0) - ROL", True, DARK)
    o += rect(40, 454, 520, 14, *BAR)
    o += rect(40, 454, max(4, 520 * m["rh199_page"] / m["rh199_total"]), 14, *AMBER)
    o += txt(40, 440, 8, f"{m['rh199_page']} / {m['rh199_total']} (~{m['rh199_pct']}%)  |  Cap. 2 ch02s03 Links  |  27 ago 2026", False, GRAY)
    o += txt(
        40,
        426,
        8,
        f"RH199: Cap. 2 ch02s03 Links / enlaces simbolicos ({m['rh199_page']}/{m['rh199_total']}).",
        True,
        GREEN,
    )

    o += txt(40, 406, 10, "Prioridad de estudio (importancia + comodidad; 1 menor - 10 mayor)", True, DARK)
    o += txt(
        40,
        394,
        8,
        "Combina importancia para el examen y comodidad actual (1 = menor necesidad, 10 = mayor).",
        False,
        GRAY,
    )
    prios = [
        ("Reset root / rd.break", 10, RED),
        ("Persistencia al reboot", 10, RED),
        ("Storage + LVM + fstab", 10, RED),
        ("SELinux", 10, RED),
        ("Red + firewall (nmcli/nmtui)", 9, AMBER),
        ("Boot / troubleshoot", 9, AMBER),
        ("systemd + cron", 7, CHART),
        ("DNF + Flatpak", 5, GREEN),
        ("Users / grupos", 4, GREEN),
        ("Permisos + ACL", 3, GREEN),  # chmod OK (11 sep); afianzar chown/ACL
        ("SSH", 3, GREEN),
        ("Hard/soft links", 3, GREEN),
        ("Comprimir/extraer (tar)", 2, GREEN),
        ("Shell / archivos", 1, GREEN),
    ]
    y = 380
    for name, score, col in prios:
        o += txt(40, y, 7, name, False, DARK)
        o += rect(200, y - 1, 300, 6, *BAR)
        o += rect(200, y - 1, 30 * score, 6, *col)
        o += txt(510, y, 7, str(score), False, DARK)
        y -= 9

    # Ritmos uno debajo del otro (centrados en el ancho util 520)
    CONTENT_L, CONTENT_W = 40, 520
    BAR_W, STEP = 26, 52
    o += txt_centered(306, 240, 10, "Ritmo libro Van Vugt (335 / 1593)", True, DARK)
    o += txt_centered(306, 228, 8, "Pags acumuladas del PDF del libro", False, GRAY)
    libro_pts = [
        ("18 ago", 80),
        ("1 sep", 298),
        ("2 sep", 309),
        ("3 sep", 321),
        ("4 sep", 335),
    ]
    chart_w = (len(libro_pts) - 1) * STEP + BAR_W
    chart_x0 = CONTENT_L + (CONTENT_W - chart_w) / 2
    baseline_y = 180
    o += rect(chart_x0, baseline_y, chart_w, 1, *BAR)
    for i, (label, val) in enumerate(libro_pts):
        x = chart_x0 + i * STEP
        cx = x + BAR_W / 2
        h = 32 * val / 335
        col = GREEN if i == len(libro_pts) - 1 else CHART
        o += rect(x, baseline_y, BAR_W, h, *col)
        o += txt_centered(cx, 168, 7, label, False, GRAY)
        o += txt_centered(cx, baseline_y + h + 4, 7, str(val), False, DARK)

    o += txt_centered(306, 140, 10, "Ritmo RH199 Rapid Track (10 / 154)", True, DARK)
    o += txt_centered(306, 128, 8, "Pags acumuladas del curso en ROL  |  Cap. 2 ch02s03 Links", False, GRAY)
    rh199_h = max(8, 28 * 10 / 20)
    rh199_x = CONTENT_L + (CONTENT_W - BAR_W) / 2
    rh199_cx = rh199_x + BAR_W / 2
    o += rect(rh199_x, 90, BAR_W, rh199_h, *AMBER)
    o += txt_centered(rh199_cx, 78, 7, "27 ago", False, GRAY)
    o += txt_centered(rh199_cx, 90 + rh199_h + 6, 8, "10", False, DARK)
    pages_content.append(stream(o))

    # PAGE 3 - Problematicas (pagina dedicada)
    o = []
    o += rect(0, 0, 612, 792, *WHITE)
    o += rect(0, 728, 612, 64, *NAVY)
    o += txt(40, 756, 14, "Problematicas encontradas", True, WHITE)
    o += pdf_draw_image("ImHat", 538, 742, 44, 30)

    # --- 8 sep 2026 (path / cursos ROL) ---
    o += rect(32, 600, 548, 110, *LIGHT)
    o += rect(32, 600, 6, 110, *AMBER)
    o += txt(50, 692, 10, "8 sep 2026", True, AMBER)
    o += txt(
        50,
        676,
        9,
        "Encontre el path correcto para anotarme a rendir el RHCSA en ROL.",
        False,
        DARK,
    )
    o += txt(
        50,
        662,
        9,
        "Ademas de RH124 y RH134, el plan exige cursos previos de fundamentals:",
        False,
        DARK,
    )
    for i, b in enumerate(
        [
            "RH024 (video Getting Started) - COMPLETADO.",
            "RH104 Fundamentals v9.1 EN CURSO (43/56 · Cap. 4 ch04); practica en GNOME via VNC.",
            "Impacto: suma carga al plan (libro + RH199 + RH104) hasta el EX200.",
        ]
    ):
        o += txt(50, 646 - i * 13, 9, "- " + b, False, GRAY)

    # --- 31 ago 2026 (lab SSH / VMs) ---
    o += rect(32, 428, 548, 152, *LIGHT)
    o += rect(32, 428, 6, 152, *AMBER)
    o += txt(50, 562, 10, "31 ago 2026", True, AMBER)
    o += txt(
        50,
        546,
        9,
        "Para practicar Cap. 5 (SSH) de forma realista, monte 2 VMs Rocky en VirtualBox (server + client).",
        False,
        DARK,
    )
    o += txt(
        50,
        532,
        9,
        "Consumio gran parte de las horas de estudio del dia (infraestructura vs paginas del libro).",
        False,
        DARK,
    )
    prob_bullets = [
        "Clon inicial: hostname, Machine ID y MAC duplicados; puertos SSH 2200/2222 mezclados.",
        "Segundo disco LVM duplicado bloqueo boot en Server1-nuevo (fix: desmontar disco extra).",
        "Red host-only: IP por DHCP (192.168.56.102) vs plan estatico (.10 / .11).",
        "nmcli: nombre exacto del perfil (Conexion cableada 1, acento y minusculas).",
        "Resuelto: lab 2 VMs (servera .10 + workstation .11); SSH, scp, sftp y claves (Ex 5-5).",
        "Nota examen: VirtualBox/clonado no entra; si puede pedirse IP estatica con nmcli.",
    ]
    y_prob = 514
    for b in prob_bullets:
        o += txt(50, y_prob, 9, "- " + b, False, GRAY)
        y_prob -= 14
    pages_content.append(stream(o))

    # PAGE 4 - Plan de estudio y referencias
    o = []
    o += rect(0, 0, 612, 792, *WHITE)
    o += rect(0, 728, 612, 64, *NAVY)
    o += txt(40, 756, 14, "Plan de estudio y referencias", True, WHITE)
    o += pdf_draw_image("ImHat", 538, 742, 44, 30)
    o += txt(40, 710, 12, "Credenciales y horizonte (orden de plan)", True, DARK)
    y = 680
    cred_annots: list[bytes] = []
    for title, status, col, url in [
        ("1. RH199 Rapid Track (v10.0)", "En curso - 10/154 pag · Cap. 2 ch02s03 Links (27 ago)", CHART, URL_RH199),
        ("2. RH104 Linux Fundamentals v9.1", "En curso - 43/56 · Cap. 4 (path RHCSA; 15 sep)", AMBER, None),
        ("3. RH024 Getting Started (video)", "COMPLETADO (8 sep)", GREEN, None),
        ("4. RH124 Sysadmin I", "OBTENIDO - ver certificado", GREEN, URL_RH124),
        ("5. RH134 Sysadmin II", "OBTENIDO - ver certificado", GREEN, URL_RH134),
        ("6. EX200 RHCSA / ruta EX294 RHCE", "Objetivo; requerido para RHCE", AMBER, None),
    ]:
        o += rect(40, y - 6, 8, 28, *col)
        o += txt(56, y + 8, 10, title, True, LINK if url else DARK)
        o += txt(56, y - 6, 8, status, False, LINK if url else GRAY)
        if url:
            cred_annots.append(uri_annot(56, y - 12, 430, y + 22, url))
        y -= 36

    o += txt(40, 445, 12, "Fases de estudio RHCSA 10 (finalizacion ~30 oct 2026)", True, DARK)
    y = 420
    for name, focus, col in [
        ("Hecho", "Cap. 1-6: install, tools, files, SSH, users/groups", GREEN),
        ("Ahora", "Cap. 7: chmod OK; afianzar chown/ownership + ACL (pag 335 · 15 sep)", CHART),
        ("Bloque B", "Red nmcli (Cap. 8) - SSH ya hecho", AMBER),
        ("Bloque C", "DNF + Flatpak + systemd/cron", AMBER),
        ("Critico", "Storage LVM/fstab (+ NFS/autofs)", AMBER),
        ("Seguridad", "SELinux + firewall + boot", AMBER),
        ("Cierre", "Repaso / practice exams (EX200 RHEL 10)", GREEN),
    ]:
        o += rect(40, y, 100, 18, *col)
        o += txt(48, y + 5, 8, name, True, WHITE)
        o += txt(150, y + 5, 8, focus, False, DARK)
        y -= 22
    pages_content.append(stream(o))

    # PAGE 5 - Bibliografia, videos, enlaces y pie
    o = []
    o += rect(0, 0, 612, 792, *WHITE)
    o += rect(0, 728, 612, 64, *NAVY)
    o += txt(40, 756, 14, "Bibliografia y enlaces", True, WHITE)
    o += pdf_draw_image("ImHat", 538, 742, 44, 30)

    o += txt(40, 710, 11, "Bibliografia", True, DARK)
    biblio_y = 692
    for line in [
        "van Vugt, S. - Red Hat RHCSA 9 Cert Guide (Pearson; libro principal de estudio)",
        "Red Hat - RH024 Getting Started (video; completado 8 sep)",
        "Red Hat - RH104 Getting Started with Linux Fundamentals v9.1 (43/56 · Cap. 4 en curso)",
        "Red Hat - RH124 System Administration I",
        "Red Hat - RH134 System Administration II",
        "Red Hat - RH199 RHCSA Rapid Track (v10.0)",
    ]:
        o += txt(48, biblio_y, 8, "- " + line, False, DARK)
        biblio_y -= 14

    o += txt(40, biblio_y - 10, 11, "Videos", True, DARK)
    video_y = biblio_y - 28
    o += txt(48, video_y, 8, "Vistos:", True, DARK)
    video_y -= 14
    video_annots: list[bytes] = []
    for label, url in [
        ("How I Scored 290/290 on RHCSA - 8 Tips (YouTube)", URL_YT_TIPS),
        ("Inside a Red Hat Certification Exam (YouTube)", URL_YT_INSIDE),
    ]:
        o += txt(48, video_y, 8, "- " + label, False, LINK)
        video_annots.append(uri_annot(48, video_y - 4, 540, video_y + 12, url))
        video_y -= 14

    video_y -= 4
    o += txt(40, video_y, 10, "Por ver (importante)", True, AMBER)
    video_y -= 14
    for label, url in [
        ("3 RHCSA Exam Tasks That Will RUIN Your Score! (YouTube)", URL_YT_RUIN),
        ("RHCSA 9/10 Exam Prep: Real EX200 Questions & Solutions (YouTube)", URL_YT_PREP),
        ("Playlist RHCSA exam prep series - NicoDemos (YouTube)", URL_YT_NICODEMOS),
    ]:
        o += txt(48, video_y, 8, "- [pendiente] " + label, False, LINK)
        video_annots.append(uri_annot(48, video_y - 4, 540, video_y + 12, url))
        video_y -= 14

    # Enlaces con margen inferior generoso
    link_y = video_y - 16
    o += txt(40, link_y, 10, "Enlaces (hipervinculos)", True, DARK)
    link_items = [
        ("RH124 - badge Credly", URL_RH124),
        ("RH134 - badge Credly", URL_RH134),
        ("RH199 - Rapid Track v10.0 (ROL)", URL_RH199),
        ("EX200 - examen RHCSA oficial", URL_EX200),
        ("EX294 - examen RHCE (ruta posterior)", URL_EX294),
    ]
    link_annots: list[bytes] = []
    ly = link_y - 20
    for label, url in link_items:
        o += txt(40, ly, 8, label, False, LINK)
        link_annots.append(uri_annot(40, ly - 4, 400, ly + 12, url))
        ly -= 16
    o += txt(40, 48, 8, f"Generado {REPORT_AS_OF.strftime('%d/%m/%Y')}  |  Seguimiento preparacion RHCSA (plan de estudio)", False, GRAY)
    pages_content.append(stream(o))

    # Link hit-boxes: credenciales (pag 4) + videos + enlaces (pag 5)
    annots_p4 = cred_annots
    annots_p5 = video_annots + link_annots

    import zlib

    hat_w, hat_h, hat_rgb = load_hat_rgb()
    hat_z = zlib.compress(hat_rgb, 9)

    # 1 cat, 2 pages (x5), 3-7 page, 8-12 content, 13 image, 14-15 fonts, 16+ annots
    res = (
        b"/Resources << /Font << /F1 14 0 R /F2 15 0 R >> "
        b"/XObject << /ImHat 13 0 R >> >>"
    )
    objs: list[bytes] = []
    objs.append(b"<< /Type /Catalog /Pages 2 0 R >>")
    objs.append(b"<< /Type /Pages /Kids [3 0 R 4 0 R 5 0 R 6 0 R 7 0 R] /Count 5 >>")
    page_content_ids = [8, 9, 10, 11, 12]
    all_annots = annots_p4 + annots_p5
    annot_splits = [[], [], [], annots_p4, annots_p5]
    annot_start = 16
    for content_i, page_annots in zip(page_content_ids, annot_splits):
        if page_annots:
            n = len(page_annots)
            annot_refs = b" ".join(
                f"{annot_start + i} 0 R".encode("ascii") for i in range(n)
            )
            annot_start += n
            objs.append(
                f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Contents {content_i} 0 R ".encode(
                    "ascii"
                )
                + res
                + b" /Annots ["
                + annot_refs
                + b"] >>"
            )
        else:
            objs.append(
                f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Contents {content_i} 0 R ".encode(
                    "ascii"
                )
                + res
                + b" >>"
            )
    for s in pages_content:
        objs.append(b"<< /Length %d >>\nstream\n" % len(s) + s + b"\nendstream")
    objs.append(
        (
            f"<< /Type /XObject /Subtype /Image /Width {hat_w} /Height {hat_h} "
            f"/ColorSpace /DeviceRGB /BitsPerComponent 8 /Filter /FlateDecode "
            f"/Length {len(hat_z)} >>\nstream\n"
        ).encode("ascii")
        + hat_z
        + b"\nendstream"
    )
    objs.append(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>")
    objs.append(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold >>")
    objs.extend(all_annots)

    out = bytearray(b"%PDF-1.4\n")
    offs = [0]
    for i, obj in enumerate(objs, 1):
        offs.append(len(out))
        out.extend(f"{i} 0 obj\n".encode())
        out.extend(obj)
        out.extend(b"\nendobj\n")
    xref = len(out)
    out.extend(f"xref\n0 {len(objs)+1}\n".encode())
    out.extend(b"0000000000 65535 f \n")
    for off in offs[1:]:
        out.extend(f"{off:010d} 00000 n \n".encode())
    out.extend(
        f"trailer\n<< /Size {len(objs)+1} /Root 1 0 R >>\nstartxref\n{xref}\n%%EOF\n".encode()
    )
    return bytes(out)


def build_html() -> str:
    import base64

    m = plan_metrics()
    hat_w, hat_h, hat_rgb = load_hat_rgb()
    hat_png = encode_png_rgb(hat_w, hat_h, hat_rgb)
    hat_b64 = base64.b64encode(hat_png).decode("ascii")
    hat_src = f"data:image/png;base64,{hat_b64}"
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8"/>
<title>Informe RHCSA - Gerencia Técnica</title>
<style>
  :root {{
    --navy: #151515;
    --accent: #ee0000;
    --green: #63993d;
    --amber: #f5921b;
    --red: #ee0000;
    --bg: #f2f2f2;
    --card: #ffffff;
    --text: #1a1f2c;
    --muted: #5c6578;
  }}
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0;
    font-family: "Segoe UI", system-ui, sans-serif;
    color: var(--text);
    background: var(--bg);
    line-height: 1.45;
  }}
  .page {{ max-width: 1040px; margin: 0 auto; padding: 32px 28px 48px; }}
  .hero {{
    background: #151515; color: #fff; border-radius: 12px; padding: 36px 32px 32px;
    margin-bottom: 24px; display: flex; justify-content: space-between; align-items: center; gap: 20px;
    min-height: 140px;
  }}
  .hero-text {{ flex: 1; min-width: 0; display: flex; flex-direction: column; justify-content: center; }}
  .hero-logo {{ flex-shrink: 0; line-height: 0; display: flex; align-items: center; }}
  .hero .eyebrow {{
    font-size: 12px; letter-spacing: 0.12em; text-transform: uppercase;
    opacity: 0.95; margin-bottom: 14px;
  }}
  .hero h1 {{ margin: 0 0 12px; font-size: 28px; font-weight: 700; color: #fff; }}
  .hero p {{ margin: 5px 0; opacity: 0.95; font-size: 14px; color: #fff; }}
  .kpis {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; margin-bottom: 24px; }}
  .kpi {{
    background: var(--card); border-radius: 10px; padding: 16px;
    border-top: 4px solid var(--navy); box-shadow: 0 1px 2px rgba(0,0,0,.06);
    text-align: center;
  }}
  .kpi.g {{ border-top-color: var(--green); }}
  .kpi.a {{ border-top-color: var(--amber); }}
  .kpi .v {{ font-size: 28px; font-weight: 700; }}
  .kpi .l {{ font-size: 12px; color: var(--muted); margin-top: 4px; line-height: 1.3; }}
  .kpi.a .l {{
    max-width: 11em;
    margin-left: auto;
    margin-right: auto;
    font-size: 11px;
    line-height: 1.25;
  }}
  .card {{
    background: var(--card); border-radius: 10px; padding: 20px 22px;
    margin-bottom: 16px; box-shadow: 0 1px 2px rgba(0,0,0,.06);
  }}
  h2 {{ margin: 0 0 12px; font-size: 18px; color: var(--navy); }}
  h3 {{ margin: 16px 0 8px; font-size: 14px; color: var(--navy); }}
  ul {{ margin: 0; padding-left: 18px; }}
  li {{ margin: 6px 0; font-size: 14px; }}
  .pipeline {{ display: flex; gap: 6px; flex-wrap: nowrap; margin-top: 12px; overflow-x: auto; }}
  .pip {{
    flex: 1 1 0; min-width: 0; text-align: center; padding: 8px 4px;
    border-radius: 6px; color: #fff; font-weight: 700; font-size: 12px;
  }}
  .pip span {{ display: block; font-size: 10px; font-weight: 500; opacity: .95; margin-top: 4px; line-height: 1.2; }}
  .done {{ background: var(--green); }}
  .plan {{ background: #0066cc; }}
  .goal {{ background: var(--amber); }}
  .bar-wrap {{ margin: 10px 0 16px; }}
  .bar-label {{ display: flex; justify-content: space-between; font-size: 12px; color: var(--muted); margin-bottom: 4px; }}
  .bar {{ height: 14px; background: #e6eaef; border-radius: 7px; overflow: hidden; }}
  .bar > i {{ display: block; height: 100%; border-radius: 7px; }}
  .prio {{ display: grid; gap: 10px; }}
  .prio-row {{ display: grid; grid-template-columns: 180px 1fr 28px; align-items: center; gap: 8px; font-size: 13px; }}
  .prio-row .track {{ height: 9px; background: #e6eaef; border-radius: 5px; overflow: hidden; }}
  .prio-row .track > i {{ display: block; height: 100%; }}
  .chart-block {{ text-align: center; margin-top: 20px; }}
  .chart-block h3 {{ margin: 0 0 8px; }}
  .chart-block p {{ margin: 0 0 12px; }}
  .chart-block svg {{ display: block; margin: 0 auto; max-width: 100%; }}
  table {{ width: 100%; border-collapse: collapse; font-size: 13px; }}
  th, td {{ text-align: left; padding: 10px 8px; border-bottom: 1px solid #e6eaef; }}
  th {{ color: var(--muted); font-weight: 600; font-size: 11px; text-transform: uppercase; }}
  .tag {{ display: inline-block; padding: 2px 8px; border-radius: 999px; font-size: 11px; font-weight: 600; }}
  .tag.ok {{ background: #e5f6ec; color: var(--green); }}
  .tag.plan {{ background: #e5f2fa; color: #0066cc; }}
  .tag.warn {{ background: #fbf0dd; color: var(--amber); }}
  .ask {{
    background: #eef6fb; border-left: 4px solid #0066cc;
    padding: 18px 20px; border-radius: 0 8px 8px 0; font-size: 14px;
    width: 100%; max-width: none; box-sizing: border-box;
    line-height: 1.55;
  }}
  .ask .subhead {{ margin: 16px 0 8px; font-weight: 700; }}
  .ask .subhead:first-of-type {{ margin-top: 14px; }}
  .ask ul {{ margin: 0; padding-left: 18px; }}
  .ask ul + .subhead {{ margin-top: 16px; }}
  .footer {{ margin-top: 28px; font-size: 11px; color: var(--muted); }}
  a {{ color: #0066cc; }}
  @media print {{
    body {{ background: #fff; }}
    .page {{ max-width: none; padding: 0; }}
    .hero, .card, .kpi {{ box-shadow: none; }}
    .no-print {{ display: none; }}
  }}
</style>
</head>
<body>
  <div class="page">
    <p class="no-print" style="font-size:13px;color:#5c6578">
      Para PDF: navegador → <b>Imprimir → Guardar como PDF</b> (gráficos de fondo activados).
    </p>

    <div class="hero">
      <div class="hero-text">
        <h1>Informe de progreso - RHCSA (EX200)</h1>
        <p><b>Candidato:</b> Felipe Antonio Aleman Arce</p>
        <p>Aproximado Finalización Práctica: 30 oct 2026</p>
        <p>Examen objetivo: RHCSA (EX200) - Requerido para Ruta RHCE (EX294)</p>
        <p>Material: Red Hat RHCSA 9 Cert Guide (Sander van Vugt) + RH124/RH134</p>
      </div>
            <div class="hero-logo" aria-hidden="true">
        <img src="{hat_src}" alt="Red Hat" width="72" height="48" style="display:block"/>
      </div>
    </div>

    <div class="kpis">
      <div class="kpi g"><div class="v">{m["elapsed"]}</div><div class="l">Días desde el comienzo del plan</div></div>
      <div class="kpi a"><div class="v">{m["left"]}</div><div class="l">Días a finalizar la<br/>Práctica pre-examen</div></div>
      <div class="kpi g"><div class="v">2/3</div><div class="l">Cursos base completados</div></div>
    </div>

    <div class="card">
      <h2>Pipeline de estudio</h2>
      <div class="pipeline">
        <div class="pip done">RH024<span>Video·OK</span></div>
        <div class="pip goal">RH104<span>43/56</span></div>
        <div class="pip done">RH124<span>Hecho</span></div>
        <div class="pip done">RH134<span>Hecho</span></div>
        <div class="pip plan">Libro<span>335/1593</span></div>
        <div class="pip goal">RH199<span>10/154</span></div>
        <div class="pip goal">EX200<span>Obj.</span></div>
        <div class="pip plan">EX294<span>Ruta</span></div>
      </div>
    </div>

    <div class="card">
      <h2>Resumen</h2>
      <ul>
        <li><b>RH124</b> y <b>RH134</b> acreditados (completados previamente).</li>
        <li>Examen objetivo: <b>RHCSA (EX200)</b> - requerido para ruta <b>RHCE (EX294)</b>.</li>
        <li>Refuerzo actual: libro <b>Red Hat RHCSA 9 Cert Guide</b> (autor: Sander van Vugt) + labs diarios.</li>
        <li><b>Cap. 7 Permissions Management</b> · Libro <b>335/1593</b> + lab <code>~/lab-permisos</code> (11 sep). Cap. 6 users completado.</li>
        <li><b>RH199</b> Rapid Track v10.0 en curso (10/154 pág · Cap. 2 ch02s03 Links · 27 ago).</li>
        <li><b>Path RHCSA:</b> RH024 (video) completado; <b>RH104</b> Fundamentals v9.1 en curso (<b>43/56</b> · Cap. 4 · 15 sep).</li>
        <li>Fortaleza: shell, archivos, <b>SSH</b> y <b>chmod</b> (modos octal/simbólico). Refuerzo: <b>chown/ownership</b>, ACL, nmcli, systemd.</li>
        <li>Más adelante: storage/LVM, SELinux, firewall y boot.</li>
      </ul>
    </div>
    <div class="card" style="border-left:4px solid var(--amber)">
      <h2>Problemáticas encontradas</h2>
      <div class="ask" style="background:#fbf8f0;border-left-color:var(--amber)">
        <p class="subhead" style="margin-top:0;color:var(--amber)">8 sep 2026</p>
        <p style="margin:0 0 10px">
          Encontré el <b>path correcto</b> para anotarme a rendir el <b>RHCSA</b> en ROL.
          Además de <b>RH124</b> y <b>RH134</b>, el plan exige cursos previos de fundamentals:
        </p>
        <ul>
          <li><b>RH024</b> (video Getting Started) — <b>completado</b>.</li>
          <li><b>RH104</b> Getting Started with Linux Fundamentals <b>v9.1</b> — <b>en curso 43/56 · Cap. 4</b>.</li>
          <li>Impacto: suma carga al plan (libro + RH199 + RH104) hasta el EX200.</li>
        </ul>
      </div>
      <div class="ask" style="background:#fbf8f0;border-left-color:var(--amber);margin-top:14px;padding-bottom:10px">
        <p class="subhead" style="margin-top:0;color:var(--amber)">31 ago 2026</p>
        <p style="margin:0 0 8px">
          Para practicar <b>Cap. 5 (SSH)</b> de la forma más real posible, monté <b>dos VMs Rocky</b> en VirtualBox
          (servidor + cliente). Esto consumió <b>gran parte de las horas de estudio del día</b> (infraestructura en lugar de avanzar páginas del libro).
        </p>
        <ul style="margin-bottom:0">
          <li>Clon inicial: mismo hostname, Machine ID y MAC; conflictos SSH (puertos 2200/2222).</li>
          <li>Segundo disco con LVM duplicado trabó el boot en Server1-nuevo (fix: desmontar disco extra).</li>
          <li>Red host-only: IP por DHCP (<code>192.168.56.102</code>) en vez de estática (<code>.10</code>/<code>.11</code>).</li>
          <li><code>nmcli</code>: el nombre del perfil debe ser exacto (<i>Conexión cableada 1</i>, con acento y minúsculas).</li>
          <li><b>Resuelto:</b> lab 2 VMs (<code>servera</code> .10 + <code>workstation</code> .11); SSH, scp, sftp y claves (Ex 5-5).</li>
        </ul>
        <p style="font-size:12px;color:var(--muted);margin:8px 0 0">
          Nota examen: VirtualBox/clonado no entra; sí puede pedirse IP estática con <code>nmcli</code> en una interfaz dada.
        </p>
      </div>
    </div>

    <div class="card">
      <h2>Perfil y contexto</h2>
      <div class="ask">
        Me desenvuelvo como desarrollador <b>FullStack</b>. Al no haber trabajado
        antes en el área de sysadmin, algunos conceptos me son nuevos y otros
        ya los uso de alguna forma en el día a día.
        <p class="subhead">Disponibilidad</p>
        <ul>
          <li><b>2 hs de estudio por día</b> en el trabajo + días/horarios disponibles fuera de eso</li>
          <li><b>Extra:</b> martes, jueves y sábado 20 a 22 hs</li>
          <li>domingo todo el día</li>
        </ul>
        <p class="subhead">Días ocupados</p>
        <ul>
          <li><b>Lunes y miércoles:</b> 19 a 22 hs inglés en el CUI</li>
          <li><b>Sábados:</b> universidad de 8 a 15 hs (+ 1 hs de viaje a la universidad)</li>
        </ul>
        <p class="subhead">Otras Obligaciones</p>
        <ul>
          <li>Rendir Matemática Universidad <b>14 de septiembre</b></li>
        </ul>
      </div>
    </div>

    <div class="card">
      <h2>Credenciales y horizonte (orden de plan)</h2>
      <table>
        <thead><tr><th>Ítem</th><th>Estado</th><th>Enlace</th></tr></thead>
        <tbody>
          <tr>
            <td><b>RH199</b> Rapid Track (v10.0)</td>
            <td><span class="tag plan">En curso · 10/154 pág · Cap. 2 ch02s03 Links (27 ago)</span></td>
            <td><a href="{URL_RH199}" target="_blank" rel="noopener noreferrer">Curso en ROL</a></td>
          </tr>
          <tr>
            <td><b>RH104</b> Linux Fundamentals v9.1</td>
            <td><span class="tag warn">En curso · 43/56 · Cap. 4 · path RHCSA (15 sep)</span></td>
            <td>—</td>
          </tr>
          <tr>
            <td><b>RH024</b> Getting Started (video)</td>
            <td><span class="tag ok">Completado (8 sep)</span></td>
            <td>—</td>
          </tr>
          <tr>
            <td><a href="{URL_RH124}" target="_blank" rel="noopener noreferrer"><b>RH124</b> Sysadmin I</a></td>
            <td><span class="tag ok">Obtenido</span></td>
            <td><a href="{URL_RH124}" target="_blank" rel="noopener noreferrer">Ver certificado</a></td>
          </tr>
          <tr>
            <td><a href="{URL_RH134}" target="_blank" rel="noopener noreferrer"><b>RH134</b> Sysadmin II</a></td>
            <td><span class="tag ok">Obtenido</span></td>
            <td><a href="{URL_RH134}" target="_blank" rel="noopener noreferrer">Ver certificado</a></td>
          </tr>
          <tr>
            <td>EX200 RHCSA</td>
            <td><span class="tag warn">Objetivo</span></td>
            <td><a href="{URL_EX200}" target="_blank" rel="noopener noreferrer">Página oficial del examen</a></td>
          </tr>
          <tr>
            <td>EX294 RHCE</td>
            <td><span class="tag plan">Ruta · EX200 requerido</span></td>
            <td><a href="{URL_EX294}" target="_blank" rel="noopener noreferrer">Página oficial del examen</a></td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="card">
      <h2>Avance del plan de refuerzo</h2>
      <div class="bar-wrap">
        <div class="bar-label"><span>Calendario total del plan (18 ago → 30 oct)</span><span>{m["elapsed"]} transcurridos + {m["left"]} restantes = {m["total"]} (~{m["pct_cal"]}%)</span></div>
        <div class="bar"><i style="width:{m["pct_cal"]}%;background:#0066cc"></i></div>
      </div>
      <div class="bar-wrap">
        <div class="bar-label"><span>Libro Red Hat RHCSA 9 Cert Guide (Sander van Vugt)</span><span>{m["book_page"]} / {m["book_total"]} (~{m["book_pct"]}%) · Cap. 7 Permissions Management</span></div>
        <div class="bar"><i style="width:{m["book_pct"]}%;background:#37a3a3"></i></div>
        <p style="font-size:13px;color:#ee0000;font-weight:700;margin:8px 0 0;line-height:1.45">
          Libro (PDF {m["book_total"]}): faltan {m["book_left"]} &nbsp;|&nbsp; 15/día → ~nov &nbsp;|&nbsp; meta 30 oct ({m["left"]} d) → ~{m["need_pdf"]}/día
        </p>
        <p style="font-size:13px;color:#0066cc;font-weight:700;margin:6px 0 0;line-height:1.45">
          Libro (contenido útil ~{BOOK_USEFUL}): faltan ~{m["useful_left"]} &nbsp;|&nbsp; 15/día → ~fin oct &nbsp;|&nbsp; meta 30 oct → ~{m["need_useful"]}/día
        </p>
        <p style="font-size:13px;color:#63993d;font-weight:700;margin:6px 0 0;line-height:1.45">
          Promedio hasta hoy: ~{m["avg"]} pág/día ({m["book_page"]} en {m["elapsed"]} d) &nbsp;|&nbsp; para meta: ~{m["need_pdf"]} PDF o ~{m["need_useful"]} útil
        </p>
      </div>
      <div class="bar-wrap">
        <div class="bar-label"><span>RH104 Getting Started with Linux Fundamentals (v9.1) — ROL</span><span>{m["rh104_page"]} / {m["rh104_total"]} (~{m["rh104_pct"]}%) · Cap. 4 ch04 · path RHCSA · 15 sep</span></div>
        <div class="bar"><i style="width:{m["rh104_pct"]}%;background:#f5921b"></i></div>
        <p style="font-size:13px;color:#63993d;font-weight:700;margin:8px 0 0;line-height:1.45">
          RH104: labs en GUI GNOME via VNC (no solo CLI); faltan {m["rh104_left"]} unidades.
        </p>
      </div>
      <div class="bar-wrap">
        <div class="bar-label"><span>RH199 Rapid Track v10.0 (ROL)</span><span>{m["rh199_page"]} / {m["rh199_total"]} (~{m["rh199_pct"]}%) · Cap. 2 ch02s03 Links · 27 ago</span></div>
        <div class="bar"><i style="width:{m["rh199_pct"]}%;background:#f5921b"></i></div>
        <p style="font-size:13px;color:#63993d;font-weight:700;margin:8px 0 0;line-height:1.45">
          RH199: Cap. 2 ch02s03 Links / enlaces simbólicos ({m["rh199_page"]}/{m["rh199_total"]}).
        </p>
      </div>
      <h3>Prioridad de estudio (importancia + comodidad · 1 menor · 10 mayor)</h3>
      <p style="font-size:12px;color:var(--muted);margin:0 0 10px">Combina lo crítico para el examen con cómo nos sentimos hoy en cada tema.</p>
      <div class="prio">
        <div class="prio-row"><span>Reset root / rd.break</span><div class="track"><i style="width:100%;background:#ee0000"></i></div><span>10</span></div>
        <div class="prio-row"><span>Persistencia al reboot</span><div class="track"><i style="width:100%;background:#ee0000"></i></div><span>10</span></div>
        <div class="prio-row"><span>Storage + LVM + fstab</span><div class="track"><i style="width:100%;background:#ee0000"></i></div><span>10</span></div>
        <div class="prio-row"><span>SELinux</span><div class="track"><i style="width:100%;background:#ee0000"></i></div><span>10</span></div>
        <div class="prio-row"><span>Red + firewall (nmcli/nmtui)</span><div class="track"><i style="width:90%;background:#f5921b"></i></div><span>9</span></div>
        <div class="prio-row"><span>Boot / troubleshoot</span><div class="track"><i style="width:90%;background:#f5921b"></i></div><span>9</span></div>
        <div class="prio-row"><span>systemd + cron</span><div class="track"><i style="width:70%;background:#0066cc"></i></div><span>7</span></div>
        <div class="prio-row"><span>DNF + Flatpak</span><div class="track"><i style="width:50%;background:#63993d"></i></div><span>5</span></div>
        <div class="prio-row"><span>Users / grupos</span><div class="track"><i style="width:40%;background:#63993d"></i></div><span>4</span></div>
        <div class="prio-row"><span>Permisos + ACL</span><div class="track"><i style="width:30%;background:#63993d"></i></div><span>3</span></div>
        <div class="prio-row"><span>SSH</span><div class="track"><i style="width:30%;background:#63993d"></i></div><span>3</span></div>
        <div class="prio-row"><span>Hard/soft links</span><div class="track"><i style="width:30%;background:#63993d"></i></div><span>3</span></div>
        <div class="prio-row"><span>Comprimir/extraer (tar)</span><div class="track"><i style="width:20%;background:#63993d"></i></div><span>2</span></div>
        <div class="prio-row"><span>Shell / archivos</span><div class="track"><i style="width:10%;background:#63993d"></i></div><span>1</span></div>
      </div>
      <p style="font-size:12px;color:var(--muted);margin:8px 0 0">
        <b>Reset root / rd.break:</b> GRUB → rd.break → remount rw → chroot → passwd → touch /.autorelabel (fundamental en EX200).
        <br><b>Persistencia al reboot:</b> que la config siga tras reiniciar (fstab, enable, red/firewall permanentes, etc.).
      </p>

      <div class="chart-block">
      <h3>Ritmo libro Van Vugt (335 / 1593 pág)</h3>
      <p style="font-size:12px;color:var(--muted)">Páginas acumuladas del PDF del libro. Actual: 335 / 1593 · Cap. 7 Permissions (chmod OK; chown en refuerzo · 11 sep).</p>
      <svg viewBox="0 0 560 150" width="560" height="150" role="img" aria-label="Ritmo libro Van Vugt">
        <line x1="20" y1="118" x2="540" y2="118" stroke="#c5ced9"/>
        <rect x="20" y="91" width="16" height="27" fill="#0066cc"/>
        <text x="28" y="136" font-size="5" fill="#5c6578" text-anchor="middle">18</text>
        <text x="28" y="85" font-size="7" fill="#151515" text-anchor="middle">80</text>
        <rect x="68" y="76" width="16" height="42" fill="#0066cc"/>
        <text x="76" y="136" font-size="5" fill="#5c6578" text-anchor="middle">19</text>
        <text x="76" y="70" font-size="7" fill="#151515" text-anchor="middle">125</text>
        <rect x="116" y="65" width="16" height="53" fill="#0066cc"/>
        <text x="124" y="136" font-size="5" fill="#5c6578" text-anchor="middle">21</text>
        <text x="124" y="59" font-size="7" fill="#151515" text-anchor="middle">160</text>
        <rect x="164" y="53" width="16" height="65" fill="#0066cc"/>
        <text x="172" y="136" font-size="5" fill="#5c6578" text-anchor="middle">25</text>
        <text x="172" y="47" font-size="7" fill="#151515" text-anchor="middle">196</text>
        <rect x="212" y="47" width="16" height="71" fill="#0066cc"/>
        <text x="220" y="136" font-size="5" fill="#5c6578" text-anchor="middle">26</text>
        <text x="220" y="41" font-size="7" fill="#151515" text-anchor="middle">214</text>
        <rect x="260" y="40" width="16" height="78" fill="#0066cc"/>
        <text x="268" y="136" font-size="5" fill="#5c6578" text-anchor="middle">27</text>
        <text x="268" y="34" font-size="7" fill="#151515" text-anchor="middle">234</text>
        <rect x="308" y="35" width="16" height="83" fill="#0066cc"/>
        <text x="316" y="136" font-size="5" fill="#5c6578" text-anchor="middle">28</text>
        <text x="316" y="29" font-size="7" fill="#151515" text-anchor="middle">251</text>
        <rect x="356" y="28" width="16" height="89" fill="#0066cc"/>
        <text x="364" y="136" font-size="5" fill="#5c6578" text-anchor="middle">30</text>
        <text x="364" y="22" font-size="7" fill="#151515" text-anchor="middle">270</text>
        <rect x="404" y="27" width="16" height="90" fill="#0066cc"/>
        <text x="412" y="136" font-size="5" fill="#5c6578" text-anchor="middle">31</text>
        <text x="412" y="21" font-size="7" fill="#151515" text-anchor="middle">272</text>
        <rect x="452" y="35" width="16" height="83" fill="#0066cc"/>
        <text x="460" y="136" font-size="5" fill="#5c6578" text-anchor="middle">1 sep</text>
        <text x="460" y="35" font-size="7" fill="#151515" text-anchor="middle">298</text>

        <rect x="500" y="32" width="16" height="86" fill="#0066cc"/>
        <text x="508" y="136" font-size="5" fill="#5c6578" text-anchor="middle">2 sep</text>
        <text x="508" y="32" font-size="7" fill="#151515" text-anchor="middle">309</text>

        <rect x="548" y="29" width="16" height="89" fill="#0066cc"/>
        <text x="556" y="136" font-size="5" fill="#5c6578" text-anchor="middle">3 sep</text>
        <text x="556" y="29" font-size="7" fill="#151515" text-anchor="middle">321</text>

        <rect x="596" y="28" width="16" height="90" fill="#63993d"/>
        <text x="604" y="136" font-size="5" fill="#5c6578" text-anchor="middle">4 sep</text>
        <text x="604" y="28" font-size="7" fill="#151515" text-anchor="middle">335</text>
      </svg>
      </div>

      <div class="chart-block" style="margin-top:32px">
      <h3>Ritmo RH199 Rapid Track (10 / 154 pág)</h3>
      <p style="font-size:12px;color:var(--muted)">Páginas acumuladas del curso en ROL. Actual: 10 / 154 · Cap. 2 ch02s03 Links · 27 ago.</p>
      <svg viewBox="0 0 120 110" width="120" height="110" role="img" aria-label="Ritmo RH199 Rapid Track">
        <line x1="10" y1="78" x2="110" y2="78" stroke="#c5ced9"/>
        <rect x="46" y="58" width="28" height="20" fill="#f5921b"/>
        <text x="60" y="96" font-size="9" fill="#5c6578" text-anchor="middle">27 ago</text>
        <text x="60" y="52" font-size="10" fill="#151515" text-anchor="middle">10</text>
      </svg>
      </div>
    </div>

    <div class="card" style="margin-bottom:28px">
      <h2>Fases de estudio (RHCSA 10 / EX200)</h2>
      <table>
        <thead><tr><th>Fase</th><th>Hasta</th><th>Foco</th></tr></thead>
        <tbody>
          <tr><td>Hecho</td><td>4 sep</td><td>Cap. 1-6: install, tools, files, SSH, users/groups</td></tr>
          <tr><td>Ahora</td><td>15 sep</td><td>Cap. 7: chmod OK; afianzar chown/ownership + ACL (pág 335)</td></tr>
          <tr><td>Bloque B</td><td>sep</td><td>Red nmcli (Cap. 8) — SSH ya hecho</td></tr>
          <tr><td>Bloque C</td><td>sep</td><td>DNF + Flatpak + systemd/cron</td></tr>
          <tr><td>Crítico</td><td>fin sep</td><td>Storage LVM/fstab (+ NFS/autofs)</td></tr>
          <tr><td>Seguridad</td><td>ini oct</td><td>SELinux + firewall + boot</td></tr>
          <tr><td>Cierre</td><td>~30 oct</td><td>Repaso / practice exams (EX200 RHEL 10)</td></tr>
        </tbody>
      </table>
    </div>

    <div class="card">
      <h2>Plan de estudio</h2>
      <div class="ask">
        <ol style="margin:0;padding-left:18px">
          <li>Continuar labs en Rocky 10 según las fases anteriores.</li>
          <li><b>RH199</b> Rapid Track en curso (10/154 pág · Cap. 2 ch02s03 Links · 27 ago); EX200 como objetivo.</li>
          <li>Hito actual: <b>Cap. 7</b> pág 335 · chmod más sólido; pendiente afianzar <b>chown</b>/ownership + ACL · lab-permisos (11 sep).</li>
        </ol>
      </div>
    </div>

    <div class="card" style="margin-bottom:12px">
      <h2>Bibliografía y enlaces</h2>
      <h3 style="margin-top:0">Bibliografía</h3>
      <ul>
        <li>van Vugt, Sander — <b>Red Hat RHCSA 9 Cert Guide</b> (Pearson; libro principal de estudio).</li>
        <li>Red Hat — <b>RH124</b> System Administration I</li>
        <li>Red Hat — <b>RH134</b> System Administration II</li>
        <li>Red Hat — <b>RH199</b> RHCSA Rapid Track (v10.0)</li>
      </ul>
      <h3>Vistos</h3>
      <ul>
        <li>
          <a href="{URL_YT_TIPS}" target="_blank" rel="noopener noreferrer">
            How I Scored 290/290 on the RHCSA Exam – 8 Tips You Need to Know!
          </a>
        </li>
        <li>
          <a href="{URL_YT_INSIDE}" target="_blank" rel="noopener noreferrer">
            Inside a Red Hat Certification Exam: What you need to know
          </a>
        </li>
      </ul>
      <h3 style="color:var(--amber)">Por ver (importante)</h3>
      <ul>
        <li>
          <span class="tag warn" style="margin-right:6px">pendiente</span>
          <a href="{URL_YT_RUIN}" target="_blank" rel="noopener noreferrer">
            3 RHCSA Exam Tasks That Will RUIN Your Score!
          </a>
        </li>
        <li>
          <span class="tag warn" style="margin-right:6px">pendiente</span>
          <a href="{URL_YT_PREP}" target="_blank" rel="noopener noreferrer">
            RHCSA 9/10 Exam Prep: Real EX200 Questions &amp; Step-by-Step Solutions
          </a>
        </li>
        <li>
          <span class="tag warn" style="margin-right:6px">pendiente</span>
          <a href="{URL_YT_NICODEMOS}" target="_blank" rel="noopener noreferrer">
            Playlist RHCSA exam prep series — NicoDemos
          </a>
        </li>
      </ul>
      <h3 style="margin-top:20px">Enlaces (hipervínculos)</h3>
      <ul>
        <li><a href="{URL_RH124}" target="_blank" rel="noopener noreferrer">RH124 — badge Credly</a></li>
        <li><a href="{URL_RH134}" target="_blank" rel="noopener noreferrer">RH134 — badge Credly</a></li>
        <li><a href="{URL_RH199}" target="_blank" rel="noopener noreferrer">RH199 — Rapid Track v10.0 (ROL)</a></li>
        <li><a href="{URL_EX200}" target="_blank" rel="noopener noreferrer">EX200 — examen RHCSA oficial</a></li>
        <li><a href="{URL_EX294}" target="_blank" rel="noopener noreferrer">EX294 — examen RHCE (ruta posterior)</a></li>
      </ul>
    </div>

    <p class="footer">
      Generado {REPORT_AS_OF.strftime('%d/%m/%Y')} · Seguimiento preparación RHCSA · Plan de estudio
    </p>
  </div>
</body>
</html>
"""


def main() -> None:
    PDF_OUT.write_bytes(build_pdf())
    HTML_OUT.write_text(build_html(), encoding="utf-8")
    print(f"OK PDF:  {PDF_OUT} ({PDF_OUT.stat().st_size} bytes)")
    print(f"OK HTML: {HTML_OUT} ({HTML_OUT.stat().st_size} bytes)")
    try:
        import importlib.util

        docx_path = Path(__file__).with_name("generar-informe-rhcsa-docx.py")
        spec = importlib.util.spec_from_file_location("rhcsa_docx", docx_path)
        if spec and spec.loader:
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            mod.main()
    except Exception as e:
        print(f"WARN DOCX: {e}")


if __name__ == "__main__":
    main()
