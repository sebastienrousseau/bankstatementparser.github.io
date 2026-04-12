---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "ISO 20022 Migratiehandleiding"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Parser voor bankafschriften. Alle rechten voorbehouden."
date: "Apr 11, 2026"
description: "Een praktische gids voor de SWIFT ISO 20022-migratietijdlijn (2026-2028), de transitie van MT940 naar CAMT.053, en hoe Bank Statement Parser treasury-teams helpt migreren."
download: ""
format-detection: "telephone=no"
hreflang: "nl"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/nl/migration/index.html"
image_alt: "Logo van Bank Statement Parser, maak uw financiële analyse mogelijk met naadloze gegevensextractie"
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "ISO 20022-migratie, MT940 naar CAMT.053, SWIFT-deadline 2027, MT940-pensionering 2028, migratiepython voor bankafschriften, CAMT.053-parser, ISO 20022-tijdlijn"
language: "nl-NL"
layout: "about"
locale: "nl_NL"
logo_alt: "Logo van Bank Statement Parser, maak uw financiële analyse mogelijk met naadloze gegevensextractie"
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "ISO 20022 Migratiehandleiding"
permalink: "https://bankstatementparser.com/nl/migration/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Navigeer met de SWIFT MT naar ISO 20022 Transition"
tags: "iso20022,migratie,mt940,camt053,snel,tijdlijn"
theme_color: "rgb(73, 214, 251)"
title: "ISO 20022 Migratiegids: MT940 naar CAMT.053 Overgang"
url: "https://bankstatementparser.com/nl/migration/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/nl/migration/rss.xml"
category: "Financiële software, Python-bibliotheek, gegevensverwerking"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Een praktische gids voor de SWIFT ISO 20022-migratietijdlijn (2026-2028), de transitie van MT940 naar CAMT.053, en hoe Bank Statement Parser treasury-teams helpt migreren."
item_guid: "https://bankstatementparser.com/nl/migration/rss.xml"
item_link: "https://bankstatementparser.com/nl/migration/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "ISO 20022 Migratiegids: MT940 naar CAMT.053 Overgang"
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
apple-mobile-web-app-title: "ISO 20022 Migratiegids: MT940 naar CAMT.053 Overgang"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Een praktische gids voor de SWIFT ISO 20022-migratietijdlijn (2026-2028), de transitie van MT940 naar CAMT.053, en hoe Bank Statement Parser treasury-teams helpt migreren."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logo van Bank Statement Parser, maak uw financiële analyse mogelijk met naadloze gegevensextractie"
twitter_site: "@wwdseb"
twitter_title: "ISO 20022 Migratiegids: MT940 naar CAMT.053 Overgang"
twitter_url: "https://bankstatementparser.com/nl/migration/index.html"

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

**TL;DR:** SWIFT zal MT940 in november 2028 uitfaseren. Bank Statement Parser verwerkt zowel MT940 als CAMT.053 met één API, zodat uw parsing-pipeline tijdens de transitie en daarna blijft werken.

## Waarom deze migratie belangrijk is

SWIFT stopt met legacy MT-berichtformaten ten gunste van de rijkere ISO 20022-standaard. Voor treasury- en financiële teams betekent dit dat uw verwerkingspipelines voor bankafschriften vóór de harde deadlines moeten evolueren van MT940 naar CAMT.053.

## SWIFT-migratietijdlijn

| Datum | Mijlpaal | Impact |
|---|---|---|
| **November 2025** | MT-naar-MX coëxistentie beëindigd voor grensoverschrijdende betalingen | PACS-berichten zijn nu alleen ISO 20022 |
| **November 2026** | Gestructureerde/hybride adressen verplicht; MT101 multi-instructie afgewezen; Case Management Fase 1 | Adresformaten moeten voldoen; sommige MT-berichten worden afgewezen |
| **Eind 2026** | Opt-in begint voor ontvangst van CAMT.052/.053/.054 | Financiële instellingen kunnen native ISO-afschriften gaan ontvangen |
| **November 2027** | Alle FI's moeten CAMT.053 native ontvangen | SWIFT stopt met converteren van MT naar ISO-formaat; uw systemen moeten CAMT rechtstreeks parseren |
| **November 2028** | MT940/MT942/MT950/MT900/MT910 volledig uitgefaseerd | Legacy afschriftformaten zijn niet meer beschikbaar; CAMT.052/.053/.054 zijn de enige optie |

