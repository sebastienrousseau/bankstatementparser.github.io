---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Securitate analizator extras de cont"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Analizator extras de cont. Toate drepturile rezervate."
date: "Apr 11, 2026"
description: "Caracteristici de securitate ale analizorului extras de cont: protecție XXE, întărire cu bombă ZIP, redarea PII, securitatea lanțului de aprovizionare, ieșire deterministă și versiuni semnate."
download: ""
format-detection: "telephone=no"
hreflang: "ro"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/ro/securitate/index.html"
image_alt: "Sigla Analizor extras de cont bancar, împuterniciți-vă analiza financiară cu extragerea fără întreruperi a datelor"
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "Securitate extras de cont bancar, PII redactare python, protecție XXE, protecție ZIP bombă, securitate lanțului de aprovizionare SBOM, analiza deterministă, securitatea datelor financiare"
language: "ro-RO"
layout: "about"
locale: "ro_RO"
logo_alt: "Sigla Analizor extras de cont bancar, împuterniciți-vă analiza financiară cu extragerea fără întreruperi a datelor"
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
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
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Caracteristici de securitate ale analizorului extras de cont: protecție XXE, întărire cu bombă ZIP, redarea PII, securitatea lanțului de aprovizionare, ieșire deterministă și versiuni semnate."
twitter_image: "/images/logos/bankstatementparser.webp"
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

**TL;DR:** Bank Statement Parser procesează toate datele local, redactează PII implicit, securizează parsarea XML împotriva atacurilor XXE, rulează LLM-uri local prin Ollama și este livrat cu dependențe SHA-256 blocate cu hash și un SBOM CycloneDX.

## Securitate prin design

Bank Statement Parser este construit pentru procesarea datelor financiare sensibile. Fiecare decizie de proiectare prioritizează securitatea, confidențialitatea și auditabilitatea.

## Zero dependență de cloud

Toată procesarea are loc local în runtime. Parserele deterministe nu efectuează niciun apel de rețea. Pipeline-ul hibrid PDF folosește Ollama pentru inferență LLM locală — nicio dată nu este trimisă către API-uri cloud. Parserele XML sunt configurate explicit cu `no_network=True`, `resolve_entities=False` și `load_dtd=False` pentru a preveni orice acces de ieșire.

## Redactare PII

Informațiile de identificare personală (nume, IBAN-uri, adrese poștale) sunt redactate automat în ieșirea CLI și modul streaming. Funcția este activată implicit.

- **CLI**: Câmpurile sensibile apar ca `***REDACTED***`
- **Streaming**: `parse_streaming(redact_pii=True)` (implicit)
- **Exporturi**: CSV/JSON/Excel păstrează datele complete pentru procesarea ulterioară
- **Activare**: Folosiți `--show-pii` sau `redact_pii=False` când aveți nevoie de ieșire neredactată

## Securitate XML (protecție XXE)

Toată parsarea XML folosește `lxml` cu setări securizate:

- `resolve_entities=False` -- previne atacurile de expandare a entităților XML
- `no_network=True` -- blochează tot accesul de rețea de ieșire de la parser
- `load_dtd=False` -- previne atacurile bazate pe DTD
- Eliminarea namespace-ului înainte de procesare -- gestionează orice variantă CAMT.053 în siguranță

## Securitatea arhivelor ZIP

`iter_secure_xml_entries()` validează fiecare membru ZIP înainte de extragere:

- **Limită de dimensiune per intrare**: 10 MB per intrare (configurabil)
- **Limită dimensiune totală**: 50 MB total necomprimat (configurabil)
- **Limită raport de compresie**: 100:1 implicit -- detectează ZIP bomb
- **Respingere intrări criptate**: Intrările criptate sunt omise cu un avertisment
- **Fără scriere pe disc**: Octeții XML trec direct la parser prin `from_bytes()`

## Prevenirea traversării căilor

Validarea intrărilor blochează căile periculoase de fișiere:

- Octeții nuli, tiparele de traversare a directoarelor (`../`) și legăturile simbolice sunt respinse
- Validarea extensiilor de fișiere față de formatele așteptate
- Limite de dimensiune a fișierului (100 MB implicit, configurabil)

## Verificarea soldului (Regula de Aur)

Fiecare extracție PDF este verificată cu ecuația: `opening balance + credits − debits == closing balance`. Rezultatele sunt etichetate ca VERIFIED, DISCREPANCY sau FAILED. Discrepanțele pot fi revizuite interactiv cu `--type review`.

## Ieșire deterministă

Pentru formatele structurate (CAMT, PAIN.001, CSV, OFX, QFX, MT940), cu același fișier de intrare, parserul produce ieșire identică la nivel de octet la fiecare rulare. Fără aleatorism, fără inferență de model, fără eșantionare euristică. Acest lucru este esențial pentru:

- **Reproductibilitate de audit**: Rulați același fișier de două ori și comparați rezultatul
- **Conformitate reglementară**: Demonstrați procesare consecventă
- **Verificare CI**: 718 teste impun determinismul cu acoperire de 100% a ramurilor

## Securitatea lanțului de aprovizionare

- **Dependențe SHA-256 blocate cu hash**: Fiecare pachet din `poetry.lock` are hash-uri de fișiere verificate
- **CycloneDX SBOM**: Fiecare versiune include o listă de materiale software
- **Proveniența build-ului GitHub**: Atestarea leagă fiecare artefact la commit-ul sursă
- **Commit-uri semnate**: Toate commit-urile sunt semnate SSH și verificate în CI
- **Verificarea dependențelor**: `scripts/verify_locked_hashes.py` validează toate hash-urile local

## Verificați local

```bash
python -m pytest                          # 718 tests, 100% branch coverage
python scripts/verify_locked_hashes.py    # SHA-256 hash verification
git log --show-signature -1               # Verify commit signature
```
