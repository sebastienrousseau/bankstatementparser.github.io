---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Sebuah bangunan putih dengan jendela hitam"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/daniele-franchi-Vl6YuVBLEys.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Pengurai Laporan Bank. Semua hak dilindungi undang-undang."
date: "Apr 01, 2026"
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

-Python 3.9 hingga 3.14
- Akses terminal (macOS, Linux, atau WSL)

## Instal

```bash
pip install bankstatementparser
```

Untuk dukungan Polars DataFrame:

```bash
pip install bankstatementparser[polars]
```

## Mulai Cepat

### Deteksi Otomatis dan Parsing Format Apa Pun

```python
from bankstatementparser import create_parser, detect_statement_format

fmt = detect_statement_format("transactions.ofx")
parser = create_parser("transactions.ofx", fmt)
df = parser.parse()  # pandas DataFrame
print(df.head())
```

Ini berfungsi dengan`.xml`(CAMT / NYERI.001),`.csv`, `.ofx`, `.qfx`, `.mt940`, Dan`.sta`file.

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

## Streaming File Besar

Untuk file dengan ribuan transaksi, gunakan streaming untuk membatasi memori:

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

## Deduplikasi

Deteksi duplikat persis dan dugaan kecocokan dengan skor keyakinan:

```python
from bankstatementparser import CamtParser, Deduplicator

parser = CamtParser("statement.xml")
dedup = Deduplicator()
result = dedup.deduplicate(dedup.from_dataframe(parser.parse()))

print(f"Unique: {len(result.unique_transactions)}")
print(f"Exact duplicates: {len(result.exact_duplicates)}")
print(f"Suspected matches: {len(result.suspected_matches)}")
```

## Pemrosesan ZIP Aman

Proses file XML zip dengan pemeriksaan keamanan bawaan (perlindungan bom, penolakan entri terenkripsi):

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
```

## Penggunaan CLI

```bash
# Parse and display
python -m bankstatementparser.cli --type camt --input statement.xml

# Export to CSV
python -m bankstatementparser.cli --type camt --input statement.xml --output transactions.csv

# Stream with PII visible
python -m bankstatementparser.cli --type camt --input statement.xml --streaming --show-pii
```

Opsi CLI:

- `--type {camt,pain001}`-- tipe pengurai
-`--input <path>`-- memasukkan berkas
-`--output <csv_path>`-- ekspor ke CSV
-`--streaming`-- streaming file besar
-`--show-pii`-- tampilkan bidang sensitif (dihapus secara default)
-`--max-size <MB>`-- batas ukuran file

## Pengaturan Pembangunan Lokal

```bash
git clone https://github.com/sebastienrousseau/bankstatementparser.git
cd bankstatementparser
python3 -m venv .venv && source .venv/bin/activate
pip install poetry && poetry install --with dev
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
| `Pain001Parser` | SAKIT.001 (ISO 20022) | `from bankstatementparser import Pain001Parser` |
| `CsvStatementParser` | CSV | `from bankstatementparser import CsvStatementParser` |
| `OfxParser` | OFX | `from bankstatementparser import OfxParser` |
| `QfxParser` | QFX | `from bankstatementparser import QfxParser` |
| `Mt940Parser` | MT940 | `from bankstatementparser import Mt940Parser` |

### Fungsi Utilitas

| Fungsi | Tujuan |
|---|---|
| `detect_statement_format(path)` | Deteksi otomatis format file |
| `create_parser(path, fmt)` | Buat parser yang sesuai |
| `parse_files_parallel(paths)` | Parsing beberapa file secara bersamaan |
| `iter_secure_xml_entries(zip_path)` | Ulangi entri ZIP dengan aman |

### Kelas Data

| Kelas | Tujuan |
|---|---|
| `Deduplicator` | Deteksi transaksi duplikat |
| `DeduplicationResult` | Hasil dengan kecocokan yang unik, tepat, dan mencurigakan |
| `InputValidator` | Validasi jalur dan format file |
| `Transaction` | Catatan transaksi yang dinormalisasi |
| `FileResult` | Hasil dari penguraian paralel |
| `ZipXMLSource` | Pembungkus anggota ZIP |

### Pengecualian

| Pengecualian | Saat Dibesarkan |
|---|---|
| `ParserError` | Kegagalan penguraian |
| `ExportError` | Kegagalan ekspor (CSV/JSON/Excel) |
| `ValidationError` | Kegagalan validasi masukan |
| `ZipSecurityError` | Kegagalan pemeriksaan keamanan ZIP |
