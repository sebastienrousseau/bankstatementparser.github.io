---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Fassarar Canjin Bayanan Banki"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Fassarar Bayanin Banki. An kiyaye duk haƙƙoƙi."
date: "Apr 11, 2026"
description: "Saki tarihin da canji na bayanin Bayanan Banki. Bibiyar sabbin fasalulluka, haɓakawa, da gyare-gyaren kwaro a duk nau'ikan."
download: ""
format-detection: "telephone=no"
hreflang: "ha"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/ha/journal-des-modifications/index.html"
image_alt: "Tambarin Fassarar Bayanin Banki, Ƙarfafa Binciken Kuɗi na Kuɗi tare da Haɓakar Bayanai mara Tsayi"
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "canjin bayanan banki, bayanin kula, tarihin sigar, sabuntawa"
language: "ha-NG"
layout: "about"
locale: "ha_NG"
logo_alt: "Tambarin Fassarar Bayanin Banki, Ƙarfafa Binciken Kuɗi na Kuɗi tare da Haɓakar Bayanai mara Tsayi"
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Canji"
permalink: "https://bankstatementparser.com/ha/journal-des-modifications/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Saki Tarihi da Menene Sabo"
tags: "canji, sakewa, sabuntawa, sigogin, sanarwa, bulogi"
theme_color: "rgb(73, 214, 251)"
title: "Fassarar Canjin Bayanan Banki"
url: "https://bankstatementparser.com/ha/journal-des-modifications/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/ha/journal-des-modifications/rss.xml"
category: "Software na Kuɗi, Laburaren Python, Gudanar da Bayanai"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Saki tarihin da canji na bayanin Bayanan Banki. Bibiyar sabbin fasalulluka, haɓakawa, da gyare-gyaren kwaro a duk nau'ikan."
item_guid: "https://bankstatementparser.com/ha/journal-des-modifications/rss.xml"
item_link: "https://bankstatementparser.com/ha/journal-des-modifications/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Fassarar Canjin Bayanan Banki"
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
apple-mobile-web-app-title: "Fassarar Canjin Bayanan Banki"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Saki tarihin da canji na bayanin Bayanan Banki. Bibiyar sabbin fasalulluka, haɓakawa, da gyare-gyaren kwaro a duk nau'ikan."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Tambarin Fassarar Bayanin Banki, Ƙarfafa Binciken Kuɗi na Kuɗi tare da Haɓakar Bayanai mara Tsayi"
twitter_site: "@wwdseb"
twitter_title: "Fassarar Canjin Bayanan Banki"
twitter_url: "https://bankstatementparser.com/ha/journal-des-modifications/index.html"

# Humans.txt - The Humans.txt front matter (YAML).

author_website: "https://bankstatementparser.com"
author_twitter: "@wwdseb"
author_location: "London, UK"
thanks: "Na gode da karantawa!"
site_last_updated: "2026-04-01"
site_standards: "HTML5, CSS3, RSS, Atom, JSON, XML, YAML, Markdown, TOML"
site_components: "Shokunin SSG, Shokunin CLI, Shokunin Templates, Shokunin Themes, Kaishi SSG, Kaishi CLI, Kaishi Templates, Kaishi Themes"
site_software: "Shokunin, Rust"

---

Bi Ci gaban Fassarar Bayanin Banki. Biyan kuɗi ta [RSS] (/changelog/rss.xml) ko kalli [majigin GitHub](https://github.com/sebastienrousseau/bankstatementparser) don sanarwar sanarwa.

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

## v0.0.4 - 2026-03-15 (Na baya)

- Ƙara daidaitaccen fayil ɗin bincike tare da`parse_files_parallel()`ta amfani da ProcessPoolExecutor.
- Ƙara ingantaccen yawo don manyan fayilolin PAIN.001 (50 MB+) tare da ƙayyadaddun ƙwaƙwalwar ajiya.
- Haɓaka aiki: Abubuwan da aka samar na CAMT yanzu sun wuce 27,000 tx/s, PAIN.001 ya wuce 52,000 tx/s.
- Kara`Deduplicator`aji don gano ainihin kwafi da matches da ake zargi tare da makin amincewa.
- Kara`from_string()`kuma`from_bytes()`hanyoyin don tantancewa cikin ƙwaƙwalwar ajiya ba tare da faifai I/O ba.
- Kara`iter_secure_xml_entries()`don amintaccen sarrafa kayan tarihin ZIP.
- Ƙarfafa CI tare da aiwatar da matakin aiki.

## v0.0.3 - 2025-11-20

- Ƙara CSV, OFX, QFX, da tallafin parser MT940.
- Ƙara tsarin ganowa ta atomatik tare da`detect_statement_format()`kuma`create_parser()`.
- Ƙara sabuntawar PII (a kunne ta tsohuwa a cikin CLI da yanayin yawo).
- Ƙara mataimakan fitarwa zuwa CSV, JSON, da Excel.
- Ƙara goyon bayan Polars DataFrame na zaɓi.
- Fadada ɗakin gwaji zuwa gwaje-gwaje 718 tare da ɗaukar hoto 100%.

## v0.0.2 - 2025-06-10

- An ƙara PAIN.001 parser (`Pain001Parser`) don fayilolin ƙaddamar da canja wurin kuɗi na ISO 20022.
- Ƙara CLI interface (`python -m bankstatementparser.cli`).
- Ƙara yanayin yawo tare da`parse_streaming()`.
- Ƙara ingantaccen shigarwar da iyakokin girman fayil.

## v0.0.1 - 2025-01-15

- Sakin farko.
Bayani: CAMT.053`CamtParser`) don bayanan banki-da-abokin ciniki na ISO 20022.
- Pandas DataFrame fitarwa.
- Ƙarfafa tsaro na XML na asali (kariyar XXE, no_network).

Duba cikakken tarihin sadaukarwa akan [GitHub](https://github.com/sebastienrousseau/bankstatementparser/commits/main).

<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type": "SoftwareApplication",
  "name": "Mai Fassarar Bayanin Banki",
  "applicationCategory": "DeveloperApplication",
  "operatingSystem": "Cross-platform",
  "softwareVersion": "0.0.8",
  "datePublished": "2026-04-11",
  "releaseNotes": "Ƙara daidaitawar fayil ɗin layi ɗaya, yawo na gaskiya don PAIN.001, inganta aikin aiki (27K+ tx/s CAMT, 52K+ tx/s PAIN.001), aji Deduplicator, nazarin ƙwaƙwalwar ajiya, amintaccen sarrafa ZIP.",
  "downloadUrl":"https://pypi.org/project/bankstatementparser/",
  "lasisi":"https://opensource.org/licenses/Apache-2.0",
  "marubuci": {
    "@type": "Mutum",
    "name": "Sebastien Rousseau"
  }
}
</script>
