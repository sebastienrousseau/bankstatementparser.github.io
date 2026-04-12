---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "A white building with black windows"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/daniele-franchi-Vl6YuVBLEys.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Bank Statement Parser. All rights reserved."
date: "Apr 11, 2026"
description: "Get started with Bank Statement Parser for Python: install, parse CAMT/PAIN.001/CSV/OFX/QFX/MT940/PDF files, hybrid pipeline, REST API, and CLI workflows."
download: ""
format-detection: "telephone=no"
hreflang: "en"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/getting-started/index.html"
image_alt: "Logo of Bank Statement Parser, a powerful Python tool designed for quick, accurate financial data processing and insights extraction."
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "bank statement parser, getting started, python, CAMT, PAIN.001, CSV, OFX, QFX, MT940, financial data"
language: "en-GB"
layout: "start"
locale: "en_GB"
logo_alt: "Logo of Bank Statement Parser, a powerful Python tool designed for quick, accurate financial data processing and insights extraction."
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Getting Started"
permalink: "https://bankstatementparser.com/getting-started/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Start Building Secure Applications with Bank Statement Parser"
tags: "bank,statement,parser,python,camt,pain001,csv,ofx,qfx,mt940,streaming,cli"
theme_color: "rgb(73, 214, 251)"
title: "Bank Statement Parser: Installation and Usage Guide"
url: "https://bankstatementparser.com/getting-started/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/getting-started/rss.xml"
category: "Finance Software, Python Library, Developer Guide"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Get started with Bank Statement Parser for Python: install, parse CAMT/PAIN.001/CSV/OFX/QFX/MT940 files, and use streaming or CLI workflows."
item_guid: "https://bankstatementparser.com/getting-started/rss.xml"
item_link: "https://bankstatementparser.com/getting-started/rss.xml"
item_pub_date: "2026-04-11T00:00:00+00:00"
item_title: "Bank Statement Parser: Installation and Usage Guide"
last_build_date: "2026-04-11T00:00:00+00:00"
managing_editor: "contact@bankstatementparser.com"
pub_date: "2026-04-11T00:00:00+00:00"
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
apple-mobile-web-app-title: "Bank Statement Parser: Installation and Usage Guide"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Install and use Bank Statement Parser to parse CAMT, PAIN.001, CSV, OFX/QFX, and MT940 files in Python."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logo of Bank Statement Parser, a powerful Python tool designed for quick, accurate financial data processing and insights extraction."
twitter_site: "@wwdseb"
twitter_title: "Bank Statement Parser: Installation and Usage Guide"
twitter_url: "https://bankstatementparser.com/getting-started/index.html"

# Humans.txt - The Humans.txt front matter (YAML).

author_website: "https://bankstatementparser.com"
author_twitter: "@wwdseb"
author_location: "London, UK"
thanks: "Thanks for reading!"
site_last_updated: "2026-04-11"
site_standards: "HTML5, CSS3, RSS, Atom, JSON, XML, YAML, Markdown, TOML"
site_components: "Shokunin SSG, Shokunin CLI, Shokunin Templates, Shokunin Themes, Kaishi SSG, Kaishi CLI, Kaishi Templates, Kaishi Themes"
site_software: "Shokunin, Rust"

---

## Requirements

- Python 3.10 to 3.14
- Terminal access (macOS, Linux, or WSL)

## Install

```bash
# Core install (deterministic parsers only)
pip install bankstatementparser
```

Optional extras for additional capabilities:

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

## Quick Start

### Auto-Detect and Parse Any Structured Format

```python
from bankstatementparser import create_parser, detect_statement_format

fmt = detect_statement_format("transactions.ofx")
parser = create_parser("transactions.ofx", fmt)
df = parser.parse()  # pandas DataFrame
print(df.head())
```

This works with `.xml` (CAMT/PAIN.001), `.csv`, `.ofx`, `.qfx`, `.mt940`, and `.sta` files.

### Parse CAMT.053

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

### Parse PDF Bank Statements (Hybrid Pipeline)

The hybrid pipeline intelligently routes PDFs through three extraction paths:

```python
from bankstatementparser.hybrid import smart_ingest

result = smart_ingest("statement.pdf")
print(result.source_method)         # "deterministic" | "llm" | "vision"
print(result.verification.status)   # VERIFIED | DISCREPANCY | FAILED
print(result.transactions)          # List of extracted transactions
```

Every extraction is verified with the **Golden Rule**: `opening + credits − debits == closing`.

## Streaming Large Files

For files with thousands of transactions, use streaming to keep memory bounded:

```python
parser = CamtParser("large_statement.xml")
for transaction in parser.parse_streaming(redact_pii=True):
    process(transaction)  # Memory stays constant
```

## In-Memory Parsing

Parse from bytes without disk I/O -- useful for SFTP or API workflows:

```python
xml_bytes = download_from_sftp()
parser = CamtParser.from_bytes(xml_bytes, source_name="daily.xml")
transactions = parser.parse()
```

## Parallel File Processing

Parse multiple files concurrently:

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

## Bulk Directory Scanning

Process entire folder trees with automatic deduplication:

```python
from bankstatementparser.hybrid import scan_and_ingest

batch = scan_and_ingest("statements/2026/", pattern="**/*.pdf")
print(f"Processed: {len(batch.results)} files")
print(f"Unique transactions: {batch.unique_count}")
```

## Deduplication

Idempotent transaction hashes for safe incremental ingestion:

```python
from bankstatementparser import CamtParser, Deduplicator

parser = CamtParser("statement.xml")
dedup = Deduplicator()
result = dedup.deduplicate(dedup.from_dataframe(parser.parse()))

print(f"Unique: {len(result.unique_transactions)}")
print(f"Exact duplicates: {len(result.exact_duplicates)}")
print(f"Suspected matches: {len(result.suspected_matches)}")
```

## Transaction Categorisation (Enrichment)

Automatically categorise transactions using LLM-powered classification:

```python
from bankstatementparser.enrichment import Categorizer

categorizer = Categorizer()
enriched = categorizer.categorize_batch(transactions)
for txn in enriched:
    print(f"{txn.description}: {txn.category}")
```

## Ledger Export (hledger / beancount)

Export transactions to plaintext-accounting journal formats:

```python
from bankstatementparser.export import to_hledger, to_beancount

journal = to_hledger(transactions, account="Assets:Bank:Checking")
beancount_journal = to_beancount(transactions, account="Assets:Bank:Checking")
```

## Multi-Currency Balance Verification

Verify balances independently per currency group:

```python
from bankstatementparser.hybrid import verify_balance_multi_currency

results = verify_balance_multi_currency(transactions)
for currency, verification in results.items():
    print(f"{currency}: {verification.status}")
```

## REST API

Deploy as a FastAPI microservice:

```bash
# Start the API server
bankstatementparser-api --port 8000

# For container deployments
bankstatementparser-api --host 0.0.0.0 --port 9000
```

Endpoints:
- `POST /ingest` -- Parse a bank statement file
- `GET /health` -- Health check

## Secure ZIP Processing

Process zipped XML files with built-in security checks (bomb protection, encrypted entry rejection):

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

## CLI Usage

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

CLI options:

- `--type {camt,pain001,ingest,review}` -- parser type or mode
- `--input <path>` -- input file
- `--output <path>` -- export file (CSV or JSON)
- `--streaming` -- stream large files
- `--show-pii` -- show sensitive fields (redacted by default)
- `--max-size <MB>` -- file size limit

## Local Development Setup

```bash
git clone https://github.com/sebastienrousseau/bankstatementparser.git
cd bankstatementparser
python3 -m venv .venv && source .venv/bin/activate
pip install poetry && poetry install --with dev
make install-hooks   # pre-commit hook runs `make verify` before every commit
```

Run the test suite:

```bash
pytest
```

## API Reference

### Parser Classes

| Class | Format | Import |
|---|---|---|
| `CamtParser` | CAMT.053 (ISO 20022) | `from bankstatementparser import CamtParser` |
| `Pain001Parser` | PAIN.001 (ISO 20022) | `from bankstatementparser import Pain001Parser` |
| `CsvStatementParser` | CSV | `from bankstatementparser import CsvStatementParser` |
| `OfxParser` | OFX | `from bankstatementparser import OfxParser` |
| `QfxParser` | QFX | `from bankstatementparser import QfxParser` |
| `Mt940Parser` | MT940 | `from bankstatementparser import Mt940Parser` |
| `smart_ingest()` | PDF (hybrid pipeline) | `from bankstatementparser.hybrid import smart_ingest` |

### Utility Functions

| Function | Purpose |
|---|---|
| `detect_statement_format(path)` | Auto-detect file format |
| `create_parser(path, fmt)` | Create the appropriate parser |
| `parse_files_parallel(paths)` | Parse multiple files concurrently |
| `iter_secure_xml_entries(zip_path)` | Iterate ZIP entries securely |
| `smart_ingest(path)` | Hybrid PDF extraction with verification |
| `scan_and_ingest(dir, pattern)` | Bulk directory scanning |
| `verify_balance_multi_currency(txns)` | Per-currency balance verification |
| `to_hledger(txns, account)` | Export to hledger journal format |
| `to_beancount(txns, account)` | Export to beancount journal format |

### Data Classes

| Class | Purpose |
|---|---|
| `Deduplicator` | Detect duplicate transactions |
| `DeduplicationResult` | Result with unique, exact, and suspected matches |
| `InputValidator` | Validate file paths and formats |
| `Transaction` | Normalised transaction record |
| `FileResult` | Result from parallel parsing |
| `ZipXMLSource` | ZIP member wrapper |
| `IngestResult` | Hybrid pipeline result with verification |
| `VerificationResult` | Balance verification outcome |
| `Categorizer` | LLM-powered transaction categorisation |
| `AccountMapper` | Regex-based account mapping rules |

### Exceptions

| Exception | When Raised |
|---|---|
| `ParserError` | Parsing failures |
| `ExportError` | Export failures (CSV/JSON/Excel) |
| `ValidationError` | Input validation failures |
| `ZipSecurityError` | ZIP security check failures |
