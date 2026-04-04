---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Preguntas frecuentes sobre el analizador de extractos bancarios"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/corporate-finance.webp"
cdn: "https://cloudcdn.pro"
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Analizador de extractos bancarios. Reservados todos los derechos."
date: "Apr 01, 2026"
description: "Respuestas a preguntas comunes sobre Bank Statement Parser: privacidad de datos, redacción de PII, rendimiento, compatibilidad con ISO 20022, transmisión, cumplimiento y flujos de trabajo de tesorería."
download: ""
format-detection: "telephone=no"
hreflang: "es"
icon: "https://cloudcdn.pro/bankstatementparser/images/favicon.ico"
id: "https://bankstatementparser.com/es/faq/index.html"
image_alt: "Logotipo de Bank Statement Parser, una potente herramienta Python diseñada para el procesamiento de datos financieros y la extracción de conocimientos de forma rápida y precisa."
image_height: "630"
image_width: "1200"
image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
keywords: "Preguntas frecuentes sobre el analizador de extractos bancarios, preguntas sobre el analizador CAMT, preguntas frecuentes sobre PAIN.001, preguntas frecuentes sobre Python ISO 20022, redacción de PII bancaria, rendimiento del analizador bancario, privacidad de datos financieros, preguntas frecuentes sobre el analizador MT940, analizador de streaming en Python, cumplimiento de extractos bancarios"
language: "es-ES"
layout: "faq"
locale: "es_ES"
logo_alt: "Logotipo de Bank Statement Parser, una potente herramienta Python diseñada para el procesamiento de datos financieros y la extracción de conocimientos de forma rápida y precisa."
logo_height: "44"
logo_width: "44"
logo: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Preguntas frecuentes"
permalink: "https://bankstatementparser.com/es/faq/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Preguntas comunes sobre el analizador de extractos bancarios"
tags: "preguntas frecuentes, banco, extracto, analizador, privacidad, cumplimiento, rendimiento, streaming, iso20022, python"
theme_color: "rgb(73, 214, 251)"
title: "Preguntas frecuentes sobre el analizador de extractos bancarios: privacidad, rendimiento y uso"
url: "https://bankstatementparser.com/es/faq/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/es/faq/rss.xml"
category: "Software financiero, biblioteca Python, preguntas frecuentes"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Respuestas a preguntas comunes sobre Bank Statement Parser: privacidad de datos, redacción de PII, rendimiento, compatibilidad con ISO 20022, transmisión, cumplimiento y flujos de trabajo de tesorería."
item_guid: "https://bankstatementparser.com/es/faq/rss.xml"
item_link: "https://bankstatementparser.com/es/faq/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Preguntas frecuentes sobre el analizador de extractos bancarios: privacidad, rendimiento y uso"
last_build_date: "2026-04-01T00:00:00+00:00"
managing_editor: "contact@bankstatementparser.com"
pub_date: "2026-04-01T00:00:00+00:00"
ttl: "60"
type: "website"
webmaster: "contact@bankstatementparser.com"

# Apple - The Apple front matter (YAML).

apple_mobile_web_app_orientations: "portrait"
apple_touch_icon_sizes: "192x192"
apple-mobile-web-app-capable: "yes"
mobile-web-app-capable: "yes"
apple-mobile-web-app-status-bar-inset: "black"
apple-mobile-web-app-status-bar-style: "black-translucent"
apple-mobile-web-app-title: "Preguntas frecuentes sobre el analizador de extractos bancarios: privacidad, rendimiento y uso"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Respuestas a preguntas comunes sobre Bank Statement Parser: privacidad de datos, redacción de PII, rendimiento, compatibilidad con ISO 20022 y flujos de trabajo de tesorería."
twitter_image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logotipo de Bank Statement Parser, una potente herramienta Python diseñada para el procesamiento de datos financieros y la extracción de conocimientos de forma rápida y precisa."
twitter_site: "@wwdseb"
twitter_title: "Preguntas frecuentes sobre el analizador de extractos bancarios: privacidad, rendimiento y uso"
twitter_url: "https://bankstatementparser.com/es/faq/index.html"

# Humans.txt - The Humans.txt front matter (YAML).

author_website: "https://bankstatementparser.com"
author_twitter: "@wwdseb"
author_location: "London, UK"
thanks: "¡Gracias por leer!"
site_last_updated: "2026-04-01"
site_standards: "HTML5, CSS3, RSS, Atom, JSON, XML, YAML, Markdown, TOML"
site_components: "Shokunin SSG, Shokunin CLI, Shokunin Templates, Kaishi Templates, Kaishi Themes"
site_software: "Shokunin, Rust"