## Wat verandert er voor uw code

### Vroeger: alleen MT940

```python
from bankstatementparser import Mt940Parser

parser = Mt940Parser("statement.mt940")
df = parser.parse()
```

### Nu: beide formaten met automatische detectie

```python
from bankstatementparser import create_parser, detect_statement_format

fmt = detect_statement_format("statement.xml")  # or .mt940
parser = create_parser("statement.xml", fmt)
df = parser.parse()  # Same DataFrame schema regardless of format
```

De `detect_statement_format()`-functie herkent of het bestand MT940, CAMT.053, PAIN.001 of een ander ondersteund formaat is. De `create_parser()`-functie geeft de juiste parser terug. Uw verdere code werkt identiek, ongeacht het bronformaat.

## CAMT.053 vs MT940: belangrijkste verschillen

| Kenmerk | MT940 | CAMT.053 |
|---|---|---|
| Gegevensrijkdom | Beperkte velden | 3-5x meer data per transactie |
| Tekenset | Beperkt (SWIFT-tekenset) | Volledige Unicode |
| Structuur | Platte tekst met tags | XML met naamruimten |
| Saldorapportage | Alleen opening/sluiting | Meerdere saldotypes |
| Referenties | Eén referentieveld | Meerdere referentietypen |
| Valutaverwerking | Basis | Volledige multi-valuta met wisselkoersen |

## Hoe Bank Statement Parser helpt

- **Uniforme API**: Parseer MT940, CAMT.053 en PDF-afschriften met dezelfde workflow. De DataFrame-uitvoer is consistent.
- **Automatische detectie**: U hoeft het formaat niet vooraf te kennen. `detect_statement_format()` herkent het automatisch.
- **Hybride PDF-pipeline**: Banken die tijdens de transitie alleen PDF-afschriften bieden, worden verwerkt door `smart_ingest()` met automatische saldoverificatie.
- **Naamruimte-agnostisch**: Verwerkt elke CAMT.053-variant (001.02, 001.04 of bankspecifieke wrappers) zonder configuratie.
- **Multi-valutaverificatie**: `verify_balance_multi_currency()` voert de Golden Rule per valutagroep uit — essentieel voor multi-valuta CAMT-afschriften.
- **Streaming**: Verwerk grote CAMT-bestanden (50 MB+, 50K+ transacties) met begrensd geheugen.
- **Ledger-export**: Exporteer direct naar hledger- of beancount-journaalformaat voor treasury-boekhouding.
- **Migratietests**: Voer beide parsers naast elkaar uit op dezelfde periode om uitvoerconsistentie te verifiëren voordat u overschakelt.

## Aan de slag

```bash
pip install bankstatementparser
```

```python
from bankstatementparser import create_parser, detect_statement_format

# Works with MT940 today, CAMT.053 tomorrow, PDF anytime
for file in bank_statement_files:
    fmt = detect_statement_format(file)
    parser = create_parser(file, fmt)
    df = parser.parse()
    process(df)  # Your code doesn't change
```

Voor PDF-afschriften van banken die nog geen gestructureerde CAMT-exports bieden:

```python
from bankstatementparser.hybrid import smart_ingest

result = smart_ingest("statement.pdf")
assert result.verification.status == "VERIFIED"
```

[Lees de volledige documentatie](/getting-started/index.html)

[Vergelijk met alternatieven ❯](/comparison/index.html) | [Bekijk praktijkvoorbeelden ❯](/use-cases/index.html)
