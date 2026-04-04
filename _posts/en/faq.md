---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Frequently Asked Questions about Bank Statement Parser"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Bank Statement Parser. All rights reserved."
date: "Apr 01, 2026"
description: "Answers to common questions about Bank Statement Parser: data privacy, PII redaction, performance, ISO 20022 support, streaming, compliance, and treasury workflows."
download: ""
format-detection: "telephone=no"
hreflang: "en"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/faq/index.html"
image_alt: "Logo of Bank Statement Parser, a powerful Python tool designed for quick, accurate financial data processing and insights extraction."
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "bank statement parser FAQ, CAMT parser questions, PAIN.001 FAQ, ISO 20022 python FAQ, PII redaction banking, bank parser performance, financial data privacy, MT940 parser FAQ, streaming parser python, bank statement compliance"
language: "en-GB"
layout: "faq"
locale: "en_GB"
logo_alt: "Logo of Bank Statement Parser, a powerful Python tool designed for quick, accurate financial data processing and insights extraction."
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "FAQ"
permalink: "https://bankstatementparser.com/faq/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Common Questions About Bank Statement Parser"
tags: "faq,bank,statement,parser,privacy,compliance,performance,streaming,iso20022,python"
theme_color: "rgb(73, 214, 251)"
title: "Bank Statement Parser FAQ: Privacy, Performance, and Usage"
url: "https://bankstatementparser.com/faq/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/faq/rss.xml"
category: "Finance Software, Python Library, FAQ"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Answers to common questions about Bank Statement Parser: data privacy, PII redaction, performance, ISO 20022 support, streaming, compliance, and treasury workflows."
item_guid: "https://bankstatementparser.com/faq/rss.xml"
item_link: "https://bankstatementparser.com/faq/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Bank Statement Parser FAQ: Privacy, Performance, and Usage"
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
apple-mobile-web-app-title: "Bank Statement Parser FAQ: Privacy, Performance, and Usage"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Answers to common questions about Bank Statement Parser: data privacy, PII redaction, performance, ISO 20022 support, and treasury workflows."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logo of Bank Statement Parser, a powerful Python tool designed for quick, accurate financial data processing and insights extraction."
twitter_site: "@wwdseb"
twitter_title: "Bank Statement Parser FAQ: Privacy, Performance, and Usage"
twitter_url: "https://bankstatementparser.com/faq/index.html"

# Humans.txt - The Humans.txt front matter (YAML).

author_website: "https://bankstatementparser.com"
author_twitter: "@wwdseb"
author_location: "London, UK"
thanks: "Thanks for reading!"
site_last_updated: "2026-04-01"
site_standards: "HTML5, CSS3, RSS, Atom, JSON, XML, YAML, Markdown, TOML"
site_components: "Shokunin SSG, Shokunin CLI, Shokunin Templates, Kaishi Templates, Kaishi Themes"
site_software: "Shokunin, Rust"

---

## Data Privacy and Compliance

### Does any data leave my infrastructure?

**No.** Bank Statement Parser operates as a stateless library. All processing -- parsing, PII redaction, archive extraction -- occurs within your local runtime memory. No API calls, no cloud services, no telemetry. XML parsers are hardened with `no_network=True`, blocking all outbound access at the parser level. Your financial data never leaves your environment.

### How does PII redaction work?

Sensitive fields are masked before they reach your application logic. The parser identifies debtor names, creditor names, IBANs, and postal addresses, replacing them with `***REDACTED***` in console output and streaming mode.

- **Redaction is on by default** in CLI output and streaming mode.
- **File exports** (CSV, JSON, Excel) retain unredacted data for downstream processing.
- **Opt in** to full data with `--show-pii` on the CLI or `redact_pii=False` in the API.

### Is the extraction process deterministic?

**Yes -- byte-identical output on every run.** Given the same input file, the parser produces the same result every time. No randomness, no model inference, no heuristic sampling. CI enforces determinism with 467 tests at 100% branch coverage, including property-based fuzzing via Hypothesis.

### What compliance standards does the project follow?

The project maintains ISO 13485-aligned documentation with full traceability:

- A quantified **Risk Register** with severity/probability scoring and residual risk assessment.
- A **Verification and Validation Plan** with 19 gated steps across 5 phases.
- A **Change Control Procedure** with impact assessment and rollback protocols.
- A **SOUP Register** covering all dependencies with risk levels and EOL tracking.
- A **Traceability Matrix** mapping design inputs to implementation and verification.

