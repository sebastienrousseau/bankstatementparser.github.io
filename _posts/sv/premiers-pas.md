---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "En vit byggnad med svarta fönster"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/daniele-franchi-Vl6YuVBLEys.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Bank Statement Parser. Alla rättigheter reserverade."
date: "Apr 11, 2026"
description: "Kom igång med Bank Statement Parser för Python: installera, analysera CAMT/PAIN.001/CSV/OFX/QFX/MT940-filer och använd streaming- eller CLI-arbetsflöden."
download: ""
format-detection: "telephone=no"
hreflang: "sv"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/sv/premiers-pas/index.html"
image_alt: "Logotypen för Bank Statement Parser, ett kraftfullt Python-verktyg designat för snabb och korrekt finansiell databearbetning och extraktion av insikter."
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "kontoutdragsparser, komma igång, python, CAMT, PAIN.001, CSV, OFX, QFX, MT940, finansiell data"
language: "sv-SE"
layout: "start"
locale: "sv_SE"
logo_alt: "Logotypen för Bank Statement Parser, ett kraftfullt Python-verktyg designat för snabb och korrekt finansiell databearbetning och extraktion av insikter."
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Komma igång"
permalink: "https://bankstatementparser.com/sv/premiers-pas/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Börja bygga säkra applikationer med Bank Statement Parser"
tags: "bank,statement,parser,python,camt,pain001,csv,ofx,qfx,mt940,streaming,cli"
theme_color: "rgb(73, 214, 251)"
title: "Bank Statement Parser: Installations- och användningsguide"
url: "https://bankstatementparser.com/sv/premiers-pas/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/sv/premiers-pas/rss.xml"
category: "Ekonomiprogramvara, Python-bibliotek, utvecklarguide"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Kom igång med Bank Statement Parser för Python: installera, analysera CAMT/PAIN.001/CSV/OFX/QFX/MT940-filer och använd streaming- eller CLI-arbetsflöden."
item_guid: "https://bankstatementparser.com/sv/premiers-pas/rss.xml"
item_link: "https://bankstatementparser.com/sv/premiers-pas/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Bank Statement Parser: Installations- och användningsguide"
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
apple-mobile-web-app-title: "Bank Statement Parser: Installations- och användningsguide"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Installera och använd Bank Statement Parser för att analysera CAMT-, PAIN.001-, CSV-, OFX/QFX- och MT940-filer i Python."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logotypen för Bank Statement Parser, ett kraftfullt Python-verktyg designat för snabb och korrekt finansiell databearbetning och extraktion av insikter."
twitter_site: "@wwdseb"
twitter_title: "Bank Statement Parser: Installations- och användningsguide"
twitter_url: "https://bankstatementparser.com/sv/premiers-pas/index.html"

# Humans.txt - The Humans.txt front matter (YAML).

author_website: "https://bankstatementparser.com"
author_twitter: "@wwdseb"
author_location: "London, UK"
thanks: "Tack för att du läste!"
site_last_updated: "2026-04-01"
site_standards: "HTML5, CSS3, RSS, Atom, JSON, XML, YAML, Markdown, TOML"
site_components: "Shokunin SSG, Shokunin CLI, Shokunin Templates, Shokunin Themes, Kaishi SSG, Kaishi CLI, Kaishi Templates, Kaishi Themes"
site_software: "Shokunin, Rust"

---

## Krav

- Python 3.10 till 3.14
- Terminalåtkomst (macOS, Linux eller WSL)

## Installera

```bash
# Grundinstallation (enbart deterministiska parsers)
pip install bankstatementparser
```

Valfria tillägg för ytterligare funktioner:

```bash
# Text-LLM-väg för digitala PDF:er (litellm + pypdf)
pip install 'bankstatementparser[hybrid]'

# Högre kvalitet på tabellextraktion (lägger till pdfplumber)
pip install 'bankstatementparser[hybrid-plus]'

# Vision-LLM-väg för skannade PDF:er (lägger till pypdfium2)
pip install 'bankstatementparser[hybrid-vision]'

# LLM-driven transaktionskategorisering
pip install 'bankstatementparser[enrichment]'

# REST API-mikrotjänst (FastAPI + uvicorn)
pip install 'bankstatementparser[api]'

# Valfritt Polars DataFrame-stöd
pip install 'bankstatementparser[polars]'
```

