---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Architectural photography of glass building"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/christian-ladewig-T0iFfJw-rB0.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: "bankstatementparser.com"
copyright: "© 2023-2026 Bank Statement Parser. All rights reserved."
date: "Apr 11, 2026"
description: "Open-source Python library to parse CAMT.053, PAIN.001, CSV, OFX, QFX, MT940, and PDF bank statements into pandas DataFrames. 27K+ tx/s, hybrid PDF pipeline, REST API, 100% local."
download_url: "https://pypi.org/project/bankstatementparser/"
download_title: "pip install bankstatementparser"
format-detection: "telephone=no"
hero_description: "Parse CAMT.053, PAIN.001, CSV, OFX, QFX, MT940, and PDF into pandas DataFrames. 27K+ tx/s, hybrid PDF pipeline, REST API, zero network calls."
hreflang: "en"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com"
image_alt: "Logo of Bank Statement Parser, a powerful Python tool designed for quick, accurate financial data processing and insights extraction."
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "bank statement parser, ISO 20022 parser python, CAMT.053 python, PAIN.001 parser, MT940 to CAMT migration, parse bank statements locally, OFX QFX parser, PDF bank statement parser, hybrid LLM extraction, REST API bank parser"
language: "en-GB"
layout: "index"
locale: "en_GB"
logo_alt: "Logo of Bank Statement Parser, a powerful Python tool designed for quick, accurate financial data processing and insights extraction."
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Bank Statement Parser"
permalink: "https://bankstatementparser.com"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Parse 7 Bank Statement Formats in Python — Including PDF. No SaaS. No Data Leaves Your Machine."
tags: "banking,finance,python,camt,pain001,csv,ofx,qfx,mt940,pdf,automation"
theme_color: "rgb(73, 214, 251)"
title: "Bank Statement Parser: Parse 7 Formats in Python, 100% Local"
url: "https://bankstatementparser.com"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/rss.xml"
category: "Financial Software, Data Analysis Tools, Banking Solutions, Financial Python Library, Treasury Management Systems"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Open-source Python library to parse CAMT.053, PAIN.001, CSV, OFX, QFX, MT940, and PDF bank statements into pandas DataFrames. 27K+ tx/s, hybrid PDF pipeline, REST API, 100% local."
item_guid: "https://bankstatementparser.com/rss.xml"
item_link: "https://bankstatementparser.com/rss.xml"
item_pub_date: "2026-04-11T00:00:00+00:00"
item_title: "Bank Statement Parser — RSS Feed"
last_build_date: "2026-04-11T00:00:00+00:00"
managing_editor: "contact@bankstatementparser.com"
pub_date: "2026-04-11T00:00:00+00:00"
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
apple-mobile-web-app-title: "Bank Statement Parser: Parse 7 Formats Including PDF, 100% Local"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Open-source Python library to parse CAMT.053, PAIN.001, CSV, OFX, QFX, MT940, and PDF bank statements. 27K+ tx/s, hybrid PDF pipeline, REST API."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logo of Bank Statement Parser, a powerful Python tool designed for quick, accurate financial data processing and insights extraction."
twitter_site: "@wwdseb"
twitter_title: "Bank Statement Parser: Parse 7 Formats in Python, 100% Local"
twitter_url: "https://bankstatementparser.com/"

# Humans.txt - The Humans.txt front matter (YAML).

author_website: "https://bankstatementparser.com"
author_twitter: "@wwdseb"
author_location: "London, UK"
thanks: "Thanks for reading!"
site_last_updated: "2026-04-11"
site_standards: "HTML5, CSS3, RSS, Atom, JSON, XML, YAML, Markdown, TOML"
site_components: "Shokunin SSG, Shokunin CLI, Shokunin Templates, Kaishi Templates, Kaishi Themes"
site_software: "Shokunin, Rust"

---

**Bank Statement Parser** is an open-source Python library that parses bank statements from seven formats (CAMT.053, PAIN.001, CSV, OFX, QFX, MT940, and PDF) into structured pandas DataFrames. All processing runs locally — deterministic output, automatic PII redaction, and an optional hybrid PDF pipeline that routes through local LLMs when needed.

## Get Started in Seconds

```bash
pip install bankstatementparser
```

```python
from bankstatementparser import create_parser, detect_statement_format

fmt = detect_statement_format("statement.xml")
parser = create_parser("statement.xml", fmt)
df = parser.parse()  # pandas DataFrame, ready to use
```

```python
# Parse PDFs with the hybrid pipeline (v0.0.5+)
from bankstatementparser.hybrid import smart_ingest

result = smart_ingest("statement.pdf")
print(result.source_method)         # "deterministic" | "llm" | "vision"
print(result.verification.status)   # VERIFIED | DISCREPANCY | FAILED
```