Every release includes a CycloneDX SBOM, SHA-256 checksums, and GitHub build provenance attestation.

## Performance and Scalability

### How fast is Bank Statement Parser?

Performance thresholds are validated in CI on every commit:

| Metric | Value |
|---|---|
| CAMT.053 throughput | 27,000+ transactions/second |
| PAIN.001 throughput | 52,000+ transactions/second |
| Per-transaction latency (CAMT) | 37 microseconds |
| Per-transaction latency (PAIN.001) | 19 microseconds |
| Time to first result | < 2 ms |

### How are large files handled?

**Streaming with bounded memory -- tested at 50,000 transactions per file.** Use `parse_streaming()` to process XML files incrementally. Each transaction is yielded as a dictionary; elements are cleared after processing to prevent memory growth. Memory does not scale with file size -- the 50K-transaction test (25+ MB) uses less than 2x the memory of the 10K-transaction test.

For files exceeding 50 MB (e.g., host-to-host PAIN.001 batches with 100K+ payments), the parser streams through a temporary file with chunk-based namespace stripping -- the full document is never loaded into memory.

### How are ZIP archives processed securely?

`iter_secure_xml_entries()` validates each member before extraction:

- **Entry size cap** (default 10 MB per entry)
- **Total uncompressed size cap** (default 50 MB)
- **Compression ratio limit** (default 100:1) to prevent ZIP bombs
- **Encrypted entry rejection**

No file is written to disk. XML bytes pass directly to the parser via `from_bytes()`.

### Can I parse multiple files in parallel?

**Yes.** Use `parse_files_parallel()` which distributes work across a `ProcessPoolExecutor`:

```python
from bankstatementparser import parse_files_parallel

results = parse_files_parallel([
    "statements/jan.xml",
    "statements/feb.xml",
    "statements/mar.xml",
])
for r in results:
    print(r.path, r.status, len(r.transactions), "rows")
```

## Supported Formats

### Which bank statement formats are supported?

| Format | Standard | File Types | Parser Class |
|---|---|---|---|
| CAMT.053 | ISO 20022 Bank-to-Customer Statement | `.xml` | `CamtParser` |
| PAIN.001 | ISO 20022 Credit Transfer Initiation | `.xml` | `Pain001Parser` |
| CSV | Generic bank exports | `.csv` | `CsvStatementParser` |
| OFX | Open Financial Exchange | `.ofx` | `OfxParser` |
| QFX | Quicken Financial Exchange | `.qfx` | `QfxParser` |
| MT940 | SWIFT standard | `.mt940`, `.sta` | `Mt940Parser` |

### Does the parser handle bank-specific dialects of CAMT.053?

**Yes -- namespace-agnostic by design.** The parser strips XML namespaces before processing, handling any CAMT.053 variant (`camt.053.001.02`, `camt.053.001.04`, or proprietary bank wrappers) without namespace-specific configuration. XPath queries target element structure, not namespace URIs.

For banks that wrap CAMT in a custom envelope, use `from_string()` or `from_bytes()` to feed the inner document directly.

### Can I map custom CSV column headers to the standard schema?

**Yes -- automatic normalisation, zero configuration.** `CsvStatementParser` recognises common header variations: `"Date"`, `"Transaction Date"`, `"Booking Date"` all map to the `date` field. `"Amount"`, `"Value"`, `"Sum"` map to `amount`. Split credit/debit columns (e.g., `"Credit"` and `"Debit"`) are detected and combined into a single signed amount automatically.

### What is the output format?

All parsers produce standardised pandas DataFrames with consistent column types:

| Format | Key Columns |
|---|---|
| **CAMT** | `Amount`, `Currency`, `DrCr`, `Debtor`, `Creditor`, `Reference`, `ValDt`, `BookgDt`, `AccountId` |
| **PAIN.001** | `PmtInfId`, `PmtMtd`, `InstdAmt`, `Currency`, `CdtrNm`, `EndToEndId`, `MsgId`, `CreDtTm`, `NbOfTxs` |
| **CSV/OFX/QFX/MT940** | `date`, `description`, `amount` (normalised) |

You can also export to CSV, JSON, Excel, or convert to Polars DataFrames.

## Treasury Workflows

### How does the parser handle multi-currency statements?

**Each transaction preserves its original currency -- no implicit conversion.** The `Currency` field is extracted from the XML `Ccy` attribute per transaction. Multi-currency statements remain as-is. The `get_account_balances()` method returns opening and closing balances per account with original currency codes. Cross-currency reconciliation is left to your downstream logic, where you control the exchange rate source.

