import {
  BarChart,
  Callout,
  Card,
  CardBody,
  CardHeader,
  Divider,
  Grid,
  H1,
  H2,
  H3,
  LineChart,
  Link,
  Pill,
  Row,
  Stack,
  Stat,
  Table,
  Text,
  UsageBar,
} from "cursor/canvas";

/** Red Hat Brand: red-50 #ee0000 · gray-95 #151515 · white */
const RH = {
  red: "#ee0000",
  red10: "#fce3e3",
  black: "#151515",
  gray50: "#707070",
  white: "#ffffff",
  green: "#63993d",
  orange: "#f5921b",
  teal: "#37a3a3",
};

/** Fedora: rojo + banda negra al medio (logo Red Hat) */
function RedHatLogo({ size = 48 }: { size?: number }) {
  return (
    <svg
      width={size}
      height={Math.round(size * 0.76)}
      viewBox="0 0 192.3 146"
      aria-label="Red Hat"
      role="img"
    >
      <path
        fill={RH.red}
        d="m 128,84 c 12.5,0 30.6,-2.6 30.6,-17.5 a 19.53,19.53 0 0 0 -0.3,-3.4 L 150.9,30.7 C 149.2,23.6 147.7,20.3 135.2,14.1 125.5,9.1 104.4,1 98.1,1 92.2,1 90.5,8.5 83.6,8.5 76.9,8.5 72,2.9 65.7,2.9 c -6,0 -9.9,4.1 -12.9,12.5 0,0 -8.4,23.7 -9.5,27.2 a 6.15,6.15 0 0 0 -0.2,1.9 C 43,53.7 79.3,83.9 128,84 m 32.5,-11.4 c 1.7,8.2 1.7,9.1 1.7,10.1 0,14 -15.7,21.8 -36.4,21.8 C 79,104.5 38.1,77.1 38.1,59 a 18.35,18.35 0 0 1 1.5,-7.3 C 22.8,52.5 1,55.5 1,74.7 1,106.2 75.6,145 134.6,145 c 45.3,0 56.7,-20.5 56.7,-36.7 0,-12.7 -11,-27.1 -30.8,-35.7"
      />
      <path
        fill="#000000"
        d="m 160.5,72.6 c 1.7,8.2 1.7,9.1 1.7,10.1 0,14 -15.7,21.8 -36.4,21.8 C 79,104.5 38.1,77.1 38.1,59 a 18.35,18.35 0 0 1 1.5,-7.3 l 3.7,-9.1 a 6.15,6.15 0 0 0 -0.2,1.9 c 0,9.2 36.3,39.4 84.9,39.4 12.5,0 30.6,-2.6 30.6,-17.5 A 19.53,19.53 0 0 0 158.3,63 Z"
      />
    </svg>
  );
}

