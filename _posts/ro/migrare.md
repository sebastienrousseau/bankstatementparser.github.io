---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Ghid de migrare ISO 20022"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Analizator extras de cont. Toate drepturile rezervate."
date: "Apr 01, 2026"
description: "Un ghid practic pentru cronologia migrației SWIFT ISO 20022 (2026-2028), tranziția MT940 la CAMT.053 și modul în care Analizatorul de extrase bancare ajută echipele de trezorerie să migreze."
download: ""
format-detection: "telephone=no"
hreflang: "ro"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/ro/migrare/index.html"
image_alt: "Sigla Analizor extras de cont bancar, împuterniciți-vă analiza financiară cu extragerea fără întreruperi a datelor"
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "Migrare ISO 20022, MT940 la CAMT.053, termen SWIFT 2027, retragere MT940 2028, python de migrare extras de cont, parser CAMT.053, cronologie ISO 20022"
language: "ro-RO"
layout: "about"
locale: "ro_RO"
logo_alt: "Sigla Analizor extras de cont bancar, împuterniciți-vă analiza financiară cu extragerea fără întreruperi a datelor"
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Ghid de migrare ISO 20022"
permalink: "https://bankstatementparser.com/ro/migrare/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Navigați pe SWIFT MT la ISO 20022 de tranziție"
tags: "iso20022,migrare,mt940,camt053,rapid,cronologie"
theme_color: "rgb(73, 214, 251)"
title: "Ghid de migrare ISO 20022: Tranziție MT940 la CAMT.053"
url: "https://bankstatementparser.com/ro/migrare/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/ro/migrare/rss.xml"
category: "Software pentru finanțe, Biblioteca Python, Procesarea datelor"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Un ghid practic pentru cronologia migrației SWIFT ISO 20022 (2026-2028), tranziția MT940 la CAMT.053 și modul în care Analizatorul de extrase bancare ajută echipele de trezorerie să migreze."
item_guid: "https://bankstatementparser.com/ro/migrare/rss.xml"
item_link: "https://bankstatementparser.com/ro/migrare/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Ghid de migrare ISO 20022: Tranziție MT940 la CAMT.053"
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
apple-mobile-web-app-title: "Ghid de migrare ISO 20022: Tranziție MT940 la CAMT.053"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Un ghid practic pentru cronologia migrației SWIFT ISO 20022 (2026-2028), tranziția MT940 la CAMT.053 și modul în care Analizatorul de extrase bancare ajută echipele de trezorerie să migreze."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Sigla Analizor extras de cont bancar, împuterniciți-vă analiza financiară cu extragerea fără întreruperi a datelor"
twitter_site: "@wwdseb"
twitter_title: "Ghid de migrare ISO 20022: Tranziție MT940 la CAMT.053"
twitter_url: "https://bankstatementparser.com/ro/migrare/index.html"

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

**TL;DR:** SWIFT va retrage MT940 până în noiembrie 2028. Analizor de extrase de cont se ocupă atât de MT940, cât și de CAMT.053 cu un singur API, astfel încât canalul dvs. de analiză funcționează în timpul tranziției și după.

## De ce este importantă această migrație

SWIFT retrage formatele vechi de mesaje MT în favoarea standardului ISO 20022 mai bogat. Pentru echipele de trezorerie și finanțe, aceasta înseamnă că conductele dvs. de procesare a extraselor bancare trebuie să evolueze de la MT940 la CAMT.053 înainte de termenele limită stricte.

## Cronologia migrației SWIFT

| Data | Piatra de hotar | Impact |
|---|---|---|
| **noiembrie 2025** | Coexistența MT la MX sa încheiat pentru plățile transfrontaliere | Mesajele PACS sunt acum doar ISO 20022 |
| **noiembrie 2026** | Adresele structurate/hibride obligatorii; Multi-instrucțiune MT101 respinsă; Managementul cazului Faza 1 | Formatele de adrese trebuie să respecte; unele mesaje MT vor fi respinse |
| **Sfârșitul anului 2026** | Începe înscrierea pentru primirea CAMT.052/.053/.054 | Instituțiile financiare pot începe să primească declarații ISO native |
| **noiembrie 2027** | Toate FI trebuie să primească CAMT.053 nativ | SWIFT oprește conversia formatului MT în ISO; sistemele dumneavoastră trebuie să analizeze direct CAMT |
| **noiembrie 2028** | MT940/MT942/MT950/MT900/MT910 retras complet | Formatele de declarații vechi nu mai sunt disponibile; CAMT.052/.053/.054 sunt singura opțiune |

## Ce se schimbă pentru codul dvs

### Înainte: Numai MT940

```python
from bankstatementparser import Mt940Parser

parser = Mt940Parser("statement.mt940")
df = parser.parse()
```

### După: Ambele formate cu Auto-Detection

```python
from bankstatementparser import create_parser, detect_statement_format

fmt = detect_statement_format("statement.xml")  # or .mt940
parser = create_parser("statement.xml", fmt)
df = parser.parse()  # Same DataFrame schema regardless of format
```

The`detect_statement_format()`funcția identifică dacă fișierul este MT940, CAMT.053, PAIN.001 sau orice alt format acceptat. The`create_parser()`funcția returnează analizatorul corect. Codul dvs. din aval funcționează identic, indiferent de formatul sursă.

## CAMT.053 vs MT940: diferențe cheie

| Caracteristică | MT940 | CAMT.053 |
|---|---|---|
| Bogăția de date | Câmpuri limitate | De 3-5 ori mai multe date per tranzacție |
| Set de caractere | Limitat (set de caractere SWIFT) | Unicode complet |
| Structura | Text plat cu etichete | XML cu spații de nume |
| Raportarea soldului | Doar deschidere/închidere | Mai multe tipuri de echilibru |
| Referințe | Câmp de referință unic | Mai multe tipuri de referință |
| Manevrarea valutei | De bază | Multi-valută completă cu rate de schimb |

## Cum ajută analizatorul extras de cont

- **Unified API**: analizați atât MT940, cât și CAMT.053 cu același lucru`parse()`metoda, producând scheme DataFrame identice.
- **Detecție automată**: nu este nevoie să cunoașteți formatul în avans.`detect_statement_format()`îl identifică automat.
- **Namspace-agnostic**: gestionează orice variantă CAMT.053 (001.02, 001.04 sau wrapper-uri specifice băncii) fără configurație.
- **Streaming**: procesați fișiere CAMT mari (50 MB+, 50K+ tranzacții) cu memorie limitată.
- **Testare de migrare**: rulați ambele analizoare unul lângă altul în același interval de date pentru a verifica coerența rezultatelor înainte de a comuta.

## Noțiuni de bază

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

[Citiți documentația completă](/getting-started/index.html)

[Comparați cu alternative ❯](/comparison/index.html) | [Vedeți cazurile de utilizare din lumea reală ❯](/use-cases/index.html)
