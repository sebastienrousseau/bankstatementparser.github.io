---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Preguntas frecuentes sobre el analizador de extractos bancarios"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Analizador de extractos bancarios. Reservados todos los derechos."
date: "Apr 11, 2026"
description: "Respuestas a preguntas comunes sobre Bank Statement Parser: privacidad de datos, redacción de PII, rendimiento, compatibilidad con ISO 20022, transmisión, cumplimiento y flujos de trabajo de tesorería."
download: ""
format-detection: "telephone=no"
hreflang: "es"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/es/faq/index.html"
image_alt: "Logotipo de Bank Statement Parser, una potente herramienta Python diseñada para el procesamiento de datos financieros y la extracción de conocimientos de forma rápida y precisa."
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "Preguntas frecuentes sobre el analizador de extractos bancarios, preguntas sobre el analizador CAMT, preguntas frecuentes sobre PAIN.001, preguntas frecuentes sobre Python ISO 20022, redacción de PII bancaria, rendimiento del analizador bancario, privacidad de datos financieros, preguntas frecuentes sobre el analizador MT940, analizador de streaming en Python, cumplimiento de extractos bancarios"
language: "es-ES"
layout: "faq"
locale: "es_ES"
logo_alt: "Logotipo de Bank Statement Parser, una potente herramienta Python diseñada para el procesamiento de datos financieros y la extracción de conocimientos de forma rápida y precisa."
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
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
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Respuestas a preguntas comunes sobre Bank Statement Parser: privacidad de datos, redacción de PII, rendimiento, compatibilidad con ISO 20022 y flujos de trabajo de tesorería."
twitter_image: "/images/logos/bankstatementparser.webp"
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

## Privacidad de datos y cumplimiento

### ¿Algún dato sale de mi infraestructura?

**No — ni siquiera para la extracción de PDF.** Bank Statement Parser funciona como una biblioteca sin estado. Todo el procesamiento — análisis, redacción de PII, extracción de archivos — se produce dentro de la memoria de ejecución local. El pipeline híbrido para PDF usa Ollama para inferencia local de LLM — sin APIs en la nube. Los analizadores XML están reforzados con `no_network=True`, bloqueando todo acceso saliente a nivel de analizador. Sus datos financieros nunca salen de su entorno.

### ¿Cómo funciona la redacción de PII?

Los campos sensibles se enmascaran antes de llegar a la lógica de su aplicación. El analizador identifica nombres de deudores, nombres de acreedores, IBANs y direcciones postales, reemplazándolos con `***REDACTED***` en la salida de consola y en modo streaming.

- **La redacción está activada por defecto** en la salida CLI y en modo streaming.
- **Las exportaciones de archivos** (CSV, JSON, Excel) conservan datos sin redactar para procesamiento posterior.
- **Active** los datos completos con `--show-pii` en la CLI o `redact_pii=False` en la API.

### ¿El proceso de extracción es determinista?

**Sí para formatos estructurados — salida byte a byte idéntica en cada ejecución.** Dado el mismo archivo de entrada, los analizadores deterministas (CAMT, PAIN.001, CSV, OFX, QFX, MT940) producen el mismo resultado cada vez. Sin aleatoriedad, sin inferencia de modelo, sin muestreo heurístico.

Para el pipeline híbrido de PDF, las rutas de extracción basadas en LLM pueden producir variaciones menores entre ejecuciones. Por eso cada extracción de PDF se verifica con la **Regla de Oro** (`opening + credits − debits == closing`) y las discrepancias marcadas pueden revisarse de forma interactiva.

CI impone el determinismo con 718 pruebas y cobertura de ramas del 100%, incluyendo fuzzing basado en propiedades vía Hypothesis.

### ¿Qué estándares de cumplimiento sigue el proyecto?

El proyecto mantiene documentación alineada con ISO 13485 con trazabilidad completa:

- Un **Registro de riesgos** cuantificado con puntuación de gravedad/probabilidad y evaluación de riesgo residual.
- Un **Plan de verificación y validación** con 19 pasos controlados en 5 fases.
- Un **Procedimiento de control de cambios** con evaluación de impacto y protocolos de reversión.
- Un **Registro SOUP** que cubre todas las dependencias con niveles de riesgo y seguimiento de fin de vida.
- Una **Matriz de trazabilidad** que mapea entradas de diseño a implementación y verificación.

Cada versión incluye un SBOM CycloneDX, sumas de verificación SHA-256 y certificación de procedencia de compilación de GitHub.

## Rendimiento y escalabilidad

### ¿Qué tan rápido es Bank Statement Parser?

Los umbrales de rendimiento se validan en CI en cada commit:

| Métrica | Valor |
|---|---|
| Rendimiento CAMT.053 | 27.000+ transacciones/segundo |
| Rendimiento PAIN.001 | 52.000+ transacciones/segundo |
| Latencia por transacción (CAMT) | 37 microsegundos |
| Latencia por transacción (PAIN.001) | 19 microsegundos |
| Tiempo hasta el primer resultado | < 2 ms |

La velocidad de extracción de PDF depende de la ruta: determinista (menos de un segundo), texto-LLM (segundos), visión-LLM (segundos por página).

### ¿Cómo se manejan los archivos grandes?

**Streaming con memoria acotada — probado con 50.000 transacciones por archivo.** Use `parse_streaming()` para procesar archivos XML de forma incremental. Cada transacción se genera como un diccionario; los elementos se liberan tras el procesamiento para evitar crecimiento de memoria. La memoria no escala con el tamaño del archivo — la prueba de 50K transacciones (más de 25 MB) usa menos del doble de memoria que la prueba de 10K.

Para archivos que superan los 50 MB (p. ej., lotes PAIN.001 host-to-host con más de 100K pagos), el analizador transmite a través de un archivo temporal con eliminación de namespaces por fragmentos — el documento completo nunca se carga en memoria.

### ¿Cómo se procesan de forma segura los archivos ZIP?

`iter_secure_xml_entries()` valida cada miembro antes de la extracción:

- **Límite de tamaño de entrada** (10 MB por defecto por entrada)
- **Límite de tamaño total sin comprimir** (50 MB por defecto)
- **Límite de ratio de compresión** (100:1 por defecto) para prevenir ZIP bombs
- **Rechazo de entradas cifradas**

No se escribe ningún archivo en disco. Los bytes XML pasan directamente al analizador vía `from_bytes()`.

### ¿Puedo analizar varios archivos en paralelo?

**Sí.** Use `parse_files_parallel()` que distribuye el trabajo en un `ProcessPoolExecutor`:

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

Para ingesta masiva de PDF, use `scan_and_ingest()` que procesa árboles de carpetas completos con deduplicación automática.

## Formatos admitidos

### ¿Qué formatos de extractos bancarios son compatibles?

| Formato | Estándar | Tipos de archivo | Analizador/Método |
|---|---|---|---|
| CAMT.053 | ISO 20022 Extracto banco-a-cliente | `.xml` | `CamtParser` |
| PAIN.001 | ISO 20022 Iniciación de transferencia de crédito | `.xml` | `Pain001Parser` |
| CSV | Exportaciones bancarias genéricas | `.csv` | `CsvStatementParser` |
| OFX | Open Financial Exchange | `.ofx` | `OfxParser` |
| QFX | Quicken Financial Exchange | `.qfx` | `QfxParser` |
| MT940 | Estándar SWIFT | `.mt940`, `.sta` | `Mt940Parser` |
| PDF | Extractos digitales y escaneados | `.pdf` | `smart_ingest()` |

### ¿Cómo funciona el pipeline híbrido para PDF?

El pipeline híbrido (v0.0.5+) enruta los PDF de forma inteligente por tres rutas de extracción:

- **Ruta A (Determinista)**: Tablas PDF estructuradas analizadas directamente — gratis, la más rápida, sin necesidad de LLM.
- **Ruta B (Texto-LLM)**: PDFs digitales con diseños complejos extraídos mediante LLM local (LiteLLM/Ollama).
- **Ruta C (Visión-LLM)**: Extractos escaneados o fotocopiados procesados con modelos de visión multimodal.

Cada extracción se verifica con la Regla de Oro (`opening + credits − debits == closing`). Las discrepancias pueden revisarse de forma interactiva con `--type review`.

### ¿El analizador maneja dialectos específicos de banco de CAMT.053?

**Sí — independiente del namespace por diseño.** El analizador elimina los namespaces XML antes del procesamiento, manejando cualquier variante de CAMT.053 (`camt.053.001.02`, `camt.053.001.04`, o envolturas propietarias de bancos) sin configuración específica de namespace. Las consultas XPath apuntan a la estructura de elementos, no a URIs de namespace.

Para bancos que envuelven CAMT en un sobre personalizado, use `from_string()` o `from_bytes()` para alimentar el documento interno directamente.

### ¿Puedo mapear encabezados de columna CSV personalizados al esquema estándar?

**Sí — normalización automática, configuración cero.** `CsvStatementParser` reconoce variaciones comunes de encabezado: `"Date"`, `"Transaction Date"`, `"Booking Date"` se mapean al campo `date`. `"Amount"`, `"Value"`, `"Sum"` se mapean a `amount`. Las columnas separadas de crédito/débito (p. ej., `"Credit"` y `"Debit"`) se detectan y combinan en un único importe con signo automáticamente.

