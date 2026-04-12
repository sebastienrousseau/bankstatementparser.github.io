---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Seguridad ng Parser ng Bank Statement"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Bank Statement Parser. Lahat ng karapatan ay nakalaan."
date: "Apr 11, 2026"
description: "Mga feature ng seguridad ng Bank Statement Parser: Proteksyon ng XXE, ZIP bomb hardening, PII redaction, supply chain security, deterministic na output, at signed build."
download: ""
format-detection: "telephone=no"
hreflang: "tl"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/tl/securite/index.html"
image_alt: "Logo ng Bank Statement Parser, Bigyan ang Iyong Pagsusuri sa Pananalapi gamit ang Seamless Data Extraction"
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "seguridad sa bank statement, PII redaction python, XXE protection, ZIP bomb protection, supply chain security SBOM, deterministic parsing, financial data security"
language: "tl-PH"
layout: "about"
locale: "tl_PH"
logo_alt: "Logo ng Bank Statement Parser, Bigyan ang Iyong Pagsusuri sa Pananalapi gamit ang Seamless Data Extraction"
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Seguridad"
permalink: "https://bankstatementparser.com/tl/securite/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Paano Namin Pinoprotektahan ang Iyong Financial Data"
tags: "seguridad,pii,xxe,sbom,supply-chain,deterministic"
theme_color: "rgb(73, 214, 251)"
title: "Bank Statement Parser Security: Proteksyon ng Data at Supply Chain"
url: "https://bankstatementparser.com/tl/securite/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/tl/securite/rss.xml"
category: "Software sa Pananalapi, Python Library, Pagproseso ng Data"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Mga feature ng seguridad ng Bank Statement Parser: Proteksyon ng XXE, ZIP bomb hardening, PII redaction, supply chain security, deterministic na output, at signed build."
item_guid: "https://bankstatementparser.com/tl/securite/rss.xml"
item_link: "https://bankstatementparser.com/tl/securite/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Bank Statement Parser Security: Proteksyon ng Data at Supply Chain"
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
apple-mobile-web-app-title: "Bank Statement Parser Security: Proteksyon ng Data at Supply Chain"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Mga feature ng seguridad ng Bank Statement Parser: Proteksyon ng XXE, ZIP bomb hardening, PII redaction, supply chain security, deterministic na output, at signed build."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logo ng Bank Statement Parser, Bigyan ang Iyong Pagsusuri sa Pananalapi gamit ang Seamless Data Extraction"
twitter_site: "@wwdseb"
twitter_title: "Bank Statement Parser Security: Proteksyon ng Data at Supply Chain"
twitter_url: "https://bankstatementparser.com/tl/securite/index.html"

# Humans.txt - The Humans.txt front matter (YAML).

author_website: "https://bankstatementparser.com"
author_twitter: "@wwdseb"
author_location: "London, UK"
thanks: "Salamat sa pagbabasa!"
site_last_updated: "2026-04-01"
site_standards: "HTML5, CSS3, RSS, Atom, JSON, XML, YAML, Markdown, TOML"
site_components: "Shokunin SSG, Shokunin CLI, Shokunin Templates, Shokunin Themes, Kaishi SSG, Kaishi CLI, Kaishi Templates, Kaishi Themes"
site_software: "Shokunin, Rust"

---

**TL;DR:** Pinoproseso ng Bank Statement Parser ang lahat ng data nang lokal, rine-redact ang PII bilang default, pinatitigas ang XML parsing laban sa mga XXE attack, pinapatakbo ang mga LLM nang lokal sa pamamagitan ng Ollama, at kasama ang SHA-256 hash-locked dependencies at CycloneDX SBOM.

## Seguridad ayon sa Disenyo

Ang Bank Statement Parser ay binuo para sa pagproseso ng sensitibong data sa pananalapi. Ang bawat desisyon sa disenyo ay inuuna ang seguridad, privacy, at auditability.

## Zero Cloud Dependency

