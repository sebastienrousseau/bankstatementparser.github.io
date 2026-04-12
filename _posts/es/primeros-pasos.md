---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Un edificio blanco con ventanas negras."
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/daniele-franchi-Vl6YuVBLEys.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Analizador de extractos bancarios. Reservados todos los derechos."
date: "Apr 11, 2026"
description: "Comience con Bank Statement Parser para Python: instale, analice archivos CAMT/PAIN.001/CSV/OFX/QFX/MT940 y utilice flujos de trabajo CLI o streaming."
download: ""
format-detection: "telephone=no"
hreflang: "es"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/es/primeros-pasos/index.html"
image_alt: "Logotipo de Bank Statement Parser, una potente herramienta Python diseñada para el procesamiento de datos financieros y la extracción de conocimientos de forma rápida y precisa."
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "analizador de extractos bancarios, introducción, python, CAMT, PAIN.001, CSV, OFX, QFX, MT940, datos financieros"
language: "es-ES"
layout: "start"
locale: "es_ES"
logo_alt: "Logotipo de Bank Statement Parser, una potente herramienta Python diseñada para el procesamiento de datos financieros y la extracción de conocimientos de forma rápida y precisa."
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Empezando"
permalink: "https://bankstatementparser.com/es/primeros-pasos/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Comience a crear aplicaciones seguras con Bank Statement Parser"
tags: "banco, extracto, analizador, python, camt, dolor001, csv, ofx, qfx, mt940, streaming, cli"
theme_color: "rgb(73, 214, 251)"
title: "Analizador de extractos bancarios: guía de instalación y uso"
url: "https://bankstatementparser.com/es/primeros-pasos/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/es/primeros-pasos/rss.xml"
category: "Software financiero, biblioteca Python, guía para desarrolladores"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Comience con Bank Statement Parser para Python: instale, analice archivos CAMT/PAIN.001/CSV/OFX/QFX/MT940 y utilice flujos de trabajo CLI o streaming."
item_guid: "https://bankstatementparser.com/es/primeros-pasos/rss.xml"
item_link: "https://bankstatementparser.com/es/primeros-pasos/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Analizador de extractos bancarios: guía de instalación y uso"
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
apple-mobile-web-app-title: "Analizador de extractos bancarios: guía de instalación y uso"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Instale y utilice Bank Statement Parser para analizar archivos CAMT, PAIN.001, CSV, OFX/QFX y MT940 en Python."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logotipo de Bank Statement Parser, una potente herramienta Python diseñada para el procesamiento de datos financieros y la extracción de conocimientos de forma rápida y precisa."
twitter_site: "@wwdseb"
twitter_title: "Analizador de extractos bancarios: guía de instalación y uso"
twitter_url: "https://bankstatementparser.com/es/primeros-pasos/index.html"

# Humans.txt - The Humans.txt front matter (YAML).

author_website: "https://bankstatementparser.com"
author_twitter: "@wwdseb"
author_location: "London, UK"
thanks: "¡Gracias por leer!"
site_last_updated: "2026-04-01"
site_standards: "HTML5, CSS3, RSS, Atom, JSON, XML, YAML, Markdown, TOML"
site_components: "Shokunin SSG, Shokunin CLI, Shokunin Templates, Shokunin Themes, Kaishi SSG, Kaishi CLI, Kaishi Templates, Kaishi Themes"
site_software: "Shokunin, Rust"

---

## Requisitos

- Python 3.10 a 3.14
- Acceso a terminal (macOS, Linux o WSL)

## Instalar

```bash
# Core install (deterministic parsers only)
pip install bankstatementparser
```

Extras opcionales para funcionalidades adicionales:

```bash
# Text-LLM path for digital PDFs (litellm + pypdf)
pip install 'bankstatementparser[hybrid]'

# Higher-fidelity table extraction (adds pdfplumber)
pip install 'bankstatementparser[hybrid-plus]'

# Vision-LLM path for scanned PDFs (adds pypdfium2)
pip install 'bankstatementparser[hybrid-vision]'

# LLM-powered transaction categorisation
pip install 'bankstatementparser[enrichment]'

# REST API microservice (FastAPI + uvicorn)
pip install 'bankstatementparser[api]'

# Optional Polars DataFrame support
pip install 'bankstatementparser[polars]'
```

## Inicio rápido

### Detectar y analizar cualquier formato estructurado