---

## Privacidad y cumplimiento de datos

### ¿Algún dato sale de mi infraestructura?

**No.** Bank Statement Parser funciona como una biblioteca sin estado. Todo el procesamiento (análisis, redacción de PII, extracción de archivos) se produce dentro de su memoria de ejecución local. Sin llamadas API, sin servicios en la nube, sin telemetría. Los analizadores XML están reforzados con`no_network=True`, bloqueando todo el acceso saliente en el nivel del analizador. Tus datos financieros nunca abandonan tu entorno.

### ¿Cómo funciona la redacción de PII?

Los campos confidenciales se enmascaran antes de que lleguen a la lógica de su aplicación. El analizador identifica los nombres de los deudores, los nombres de los acreedores, los IBAN y las direcciones postales, reemplazándolos con`***REDACTED***`en salida de consola y modo streaming.

- **La redacción está activada de forma predeterminada** en el modo de salida y transmisión CLI.
- **Las exportaciones de archivos** (CSV, JSON, Excel) conservan datos sin editar para su procesamiento posterior.
- **Suscribirse** para recibir datos completos con`--show-pii`en la CLI o`redact_pii=False`en la API.

### ¿El proceso de extracción es determinista?

**Sí, salida con bytes idénticos en cada ejecución.** Dado el mismo archivo de entrada, el analizador produce el mismo resultado cada vez. Sin aleatoriedad, sin inferencia de modelo, sin muestreo heurístico. CI impone el determinismo con 467 pruebas con una cobertura de sucursales del 100 %, incluida la fuzzing basada en propiedades a través de Hypothesis.

### ¿Qué estándares de cumplimiento sigue el proyecto?

El proyecto mantiene documentación alineada con ISO 13485 con trazabilidad completa:

- Un **Registro de Riesgos** cuantificado con puntuación de gravedad/probabilidad y evaluación de riesgos residuales.
- Un **Plan de verificación y validación** con 19 pasos cerrados en 5 fases.
- Un **Procedimiento de Control de Cambios** con evaluación de impacto y protocolos de reversión.
- Un **Registro SOUP** que cubre todas las dependencias con niveles de riesgo y seguimiento de EOL.
- Una **Matriz de Trazabilidad** para el diseño del mapeo de insumos para la implementación y verificación.

Cada versión incluye un SBOM CycloneDX, sumas de verificación SHA-256 y una certificación de procedencia de compilación de GitHub.

## Rendimiento y escalabilidad

### ¿Qué tan rápido es el analizador de extractos bancarios?

Los umbrales de rendimiento se validan en CI en cada confirmación:

| Métrico | Valor |
|---|---|
| Rendimiento de CAMT.053 | Más de 27.000 transacciones/segundo |
| Rendimiento de PAIN.001 | Más de 52.000 transacciones/segundo |
| Latencia por transacción (CAMT) | 37 microsegundos |
| Latencia por transacción (PAIN.001) | 19 microsegundos |
| Tiempo hasta el primer resultado | < 2 ms |

### ¿Cómo se manejan los archivos grandes?

**Transmisión con memoria limitada: probada con 50 000 transacciones por archivo.** Uso`parse_streaming()`para procesar archivos XML de forma incremental. Cada transacción se genera como un diccionario; Los elementos se borran después del procesamiento para evitar el crecimiento de la memoria. La memoria no escala con el tamaño del archivo: la prueba de transacciones de 50 000 (más de 25 MB) utiliza menos del doble de memoria que la prueba de transacciones de 10 000.

Para archivos que superan los 50 MB (por ejemplo, lotes PAIN.001 de host a host con pagos de más de 100 000), el analizador transmite a través de un archivo temporal con eliminación de espacios de nombres basada en fragmentos: el documento completo nunca se carga en la memoria.

### ¿Cómo se procesan de forma segura los archivos ZIP?

`iter_secure_xml_entries()`valida cada miembro antes de la extracción:

- **Límite de tamaño de entrada** (predeterminado 10 MB por entrada)
- **Límite de tamaño total sin comprimir** (predeterminado 50 MB)
- **Límite de relación de compresión** (predeterminado 100:1) para evitar bombas ZIP
- **Rechazo de entrada cifrado**

No se escribe ningún archivo en el disco. Los bytes XML pasan directamente al analizador a través de`from_bytes()`.

### ¿Puedo analizar varios archivos en paralelo?

