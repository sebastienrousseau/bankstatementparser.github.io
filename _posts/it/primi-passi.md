---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Un edificio bianco con finestre nere"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/daniele-franchi-Vl6YuVBLEys.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Analizzatore di estratti conto bancari. Tutti i diritti riservati."
date: "Apr 11, 2026"
description: "Inizia con Bank Statement Parser per Python: installa, analizza file CAMT/PAIN.001/CSV/OFX/QFX/MT940 e utilizza flussi di lavoro in streaming o CLI."
download: ""
format-detection: "telephone=no"
hreflang: "it"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/it/primi-passi/index.html"
image_alt: "Logo di Bank Statement Parser, un potente strumento Python progettato per l'elaborazione rapida e accurata dei dati finanziari e l'estrazione di informazioni approfondite."
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "analizzatore di estratti conto, guida introduttiva, Python, CAMT, PAIN.001, CSV, OFX, QFX, MT940, dati finanziari"
language: "it-IT"
layout: "start"
locale: "it_IT"
logo_alt: "Logo di Bank Statement Parser, un potente strumento Python progettato per l'elaborazione rapida e accurata dei dati finanziari e l'estrazione di informazioni approfondite."
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Iniziare"
permalink: "https://bankstatementparser.com/it/primi-passi/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Inizia a creare applicazioni sicure con il parser di estratti conto bancari"
tags: "banca,istruzione,parser,python,camt,pain001,csv,ofx,qfx,mt940,streaming,cli"
theme_color: "rgb(73, 214, 251)"
title: "Parser estratto conto: guida all'installazione e all'utilizzo"
url: "https://bankstatementparser.com/it/primi-passi/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/it/primi-passi/rss.xml"
category: "Software finanziario, libreria Python, guida per sviluppatori"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin (version 0.0.20)"
item_description: "Inizia con Bank Statement Parser per Python: installa, analizza file CAMT/PAIN.001/CSV/OFX/QFX/MT940 e utilizza flussi di lavoro in streaming o CLI."
item_guid: "https://bankstatementparser.com/it/primi-passi/rss.xml"
item_link: "https://bankstatementparser.com/it/primi-passi/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Parser estratto conto: guida all'installazione e all'utilizzo"
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
apple-mobile-web-app-title: "Parser estratto conto: guida all'installazione e all'utilizzo"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Installa e utilizza Bank Statement Parser per analizzare file CAMT, PAIN.001, CSV, OFX/QFX e MT940 in Python."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logo di Bank Statement Parser, un potente strumento Python progettato per l'elaborazione rapida e accurata dei dati finanziari e l'estrazione di informazioni approfondite."
twitter_site: "@wwdseb"
twitter_title: "Parser estratto conto: guida all'installazione e all'utilizzo"
twitter_url: "https://bankstatementparser.com/it/primi-passi/index.html"

# Humans.txt - The Humans.txt front matter (YAML).

author_website: "https://bankstatementparser.com"
author_twitter: "@wwdseb"
author_location: "London, UK"
thanks: "Grazie per aver letto!"
site_last_updated: "2026-04-01"
site_standards: "HTML5, CSS3, RSS, Atom, JSON, XML, YAML, Markdown, TOML"
site_components: "Shokunin SSG, Shokunin CLI, Shokunin Templates, Shokunin Themes, Kaishi SSG, Kaishi CLI, Kaishi Templates, Kaishi Themes"
site_software: "Shokunin, Rust"

---

## Requisiti

- Python da 3.10 a 3.14
- Accesso al terminale (macOS, Linux o WSL)

## Installazione

```bash
# Core install (deterministic parsers only)
pip install bankstatementparser
```

Extra opzionali per funzionalità aggiuntive:

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

## Avvio rapido

### Rileva automaticamente e analizza qualsiasi formato strutturato

```python
from bankstatementparser import create_parser, detect_statement_format

fmt = detect_statement_format("transactions.ofx")
parser = create_parser("transactions.ofx", fmt)
df = parser.parse()  # pandas DataFrame
print(df.head())
```

