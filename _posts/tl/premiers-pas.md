---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Isang puting gusali na may itim na bintana"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/daniele-franchi-Vl6YuVBLEys.webp"
cdn: "https://cloudcdn.pro"
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Bank Statement Parser. Lahat ng karapatan ay nakalaan."
date: "Apr 01, 2026"
description: "Magsimula sa Bank Statement Parser para sa Python: i-install, i-parse ang mga file ng CAMT/PAIN.001/CSV/OFX/QFX/MT940, at gumamit ng streaming o CLI na mga daloy ng trabaho."
download: ""
format-detection: "telephone=no"
hreflang: "tl"
icon: "https://cloudcdn.pro/bankstatementparser/images/favicon.ico"
id: "https://bankstatementparser.com/tl/premiers-pas/index.html"
image_alt: "Logo ng Bank Statement Parser, isang makapangyarihang Python tool na idinisenyo para sa mabilis, tumpak na pinansiyal na pagpoproseso ng data at pagkuha ng mga insight."
image_height: "630"
image_width: "1200"
image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
keywords: "bank statement parser, pagsisimula, python, CAMT, PAIN.001, CSV, OFX, QFX, MT940, data sa pananalapi"
language: "tl-PH"
layout: "start"
locale: "tl_PH"
logo_alt: "Logo ng Bank Statement Parser, isang makapangyarihang Python tool na idinisenyo para sa mabilis, tumpak na pinansiyal na pagpoproseso ng data at pagkuha ng mga insight."
logo_height: "44"
logo_width: "44"
logo: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Pagsisimula"
permalink: "https://bankstatementparser.com/tl/premiers-pas/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Simulan ang Pagbuo ng Mga Secure na Application gamit ang Bank Statement Parser"
tags: "bangko,statement,parser,python,camt,pain001,csv,ofx,qfx,mt940,streaming,cli"
theme_color: "rgb(73, 214, 251)"
title: "Parser ng Bank Statement: Gabay sa Pag-install at Paggamit"
url: "https://bankstatementparser.com/tl/premiers-pas/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/tl/premiers-pas/rss.xml"
category: "Software sa Pananalapi, Python Library, Gabay sa Developer"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Magsimula sa Bank Statement Parser para sa Python: i-install, i-parse ang mga file ng CAMT/PAIN.001/CSV/OFX/QFX/MT940, at gumamit ng streaming o CLI na mga daloy ng trabaho."
item_guid: "https://bankstatementparser.com/tl/premiers-pas/rss.xml"
item_link: "https://bankstatementparser.com/tl/premiers-pas/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Parser ng Bank Statement: Gabay sa Pag-install at Paggamit"
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
apple-mobile-web-app-title: "Parser ng Bank Statement: Gabay sa Pag-install at Paggamit"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "I-install at gamitin ang Bank Statement Parser para i-parse ang CAMT, PAIN.001, CSV, OFX/QFX, at MT940 na mga file sa Python."
twitter_image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logo ng Bank Statement Parser, isang makapangyarihang Python tool na idinisenyo para sa mabilis, tumpak na pinansiyal na pagpoproseso ng data at pagkuha ng mga insight."
twitter_site: "@wwdseb"
twitter_title: "Parser ng Bank Statement: Gabay sa Pag-install at Paggamit"
twitter_url: "https://bankstatementparser.com/tl/premiers-pas/index.html"

# Humans.txt - The Humans.txt front matter (YAML).

author_website: "https://bankstatementparser.com"
author_twitter: "@wwdseb"
author_location: "London, UK"
thanks: "Salamat sa pagbabasa!"
site_last_updated: "2026-04-01"
site_standards: "HTML5, CSS3, RSS, Atom, JSON, XML, YAML, Markdown, TOML"
site_components: "Shokunin SSG, Shokunin CLI, Shokunin Templates, Shokunin Themes, Kaishi SSG, Kaishi CLI, Kaishi Templates, Kaishi Themes"
site_software: "Shokunin, Rust"

---

## Mga Kinakailangan

- Python 3.9 hanggang 3.14
- Terminal access (macOS, Linux, o WSL)

## I-install

```bash
pip install bankstatementparser
```

Para sa suporta ng Polars DataFrame:

```bash
pip install bankstatementparser[polars]
```

## Mabilis na Pagsisimula

### Auto-Detect at I-parse ang Anumang Format

```python
from bankstatementparser import create_parser, detect_statement_format

fmt = detect_statement_format("transactions.ofx")
parser = create_parser("transactions.ofx", fmt)
df = parser.parse()  # pandas DataFrame
print(df.head())
```

Gumagana ito sa`.xml`(CAMT/PAIN.001),`.csv`, `.ofx`, `.qfx`, `.mt940`, at`.sta`mga file.

### I-parse ang CAMT.053

```python
from bankstatementparser import CamtParser

parser = CamtParser("statement.xml")
transactions = parser.parse()
```

### Parse PAIN.001

```python
from bankstatementparser import Pain001Parser

parser = Pain001Parser("payment.xml")
payments = parser.parse()
```

