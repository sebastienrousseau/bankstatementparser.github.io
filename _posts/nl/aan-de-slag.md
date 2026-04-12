---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Een wit gebouw met zwarte ramen"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/daniele-franchi-Vl6YuVBLEys.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Parser voor bankafschriften. Alle rechten voorbehouden."
date: "Apr 11, 2026"
description: "Ga aan de slag met Bank Statement Parser voor Python: installeer, parseer CAMT/PAIN.001/CSV/OFX/QFX/MT940-bestanden en gebruik streaming- of CLI-workflows."
download: ""
format-detection: "telephone=no"
hreflang: "nl"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/nl/aan-de-slag/index.html"
image_alt: "Logo van Bank Statement Parser, een krachtige Python-tool ontworpen voor snelle, nauwkeurige verwerking van financiële gegevens en extractie van inzichten."
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "bankafschriftparser, aan de slag, python, CAMT, PAIN.001, CSV, OFX, QFX, MT940, financiële gegevens"
language: "nl-NL"
layout: "start"
locale: "nl_NL"
logo_alt: "Logo van Bank Statement Parser, een krachtige Python-tool ontworpen voor snelle, nauwkeurige verwerking van financiële gegevens en extractie van inzichten."
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Aan de slag"
permalink: "https://bankstatementparser.com/nl/aan-de-slag/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Begin met het bouwen van veilige applicaties met Bank Statement Parser"
tags: "bank,verklaring,parser,python,camt,pain001,csv,ofx,qfx,mt940,streaming,cli"
theme_color: "rgb(73, 214, 251)"
title: "Bankafschriftparser: installatie- en gebruikshandleiding"
url: "https://bankstatementparser.com/nl/aan-de-slag/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/nl/aan-de-slag/rss.xml"
category: "Financiële software, Python-bibliotheek, handleiding voor ontwikkelaars"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Ga aan de slag met Bank Statement Parser voor Python: installeer, parseer CAMT/PAIN.001/CSV/OFX/QFX/MT940-bestanden en gebruik streaming- of CLI-workflows."
item_guid: "https://bankstatementparser.com/nl/aan-de-slag/rss.xml"
item_link: "https://bankstatementparser.com/nl/aan-de-slag/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Bankafschriftparser: installatie- en gebruikshandleiding"
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
apple-mobile-web-app-title: "Bankafschriftparser: installatie- en gebruikshandleiding"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Installeer en gebruik Bank Statement Parser om CAMT-, PAIN.001-, CSV-, OFX/QFX- en MT940-bestanden in Python te parseren."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logo van Bank Statement Parser, een krachtige Python-tool ontworpen voor snelle, nauwkeurige verwerking van financiële gegevens en extractie van inzichten."
twitter_site: "@wwdseb"
twitter_title: "Bankafschriftparser: installatie- en gebruikshandleiding"
twitter_url: "https://bankstatementparser.com/nl/aan-de-slag/index.html"

# Humans.txt - The Humans.txt front matter (YAML).

author_website: "https://bankstatementparser.com"
author_twitter: "@wwdseb"
author_location: "London, UK"
thanks: "Bedankt voor het lezen!"
site_last_updated: "2026-04-01"
site_standards: "HTML5, CSS3, RSS, Atom, JSON, XML, YAML, Markdown, TOML"
site_components: "Shokunin SSG, Shokunin CLI, Shokunin Templates, Shokunin Themes, Kaishi SSG, Kaishi CLI, Kaishi Templates, Kaishi Themes"
site_software: "Shokunin, Rust"

---

## Vereisten

- Python 3.10 tot 3.14
- Terminaltoegang (macOS, Linux of WSL)

## Installeren

```bash
# Basisinstallatie (alleen deterministische parsers)
pip install bankstatementparser
```

Optionele extra's voor aanvullende mogelijkheden:

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

## Snelle start

### Elk gestructureerd formaat automatisch detecteren en parseren

```python
from bankstatementparser import create_parser, detect_statement_format

fmt = detect_statement_format("transactions.ofx")
parser = create_parser("transactions.ofx", fmt)
df = parser.parse()  # pandas DataFrame
print(df.head())
```

