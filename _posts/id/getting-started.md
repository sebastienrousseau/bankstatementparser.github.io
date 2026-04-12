---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Sebuah bangunan putih dengan jendela hitam"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/daniele-franchi-Vl6YuVBLEys.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Pengurai Laporan Bank. Semua hak dilindungi undang-undang."
date: "Apr 11, 2026"
description: "Mulailah dengan Parser Laporan Bank untuk Python: instal, parsing file CAMT/PAIN.001/CSV/OFX/QFX/MT940, dan gunakan alur kerja streaming atau CLI."
download: ""
format-detection: "telephone=no"
hreflang: "id"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/id/getting-started/index.html"
image_alt: "Logo Parser Laporan Bank, alat Python canggih yang dirancang untuk pemrosesan data keuangan dan ekstraksi wawasan yang cepat dan akurat."
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "pengurai laporan bank, memulai, python, CAMT, PAIN.001, CSV, OFX, QFX, MT940, data keuangan"
language: "id-ID"
layout: "start"
locale: "id_ID"
logo_alt: "Logo Parser Laporan Bank, alat Python canggih yang dirancang untuk pemrosesan data keuangan dan ekstraksi wawasan yang cepat dan akurat."
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Memulai"
permalink: "https://bankstatementparser.com/id/getting-started/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Mulai Membangun Aplikasi Aman dengan Parser Laporan Bank"
tags: "bank,pernyataan,parser,python,camt,pain001,csv,ofx,qfx,mt940,streaming,cli"
theme_color: "rgb(73, 214, 251)"
title: "Parser Laporan Bank: Panduan Instalasi dan Penggunaan"
url: "https://bankstatementparser.com/id/getting-started/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/id/getting-started/rss.xml"
category: "Perangkat Lunak Keuangan, Perpustakaan Python, Panduan Pengembang"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Mulailah dengan Parser Laporan Bank untuk Python: instal, parsing file CAMT/PAIN.001/CSV/OFX/QFX/MT940, dan gunakan alur kerja streaming atau CLI."
item_guid: "https://bankstatementparser.com/id/getting-started/rss.xml"
item_link: "https://bankstatementparser.com/id/getting-started/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Parser Laporan Bank: Panduan Instalasi dan Penggunaan"
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
apple-mobile-web-app-title: "Parser Laporan Bank: Panduan Instalasi dan Penggunaan"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Instal dan gunakan Bank Statement Parser untuk mengurai file CAMT, PAIN.001, CSV, OFX/QFX, dan MT940 dengan Python."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logo Parser Laporan Bank, alat Python canggih yang dirancang untuk pemrosesan data keuangan dan ekstraksi wawasan yang cepat dan akurat."
twitter_site: "@wwdseb"
twitter_title: "Parser Laporan Bank: Panduan Instalasi dan Penggunaan"
twitter_url: "https://bankstatementparser.com/id/getting-started/index.html"

# Humans.txt - The Humans.txt front matter (YAML).

author_website: "https://bankstatementparser.com"
author_twitter: "@wwdseb"
author_location: "London, UK"
thanks: "Terima kasih telah membaca!"
site_last_updated: "2026-04-01"
site_standards: "HTML5, CSS3, RSS, Atom, JSON, XML, YAML, Markdown, TOML"
site_components: "Shokunin SSG, Shokunin CLI, Shokunin Templates, Shokunin Themes, Kaishi SSG, Kaishi CLI, Kaishi Templates, Kaishi Themes"
site_software: "Shokunin, Rust"

---

## Persyaratan

- Python 3.10 hingga 3.14
- Akses terminal (macOS, Linux, atau WSL)

## Instalasi

```bash
# Instalasi inti (parser deterministik saja)
pip install bankstatementparser
```

Ekstra opsional untuk kemampuan tambahan:

```bash
# Jalur Text-LLM untuk PDF digital (litellm + pypdf)
pip install 'bankstatementparser[hybrid]'

# Ekstraksi tabel fidelitas lebih tinggi (menambahkan pdfplumber)
pip install 'bankstatementparser[hybrid-plus]'

# Jalur Vision-LLM untuk PDF hasil pindai (menambahkan pypdfium2)
pip install 'bankstatementparser[hybrid-vision]'

# Kategorisasi transaksi berbasis LLM
pip install 'bankstatementparser[enrichment]'

# Microservice REST API (FastAPI + uvicorn)
pip install 'bankstatementparser[api]'

# Dukungan Polars DataFrame opsional
pip install 'bankstatementparser[polars]'
```

## Mulai Cepat

