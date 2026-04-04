---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Un edificio bianco con finestre nere"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/daniele-franchi-Vl6YuVBLEys.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Analizzatore di estratti conto bancari. Tutti i diritti riservati."
date: "Apr 01, 2026"
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

- Python dalla 3.9 alla 3.14
- Accesso al terminale (macOS, Linux o WSL)

## Installa

```bash
pip install bankstatementparser
```

Per il supporto Polars DataFrame:

```bash
pip install bankstatementparser[polars]
```

## Avvio rapido

### Rileva automaticamente e analizza qualsiasi formato

```python
from bankstatementparser import create_parser, detect_statement_format

fmt = detect_statement_format("transactions.ofx")
parser = create_parser("transactions.ofx", fmt)
df = parser.parse()  # pandas DataFrame
print(df.head())
```

Funziona con`.xml`(CAMT/PAIN.001),`.csv`, `.ofx`, `.qfx`, `.mt940`, E`.sta`file.

### Analizza CAMT.053

```python
from bankstatementparser import CamtParser

parser = CamtParser("statement.xml")
transactions = parser.parse()
```

### Analizza PAIN.001

```python
from bankstatementparser import Pain001Parser

parser = Pain001Parser("payment.xml")
payments = parser.parse()
```

## Streaming di file di grandi dimensioni

Per i file con migliaia di transazioni, utilizza lo streaming per mantenere limitata la memoria:

```python
parser = CamtParser("large_statement.xml")
for transaction in parser.parse_streaming(redact_pii=True):
    process(transaction)  # Memory stays constant
```

## Analisi in memoria

Analisi da byte senza I/O su disco: utile per flussi di lavoro SFTP o API:

```python
xml_bytes = download_from_sftp()
parser = CamtParser.from_bytes(xml_bytes, source_name="daily.xml")
transactions = parser.parse()
```

## Elaborazione file parallela

Analizza più file contemporaneamente:

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

## Deduplicazione

Rileva duplicati esatti e corrispondenze sospette con punteggi di confidenza:

```python
from bankstatementparser import CamtParser, Deduplicator

parser = CamtParser("statement.xml")
dedup = Deduplicator()
result = dedup.deduplicate(dedup.from_dataframe(parser.parse()))

print(f"Unique: {len(result.unique_transactions)}")
print(f"Exact duplicates: {len(result.exact_duplicates)}")
print(f"Suspected matches: {len(result.suspected_matches)}")
```

## Elaborazione ZIP sicura

Elabora file XML compressi con controlli di sicurezza integrati (protezione anti-bomb, rifiuto di voci crittografate):

```python
from bankstatementparser import iter_secure_xml_entries, CamtParser

for entry in iter_secure_xml_entries("statements.zip"):
    parser = CamtParser.from_bytes(entry.xml_bytes, source_name=entry.source_name)
    print(f"{entry.source_name}: {len(parser.parse())} transactions")
```

## Esporta

```python
parser = CamtParser("statement.xml")
parser.export_csv("output.csv")
parser.export_json("output.json")

# Polars (requires bankstatementparser[polars])
polars_df = parser.to_polars()
```

## Utilizzo della CLI

```bash
# Parse and display
python -m bankstatementparser.cli --type camt --input statement.xml

# Export to CSV
python -m bankstatementparser.cli --type camt --input statement.xml --output transactions.csv

# Stream with PII visible
python -m bankstatementparser.cli --type camt --input statement.xml --streaming --show-pii
```

Opzioni CLI:

- `--type {camt,pain001}`-- tipo di analizzatore
-`--input <path>`-file di input
-`--output <csv_path>`-- esporta in CSV
-`--streaming`- streaming di file di grandi dimensioni
-`--show-pii`-- mostra campi sensibili (oscurati per impostazione predefinita)
-`--max-size <MB>`-- limite di dimensione del file

## Impostazione dello sviluppo locale

```bash
git clone https://github.com/sebastienrousseau/bankstatementparser.git
cd bankstatementparser
python3 -m venv .venv && source .venv/bin/activate
pip install poetry && poetry install --with dev
```

Esegui la suite di test:

```bash
pytest
```

## Riferimento API

### Classi del parser

| Classe | Formato | Importare |
|---|---|---|
| `CamtParser` | CAMT.053 (ISO 20022) | `from bankstatementparser import CamtParser` |
| `Pain001Parser` | PAIN.001 (ISO 20022) | `from bankstatementparser import Pain001Parser` |
| `CsvStatementParser` | CSV | `from bankstatementparser import CsvStatementParser` |
| `OfxParser` | OFX | `from bankstatementparser import OfxParser` |
| `QfxParser` | QFX | `from bankstatementparser import QfxParser` |
| `Mt940Parser` | MT940 | `from bankstatementparser import Mt940Parser` |

### Funzioni di utilità

| Funzione | Scopo |
|---|---|
| `detect_statement_format(path)` | Rilevamento automatico del formato file |
| `create_parser(path, fmt)` | Creare il parser appropriato |
| `parse_files_parallel(paths)` | Analizza più file contemporaneamente |
| `iter_secure_xml_entries(zip_path)` | Itera le voci ZIP in modo sicuro |

### Classi di dati

| Classe | Scopo |
|---|---|
| `Deduplicator` | Rileva transazioni duplicate |
| `DeduplicationResult` | Risultato con corrispondenze univoche, esatte e sospette |
| `InputValidator` | Convalidare percorsi e formati di file |
| `Transaction` | Record di transazione normalizzato |
| `FileResult` | Risultato dell'analisi parallela |
| `ZipXMLSource` | Wrapper membro ZIP |

### Eccezioni

| Eccezione | Quando sollevato |
|---|---|
| `ParserError` | Analisi degli errori |
| `ExportError` | Errori di esportazione (CSV/JSON/Excel) |
| `ValidationError` | Errori di convalida dell'input |
| `ZipSecurityError` | Errori del controllo di sicurezza ZIP |