Dit werkt met `.xml` (CAMT/PAIN.001), `.csv`, `.ofx`, `.qfx`, `.mt940` en `.sta` bestanden.

### CAMT.053 parseren

```python
from bankstatementparser import CamtParser

parser = CamtParser("statement.xml")
transactions = parser.parse()
```

### PAIN.001 parseren

```python
from bankstatementparser import Pain001Parser

parser = Pain001Parser("payment.xml")
payments = parser.parse()
```

### PDF-bankafschriften parseren (hybride pipeline)

De hybride pipeline routeert PDF's op een slimme manier via drie extractiepaden:

```python
from bankstatementparser.hybrid import smart_ingest

result = smart_ingest("statement.pdf")
print(result.source_method)         # "deterministic" | "llm" | "vision"
print(result.verification.status)   # VERIFIED | DISCREPANCY | FAILED
print(result.transactions)          # List of extracted transactions
```

Elke extractie wordt geverifieerd met de **Golden Rule**: `opening + credits − debits == closing`.

## Grote bestanden streamen

Voor bestanden met duizenden transacties kunt u streaming gebruiken om het geheugen beperkt te houden:

```python
parser = CamtParser("large_statement.xml")
for transaction in parser.parse_streaming(redact_pii=True):
    process(transaction)  # Memory stays constant
```

## Parseren in het geheugen

Parseren van bytes zonder schijf-I/O -- handig voor SFTP- of API-workflows:

```python
xml_bytes = download_from_sftp()
parser = CamtParser.from_bytes(xml_bytes, source_name="daily.xml")
transactions = parser.parse()
```

## Parallelle bestandsverwerking

Meerdere bestanden gelijktijdig parseren:

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

## Bulk-mappen scannen

Verwerk volledige mappenbomen met automatische ontdubbeling:

```python
from bankstatementparser.hybrid import scan_and_ingest

batch = scan_and_ingest("statements/2026/", pattern="**/*.pdf")
print(f"Processed: {len(batch.results)} files")
print(f"Unique transactions: {batch.unique_count}")
```

## Ontdubbeling

Idempotente transactie-hashes voor veilige incrementele opname:

```python
from bankstatementparser import CamtParser, Deduplicator

parser = CamtParser("statement.xml")
dedup = Deduplicator()
result = dedup.deduplicate(dedup.from_dataframe(parser.parse()))

print(f"Unique: {len(result.unique_transactions)}")
print(f"Exact duplicates: {len(result.exact_duplicates)}")
print(f"Suspected matches: {len(result.suspected_matches)}")
```

## Transactiecategorisatie (verrijking)

Categoriseer transacties automatisch met LLM-gestuurde classificatie:

```python
from bankstatementparser.enrichment import Categorizer

categorizer = Categorizer()
enriched = categorizer.categorize_batch(transactions)
for txn in enriched:
    print(f"{txn.description}: {txn.category}")
```

## Ledger-export (hledger / beancount)

Exporteer transacties naar plaintext-accounting journaalformaten:

```python
from bankstatementparser.export import to_hledger, to_beancount

journal = to_hledger(transactions, account="Assets:Bank:Checking")
beancount_journal = to_beancount(transactions, account="Assets:Bank:Checking")
```

## Multi-valuta saldoverificatie

Verifieer saldi onafhankelijk per valutagroep:

```python
from bankstatementparser.hybrid import verify_balance_multi_currency

results = verify_balance_multi_currency(transactions)
for currency, verification in results.items():
    print(f"{currency}: {verification.status}")
```

## REST API

Implementeer als FastAPI-microservice:

```bash
# Start the API server
bankstatementparser-api --port 8000

# For container deployments
bankstatementparser-api --host 0.0.0.0 --port 9000
```

Endpoints:
- `POST /ingest` -- Een bankafschriftbestand parseren
- `GET /health` -- Gezondheidscontrole

## Veilige ZIP-verwerking

Verwerk gecomprimeerde XML-bestanden met ingebouwde veiligheidscontroles (bombeveiliging, afwijzing van versleutelde bestanden):

