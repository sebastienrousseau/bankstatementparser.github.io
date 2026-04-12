---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Biały budynek z czarnymi oknami"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/daniele-franchi-Vl6YuVBLEys.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Parser wyciągów bankowych. Wszelkie prawa zastrzeżone."
date: "Apr 11, 2026"
description: "Rozpocznij pracę z analizatorem wyciągów bankowych dla języka Python: zainstaluj, analizuj pliki CAMT/PAIN.001/CSV/OFX/QFX/MT940 i korzystaj ze strumieniowania lub przepływów pracy CLI."
download: ""
format-detection: "telephone=no"
hreflang: "pl"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/pl/pierwsze-kroki/index.html"
image_alt: "Logo Parsera wyciągów bankowych, potężnego narzędzia Pythona przeznaczonego do szybkiego i dokładnego przetwarzania danych finansowych i wydobywania spostrzeżeń."
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "parser wyciągów bankowych, pierwsze kroki, python, CAMT, PAIN.001, CSV, OFX, QFX, MT940, dane finansowe"
language: "pl-PL"
layout: "start"
locale: "pl_PL"
logo_alt: "Logo Parsera wyciągów bankowych, potężnego narzędzia Pythona przeznaczonego do szybkiego i dokładnego przetwarzania danych finansowych i wydobywania spostrzeżeń."
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Pierwsze kroki"
permalink: "https://bankstatementparser.com/pl/pierwsze-kroki/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Rozpocznij tworzenie bezpiecznych aplikacji za pomocą analizatora wyciągów bankowych"
tags: "bank, wyciąg, parser, python, camt, pain001, csv, ofx, qfx, mt940, przesyłanie strumieniowe, cli"
theme_color: "rgb(73, 214, 251)"
title: "Parser wyciągów bankowych: podręcznik instalacji i użytkowania"
url: "https://bankstatementparser.com/pl/pierwsze-kroki/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/pl/pierwsze-kroki/rss.xml"
category: "Oprogramowanie finansowe, biblioteka Pythona, przewodnik programisty"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Rozpocznij pracę z analizatorem wyciągów bankowych dla języka Python: zainstaluj, analizuj pliki CAMT/PAIN.001/CSV/OFX/QFX/MT940 i korzystaj ze strumieniowania lub przepływów pracy CLI."
item_guid: "https://bankstatementparser.com/pl/pierwsze-kroki/rss.xml"
item_link: "https://bankstatementparser.com/pl/pierwsze-kroki/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Parser wyciągów bankowych: podręcznik instalacji i użytkowania"
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
apple-mobile-web-app-title: "Parser wyciągów bankowych: podręcznik instalacji i użytkowania"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Zainstaluj i używaj Parsera wyciągów bankowych do analizowania plików CAMT, PAIN.001, CSV, OFX/QFX i MT940 w języku Python."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logo Parsera wyciągów bankowych, potężnego narzędzia Pythona przeznaczonego do szybkiego i dokładnego przetwarzania danych finansowych i wydobywania spostrzeżeń."
twitter_site: "@wwdseb"
twitter_title: "Parser wyciągów bankowych: podręcznik instalacji i użytkowania"
twitter_url: "https://bankstatementparser.com/pl/pierwsze-kroki/index.html"

# Humans.txt - The Humans.txt front matter (YAML).

author_website: "https://bankstatementparser.com"
author_twitter: "@wwdseb"
author_location: "London, UK"
thanks: "Dziękuję za przeczytanie!"
site_last_updated: "2026-04-01"
site_standards: "HTML5, CSS3, RSS, Atom, JSON, XML, YAML, Markdown, TOML"
site_components: "Shokunin SSG, Shokunin CLI, Shokunin Templates, Shokunin Themes, Kaishi SSG, Kaishi CLI, Kaishi Templates, Kaishi Themes"
site_software: "Shokunin, Rust"

---

## Wymagania

- Python 3.10 do 3.14
- Dostęp do terminala (macOS, Linux lub WSL)

## Instalacja

```bash
# Instalacja podstawowa (tylko parsery deterministyczne)
pip install bankstatementparser
```

Opcjonalne rozszerzenia dla dodatkowych możliwości:

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

## Szybki start

### Automatyczne wykrywanie i parsowanie dowolnego formatu strukturalnego