export default function RhcsaProgreso() {
  return (
    <Stack gap={0} style={{ maxWidth: 960 }}>
      {/* Header: fondo negro, gorrito rojo visible */}
      <Stack
        gap={12}
        style={{
          background: RH.black,
          padding: "28px 28px",
          minHeight: 120,
          justifyContent: "center",
        }}
      >
        <Row gap={14} align="center" justify="space-between">
          <Stack gap={6} style={{ flex: 1, minWidth: 0 }}>
            <H1 style={{ color: RH.white, margin: 0 }}>
              RHCSA - Tablero de progreso
            </H1>
            <Text size="small" style={{ color: RH.white }}>
              Felipe Antonio Aleman Arce · Meta RHCSA (EX200) → RHCE (EX294)
            </Text>
          </Stack>
          <RedHatLogo size={52} />
        </Row>
        <Row gap={8} wrap>
          <Pill tone="success" size="sm">
            RH124 Credly
          </Pill>
          <Pill tone="success" size="sm">
            RH134 Credly
          </Pill>
          <Pill tone="neutral" size="sm">
            EX200 horizonte
          </Pill>
        </Row>
      </Stack>

      {/* Cuerpo: fondo blanco, texto oscuro */}
      <Stack
        gap={20}
        style={{
          background: RH.white,
          padding: 24,
          color: RH.black,
        }}
      >
        <Grid columns={3} gap={12}>
          <div
            style={{
              background: RH.white,
              border: `1px solid #e0e0e0`,
              borderTop: `3px solid ${RH.green}`,
              padding: 12,
              borderRadius: 8,
            }}
          >
            <Stat value="28" label="Días desde el comienzo del plan" />
          </div>
          <div
            style={{
              background: RH.white,
              border: `1px solid #e0e0e0`,
              borderTop: `3px solid ${RH.orange}`,
              padding: 12,
              borderRadius: 8,
            }}
          >
            <Stat value="45" label="Días a finalizar la · Práctica pre-examen" tone="warning" />
          </div>
          <div
            style={{
              background: RH.white,
              border: `1px solid #e0e0e0`,
              borderTop: `3px solid ${RH.green}`,
              padding: 12,
              borderRadius: 8,
            }}
          >
            <Stat value="2/3" label="Cursos → Examen" tone="success" />
          </div>
        </Grid>

        <Callout tone="info">
          Examen objetivo: RHCSA (EX200) - requerido para ruta RHCE (EX294).
          Pipeline: RH024 → RH104 → RH124 → RH134 → Libro → RH199 → EX200 →
          EX294.
        </Callout>

        <H2 style={{ color: RH.black }}>Credenciales y examen</H2>
        <Table
          headers={["Ítem", "Estado", "Referencia"]}
          rows={[
            [
              "RH024 Getting Started (video)",
              "Terminado",
              "8 sep 2026",
            ],
            [
              "RH104 Linux Fundamentals v9.1",
              "En curso · 43/56 · Cap. 4",
              "Path RHCSA · 8 sep",
            ],
            [
              "RH199 Rapid Track (v10.0)",
              "En curso · 10/154 pág · ch02s03 Links",
              "Desde 27 ago",
            ],
            ["RH124 Sysadmin I", "Obtenido", "Ver certificado"],
            ["RH134 Sysadmin II", "Obtenido", "Ver certificado"],
            ["EX200 RHCSA", "Objetivo", "Siguiente paso"],
            [
              "EX294 RHCE",
              "Ruta posterior",
              "EX200 requerido para RHCE",
            ],
          ]}
          rowTone={[
            "success",
            "warning",
            "info",
            "success",
            "success",
            "warning",
            "info",
          ]}
        />
        <Stack gap={4}>
          <Text size="small">
            <Link
              href="https://www.credly.com/badges/b3bb2779-eefd-4646-813c-e142e5c9d219/linked_in_profile"
              target="_blank"
            >
              Certificado RH124
            </Link>
            {" · "}
            <Link
              href="https://www.credly.com/badges/a6a4a878-0fec-4a05-9c66-57cc1e6de2f6/linked_in?t=tioxto"
              target="_blank"
            >
              Certificado RH134
            </Link>
          </Text>
          <Text size="small">
            <Link
              href="https://rol.redhat.com/rol/app/courses/rh199-10.0/pages/pr01"
              target="_blank"
            >
              RH199 - Rapid Track v10.0 (ROL)
            </Link>
          </Text>
          <Text size="small">
            <Link
              href="https://www.redhat.com/es/services/training/ex200-red-hat-certified-system-administrator-rhcsa-exam"
              target="_blank"
            >
              EX200 - examen RHCSA
            </Link>
          </Text>
          <Text size="small">
            <Link
              href="https://www.redhat.com/es/services/training/ex294-red-hat-certified-engineer-rhce-exam-red-hat-enterprise-linux-9"
              target="_blank"
            >
              EX294 - examen RHCE
            </Link>
          </Text>
        </Stack>

        <Divider />

        <H2 style={{ color: RH.black }}>RH199 en el plan</H2>
        <Grid columns={2} gap={12}>
          <Card>
            <CardHeader>Qué es</CardHeader>
            <CardBody>
              <Text size="small">
                RHCSA Rapid Track v10.0: review intensivo hacia EX200, para
                perfiles con experiencia / sysadmin previo.
              </Text>
            </CardBody>
          </Card>
          <Card>
            <CardHeader>En el plan</CardHeader>
            <CardBody>
              <Text size="small">
                En curso desde 27 ago (10/154 pág · Cap. 2 ch02s03 Links en ROL). Complementa el libro
                Van Vugt + labs en Rocky 10.
              </Text>
            </CardBody>
          </Card>
        </Grid>

        <Divider />

        <Stack gap={10}>
          <H2 style={{ color: RH.black }}>
            Plazo refuerzo (finalización ~30 oct)
          </H2>
          <UsageBar
            total={73}
            topLeftLabel="28 transcurridos / 73 total"
            topRightLabel="45 restantes (28+45=73)"
            segments={[
              { id: "done", value: 28, color: "blue" },
              { id: "left", value: 45, color: "gray" },
            ]}
          />
        </Stack>

        <Stack gap={10}>
          <H2 style={{ color: RH.black }}>
            Avance: libro Van Vugt + RH104 + RH199
          </H2>
          <UsageBar
            total={1593}
            topLeftLabel="Libro Van Vugt · ~21%"
            topRightLabel="335 / 1593"
            segments={[
              { id: "read", value: 335, color: "cyan" },
              { id: "unread", value: 1258, color: "gray" },
            ]}
          />
          <Text
            size="small"
            weight="semibold"
            style={{ color: RH.red }}
          >
            Libro (PDF 1593): faltan 1258 · meta 30 oct → ~28/día
          </Text>
          <Text
            size="small"
            weight="semibold"
            style={{ color: "#0066cc" }}
          >
            Libro (útil ~1135): faltan ~800 · meta 30 oct → ~18/día
          </Text>
          <UsageBar
            total={56}
            topLeftLabel="RH104 Fundamentals v9.1 · ~77%"
            topRightLabel="43 / 56"
            segments={[
              { id: "done", value: 43, color: "orange" },
              { id: "todo", value: 13, color: "gray" },
            ]}
          />
          <Text
            size="small"
            weight="semibold"
            style={{ color: RH.green }}
          >
            RH104: labs en GUI GNOME vía VNC (no solo CLI) · Cap. 4 ch04 · path RHCSA (15 sep).
          </Text>
          <UsageBar
            total={154}
            topLeftLabel="RH199 Rapid Track · ~6%"
            topRightLabel="10 / 154"
            segments={[
              { id: "done", value: 10, color: "orange" },
              { id: "todo", value: 144, color: "gray" },
            ]}
          />
          <Text
            size="small"
            weight="semibold"
            style={{ color: RH.green }}
          >
            RH199: Cap. 2 ch02s03 Links / enlaces simbólicos (10/154).
          </Text>
        </Stack>

        <Card>
          <CardHeader>Ritmo libro Van Vugt</CardHeader>
          <CardBody>
            <Text size="small" style={{ marginBottom: 8, color: RH.gray50 }}>
              Páginas del PDF · Actual: 335 / 1593 · Cap. 7 (4 sep)
            </Text>
            <BarChart
              height={180}
              categories={["18 ago", "1 sep", "2 sep", "3 sep", "4 sep"]}
              series={[
                {
                  name: "Pág. libro",
                  data: [80, 298, 309, 321, 335],
                  tone: "info",
                },
              ]}
              yMin={0}
              yMax={335}
              showValues
            />
          </CardBody>
        </Card>
        <Card>
          <CardHeader>Ritmo RH199 Rapid Track</CardHeader>
          <CardBody>
            <Text size="small" style={{ marginBottom: 8, color: RH.gray50 }}>
              Páginas del curso ROL · Actual: 10 / 154 · Cap. 2 ch02s03 Links · 27 ago
            </Text>
            <LineChart
              height={160}
              categories={["27 ago"]}
              series={[
                {
                  name: "Pág. RH199",
                  data: [10],
                  tone: "warning",
                },
              ]}
              yMin={0}
              yMax={20}
            />
          </CardBody>
        </Card>

        <H2 style={{ color: RH.black }}>
          Prioridad de estudio (importancia + comodidad · 1 menor · 10 mayor)
        </H2>
        <Text size="small" style={{ color: RH.gray50, marginBottom: 8 }}>
          Combina lo crítico para el examen con cómo nos sentimos hoy en cada
          tema.
        </Text>
        <BarChart
          height={280}
          horizontal
          categories={[
            "Reset root / rd.break",
            "Persistencia al reboot",
            "Storage + LVM + fstab",
            "SELinux",
            "Red + firewall (nmcli/nmtui)",
            "Boot / troubleshoot",
            "systemd + cron",
            "DNF + Flatpak",
            "Users / grupos",
            "Permisos + ACL",
            "SSH",
            "Hard/soft links",
            "Comprimir/extraer (tar)",
            "Shell / archivos",
          ]}
          series={[
            {
              name: "Prioridad (1-10)",
              data: [10, 10, 10, 10, 9, 9, 7, 5, 4, 3, 3, 3, 2, 1],
              tone: "info",
            },
          ]}
        />

        <Callout tone="info">
          Cap. 7 (11 sep): más seguro con chmod (octal/simbólico). Pendiente
          afianzar chown usuario:grupo y ownership; después ACL /
          SUID-SGID-sticky.
        </Callout>

        <Callout tone="warning">
          Reset root / rd.break (10): GRUB → rd.break → remount rw → chroot →
          passwd → touch /.autorelabel. Fundamental en EX200. Persistencia al
          reboot: fstab, enable, red/firewall permanentes.
        </Callout>

        <H2 style={{ color: RH.black }}>Fases hasta el examen (RHCSA 10)</H2>
        <Table
          headers={["Fase", "Hasta", "Foco"]}
          rows={[
            ["Hecho", "4 sep", "Cap. 1-6: install, tools, files, SSH, users/groups"],
            ["Ahora", "15 sep", "Cap. 7: chmod OK; afianzar chown/ownership + ACL (pág 335)"],
            ["Bloque B", "sep", "Red nmcli (Cap. 8) — SSH ya hecho"],
            ["Bloque C", "sep", "DNF + Flatpak + systemd/cron"],
            ["Crítico", "fin sep", "Storage LVM/fstab (+ NFS/autofs)"],
            ["Seguridad", "ini oct", "SELinux + firewall + boot"],
            ["Cierre", "~30 oct", "Practice exams → EX200 RHEL 10"],
          ]}
          rowTone={[
            "success",
            "info",
            "warning",
            "warning",
            "warning",
            "info",
            "success",
          ]}
        />

        <H2 style={{ color: RH.black }}>Bibliografía</H2>
        <Table
          headers={["Material", "Uso"]}
          rows={[
            [
              "van Vugt — Red Hat RHCSA 9 Cert Guide",
              "Libro principal de estudio",
            ],
            ["RH124 Sysadmin I (Red Hat)", "Curso oficial"],
            ["RH134 Sysadmin II (Red Hat)", "Curso oficial"],
          ]}
        />

        <H2 style={{ color: RH.black }}>Videos vistos</H2>
        <Table
          headers={["Video", "Enlace"]}
          rows={[
            [
              "How I Scored 300/300 on the RHCSA Exam – 8 Tips",
              "YouTube",
            ],
            [
              "Inside a Red Hat Certification Exam: What you need to know",
              "YouTube",
            ],
          ]}
        />
        <Stack gap={4}>
          <Text size="small">
            <Link href="https://www.youtube.com/watch?v=QlAwLcLz8CM" target="_blank">
              Tips 300/300 RHCSA
            </Link>
            {" · "}
            <Link href="https://www.youtube.com/watch?v=Me6Y12-sux8" target="_blank">
              Inside a Red Hat Certification Exam
            </Link>
          </Text>
        </Stack>

        <Stack
          gap={12}
          style={{
            background: "#eef6fb",
            padding: 20,
            borderRadius: 8,
            borderLeft: `4px solid #0066cc`,
            width: "100%",
            maxWidth: "100%",
          }}
        >
          <H3 style={{ color: RH.black, margin: 0 }}>Perfil y contexto</H3>
          <Text style={{ color: RH.black, maxWidth: "100%", width: "100%" }}>
            Me desenvuelvo como desarrollador FullStack. Al no haber trabajado
            antes en el área de sysadmin, algunos conceptos me son nuevos y
            otros ya los uso de alguna forma en el día a día.
          </Text>
          <Text weight="semibold" style={{ color: RH.black, marginTop: 4 }}>
            Disponibilidad
          </Text>
          <Text style={{ color: RH.black }}>
            - 2 hs de estudio por día en el trabajo + días/horarios disponibles
              fuera de eso
          </Text>
          <Text style={{ color: RH.black }}>
            - Extra: martes, jueves y sábado 20 a 22 hs
          </Text>
          <Text style={{ color: RH.black }}>- domingo todo el día</Text>
          <Text weight="semibold" style={{ color: RH.black, marginTop: 4 }}>
            Días ocupados
          </Text>
          <Text style={{ color: RH.black }}>
            - Lunes y miércoles: 19 a 22 hs inglés en el CUI
          </Text>
          <Text style={{ color: RH.black }}>
            - Sábados: universidad de 8 a 15 hs (+ 1 hs de viaje a la
              universidad)
          </Text>
          <Text weight="semibold" style={{ color: RH.black, marginTop: 4 }}>
            Otras Obligaciones
          </Text>
          <Text style={{ color: RH.black }}>
            - Rendir Matemática Universidad 14 de septiembre
          </Text>
        </Stack>
      </Stack>
    </Stack>
  );
}