```python
from bankstatementparser import create_parser, detect_statement_format

fmt = detect_statement_format("transactions.ofx")
parser = create_parser("transactions.ofx", fmt)
df = parser.parse()  # pandas DataFrame
print(df.head())
```

Funciona con archivos `.xml` (CAMT/PAIN.001), `.csv`, `.ofx`, `.qfx`, `.mt940` y `.sta`.

### Analizar CAMT.053

```python
from bankstatementparser import CamtParser

parser = CamtParser("statement.xml")
transactions = parser.parse()
```

### Analizar PAIN.001

```python
from bankstatementparser import Pain001Parser

parser = Pain001Parser("payment.xml")
payments = parser.parse()
```

### Analizar extractos bancarios en PDF (pipeline híbrido)

El pipeline híbrido enruta los PDF de forma inteligente por tres rutas de extracción:

```python
from bankstatementparser.hybrid import smart_ingest

result = smart_ingest("statement.pdf")
print(result.source_method)         # "deterministic" | "llm" | "vision"
print(result.verification.status)   # VERIFIED | DISCREPANCY | FAILED
print(result.transactions)          # List of extracted transactions
```

Cada extracción se verifica con la **Regla de Oro**: `opening + credits − debits == closing`.

## Streaming de archivos grandes

Para archivos con miles de transacciones, use streaming para mantener la memoria acotada:

```python
parser = CamtParser("large_statement.xml")
for transaction in parser.parse_streaming(redact_pii=True):
    process(transaction)  # Memory stays constant
```

## Análisis en memoria

Analice desde bytes sin E/S de disco — útil para flujos de trabajo SFTP o API:

```python
xml_bytes = download_from_sftp()
parser = CamtParser.from_bytes(xml_bytes, source_name="daily.xml")
transactions = parser.parse()
```

## Procesamiento paralelo de archivos

Analice varios archivos de forma concurrente:

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

## Escaneo masivo de directorios

Procese árboles de carpetas completos con deduplicación automática:

```python
from bankstatementparser.hybrid import scan_and_ingest

batch = scan_and_ingest("statements/2026/", pattern="**/*.pdf")
print(f"Processed: {len(batch.results)} files")
print(f"Unique transactions: {batch.unique_count}")
```

## Deduplicación

Hashes de transacción idempotentes para ingesta incremental segura:

```python
from bankstatementparser import CamtParser, Deduplicator

parser = CamtParser("statement.xml")
dedup = Deduplicator()
result = dedup.deduplicate(dedup.from_dataframe(parser.parse()))

print(f"Unique: {len(result.unique_transactions)}")
print(f"Exact duplicates: {len(result.exact_duplicates)}")
print(f"Suspected matches: {len(result.suspected_matches)}")
```

## Categorización de transacciones (enriquecimiento)

Categorice transacciones automáticamente con clasificación basada en LLM:

```python
from bankstatementparser.enrichment import Categorizer

categorizer = Categorizer()
enriched = categorizer.categorize_batch(transactions)
for txn in enriched:
    print(f"{txn.description}: {txn.category}")
```

## Exportación contable (hledger / beancount)

Exporte transacciones a formatos de diario de contabilidad en texto plano:

```python
from bankstatementparser.export import to_hledger, to_beancount

journal = to_hledger(transactions, account="Assets:Bank:Checking")
beancount_journal = to_beancount(transactions, account="Assets:Bank:Checking")
```

## Verificación de saldo multidivisa

Verifique saldos de forma independiente por grupo de divisa:

```python
from bankstatementparser.hybrid import verify_balance_multi_currency

results = verify_balance_multi_currency(transactions)
for currency, verification in results.items():
    print(f"{currency}: {verification.status}")
```

## REST API

Despliegue como microservicio FastAPI:

```bash
# Start the API server
bankstatementparser-api --port 8000

# For container deployments
bankstatementparser-api --host 0.0.0.0 --port 9000
```

Endpoints:
- `POST /ingest` -- Analizar un archivo de extracto bancario
- `GET /health` -- Comprobación de estado

## Procesamiento ZIP seguro

Procese archivos XML comprimidos con controles de seguridad integrados (protección contra bombas, rechazo de entradas cifradas):

```python
from bankstatementparser import iter_secure_xml_entries, CamtParser

for entry in iter_secure_xml_entries("statements.zip"):
    parser = CamtParser.from_bytes(entry.xml_bytes, source_name=entry.source_name)
    print(f"{entry.source_name}: {len(parser.parse())} transactions")
```

