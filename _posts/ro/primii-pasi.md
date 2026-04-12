---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "O clădire albă cu ferestre negre"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/daniele-franchi-Vl6YuVBLEys.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Analizator extras de cont. Toate drepturile rezervate."
date: "Apr 11, 2026"
description: "Începeți cu analizatorul de extrase de cont pentru Python: instalați, analizați fișierele CAMT/PAIN.001/CSV/OFX/QFX/MT940 și utilizați fluxurile de lucru în flux sau CLI."
download: ""
format-detection: "telephone=no"
hreflang: "ro"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/ro/primii-pasi/index.html"
image_alt: "Logo-ul Bank Statement Parser, un instrument puternic Python conceput pentru procesarea rapidă și precisă a datelor financiare și extragerea de informații."
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "analizator extras de cont, noțiuni introductive, python, CAMT, PAIN.001, CSV, OFX, QFX, MT940, date financiare"
language: "ro-RO"
layout: "start"
locale: "ro_RO"
logo_alt: "Logo-ul Bank Statement Parser, un instrument puternic Python conceput pentru procesarea rapidă și precisă a datelor financiare și extragerea de informații."
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Noțiuni de bază"
permalink: "https://bankstatementparser.com/ro/primii-pasi/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Începeți să construiți aplicații securizate cu analizatorul extras de cont"
tags: "bank,extras,parser,python,camt,pain001,csv,ofx,qfx,mt940,streaming,cli"
theme_color: "rgb(73, 214, 251)"
title: "Analizator extras de cont: Ghid de instalare și utilizare"
url: "https://bankstatementparser.com/ro/primii-pasi/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/ro/primii-pasi/rss.xml"
category: "Software financiar, Biblioteca Python, Ghid pentru dezvoltatori"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Începeți cu analizatorul de extrase de cont pentru Python: instalați, analizați fișierele CAMT/PAIN.001/CSV/OFX/QFX/MT940 și utilizați fluxurile de lucru în flux sau CLI."
item_guid: "https://bankstatementparser.com/ro/primii-pasi/rss.xml"
item_link: "https://bankstatementparser.com/ro/primii-pasi/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Analizator extras de cont: Ghid de instalare și utilizare"
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
apple-mobile-web-app-title: "Analizator extras de cont: Ghid de instalare și utilizare"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Instalați și utilizați analizatorul de extrase de cont pentru a analiza fișierele CAMT, PAIN.001, CSV, OFX/QFX și MT940 în Python."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logo-ul Bank Statement Parser, un instrument puternic Python conceput pentru procesarea rapidă și precisă a datelor financiare și extragerea de informații."
twitter_site: "@wwdseb"
twitter_title: "Analizator extras de cont: Ghid de instalare și utilizare"
twitter_url: "https://bankstatementparser.com/ro/primii-pasi/index.html"

# Humans.txt - The Humans.txt front matter (YAML).

author_website: "https://bankstatementparser.com"
author_twitter: "@wwdseb"
author_location: "London, UK"
thanks: "Multumesc pentru lectura!"
site_last_updated: "2026-04-01"
site_standards: "HTML5, CSS3, RSS, Atom, JSON, XML, YAML, Markdown, TOML"
site_components: "Shokunin SSG, Shokunin CLI, Shokunin Templates, Shokunin Themes, Kaishi SSG, Kaishi CLI, Kaishi Templates, Kaishi Themes"
site_software: "Shokunin, Rust"

---

## Cerințe

- Python 3.10 până la 3.14
- Acces la terminal (macOS, Linux sau WSL)

## Instalare

```bash
# Instalare de bază (doar parsere deterministe)
pip install bankstatementparser
```

Extensii opționale pentru funcționalități suplimentare:

```bash
# Calea Text-LLM pentru PDF-uri digitale (litellm + pypdf)
pip install 'bankstatementparser[hybrid]'

# Extracție de tabele cu fidelitate mai mare (adaugă pdfplumber)
pip install 'bankstatementparser[hybrid-plus]'

# Calea Vision-LLM pentru PDF-uri scanate (adaugă pypdfium2)
pip install 'bankstatementparser[hybrid-vision]'

# Categorizare a tranzacțiilor prin LLM
pip install 'bankstatementparser[enrichment]'

# Microserviciu REST API (FastAPI + uvicorn)
pip install 'bankstatementparser[api]'

# Suport opțional pentru DataFrames Polars
pip install 'bankstatementparser[polars]'
```

