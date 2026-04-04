---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Un bâtiment blanc avec des fenêtres noires"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/daniele-franchi-Vl6YuVBLEys.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Analyseur de relevés bancaires. Tous droits réservés."
date: "Apr 01, 2026"
description: "Démarrez avec Bank Statement Parser pour Python : installez, analysez les fichiers CAMT/PAIN.001/CSV/OFX/QFX/MT940 et utilisez des flux de travail en streaming ou CLI."
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
title: "Analyseur de relevés bancaires : guide d'installation et d'utilisation"
url: "https://bankstatementparser.com/fr/premiers-pas/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/fr/premiers-pas/rss.xml"
category: "Logiciel financier, bibliothèque Python, guide du développeur"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Démarrez avec Bank Statement Parser pour Python : installez, analysez les fichiers CAMT/PAIN.001/CSV/OFX/QFX/MT940 et utilisez des flux de travail en streaming ou CLI."
item_guid: "https://bankstatementparser.com/fr/premiers-pas/rss.xml"
item_link: "https://bankstatementparser.com/fr/premiers-pas/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Analyseur de relevés bancaires : guide d'installation et d'utilisation"
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
apple-mobile-web-app-title: "Analyseur de relevés bancaires : guide d'installation et d'utilisation"
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
twitter_title: "Analyseur de relevés bancaires : guide d'installation et d'utilisation"
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

## Exigences

-Python 3.9 à 3.14
- Accès au terminal (macOS, Linux ou WSL)

## Installer

```bash
pip install bankstatementparser
```

Pour la prise en charge de Polars DataFrame :

```bash
pip install bankstatementparser[polars]
```

## Démarrage rapide

### Détecter et analyser automatiquement n'importe quel format

```python
from bankstatementparser import create_parser, detect_statement_format

fmt = detect_statement_format("transactions.ofx")
parser = create_parser("transactions.ofx", fmt)
df = parser.parse()  # pandas DataFrame
print(df.head())
```

Cela fonctionne avec`.xml`(CAMT/DOULEUR.001),`.csv`, `.ofx`, `.qfx`, `.mt940`, et`.sta`fichiers.

### Analyser CAMT.053

```python
from bankstatementparser import CamtParser

parser = CamtParser("statement.xml")
transactions = parser.parse()
```

### Analyser PAIN.001

```python
from bankstatementparser import Pain001Parser

parser = Pain001Parser("payment.xml")
payments = parser.parse()
```

## Streaming de fichiers volumineux

Pour les fichiers contenant des milliers de transactions, utilisez le streaming pour limiter la mémoire :

```python
parser = CamtParser("large_statement.xml")
for transaction in parser.parse_streaming(redact_pii=True):
    process(transaction)  # Memory stays constant
```

## Analyse en mémoire

Analyser à partir d'octets sans E/S disque – utile pour les workflows SFTP ou API :

```python
xml_bytes = download_from_sftp()
parser = CamtParser.from_bytes(xml_bytes, source_name="daily.xml")
transactions = parser.parse()
```

## Traitement de fichiers parallèles

Analyser plusieurs fichiers simultanément :

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

## Déduplication

Détectez les doublons exacts et les correspondances suspectées grâce aux scores de confiance :

```python
from bankstatementparser import CamtParser, Deduplicator

parser = CamtParser("statement.xml")
dedup = Deduplicator()
result = dedup.deduplicate(dedup.from_dataframe(parser.parse()))

print(f"Unique: {len(result.unique_transactions)}")
print(f"Exact duplicates: {len(result.exact_duplicates)}")
print(f"Suspected matches: {len(result.suspected_matches)}")
```

## Traitement ZIP sécurisé

Traitez les fichiers XML compressés avec des contrôles de sécurité intégrés (protection contre les bombes, rejet d'entrée crypté) :

```python
from bankstatementparser import iter_secure_xml_entries, CamtParser

for entry in iter_secure_xml_entries("statements.zip"):
    parser = CamtParser.from_bytes(entry.xml_bytes, source_name=entry.source_name)
    print(f"{entry.source_name}: {len(parser.parse())} transactions")
```

## Exporter

```python
parser = CamtParser("statement.xml")
parser.export_csv("output.csv")
parser.export_json("output.json")

# Polars (requires bankstatementparser[polars])
polars_df = parser.to_polars()
```

## Utilisation de la CLI

```bash
# Parse and display
python -m bankstatementparser.cli --type camt --input statement.xml

# Export to CSV
python -m bankstatementparser.cli --type camt --input statement.xml --output transactions.csv

# Stream with PII visible
python -m bankstatementparser.cli --type camt --input statement.xml --streaming --show-pii
```

Options CLI :

- `--type {camt,pain001}`-- type d'analyseur
-`--input <path>`-- fichier d'entrée
-`--output <csv_path>`-- exporter au format CSV
-`--streaming`- diffuser des fichiers volumineux
-`--show-pii`-- afficher les champs sensibles (expurgés par défaut)
-`--max-size <MB>`-- limite de taille de fichier

## Configuration du développement local

```bash
git clone https://github.com/sebastienrousseau/bankstatementparser.git
cd bankstatementparser
python3 -m venv .venv && source .venv/bin/activate
pip install poetry && poetry install --with dev
```

Exécutez la suite de tests :

```bash
pytest
```

## Référence API

### Classes d'analyseur

| Classe | Format | Importer |
|---|---|---|
| `CamtParser` | CAMT.053 (ISO 20022) | `from bankstatementparser import CamtParser` |
| `Pain001Parser` | DOULEUR.001 (ISO 20022) | `from bankstatementparser import Pain001Parser` |
| `CsvStatementParser` | CSV | `from bankstatementparser import CsvStatementParser` |
| `OfxParser` | OFX | `from bankstatementparser import OfxParser` |
| `QfxParser` | QFX | `from bankstatementparser import QfxParser` |
| `Mt940Parser` | MT940 | `from bankstatementparser import Mt940Parser` |

### Fonctions utilitaires

| Fonction | But |
|---|---|
| `detect_statement_format(path)` | Détection automatique du format de fichier |
| `create_parser(path, fmt)` | Créer l'analyseur approprié |
| `parse_files_parallel(paths)` | Analyser plusieurs fichiers simultanément |
| `iter_secure_xml_entries(zip_path)` | Itérer les entrées ZIP en toute sécurité |

### Classes de données

| Classe | But |
|---|---|
| `Deduplicator` | Détecter les transactions en double |
| `DeduplicationResult` | Résultat avec des correspondances uniques, exactes et suspectées |
| `InputValidator` | Valider les chemins et formats de fichiers |
| `Transaction` | Enregistrement de transaction normalisé |
| `FileResult` | Résultat de l'analyse parallèle |
| `ZipXMLSource` | Wrapper de membre ZIP |

###Exceptions

| Exception | Une fois élevé |
|---|---|
| `ParserError` | Échecs d'analyse |
| `ExportError` | Échecs d'exportation (CSV/JSON/Excel) |
| `ValidationError` | Échecs de validation des entrées |
| `ZipSecurityError` | Échecs du contrôle de sécurité ZIP |
