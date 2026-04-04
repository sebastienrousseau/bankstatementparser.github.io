---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Un edificio blanco con ventanas negras."
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/daniele-franchi-Vl6YuVBLEys.webp"
cdn: "https://cloudcdn.pro"
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Analizador de extractos bancarios. Reservados todos los derechos."
date: "Apr 01, 2026"
description: "Comience con Bank Statement Parser para Python: instale, analice archivos CAMT/PAIN.001/CSV/OFX/QFX/MT940 y utilice flujos de trabajo CLI o streaming."
download: ""
format-detection: "telephone=no"
hreflang: "es"
icon: "https://cloudcdn.pro/bankstatementparser/images/favicon.ico"
id: "https://bankstatementparser.com/es/primeros-pasos/index.html"
image_alt: "Logotipo de Bank Statement Parser, una potente herramienta Python diseñada para el procesamiento de datos financieros y la extracción de conocimientos de forma rápida y precisa."
image_height: "630"
image_width: "1200"
image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
keywords: "analizador de extractos bancarios, introducción, python, CAMT, PAIN.001, CSV, OFX, QFX, MT940, datos financieros"
language: "es-ES"
layout: "start"
locale: "es_ES"
logo_alt: "Logotipo de Bank Statement Parser, una potente herramienta Python diseñada para el procesamiento de datos financieros y la extracción de conocimientos de forma rápida y precisa."
logo_height: "44"
logo_width: "44"
logo: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
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
msapplication_tile_image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Instale y utilice Bank Statement Parser para analizar archivos CAMT, PAIN.001, CSV, OFX/QFX y MT940 en Python."
twitter_image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
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

-Python 3.9 a 3.14
- Acceso a terminal (macOS, Linux o WSL)

## Instalar

```bash
pip install bankstatementparser
```

Para compatibilidad con Polars DataFrame:

```bash
pip install bankstatementparser[polars]
```

## Inicio rápido

### Detectar automáticamente y analizar cualquier formato

```python
from bankstatementparser import create_parser, detect_statement_format

fmt = detect_statement_format("transactions.ofx")
parser = create_parser("transactions.ofx", fmt)
df = parser.parse()  # pandas DataFrame
print(df.head())
```

Esto funciona con`.xml`(CAMT/DOLOR.001),`.csv`, `.ofx`, `.qfx`, `.mt940`, y`.sta`archivos.

### Analizar CAMT.053

```python
from bankstatementparser import CamtParser

parser = CamtParser("statement.xml")
transactions = parser.parse()
```

### Analizar DOLOR.001

```python
from bankstatementparser import Pain001Parser

parser = Pain001Parser("payment.xml")
payments = parser.parse()
```

## Transmisión de archivos grandes

Para archivos con miles de transacciones, utilice la transmisión para mantener la memoria limitada:

```python
parser = CamtParser("large_statement.xml")
for transaction in parser.parse_streaming(redact_pii=True):
    process(transaction)  # Memory stays constant
```

## Análisis en memoria

Análisis a partir de bytes sin E/S de disco: útil para flujos de trabajo SFTP o API:

```python
xml_bytes = download_from_sftp()
parser = CamtParser.from_bytes(xml_bytes, source_name="daily.xml")
transactions = parser.parse()
```

## Procesamiento de archivos paralelo

Analizar varios archivos al mismo tiempo:

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

## Deduplicación

Detecte duplicados exactos y coincidencias sospechosas con puntuaciones de confianza:

```python
from bankstatementparser import CamtParser, Deduplicator

parser = CamtParser("statement.xml")
dedup = Deduplicator()
result = dedup.deduplicate(dedup.from_dataframe(parser.parse()))

print(f"Unique: {len(result.unique_transactions)}")
print(f"Exact duplicates: {len(result.exact_duplicates)}")
print(f"Suspected matches: {len(result.suspected_matches)}")
```

## Procesamiento ZIP seguro

Procese archivos XML comprimidos con controles de seguridad integrados (protección contra bombas, rechazo de entrada cifrada):

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
```

## Uso de CLI

```bash
# Parse and display
python -m bankstatementparser.cli --type camt --input statement.xml

# Export to CSV
python -m bankstatementparser.cli --type camt --input statement.xml --output transactions.csv

# Stream with PII visible
python -m bankstatementparser.cli --type camt --input statement.xml --streaming --show-pii
```

Opciones de CLI:

- `--type {camt,pain001}`-- tipo de analizador
-`--input <path>`-- archivo de entrada
-`--output <csv_path>`-- exportar a CSV
-`--streaming`- transmitir archivos grandes
-`--show-pii`-- mostrar campos confidenciales (redactados de forma predeterminada)
-`--max-size <MB>`-- límite de tamaño de archivo

## Configuración de desarrollo local

```bash
git clone https://github.com/sebastienrousseau/bankstatementparser.git
cd bankstatementparser
python3 -m venv .venv && source .venv/bin/activate
pip install poetry && poetry install --with dev
```

Ejecute el conjunto de pruebas:

```bash
pytest
```

## Referencia de API

### Clases de analizador

| Clase | Formato | Importar |
|---|---|---|
| `CamtParser` | CAMT.053 (ISO 20022) | `from bankstatementparser import CamtParser` |
| `Pain001Parser` | DOLOR.001 (ISO 20022) | `from bankstatementparser import Pain001Parser` |
| `CsvStatementParser` | CSV | `from bankstatementparser import CsvStatementParser` |
| `OfxParser` | OFX | `from bankstatementparser import OfxParser` |
| `QfxParser` | QFX | `from bankstatementparser import QfxParser` |
| `Mt940Parser` | MT940 | `from bankstatementparser import Mt940Parser` |

### Funciones de utilidad

| Función | Objetivo |
|---|---|
| `detect_statement_format(path)` | Formato de archivo de detección automática |
| `create_parser(path, fmt)` | Crear el analizador apropiado |
| `parse_files_parallel(paths)` | Analizar varios archivos simultáneamente |
| `iter_secure_xml_entries(zip_path)` | Iterar entradas ZIP de forma segura |

### Clases de datos

| Clase | Objetivo |
|---|---|
| `Deduplicator` | Detectar transacciones duplicadas |
| `DeduplicationResult` | Resultado con coincidencias únicas, exactas y sospechosas. |
| `InputValidator` | Validar rutas y formatos de archivos |
| `Transaction` | Registro de transacciones normalizadas |
| `FileResult` | Resultado del análisis paralelo |
| `ZipXMLSource` | Envoltorio de miembros ZIP |

### Excepciones

| Excepción | Cuando se levanta |
|---|---|
| `ParserError` | Fallos de análisis |
| `ExportError` | Fallos de exportación (CSV/JSON/Excel) |
| `ValidationError` | Fallos de validación de entrada |
| `ZipSecurityError` | Fallos en el control de seguridad ZIP |
