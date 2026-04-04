---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "En vit byggnad med svarta fönster"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/daniele-franchi-Vl6YuVBLEys.webp"
cdn: "https://cloudcdn.pro"
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Bank Statement Parser. Alla rättigheter reserverade."
date: "Apr 01, 2026"
description: "Kom igång med Bank Statement Parser för Python: installera, analysera CAMT/PAIN.001/CSV/OFX/QFX/MT940-filer och använd streaming- eller CLI-arbetsflöden."
download: ""
format-detection: "telephone=no"
hreflang: "sv"
icon: "https://cloudcdn.pro/bankstatementparser/images/favicon.ico"
id: "https://bankstatementparser.com/sv/premiers-pas/index.html"
image_alt: "Logotypen för Bank Statement Parser, ett kraftfullt Python-verktyg designat för snabb och korrekt finansiell databearbetning och extraktion av insikter."
image_height: "630"
image_width: "1200"
image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
keywords: "kontoutdragsparser, komma igång, python, CAMT, PAIN.001, CSV, OFX, QFX, MT940, finansiell data"
language: "sv-SE"
layout: "start"
locale: "sv_SE"
logo_alt: "Logotypen för Bank Statement Parser, ett kraftfullt Python-verktyg designat för snabb och korrekt finansiell databearbetning och extraktion av insikter."
logo_height: "44"
logo_width: "44"
logo: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
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
msapplication_tile_image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Installera och använd Bank Statement Parser för att analysera CAMT-, PAIN.001-, CSV-, OFX/QFX- och MT940-filer i Python."
twitter_image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
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

- Python 3.9 till 3.14
- Terminalåtkomst (macOS, Linux eller WSL)

## Installera

```bash
pip install bankstatementparser
```

För Polars DataFrame-stöd:

```bash
pip install bankstatementparser[polars]
```

## Snabbstart

### Autoupptäck och analysera alla format

```python
from bankstatementparser import create_parser, detect_statement_format

fmt = detect_statement_format("transactions.ofx")
parser = create_parser("transactions.ofx", fmt)
df = parser.parse()  # pandas DataFrame
print(df.head())
```

Detta fungerar med`.xml`(CAMT/PAIN.001),`.csv`, `.ofx`, `.qfx`, `.mt940`, och`.sta`filer.

### Analysera CAMT.053

```python
from bankstatementparser import CamtParser

parser = CamtParser("statement.xml")
transactions = parser.parse()
```

### Analysera PAIN.001

```python
from bankstatementparser import Pain001Parser

parser = Pain001Parser("payment.xml")
payments = parser.parse()
```

## Strömmande stora filer

För filer med tusentals transaktioner, använd streaming för att hålla minnet begränsat:

```python
parser = CamtParser("large_statement.xml")
for transaction in parser.parse_streaming(redact_pii=True):
    process(transaction)  # Memory stays constant
```

## In-Memory Parsing

Analysera från byte utan disk I/O -- användbart för SFTP- eller API-arbetsflöden:

```python
xml_bytes = download_from_sftp()
parser = CamtParser.from_bytes(xml_bytes, source_name="daily.xml")
transactions = parser.parse()
```

## Parallell filbehandling

Analysera flera filer samtidigt:

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

## Deduplicering

Upptäck exakta dubbletter och misstänkta matchningar med konfidenspoäng:

```python
from bankstatementparser import CamtParser, Deduplicator

parser = CamtParser("statement.xml")
dedup = Deduplicator()
result = dedup.deduplicate(dedup.from_dataframe(parser.parse()))

print(f"Unique: {len(result.unique_transactions)}")
print(f"Exact duplicates: {len(result.exact_duplicates)}")
print(f"Suspected matches: {len(result.suspected_matches)}")
```

## Säker ZIP-bearbetning

Bearbeta zippade XML-filer med inbyggda säkerhetskontroller (bombskydd, krypterad inmatningsavvisning):

```python
from bankstatementparser import iter_secure_xml_entries, CamtParser

for entry in iter_secure_xml_entries("statements.zip"):
    parser = CamtParser.from_bytes(entry.xml_bytes, source_name=entry.source_name)
    print(f"{entry.source_name}: {len(parser.parse())} transactions")
```

## Exportera

```python
parser = CamtParser("statement.xml")
parser.export_csv("output.csv")
parser.export_json("output.json")

# Polars (requires bankstatementparser[polars])
polars_df = parser.to_polars()
```

## CLI-användning

```bash
# Parse and display
python -m bankstatementparser.cli --type camt --input statement.xml

# Export to CSV
python -m bankstatementparser.cli --type camt --input statement.xml --output transactions.csv

# Stream with PII visible
python -m bankstatementparser.cli --type camt --input statement.xml --streaming --show-pii
```

CLI-alternativ:

- `--type {camt,pain001}`-- parsertyp
-`--input <path>`-- indatafil
-`--output <csv_path>`-- exportera till CSV
-`--streaming`-- streama stora filer
-`--show-pii`-- visa känsliga fält (redigerad som standard)
-`--max-size <MB>`-- filstorleksgräns

## Lokal utveckling Setup

```bash
git clone https://github.com/sebastienrousseau/bankstatementparser.git
cd bankstatementparser
python3 -m venv .venv && source .venv/bin/activate
pip install poetry && poetry install --with dev
```

Kör testsviten:

```bash
pytest
```

## API-referens

### Parser-klasser

| Klass | Formatera | Importera |
|---|---|---|
| `CamtParser` | CAMT.053 (ISO 20022) | `from bankstatementparser import CamtParser` |
| `Pain001Parser` | PAIN.001 (ISO 20022) | `from bankstatementparser import Pain001Parser` |
| `CsvStatementParser` | CSV | `from bankstatementparser import CsvStatementParser` |
| `OfxParser` | OFX | `from bankstatementparser import OfxParser` |
| `QfxParser` | QFX | `from bankstatementparser import QfxParser` |
| `Mt940Parser` | MT940 | `from bankstatementparser import Mt940Parser` |

### Verktygsfunktioner

| Fungera | Ändamål |
|---|---|
| `detect_statement_format(path)` | Autoupptäck filformat |
| `create_parser(path, fmt)` | Skapa lämplig analysator |
| `parse_files_parallel(paths)` | Analysera flera filer samtidigt |
| `iter_secure_xml_entries(zip_path)` | Iterera ZIP-poster säkert |

### Dataklasser

| Klass | Ändamål |
|---|---|
| `Deduplicator` | Upptäck dubbletter av transaktioner |
| `DeduplicationResult` | Resultat med unika, exakta och misstänkta matchningar |
| `InputValidator` | Validera filsökvägar och format |
| `Transaction` | Normaliserad transaktionspost |
| `FileResult` | Resultat från parallell analys |
| `ZipXMLSource` | ZIP-medlemsomslag |

### Undantag

| Undantag | När uppvuxen |
|---|---|
| `ParserError` | Analysfel |
| `ExportError` | Exportfel (CSV/JSON/Excel) |
| `ValidationError` | Indatavalideringsfel |
| `ZipSecurityError` | ZIP säkerhetskontroll misslyckades |