**Sí.** Usar`parse_files_parallel()`que distribuye el trabajo en un`ProcessPoolExecutor`:

```python
from bankstatementparser import parse_files_parallel

results = parse_files_parallel([
    "statements/jan.xml",
    "statements/feb.xml",
    "statements/mar.xml",
])
for r in results:
    print(r.path, r.status, len(r.transactions), "rows")
```

## Formatos admitidos

### ¿Qué formatos de extractos bancarios son compatibles?

| Formato | Estándar | Tipos de archivos | Clase de analizador |
|---|---|---|---|
| CAMT.053 | Declaración de banco a cliente ISO 20022 | `.xml` | `CamtParser` |
| DOLOR.001 | Iniciación de transferencia de crédito ISO 20022 | `.xml` | `Pain001Parser` |
| CSV | Exportaciones bancarias genéricas | `.csv` | `CsvStatementParser` |
| OFX | Intercambio financiero abierto | `.ofx` | `OfxParser` |
| QFX | Acelerar el intercambio financiero | `.qfx` | `QfxParser` |
| MT940 | Estándar SWIFT | `.mt940`, `.sta` | `Mt940Parser` |

### ¿El analizador maneja dialectos específicos del banco de CAMT.053?

**Sí, independiente del espacio de nombres por diseño.** El analizador elimina los espacios de nombres XML antes de procesarlos, manejando cualquier variante CAMT.053 (`camt.053.001.02`, `camt.053.001.04`, o envoltorios bancarios propietarios) sin configuración específica del espacio de nombres. XPath consulta la estructura del elemento de destino, no los URI del espacio de nombres.

Para los bancos que envuelven CAMT en un sobre personalizado, utilice`from_string()`o`from_bytes()`para alimentar el documento interno directamente.

### ¿Puedo asignar encabezados de columna CSV personalizados al esquema estándar?

**Sí: normalización automática, configuración cero.**`CsvStatementParser`reconoce variaciones comunes de encabezado:`"Date"`, `"Transaction Date"`, `"Booking Date"`todo el mapa al`date`campo.`"Amount"`, `"Value"`, `"Sum"`mapa a`amount`. Dividir columnas de crédito/débito (p. ej.,`"Credit"`y`"Debit"`) se detectan y combinan en una única cantidad firmada automáticamente.

### ¿Cuál es el formato de salida?

Todos los analizadores producen DataFrames pandas estandarizados con tipos de columnas consistentes:

| Formato | Columnas clave |
|---|---|
| **CAMT** | `Amount`, `Currency`, `DrCr`, `Debtor`, `Creditor`, `Reference`, `ValDt`, `BookgDt`, `AccountId` |
| **DOLOR.001** | `PmtInfId`, `PmtMtd`, `InstdAmt`, `Currency`, `CdtrNm`, `EndToEndId`, `MsgId`, `CreDtTm`, `NbOfTxs` |
| **CSV/OFX/QFX/MT940** | `date`, `description`, `amount`(normalizado) |

También puede exportar a CSV, JSON, Excel o convertir a Polars DataFrames.

## Flujos de trabajo de tesorería

### ¿Cómo maneja el analizador los extractos multidivisa?

**Cada transacción conserva su moneda original, sin conversión implícita.** El`Currency`El campo se extrae del XML.`Ccy`atributo por transacción. Los estados de cuenta multidivisa permanecen como están. El`get_account_balances()`El método devuelve saldos de apertura y cierre por cuenta con códigos de moneda originales. La conciliación entre divisas se deja a su lógica descendente, donde usted controla la fuente del tipo de cambio.

### ¿El analizador admite formatos entrantes y salientes?

**Sí.**`Pain001Parser`maneja archivos de inicio de transferencia de crédito ISO 20022 PAIN.001 (pagos salientes).`CamtParser`maneja archivos de extractos de banco a cliente CAMT.053 (informes entrantes). Ambos admiten transmisión, redacción de PII y exportación a CSV, JSON y Excel. Usar`detect_statement_format()`para identificar el formato automáticamente.

### ¿Qué sucede cuando la entrada de una transacción tiene un formato incorrecto?

El comportamiento depende del modo de análisis:

- **`parse()`(modo por lotes)**: a las entradas con formato incorrecto les faltan campos obligatorios (`Amount`, `Currency`, o`CdtDbtInd`) se omiten con un registro de advertencia. El resto de la declaración se analiza normalmente.
- **`parse_streaming()`(modo de transmisión)**: los errores de análisis se propagan inmediatamente como excepciones. Sin pérdida de datos silenciosa. Este comportamiento a prueba de fallas es intencional para los flujos de trabajo financieros donde se debe contabilizar cada transacción.

