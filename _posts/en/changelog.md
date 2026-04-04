---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Bank Statement Parser Changelog"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/corporate-finance.webp"
cdn: "https://cloudcdn.pro"
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Bank Statement Parser. All rights reserved."
date: "Apr 01, 2026"
description: "Release history and changelog for Bank Statement Parser. Track new features, improvements, and bug fixes across all versions."
download: ""
format-detection: "telephone=no"
hreflang: "en"
icon: "https://cloudcdn.pro/bankstatementparser/images/favicon.ico"
id: "https://bankstatementparser.com/changelog/index.html"
image_alt: "Logo of Bank Statement Parser, Empower Your Financial Analysis with Seamless Data Extraction"
image_height: "630"
image_width: "1200"
image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
keywords: "bank statement parser changelog, release notes, version history, updates"
language: "en-GB"
layout: "about"
locale: "en_GB"
logo_alt: "Logo of Bank Statement Parser, Empower Your Financial Analysis with Seamless Data Extraction"
logo_height: "44"
logo_width: "44"
logo: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Changelog"
permalink: "https://bankstatementparser.com/changelog/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Release History and What's New"
tags: "changelog,releases,updates,versions,announcements,blog"
theme_color: "rgb(73, 214, 251)"
title: "Bank Statement Parser Changelog"
url: "https://bankstatementparser.com/changelog/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/changelog/rss.xml"
category: "Finance Software, Python Library, Data Processing"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Release history and changelog for Bank Statement Parser. Track new features, improvements, and bug fixes across all versions."
item_guid: "https://bankstatementparser.com/changelog/rss.xml"
item_link: "https://bankstatementparser.com/changelog/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Bank Statement Parser Changelog"
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
apple-mobile-web-app-title: "Bank Statement Parser Changelog"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Release history and changelog for Bank Statement Parser. Track new features, improvements, and bug fixes across all versions."
twitter_image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logo of Bank Statement Parser, Empower Your Financial Analysis with Seamless Data Extraction"
twitter_site: "@wwdseb"
twitter_title: "Bank Statement Parser Changelog"
twitter_url: "https://bankstatementparser.com/changelog/index.html"

# Humans.txt - The Humans.txt front matter (YAML).

author_website: "https://bankstatementparser.com"
author_twitter: "@wwdseb"
author_location: "London, UK"
thanks: "Thanks for reading!"
site_last_updated: "2026-04-01"
site_standards: "HTML5, CSS3, RSS, Atom, JSON, XML, YAML, Markdown, TOML"
site_components: "Shokunin SSG, Shokunin CLI, Shokunin Templates, Shokunin Themes, Kaishi SSG, Kaishi CLI, Kaishi Templates, Kaishi Themes"
site_software: "Shokunin, Rust"

---

Follow Bank Statement Parser development. Subscribe via [RSS](/changelog/rss.xml) or watch the [GitHub repository](https://github.com/sebastienrousseau/bankstatementparser) for release notifications.

## v0.0.4 — 2026-03-15 (Latest)

- Added parallel file parsing with `parse_files_parallel()` using ProcessPoolExecutor.
- Added true streaming for large PAIN.001 files (50 MB+) with bounded memory.
- Performance optimisations: CAMT throughput now exceeds 27,000 tx/s, PAIN.001 exceeds 52,000 tx/s.
- Added `Deduplicator` class for detecting exact duplicates and suspected matches with confidence scores.
- Added `from_string()` and `from_bytes()` methods for in-memory parsing without disk I/O.
- Added `iter_secure_xml_entries()` for secure ZIP archive processing.
- Extended CI with performance threshold enforcement.

## v0.0.3 — 2025-11-20

- Added CSV, OFX, QFX, and MT940 parser support.
- Added format auto-detection with `detect_statement_format()` and `create_parser()`.
- Added PII redaction (on by default in CLI and streaming mode).
- Added export helpers for CSV, JSON, and Excel.
- Added optional Polars DataFrame support.
- Expanded test suite to 467 tests with 100% branch coverage.

## v0.0.2 — 2025-06-10

- Added PAIN.001 parser (`Pain001Parser`) for ISO 20022 credit transfer initiation files.
- Added CLI interface (`python -m bankstatementparser.cli`).
- Added streaming mode with `parse_streaming()`.
- Added input validation and file size limits.

## v0.0.1 — 2025-01-15

- Initial release.
- CAMT.053 parser (`CamtParser`) for ISO 20022 bank-to-customer statements.
- pandas DataFrame output.
- Basic XML security hardening (XXE protection, no_network).

View the full commit history on [GitHub](https://github.com/sebastienrousseau/bankstatementparser/commits/main).

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "Bank Statement Parser",
  "applicationCategory": "DeveloperApplication",
  "operatingSystem": "Cross-platform",
  "softwareVersion": "0.0.4",
  "datePublished": "2026-03-15",
  "releaseNotes": "Added parallel file parsing, true streaming for PAIN.001, performance optimisations (27K+ tx/s CAMT, 52K+ tx/s PAIN.001), Deduplicator class, in-memory parsing, secure ZIP processing.",
  "downloadUrl": "https://pypi.org/project/bankstatementparser/",
  "license": "https://opensource.org/licenses/Apache-2.0",
  "author": {
    "@type": "Person",
    "name": "Sebastien Rousseau"
  }
}
</script>
