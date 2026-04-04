---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "About Bank Statement Parser: Features, Formats, and Performance"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Bank Statement Parser. All rights reserved."
date: "Apr 01, 2026"
description: "Bank Statement Parser is an open-source Python library for parsing CAMT.053, PAIN.001, CSV, OFX, QFX, and MT940 into pandas DataFrames. 100% local, PII redaction, 27K+ tx/s."
download: ""
format-detection: "telephone=no"
hreflang: "en"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/about/index.html"
image_alt: "Logo of Bank Statement Parser, Empower Your Financial Analysis with Seamless Data Extraction"
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "bank statement parser python, CAMT.053 parser, PAIN.001 parser, ISO 20022 python library, MT940 parser, OFX QFX parser, open source bank parser, local financial data processing, PII redaction banking, MT940 to CAMT migration"
language: "en-GB"
layout: "about"
locale: "en_GB"
logo_alt: "Logo of Bank Statement Parser, Empower Your Financial Analysis with Seamless Data Extraction"
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "About the Bank Statement Parser"
permalink: "https://bankstatementparser.com/about/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "One Library. Six Formats. Zero Network Calls."
tags: "bank,statement,parser,finance,python,camt,pain001,csv,ofx,qfx,mt940"
theme_color: "rgb(73, 214, 251)"
title: "About Bank Statement Parser: Features, Formats, and Performance"
url: "https://bankstatementparser.com/about/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/about/rss.xml"
category: "Finance Software, Python Library, Data Processing"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Bank Statement Parser is an open-source Python library for parsing CAMT.053, PAIN.001, CSV, OFX, QFX, and MT940 into pandas DataFrames. 100% local, PII redaction, 27K+ tx/s."
item_guid: "https://bankstatementparser.com/about/rss.xml"
item_link: "https://bankstatementparser.com/about/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "About Bank Statement Parser: Features, Formats, and Performance"
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
apple-mobile-web-app-title: "About Bank Statement Parser: Features, Formats, and Performance"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Open-source Python library: parse CAMT.053, PAIN.001, CSV, OFX, QFX, MT940 into DataFrames. 100% local, PII redaction, 27K+ tx/s."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logo of Bank Statement Parser, Empower Your Financial Analysis with Seamless Data Extraction"
twitter_site: "@wwdseb"
twitter_title: "About Bank Statement Parser: 6 Formats, 27K+ tx/s, 100% Local"
twitter_url: "https://bankstatementparser.com/about/index.html"

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

**TL;DR:** Bank Statement Parser is an open-source Python library that parses six bank statement formats (CAMT.053, PAIN.001, CSV, OFX, QFX, MT940) into pandas DataFrames. 100% local processing, PII redaction by default, 27K+ tx/s throughput.

Bank Statement Parser is an open-source Python library that parses bank statements from six formats into structured pandas DataFrames. All processing happens locally -- zero network calls, deterministic output, and automatic PII redaction.

## Who Is This For?

- **Treasury teams** migrating from MT940 to CAMT.053 who need a parser that handles both old and new formats during the transition.
- **Fintech developers** building reconciliation, reporting, or accounting pipelines who want a single dependency instead of stitching together mt940 + ofxparse + custom CSV logic.
- **Compliance teams** who need PII redaction by default and audit-ready, deterministic output that never sends data to external services.
- **Anyone** who refuses to send sensitive financial data to a third-party SaaS when a local, open-source tool can do the job.

## Supported Formats

| Format | Standard | File Types | Parser Class |
|---|---|---|---|
| CAMT.053 | ISO 20022 Bank-to-Customer Statement | `.xml` | `CamtParser` |
| PAIN.001 | ISO 20022 Credit Transfer Initiation | `.xml` | `Pain001Parser` |
| CSV | Generic bank exports | `.csv` | `CsvStatementParser` |
| OFX | Open Financial Exchange | `.ofx` | `OfxParser` |
| QFX | Quicken Financial Exchange | `.qfx` | `QfxParser` |
| MT940 | SWIFT standard | `.mt940`, `.sta` | `Mt940Parser` |

All formats produce normalised pandas DataFrames with consistent column names, making downstream processing format-agnostic.

## Key Capabilities

- **Format Auto-Detection**: `detect_statement_format()` identifies the format; `create_parser()` instantiates the right parser.
- **Streaming Parsing**: Process large files (50 MB+, 50K+ transactions) with bounded memory using `parse_streaming()`.
- **Parallel Processing**: Parse multiple files concurrently with `parse_files_parallel()` using ProcessPoolExecutor.
- **Deduplication**: Detect exact duplicates and suspected matches with explainable confidence scores.
- **In-Memory Parsing**: `from_string()` and `from_bytes()` for SFTP and API workflows with no disk I/O.
- **Secure ZIP Processing**: `iter_secure_xml_entries()` with compression ratio limits, entry size caps, and encrypted entry rejection.
- **Export**: CSV, JSON, Excel (`.xlsx`), and optional Polars DataFrames.

## Security And Privacy

- **PII Redaction**: Names, IBANs, and addresses are masked by default in CLI output. Opt in with `--show-pii`.
- **XXE Protection**: XML parsing uses `resolve_entities=False`, `no_network=True`, `load_dtd=False`.
- **ZIP Bomb Protection**: Compression ratio limits (100:1 default), entry size caps (10 MB), encrypted entry rejection.
- **Path Traversal Prevention**: Dangerous pattern blocklist and symlink resolution.
- **Supply Chain Security**: SHA-256 hash-locked dependencies, CycloneDX SBOM, build provenance attestation.

## Performance

| Metric | Value |
|---|---|
| CAMT.053 throughput | 27,000+ tx/s |
| PAIN.001 throughput | 52,000+ tx/s |
| Per-transaction latency (CAMT) | 37 microseconds |
| Per-transaction latency (PAIN.001) | 19 microseconds |
| Time to first result | < 2 ms |
| Memory scaling (1K-50K tx) | Constant (streaming) |
| Test coverage | 100% branch coverage |
| Tests | 467 across 29 test files |

## Start Building

[Get started with installation and examples ❯][01]

[01]: /getting-started/index.html "Getting Started"
 "GitHub Repository"
