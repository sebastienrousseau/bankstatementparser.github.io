---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Over bankafschriftparser: functies, formaten en prestaties"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Parser voor bankafschriften. Alle rechten voorbehouden."
date: "Apr 01, 2026"
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
subtitle: "Eén bibliotheek. Zes formaten. Geen netwerkoproepen."
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

**TL;DR:** Bankafschriftparser is een open-source Python-bibliotheek die zes bankafschriftformaten (CAMT.053, PAIN.001, CSV, OFX, QFX, MT940) parseert in panda's DataFrames. 100% lokale verwerking, standaard PII-redactie, 27K+ tx/s-doorvoer.

Bank Statement Parser is een open-source Python-bibliotheek die bankafschriften uit zes formaten parseert in gestructureerde panda's DataFrames. Alle verwerking vindt lokaal plaats: geen netwerkoproepen, deterministische uitvoer en automatische PII-redactie.

## Voor wie is dit bedoeld?

- **Treasury-teams** die migreren van MT940 naar CAMT.053 en die een parser nodig hebben die zowel oude als nieuwe formaten verwerkt tijdens de transitie.
- **Fintech-ontwikkelaars** die pijplijnen voor afstemming, rapportage of boekhouding bouwen die één enkele afhankelijkheid willen in plaats van mt940 + ofxparse + aangepaste CSV-logica aan elkaar te naaien.
- **Complianceteams** die standaard PII-redactie nodig hebben en audit-ready, deterministische output die nooit gegevens naar externe services verzendt.
- **Iedereen** die weigert gevoelige financiële gegevens naar een SaaS van derden te sturen terwijl een lokale, open source-tool het werk kan doen.

## Ondersteunde formaten

| Formaat | Standaard | Bestandstypen | Parser-klasse |
|---|---|---|---|
| CAMT.053 | ISO 20022 Bank-naar-klantverklaring | `.xml` | `CamtParser` |
| PIJN.001 | ISO 20022 Initiatie van kredietoverdracht | `.xml` | `Pain001Parser` |
| CSV | Generieke bankexporten | `.csv` | `CsvStatementParser` |
| OFX | Open financiële uitwisseling | `.ofx` | `OfxParser` |
| QFX | Quicken financiële uitwisseling | `.qfx` | `QfxParser` |
| MT940 | SWIFT-standaard | `.mt940`, `.sta` | `Mt940Parser` |

Alle formaten produceren genormaliseerde panda's DataFrames met consistente kolomnamen, waardoor downstream-verwerkingsformaten agnostisch worden.

## Belangrijkste mogelijkheden

- **Formaat automatische detectie**:`detect_statement_format()`identificeert het formaat;`create_parser()`Instantiseert de juiste parser.
- **Streaming Parsing**: Verwerk grote bestanden (50 MB+, 50K+ transacties) met begrensd geheugen met behulp van`parse_streaming()`.
- **Parallelle verwerking**: parseer meerdere bestanden gelijktijdig met`parse_files_parallel()`met behulp van ProcessPoolExecutor.
- **Ontdubbeling**: detecteer exacte duplicaten en vermoedelijke overeenkomsten met verklaarbare betrouwbaarheidsscores.
- **In-memory parseren**:`from_string()`En`from_bytes()`voor SFTP- en API-workflows zonder schijf-I/O.
- **Veilige ZIP-verwerking**:`iter_secure_xml_entries()`met compressieverhoudingslimieten, limieten voor invoergroottes en gecodeerde invoerafwijzing.
- **Exporteren**: CSV, JSON, Excel (`.xlsx`) en optionele Polars DataFrames.

## Beveiliging en privacy

- **PII-redactie**: namen, IBAN's en adressen worden standaard gemaskeerd in CLI-uitvoer. Meld u aan met`--show-pii`.
- **XXE-beveiliging**: gebruik van XML-parsing`resolve_entities=False`, `no_network=True`, `load_dtd=False`.
- **ZIP Bomb Protection**: Compressieverhoudingslimieten (standaard 100:1), maximale invoergrootte (10 MB), versleutelde invoerafwijzing.
- **Path Traversal Prevention**: blokkeerlijst met gevaarlijke patronen en resolutie van symlinks.
- **Supply Chain-beveiliging**: SHA-256 hash-locked afhankelijkheden, CycloneDX SBOM, attest van herkomst van build.

## Prestatie

| Metrisch | Waarde |
|---|---|
| CAMT.053-doorvoer | 27.000+ tx/s |
| PAIN.001-doorvoer | 52.000+ tx/s |
| Latentie per transactie (CAMT) | 37 microseconden |
| Latentie per transactie (PAIN.001) | 19 microseconden |
| Tijd voor het eerste resultaat | < 2 ms |
| Geheugenschaling (1K-50K tx) | Constant (streaming) |
| Testdekking | 100% vestigingsdekking |
| Testen | 467 verdeeld over 29 testbestanden |

## Begin met bouwen

[Aan de slag met installatie en voorbeelden ❯][01]

[01]: /getting-started/index.html "Aan de slag"
 "GitHub-opslagplaats"
