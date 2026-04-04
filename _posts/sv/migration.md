---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "ISO 20022 Migration Guide"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/corporate-finance.webp"
cdn: "https://cloudcdn.pro"
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Bank Statement Parser. Alla rättigheter reserverade."
date: "Apr 01, 2026"
description: "En praktisk guide till SWIFT ISO 20022-migreringstidslinjen (2026-2028), MT940 till CAMT.053-övergången och hur Bank Statement Parser hjälper treasury-team att migrera."
download: ""
format-detection: "telephone=no"
hreflang: "sv"
icon: "https://cloudcdn.pro/bankstatementparser/images/favicon.ico"
id: "https://bankstatementparser.com/sv/migration/index.html"
image_alt: "Logotyp för Bank Statement Parser, styrka din finansiella analys med sömlös dataextraktion"
image_height: "630"
image_width: "1200"
image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
keywords: "ISO 20022 migrering, MT940 till CAMT.053, SWIFT deadline 2027, MT940 retirement 2028, kontoutdrag migration python, CAMT.053 parser, ISO 20022 tidslinje"
language: "sv-SE"
layout: "about"
locale: "sv_SE"
logo_alt: "Logotyp för Bank Statement Parser, styrka din finansiella analys med sömlös dataextraktion"
logo_height: "44"
logo_width: "44"
logo: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "ISO 20022 Migration Guide"
permalink: "https://bankstatementparser.com/sv/migration/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Navigera SWIFT MT till ISO 20022 Transition"
tags: "iso20022,migrering,mt940,camt053,swift,tidslinje"
theme_color: "rgb(73, 214, 251)"
title: "ISO 20022 Migration Guide: MT940 till CAMT.053 Transition"
url: "https://bankstatementparser.com/sv/migration/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/sv/migration/rss.xml"
category: "Finansprogram, Python-bibliotek, databehandling"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "En praktisk guide till SWIFT ISO 20022-migreringstidslinjen (2026-2028), MT940 till CAMT.053-övergången och hur Bank Statement Parser hjälper treasury-team att migrera."
item_guid: "https://bankstatementparser.com/sv/migration/rss.xml"
item_link: "https://bankstatementparser.com/sv/migration/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "ISO 20022 Migration Guide: MT940 till CAMT.053 Transition"
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
apple-mobile-web-app-title: "ISO 20022 Migration Guide: MT940 till CAMT.053 Transition"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "En praktisk guide till SWIFT ISO 20022-migreringstidslinjen (2026-2028), MT940 till CAMT.053-övergången och hur Bank Statement Parser hjälper treasury-team att migrera."
twitter_image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logotyp för Bank Statement Parser, styrka din finansiella analys med sömlös dataextraktion"
twitter_site: "@wwdseb"
twitter_title: "ISO 20022 Migration Guide: MT940 till CAMT.053 Transition"
twitter_url: "https://bankstatementparser.com/sv/migration/index.html"

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

**TL;DR:** SWIFT kommer att avveckla MT940 i november 2028. Bank Statement Parser hanterar både MT940 och CAMT.053 med ett enda API, så din analyspipeline fungerar under och efter övergången.

## Varför denna migration är viktig

SWIFT drar tillbaka äldre MT-meddelandeformat till förmån för den rikare ISO 20022-standarden. För treasury- och finansteam innebär detta att dina bankutdragsbearbetningspipelines måste utvecklas från MT940 till CAMT.053 innan de hårda tidsfristerna.

## SWIFT migreringstidslinje

| Datum | Milstolpe | Inverkan |
|---|---|---|
| **November 2025** | Samexistensen mellan MT och MX upphörde för gränsöverskridande betalningar | PACS-meddelanden är nu endast ISO 20022 |
| **November 2026** | Strukturerade/hybridadresser obligatoriska; MT101 multi-instruktion avvisad; Ärendehantering Fas 1 | Adressformat måste följa; vissa MT-meddelanden kommer att avvisas |
| **Sent 2026** | Opt-in börjar för att ta emot CAMT.052/.053/.054 | Finansiella institutioner kan börja ta emot inhemska ISO-utlåtanden |
| **November 2027** | Alla FI:er måste ta emot CAMT.053 inbyggt | SWIFT slutar konvertera MT-format till ISO; dina system måste analysera CAMT direkt |
| **November 2028** | MT940/MT942/MT950/MT900/MT910 helt pensionerad | Äldre uttalandeformat är inte längre tillgängliga; CAMT.052/.053/.054 är det enda alternativet |

## Vad ändras för din kod

### Före: Endast MT940

```python
from bankstatementparser import Mt940Parser

parser = Mt940Parser("statement.mt940")
df = parser.parse()
```

### Efter: Båda formaten med automatisk upptäckt

```python
from bankstatementparser import create_parser, detect_statement_format

fmt = detect_statement_format("statement.xml")  # or .mt940
parser = create_parser("statement.xml", fmt)
df = parser.parse()  # Same DataFrame schema regardless of format
```

De`detect_statement_format()`funktionen identifierar om filen är MT940, CAMT.053, PAIN.001 eller något annat format som stöds. De`create_parser()`funktion returnerar rätt analysator. Din nedströmskod fungerar identiskt oavsett källformat.

## CAMT.053 vs MT940: Nyckelskillnader

| Särdrag | MT940 | CAMT.053 |
|---|---|---|
| Datarikedom | Begränsade fält | 3-5 gånger mer data per transaktion |
| Karaktärsuppsättning | Begränsad (SWIFT-teckenuppsättning) | Fullständig Unicode |
| Strukturera | Platt text med taggar | XML med namnrymder |
| Balansrapportering | Endast öppning/stängning | Flera balanstyper |
| Referenser | Enstaka referensfält | Flera referenstyper |
| Valutahantering | Grundläggande | Full multi-valuta med växelkurser |

## Hur kontoutdrag Parser hjälper

- **Unified API**: Analysera både MT940 och CAMT.053 med samma`parse()`metod, som producerar identiska DataFrame-scheman.
- **Automatisk upptäckt**: Inget behov av att veta formatet i förväg.`detect_statement_format()`identifierar det automatiskt.
- **Namespace-agnostic**: Hanterar alla CAMT.053-varianter (001.02, 001.04 eller bankspecifika wrappers) utan konfiguration.
- **Streaming**: Behandla stora CAMT-filer (50 MB+, 50K+ transaktioner) med begränsat minne.
- **Migrationstest**: Kör båda parsarna sida vid sida på samma datumintervall för att verifiera utdatakonsistensen innan du byter.

## Komma igång

```bash
pip install bankstatementparser
```

```python
from bankstatementparser import create_parser, detect_statement_format

# Works with MT940 today, CAMT.053 tomorrow
for file in bank_statement_files:
    fmt = detect_statement_format(file)
    parser = create_parser(file, fmt)
    df = parser.parse()
    process(df)  # Your code doesn't change
```

[Läs hela dokumentationen](/getting-started/index.html)

[Jämför med alternativ ❯](/comparison/index.html) | [Se användningsfall i verkliga världen ❯](/use-cases/index.html)