## Snabbstart

### Autodetektera och tolka alla strukturerade format

```python
from bankstatementparser import create_parser, detect_statement_format

fmt = detect_statement_format("transactions.ofx")
parser = create_parser("transactions.ofx", fmt)
df = parser.parse()  # pandas DataFrame
print(df.head())
```

Detta fungerar med `.xml` (CAMT/PAIN.001), `.csv`, `.ofx`, `.qfx`, `.mt940` och `.sta`-filer.

### Tolka CAMT.053

```python
from bankstatementparser import CamtParser

parser = CamtParser("statement.xml")
transactions = parser.parse()
```

### Tolka PAIN.001

```python
from bankstatementparser import Pain001Parser

parser = Pain001Parser("payment.xml")
payments = parser.parse()
```

### Tolka PDF-kontoutdrag (hybrid-pipeline)

Hybrid-pipelinen dirigerar PDF:er intelligent genom tre extraktionsvägar:

```python
from bankstatementparser.hybrid import smart_ingest

result = smart_ingest("statement.pdf")
print(result.source_method)         # "deterministic" | "llm" | "vision"
print(result.verification.status)   # VERIFIED | DISCREPANCY | FAILED
print(result.transactions)          # List of extracted transactions
```

Varje extraktion verifieras med **Golden Rule**: `opening + credits − debits == closing`.

## Streaming av stora filer

För filer med tusentals transaktioner, använd streaming för att hålla minnet begränsat:

```python
parser = CamtParser("large_statement.xml")
for transaction in parser.parse_streaming(redact_pii=True):
    process(transaction)  # Memory stays constant
```

## In-memory-tolkning

Tolka från byte utan disk-I/O — användbart för SFTP- eller API-arbetsflöden:

```python
xml_bytes = download_from_sftp()
parser = CamtParser.from_bytes(xml_bytes, source_name="daily.xml")
transactions = parser.parse()
```

## Parallell filbearbetning

Tolka flera filer samtidigt:

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

## Massbearbetning av mappar

Bearbeta hela mappträd med automatisk deduplicering:

```python
from bankstatementparser.hybrid import scan_and_ingest

batch = scan_and_ingest("statements/2026/", pattern="**/*.pdf")
print(f"Processed: {len(batch.results)} files")
print(f"Unique transactions: {batch.unique_count}")
```

## Deduplicering

Idempotenta transaktionshashar för säker inkrementell inmatning:

```python
from bankstatementparser import CamtParser, Deduplicator

parser = CamtParser("statement.xml")
dedup = Deduplicator()
result = dedup.deduplicate(dedup.from_dataframe(parser.parse()))

print(f"Unique: {len(result.unique_transactions)}")
print(f"Exact duplicates: {len(result.exact_duplicates)}")
print(f"Suspected matches: {len(result.suspected_matches)}")
```

## Transaktionskategorisering (berikande)

Kategorisera transaktioner automatiskt med LLM-driven klassificering:

```python
from bankstatementparser.enrichment import Categorizer

categorizer = Categorizer()
enriched = categorizer.categorize_batch(transactions)
for txn in enriched:
    print(f"{txn.description}: {txn.category}")
```

## Ledger-export (hledger / beancount)

Exportera transaktioner till plaintext-accounting-journalformat:

```python
from bankstatementparser.export import to_hledger, to_beancount

journal = to_hledger(transactions, account="Assets:Bank:Checking")
beancount_journal = to_beancount(transactions, account="Assets:Bank:Checking")
```

## Multivaluta-saldoverifiering

Verifiera saldon oberoende per valutgrupp:

```python
from bankstatementparser.hybrid import verify_balance_multi_currency

results = verify_balance_multi_currency(transactions)
for currency, verification in results.items():
    print(f"{currency}: {verification.status}")
```

## REST API

Driftsätt som en FastAPI-mikrotjänst:

```bash
# Start the API server
bankstatementparser-api --port 8000

# For container deployments
bankstatementparser-api --host 0.0.0.0 --port 9000
```

