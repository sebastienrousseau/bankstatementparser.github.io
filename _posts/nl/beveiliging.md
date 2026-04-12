---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Parserbeveiliging van bankafschriften"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Parser voor bankafschriften. Alle rechten voorbehouden."
date: "Apr 11, 2026"
description: "Beveiligingsfuncties van Bank Statement Parser: XXE-bescherming, ZIP-bomverharding, PII-redactie, beveiliging van de toeleveringsketen, deterministische uitvoer en ondertekende builds."
download: ""
format-detection: "telephone=no"
hreflang: "nl"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/nl/beveiliging/index.html"
image_alt: "Logo van Bank Statement Parser, maak uw financiële analyse mogelijk met naadloze gegevensextractie"
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "beveiliging van bankafschriften, PII-redactiepython, XXE-bescherming, ZIP-bombeveiliging, beveiliging van de toeleveringsketen SBOM, deterministische parsing, beveiliging van financiële gegevens"
language: "nl-NL"
layout: "about"
locale: "nl_NL"
logo_alt: "Logo van Bank Statement Parser, maak uw financiële analyse mogelijk met naadloze gegevensextractie"
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Beveiliging"
permalink: "https://bankstatementparser.com/nl/beveiliging/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Hoe wij uw financiële gegevens beschermen"
tags: "veiligheid,pii,xxe,sbom,toeleveringsketen,deterministisch"
theme_color: "rgb(73, 214, 251)"
title: "Beveiliging van bankafschriftenparser: gegevensbescherming en toeleveringsketen"
url: "https://bankstatementparser.com/nl/beveiliging/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/nl/beveiliging/rss.xml"
category: "Financiële software, Python-bibliotheek, gegevensverwerking"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Beveiligingsfuncties van Bank Statement Parser: XXE-bescherming, ZIP-bomverharding, PII-redactie, beveiliging van de toeleveringsketen, deterministische uitvoer en ondertekende builds."
item_guid: "https://bankstatementparser.com/nl/beveiliging/rss.xml"
item_link: "https://bankstatementparser.com/nl/beveiliging/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Beveiliging van bankafschriftenparser: gegevensbescherming en toeleveringsketen"
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
apple-mobile-web-app-title: "Beveiliging van bankafschriftenparser: gegevensbescherming en toeleveringsketen"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Beveiligingsfuncties van Bank Statement Parser: XXE-bescherming, ZIP-bomverharding, PII-redactie, beveiliging van de toeleveringsketen, deterministische uitvoer en ondertekende builds."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logo van Bank Statement Parser, maak uw financiële analyse mogelijk met naadloze gegevensextractie"
twitter_site: "@wwdseb"
twitter_title: "Beveiliging van bankafschriftenparser: gegevensbescherming en toeleveringsketen"
twitter_url: "https://bankstatementparser.com/nl/beveiliging/index.html"

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

**TL;DR:** Bank Statement Parser verwerkt alle gegevens lokaal, redigeert PII standaard, verhardt XML-parsing tegen XXE-aanvallen, draait LLM's lokaal via Ollama en wordt geleverd met SHA-256 hash-locked afhankelijkheden en een CycloneDX SBOM.

## Beveiliging door ontwerp

Bank Statement Parser is gebouwd voor het verwerken van gevoelige financiële gegevens. Elke ontwerpbeslissing geeft prioriteit aan beveiliging, privacy en controleerbaarheid.

## Geen cloudafhankelijkheid

Alle verwerking gebeurt lokaal binnen uw runtime. De deterministische parsers maken nul netwerkoproepen. De hybride PDF-pipeline gebruikt Ollama voor lokale LLM-inferentie — er worden geen gegevens naar cloud-API's gestuurd. XML-parsers zijn expliciet geconfigureerd met `no_network=True`, `resolve_entities=False` en `load_dtd=False` om uitgaande toegang te voorkomen.

## PII-redactie

Persoonlijk identificeerbare informatie (namen, IBAN's, postadressen) wordt automatisch geredigeerd in CLI-uitvoer en streaming-modus. Dit staat standaard aan.

- **CLI**: Gevoelige velden worden weergegeven als `***REDACTED***`
- **Streaming**: `parse_streaming(redact_pii=True)` (standaard)
- **Exports**: CSV/JSON/Excel behoudt volledige gegevens voor verdere verwerking
- **Opt-in**: Gebruik `--show-pii` of `redact_pii=False` wanneer u niet-geredigeerde uitvoer nodig heeft

## XML-beveiliging (XXE-bescherming)

Alle XML-parsing gebruikt `lxml` met geharde instellingen:

- `resolve_entities=False` -- voorkomt XML entity expansion-aanvallen
- `no_network=True` -- blokkeert alle uitgaande netwerktoegang van de parser
- `load_dtd=False` -- voorkomt DTD-gebaseerde aanvallen
- Naamruimtestripping vóór verwerking -- verwerkt elke CAMT.053-variant veilig

## ZIP-archiefbeveiliging

`iter_secure_xml_entries()` valideert elk ZIP-bestand vóór extractie:

- **Maximale invoergrootte**: 10 MB per bestand (configureerbaar)
- **Totale maximale grootte**: 50 MB totaal ongecomprimeerd (configureerbaar)
- **Compressieverhoudingslimiet**: standaard 100:1 -- detecteert ZIP-bommen
- **Afwijzing van versleutelde bestanden**: Versleutelde bestanden worden overgeslagen met een waarschuwing
- **Geen schijfschrijfbewerkingen**: XML-bytes gaan rechtstreeks naar de parser via `from_bytes()`

## Pad-traversalpreventie

Invoervalidatie blokkeert gevaarlijke bestandspaden:

- Null bytes, directory-traversalpatronen (`../`) en symlinks worden afgewezen
- Validatie van bestandsextensies tegen verwachte formaten
- Bestandsgroottelimieten (standaard 100 MB, configureerbaar)

## Saldoverificatie (Golden Rule)

Elke PDF-extractie wordt geverifieerd met de formule: `opening balance + credits − debits == closing balance`. Resultaten worden gemarkeerd als VERIFIED, DISCREPANCY of FAILED. Afwijkingen kunt u interactief beoordelen met `--type review`.

## Deterministische uitvoer

Voor gestructureerde formaten (CAMT, PAIN.001, CSV, OFX, QFX, MT940) produceert de parser bij hetzelfde invoerbestand elke run byte-identieke uitvoer. Geen willekeur, geen modelinferentie, geen heuristische bemonstering. Dit is essentieel voor:

- **Auditreproduceerbaarheid**: Voer hetzelfde bestand twee keer uit en vergelijk de uitvoer
- **Naleving van regelgeving**: Toon consistente verwerking aan
- **CI-verificatie**: 718 tests dwingen determinisme af met 100% branchdekking

## Supply-chainbeveiliging

- **SHA-256 hash-locked afhankelijkheden**: Elk pakket in `poetry.lock` heeft geverifieerde bestandshashes
- **CycloneDX SBOM**: Elke release bevat een Software Bill of Materials
- **GitHub build-herkomst**: Attestation koppelt elk artefact aan zijn broncommit
- **Ondertekende commits**: Alle commits zijn SSH-ondertekend en geverifieerd in CI
- **Afhankelijkheidsverificatie**: `scripts/verify_locked_hashes.py` valideert alle hashes lokaal

## Lokaal verifiëren

```bash
python -m pytest                          # 718 tests, 100% branch coverage
python scripts/verify_locked_hashes.py    # SHA-256 hash verification
git log --show-signature -1               # Verify commit signature
```
