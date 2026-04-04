---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Bílá budova s ​​černými okny"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/daniele-franchi-Vl6YuVBLEys.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023–2026 Analyzátor bankovních výpisů. Všechna práva vyhrazena."
date: "Apr 01, 2026"
description: "Začněte s Bank Statement Parser pro Python: nainstalujte, analyzujte soubory CAMT/PAIN.001/CSV/OFX/QFX/MT940 a použijte streaming nebo pracovní postupy CLI."
download: ""
format-detection: "telephone=no"
hreflang: "cs"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/cs/premiers-pas/index.html"
image_alt: "Logo nástroje Bank Statement Parser, výkonného nástroje Pythonu určeného pro rychlé a přesné zpracování finančních dat a extrakci přehledů."
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "analyzátor bankovních výpisů, začínáme, python, CAMT, PAIN.001, CSV, OFX, QFX, MT940, finanční údaje"
language: "cs-CZ"
layout: "start"
locale: "cs_CZ"
logo_alt: "Logo nástroje Bank Statement Parser, výkonného nástroje Pythonu určeného pro rychlé a přesné zpracování finančních dat a extrakci přehledů."
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Začínáme"
permalink: "https://bankstatementparser.com/cs/premiers-pas/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Začněte vytvářet zabezpečené aplikace pomocí analyzátoru bankovních výpisů"
tags: "banka,výpis,analyzátor,python,camt,pain001,csv,ofx,qfx,mt940,streaming,cli"
theme_color: "rgb(73, 214, 251)"
title: "Analyzátor výpisů z účtu: Průvodce instalací a používáním"
url: "https://bankstatementparser.com/cs/premiers-pas/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/cs/premiers-pas/rss.xml"
category: "Finance Software, Python Library, Developer Guide"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Začněte s Bank Statement Parser pro Python: nainstalujte, analyzujte soubory CAMT/PAIN.001/CSV/OFX/QFX/MT940 a použijte streaming nebo pracovní postupy CLI."
item_guid: "https://bankstatementparser.com/cs/premiers-pas/rss.xml"
item_link: "https://bankstatementparser.com/cs/premiers-pas/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Analyzátor výpisů z účtu: Průvodce instalací a používáním"
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
apple-mobile-web-app-title: "Analyzátor výpisů z účtu: Průvodce instalací a používáním"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Nainstalujte a použijte Bank Statement Parser k analýze souborů CAMT, PAIN.001, CSV, OFX/QFX a MT940 v Pythonu."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logo nástroje Bank Statement Parser, výkonného nástroje Pythonu určeného pro rychlé a přesné zpracování finančních dat a extrakci přehledů."
twitter_site: "@wwdseb"
twitter_title: "Analyzátor výpisů z účtu: Průvodce instalací a používáním"
twitter_url: "https://bankstatementparser.com/cs/premiers-pas/index.html"

# Humans.txt - The Humans.txt front matter (YAML).

author_website: "https://bankstatementparser.com"
author_twitter: "@wwdseb"
author_location: "London, UK"
thanks: "Díky za přečtení!"
site_last_updated: "2026-04-01"
site_standards: "HTML5, CSS3, RSS, Atom, JSON, XML, YAML, Markdown, TOML"
site_components: "Shokunin SSG, Shokunin CLI, Shokunin Templates, Shokunin Themes, Kaishi SSG, Kaishi CLI, Kaishi Templates, Kaishi Themes"
site_software: "Shokunin, Rust"

---

## Požadavky

- Python 3.9 až 3.14
- Terminálový přístup (macOS, Linux nebo WSL)

## Nainstalujte

```bash
pip install bankstatementparser
```

Pro podporu Polar DataFrame:

```bash
pip install bankstatementparser[polars]
```

## Rychlý start

### Automaticky detekovat a analyzovat jakýkoli formát

```python
from bankstatementparser import create_parser, detect_statement_format

fmt = detect_statement_format("transactions.ofx")
parser = create_parser("transactions.ofx", fmt)
df = parser.parse()  # pandas DataFrame
print(df.head())
```

Toto funguje s`.xml`(CAMT/PAIN.001),`.csv`, `.ofx`, `.qfx`, `.mt940`a`.sta`soubory.

### Analyzujte CAMT.053

```python
from bankstatementparser import CamtParser

parser = CamtParser("statement.xml")
transactions = parser.parse()
```

### Rozebrat PAIN.001