Ändpunkter:
- `POST /ingest` — Tolka en kontoutdragsfil
- `GET /health` — Hälsokontroll

## Säker ZIP-bearbetning

Bearbeta zippade XML-filer med inbyggda säkerhetskontroller (bombskydd, avvisning av krypterade poster):

```python
from bankstatementparser import iter_secure_xml_entries, CamtParser

for entry in iter_secure_xml_entries("statements.zip"):
    parser = CamtParser.from_bytes(entry.xml_bytes, source_name=entry.source_name)
    print(f"{entry.source_name}: {len(parser.parse())} transactions")
```

## Export

```python
parser = CamtParser("statement.xml")
parser.export_csv("output.csv")
parser.export_json("output.json")

# Polars (requires bankstatementparser[polars])
polars_df = parser.to_polars()

# Excel
parser.camt_to_excel("output.xlsx")
```

## CLI-användning

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

CLI-alternativ:

- `--type {camt,pain001,ingest,review}` — parsertyp eller läge
- `--input <path>` — indatafil
- `--output <path>` — exportfil (CSV eller JSON)
- `--streaming` — streama stora filer
- `--show-pii` — visa känsliga fält (redakterade som standard)
- `--max-size <MB>` — filstorleksgräns

## Lokal utvecklingsmiljö

```bash
git clone https://github.com/sebastienrousseau/bankstatementparser.git
cd bankstatementparser
python3 -m venv .venv && source .venv/bin/activate
pip install poetry && poetry install --with dev
make install-hooks   # pre-commit hook runs `make verify` before every commit
```

Kör testsviten:

```bash
pytest
```

## API-referens

### Parser-klasser

| Klass | Format | Import |
|---|---|---|
| `CamtParser` | CAMT.053 (ISO 20022) | `from bankstatementparser import CamtParser` |
| `Pain001Parser` | PAIN.001 (ISO 20022) | `from bankstatementparser import Pain001Parser` |
| `CsvStatementParser` | CSV | `from bankstatementparser import CsvStatementParser` |
| `OfxParser` | OFX | `from bankstatementparser import OfxParser` |
| `QfxParser` | QFX | `from bankstatementparser import QfxParser` |
| `Mt940Parser` | MT940 | `from bankstatementparser import Mt940Parser` |
| `smart_ingest()` | PDF (hybrid-pipeline) | `from bankstatementparser.hybrid import smart_ingest` |

### Verktygsfunktioner

| Funktion | Syfte |
|---|---|
| `detect_statement_format(path)` | Autodetektera filformat |
| `create_parser(path, fmt)` | Skapa lämplig parser |
| `parse_files_parallel(paths)` | Tolka flera filer samtidigt |
| `iter_secure_xml_entries(zip_path)` | Iterera ZIP-poster säkert |
| `smart_ingest(path)` | Hybrid-PDF-extraktion med verifiering |
| `scan_and_ingest(dir, pattern)` | Massbearbetning av mappar |
| `verify_balance_multi_currency(txns)` | Saldoverifiering per valuta |
| `to_hledger(txns, account)` | Exportera till hledger-journalformat |
| `to_beancount(txns, account)` | Exportera till beancount-journalformat |

### Dataklasser

| Klass | Syfte |
|---|---|
| `Deduplicator` | Upptäck dubbletter av transaktioner |
| `DeduplicationResult` | Resultat med unika, exakta och misstänkta matchningar |
| `InputValidator` | Validera filsökvägar och format |
| `Transaction` | Normaliserad transaktionspost |
| `FileResult` | Resultat från parallell tolkning |
| `ZipXMLSource` | ZIP-medlemsomslag |
| `IngestResult` | Hybrid-pipelineresultat med verifiering |
| `VerificationResult` | Saldoverifieringsutfall |
| `Categorizer` | LLM-driven transaktionskategorisering |
| `AccountMapper` | Regex-baserade kontomappningsregler |

### Undantag

| Undantag | När det kastas |
|---|---|
| `ParserError` | Tolkningsfel |
| `ExportError` | Exportfel (CSV/JSON/Excel) |
| `ValidationError` | Indatavalideringsfel |
| `ZipSecurityError` | ZIP-säkerhetskontroll misslyckades |