```python
from bankstatementparser import create_parser, detect_statement_format

fmt = detect_statement_format("transactions.ofx")
parser = create_parser("transactions.ofx", fmt)
df = parser.parse()  # pandas DataFrame
print(df.head())
```

Działa z plikami `.xml` (CAMT/PAIN.001), `.csv`, `.ofx`, `.qfx`, `.mt940` i `.sta`.

### Parsowanie CAMT.053

```python
from bankstatementparser import CamtParser

parser = CamtParser("statement.xml")
transactions = parser.parse()
```

### Parsowanie PAIN.001

```python
from bankstatementparser import Pain001Parser

parser = Pain001Parser("payment.xml")
payments = parser.parse()
```

### Parsowanie wyciągów bankowych PDF (hybrydowy pipeline)

Hybrydowy pipeline inteligentnie kieruje pliki PDF przez trzy ścieżki ekstrakcji:

```python
from bankstatementparser.hybrid import smart_ingest

result = smart_ingest("statement.pdf")
print(result.source_method)         # "deterministic" | "llm" | "vision"
print(result.verification.status)   # VERIFIED | DISCREPANCY | FAILED
print(result.transactions)          # List of extracted transactions
```

Każda ekstrakcja jest weryfikowana za pomocą **Golden Rule**: `opening + credits − debits == closing`.

## Streaming dużych plików

Dla plików z tysiącami transakcji użyj streaming, aby ograniczyć zużycie pamięci:

```python
parser = CamtParser("large_statement.xml")
for transaction in parser.parse_streaming(redact_pii=True):
    process(transaction)  # Memory stays constant
```

## Parsowanie w pamięci

Parsowanie z bajtów bez operacji dyskowych — przydatne w przepływach SFTP lub API:

```python
xml_bytes = download_from_sftp()
parser = CamtParser.from_bytes(xml_bytes, source_name="daily.xml")
transactions = parser.parse()
```

## Równoległe przetwarzanie plików

Parsowanie wielu plików jednocześnie:

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

## Masowe skanowanie katalogów

Przetwarzanie całych drzew folderów z automatyczną deduplikacją:

```python
from bankstatementparser.hybrid import scan_and_ingest

batch = scan_and_ingest("statements/2026/", pattern="**/*.pdf")
print(f"Processed: {len(batch.results)} files")
print(f"Unique transactions: {batch.unique_count}")
```

## Deduplikacja

Idempotentne hash transakcji do bezpiecznego przyrostowego importu:

```python
from bankstatementparser import CamtParser, Deduplicator

parser = CamtParser("statement.xml")
dedup = Deduplicator()
result = dedup.deduplicate(dedup.from_dataframe(parser.parse()))

print(f"Unique: {len(result.unique_transactions)}")
print(f"Exact duplicates: {len(result.exact_duplicates)}")
print(f"Suspected matches: {len(result.suspected_matches)}")
```

## Kategoryzacja transakcji (wzbogacanie)

Automatyczna kategoryzacja transakcji z użyciem klasyfikacji opartej na LLM:

```python
from bankstatementparser.enrichment import Categorizer

categorizer = Categorizer()
enriched = categorizer.categorize_batch(transactions)
for txn in enriched:
    print(f"{txn.description}: {txn.category}")
```

## Eksport do księgi (hledger / beancount)

Eksport transakcji do formatów plaintext-accounting:

```python
from bankstatementparser.export import to_hledger, to_beancount

journal = to_hledger(transactions, account="Assets:Bank:Checking")
beancount_journal = to_beancount(transactions, account="Assets:Bank:Checking")
```

## Wielowalutowa weryfikacja salda

Niezależna weryfikacja salda dla każdej grupy walutowej:

```python
from bankstatementparser.hybrid import verify_balance_multi_currency

results = verify_balance_multi_currency(transactions)
for currency, verification in results.items():
    print(f"{currency}: {verification.status}")
```

## REST API

Wdrożenie jako mikroserwis FastAPI:

```bash
# Start the API server
bankstatementparser-api --port 8000

# For container deployments
bankstatementparser-api --host 0.0.0.0 --port 9000
```

Endpointy:
- `POST /ingest` -- Parsowanie pliku wyciągu bankowego
- `GET /health` -- Sprawdzenie stanu

## Bezpieczne przetwarzanie ZIP

Przetwarzanie spakowanych plików XML z wbudowanymi kontrolami bezpieczeństwa (ochrona przed bombami, odrzucanie zaszyfrowanych wpisów):