## Pag-stream ng Malaking File

Para sa mga file na may libu-libong transaksyon, gumamit ng streaming upang panatilihing limitado ang memorya:

```python
parser = CamtParser("large_statement.xml")
for transaction in parser.parse_streaming(redact_pii=True):
    process(transaction)  # Memory stays constant
```

## In-Memory Parsing

I-parse mula sa mga byte na walang disk I/O -- kapaki-pakinabang para sa mga workflow ng SFTP o API:

```python
xml_bytes = download_from_sftp()
parser = CamtParser.from_bytes(xml_bytes, source_name="daily.xml")
transactions = parser.parse()
```

## Parallel File Processing

Mag-parse ng maraming file nang sabay-sabay:

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

## Deduplication

Tuklasin ang mga eksaktong duplicate at pinaghihinalaang tugma na may mga marka ng kumpiyansa:

```python
from bankstatementparser import CamtParser, Deduplicator

parser = CamtParser("statement.xml")
dedup = Deduplicator()
result = dedup.deduplicate(dedup.from_dataframe(parser.parse()))

print(f"Unique: {len(result.unique_transactions)}")
print(f"Exact duplicates: {len(result.exact_duplicates)}")
print(f"Suspected matches: {len(result.suspected_matches)}")
```

## Secure na Pagproseso ng ZIP

Iproseso ang mga naka-zip na XML file na may built-in na mga pagsusuri sa seguridad (proteksyon sa bomba, naka-encrypt na pagtanggi sa pagpasok):

```python
from bankstatementparser import iter_secure_xml_entries, CamtParser

for entry in iter_secure_xml_entries("statements.zip"):
    parser = CamtParser.from_bytes(entry.xml_bytes, source_name=entry.source_name)
    print(f"{entry.source_name}: {len(parser.parse())} transactions")
```

## I-export

```python
parser = CamtParser("statement.xml")
parser.export_csv("output.csv")
parser.export_json("output.json")

# Polars (requires bankstatementparser[polars])
polars_df = parser.to_polars()
```

## Paggamit ng CLI

```bash
# Parse and display
python -m bankstatementparser.cli --type camt --input statement.xml

# Export to CSV
python -m bankstatementparser.cli --type camt --input statement.xml --output transactions.csv

# Stream with PII visible
python -m bankstatementparser.cli --type camt --input statement.xml --streaming --show-pii
```

Mga opsyon sa CLI:

- `--type {camt,pain001}`-- uri ng parser
-`--input <path>`-- input file
-`--output <csv_path>`-- i-export sa CSV
-`--streaming`-- stream ng malalaking file
-`--show-pii`-- ipakita ang mga sensitibong field (na-redact bilang default)
-`--max-size <MB>`-- limitasyon sa laki ng file

## Local Development Setup

```bash
git clone https://github.com/sebastienrousseau/bankstatementparser.git
cd bankstatementparser
python3 -m venv .venv && source .venv/bin/activate
pip install poetry && poetry install --with dev
```

Patakbuhin ang test suite:

```bash
pytest
```

## Sanggunian ng API

### Mga Klase ng Parser

| Klase | Format | Mag-import |
|---|---|---|
| `CamtParser` | CAMT.053 (ISO 20022) | `from bankstatementparser import CamtParser` |
| `Pain001Parser` | PAIN.001 (ISO 20022) | `from bankstatementparser import Pain001Parser` |
| `CsvStatementParser` | CSV | `from bankstatementparser import CsvStatementParser` |
| `OfxParser` | OFX | `from bankstatementparser import OfxParser` |
| `QfxParser` | QFX | `from bankstatementparser import QfxParser` |
| `Mt940Parser` | MT940 | `from bankstatementparser import Mt940Parser` |

### Mga Pag-andar ng Utility

| Function | Layunin |
|---|---|
| `detect_statement_format(path)` | Auto-detect ang format ng file |
| `create_parser(path, fmt)` | Lumikha ng naaangkop na parser |
| `parse_files_parallel(paths)` | Mag-parse ng maraming file nang sabay-sabay |
| `iter_secure_xml_entries(zip_path)` | Ulitin ang mga entry sa ZIP nang secure |

### Mga Klase ng Data

| Klase | Layunin |
|---|---|
| `Deduplicator` | I-detect ang mga duplicate na transaksyon |
| `DeduplicationResult` | Resulta na may natatangi, eksakto, at pinaghihinalaang mga tugma |
| `InputValidator` | I-validate ang mga path at format ng file |
| `Transaction` | Normalized na rekord ng transaksyon |
| `FileResult` | Resulta mula sa parallel parsing |
| `ZipXMLSource` | ZIP member wrapper |

### Mga pagbubukod

| Exception | Kapag Itinaas |
|---|---|
| `ParserError` | Mga pagkabigo sa pag-parse |
| `ExportError` | Mga pagkabigo sa pag-export (CSV/JSON/Excel) |
| `ValidationError` | Mga pagkabigo sa pagpapatunay ng input |
| `ZipSecurityError` | Mga pagkabigo sa pagsusuri sa seguridad ng ZIP |