```python
from bankstatementparser import iter_secure_xml_entries, CamtParser

for entry in iter_secure_xml_entries("statements.zip"):
    parser = CamtParser.from_bytes(entry.xml_bytes, source_name=entry.source_name)
    print(f"{entry.source_name}: {len(parser.parse())} transactions")
```

## Exporteren

```python
parser = CamtParser("statement.xml")
parser.export_csv("output.csv")
parser.export_json("output.json")

# Polars (requires bankstatementparser[polars])
polars_df = parser.to_polars()

# Excel
parser.camt_to_excel("output.xlsx")
```

## CLI-gebruik

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

CLI-opties:

- `--type {camt,pain001,ingest,review}` -- parsertype of modus
- `--input <path>` -- invoerbestand
- `--output <path>` -- exportbestand (CSV of JSON)
- `--streaming` -- grote bestanden streamen
- `--show-pii` -- gevoelige velden tonen (standaard geanonimiseerd)
- `--max-size <MB>` -- limiet bestandsgrootte

## Lokale ontwikkeling instellen

```bash
git clone https://github.com/sebastienrousseau/bankstatementparser.git
cd bankstatementparser
python3 -m venv .venv && source .venv/bin/activate
pip install poetry && poetry install --with dev
make install-hooks   # pre-commit hook runs `make verify` before every commit
```

Voer het testpakket uit:

```bash
pytest
```

## API-referentie

### Parser-klassen

| Klasse | Formaat | Import |
|---|---|---|
| `CamtParser` | CAMT.053 (ISO 20022) | `from bankstatementparser import CamtParser` |
| `Pain001Parser` | PAIN.001 (ISO 20022) | `from bankstatementparser import Pain001Parser` |
| `CsvStatementParser` | CSV | `from bankstatementparser import CsvStatementParser` |
| `OfxParser` | OFX | `from bankstatementparser import OfxParser` |
| `QfxParser` | QFX | `from bankstatementparser import QfxParser` |
| `Mt940Parser` | MT940 | `from bankstatementparser import Mt940Parser` |
| `smart_ingest()` | PDF (hybride pipeline) | `from bankstatementparser.hybrid import smart_ingest` |

### Hulpfuncties

| Functie | Doel |
|---|---|
| `detect_statement_format(path)` | Bestandsformaat automatisch detecteren |
| `create_parser(path, fmt)` | De juiste parser aanmaken |
| `parse_files_parallel(paths)` | Meerdere bestanden gelijktijdig parseren |
| `iter_secure_xml_entries(zip_path)` | ZIP-bestanden veilig doorlopen |
| `smart_ingest(path)` | Hybride PDF-extractie met verificatie |
| `scan_and_ingest(dir, pattern)` | Bulk-mappen scannen |
| `verify_balance_multi_currency(txns)` | Saldoverificatie per valuta |
| `to_hledger(txns, account)` | Exporteren naar hledger-journaalformaat |
| `to_beancount(txns, account)` | Exporteren naar beancount-journaalformaat |

### Gegevensklassen

| Klasse | Doel |
|---|---|
| `Deduplicator` | Dubbele transacties detecteren |
| `DeduplicationResult` | Resultaat met unieke, exacte en vermoedelijke overeenkomsten |
| `InputValidator` | Bestandspaden en formaten valideren |
| `Transaction` | Genormaliseerd transactierecord |
| `FileResult` | Resultaat van parallelle parsing |
| `ZipXMLSource` | ZIP-bestandswrapper |
| `IngestResult` | Resultaat hybride pipeline met verificatie |
| `VerificationResult` | Uitkomst saldoverificatie |
| `Categorizer` | LLM-gestuurde transactiecategorisatie |
| `AccountMapper` | Regex-gebaseerde rekeningkoppelingsregels |

### Uitzonderingen

| Uitzondering | Wanneer gegenereerd |
|---|---|
| `ParserError` | Parseerfouten |
| `ExportError` | Exportfouten (CSV/JSON/Excel) |
| `ValidationError` | Fouten bij invoervalidatie |
| `ZipSecurityError` | ZIP-beveiligingscontrole mislukt |
