---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Änderungsprotokoll zum Kontoauszugsparser"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Kontoauszugsparser. Alle Rechte vorbehalten."
date: "Apr 11, 2026"
description: "Versionsverlauf und Änderungsprotokoll für Bank Statement Parser. Verfolgen Sie neue Funktionen, Verbesserungen und Fehlerbehebungen in allen Versionen."
download: ""
format-detection: "telephone=no"
hreflang: "de"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/de/aenderungsprotokoll/index.html"
image_alt: "Logo von Bank Statement Parser, stärken Sie Ihre Finanzanalyse mit nahtloser Datenextraktion"
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "Änderungsprotokoll zum Kontoauszugsparser, Versionshinweise, Versionsverlauf, Aktualisierungen"
language: "de-DE"
layout: "about"
locale: "de_DE"
logo_alt: "Logo von Bank Statement Parser, stärken Sie Ihre Finanzanalyse mit nahtloser Datenextraktion"
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Änderungsprotokoll"
permalink: "https://bankstatementparser.com/de/aenderungsprotokoll/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Veröffentlichungsverlauf und Neuigkeiten"
tags: "Änderungsprotokoll, Veröffentlichungen, Updates, Versionen, Ankündigungen, Blog"
theme_color: "rgb(73, 214, 251)"
title: "Änderungsprotokoll zum Kontoauszugsparser"
url: "https://bankstatementparser.com/de/aenderungsprotokoll/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/de/aenderungsprotokoll/rss.xml"
category: "Finanzsoftware, Python-Bibliothek, Datenverarbeitung"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Versionsverlauf und Änderungsprotokoll für Bank Statement Parser. Verfolgen Sie neue Funktionen, Verbesserungen und Fehlerbehebungen in allen Versionen."
item_guid: "https://bankstatementparser.com/de/aenderungsprotokoll/rss.xml"
item_link: "https://bankstatementparser.com/de/aenderungsprotokoll/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Änderungsprotokoll zum Kontoauszugsparser"
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
apple-mobile-web-app-title: "Änderungsprotokoll zum Kontoauszugsparser"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Versionsverlauf und Änderungsprotokoll für Bank Statement Parser. Verfolgen Sie neue Funktionen, Verbesserungen und Fehlerbehebungen in allen Versionen."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logo von Bank Statement Parser, stärken Sie Ihre Finanzanalyse mit nahtloser Datenextraktion"
twitter_site: "@wwdseb"
twitter_title: "Änderungsprotokoll zum Kontoauszugsparser"
twitter_url: "https://bankstatementparser.com/de/aenderungsprotokoll/index.html"

# Humans.txt - The Humans.txt front matter (YAML).

author_website: "https://bankstatementparser.com"
author_twitter: "@wwdseb"
author_location: "London, UK"
thanks: "Danke fürs Lesen!"
site_last_updated: "2026-04-01"
site_standards: "HTML5, CSS3, RSS, Atom, JSON, XML, YAML, Markdown, TOML"
site_components: "Shokunin SSG, Shokunin CLI, Shokunin Templates, Shokunin Themes, Kaishi SSG, Kaishi CLI, Kaishi Templates, Kaishi Themes"
site_software: "Shokunin, Rust"

---

Verfolgen Sie die Entwicklung des Bank Statement Parser. Abonnieren Sie über [RSS](/changelog/rss.xml) oder schauen Sie sich das [GitHub-Repository] an (https://github.com/sebastienrousseau/bankstatementparser) für Freigabebenachrichtigungen.

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

## v0.0.4 – 15.03.2026 (Neueste)

- Paralleles Parsen von Dateien mit hinzugefügt`parse_files_parallel()`mit ProcessPoolExecutor.
– Echtes Streaming für große PAIN.001-Dateien (50 MB+) mit begrenztem Speicher hinzugefügt.
- Leistungsoptimierungen: Der CAMT-Durchsatz übersteigt jetzt 27.000 Tx/s, PAIN.001 übersteigt 52.000 Tx/s.
- Hinzugefügt`Deduplicator`Klasse zum Erkennen exakter Duplikate und vermuteter Übereinstimmungen mit Konfidenzwerten.
- Hinzugefügt`from_string()`Und`from_bytes()`Methoden für das In-Memory-Parsing ohne Festplatten-I/O.
- Hinzugefügt`iter_secure_xml_entries()`für die sichere Verarbeitung von ZIP-Archiven.
– Erweitertes CI mit Durchsetzung von Leistungsschwellenwerten.

## v0.0.3 – 20.11.2025

- CSV-, OFX-, QFX- und MT940-Parser-Unterstützung hinzugefügt.
- Automatische Formaterkennung mit hinzugefügt`detect_statement_format()`Und`create_parser()`.
– PII-Schwärzung hinzugefügt (standardmäßig aktiviert im CLI- und Streaming-Modus).
- Exporthilfen für CSV, JSON und Excel hinzugefügt.
- Optionale Polars DataFrame-Unterstützung hinzugefügt.
- Erweiterte Testsuite auf 718 Tests mit 100 % Zweigstellenabdeckung.

## v0.0.2 – 10.06.2025

- PAIN.001-Parser hinzugefügt (`Pain001Parser`) für ISO 20022-Credit-Transfer-Initiierungsdateien.
- CLI-Schnittstelle hinzugefügt (`python -m bankstatementparser.cli`).
- Streaming-Modus mit hinzugefügt`parse_streaming()`.
- Eingabevalidierung und Dateigrößenbeschränkungen hinzugefügt.

## v0.0.1 – 15.01.2025

- Erstveröffentlichung.
- CAMT.053-Parser (`CamtParser`) für Bank-zu-Kunden-Kontoauszüge nach ISO 20022.
- Pandas DataFrame-Ausgabe.
- Grundlegende XML-Sicherheitshärtung (XXE-Schutz, no_network).

Sehen Sie sich den vollständigen Commit-Verlauf auf [GitHub] an.https://github.com/sebastienrousseau/bankstatementparser/commits/main).

<script type="application/ld+json">
{
  „@context“: „https://schema.org",
  „@type“: „SoftwareApplication“,
  „name“: „Kontoauszug-Parser“,
  „applicationCategory“: „DeveloperApplication“,
  „operatingSystem“: „Plattformübergreifend“,
  „softwareVersion": "0.0.8“,
  „datePublished“: „2026-03-15“,
  „releaseNotes“: „Paralleles Dateiparsing, echtes Streaming für PAIN.001, Leistungsoptimierungen (27K+ tx/s CAMT, 52K+ tx/s PAIN.001), Deduplicator-Klasse, In-Memory-Parsing, sichere ZIP-Verarbeitung hinzugefügt.“,
  „downloadUrl“: „https://pypi.org/project/bankstatementparser/",
  „Lizenz“: „https://opensource.org/licenses/Apache-2.0",
  „Autor“: {
    „@type“: „Person“,
    „Name“: „Sebastien Rousseau“
  }
}
</script>