<img src="https://img.shields.io/github/stars/sebastienrousseau/bankstatementparser?style=for-the-badge&label=Stars" height="28" alt="GitHub Stars" loading="lazy" style="margin:0 .25rem .5rem 0" />
<img src="https://img.shields.io/pypi/dm/bankstatementparser?style=for-the-badge&label=Downloads" height="28" alt="Monthly Downloads" loading="lazy" style="margin:0 .25rem .5rem 0" />
<img src="https://img.shields.io/pypi/v/bankstatementparser?style=for-the-badge&label=PyPI" height="28" width="119" alt="PyPI Version" loading="lazy" style="margin:0 .25rem .5rem 0" />
<img src="https://img.shields.io/pypi/pyversions/bankstatementparser?style=for-the-badge&label=Python" height="28" width="347" alt="Python" loading="lazy" style="margin:0 .25rem .5rem 0" />
<img src="https://img.shields.io/pypi/l/bankstatementparser?style=for-the-badge&label=License" height="28" width="292" alt="License" loading="lazy" style="margin:0 .25rem .5rem 0" />
<img src="https://img.shields.io/badge/tests-718%20passed-brightgreen?style=for-the-badge" height="28" width="168" alt="Tests" loading="lazy" style="margin:0 .25rem .5rem 0" />
<img src="https://img.shields.io/badge/coverage-100%25-brightgreen?style=for-the-badge" height="28" width="152" alt="Coverage" loading="lazy" style="margin:0 .25rem .5rem 0" />

## One Library, Seven Formats

Parse CAMT.053, PAIN.001, CSV, OFX, QFX, MT940, and PDF into structured pandas DataFrames with a single, unified API. No need to install separate packages for each format.

| Feature | Bank Statement Parser | Single-format OSS (mt940, ofxparse) | SaaS (Ocrolus, Parseur) |
|---|---|---|---|
| Formats supported | 7, unified API | 1 each | Many (via OCR) |
| PDF support | Hybrid pipeline (deterministic + LLM + vision) | No | Yes (cloud OCR) |
| Data privacy | 100% local (LLMs run locally via Ollama) | 100% local | Data sent externally |
| Cost | Free, Apache 2.0 | Free | $49-$1,000+/mo |
| Balance verification | Golden Rule (opening + credits − debits = closing) | No | Varies |
| PII redaction | Built-in, on by default | No | Varies |
| Streaming | Bounded memory | No | N/A |
| REST API | Built-in FastAPI microservice | No | Yes |
| Deduplication | Idempotent transaction hashes | No | Some |
| Ledger export | hledger + beancount | No | No |

## Hybrid PDF Pipeline

Bank Statement Parser v0.0.5+ includes a three-path hybrid pipeline for PDF bank statements:

- **Path A (Deterministic)**: Structured PDF tables parsed directly — free, fastest, no LLM needed.
- **Path B (Text-LLM)**: Digital PDFs with complex layouts extracted via local LLM (LiteLLM/Ollama).
- **Path C (Vision-LLM)**: Scanned or photocopied statements processed with multimodal vision models.

Every extraction is verified with the **Golden Rule**: `opening balance + credits − debits == closing balance`.

## Built for the ISO 20022 Migration

SWIFT has set firm deadlines: all financial institutions must receive CAMT.053 by November 2027, and MT940/MT942/MT950 will be fully retired by November 2028. Bank Statement Parser handles both legacy MT940 and modern ISO 20022 formats (CAMT.053, PAIN.001) in a single API, so your parsing pipeline works during the transition and beyond.

## Performance

- **27,000+ transactions/second** for CAMT.053 parsing
- **52,000+ transactions/second** for PAIN.001 parsing
- **< 2 ms** time to first result
- **Constant memory** from 1K to 50K+ transactions via streaming
- **718 tests** with 100% branch coverage across Python 3.10 to 3.14

## Why Bank Statement Parser?

- **Hybrid PDF Extraction**: `smart_ingest()` handles digital and scanned PDFs with automatic routing and balance verification.
- **Format Auto-Detection**: `detect_statement_format()` identifies files automatically and `create_parser()` returns the right parser.
- **Privacy First**: PII redaction is on by default. LLMs run locally via Ollama — no data leaves your machine.
- **REST API**: Deploy as a FastAPI microservice with `/ingest` and `/health` endpoints.
- **Enrichment**: LLM-powered transaction categorisation with pluggable schemas (Plaid 13-category default).
- **Ledger Export**: Export to hledger and beancount journal formats for plaintext-accounting workflows.
- **Bulk Scanning**: `scan_and_ingest()` processes folder trees with automatic cross-file deduplication.
- **Multi-Currency**: `verify_balance_multi_currency()` runs Golden Rule verification per currency group.
- **Production Ready**: Secure ZIP ingestion, input validation, path traversal prevention, and interactive review mode.
- **Flexible Output**: Export to CSV, JSON, Excel, Polars, hledger, or beancount.
- **Parallel Processing**: Parse multiple files concurrently with `parse_files_parallel()`.


## Built for Production

Bank Statement Parser is designed for treasury teams, fintech developers, and compliance officers processing sensitive financial data. The library is used in MT940-to-CAMT migration pipelines, automated reconciliation systems, PDF statement ingestion, and regulatory audit workflows across financial institutions.

- **718 tests** with 100% branch coverage across Python 3.10 to 3.14
- **SHA-256 hash-locked dependencies** with CycloneDX SBOM for every release
- **Deterministic output** — identical input produces byte-identical results, every run
- **Apache 2.0 licensed** — use freely in commercial and internal systems

**Evaluating alternatives?** [See how Bank Statement Parser compares ❯](/comparison/index.html) | [Explore real-world use cases ❯](/use-cases/index.html)

[Get started ❯][01] | [View on GitHub ❯][02] | [View on PyPI ❯][03]

[01]: /getting-started/index.html
[02]: https://github.com/sebastienrousseau/bankstatementparser
[03]: https://pypi.org/project/bankstatementparser/
