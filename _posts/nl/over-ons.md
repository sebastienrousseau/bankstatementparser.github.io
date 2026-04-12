---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Over bankafschriftparser: functies, formaten en prestaties"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Parser voor bankafschriften. Alle rechten voorbehouden."
date: "Apr 11, 2026"
description: "Bank Statement Parser is een open-source Python-bibliotheek voor het parseren van CAMT.053, PAIN.001, CSV, OFX, QFX en MT940 in panda's DataFrames. 100% lokaal, PII-redactie, 27K+ tx/s."
download: ""
format-detection: "telephone=no"
hreflang: "nl"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/nl/over-ons/index.html"
image_alt: "Logo van Bank Statement Parser, maak uw financiële analyse mogelijk met naadloze gegevensextractie"
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "bankafschrift-parser python, CAMT.053-parser, PAIN.001-parser, ISO 20022 python-bibliotheek, MT940-parser, OFX QFX-parser, open source bankparser, lokale financiële gegevensverwerking, PII-redactiebankieren, MT940 naar CAMT-migratie"
language: "nl-NL"
layout: "about"
locale: "nl_NL"
logo_alt: "Logo van Bank Statement Parser, maak uw financiële analyse mogelijk met naadloze gegevensextractie"
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Over de bankafschriftparser"
permalink: "https://bankstatementparser.com/nl/over-ons/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Eén bibliotheek. Zeven formaten. Geen netwerkoproepen."
tags: "bank,verklaring,parser,financiën,python,camt,pain001,csv,ofx,qfx,mt940"
theme_color: "rgb(73, 214, 251)"
title: "Over bankafschriftparser: functies, formaten en prestaties"
url: "https://bankstatementparser.com/nl/over-ons/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/nl/over-ons/rss.xml"
category: "Financiële software, Python-bibliotheek, gegevensverwerking"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Bank Statement Parser is een open-source Python-bibliotheek voor het parseren van CAMT.053, PAIN.001, CSV, OFX, QFX en MT940 in panda's DataFrames. 100% lokaal, PII-redactie, 27K+ tx/s."
item_guid: "https://bankstatementparser.com/nl/over-ons/rss.xml"
item_link: "https://bankstatementparser.com/nl/over-ons/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Over bankafschriftparser: functies, formaten en prestaties"
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
apple-mobile-web-app-title: "Over bankafschriftparser: functies, formaten en prestaties"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Open-source Python-bibliotheek: parseer CAMT.053, PAIN.001, CSV, OFX, QFX, MT940 in DataFrames. 100% lokaal, PII-redactie, 27K+ tx/s."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logo van Bank Statement Parser, maak uw financiële analyse mogelijk met naadloze gegevensextractie"
twitter_site: "@wwdseb"
twitter_title: "Over bankafschriftparser: 6 formaten, 27K+ tx/s, 100% lokaal"
twitter_url: "https://bankstatementparser.com/nl/over-ons/index.html"

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

**TL;DR:** Bank Statement Parser is een open-source Python-bibliotheek die zeven bankafschriftformaten (CAMT.053, PAIN.001, CSV, OFX, QFX, MT940 en PDF) parseert in pandas DataFrames. Hybride PDF-pipeline met saldoverificatie, REST API, verrijking, ledger-export, 27K+ tx/s doorvoer.

Bank Statement Parser is een open-source Python-bibliotheek die bankafschriften uit zeven formaten parseert in gestructureerde pandas DataFrames. De deterministische kern verwerkt gestructureerde formaten lokaal zonder netwerkverkeer. De optionele hybride PDF-pipeline routeert via lokale LLM's (via Ollama) voor digitale en gescande afschriften.

## Voor wie is dit bedoeld?

- **Treasury-teams** die migreren van MT940 naar CAMT.053 en een parser nodig hebben die beide formaten verwerkt tijdens de transitie, plus PDF-afschriften van banken zonder gestructureerde exports.
- **Fintech-ontwikkelaars** die pipelines bouwen voor afstemming, rapportage of boekhouding en één afhankelijkheid willen met ingebouwde saldoverificatie, categorisatie en ledger-export.
- **Complianceteams** die standaard PII-redactie nodig hebben, deterministische uitvoer en Golden Rule-verificatie die afwijkingen signaleert voordat ze het grootboek bereiken.
- **Plaintext-accounting gebruikers** die geautomatiseerde opname willen van PDF-bankafschriften rechtstreeks naar hledger- of beancount-journalen.
- **Iedereen** die weigert gevoelige financiële gegevens naar een SaaS van derden te sturen wanneer een lokale, open-source tool het werk kan doen.

## Ondersteunde formaten

