---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Farin gini mai baƙar fata"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/daniele-franchi-Vl6YuVBLEys.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Fassarar Bayanin Banki. An kiyaye duk haƙƙoƙi."
date: "Apr 01, 2026"
description: "Fara da Parser Statement Parser na Banki don Python: shigar, rarraba fayilolin CAMT/PAIN.001/CSV/OFX/QFX/MT940, da amfani da yawo ko ayyukan CLI."
download: ""
format-detection: "telephone=no"
hreflang: "ha"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/ha/premiers-pas/index.html"
image_alt: "Tambarin Mai nazarin bayanin banki, ƙaƙƙarfan kayan aikin Python wanda aka ƙera don saurin sarrafa bayanai na kuɗi da sauri da kuma haƙar haske."
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "bayanin bayanin banki, farawa, Python, CAMT, PAIN.001, CSV, OFX, QFX, MT940, bayanan kuɗi"
language: "ha-NG"
layout: "start"
locale: "ha_NG"
logo_alt: "Tambarin Mai nazarin bayanin banki, ƙaƙƙarfan kayan aikin Python wanda aka ƙera don saurin sarrafa bayanai na kuɗi da sauri da kuma haƙar haske."
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Farawa"
permalink: "https://bankstatementparser.com/ha/premiers-pas/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Fara Gina Amintattun Aikace-aikace tare da Fassarar Bayanin Banki"
tags: "banki, sanarwa, parser, Python, Camt, Pain001, csv,ofx,qfx,mt940,streaming,cli"
theme_color: "rgb(73, 214, 251)"
title: "Fassarar Bayanin Banki: Shigarwa da Jagorar Amfani"
url: "https://bankstatementparser.com/ha/premiers-pas/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/ha/premiers-pas/rss.xml"
category: "Software na Kuɗi, Laburaren Python, Jagorar Mai Haɓakawa"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Fara da Parser Statement Parser na Banki don Python: shigar, rarraba fayilolin CAMT/PAIN.001/CSV/OFX/QFX/MT940, da amfani da yawo ko ayyukan CLI."
item_guid: "https://bankstatementparser.com/ha/premiers-pas/rss.xml"
item_link: "https://bankstatementparser.com/ha/premiers-pas/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Fassarar Bayanin Banki: Shigarwa da Jagorar Amfani"
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
apple-mobile-web-app-title: "Fassarar Bayanin Banki: Shigarwa da Jagorar Amfani"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Shigar da amfani da Parser Bayanin Banki don tantance fayilolin CAMT, PAIN.001, CSV, OFX/QFX, da MT940 a cikin Python."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Tambarin Mai nazarin bayanin banki, ƙaƙƙarfan kayan aikin Python wanda aka ƙera don saurin sarrafa bayanai na kuɗi da sauri da kuma haƙar haske."
twitter_site: "@wwdseb"
twitter_title: "Fassarar Bayanin Banki: Shigarwa da Jagorar Amfani"
twitter_url: "https://bankstatementparser.com/ha/premiers-pas/index.html"

# Humans.txt - The Humans.txt front matter (YAML).

author_website: "https://bankstatementparser.com"
author_twitter: "@wwdseb"
author_location: "London, UK"
thanks: "Na gode da karantawa!"
site_last_updated: "2026-04-01"
site_standards: "HTML5, CSS3, RSS, Atom, JSON, XML, YAML, Markdown, TOML"
site_components: "Shokunin SSG, Shokunin CLI, Shokunin Templates, Shokunin Themes, Kaishi SSG, Kaishi CLI, Kaishi Templates, Kaishi Themes"
site_software: "Shokunin, Rust"

---

## Bukatun

- Python 3.9 zuwa 3.14
- Samun damar shiga (macOS, Linux, ko WSL)

## Shigar

```bash
pip install bankstatementparser
```

Don tallafin Polars DataFrame:

```bash
pip install bankstatementparser[polars]
```

## Gaggauta Farawa

### Gano Kai-da-kai da Rarraba Duk wani Tsarin

```python
from bankstatementparser import create_parser, detect_statement_format

fmt = detect_statement_format("transactions.ofx")
parser = create_parser("transactions.ofx", fmt)
df = parser.parse()  # pandas DataFrame
print(df.head())
```

Wannan yana aiki da`.xml`(CAMT/PAIN.001),`.csv`, `.ofx`, `.qfx`, `.mt940`, kuma`.sta`fayiloli.

### Fassarar CAMT.053

```python
from bankstatementparser import CamtParser

parser = CamtParser("statement.xml")
transactions = parser.parse()
```

### Fassarar PIN.001

```python
from bankstatementparser import Pain001Parser

parser = Pain001Parser("payment.xml")
payments = parser.parse()
```

## Manyan Fayilolin Yawo

Don fayiloli tare da dubban ma'amaloli, yi amfani da yawo don kiyaye iyakacin ƙwaƙwalwar ajiya:

```python
parser = CamtParser("large_statement.xml")
for transaction in parser.parse_streaming(redact_pii=True):
    process(transaction)  # Memory stays constant
```

## Fassarar A-Memory

Rarraba daga bytes ba tare da faifai I/O ba -- mai amfani ga SFTP ko ayyukan API:

```python
xml_bytes = download_from_sftp()
parser = CamtParser.from_bytes(xml_bytes, source_name="daily.xml")
transactions = parser.parse()
```

## Tsarin Fayil na Daidaitawa

Fassara fayiloli da yawa a lokaci guda:

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

## Ragewa

Gano ainihin kwafi da matches da ake zargi tare da ƙima mai ƙarfi:

```python
from bankstatementparser import CamtParser, Deduplicator

parser = CamtParser("statement.xml")
dedup = Deduplicator()
result = dedup.deduplicate(dedup.from_dataframe(parser.parse()))

print(f"Unique: {len(result.unique_transactions)}")
print(f"Exact duplicates: {len(result.exact_duplicates)}")
print(f"Suspected matches: {len(result.suspected_matches)}")
```

## Amintaccen Tsarin ZIP

Tsara fayilolin XML da aka zub da su tare da ginanniyar binciken tsaro (kariyar bam, ƙirƙirar shigar da ɓoye):

```python
from bankstatementparser import iter_secure_xml_entries, CamtParser

for entry in iter_secure_xml_entries("statements.zip"):
    parser = CamtParser.from_bytes(entry.xml_bytes, source_name=entry.source_name)
    print(f"{entry.source_name}: {len(parser.parse())} transactions")
```

## fitarwa

```python
parser = CamtParser("statement.xml")
parser.export_csv("output.csv")
parser.export_json("output.json")

# Polars (requires bankstatementparser[polars])
polars_df = parser.to_polars()
```

## Amfanin CLI

```bash
# Parse and display
python -m bankstatementparser.cli --type camt --input statement.xml

# Export to CSV
python -m bankstatementparser.cli --type camt --input statement.xml --output transactions.csv

# Stream with PII visible
python -m bankstatementparser.cli --type camt --input statement.xml --streaming --show-pii
```

Zaɓuɓɓukan CLI:

- `--type {camt,pain001}`-- nau'in parser
-`--input <path>`-- fayil ɗin shigarwa
-`--output <csv_path>`-- fitarwa zuwa CSV
-`--streaming`-- jera manyan fayiloli
-`--show-pii`-- nuna filaye masu mahimmanci (wanda aka gyara ta tsohuwa)
-`--max-size <MB>`-- iyakar girman fayil

## Saitin Ci gaban Gida

```bash
git clone https://github.com/sebastienrousseau/bankstatementparser.git
cd bankstatementparser
python3 -m venv .venv && source .venv/bin/activate
pip install poetry && poetry install --with dev
```

Gudanar da gwajin gwaji:

```bash
pytest
```

## Bayanin API

### Darussan Fassara

| Class | Tsarin | Shigo da |
|---|---|---|
| `CamtParser` | CAMT.053 (ISO 20022) | `from bankstatementparser import CamtParser` |
| `Pain001Parser` | PAIN.001 (ISO 20022) | `from bankstatementparser import Pain001Parser` |
| `CsvStatementParser` | CSV | `from bankstatementparser import CsvStatementParser` |
| `OfxParser` | OFX | `from bankstatementparser import OfxParser` |
| `QfxParser` | QFX | `from bankstatementparser import QfxParser` |
| `Mt940Parser` | Farashin MT940 | `from bankstatementparser import Mt940Parser` |

### Ayyukan Amfani

| Aiki | Manufar |
|---|---|
| `detect_statement_format(path)` | Gano tsarin fayil ta atomatik |
| `create_parser(path, fmt)` | Ƙirƙirar fassar da ta dace |
| `parse_files_parallel(paths)` | Fassara fayiloli da yawa a lokaci guda |
| `iter_secure_xml_entries(zip_path)` | Maimaita shigarwar ZIP amintacce |

### Data Classes

| Class | Manufar |
|---|---|
| `Deduplicator` | Gano kwafin ma'amaloli |
| `DeduplicationResult` | Sakamako tare da na musamman, daidai, da matches da ake zargi |
| `InputValidator` | Tabbatar da hanyoyin fayil da tsari |
| `Transaction` | Daidaitaccen rikodin ma'amala |
| `FileResult` | Sakamako daga layi daya |
| `ZipXMLSource` | Kundin memba na ZIP |

### Banda

| Banda | Lokacin Tashe |
|---|---|
| `ParserError` | Fassara gazawar |
| `ExportError` | Kasawar fitarwa (CSV/JSON/Excel) |
| `ValidationError` | gazawar tabbatar da shigarwa |
| `ZipSecurityError` | ZIP tsaro ya gaza |