```python
from bankstatementparser import Pain001Parser

parser = Pain001Parser("payment.xml")
payments = parser.parse()
```

## Streamování velkých souborů

U souborů s tisíci transakcemi použijte streamování, abyste udrželi paměť omezenou:

```python
parser = CamtParser("large_statement.xml")
for transaction in parser.parse_streaming(redact_pii=True):
    process(transaction)  # Memory stays constant
```

## Analýza v paměti

Analýza z bajtů bez diskových I/O – užitečné pro pracovní postupy SFTP nebo API:

```python
xml_bytes = download_from_sftp()
parser = CamtParser.from_bytes(xml_bytes, source_name="daily.xml")
transactions = parser.parse()
```

## Paralelní zpracování souborů

Analyzovat více souborů současně:

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

## Deduplikace

Zjistěte přesné duplikáty a podezřelé shody pomocí skóre spolehlivosti:

```python
from bankstatementparser import CamtParser, Deduplicator

parser = CamtParser("statement.xml")
dedup = Deduplicator()
result = dedup.deduplicate(dedup.from_dataframe(parser.parse()))

print(f"Unique: {len(result.unique_transactions)}")
print(f"Exact duplicates: {len(result.exact_duplicates)}")
print(f"Suspected matches: {len(result.suspected_matches)}")
```

## Bezpečné zpracování ZIP

Zpracujte zazipované soubory XML s vestavěnými bezpečnostními kontrolami (ochrana proti bombám, odmítnutí šifrovaných záznamů):

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

## Použití CLI

```bash
# Parse and display
python -m bankstatementparser.cli --type camt --input statement.xml

# Export to CSV
python -m bankstatementparser.cli --type camt --input statement.xml --output transactions.csv

# Stream with PII visible
python -m bankstatementparser.cli --type camt --input statement.xml --streaming --show-pii
```

Možnosti CLI:

- `--type {camt,pain001}`-- typ analyzátoru
-`--input <path>`-- vstupní soubor
-`--output <csv_path>`-- export do CSV
-`--streaming`-- streamování velkých souborů
-`--show-pii`-- zobrazit citlivá pole (ve výchozím nastavení upraveno)
-`--max-size <MB>`-- limit velikosti souboru

## Nastavení místního rozvoje

```bash
git clone https://github.com/sebastienrousseau/bankstatementparser.git
cd bankstatementparser
python3 -m venv .venv && source .venv/bin/activate
pip install poetry && poetry install --with dev
```

Spusťte testovací sadu:

```bash
pytest
```

## Reference API

### Třídy analyzátoru

| Třída | Formát | Importovat |
|---|---|---|
| `CamtParser` | CAMT.053 (ISO 20022) | `from bankstatementparser import CamtParser` |
| `Pain001Parser` | PAIN.001 (ISO 20022) | `from bankstatementparser import Pain001Parser` |
| `CsvStatementParser` | CSV | `from bankstatementparser import CsvStatementParser` |
| `OfxParser` | OFX | `from bankstatementparser import OfxParser` |
| `QfxParser` | QFX | `from bankstatementparser import QfxParser` |
| `Mt940Parser` | MT940 | `from bankstatementparser import Mt940Parser` |

### Užitkové funkce

| Funkce | Účel |
|---|---|
| `detect_statement_format(path)` | Automaticky detekovat formát souboru |
| `create_parser(path, fmt)` | Vytvořte příslušný analyzátor |
| `parse_files_parallel(paths)` | Analyzujte více souborů současně |
| `iter_secure_xml_entries(zip_path)` | Iterujte položky ZIP bezpečně |

### Datové třídy

| Třída | Účel |
|---|---|
| `Deduplicator` | Detekce duplicitních transakcí |
| `DeduplicationResult` | Výsledkem jsou jedinečné, přesné a podezřelé shody |
| `InputValidator` | Ověřte cesty a formáty souborů |
| `Transaction` | Normalizovaný záznam transakce |
| `FileResult` | Výsledek paralelní analýzy |
| `ZipXMLSource` | Obal člena ZIP |

### Výjimky

| Výjimka | Když Raised |
|---|---|
| `ParserError` | Selhání analýzy |
| `ExportError` | Selhání exportu (CSV/JSON/Excel) |
| `ValidationError` | Selhání ověření vstupu |
| `ZipSecurityError` | Selhání bezpečnostní kontroly ZIP |
