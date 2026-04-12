---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Un bâtiment blanc avec des fenêtres noires"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/daniele-franchi-Vl6YuVBLEys.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Analyseur de relevés bancaires. Tous droits réservés."
date: "Apr 11, 2026"
description: "Démarrez avec Bank Statement Parser pour Python : installez, analysez les fichiers CAMT/PAIN.001/CSV/OFX/QFX/MT940 et utilisez des flux de travail en streaming ou CLI."
download: ""
format-detection: "telephone=no"
hreflang: "fr"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/fr/premiers-pas/index.html"
image_alt: "Logo de Bank Statement Parser, un puissant outil Python conçu pour le traitement rapide et précis des données financières et l'extraction d'informations."
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "analyseur de relevés bancaires, premiers pas, python, CAMT, PAIN.001, CSV, OFX, QFX, MT940, données financières"
language: "fr-FR"
layout: "start"
locale: "fr_FR"
logo_alt: "Logo de Bank Statement Parser, un puissant outil Python conçu pour le traitement rapide et précis des données financières et l'extraction d'informations."
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Commencer"
permalink: "https://bankstatementparser.com/fr/premiers-pas/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Commencez à créer des applications sécurisées avec l'analyseur de relevés bancaires"
tags: "banque, relevé, analyseur, python, camt, pain001, csv, ofx, qfx, mt940, streaming, cli"
theme_color: "rgb(73, 214, 251)"
title: "Analyseur de relevés bancaires : guide d'installation et d'utilisation"
url: "https://bankstatementparser.com/fr/premiers-pas/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/fr/premiers-pas/rss.xml"
category: "Logiciel financier, bibliothèque Python, guide du développeur"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Démarrez avec Bank Statement Parser pour Python : installez, analysez les fichiers CAMT/PAIN.001/CSV/OFX/QFX/MT940 et utilisez des flux de travail en streaming ou CLI."
item_guid: "https://bankstatementparser.com/fr/premiers-pas/rss.xml"
item_link: "https://bankstatementparser.com/fr/premiers-pas/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Analyseur de relevés bancaires : guide d'installation et d'utilisation"
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
apple-mobile-web-app-title: "Analyseur de relevés bancaires : guide d'installation et d'utilisation"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Installez et utilisez Bank Statement Parser pour analyser les fichiers CAMT, PAIN.001, CSV, OFX/QFX et MT940 en Python."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logo de Bank Statement Parser, un puissant outil Python conçu pour le traitement rapide et précis des données financières et l'extraction d'informations."
twitter_site: "@wwdseb"
twitter_title: "Analyseur de relevés bancaires : guide d'installation et d'utilisation"
twitter_url: "https://bankstatementparser.com/fr/premiers-pas/index.html"

# Humans.txt - The Humans.txt front matter (YAML).

author_website: "https://bankstatementparser.com"
author_twitter: "@wwdseb"
author_location: "London, UK"
thanks: "Merci d'avoir lu!"
site_last_updated: "2026-04-01"
site_standards: "HTML5, CSS3, RSS, Atom, JSON, XML, YAML, Markdown, TOML"
site_components: "Shokunin SSG, Shokunin CLI, Shokunin Templates, Shokunin Themes, Kaishi SSG, Kaishi CLI, Kaishi Templates, Kaishi Themes"
site_software: "Shokunin, Rust"

---

## Prérequis

- Python 3.10 à 3.14
- Accès au terminal (macOS, Linux ou WSL)

## Installation

```bash
# Installation de base (analyseurs déterministes uniquement)
pip install bankstatementparser
```

Extras optionnels pour des fonctionnalités supplémentaires :

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

## Démarrage rapide

### Détection automatique et analyse de tout format structuré

```python
from bankstatementparser import create_parser, detect_statement_format

fmt = detect_statement_format("transactions.ofx")
parser = create_parser("transactions.ofx", fmt)
df = parser.parse()  # pandas DataFrame
print(df.head())
```

Fonctionne avec les fichiers `.xml` (CAMT/PAIN.001), `.csv`, `.ofx`, `.qfx`, `.mt940` et `.sta`.

### Analyser un fichier CAMT.053

```python
from bankstatementparser import CamtParser

parser = CamtParser("statement.xml")
transactions = parser.parse()
```

### Analyser un fichier PAIN.001

```python
from bankstatementparser import Pain001Parser

parser = Pain001Parser("payment.xml")
payments = parser.parse()
```

### Analyser des relevés bancaires PDF (pipeline hybride)

Le pipeline hybride achemine les PDF de manière intelligente via trois voies d'extraction :

```python
from bankstatementparser.hybrid import smart_ingest

result = smart_ingest("statement.pdf")
print(result.source_method)         # "deterministic" | "llm" | "vision"
print(result.verification.status)   # VERIFIED | DISCREPANCY | FAILED
print(result.transactions)          # List of extracted transactions
```

Chaque extraction est vérifiée avec la **Règle d'or** : `opening + credits − debits == closing`.

## Streaming de fichiers volumineux

Pour les fichiers contenant des milliers de transactions, utilisez le streaming pour limiter la mémoire :

```python
parser = CamtParser("large_statement.xml")
for transaction in parser.parse_streaming(redact_pii=True):
    process(transaction)  # Memory stays constant
```

## Analyse en mémoire

Analysez depuis des octets sans E/S disque — utile pour les flux SFTP ou API :

```python
xml_bytes = download_from_sftp()
parser = CamtParser.from_bytes(xml_bytes, source_name="daily.xml")
transactions = parser.parse()
```

## Traitement parallèle de fichiers

Analysez plusieurs fichiers simultanément :

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

## Scan de répertoires en masse

Traitez des arborescences complètes avec déduplication automatique :