Lahat ng pagproseso ay nangyayari nang lokal sa loob ng iyong runtime. Ang mga deterministikong parser ay gumagawa ng zero na tawag sa network. Ang hybrid PDF pipeline ay gumagamit ng Ollama para sa lokal na LLM inference — walang data na ipinapadala sa mga cloud API. Ang mga XML parser ay tahasang naka-configure gamit ang `no_network=True`, `resolve_entities=False`, at `load_dtd=False` upang maiwasan ang anumang papalabas na access.

## PII Redaction

Ang personally identifiable information (mga pangalan, IBAN, mga postal address) ay awtomatikong rine-redact sa CLI output at streaming mode. Naka-on ito bilang default.

- **CLI**: Ang mga sensitibong field ay ipinapakita bilang `***REDACTED***`
- **Streaming**: `parse_streaming(redact_pii=True)` (default)
- **Mga Export**: Ang CSV/JSON/Excel ay nagpapanatili ng buong data para sa downstream processing
- **Opt-in**: Gamitin ang `--show-pii` o `redact_pii=False` kapag kailangan mo ng hindi na-redact na output

## XML Security (XXE Protection)

Lahat ng XML parsing ay gumagamit ng `lxml` na may hardened na setting:

- `resolve_entities=False` -- pinipigilan ang mga XML entity expansion attack
- `no_network=True` -- hinaharangan ang lahat ng papalabas na network access mula sa parser
- `load_dtd=False` -- pinipigilan ang mga DTD-based na attack
- Namespace stripping bago iproseso -- ligtas na pinangangasiwaan ang anumang CAMT.053 variant

## ZIP Archive Security

Bineberipika ng `iter_secure_xml_entries()` ang bawat ZIP member bago ang extraction:

- **Entry size cap**: 10 MB bawat entry (nako-configure)
- **Total size cap**: 50 MB kabuuang uncompressed (nako-configure)
- **Compression ratio limit**: 100:1 default -- nakaka-detect ng mga ZIP bomb
- **Encrypted entry rejection**: Nilalaktawan ang mga encrypted entry na may babala
- **Walang disk write**: Ang mga XML byte ay direktang dumadaan sa parser sa pamamagitan ng `from_bytes()`

## Path Traversal Prevention

Hinaharangan ng input validation ang mga mapanganib na file path:

- Null bytes, directory traversal pattern (`../`), at mga symlink ay tinatanggihan
- File extension validation laban sa mga inaasahang format
- Mga file size limit (100 MB default, nako-configure)

## Beripikasyon ng Balanse (Golden Rule)

Bawat PDF extraction ay bineberipika gamit ang equation: `opening balance + credits − debits == closing balance`. Ang mga resulta ay tina-tag bilang VERIFIED, DISCREPANCY, o FAILED. Ang mga diskrepansya ay maaaring suriin nang interactive gamit ang `--type review`.

## Deterministikong Output

Para sa mga structured na format (CAMT, PAIN.001, CSV, OFX, QFX, MT940), sa parehong input file, ang parser ay gumagawa ng byte-identical na output sa bawat run. Walang randomness, walang model inference, walang heuristic sampling. Kritikal ito para sa:

- **Audit reproducibility**: Patakbuhin ang parehong file nang dalawang beses at i-diff ang output
- **Regulatory compliance**: Magpakita ng pare-parehong pagproseso
- **CI verification**: 718 na pagsubok ang nagpapatupad ng determinismo na may 100% branch coverage

## Supply Chain Security

- **SHA-256 hash-locked dependencies**: Bawat package sa `poetry.lock` ay may na-verify na file hash
- **CycloneDX SBOM**: Ang bawat release ay may kasamang Software Bill of Materials
- **GitHub build provenance**: Iniuugnay ng attestation ang bawat artifact sa source commit nito
- **Signed commits**: Lahat ng commit ay SSH-signed at na-verify sa CI
- **Dependency verification**: Bineberipika ng `scripts/verify_locked_hashes.py` ang lahat ng hash nang lokal

## I-verify nang Lokal

```bash
python -m pytest                          # 718 tests, 100% branch coverage
python scripts/verify_locked_hashes.py    # SHA-256 hash verification
git log --show-signature -1               # Verify commit signature
```
