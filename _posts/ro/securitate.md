---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Securitate analizator extras de cont"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/corporate-finance.webp"
cdn: "https://cloudcdn.pro"
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Analizator extras de cont. Toate drepturile rezervate."
date: "Apr 01, 2026"
description: "Caracteristici de securitate ale analizorului extras de cont: protecție XXE, întărire cu bombă ZIP, redarea PII, securitatea lanțului de aprovizionare, ieșire deterministă și versiuni semnate."
download: ""
format-detection: "telephone=no"
hreflang: "ro"
icon: "https://cloudcdn.pro/bankstatementparser/images/favicon.ico"
id: "https://bankstatementparser.com/ro/securitate/index.html"
image_alt: "Sigla Analizor extras de cont bancar, împuterniciți-vă analiza financiară cu extragerea fără întreruperi a datelor"
image_height: "630"
image_width: "1200"
image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
keywords: "Securitate extras de cont bancar, PII redactare python, protecție XXE, protecție ZIP bombă, securitate lanțului de aprovizionare SBOM, analiza deterministă, securitatea datelor financiare"
language: "ro-RO"
layout: "about"
locale: "ro_RO"
logo_alt: "Sigla Analizor extras de cont bancar, împuterniciți-vă analiza financiară cu extragerea fără întreruperi a datelor"
logo_height: "44"
logo_width: "44"
logo: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Securitate"
permalink: "https://bankstatementparser.com/ro/securitate/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Cum vă protejăm datele financiare"
tags: "securitate,pii,xxe,sbom,lanțul de aprovizionare,determinist"
theme_color: "rgb(73, 214, 251)"
title: "Securitate analizator extras de cont: protecția datelor și lanțul de aprovizionare"
url: "https://bankstatementparser.com/ro/securitate/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/ro/securitate/rss.xml"
category: "Software pentru finanțe, Biblioteca Python, Procesarea datelor"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Caracteristici de securitate ale analizorului extras de cont: protecție XXE, întărire cu bombă ZIP, redarea PII, securitatea lanțului de aprovizionare, ieșire deterministă și versiuni semnate."
item_guid: "https://bankstatementparser.com/ro/securitate/rss.xml"
item_link: "https://bankstatementparser.com/ro/securitate/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Securitate analizator extras de cont: protecția datelor și lanțul de aprovizionare"
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
apple-mobile-web-app-title: "Securitate analizator extras de cont: protecția datelor și lanțul de aprovizionare"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Caracteristici de securitate ale analizorului extras de cont: protecție XXE, întărire cu bombă ZIP, redarea PII, securitatea lanțului de aprovizionare, ieșire deterministă și versiuni semnate."
twitter_image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
twitter_image_alt: "Sigla Analizor extras de cont bancar, împuterniciți-vă analiza financiară cu extragerea fără întreruperi a datelor"
twitter_site: "@wwdseb"
twitter_title: "Securitate analizator extras de cont: protecția datelor și lanțul de aprovizionare"
twitter_url: "https://bankstatementparser.com/ro/securitate/index.html"

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

**TL;DR:** Bank Statement Parser nu efectuează apeluri de rețea, elimină PII în mod implicit, întărește analiza XML împotriva atacurilor XXE și este livrat cu dependențe SHA-256 blocate cu hash și un SBOM CycloneDX.

## Securitate prin proiectare

Analiza extrasului bancar este creat pentru procesarea datelor financiare sensibile. Fiecare decizie de proiectare acordă prioritate securității, confidențialității și auditabilității.

## Acces zero la rețea

Toată procesarea are loc local în timpul de execuție. Biblioteca efectuează zero apeluri API, zero conexiuni la cloud și colectează zero telemetrie. Analizoarele XML sunt configurate explicit cu`no_network=True`, `resolve_entities=False`, și`load_dtd=False`pentru a preveni orice acces la ieșire.

## Redactare IPI

Informațiile de identificare personală (nume, IBAN-uri, adrese poștale) sunt redactate automat în modul de ieșire și streaming CLI. Aceasta este activată în mod implicit.

- **CLI**: Câmpurile sensibile arată ca`***REDACTED***`
- **Streaming**:`parse_streaming(redact_pii=True)`(implicit)
- **Exporturi**: CSV/JSON/Excel păstrează datele complete pentru procesarea în aval
- **Opt-in**: Utilizați`--show-pii`sau`redact_pii=False`când aveți nevoie de rezultate neredatate

## Securitate XML (protecție XXE)

Toate utilizările de analiză XML`lxml`cu setări întărite:

- `resolve_entities=False`-- previne atacurile de extindere a entităților XML
-`no_network=True`-- blochează toate accesul la rețea de ieșire de la parser
-`load_dtd=False`-- previne atacurile bazate pe DTD
- Eliminarea spațiului de nume înainte de procesare -- gestionează orice variantă CAMT.053 în siguranță

## Securitatea arhivei ZIP

`iter_secure_xml_entries()`validează fiecare membru ZIP înainte de extragere:

- **Limite pentru dimensiunea intrării**: 10 MB per intrare (configurabil)
- **Dimensiunea maximă totală**: 50 MB total necomprimat (configurabil)
- **Limita raportului de compresie**: 100:1 implicit -- detectează bombe ZIP
- **Respingerea intrării criptate**: intrările criptate sunt omise cu un avertisment
- **Fără scriere pe disc**: octeții XML trec direct la parser prin`from_bytes()`

## Prevenirea traversării căilor

Validarea intrărilor blochează căile periculoase ale fișierelor:

- Octeți nuli, modele de traversare a directoarelor (`../`), iar linkurile simbolice sunt respinse
- Validarea extensiilor de fișiere față de formatele așteptate
- Limite de dimensiune a fișierului (100 MB implicit, configurabil)

## Ieșire deterministă

Având în vedere același fișier de intrare, analizatorul produce o ieșire identică pentru octeți la fiecare rulare. Fără aleatorie, fără inferență de model, fără eșantionare euristică. Acest lucru este critic pentru:

- **Reproducibilitate de audit**: Rulați același fișier de două ori și diferențiază rezultatul
- **Conformitatea cu reglementările**: Demonstrați o procesare consecventă
- **Verificare CI**: 467 de teste impun determinismul cu o acoperire de 100% a ramurilor

## Securitatea lanțului de aprovizionare

- **SHA-256 dependențe blocate cu hash**: fiecare pachet în`poetry.lock`are hash-uri verificate de fișiere
- **CycloneDX SBOM**: Fiecare versiune include o listă de materiale software
- **Proveniența construcției GitHub**: Atestarea leagă fiecare artefact la comiterea sursă
- **Signed commits**: Toate commit-urile sunt semnate SSH și verificate în CI
- **Verificarea dependenței**:`scripts/verify_locked_hashes.py`validează toate hashurile la nivel local

## Verificați local

```bash
python -m pytest                          # 467 tests, 100% branch coverage
python scripts/verify_locked_hashes.py    # SHA-256 hash verification
git log --show-signature -1               # Verify commit signature
```