### Does the parser support both outgoing and incoming formats?

**Yes.** `Pain001Parser` handles ISO 20022 PAIN.001 credit transfer initiation files (outgoing payments). `CamtParser` handles CAMT.053 bank-to-customer statement files (incoming reporting). Both support streaming, PII redaction, and export to CSV, JSON, and Excel. Use `detect_statement_format()` to identify the format automatically.

### What happens when a transaction entry is malformed?

Behaviour depends on the parsing mode:

- **`parse()` (batch mode)** -- Malformed entries missing required fields (`Amount`, `Currency`, or `CdtDbtInd`) are skipped with a warning log. The rest of the statement parses normally.
- **`parse_streaming()` (streaming mode)** -- Parse errors propagate immediately as exceptions. No silent data loss. This fail-fast behaviour is intentional for financial workflows where every transaction must be accounted for.

### How does deduplication work?

The `Deduplicator` class detects exact duplicates and suspected matches with explainable confidence scores:

```python
from bankstatementparser import CamtParser, Deduplicator

parser = CamtParser("statement.xml")
dedup = Deduplicator()
result = dedup.deduplicate(dedup.from_dataframe(parser.parse()))

print(f"Unique: {len(result.unique_transactions)}")
print(f"Exact duplicates: {len(result.exact_duplicates)}")
print(f"Suspected matches: {len(result.suspected_matches)}")
```

## Installation and Compatibility

### How do I install Bank Statement Parser?

```bash
pip install bankstatementparser
```

For optional Polars DataFrame support:

```bash
pip install bankstatementparser[polars]
```

### Which Python versions are supported?

Python 3.9 through 3.14. All versions are tested in CI with 467 tests at 100% branch coverage.

### What are the dependencies?

The library has 5 direct dependencies:

- `lxml` -- XML parsing with security hardening
- `pandas` -- DataFrames and data manipulation
- `openpyxl` -- Excel export
- `pydantic` -- Data validation and models
- `defusedxml` -- XXE protection

All dependencies have SHA-256 hash-locked versions. The CycloneDX SBOM maps every runtime component.

### Does it work on macOS, Linux, and Windows?

**Yes.** The library works on macOS, Linux, and Windows (via WSL). It has no platform-specific dependencies.

## Reproducibility and Security

### How can I verify reproducibility?

```bash
python -m pytest                              # 467 tests, 100% branch coverage
python scripts/verify_locked_hashes.py        # SHA-256 hash verification
git log --show-signature -1                   # Verify commit signature
```

### What security protections are built in?

- **XXE Protection**: `resolve_entities=False`, `no_network=True`, `load_dtd=False`
- **ZIP Bomb Protection**: Compression ratio limits, entry size caps, encrypted entry rejection
- **Path Traversal Prevention**: Dangerous pattern blocklist and symlink resolution
- **Input Validation**: File size limits (100 MB default), extension/format validation
- **Supply Chain**: SHA-256 hash-locked dependencies, CycloneDX SBOM, build provenance attestation
- **Signed Commits**: Enforced in CI

### How does Bank Statement Parser compare to pyiso20022?

pyiso20022 is a broad ISO 20022 toolkit that generates Python dataclasses from ISO XML schemas. It covers a wide range of ISO 20022 message types (PACS, PAIN, CAMT, ADMI) with schema validation. Bank Statement Parser is purpose-built for bank statement parsing with streaming support, PII redaction, deduplication, and a unified API across six formats including non-ISO formats (CSV, OFX, QFX, MT940). If you need to parse bank statements into DataFrames with production-grade security, use Bank Statement Parser. If you need to work with the full ISO 20022 message catalogue, use pyiso20022.

### What are the SWIFT ISO 20022 migration deadlines?

SWIFT has published a phased migration timeline:

- **November 2026**: Structured and hybrid addresses become mandatory. MT101 multi-instruction messages will be rejected. Case Management Phase 1 begins.
- **November 2027**: All financial institutions must be able to receive CAMT.053 statements natively. SWIFT will stop converting MT to ISO format.
- **November 2028**: Full retirement of MT940, MT942, MT950, MT900, and MT910. These will be replaced by CAMT.052, CAMT.053, and CAMT.054 equivalents.

Bank Statement Parser supports both the legacy MT940 format and the modern CAMT.053/PAIN.001 formats, making it ideal for the transition period.