### Deteksi Otomatis dan Parsing Format Terstruktur Apa Pun

```python
from bankstatementparser import create_parser, detect_statement_format

fmt = detect_statement_format("transactions.ofx")
parser = create_parser("transactions.ofx", fmt)
df = parser.parse()  # pandas DataFrame
print(df.head())
```

Ini berfungsi dengan file `.xml` (CAMT/PAIN.001), `.csv`, `.ofx`, `.qfx`, `.mt940`, dan `.sta`.

### Parsing CAMT.053

```python
from bankstatementparser import CamtParser

parser = CamtParser("statement.xml")
transactions = parser.parse()
```

### Parsing PAIN.001

```python
from bankstatementparser import Pain001Parser

parser = Pain001Parser("payment.xml")
payments = parser.parse()
```

### Parsing Laporan Bank PDF (Pipeline Hibrida)

Pipeline hibrida secara cerdas merutekan PDF melalui tiga jalur ekstraksi:

```python
from bankstatementparser.hybrid import smart_ingest

result = smart_ingest("statement.pdf")
print(result.source_method)         # "deterministic" | "llm" | "vision"
print(result.verification.status)   # VERIFIED | DISCREPANCY | FAILED
print(result.transactions)          # List of extracted transactions
```

Setiap ekstraksi diverifikasi dengan **Golden Rule**: `opening + credits − debits == closing`.

## Streaming File Besar

Untuk file dengan ribuan transaksi, gunakan streaming agar memori tetap terbatas:

```python
parser = CamtParser("large_statement.xml")
for transaction in parser.parse_streaming(redact_pii=True):
    process(transaction)  # Memory stays constant
```

## Parsing Dalam Memori

Parsing dari byte tanpa I/O disk -- berguna untuk alur kerja SFTP atau API:

```python
xml_bytes = download_from_sftp()
parser = CamtParser.from_bytes(xml_bytes, source_name="daily.xml")
transactions = parser.parse()
```

## Pemrosesan File Paralel

Parsing beberapa file secara bersamaan:

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

## Pemindaian Direktori Massal

Proses seluruh pohon folder dengan deduplikasi otomatis:

```python
from bankstatementparser.hybrid import scan_and_ingest

batch = scan_and_ingest("statements/2026/", pattern="**/*.pdf")
print(f"Processed: {len(batch.results)} files")
print(f"Unique transactions: {batch.unique_count}")
```

## Deduplikasi

Hash transaksi idempoten untuk ingesti inkremental yang aman:

```python
from bankstatementparser import CamtParser, Deduplicator

parser = CamtParser("statement.xml")
dedup = Deduplicator()
result = dedup.deduplicate(dedup.from_dataframe(parser.parse()))

print(f"Unique: {len(result.unique_transactions)}")
print(f"Exact duplicates: {len(result.exact_duplicates)}")
print(f"Suspected matches: {len(result.suspected_matches)}")
```

## Kategorisasi Transaksi (Pengayaan)

Kategorikan transaksi secara otomatis menggunakan klasifikasi berbasis LLM:

```python
from bankstatementparser.enrichment import Categorizer

categorizer = Categorizer()
enriched = categorizer.categorize_batch(transactions)
for txn in enriched:
    print(f"{txn.description}: {txn.category}")
```

## Ekspor Ledger (hledger / beancount)

Ekspor transaksi ke format jurnal plaintext-accounting:

```python
from bankstatementparser.export import to_hledger, to_beancount

journal = to_hledger(transactions, account="Assets:Bank:Checking")
beancount_journal = to_beancount(transactions, account="Assets:Bank:Checking")
```

## Verifikasi Saldo Multi-Mata Uang

Verifikasi saldo secara independen per kelompok mata uang:

```python
from bankstatementparser.hybrid import verify_balance_multi_currency

results = verify_balance_multi_currency(transactions)
for currency, verification in results.items():
    print(f"{currency}: {verification.status}")
```

## REST API

Deploy sebagai microservice FastAPI:

```bash
# Start the API server
bankstatementparser-api --port 8000

# For container deployments
bankstatementparser-api --host 0.0.0.0 --port 9000
```

Endpoint:
- `POST /ingest` -- Parsing file laporan bank
- `GET /health` -- Pemeriksaan kesehatan

## Pemrosesan ZIP Aman

Proses file XML dalam ZIP dengan pemeriksaan keamanan bawaan (perlindungan bom, penolakan entri terenkripsi):

```python
from bankstatementparser import iter_secure_xml_entries, CamtParser

for entry in iter_secure_xml_entries("statements.zip"):
    parser = CamtParser.from_bytes(entry.xml_bytes, source_name=entry.source_name)
    print(f"{entry.source_name}: {len(parser.parse())} transactions")
```

