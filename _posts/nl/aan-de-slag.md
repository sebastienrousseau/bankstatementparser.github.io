---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Een wit gebouw met zwarte ramen"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/daniele-franchi-Vl6YuVBLEys.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Parser voor bankafschriften. Alle rechten voorbehouden."
date: "Apr 01, 2026"
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

- Python 3.9 tot 3.14
- Terminaltoegang (macOS, Linux of WSL)

## Installeren

```bash
pip install bankstatementparser
```

Voor Polars DataFrame-ondersteuning:

```bash
pip install bankstatementparser[polars]
```

## Snelle start

### Elk formaat automatisch detecteren en parseren

```python
from bankstatementparser import create_parser, detect_statement_format

fmt = detect_statement_format("transactions.ofx")
parser = create_parser("transactions.ofx", fmt)
df = parser.parse()  # pandas DataFrame
print(df.head())
```

Dit werkt met`.xml`(CAMT/PIJN.001),`.csv`, `.ofx`, `.qfx`, `.mt940`, En`.sta`bestanden.

### CAMT.053 parseren

```python
from bankstatementparser import CamtParser

parser = CamtParser("statement.xml")
transactions = parser.parse()
```

### Parseer PAIN.001

```python
from bankstatementparser import Pain001Parser

parser = Pain001Parser("payment.xml")
payments = parser.parse()
```

## Grote bestanden streamen

Voor bestanden met duizenden transacties kunt u streaming gebruiken om het geheugen beperkt te houden:

```python
parser = CamtParser("large_statement.xml")
for transaction in parser.parse_streaming(redact_pii=True):
    process(transaction)  # Memory stays constant
```

## Parseren in het geheugen

Parseren van bytes zonder schijf-I/O - handig voor SFTP- of API-workflows:

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

## Ontdubbeling

Detecteer exacte duplicaten en vermoedelijke overeenkomsten met betrouwbaarheidsscores:

```python
from bankstatementparser import CamtParser, Deduplicator

parser = CamtParser("statement.xml")
dedup = Deduplicator()
result = dedup.deduplicate(dedup.from_dataframe(parser.parse()))

print(f"Unique: {len(result.unique_transactions)}")
print(f"Exact duplicates: {len(result.exact_duplicates)}")
print(f"Suspected matches: {len(result.suspected_matches)}")
```

## Veilige ZIP-verwerking

Verwerk gecomprimeerde XML-bestanden met ingebouwde veiligheidscontroles (bombeveiliging, afwijzing van gecodeerde toegang):

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
```

## CLI-gebruik

```bash
# Parse and display
python -m bankstatementparser.cli --type camt --input statement.xml

# Export to CSV
python -m bankstatementparser.cli --type camt --input statement.xml --output transactions.csv

# Stream with PII visible
python -m bankstatementparser.cli --type camt --input statement.xml --streaming --show-pii
```

CLI-opties:

- `--type {camt,pain001}`-- parsertype
-`--input <path>`--invoerbestand
-`--output <csv_path>`-- exporteren naar CSV
-`--streaming`- grote bestanden streamen
-`--show-pii`-- gevoelige velden tonen (standaard geredigeerd)
-`--max-size <MB>`--limiet bestandsgrootte

## Lokale ontwikkeling instellen

```bash
git clone https://github.com/sebastienrousseau/bankstatementparser.git
cd bankstatementparser
python3 -m venv .venv && source .venv/bin/activate
pip install poetry && poetry install --with dev
```

Voer het testpakket uit:

```bash
pytest
```

## API-referentie

### Parser-klassen

| Klas | Formaat | Importeren |
|---|---|---|
| `CamtParser` | CAMT.053 (ISO 20022) | `from bankstatementparser import CamtParser` |
| `Pain001Parser` | PAIN.001 (ISO 20022) | `from bankstatementparser import Pain001Parser` |
| `CsvStatementParser` | CSV | `from bankstatementparser import CsvStatementParser` |
| `OfxParser` | OFX | `from bankstatementparser import OfxParser` |
| `QfxParser` | QFX | `from bankstatementparser import QfxParser` |
| `Mt940Parser` | MT940 | `from bankstatementparser import Mt940Parser` |

### Nutsfuncties

| Functie | Doel |
|---|---|
| `detect_statement_format(path)` | Bestandsformaat automatisch detecteren |
| `create_parser(path, fmt)` | Maak de juiste parser |
| `parse_files_parallel(paths)` | Parseer meerdere bestanden tegelijkertijd |
| `iter_secure_xml_entries(zip_path)` | Herhaal ZIP-vermeldingen veilig |

### Gegevensklassen

| Klas | Doel |
|---|---|
| `Deduplicator` | Detecteer dubbele transacties |
| `DeduplicationResult` | Resultaat met unieke, exacte en vermoedelijke overeenkomsten |
| `InputValidator` | Valideer bestandspaden en formaten |
| `Transaction` | Genormaliseerd transactierecord |
| `FileResult` | Resultaat van parallelle parsering |
| `ZipXMLSource` | ZIP-ledenverpakking |

### Uitzonderingen

| Uitzondering | Wanneer opgevoed |
|---|---|
| `ParserError` | Parseerfouten |
| `ExportError` | Exportfouten (CSV/JSON/Excel) |
| `ValidationError` | Fouten bij invoervalidatie |
| `ZipSecurityError` | ZIP-beveiligingscontrole mislukt |