Funziona con file `.xml` (CAMT/PAIN.001), `.csv`, `.ofx`, `.qfx`, `.mt940` e `.sta`.

### Analisi CAMT.053

```python
from bankstatementparser import CamtParser

parser = CamtParser("statement.xml")
transactions = parser.parse()
```

### Analisi PAIN.001

```python
from bankstatementparser import Pain001Parser

parser = Pain001Parser("payment.xml")
payments = parser.parse()
```

### Analisi di estratti conto PDF (pipeline ibrida)

La pipeline ibrida instrada i PDF in modo intelligente su tre percorsi di estrazione:

```python
from bankstatementparser.hybrid import smart_ingest

result = smart_ingest("statement.pdf")
print(result.source_method)         # "deterministic" | "llm" | "vision"
print(result.verification.status)   # VERIFIED | DISCREPANCY | FAILED
print(result.transactions)          # List of extracted transactions
```

Ogni estrazione viene verificata con la **Golden Rule**: `opening + credits − debits == closing`.

## Streaming di file di grandi dimensioni

Per file con migliaia di transazioni, lo streaming mantiene la memoria limitata:

```python
parser = CamtParser("large_statement.xml")
for transaction in parser.parse_streaming(redact_pii=True):
    process(transaction)  # Memory stays constant
```

## Parsing in memoria

Analisi da byte senza I/O su disco — utile per flussi di lavoro SFTP o API:

```python
xml_bytes = download_from_sftp()
parser = CamtParser.from_bytes(xml_bytes, source_name="daily.xml")
transactions = parser.parse()
```

## Elaborazione file in parallelo

Analisi di più file in contemporanea:

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

## Scansione in blocco di cartelle

Elabora intere cartelle con deduplicazione automatica:

```python
from bankstatementparser.hybrid import scan_and_ingest

batch = scan_and_ingest("statements/2026/", pattern="**/*.pdf")
print(f"Processed: {len(batch.results)} files")
print(f"Unique transactions: {batch.unique_count}")
```

## Deduplicazione

Hash idempotenti delle transazioni per un'ingestione incrementale sicura:

```python
from bankstatementparser import CamtParser, Deduplicator

parser = CamtParser("statement.xml")
dedup = Deduplicator()
result = dedup.deduplicate(dedup.from_dataframe(parser.parse()))

print(f"Unique: {len(result.unique_transactions)}")
print(f"Exact duplicates: {len(result.exact_duplicates)}")
print(f"Suspected matches: {len(result.suspected_matches)}")
```

## Categorizzazione delle transazioni (arricchimento)

Categorizzazione automatica delle transazioni tramite classificazione LLM:

```python
from bankstatementparser.enrichment import Categorizer

categorizer = Categorizer()
enriched = categorizer.categorize_batch(transactions)
for txn in enriched:
    print(f"{txn.description}: {txn.category}")
```

## Esportazione contabile (hledger / beancount)

Esporta le transazioni in formato journal per la contabilità plaintext:

```python
from bankstatementparser.export import to_hledger, to_beancount

journal = to_hledger(transactions, account="Assets:Bank:Checking")
beancount_journal = to_beancount(transactions, account="Assets:Bank:Checking")
```

## Verifica saldo multi-valuta

Verifica dei saldi in modo indipendente per ogni gruppo di valuta:

```python
from bankstatementparser.hybrid import verify_balance_multi_currency

results = verify_balance_multi_currency(transactions)
for currency, verification in results.items():
    print(f"{currency}: {verification.status}")
```

## REST API

Deploy come microservizio FastAPI:

```bash
# Start the API server
bankstatementparser-api --port 8000

# For container deployments
bankstatementparser-api --host 0.0.0.0 --port 9000
```

Endpoint:
- `POST /ingest` -- Analizza un file di estratto conto
- `GET /health` -- Controllo stato di salute

## Elaborazione ZIP sicura

Elabora file XML compressi con controlli di sicurezza integrati (protezione anti-bomb, rifiuto di voci crittografate):

