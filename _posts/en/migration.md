---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "ISO 20022 Migration Guide"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Bank Statement Parser. All rights reserved."
date: "Apr 11, 2026"
description: "A practical guide to the SWIFT ISO 20022 migration timeline (2026-2028), MT940 to CAMT.053 transition, and how Bank Statement Parser helps treasury teams migrate."
download: ""
format-detection: "telephone=no"
hreflang: "en"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/migration/index.html"
image_alt: "Logo of Bank Statement Parser, Empower Your Financial Analysis with Seamless Data Extraction"
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "ISO 20022 migration, MT940 to CAMT.053, SWIFT deadline 2027, MT940 retirement 2028, bank statement migration python, CAMT.053 parser, ISO 20022 timeline"
language: "en-GB"
layout: "about"
locale: "en_GB"
logo_alt: "Logo of Bank Statement Parser, Empower Your Financial Analysis with Seamless Data Extraction"
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "ISO 20022 Migration Guide"
permalink: "https://bankstatementparser.com/migration/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Navigate the SWIFT MT to ISO 20022 Transition"
tags: "iso20022,migration,mt940,camt053,swift,timeline"
theme_color: "rgb(73, 214, 251)"
title: "ISO 20022 Migration Guide: MT940 to CAMT.053 Transition"
url: "https://bankstatementparser.com/migration/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/migration/rss.xml"
category: "Finance Software, Python Library, Data Processing"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "A practical guide to the SWIFT ISO 20022 migration timeline (2026-2028), MT940 to CAMT.053 transition, and how Bank Statement Parser helps treasury teams migrate."
item_guid: "https://bankstatementparser.com/migration/rss.xml"
item_link: "https://bankstatementparser.com/migration/rss.xml"
item_pub_date: "2026-04-11T00:00:00+00:00"
item_title: "ISO 20022 Migration Guide: MT940 to CAMT.053 Transition"
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
apple-mobile-web-app-title: "ISO 20022 Migration Guide: MT940 to CAMT.053 Transition"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "A practical guide to the SWIFT ISO 20022 migration timeline (2026-2028), MT940 to CAMT.053 transition, and how Bank Statement Parser helps treasury teams migrate."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logo of Bank Statement Parser, Empower Your Financial Analysis with Seamless Data Extraction"
twitter_site: "@wwdseb"
twitter_title: "ISO 20022 Migration Guide: MT940 to CAMT.053 Transition"
twitter_url: "https://bankstatementparser.com/migration/index.html"

# Humans.txt - The Humans.txt front matter (YAML).

author_website: "https://bankstatementparser.com"
author_twitter: "@wwdseb"
author_location: "London, UK"
thanks: "Thanks for reading!"
site_last_updated: "2026-04-11"
site_standards: "HTML5, CSS3, RSS, Atom, JSON, XML, YAML, Markdown, TOML"
site_components: "Shokunin SSG, Shokunin CLI, Shokunin Templates, Shokunin Themes, Kaishi SSG, Kaishi CLI, Kaishi Templates, Kaishi Themes"
site_software: "Shokunin, Rust"

---

**TL;DR:** SWIFT will retire MT940 by November 2028. Bank Statement Parser handles both MT940 and CAMT.053 with a single API, so your parsing pipeline works during the transition and after.

## Why This Migration Matters

SWIFT is retiring legacy MT message formats in favour of the richer ISO 20022 standard. For treasury and finance teams, this means your bank statement processing pipelines must evolve from MT940 to CAMT.053 before the hard deadlines.

## SWIFT Migration Timeline

| Date | Milestone | Impact |
|---|---|---|
| **November 2025** | MT-to-MX coexistence ended for cross-border payments | PACS messages are now ISO 20022 only |
| **November 2026** | Structured/hybrid addresses mandatory; MT101 multi-instruction rejected; Case Management Phase 1 | Address formats must comply; some MT messages will be rejected |
| **Late 2026** | Opt-in begins for receiving CAMT.052/.053/.054 | Financial institutions can start receiving native ISO statements |
| **November 2027** | All FIs must receive CAMT.053 natively | SWIFT stops converting MT format to ISO; your systems must parse CAMT directly |
| **November 2028** | MT940/MT942/MT950/MT900/MT910 fully retired | Legacy statement formats no longer available; CAMT.052/.053/.054 are the only option |

## What Changes for Your Code

### Before: MT940 Only

```python
from bankstatementparser import Mt940Parser

parser = Mt940Parser("statement.mt940")
df = parser.parse()
```

### After: Both Formats with Auto-Detection

```python
from bankstatementparser import create_parser, detect_statement_format

fmt = detect_statement_format("statement.xml")  # or .mt940
parser = create_parser("statement.xml", fmt)
df = parser.parse()  # Same DataFrame schema regardless of format
```

The `detect_statement_format()` function identifies whether the file is MT940, CAMT.053, PAIN.001, or any other supported format. The `create_parser()` function returns the correct parser. Your downstream code works identically regardless of the source format.

## CAMT.053 vs MT940: Key Differences

| Feature | MT940 | CAMT.053 |
|---|---|---|
| Data richness | Limited fields | 3-5x more data per transaction |
| Character set | Limited (SWIFT charset) | Full Unicode |
| Structure | Flat text with tags | XML with namespaces |
| Balance reporting | Opening/closing only | Multiple balance types |
| References | Single reference field | Multiple reference types |
| Currency handling | Basic | Full multi-currency with exchange rates |

## How Bank Statement Parser Helps

- **Unified API**: Parse MT940, CAMT.053, and PDF statements with the same workflow, producing consistent DataFrame output.
- **Auto-detection**: No need to know the format in advance. `detect_statement_format()` identifies it automatically.
- **Hybrid PDF pipeline**: Banks that provide PDF-only statements during the transition are handled by `smart_ingest()` with automatic balance verification.
- **Namespace-agnostic**: Handles any CAMT.053 variant (001.02, 001.04, or bank-specific wrappers) without configuration.
- **Multi-currency verification**: `verify_balance_multi_currency()` runs the Golden Rule per currency group — essential for multi-currency CAMT statements.
- **Streaming**: Process large CAMT files (50 MB+, 50K+ transactions) with bounded memory.
- **Ledger export**: Export directly to hledger or beancount journal format for treasury accounting.
- **Migration testing**: Run both parsers side-by-side on the same date range to verify output consistency before switching.

## Getting Started

```bash
pip install bankstatementparser
```

```python
from bankstatementparser import create_parser, detect_statement_format

# Works with MT940 today, CAMT.053 tomorrow, PDF anytime
for file in bank_statement_files:
    fmt = detect_statement_format(file)
    parser = create_parser(file, fmt)
    df = parser.parse()
    process(df)  # Your code doesn't change
```

For PDF statements from banks that don't yet offer structured CAMT exports:

```python
from bankstatementparser.hybrid import smart_ingest

result = smart_ingest("statement.pdf")
assert result.verification.status == "VERIFIED"
```

[Read the full documentation](/getting-started/index.html)

[Compare with alternatives ❯](/comparison/index.html) | [See real-world use cases ❯](/use-cases/index.html)