## Ekspor

```python
parser = CamtParser("statement.xml")
parser.export_csv("output.csv")
parser.export_json("output.json")

# Polars (requires bankstatementparser[polars])
polars_df = parser.to_polars()

# Excel
parser.camt_to_excel("output.xlsx")
```

## Penggunaan CLI

```bash
# Parsing format terstruktur
bankstatementparser --type camt --input statement.xml
bankstatementparser --type pain001 --input payment.xml

# Pipeline PDF hibrida
bankstatementparser --type ingest --input statement.pdf
bankstatementparser --type ingest --input statement.pdf --output ledger.csv

# Mode tinjauan interaktif
bankstatementparser --type review --input result.json
bankstatementparser --type review --input result.json --output reviewed.json

# Ekspor ke CSV dengan streaming
bankstatementparser --type camt --input statement.xml --output transactions.csv
bankstatementparser --type camt --input statement.xml --streaming --show-pii
```

Opsi CLI:

- `--type {camt,pain001,ingest,review}` -- tipe parser atau mode
- `--input <path>` -- file masukan
- `--output <path>` -- file ekspor (CSV atau JSON)
- `--streaming` -- streaming file besar
- `--show-pii` -- tampilkan bidang sensitif (diredaksi secara default)
- `--max-size <MB>` -- batas ukuran file

## Pengaturan Pengembangan Lokal

```bash
git clone https://github.com/sebastienrousseau/bankstatementparser.git
cd bankstatementparser
python3 -m venv .venv && source .venv/bin/activate
pip install poetry && poetry install --with dev
make install-hooks   # pre-commit hook runs `make verify` before every commit
```

Jalankan rangkaian pengujian:

```bash
pytest
```

## Referensi API

### Kelas Parser

| Kelas | Format | Impor |
|---|---|---|
| `CamtParser` | CAMT.053 (ISO 20022) | `from bankstatementparser import CamtParser` |
| `Pain001Parser` | PAIN.001 (ISO 20022) | `from bankstatementparser import Pain001Parser` |
| `CsvStatementParser` | CSV | `from bankstatementparser import CsvStatementParser` |
| `OfxParser` | OFX | `from bankstatementparser import OfxParser` |
| `QfxParser` | QFX | `from bankstatementparser import QfxParser` |
| `Mt940Parser` | MT940 | `from bankstatementparser import Mt940Parser` |
| `smart_ingest()` | PDF (pipeline hibrida) | `from bankstatementparser.hybrid import smart_ingest` |

### Fungsi Utilitas

| Fungsi | Tujuan |
|---|---|
| `detect_statement_format(path)` | Deteksi otomatis format file |
| `create_parser(path, fmt)` | Buat parser yang sesuai |
| `parse_files_parallel(paths)` | Parsing beberapa file secara bersamaan |
| `iter_secure_xml_entries(zip_path)` | Iterasi entri ZIP dengan aman |
| `smart_ingest(path)` | Ekstraksi PDF hibrida dengan verifikasi |
| `scan_and_ingest(dir, pattern)` | Pemindaian direktori massal |
| `verify_balance_multi_currency(txns)` | Verifikasi saldo per mata uang |
| `to_hledger(txns, account)` | Ekspor ke format jurnal hledger |
| `to_beancount(txns, account)` | Ekspor ke format jurnal beancount |

### Kelas Data

| Kelas | Tujuan |
|---|---|
| `Deduplicator` | Deteksi transaksi duplikat |
| `DeduplicationResult` | Hasil dengan kecocokan unik, tepat, dan dugaan |
| `InputValidator` | Validasi jalur dan format file |
| `Transaction` | Catatan transaksi yang dinormalisasi |
| `FileResult` | Hasil dari penguraian paralel |
| `ZipXMLSource` | Pembungkus anggota ZIP |
| `IngestResult` | Hasil pipeline hibrida dengan verifikasi |
| `VerificationResult` | Hasil verifikasi saldo |
| `Categorizer` | Kategorisasi transaksi berbasis LLM |
| `AccountMapper` | Aturan pemetaan akun berbasis regex |

### Pengecualian

| Pengecualian | Kapan Dipicu |
|---|---|
| `ParserError` | Kegagalan penguraian |
| `ExportError` | Kegagalan ekspor (CSV/JSON/Excel) |
| `ValidationError` | Kegagalan validasi masukan |
| `ZipSecurityError` | Kegagalan pemeriksaan keamanan ZIP |
