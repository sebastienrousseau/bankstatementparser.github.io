---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Wijzigingslogboek voor parser van bankafschriften"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Parser voor bankafschriften. Alle rechten voorbehouden."
date: "Apr 11, 2026"
description: "Releasegeschiedenis en wijzigingslogboek voor bankafschriftparser. Volg nieuwe functies, verbeteringen en bugfixes in alle versies."
download: ""
format-detection: "telephone=no"
hreflang: "nl"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/nl/wijzigingslogboek/index.html"
image_alt: "Logo van Bank Statement Parser, maak uw financiële analyse mogelijk met naadloze gegevensextractie"
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "bankafschrift parser changelog, release-opmerkingen, versiegeschiedenis, updates"
language: "nl-NL"
layout: "about"
locale: "nl_NL"
logo_alt: "Logo van Bank Statement Parser, maak uw financiële analyse mogelijk met naadloze gegevensextractie"
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Wijzigingslog"
permalink: "https://bankstatementparser.com/nl/wijzigingslogboek/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Releasegeschiedenis en wat er nieuw is"
tags: "changelog,releases,updates,versies,aankondigingen,blog"
theme_color: "rgb(73, 214, 251)"
title: "Wijzigingslogboek voor parser van bankafschriften"
url: "https://bankstatementparser.com/nl/wijzigingslogboek/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/nl/wijzigingslogboek/rss.xml"
category: "Financiële software, Python-bibliotheek, gegevensverwerking"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Releasegeschiedenis en wijzigingslogboek voor bankafschriftparser. Volg nieuwe functies, verbeteringen en bugfixes in alle versies."
item_guid: "https://bankstatementparser.com/nl/wijzigingslogboek/rss.xml"
item_link: "https://bankstatementparser.com/nl/wijzigingslogboek/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Wijzigingslogboek voor parser van bankafschriften"
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
apple-mobile-web-app-title: "Wijzigingslogboek voor parser van bankafschriften"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Releasegeschiedenis en wijzigingslogboek voor bankafschriftparser. Volg nieuwe functies, verbeteringen en bugfixes in alle versies."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logo van Bank Statement Parser, maak uw financiële analyse mogelijk met naadloze gegevensextractie"
twitter_site: "@wwdseb"
twitter_title: "Wijzigingslogboek voor parser van bankafschriften"
twitter_url: "https://bankstatementparser.com/nl/wijzigingslogboek/index.html"

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

Volg de ontwikkeling van de bankafschriftparser. Abonneer je via [RSS](/changelog/rss.xml) of bekijk de [GitHub-repository](https://github.com/sebastienrousseau/bankstatementparser) voor releasemeldingen.

## v0.0.8 — 2026-04-11 (Latest) — "Full Platform"

- Multi-currency balance verification — `verify_balance_multi_currency()` groups by currency, runs Golden Rule per group.
- hledger + beancount export — `to_hledger()` and `to_beancount()` in `bankstatementparser.export`.
- Bulk directory scanner — `scan_and_ingest()` scans folder trees, deduplicates across batch.
- Account mapping rules — `AccountMapper` with ordered regex rules from JSON config.
- REST API — FastAPI wrapper with `/ingest` and `/health` endpoints (`[api]` extra).

## v0.0.7 — 2026-04-08 — "Universal Vision"

- Direct Ollama bridge (`ollama_direct_completion`) — bypasses LiteLLM long-prompt hang.
- Strip mode (`VisionExtractor.strip_rows=True`) — splits dense pages into overlapping bands for small local models.
- Recommended vision model changed from `llava` to `minicpm-v`.

## v0.0.6 — 2026-04-08 — "Intelligence Layer"

- Dropped Python 3.9 support (now 3.10-3.14).
- Enrichment module (`Categorizer`, `EnrichedTransaction`, `DEFAULT_CATEGORY_SCHEMA`).
- Interactive review mode with `--type review` CLI command.
- Per-row bounding box extraction (`Transaction.source_bbox`).

## v0.0.5 — 2026-04-08 — "Universal Extraction"

- Hybrid PDF pipeline (`smart_ingest()`) with deterministic/text-LLM/vision-LLM routing.
- `LLMExtractor` for digital PDFs via LiteLLM.
- `VisionExtractor` for scanned PDFs via multimodal vision models.
- Golden Rule balance verification (`opening + credits - debits == closing`).
- Idempotent deduplication via `transaction_hash` (MD5 fingerprint).

## v0.0.4 — 15-03-2026 (laatste)

- Parallelle bestandsparsering toegevoegd met`parse_files_parallel()`met behulp van ProcessPoolExecutor.
- Echte streaming toegevoegd voor grote PAIN.001-bestanden (50 MB+) met begrensd geheugen.
- Prestatieoptimalisaties: CAMT-doorvoer overschrijdt nu 27.000 tx/s, PAIN.001 overschrijdt 52.000 tx/s.
- Toegevoegd`Deduplicator`klasse voor het detecteren van exacte duplicaten en vermoedelijke overeenkomsten met betrouwbaarheidsscores.
- Toegevoegd`from_string()`En`from_bytes()`methoden voor parseren in het geheugen zonder schijf-I/O.
- Toegevoegd`iter_secure_xml_entries()`voor veilige ZIP-archiefverwerking.
- Uitgebreide CI met handhaving van prestatiedrempels.

## v0.0.3 — 20-11-2025

- Ondersteuning voor CSV-, OFX-, QFX- en MT940-parser toegevoegd.
- Automatische detectie van formaten toegevoegd met`detect_statement_format()`En`create_parser()`.
- PII-redactie toegevoegd (standaard ingeschakeld in CLI- en streamingmodus).
- Exporthulpmiddelen toegevoegd voor CSV, JSON en Excel.
- Optionele Polars DataFrame-ondersteuning toegevoegd.
- Uitgebreide testsuite naar 718 tests met 100% vestigingsdekking.

## v0.0.2 — 10-06-2025

- PAIN.001-parser toegevoegd (`Pain001Parser`) voor ISO 20022-initiatiebestanden voor overboekingen.
- CLI-interface toegevoegd (`python -m bankstatementparser.cli`).
- Streamingmodus toegevoegd met`parse_streaming()`.
- Toegevoegde invoervalidatie en bestandsgroottelimieten.

## v0.0.1 — 15-01-2025

- Eerste uitgave.
- CAMT.053-parser (`CamtParser`) voor bank-naar-klantafschriften volgens ISO 20022.
- panda's DataFrame-uitvoer.
- Basisversterking van XML-beveiliging (XXE-bescherming, no_network).

Bekijk de volledige commitgeschiedenis op [GitHub](https://github.com/sebastienrousseau/bankstatementparser/commits/main).

<script type="applicatie/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Softwaretoepassing",
  "name": "Bankafschriftparser",
  "applicationCategory": "DeveloperApplication",
  "operatingSystem": "Interplatform",
  "softwareversie": "0.0.4",
  "datePublished": "15-03-2026",
  "releaseNotes": "Parallelle bestandsparsing toegevoegd, echte streaming voor PAIN.001, prestatie-optimalisaties (27K+ tx/s CAMT, 52K+ tx/s PAIN.001), Deduplicator-klasse, parsing in het geheugen, veilige ZIP-verwerking.",
  "downloadUrl": "https://pypi.org/project/bankstatementparser/",
  "licentie": "https://opensource.org/licenses/Apache-2.0",
  "auteur": {
    "@type": "Persoon",
    "naam": "Sebastien Rousseau"
  }
}
</script>