### ¿Cuál es el formato de salida?

Todos los analizadores producen pandas DataFrames estandarizados con tipos de columna consistentes:

| Formato | Columnas clave |
|---|---|
| **CAMT** | `Amount`, `Currency`, `DrCr`, `Debtor`, `Creditor`, `Reference`, `ValDt`, `BookgDt`, `AccountId` |
| **PAIN.001** | `PmtInfId`, `PmtMtd`, `InstdAmt`, `Currency`, `CdtrNm`, `EndToEndId`, `MsgId`, `CreDtTm`, `NbOfTxs` |
| **CSV/OFX/QFX/MT940** | `date`, `description`, `amount` (normalizado) |

También puede exportar a CSV, JSON, Excel, Polars DataFrames, hledger o formato de diario beancount.

## Funcionalidades de PDF y LLM

### ¿Qué modelos LLM admite el pipeline híbrido?

El pipeline usa LiteLLM como capa de abstracción de modelos, con un puente directo a Ollama para prompts de visión. Modelos recomendados:

- **Extracción de texto**: Cualquier modelo compatible con LiteLLM (local o remoto).
- **Extracción por visión**: `ollama/minicpm-v` (recomendado) para PDFs escaneados.
- **Categorización**: Cualquier modelo compatible con LiteLLM.

Todos los modelos pueden ejecutarse 100% en local vía Ollama — no se necesitan claves de API.

### ¿Qué es la verificación de la Regla de Oro?

Cada extracción de PDF se verifica con la ecuación: `opening balance + credits − debits == closing balance`. Los resultados se etiquetan como:

- **VERIFIED**: Los saldos coinciden exactamente.
- **DISCREPANCY**: Los saldos no coinciden — se recomienda revisión.
- **FAILED**: No se pudo realizar la verificación (faltan datos de saldo).

### ¿Puedo categorizar transacciones automáticamente?

**Sí.** El módulo de enriquecimiento (v0.0.6+) ofrece categorización de transacciones con LLM:

```python
from bankstatementparser.enrichment import Categorizer

categorizer = Categorizer()
enriched = categorizer.categorize_batch(transactions)
```

El esquema por defecto usa 13 categorías compatibles con Plaid. Puede proporcionar su propio esquema de categorías.

### ¿Puedo exportar a hledger o beancount?

**Sí** (v0.0.8+). Exporte transacciones a formatos de diario de contabilidad en texto plano con mapeo de cuentas:

```python
from bankstatementparser.export import to_hledger, to_beancount

journal = to_hledger(transactions, account="Assets:Bank:Checking")
```

## Flujos de trabajo de tesorería

### ¿Cómo maneja el analizador los extractos multidivisa?

**Cada transacción conserva su divisa original — sin conversión implícita.** El campo `Currency` se extrae del atributo XML `Ccy` por transacción. Los extractos multidivisa permanecen tal cual. El método `get_account_balances()` devuelve saldos de apertura y cierre por cuenta con códigos de divisa originales.

Desde v0.0.8, `verify_balance_multi_currency()` agrupa transacciones por divisa y ejecuta la Regla de Oro de forma independiente por grupo — útil para cuentas que mantienen varias divisas.

### ¿El analizador admite formatos entrantes y salientes?

**Sí.** `Pain001Parser` maneja archivos de iniciación de transferencia de crédito ISO 20022 PAIN.001 (pagos salientes). `CamtParser` maneja archivos de extractos banco-a-cliente CAMT.053 (informes entrantes). Ambos admiten streaming, redacción de PII y exportación a CSV, JSON, Excel, hledger y beancount. Use `detect_statement_format()` para identificar el formato automáticamente.

### ¿Qué sucede cuando una entrada de transacción tiene formato incorrecto?

El comportamiento depende del modo de análisis:

- **`parse()` (modo por lotes)** -- Las entradas con formato incorrecto a las que les faltan campos obligatorios (`Amount`, `Currency` o `CdtDbtInd`) se omiten con un registro de advertencia. El resto del extracto se analiza normalmente.
- **`parse_streaming()` (modo streaming)** -- Los errores de análisis se propagan inmediatamente como excepciones. Sin pérdida silenciosa de datos. Este comportamiento fail-fast es intencional para flujos financieros donde cada transacción debe contabilizarse.
- **`smart_ingest()` (PDF híbrido)** -- Los errores de extracción se capturan en el `IngestResult` con estado de verificación, permitiendo revisión interactiva.

### ¿Cómo funciona la deduplicación?

A cada transacción se le asigna un `transaction_hash` idempotente (huella MD5) basado en sus campos clave. Esto permite ingesta incremental segura — reprocesar el mismo archivo produce los mismos hashes, por lo que los duplicados se detectan automáticamente.

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
# Core install (deterministic parsers only)
pip install bankstatementparser