## Exportar

```python
parser = CamtParser("statement.xml")
parser.export_csv("output.csv")
parser.export_json("output.json")

# Polars (requires bankstatementparser[polars])
polars_df = parser.to_polars()

# Excel
parser.camt_to_excel("output.xlsx")
```

## Uso de CLI

```bash
# Parse structured formats
bankstatementparser --type camt --input statement.xml
bankstatementparser --type pain001 --input payment.xml

# Hybrid PDF pipeline
bankstatementparser --type ingest --input statement.pdf
bankstatementparser --type ingest --input statement.pdf --output ledger.csv

# Interactive review mode
bankstatementparser --type review --input result.json
bankstatementparser --type review --input result.json --output reviewed.json

# Export to CSV with streaming
bankstatementparser --type camt --input statement.xml --output transactions.csv
bankstatementparser --type camt --input statement.xml --streaming --show-pii
```

Opciones de CLI:

- `--type {camt,pain001,ingest,review}` -- tipo de analizador o modo
- `--input <path>` -- archivo de entrada
- `--output <path>` -- archivo de exportación (CSV o JSON)
- `--streaming` -- streaming de archivos grandes
- `--show-pii` -- mostrar campos sensibles (redactados por defecto)
- `--max-size <MB>` -- límite de tamaño de archivo

## Configuración de desarrollo local

```bash
git clone https://github.com/sebastienrousseau/bankstatementparser.git
cd bankstatementparser
python3 -m venv .venv && source .venv/bin/activate
pip install poetry && poetry install --with dev
make install-hooks   # pre-commit hook runs `make verify` before every commit
```

Ejecute el conjunto de pruebas:

```bash
pytest
```

## Referencia de API

### Clases de analizador

| Clase | Formato | Import |
|---|---|---|
| `CamtParser` | CAMT.053 (ISO 20022) | `from bankstatementparser import CamtParser` |
| `Pain001Parser` | PAIN.001 (ISO 20022) | `from bankstatementparser import Pain001Parser` |
| `CsvStatementParser` | CSV | `from bankstatementparser import CsvStatementParser` |
| `OfxParser` | OFX | `from bankstatementparser import OfxParser` |
| `QfxParser` | QFX | `from bankstatementparser import QfxParser` |
| `Mt940Parser` | MT940 | `from bankstatementparser import Mt940Parser` |
| `smart_ingest()` | PDF (pipeline híbrido) | `from bankstatementparser.hybrid import smart_ingest` |

### Funciones de utilidad

| Función | Propósito |
|---|---|
| `detect_statement_format(path)` | Detectar formato de archivo automáticamente |
| `create_parser(path, fmt)` | Crear el analizador apropiado |
| `parse_files_parallel(paths)` | Analizar varios archivos de forma concurrente |
| `iter_secure_xml_entries(zip_path)` | Iterar entradas ZIP de forma segura |
| `smart_ingest(path)` | Extracción híbrida de PDF con verificación |
| `scan_and_ingest(dir, pattern)` | Escaneo masivo de directorios |
| `verify_balance_multi_currency(txns)` | Verificación de saldo por divisa |
| `to_hledger(txns, account)` | Exportar a formato de diario hledger |
| `to_beancount(txns, account)` | Exportar a formato de diario beancount |

### Clases de datos

| Clase | Propósito |
|---|---|
| `Deduplicator` | Detectar transacciones duplicadas |
| `DeduplicationResult` | Resultado con coincidencias únicas, exactas y sospechosas |
| `InputValidator` | Validar rutas y formatos de archivos |
| `Transaction` | Registro de transacción normalizado |
| `FileResult` | Resultado del análisis paralelo |
| `ZipXMLSource` | Envoltorio de miembros ZIP |
| `IngestResult` | Resultado del pipeline híbrido con verificación |
| `VerificationResult` | Resultado de la verificación de saldo |
| `Categorizer` | Categorización de transacciones con LLM |
| `AccountMapper` | Reglas de mapeo de cuentas basadas en regex |

### Excepciones

| Excepción | Cuándo se lanza |
|---|---|
| `ParserError` | Fallos de análisis |
| `ExportError` | Fallos de exportación (CSV/JSON/Excel) |
| `ValidationError` | Fallos de validación de entrada |
| `ZipSecurityError` | Fallos en controles de seguridad ZIP |