## Pornire rapidă

### Detectare automată și analizare a oricărui format structurat

```python
from bankstatementparser import create_parser, detect_statement_format

fmt = detect_statement_format("transactions.ofx")
parser = create_parser("transactions.ofx", fmt)
df = parser.parse()  # pandas DataFrame
print(df.head())
```

Funcționează cu fișiere `.xml` (CAMT/PAIN.001), `.csv`, `.ofx`, `.qfx`, `.mt940` și `.sta`.

### Analizare CAMT.053

```python
from bankstatementparser import CamtParser

parser = CamtParser("statement.xml")
transactions = parser.parse()
```

### Analizare PAIN.001

```python
from bankstatementparser import Pain001Parser

parser = Pain001Parser("payment.xml")
payments = parser.parse()
```

### Analizare extrase bancare PDF (pipeline hibrid)

Pipeline-ul hibrid rutează inteligent PDF-urile prin trei căi de extracție:

```python
from bankstatementparser.hybrid import smart_ingest

result = smart_ingest("statement.pdf")
print(result.source_method)         # "deterministic" | "llm" | "vision"
print(result.verification.status)   # VERIFIED | DISCREPANCY | FAILED
print(result.transactions)          # List of extracted transactions
```

Fiecare extracție este verificată cu **Regula de Aur**: `opening + credits − debits == closing`.

## Streaming pentru fișiere mari

Pentru fișiere cu mii de tranzacții, folosiți streaming pentru a menține memoria limitată:

```python
parser = CamtParser("large_statement.xml")
for transaction in parser.parse_streaming(redact_pii=True):
    process(transaction)  # Memory stays constant
```

## Parsare în memorie

Analizați din octeți fără I/O pe disc — util pentru fluxuri SFTP sau API:

```python
xml_bytes = download_from_sftp()
parser = CamtParser.from_bytes(xml_bytes, source_name="daily.xml")
transactions = parser.parse()
```

## Procesare paralelă a fișierelor

Analizați mai multe fișiere simultan:

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

## Scanare în masă a directoarelor

Procesați arbori întregi de foldere cu deduplicare automată:

```python
from bankstatementparser.hybrid import scan_and_ingest

batch = scan_and_ingest("statements/2026/", pattern="**/*.pdf")
print(f"Processed: {len(batch.results)} files")
print(f"Unique transactions: {batch.unique_count}")
```

## Deduplicare

Hash-uri idempotente ale tranzacțiilor pentru ingestie incrementală sigură:

```python
from bankstatementparser import CamtParser, Deduplicator

parser = CamtParser("statement.xml")
dedup = Deduplicator()
result = dedup.deduplicate(dedup.from_dataframe(parser.parse()))

print(f"Unique: {len(result.unique_transactions)}")
print(f"Exact duplicates: {len(result.exact_duplicates)}")
print(f"Suspected matches: {len(result.suspected_matches)}")
```

## Categorizare tranzacții (îmbogățire)

Categorizați automat tranzacțiile folosind clasificare prin LLM:

```python
from bankstatementparser.enrichment import Categorizer

categorizer = Categorizer()
enriched = categorizer.categorize_batch(transactions)
for txn in enriched:
    print(f"{txn.description}: {txn.category}")
```

## Export registru (hledger / beancount)

Exportați tranzacții în formate de jurnal pentru contabilitate în text simplu:

```python
from bankstatementparser.export import to_hledger, to_beancount

journal = to_hledger(transactions, account="Assets:Bank:Checking")
beancount_journal = to_beancount(transactions, account="Assets:Bank:Checking")
```

## Verificare sold multi-valută

Verificați soldurile independent pe fiecare grup de valută:

```python
from bankstatementparser.hybrid import verify_balance_multi_currency

results = verify_balance_multi_currency(transactions)
for currency, verification in results.items():
    print(f"{currency}: {verification.status}")
```

## REST API

Implementați ca microserviciu FastAPI:

```bash
# Start the API server
bankstatementparser-api --port 8000

# For container deployments
bankstatementparser-api --host 0.0.0.0 --port 9000
```

Endpoint-uri:
- `POST /ingest` -- Analizează un fișier de extras bancar
- `GET /health` -- Verificare de stare

## Procesare ZIP securizată

Procesați fișiere XML arhivate cu verificări de securitate încorporate (protecție bomb, respingere intrări criptate):

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

## Utilizare CLI

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

Opțiuni CLI:

- `--type {camt,pain001,ingest,review}` -- tipul parserului sau modul
- `--input <path>` -- fișier de intrare
- `--output <path>` -- fișier de export (CSV sau JSON)
- `--streaming` -- streaming pentru fișiere mari
- `--show-pii` -- afișează câmpurile sensibile (redactate implicit)
- `--max-size <MB>` -- limită de dimensiune a fișierului

## Configurare dezvoltare locală

```bash
git clone https://github.com/sebastienrousseau/bankstatementparser.git
cd bankstatementparser
python3 -m venv .venv && source .venv/bin/activate
pip install poetry && poetry install --with dev
make install-hooks   # pre-commit hook runs `make verify` before every commit
```

Rulați suita de teste:

```bash
pytest
```

## Referință API

### Clase parser

| Clasă | Format | Import |
|---|---|---|
| `CamtParser` | CAMT.053 (ISO 20022) | `from bankstatementparser import CamtParser` |
| `Pain001Parser` | PAIN.001 (ISO 20022) | `from bankstatementparser import Pain001Parser` |
| `CsvStatementParser` | CSV | `from bankstatementparser import CsvStatementParser` |
| `OfxParser` | OFX | `from bankstatementparser import OfxParser` |
| `QfxParser` | QFX | `from bankstatementparser import QfxParser` |
| `Mt940Parser` | MT940 | `from bankstatementparser import Mt940Parser` |
| `smart_ingest()` | PDF (pipeline hibrid) | `from bankstatementparser.hybrid import smart_ingest` |

### Funcții utilitare

| Funcție | Scop |
|---|---|
| `detect_statement_format(path)` | Detectare automată a formatului fișierului |
| `create_parser(path, fmt)` | Crearea parserului corespunzător |
| `parse_files_parallel(paths)` | Analizare a mai multor fișiere simultan |
| `iter_secure_xml_entries(zip_path)` | Iterare securizată a intrărilor ZIP |
| `smart_ingest(path)` | Extracție hibridă PDF cu verificare |
| `scan_and_ingest(dir, pattern)` | Scanare în masă a directoarelor |
| `verify_balance_multi_currency(txns)` | Verificare sold pe fiecare valută |
| `to_hledger(txns, account)` | Export în format jurnal hledger |
| `to_beancount(txns, account)` | Export în format jurnal beancount |

### Clase de date

| Clasă | Scop |
|---|---|
| `Deduplicator` | Detectare tranzacții duplicate |
| `DeduplicationResult` | Rezultat cu potriviri unice, exacte și suspectate |
| `InputValidator` | Validare căi și formate de fișiere |
| `Transaction` | Înregistrare normalizată a tranzacțiilor |
| `FileResult` | Rezultat din parsare paralelă |
| `ZipXMLSource` | Wrapper pentru membrii ZIP |
| `IngestResult` | Rezultat pipeline hibrid cu verificare |
| `VerificationResult` | Rezultat verificare sold |
| `Categorizer` | Categorizare tranzacții prin LLM |
| `AccountMapper` | Reguli de mapare conturi bazate pe regex |

### Excepții

| Excepție | Când este ridicată |
|---|---|
| `ParserError` | Erori de parsare |
| `ExportError` | Erori la export (CSV/JSON/Excel) |
| `ValidationError` | Erori de validare a intrărilor |
| `ZipSecurityError` | Erori la verificarea securității ZIP |
