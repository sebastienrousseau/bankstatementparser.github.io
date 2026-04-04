---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Bank Statement Parser Security"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/corporate-finance.webp"
cdn: "https://cloudcdn.pro"
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Bank Statement Parser. All rights reserved."
date: "Apr 01, 2026"
description: "Security features of Bank Statement Parser: XXE protection, ZIP bomb hardening, PII redaction, supply chain security, deterministic output, and signed builds."
download: ""
format-detection: "telephone=no"
hreflang: "en"
icon: "https://cloudcdn.pro/bankstatementparser/images/favicon.ico"
id: "https://bankstatementparser.com/security/index.html"
image_alt: "Logo of Bank Statement Parser, Empower Your Financial Analysis with Seamless Data Extraction"
image_height: "630"
image_width: "1200"
image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
keywords: "bank statement security, PII redaction python, XXE protection, ZIP bomb protection, supply chain security SBOM, deterministic parsing, financial data security"
language: "en-GB"
layout: "about"
locale: "en_GB"
logo_alt: "Logo of Bank Statement Parser, Empower Your Financial Analysis with Seamless Data Extraction"
logo_height: "44"
logo_width: "44"
logo: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Security"
permalink: "https://bankstatementparser.com/security/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "How We Protect Your Financial Data"
tags: "security,pii,xxe,sbom,supply-chain,deterministic"
theme_color: "rgb(73, 214, 251)"
title: "Bank Statement Parser Security: Data Protection and Supply Chain"
url: "https://bankstatementparser.com/security/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/security/rss.xml"
category: "Finance Software, Python Library, Data Processing"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Security features of Bank Statement Parser: XXE protection, ZIP bomb hardening, PII redaction, supply chain security, deterministic output, and signed builds."
item_guid: "https://bankstatementparser.com/security/rss.xml"
item_link: "https://bankstatementparser.com/security/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Bank Statement Parser Security: Data Protection and Supply Chain"
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
apple-mobile-web-app-title: "Bank Statement Parser Security: Data Protection and Supply Chain"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Security features of Bank Statement Parser: XXE protection, ZIP bomb hardening, PII redaction, supply chain security, deterministic output, and signed builds."
twitter_image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logo of Bank Statement Parser, Empower Your Financial Analysis with Seamless Data Extraction"
twitter_site: "@wwdseb"
twitter_title: "Bank Statement Parser Security: Data Protection and Supply Chain"
twitter_url: "https://bankstatementparser.com/security/index.html"

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

**TL;DR:** Bank Statement Parser makes zero network calls, redacts PII by default, hardens XML parsing against XXE attacks, and ships with SHA-256 hash-locked dependencies and a CycloneDX SBOM.

## Security by Design

Bank Statement Parser is built for processing sensitive financial data. Every design decision prioritises security, privacy, and auditability.

## Zero Network Access

All processing happens locally within your runtime. The library makes zero API calls, zero cloud connections, and collects zero telemetry. XML parsers are explicitly configured with `no_network=True`, `resolve_entities=False`, and `load_dtd=False` to prevent any outbound access.

## PII Redaction

Personally identifiable information (names, IBANs, postal addresses) is automatically redacted in CLI output and streaming mode. This is on by default.

- **CLI**: Sensitive fields show as `***REDACTED***`
- **Streaming**: `parse_streaming(redact_pii=True)` (default)
- **Exports**: CSV/JSON/Excel retain full data for downstream processing
- **Opt-in**: Use `--show-pii` or `redact_pii=False` when you need unredacted output

## XML Security (XXE Protection)

All XML parsing uses `lxml` with hardened settings:

- `resolve_entities=False` -- prevents XML entity expansion attacks
- `no_network=True` -- blocks all outbound network access from the parser
- `load_dtd=False` -- prevents DTD-based attacks
- Namespace stripping before processing -- handles any CAMT.053 variant safely

## ZIP Archive Security

`iter_secure_xml_entries()` validates every ZIP member before extraction:

- **Entry size cap**: 10 MB per entry (configurable)
- **Total size cap**: 50 MB total uncompressed (configurable)
- **Compression ratio limit**: 100:1 default -- detects ZIP bombs
- **Encrypted entry rejection**: Encrypted entries are skipped with a warning
- **No disk writes**: XML bytes pass directly to the parser via `from_bytes()`

## Path Traversal Prevention

Input validation blocks dangerous file paths:

- Null bytes, directory traversal patterns (`../`), and symlinks are rejected
- File extension validation against expected formats
- File size limits (100 MB default, configurable)

## Deterministic Output

Given the same input file, the parser produces byte-identical output every run. No randomness, no model inference, no heuristic sampling. This is critical for:

- **Audit reproducibility**: Run the same file twice and diff the output
- **Regulatory compliance**: Demonstrate consistent processing
- **CI verification**: 467 tests enforce determinism with 100% branch coverage

## Supply Chain Security

- **SHA-256 hash-locked dependencies**: Every package in `poetry.lock` has verified file hashes
- **CycloneDX SBOM**: Every release includes a Software Bill of Materials
- **GitHub build provenance**: Attestation links each artifact to its source commit
- **Signed commits**: All commits are SSH-signed and verified in CI
- **Dependency verification**: `scripts/verify_locked_hashes.py` validates all hashes locally

## Verify Locally

```bash
python -m pytest                          # 467 tests, 100% branch coverage
python scripts/verify_locked_hashes.py    # SHA-256 hash verification
git log --show-signature -1               # Verify commit signature
```