```python
from bankstatementparser import iter_secure_xml_entries, CamtParser

for entry in iter_secure_xml_entries("statements.zip"):
    parser = CamtParser.from_bytes(entry.xml_bytes, source_name=entry.source_name)
    print(f"{entry.source_name}: {len(parser.parse())} transactions")
```

## Esportazione

```python
parser = CamtParser("statement.xml")
parser.export_csv("output.csv")
parser.export_json("output.json")

# Polars (requires bankstatementparser[polars])
polars_df = parser.to_polars()

# Excel
parser.camt_to_excel("output.xlsx")
```

## Utilizzo della CLI

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

Opzioni CLI:

- `--type {camt,pain001,ingest,review}` -- tipo di parser o modalità
- `--input <path>` -- file di input
- `--output <path>` -- file di esportazione (CSV o JSON)
- `--streaming` -- streaming per file di grandi dimensioni
- `--show-pii` -- mostra campi sensibili (oscurati di default)
- `--max-size <MB>` -- limite dimensione file

## Configurazione per lo sviluppo locale

```bash
git clone https://github.com/sebastienrousseau/bankstatementparser.git
cd bankstatementparser
python3 -m venv .venv && source .venv/bin/activate
pip install poetry && poetry install --with dev
make install-hooks   # pre-commit hook runs `make verify` before every commit
```

Esegui la suite di test:

```bash
pytest
```

## Riferimento API

### Classi parser

| Classe | Formato | Import |
|---|---|---|
| `CamtParser` | CAMT.053 (ISO 20022) | `from bankstatementparser import CamtParser` |
| `Pain001Parser` | PAIN.001 (ISO 20022) | `from bankstatementparser import Pain001Parser` |
| `CsvStatementParser` | CSV | `from bankstatementparser import CsvStatementParser` |
| `OfxParser` | OFX | `from bankstatementparser import OfxParser` |
| `QfxParser` | QFX | `from bankstatementparser import QfxParser` |
| `Mt940Parser` | MT940 | `from bankstatementparser import Mt940Parser` |
| `smart_ingest()` | PDF (pipeline ibrida) | `from bankstatementparser.hybrid import smart_ingest` |

### Funzioni di utilità

| Funzione | Scopo |
|---|---|
| `detect_statement_format(path)` | Rilevamento automatico del formato file |
| `create_parser(path, fmt)` | Crea il parser appropriato |
| `parse_files_parallel(paths)` | Analizza più file in contemporanea |
| `iter_secure_xml_entries(zip_path)` | Itera le voci ZIP in modo sicuro |
| `smart_ingest(path)` | Estrazione PDF ibrida con verifica |
| `scan_and_ingest(dir, pattern)` | Scansione in blocco di cartelle |
| `verify_balance_multi_currency(txns)` | Verifica saldo per valuta |
| `to_hledger(txns, account)` | Esporta in formato journal hledger |
| `to_beancount(txns, account)` | Esporta in formato journal beancount |

### Classi dati

| Classe | Scopo |
|---|---|
| `Deduplicator` | Rileva transazioni duplicate |
| `DeduplicationResult` | Risultato con corrispondenze univoche, esatte e sospette |
| `InputValidator` | Valida percorsi e formati di file |
| `Transaction` | Record di transazione normalizzato |
| `FileResult` | Risultato dell'analisi parallela |
| `ZipXMLSource` | Wrapper membro ZIP |
| `IngestResult` | Risultato della pipeline ibrida con verifica |
| `VerificationResult` | Esito della verifica del saldo |
| `Categorizer` | Categorizzazione transazioni tramite LLM |
| `AccountMapper` | Regole di mappatura conti basate su regex |

### Eccezioni

| Eccezione | Quando sollevata |
|---|---|
| `ParserError` | Errori di parsing |
| `ExportError` | Errori di esportazione (CSV/JSON/Excel) |
| `ValidationError` | Errori di validazione dell'input |
| `ZipSecurityError` | Errori del controllo di sicurezza ZIP |
