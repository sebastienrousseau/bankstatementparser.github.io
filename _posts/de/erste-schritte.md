---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Ein weißes Gebäude mit schwarzen Fenstern"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/daniele-franchi-Vl6YuVBLEys.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Kontoauszugsparser. Alle Rechte vorbehalten."
date: "Apr 01, 2026"
description: "Beginnen Sie mit Bank Statement Parser für Python: Installieren, analysieren Sie CAMT/PAIN.001/CSV/OFX/QFX/MT940-Dateien und verwenden Sie Streaming- oder CLI-Workflows."
download: ""
format-detection: "telephone=no"
hreflang: "de"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/de/erste-schritte/index.html"
image_alt: "Logo von Bank Statement Parser, einem leistungsstarken Python-Tool, das für die schnelle und genaue Verarbeitung von Finanzdaten und die Gewinnung von Erkenntnissen entwickelt wurde."
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "Kontoauszugsparser, Erste Schritte, Python, CAMT, PAIN.001, CSV, OFX, QFX, MT940, Finanzdaten"
language: "de-DE"
layout: "start"
locale: "de_DE"
logo_alt: "Logo von Bank Statement Parser, einem leistungsstarken Python-Tool, das für die schnelle und genaue Verarbeitung von Finanzdaten und die Gewinnung von Erkenntnissen entwickelt wurde."
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Erste Schritte"
permalink: "https://bankstatementparser.com/de/erste-schritte/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Beginnen Sie mit der Erstellung sicherer Anwendungen mit Bank Statement Parser"
tags: "Bank, Aussage, Parser, Python, Camt, Pain001, CSV, OFX, QFX, MT940, Streaming, CLI"
theme_color: "rgb(73, 214, 251)"
title: "Kontoauszugsparser: Installations- und Nutzungshandbuch"
url: "https://bankstatementparser.com/de/erste-schritte/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/de/erste-schritte/rss.xml"
category: "Finanzsoftware, Python-Bibliothek, Entwicklerhandbuch"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Beginnen Sie mit Bank Statement Parser für Python: Installieren, analysieren Sie CAMT/PAIN.001/CSV/OFX/QFX/MT940-Dateien und verwenden Sie Streaming- oder CLI-Workflows."
item_guid: "https://bankstatementparser.com/de/erste-schritte/rss.xml"
item_link: "https://bankstatementparser.com/de/erste-schritte/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Kontoauszugsparser: Installations- und Nutzungshandbuch"
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
apple-mobile-web-app-title: "Kontoauszugsparser: Installations- und Nutzungshandbuch"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Installieren und verwenden Sie den Bank Statement Parser, um CAMT-, PAIN.001-, CSV-, OFX/QFX- und MT940-Dateien in Python zu analysieren."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logo von Bank Statement Parser, einem leistungsstarken Python-Tool, das für die schnelle und genaue Verarbeitung von Finanzdaten und die Gewinnung von Erkenntnissen entwickelt wurde."
twitter_site: "@wwdseb"
twitter_title: "Kontoauszugsparser: Installations- und Nutzungshandbuch"
twitter_url: "https://bankstatementparser.com/de/erste-schritte/index.html"

# Humans.txt - The Humans.txt front matter (YAML).

author_website: "https://bankstatementparser.com"
author_twitter: "@wwdseb"
author_location: "London, UK"
thanks: "Danke fürs Lesen!"
site_last_updated: "2026-04-01"
site_standards: "HTML5, CSS3, RSS, Atom, JSON, XML, YAML, Markdown, TOML"
site_components: "Shokunin SSG, Shokunin CLI, Shokunin Templates, Shokunin Themes, Kaishi SSG, Kaishi CLI, Kaishi Templates, Kaishi Themes"
site_software: "Shokunin, Rust"

---

## Anforderungen

- Python 3.9 bis 3.14
- Terminalzugriff (macOS, Linux oder WSL)

## Installieren

```bash
pip install bankstatementparser
```

Für Polars DataFrame-Unterstützung:

```bash
pip install bankstatementparser[polars]
```

## Schnellstart

### Jedes Format automatisch erkennen und analysieren

```python
from bankstatementparser import create_parser, detect_statement_format

fmt = detect_statement_format("transactions.ofx")
parser = create_parser("transactions.ofx", fmt)
df = parser.parse()  # pandas DataFrame
print(df.head())
```

Das funktioniert mit`.xml`(CAMT/PAIN.001),`.csv`, `.ofx`, `.qfx`, `.mt940`, Und`.sta`Dateien.

### CAMT.053 analysieren

```python
from bankstatementparser import CamtParser

parser = CamtParser("statement.xml")
transactions = parser.parse()
```

### PAIN.001 analysieren

```python
from bankstatementparser import Pain001Parser

parser = Pain001Parser("payment.xml")
payments = parser.parse()
```

## Große Dateien streamen

Verwenden Sie bei Dateien mit Tausenden von Transaktionen Streaming, um den Speicher zu begrenzen:

```python
parser = CamtParser("large_statement.xml")
for transaction in parser.parse_streaming(redact_pii=True):
    process(transaction)  # Memory stays constant
```

## In-Memory-Analyse

Analysieren Sie Bytes ohne Festplatten-E/A – nützlich für SFTP- oder API-Workflows:

```python
xml_bytes = download_from_sftp()
parser = CamtParser.from_bytes(xml_bytes, source_name="daily.xml")
transactions = parser.parse()
```

## Parallele Dateiverarbeitung

Mehrere Dateien gleichzeitig analysieren:

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

## Deduplizierung

Erkennen Sie exakte Duplikate und vermutete Übereinstimmungen mit Konfidenzwerten:

```python
from bankstatementparser import CamtParser, Deduplicator

parser = CamtParser("statement.xml")
dedup = Deduplicator()
result = dedup.deduplicate(dedup.from_dataframe(parser.parse()))

print(f"Unique: {len(result.unique_transactions)}")
print(f"Exact duplicates: {len(result.exact_duplicates)}")
print(f"Suspected matches: {len(result.suspected_matches)}")
```

## Sichere ZIP-Verarbeitung

Verarbeiten Sie gezippte XML-Dateien mit integrierten Sicherheitsprüfungen (Bombenschutz, Ablehnung verschlüsselter Eingaben):

```python
from bankstatementparser import iter_secure_xml_entries, CamtParser

for entry in iter_secure_xml_entries("statements.zip"):
    parser = CamtParser.from_bytes(entry.xml_bytes, source_name=entry.source_name)
    print(f"{entry.source_name}: {len(parser.parse())} transactions")
```

## Exportieren

```python
parser = CamtParser("statement.xml")
parser.export_csv("output.csv")
parser.export_json("output.json")

# Polars (requires bankstatementparser[polars])
polars_df = parser.to_polars()
```

## CLI-Nutzung

```bash
# Parse and display
python -m bankstatementparser.cli --type camt --input statement.xml

# Export to CSV
python -m bankstatementparser.cli --type camt --input statement.xml --output transactions.csv

# Stream with PII visible
python -m bankstatementparser.cli --type camt --input statement.xml --streaming --show-pii
```

CLI-Optionen:

- `--type {camt,pain001}`-- Parser-Typ
-`--input <path>`-- Eingabedatei
-`--output <csv_path>`- Export in CSV
-`--streaming`- Große Dateien streamen
-`--show-pii`-- sensible Felder anzeigen (standardmäßig geschwärzt)
-`--max-size <MB>`- Dateigrößenbeschränkung

## Lokale Entwicklungseinrichtung

```bash
git clone https://github.com/sebastienrousseau/bankstatementparser.git
cd bankstatementparser
python3 -m venv .venv && source .venv/bin/activate
pip install poetry && poetry install --with dev
```

Führen Sie die Testsuite aus:

```bash
pytest
```

## API-Referenz

### Parser-Klassen

| Klasse | Format | Import |
|---|---|---|
| `CamtParser` | CAMT.053 (ISO 20022) | `from bankstatementparser import CamtParser` |
| `Pain001Parser` | PAIN.001 (ISO 20022) | `from bankstatementparser import Pain001Parser` |
| `CsvStatementParser` | CSV | `from bankstatementparser import CsvStatementParser` |
| `OfxParser` | OFX | `from bankstatementparser import OfxParser` |
| `QfxParser` | QFX | `from bankstatementparser import QfxParser` |
| `Mt940Parser` | MT940 | `from bankstatementparser import Mt940Parser` |

### Utility-Funktionen

| Funktion | Zweck |
|---|---|
| `detect_statement_format(path)` | Dateiformat automatisch erkennen |
| `create_parser(path, fmt)` | Erstellen Sie den entsprechenden Parser |
| `parse_files_parallel(paths)` | Mehrere Dateien gleichzeitig analysieren |
| `iter_secure_xml_entries(zip_path)` | ZIP-Einträge sicher iterieren |

### Datenklassen

| Klasse | Zweck |
|---|---|
| `Deduplicator` | Erkennen Sie doppelte Transaktionen |
| `DeduplicationResult` | Ergebnis mit eindeutigen, genauen und vermuteten Übereinstimmungen |
| `InputValidator` | Validieren Sie Dateipfade und -formate |
| `Transaction` | Normalisierter Transaktionsdatensatz |
| `FileResult` | Ergebnis der parallelen Analyse |
| `ZipXMLSource` | ZIP-Mitglieds-Wrapper |

### Ausnahmen

| Ausnahme | Wenn er erzogen wird |
|---|---|
| `ParserError` | Fehler beim Parsen |
| `ExportError` | Exportfehler (CSV/JSON/Excel) |
| `ValidationError` | Fehler bei der Eingabevalidierung |
| `ZipSecurityError` | Fehler bei der ZIP-Sicherheitsprüfung |