```python
from bankstatementparser import iter_secure_xml_entries, CamtParser

for entry in iter_secure_xml_entries("statements.zip"):
    parser = CamtParser.from_bytes(entry.xml_bytes, source_name=entry.source_name)
    print(f"{entry.source_name}: {len(parser.parse())} transactions")
```

## Eksport

```python
parser = CamtParser("statement.xml")
parser.export_csv("output.csv")
parser.export_json("output.json")

# Polars (requires bankstatementparser[polars])
polars_df = parser.to_polars()

# Excel
parser.camt_to_excel("output.xlsx")
```

## Użycie CLI

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

Opcje CLI:

- `--type {camt,pain001,ingest,review}` -- typ parsera lub tryb
- `--input <path>` -- plik wejściowy
- `--output <path>` -- plik eksportu (CSV lub JSON)
- `--streaming` -- streaming dużych plików
- `--show-pii` -- pokaż wrażliwe pola (domyślnie zredagowane)
- `--max-size <MB>` -- limit rozmiaru pliku

## Konfiguracja lokalnego środowiska deweloperskiego

```bash
git clone https://github.com/sebastienrousseau/bankstatementparser.git
cd bankstatementparser
python3 -m venv .venv && source .venv/bin/activate
pip install poetry && poetry install --with dev
make install-hooks   # pre-commit hook runs `make verify` before every commit
```

Uruchomienie zestawu testów:

```bash
pytest
```

## Dokumentacja API

### Klasy parserów

| Klasa | Format | Import |
|---|---|---|
| `CamtParser` | CAMT.053 (ISO 20022) | `from bankstatementparser import CamtParser` |
| `Pain001Parser` | PAIN.001 (ISO 20022) | `from bankstatementparser import Pain001Parser` |
| `CsvStatementParser` | CSV | `from bankstatementparser import CsvStatementParser` |
| `OfxParser` | OFX | `from bankstatementparser import OfxParser` |
| `QfxParser` | QFX | `from bankstatementparser import QfxParser` |
| `Mt940Parser` | MT940 | `from bankstatementparser import Mt940Parser` |
| `smart_ingest()` | PDF (hybrydowy pipeline) | `from bankstatementparser.hybrid import smart_ingest` |

### Funkcje pomocnicze

| Funkcja | Przeznaczenie |
|---|---|
| `detect_statement_format(path)` | Automatyczne wykrywanie formatu pliku |
| `create_parser(path, fmt)` | Tworzenie odpowiedniego parsera |
| `parse_files_parallel(paths)` | Parsowanie wielu plików jednocześnie |
| `iter_secure_xml_entries(zip_path)` | Bezpieczna iteracja wpisów ZIP |
| `smart_ingest(path)` | Hybrydowa ekstrakcja PDF z weryfikacją |
| `scan_and_ingest(dir, pattern)` | Masowe skanowanie katalogów |
| `verify_balance_multi_currency(txns)` | Weryfikacja salda dla każdej waluty |
| `to_hledger(txns, account)` | Eksport do formatu hledger |
| `to_beancount(txns, account)` | Eksport do formatu beancount |

### Klasy danych

| Klasa | Przeznaczenie |
|---|---|
| `Deduplicator` | Wykrywanie duplikatów transakcji |
| `DeduplicationResult` | Wynik z unikalnymi, dokładnymi i podejrzanymi dopasowaniami |
| `InputValidator` | Walidacja ścieżek i formatów plików |
| `Transaction` | Znormalizowany rekord transakcji |
| `FileResult` | Wynik parsowania równoległego |
| `ZipXMLSource` | Wrapper członka ZIP |
| `IngestResult` | Wynik hybrydowego pipeline z weryfikacją |
| `VerificationResult` | Wynik weryfikacji salda |
| `Categorizer` | Kategoryzacja transakcji z użyciem LLM |
| `AccountMapper` | Reguły mapowania kont oparte na wyrażeniach regularnych |

### Wyjątki

| Wyjątek | Kiedy zgłaszany |
|---|---|
| `ParserError` | Błędy parsowania |
| `ExportError` | Błędy eksportu (CSV/JSON/Excel) |
| `ValidationError` | Błędy walidacji danych wejściowych |
| `ZipSecurityError` | Niepowodzenie kontroli bezpieczeństwa ZIP |
