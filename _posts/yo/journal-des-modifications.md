---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Bank Gbólóhùn Parser Changelog"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Itumọ Gbólóhùn Bank. Gbogbo awọn ẹtọ wa ni ipamọ."
date: "Apr 11, 2026"
description: "Itan itusilẹ ati iwe iyipada fun Parser Gbólóhùn Bank. Tọpinpin awọn ẹya tuntun, awọn ilọsiwaju, ati awọn atunṣe kokoro kọja gbogbo awọn ẹya."
download: ""
format-detection: "telephone=no"
hreflang: "yo"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/yo/journal-des-modifications/index.html"
image_alt: "Logo ti Itumọ Gbólóhùn Banki, Fi agbara fun Itupalẹ Iṣowo Rẹ pẹlu Iyọkuro Data Ailopin"
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "alaye atunto banki iyipada, awọn akọsilẹ itusilẹ, itan ẹya, awọn imudojuiwọn"
language: "yo-NG"
layout: "about"
locale: "yo_NG"
logo_alt: "Logo ti Itumọ Gbólóhùn Banki, Fi agbara fun Itupalẹ Iṣowo Rẹ pẹlu Iyọkuro Data Ailopin"
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Changelog"
permalink: "https://bankstatementparser.com/yo/journal-des-modifications/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Itan itusilẹ ati Kini Tuntun"
tags: "changelog, awọn idasilẹ, awọn imudojuiwọn, awọn ẹya, awọn ikede, bulọọgi"
theme_color: "rgb(73, 214, 251)"
title: "Bank Gbólóhùn Parser Changelog"
url: "https://bankstatementparser.com/yo/journal-des-modifications/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/yo/journal-des-modifications/rss.xml"
category: "Owo Software, Python Library, Data Processing"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Itan itusilẹ ati iwe iyipada fun Parser Gbólóhùn Bank. Tọpinpin awọn ẹya tuntun, awọn ilọsiwaju, ati awọn atunṣe kokoro kọja gbogbo awọn ẹya."
item_guid: "https://bankstatementparser.com/yo/journal-des-modifications/rss.xml"
item_link: "https://bankstatementparser.com/yo/journal-des-modifications/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Bank Gbólóhùn Parser Changelog"
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
apple-mobile-web-app-title: "Bank Gbólóhùn Parser Changelog"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Itan itusilẹ ati iwe iyipada fun Parser Gbólóhùn Bank. Tọpinpin awọn ẹya tuntun, awọn ilọsiwaju, ati awọn atunṣe kokoro kọja gbogbo awọn ẹya."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logo ti Itumọ Gbólóhùn Banki, Fi agbara fun Itupalẹ Iṣowo Rẹ pẹlu Iyọkuro Data Ailopin"
twitter_site: "@wwdseb"
twitter_title: "Bank Gbólóhùn Parser Changelog"
twitter_url: "https://bankstatementparser.com/yo/journal-des-modifications/index.html"

# Humans.txt - The Humans.txt front matter (YAML).

author_website: "https://bankstatementparser.com"
author_twitter: "@wwdseb"
author_location: "London, UK"
thanks: "O ṣeun fun kika!"
site_last_updated: "2026-04-01"
site_standards: "HTML5, CSS3, RSS, Atom, JSON, XML, YAML, Markdown, TOML"
site_components: "Shokunin SSG, Shokunin CLI, Shokunin Templates, Shokunin Themes, Kaishi SSG, Kaishi CLI, Kaishi Templates, Kaishi Themes"
site_software: "Shokunin, Rust"

---

Tẹle idagbasoke Parser Gbólóhùn Gbólóhùn Bank. Alabapin nipasẹ [RSS] (/changelog/rss.xml) tabi wo [ibi ipamọ GitHub](https://github.com/sebastienrousseau/bankstatementparser) fun awọn iwifunni idasilẹ.

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

## v0.0.4 - 2026-03-15 (Titun)

- Ṣafikun faili afiwera pẹlu`parse_files_parallel()`lilo ProcessPoolExecutor.
Fikun ṣiṣan otitọ fun awọn faili PAIN.001 nla (50 MB+) pẹlu iranti didi.
- Awọn iṣapeye iṣẹ: Iwọn CAMT kọja 27,000 tx/s, PAIN.001 kọja 52,000 tx/s.
- Fi kun`Deduplicator`kilasi fun wiwa awọn ẹda-ẹda deede ati awọn ifura ti a fura si pẹlu awọn ikun igbekele.
- Fi kun`from_string()`ati`from_bytes()`awọn ọna fun ni-iranti parsing lai disk I/O.
- Fi kun`iter_secure_xml_entries()`fun ni aabo ZIP pamosi sisẹ.
- CI ti o gbooro sii pẹlu imuṣiṣẹ ala iṣẹ.

## v0.0.3 - 2025-11-20

- Ṣafikun CSV, OFX, QFX, ati atilẹyin parser MT940.
- Fikun kika laifọwọyi erin pẹlu`detect_statement_format()`ati`create_parser()`.
- Atunṣe PII ti a ṣafikun (ni aiyipada ni CLI ati ipo ṣiṣanwọle).
- Awọn oluranlọwọ okeere ti a ṣafikun fun CSV, JSON, ati Excel.
- Ṣe afikun atilẹyin Polars DataFrame iyan.
- Suite idanwo gbooro si awọn idanwo 718 pẹlu agbegbe agbegbe 100%.

## v0.0.2 - 2025-06-10

-Afikun PAIN.001 parser (`Pain001Parser`) fun ISO 20022 awọn faili ibẹrẹ gbigbe kirẹditi.
Ni wiwo CLI ti a ṣafikun (`python -m bankstatementparser.cli`).
- Fi kun ipo sisanwọle pẹlu`parse_streaming()`.
- Fikun afọwọsi igbewọle ati awọn opin iwọn faili.

## v0.0.1 - 2025-01-15

- Itusilẹ akọkọ.
- CAMT.053 atọka (`CamtParser`) fun ISO 20022 awọn alaye banki-si-onibara.
- pandas DataFrame o wu.
- Ipilẹ aabo XML líle (Aabo XXE, no_nẹtiwọọki).

Wo itan ifaramo ni kikun lori [GitHub](https://github.com/sebastienrousseau/bankstatementparser/commits/main).

<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type": "SoftwareApplication",
  "name": "Aṣayẹwo Gbólóhùn Banki",
  "applicationCategory": "Ohun elo Olùgbéejáde",
  "operatingSystem": "Cross-platform",
  "softwareVersion": "0.0.8",
  "datePublished": "2026-04-11",
  "releaseNotes": "Fikun-itupalẹ faili ti o jọra, ṣiṣanwọle otitọ fun PAIN.001, awọn iṣapeye iṣẹ ṣiṣe (27K+ tx/s CAMT, 52K+ tx/s PAIN.001), Kilasi Deduplicator, ṣiṣayẹwo inu-iranti, sisẹ ZIP to ni aabo.",
  "downloadUrl":"https://pypi.org/project/bankstatementparser/",
  "iwe-aṣẹ":"https://opensource.org/licenses/Apache-2.0",
  "Okọwe": {
    "@type": "Ènìyàn",
    "orukọ": "Sebastien Rousseau"
  }
}
</script>