| Formaat | Standaard | Bestandstypen | Parser/Methode |
|---|---|---|---|
| CAMT.053 | ISO 20022 Bank-naar-klantafschrift | `.xml` | `CamtParser` |
| PAIN.001 | ISO 20022 Credit Transfer Initiation | `.xml` | `Pain001Parser` |
| CSV | Generieke bankexporten | `.csv` | `CsvStatementParser` |
| OFX | Open Financial Exchange | `.ofx` | `OfxParser` |
| QFX | Quicken Financial Exchange | `.qfx` | `QfxParser` |
| MT940 | SWIFT-standaard | `.mt940`, `.sta` | `Mt940Parser` |
| PDF | Digitale en gescande afschriften | `.pdf` | `smart_ingest()` |

Alle formaten produceren genormaliseerde pandas DataFrames met consistente kolomnamen. Dat maakt verdere verwerking formaatobafhankelijk.

## Belangrijkste mogelijkheden

- **Hybride PDF-pipeline**: `smart_ingest()` routeert PDF's via drie paden — deterministische tabelextractie, tekst-LLM of vision-LLM — met automatische Golden Rule-saldoverificatie.
- **Automatische formaatdetectie**: `detect_statement_format()` herkent het formaat; `create_parser()` maakt de juiste parser aan.
- **Saldoverificatie**: Golden Rule-controle (`opening + credits − debits == closing`) met status VERIFIED/DISCREPANCY/FAILED.
- **Multi-valutaverificatie**: `verify_balance_multi_currency()` groepeert transacties per valuta voor onafhankelijke verificatie.
- **REST API**: FastAPI-microservice met `/ingest`- en `/health`-endpoints voor productieomgevingen.
- **Verrijking**: LLM-gestuurde transactiecategorisatie met pluggable schema's (Plaid 13-categorie standaard).
- **Interactieve beoordeling**: Loop afwijkingen door met accepteren/bewerken/overslaan/verwijderen via `--type review`.
- **Ledger-export**: `to_hledger()` en `to_beancount()` voor plaintext-accounting workflows.
- **Bulk scanning**: `scan_and_ingest()` verwerkt mappenbomen met automatische cross-file ontdubbeling.
- **Rekeningkoppeling**: Regex-gebaseerde rekeningkoppelingsregels vanuit JSON-configuratie voor ledger-export.
- **Streaming parsing**: Verwerk grote bestanden (50 MB+, 50K+ transacties) met begrensd geheugen via `parse_streaming()`.
- **Parallelle verwerking**: Parseer meerdere bestanden gelijktijdig met `parse_files_parallel()` via ProcessPoolExecutor.
- **Ontdubbeling**: Idempotente `transaction_hash` (MD5-vingerafdruk) voor veilige incrementele opname.
- **In-memory parsing**: `from_string()` en `from_bytes()` voor SFTP- en API-workflows zonder schijf-I/O.
- **Veilige ZIP-verwerking**: `iter_secure_xml_entries()` met compressieverhoudingslimieten, maximale invoergrootte en afwijzing van versleutelde bestanden.
- **Export**: CSV, JSON, Excel (`.xlsx`), Polars DataFrames, hledger en beancount-journalen.

## Beveiliging en privacy

- **PII-redactie**: Namen, IBAN's en adressen worden standaard gemaskeerd in CLI-uitvoer. Schakel in met `--show-pii`.
- **XXE-bescherming**: XML-parsing gebruikt `resolve_entities=False`, `no_network=True`, `load_dtd=False`.
- **ZIP-bombeveiliging**: Compressieverhoudingslimieten (standaard 100:1), maximale invoergrootte (10 MB), afwijzing van versleutelde bestanden.
- **Pad-traversalpreventie**: Blokkeerlijst met gevaarlijke patronen en symlink-resolutie.
- **Supply-chainbeveiliging**: SHA-256 hash-locked afhankelijkheden, CycloneDX SBOM, build-herkomstattest.
- **Alleen lokale LLM's**: De hybride PDF-pipeline gebruikt Ollama voor lokale inferentie — geen gegevens naar cloud-API's.

## Prestaties

| Metriek | Waarde |
|---|---|
| CAMT.053-doorvoer | 27.000+ tx/s |
| PAIN.001-doorvoer | 52.000+ tx/s |
| Latentie per transactie (CAMT) | 37 microseconden |
| Latentie per transactie (PAIN.001) | 19 microseconden |
| Tijd tot eerste resultaat | < 2 ms |
| Geheugenschaling (1K–50K tx) | Constant (streaming) |
| Testdekking | 100% branchdekking |
| Tests | 718 verdeeld over 29 testbestanden |

## Begin met bouwen

[Aan de slag met installatie en voorbeelden ❯][01]

[01]: /getting-started/index.html "Aan de slag"