# PDF hybrid pipeline
pip install 'bankstatementparser[hybrid]'         # Text-LLM path
pip install 'bankstatementparser[hybrid-vision]'   # Vision-LLM path

# Extras
pip install 'bankstatementparser[enrichment]'      # Transaction categorisation
pip install 'bankstatementparser[api]'             # REST API microservice
pip install 'bankstatementparser[polars]'          # Polars DataFrame support
```

### ¿Qué versiones de Python son compatibles?

Python 3.10 a 3.14. El soporte para Python 3.9 se eliminó en v0.0.6 (EOL 2025-10-31). Todas las versiones se prueban en CI con 718 pruebas y cobertura de ramas del 100%.

### ¿Cuáles son las dependencias?

La biblioteca principal tiene 5 dependencias directas:

- `lxml` -- Análisis XML con refuerzo de seguridad
- `pandas` -- DataFrames y manipulación de datos
- `openpyxl` -- Exportación a Excel
- `pydantic` -- Validación de datos y modelos
- `defusedxml` -- Protección XXE

Los extras opcionales añaden: `litellm`, `pypdf`, `pdfplumber`, `pypdfium2`, `fastapi`, `uvicorn`, `polars`.

Todas las dependencias tienen versiones con bloqueo hash SHA-256. El SBOM CycloneDX mapea cada componente en tiempo de ejecución.

### ¿Funciona en macOS, Linux y Windows?

**Sí.** La biblioteca funciona en macOS, Linux y Windows (vía WSL). No tiene dependencias específicas de plataforma.

### ¿Hay una REST API?

**Sí** (v0.0.8+). Instale con `pip install 'bankstatementparser[api]'` y ejecute:

```bash
bankstatementparser-api --port 8000
```

Endpoints: `POST /ingest` (analizar un extracto) y `GET /health` (comprobación de estado).

## Reproducibilidad y seguridad

### ¿Cómo puedo verificar la reproducibilidad?

```bash
python -m pytest                              # 718 tests, 100% branch coverage
python scripts/verify_locked_hashes.py        # SHA-256 hash verification
git log --show-signature -1                   # Verify commit signature
```

### ¿Qué protecciones de seguridad están integradas?

- **Protección XXE**: `resolve_entities=False`, `no_network=True`, `load_dtd=False`
- **Protección contra ZIP Bomb**: Límites de ratio de compresión, límites de tamaño de entrada, rechazo de entradas cifradas
- **Prevención de cruce de rutas**: Lista de bloqueo de patrones peligrosos y resolución de enlaces simbólicos
- **Validación de entrada**: Límites de tamaño de archivo (100 MB por defecto), validación de extensión/formato
- **Cadena de suministro**: Dependencias con bloqueo hash SHA-256, CycloneDX SBOM, certificación de procedencia de compilación
- **Commits firmados**: Aplicado en CI
- **LLMs locales**: El pipeline híbrido para PDF usa Ollama — sin llamadas a APIs en la nube

### ¿Cómo se compara Bank Statement Parser con pyiso20022?

pyiso20022 es un amplio kit de herramientas ISO 20022 que genera dataclasses de Python a partir de esquemas XML ISO. Cubre una amplia gama de tipos de mensajes ISO 20022 (PACS, PAIN, CAMT, ADMI) con validación de esquemas. Bank Statement Parser está diseñado específicamente para el análisis de extractos bancarios con soporte híbrido para PDF, verificación de saldo, enriquecimiento, exportación contable y una API unificada en siete formatos, incluyendo formatos no-ISO (CSV, OFX, QFX, MT940, PDF). Si necesita analizar extractos bancarios en DataFrames con seguridad de nivel de producción, use Bank Statement Parser. Si necesita trabajar con el catálogo completo de mensajes ISO 20022, use pyiso20022.

### ¿Cuáles son los plazos de migración de SWIFT ISO 20022?

SWIFT ha publicado un cronograma de migración por fases:

- **Noviembre de 2026**: Las direcciones estructuradas e híbridas se vuelven obligatorias. Se rechazarán los mensajes de múltiples instrucciones MT101. Comienza la Fase 1 de Gestión de Casos.
- **Noviembre de 2027**: Todas las instituciones financieras deben poder recibir extractos CAMT.053 de forma nativa. SWIFT dejará de convertir formato MT a ISO.
- **Noviembre de 2028**: Retiro total de MT940, MT942, MT950, MT900 y MT910. Serán reemplazados por los equivalentes CAMT.052, CAMT.053 y CAMT.054.

Bank Statement Parser admite tanto el formato heredado MT940 como los formatos modernos CAMT.053/PAIN.001, lo que lo hace ideal para el período de transición.
