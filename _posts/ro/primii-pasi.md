---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "O clădire albă cu ferestre negre"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/daniele-franchi-Vl6YuVBLEys.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Analizator extras de cont. Toate drepturile rezervate."
date: "Apr 01, 2026"
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

- Python 3.9 până la 3.14
- Acces la terminal (macOS, Linux sau WSL)

## Instalează

```bash
pip install bankstatementparser
```

Pentru suportul Polars DataFrame:

```bash
pip install bankstatementparser[polars]
```

## Pornire rapidă

### Detectează automat și analizează orice format

```python
from bankstatementparser import create_parser, detect_statement_format

fmt = detect_statement_format("transactions.ofx")
parser = create_parser("transactions.ofx", fmt)
df = parser.parse()  # pandas DataFrame
print(df.head())
```

Aceasta funcționează cu`.xml`(CAMT/PAIN.001),`.csv`, `.ofx`, `.qfx`, `.mt940`, și`.sta`fişiere.

### Analizați CAMT.053

```python
from bankstatementparser import CamtParser

parser = CamtParser("statement.xml")
transactions = parser.parse()
```

### Analizează PAIN.001

```python
from bankstatementparser import Pain001Parser

parser = Pain001Parser("payment.xml")
payments = parser.parse()
```

## Streaming de fișiere mari

Pentru fișierele cu mii de tranzacții, utilizați fluxul pentru a păstra memoria limitată:

```python
parser = CamtParser("large_statement.xml")
for transaction in parser.parse_streaming(redact_pii=True):
    process(transaction)  # Memory stays constant
```

## Analizare în memorie

Analizați din octeți fără I/O pe disc -- util pentru fluxurile de lucru SFTP sau API:

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

## Deduplicare

Detectați duplicatele exacte și potrivirile suspectate cu scoruri de încredere:

```python
from bankstatementparser import CamtParser, Deduplicator

parser = CamtParser("statement.xml")
dedup = Deduplicator()
result = dedup.deduplicate(dedup.from_dataframe(parser.parse()))

print(f"Unique: {len(result.unique_transactions)}")
print(f"Exact duplicates: {len(result.exact_duplicates)}")
print(f"Suspected matches: {len(result.suspected_matches)}")
```

## Procesare ZIP securizată

Procesați fișierele XML arhivate cu verificări de securitate încorporate (protecție împotriva bombelor, respingerea intrării criptate):

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
```

## Utilizare CLI

```bash
# Parse and display
python -m bankstatementparser.cli --type camt --input statement.xml

# Export to CSV
python -m bankstatementparser.cli --type camt --input statement.xml --output transactions.csv

# Stream with PII visible
python -m bankstatementparser.cli --type camt --input statement.xml --streaming --show-pii
```

Opțiuni CLI:

- `--type {camt,pain001}`-- tip parser
-`--input <path>`-- fișier de intrare
-`--output <csv_path>`-- export în CSV
-`--streaming`-- transmiteți în flux fișiere mari
-`--show-pii`-- afișează câmpurile sensibile (redactate implicit)
-`--max-size <MB>`-- limită de dimensiune a fișierului

## Configurarea dezvoltării locale

```bash
git clone https://github.com/sebastienrousseau/bankstatementparser.git
cd bankstatementparser
python3 -m venv .venv && source .venv/bin/activate
pip install poetry && poetry install --with dev
```

Rulați suita de teste:

```bash
pytest
```

## Referință API

### Clase de analizator

| Clasă | Format | Import |
|---|---|---|
| `CamtParser` | CAMT.053 (ISO 20022) | `from bankstatementparser import CamtParser` |
| `Pain001Parser` | PAIN.001 (ISO 20022) | `from bankstatementparser import Pain001Parser` |
| `CsvStatementParser` | CSV | `from bankstatementparser import CsvStatementParser` |
| `OfxParser` | OFX | `from bankstatementparser import OfxParser` |
| `QfxParser` | QFX | `from bankstatementparser import QfxParser` |
| `Mt940Parser` | MT940 | `from bankstatementparser import Mt940Parser` |

### Funcții utilitare

| Funcţie | Scop |
|---|---|
| `detect_statement_format(path)` | Detectează automat formatul de fișier |
| `create_parser(path, fmt)` | Creați analizatorul adecvat |
| `parse_files_parallel(paths)` | Analizați mai multe fișiere simultan |
| `iter_secure_xml_entries(zip_path)` | Repetați intrările ZIP în siguranță |

### Clase de date

| Clasă | Scop |
|---|---|
| `Deduplicator` | Detectează tranzacțiile duplicate |
| `DeduplicationResult` | Rezultat cu potriviri unice, exacte și suspectate |
| `InputValidator` | Validați căile și formatele fișierelor |
| `Transaction` | Înregistrare normalizată a tranzacțiilor |
| `FileResult` | Rezultat din analiza paralelă |
| `ZipXMLSource` | Înveliș pentru membri ZIP |

### Excepții

| Excepţie | Când este Ridicat |
|---|---|
| `ParserError` | Eșecurile de analiză |
| `ExportError` | Eșecuri la export (CSV/JSON/Excel) |
| `ValidationError` | Eșecuri de validare a intrărilor |
| `ZipSecurityError` | Eșecuri ale verificării de securitate ZIP |