### ¿Cómo funciona la deduplicación?

El`Deduplicator`La clase detecta duplicados exactos y coincidencias sospechosas con puntuaciones de confianza explicables:

```python
from bankstatementparser import CamtParser, Deduplicator

parser = CamtParser("statement.xml")
dedup = Deduplicator()
result = dedup.deduplicate(dedup.from_dataframe(parser.parse()))

print(f"Unique: {len(result.unique_transactions)}")
print(f"Exact duplicates: {len(result.exact_duplicates)}")
print(f"Suspected matches: {len(result.suspected_matches)}")
```

## Instalación y compatibilidad

### ¿Cómo instalo Bank Statement Parser?

```bash
pip install bankstatementparser
```

Para soporte opcional de Polars DataFrame:

```bash
pip install bankstatementparser[polars]
```

### ¿Qué versiones de Python son compatibles?

Python 3.9 a 3.14. Todas las versiones se prueban en CI con 467 pruebas con una cobertura de sucursales del 100%.

### ¿Cuáles son las dependencias?

La biblioteca tiene 5 dependencias directas:

- `lxml`-- Análisis XML con refuerzo de seguridad
-`pandas`-- DataFrames y manipulación de datos
-`openpyxl`- Exportación de Excel
-`pydantic`-- Validación de datos y modelos.
-`defusedxml`-- Protección XXE

Todas las dependencias tienen versiones con bloqueo hash SHA-256. El SBOM CycloneDX asigna cada componente de tiempo de ejecución.

### ¿Funciona en macOS, Linux y Windows?

**Sí.** La biblioteca funciona en macOS, Linux y Windows (a través de WSL). No tiene dependencias específicas de la plataforma.

## Reproducibilidad y seguridad

### ¿Cómo puedo verificar la reproducibilidad?

```bash
python -m pytest                              # 467 tests, 100% branch coverage
python scripts/verify_locked_hashes.py        # SHA-256 hash verification
git log --show-signature -1                   # Verify commit signature
```

### ¿Qué protecciones de seguridad están integradas?

- **Protección XXE**:`resolve_entities=False`, `no_network=True`, `load_dtd=False`
- **ZIP Bomb Protection**: Límites de relación de compresión, límites de tamaño de entrada, rechazo de entrada cifrado
- **Prevención de recorrido de ruta**: lista de bloqueo de patrones peligrosos y resolución de enlaces simbólicos
- **Validación de entrada**: límites de tamaño de archivo (100 MB predeterminado), validación de extensión/formato
- **Cadena de suministro**: dependencias con bloqueo de hash SHA-256, CycloneDX SBOM, certificación de procedencia de compilación
- **Compromisos firmados**: aplicado en CI

### ¿Cómo se compara Bank Statement Parser con pyiso20022?

pyiso20022 es un amplio conjunto de herramientas ISO 20022 que genera clases de datos de Python a partir de esquemas ISO XML. Cubre una amplia gama de tipos de mensajes ISO 20022 (PACS, PAIN, CAMT, ADMI) con validación de esquema. Bank Statement Parser está diseñado específicamente para el análisis de extractos bancarios con soporte de transmisión, redacción de PII, deduplicación y una API unificada en seis formatos, incluidos formatos que no son ISO (CSV, OFX, QFX, MT940). Si necesita analizar extractos bancarios en DataFrames con seguridad de nivel de producción, utilice Bank Statement Parser. Si necesita trabajar con el catálogo completo de mensajes ISO 20022, utilice pyiso20022.

### ¿Cuáles son los plazos de migración de SWIFT ISO 20022?

SWIFT ha publicado un cronograma de migración por fases:

- **Noviembre de 2026**: las direcciones estructuradas e híbridas se vuelven obligatorias. Se rechazarán los mensajes de múltiples instrucciones MT101. Comienza la Fase 1 de Gestión de Casos.
- **Noviembre de 2027**: Todas las instituciones financieras deben poder recibir estados de cuenta CAMT.053 de forma nativa. SWIFT dejará de convertir MT a formato ISO.
- **Noviembre de 2028**: Retiro total de MT940, MT942, MT950, MT900 y MT910. Estos serán reemplazados por los equivalentes CAMT.052, CAMT.053 y CAMT.054.

Bank Statement Parser admite tanto el formato MT940 heredado como los formatos modernos CAMT.053/PAIN.001, lo que lo hace ideal para el período de transición.

