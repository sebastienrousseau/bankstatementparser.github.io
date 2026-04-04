---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Om Bank Statement Parser: Funktioner, format och prestanda"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Bank Statement Parser. Alla rättigheter reserverade."
date: "Apr 01, 2026"
description: "Bank Statement Parser är ett Python-bibliotek med öppen källkod för att analysera CAMT.053, PAIN.001, CSV, OFX, QFX och MT940 till pandas DataFrames. 100 % lokal, PII-redigering, 27K+ tx/s."
download: ""
format-detection: "telephone=no"
hreflang: "sv"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/sv/a-propos/index.html"
image_alt: "Logotyp för Bank Statement Parser, styrka din finansiella analys med sömlös dataextraktion"
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "bankutdragsparser python, CAMT.053-parser, PAIN.001-parser, ISO 20022 python-bibliotek, MT940-parser, OFX QFX-parser, öppen källkodsbankparser, lokal finansiell databehandling, PII-redaktionsbank, MT940 till CAMT-migrering"
language: "sv-SE"
layout: "about"
locale: "sv_SE"
logo_alt: "Logotyp för Bank Statement Parser, styrka din finansiella analys med sömlös dataextraktion"
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Om Bank Statement Parser"
permalink: "https://bankstatementparser.com/sv/a-propos/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Ett bibliotek. Sex format. Noll nätverkssamtal."
tags: "bank, kontoutdrag, parser, finans, python, camt, pain001, csv, ofx, qfx, mt940"
theme_color: "rgb(73, 214, 251)"
title: "Om Bank Statement Parser: Funktioner, format och prestanda"
url: "https://bankstatementparser.com/sv/a-propos/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/sv/a-propos/rss.xml"
category: "Finansprogram, Python-bibliotek, databehandling"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Bank Statement Parser är ett Python-bibliotek med öppen källkod för att analysera CAMT.053, PAIN.001, CSV, OFX, QFX och MT940 till pandas DataFrames. 100 % lokal, PII-redigering, 27K+ tx/s."
item_guid: "https://bankstatementparser.com/sv/a-propos/rss.xml"
item_link: "https://bankstatementparser.com/sv/a-propos/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Om Bank Statement Parser: Funktioner, format och prestanda"
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
apple-mobile-web-app-title: "Om Bank Statement Parser: Funktioner, format och prestanda"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Python-bibliotek med öppen källkod: analysera CAMT.053, PAIN.001, CSV, OFX, QFX, MT940 i DataFrames. 100 % lokal, PII-redigering, 27K+ tx/s."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logotyp för Bank Statement Parser, styrka din finansiella analys med sömlös dataextraktion"
twitter_site: "@wwdseb"
twitter_title: "Om kontoutdragsparser: 6 format, 27K+ tx/s, 100 % lokalt"
twitter_url: "https://bankstatementparser.com/sv/a-propos/index.html"

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

**TL;DR:** Bank Statement Parser är ett Python-bibliotek med öppen källkod som analyserar sex kontoutdragsformat (CAMT.053, PAIN.001, CSV, OFX, QFX, MT940) till pandas DataFrames. 100 % lokal bearbetning, PII-redigering som standard, 27K+ tx/s genomströmning.

Bank Statement Parser är ett Python-bibliotek med öppen källkod som analyserar kontoutdrag från sex format till strukturerade pandas DataFrames. All bearbetning sker lokalt -- noll nätverksanrop, deterministisk utdata och automatisk PII-redaktion.

## Vem är detta till för?

- **Treasury-team** som migrerar från MT940 till CAMT.053 som behöver en parser som hanterar både gamla och nya format under övergången.
- **Fintech-utvecklare** bygger avstämnings-, rapporterings- eller redovisningspipelines som vill ha ett enda beroende istället för att sammanfoga mt940 + ofxparse + anpassad CSV-logik.
- **Compliance-team** som behöver PII-redigering som standard och revisionsklar, deterministisk utdata som aldrig skickar data till externa tjänster.
- **Alla** som vägrar att skicka känslig ekonomisk data till en tredjeparts SaaS när ett lokalt verktyg med öppen källkod kan göra jobbet.

## Format som stöds

| Formatera | Standard | Filtyper | Parser klass |
|---|---|---|---|
| CAMT.053 | ISO 20022 bank-till-kund-uttalande | `.xml` | `CamtParser` |
| PAIN.001 | Initiering av tillgodoräknande enligt ISO 20022 | `.xml` | `Pain001Parser` |
| CSV | Generisk bankexport | `.csv` | `CsvStatementParser` |
| OFX | Öppna finansiell börs | `.ofx` | `OfxParser` |
| QFX | Quicken Financial Exchange | `.qfx` | `QfxParser` |
| MT940 | SWIFT standard | `.mt940`, `.sta` | `Mt940Parser` |

Alla format producerar normaliserade pandor DataFrames med konsekventa kolumnnamn, vilket gör nedströms bearbetning formatagnostisk.

## Nyckelfunktioner

- **Format automatisk identifiering**:`detect_statement_format()`identifierar formatet;`create_parser()`instansierar den högra parsern.
- **Streaming Parsing**: Behandla stora filer (50 MB+, 50K+ transaktioner) med begränsat minne med`parse_streaming()`.
- **Parallell bearbetning**: Analysera flera filer samtidigt med`parse_files_parallel()`med ProcessPoolExecutor.
- **Deduplicering**: Upptäck exakta dubbletter och misstänkta matchningar med förklarliga konfidenspoäng.
- **In-Memory Parsing**:`from_string()`och`from_bytes()`för SFTP- och API-arbetsflöden utan disk I/O.
- **Säker ZIP-bearbetning**:`iter_secure_xml_entries()`med gränser för kompressionsförhållande, gränser för inträdesstorlekar och krypterad inträdesavvisning.
- **Export**: CSV, JSON, Excel (`.xlsx`), och valfria Polars DataFrames.

## Säkerhet och integritet

- **PII-redaktion**: Namn, IBAN och adresser är maskerade som standard i CLI-utdata. Välj med`--show-pii`.
- **XXE-skydd**: XML-tolkning används`resolve_entities=False`, `no_network=True`, `load_dtd=False`.
- **ZIP Bomb Protection**: Kompressionsförhållandegränser (100:1 standard), inträdesstorlekstak (10 MB), krypterad ingångsavvisning.
- **Path Traversal Prevention**: Spärrlista för farliga mönster och symlinkupplösning.
- **Supply Chain Security**: SHA-256 hash-låsta beroenden, CycloneDX SBOM, bygg härkomstintyg.

## Prestanda

| Metrisk | Värde |
|---|---|
| CAMT.053 genomströmning | 27 000+ tx/s |
| PAIN.001 genomströmning | 52 000+ tx/s |
| Latens per transaktion (CAMT) | 37 mikrosekunder |
| Latens per transaktion (PAIN.001) | 19 mikrosekunder |
| Dags för första resultat | < 2 ms |
| Minnesskalning (1K-50K tx) | Konstant (streaming) |
| Testtäckning | 100 % filialtäckning |
| Tester | 467 över 29 testfiler |

## Börja bygga

[Kom igång med installation och exempel ❯][01]

[01]: /getting-started/index.html "Komma igång"
 "GitHub Repository"