```python
from bankstatementparser.hybrid import scan_and_ingest

batch = scan_and_ingest("statements/2026/", pattern="**/*.pdf")
print(f"Processed: {len(batch.results)} files")
print(f"Unique transactions: {batch.unique_count}")
```

## Déduplication

Hash idempotent des transactions pour une ingestion incrémentale fiable :

```python
from bankstatementparser import CamtParser, Deduplicator

parser = CamtParser("statement.xml")
dedup = Deduplicator()
result = dedup.deduplicate(dedup.from_dataframe(parser.parse()))

print(f"Unique: {len(result.unique_transactions)}")
print(f"Exact duplicates: {len(result.exact_duplicates)}")
print(f"Suspected matches: {len(result.suspected_matches)}")
```

## Catégorisation des transactions (enrichissement)

Catégorisez automatiquement les transactions via une classification par LLM :

```python
from bankstatementparser.enrichment import Categorizer

categorizer = Categorizer()
enriched = categorizer.categorize_batch(transactions)
for txn in enriched:
    print(f"{txn.description}: {txn.category}")
```

## Export comptable (hledger / beancount)

Exportez les transactions au format journal de comptabilité en texte brut :

```python
from bankstatementparser.export import to_hledger, to_beancount

journal = to_hledger(transactions, account="Assets:Bank:Checking")
beancount_journal = to_beancount(transactions, account="Assets:Bank:Checking")
```

## Vérification du solde multi-devises

Vérifiez les soldes de manière indépendante par groupe de devises :

```python
from bankstatementparser.hybrid import verify_balance_multi_currency

results = verify_balance_multi_currency(transactions)
for currency, verification in results.items():
    print(f"{currency}: {verification.status}")
```

## API REST

Déployez comme microservice FastAPI :

```bash
# Start the API server
bankstatementparser-api --port 8000

# For container deployments
bankstatementparser-api --host 0.0.0.0 --port 9000
```

Endpoints :
- `POST /ingest` -- Analyser un fichier de relevé bancaire
- `GET /health` -- Vérification de l'état

## Traitement ZIP sécurisé

Traitez des fichiers XML compressés avec des contrôles de sécurité intégrés (protection contre les bombes, rejet des entrées chiffrées) :

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

# Excel
parser.camt_to_excel("output.xlsx")
```

## Utilisation en ligne de commande

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

Options CLI :

- `--type {camt,pain001,ingest,review}` -- type d'analyseur ou mode
- `--input <path>` -- fichier d'entrée
- `--output <path>` -- fichier d'export (CSV ou JSON)
- `--streaming` -- streaming des fichiers volumineux
- `--show-pii` -- afficher les champs sensibles (masqués par défaut)
- `--max-size <MB>` -- limite de taille de fichier

## Configuration de l'environnement de développement

```bash
git clone https://github.com/sebastienrousseau/bankstatementparser.git
cd bankstatementparser
python3 -m venv .venv && source .venv/bin/activate
pip install poetry && poetry install --with dev
make install-hooks   # pre-commit hook runs `make verify` before every commit
```

Exécutez la suite de tests :

```bash
pytest
```

## Référence API

### Classes d'analyseurs

| Classe | Format | Import |
|---|---|---|
| `CamtParser` | CAMT.053 (ISO 20022) | `from bankstatementparser import CamtParser` |
| `Pain001Parser` | PAIN.001 (ISO 20022) | `from bankstatementparser import Pain001Parser` |
| `CsvStatementParser` | CSV | `from bankstatementparser import CsvStatementParser` |
| `OfxParser` | OFX | `from bankstatementparser import OfxParser` |
| `QfxParser` | QFX | `from bankstatementparser import QfxParser` |
| `Mt940Parser` | MT940 | `from bankstatementparser import Mt940Parser` |
| `smart_ingest()` | PDF (pipeline hybride) | `from bankstatementparser.hybrid import smart_ingest` |

### Fonctions utilitaires

| Fonction | Objectif |
|---|---|
| `detect_statement_format(path)` | Détection automatique du format |
| `create_parser(path, fmt)` | Créer l'analyseur approprié |
| `parse_files_parallel(paths)` | Analyser plusieurs fichiers simultanément |
| `iter_secure_xml_entries(zip_path)` | Itérer sur les entrées ZIP de manière sécurisée |
| `smart_ingest(path)` | Extraction PDF hybride avec vérification |
| `scan_and_ingest(dir, pattern)` | Scan de répertoires en masse |
| `verify_balance_multi_currency(txns)` | Vérification du solde par devise |
| `to_hledger(txns, account)` | Export au format journal hledger |
| `to_beancount(txns, account)` | Export au format journal beancount |

### Classes de données

| Classe | Objectif |
|---|---|
| `Deduplicator` | Détecter les transactions en double |
| `DeduplicationResult` | Résultat avec correspondances uniques, exactes et suspectes |
| `InputValidator` | Valider les chemins et formats de fichiers |
| `Transaction` | Enregistrement de transaction normalisé |
| `FileResult` | Résultat de l'analyse parallèle |
| `ZipXMLSource` | Enveloppe de membre ZIP |
| `IngestResult` | Résultat du pipeline hybride avec vérification |
| `VerificationResult` | Résultat de la vérification du solde |
| `Categorizer` | Catégorisation des transactions par LLM |
| `AccountMapper` | Règles de mappage de comptes basées sur des regex |

### Exceptions

| Exception | Déclenchée quand |
|---|---|
| `ParserError` | Échec de l'analyse |
| `ExportError` | Échec de l'export (CSV/JSON/Excel) |
| `ValidationError` | Échec de la validation des entrées |
| `ZipSecurityError` | Échec des contrôles de sécurité ZIP |
