---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Bank Statement Parser Use Cases"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Bank Statement Parser. All rights reserved."
date: "Apr 11, 2026"
description: "How treasury teams, fintech developers, and compliance officers use Bank Statement Parser for MT940-to-CAMT migration, reconciliation, audit pipelines, and multi-bank consolidation."
download: ""
format-detection: "telephone=no"
hreflang: "en"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/use-cases/index.html"
image_alt: "Logo of Bank Statement Parser, Empower Your Financial Analysis with Seamless Data Extraction"
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "bank statement use cases, treasury MT940 migration, bank reconciliation python, compliance audit pipeline, multi-bank consolidation, SFTP bank statement processing"
language: "en-GB"
layout: "about"
locale: "en_GB"
logo_alt: "Logo of Bank Statement Parser, Empower Your Financial Analysis with Seamless Data Extraction"
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Use Cases"
permalink: "https://bankstatementparser.com/use-cases/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Real-World Applications"
tags: "use-cases,treasury,reconciliation,compliance,migration"
theme_color: "rgb(73, 214, 251)"
title: "Bank Statement Parser Use Cases: Treasury, Reconciliation, and Compliance"
url: "https://bankstatementparser.com/use-cases/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/use-cases/rss.xml"
category: "Finance Software, Python Library, Data Processing"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "How treasury teams, fintech developers, and compliance officers use Bank Statement Parser for MT940-to-CAMT migration, reconciliation, audit pipelines, and multi-bank consolidation."
item_guid: "https://bankstatementparser.com/use-cases/rss.xml"
item_link: "https://bankstatementparser.com/use-cases/rss.xml"
item_pub_date: "2026-04-11T00:00:00+00:00"
item_title: "Bank Statement Parser Use Cases: Treasury, Reconciliation, and Compliance"
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
apple-mobile-web-app-title: "Bank Statement Parser Use Cases: Treasury, Reconciliation, and Compliance"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "How treasury teams, fintech developers, and compliance officers use Bank Statement Parser for MT940-to-CAMT migration, reconciliation, audit pipelines, and multi-bank consolidation."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logo of Bank Statement Parser, Empower Your Financial Analysis with Seamless Data Extraction"
twitter_site: "@wwdseb"
twitter_title: "Bank Statement Parser Use Cases: Treasury, Reconciliation, and Compliance"
twitter_url: "https://bankstatementparser.com/use-cases/index.html"

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

Bank Statement Parser handles real-world financial workflows: PDF bank statement ingestion, MT940-to-CAMT migration, automated reconciliation with balance verification, compliance pipelines, plaintext-accounting export, REST API deployments, bulk scanning, and multi-bank consolidation.

## PDF Bank Statement Ingestion

**Result:** Parse digital and scanned PDF bank statements with automatic balance verification — no cloud APIs, no data leaves your machine.

The hybrid PDF pipeline routes each PDF through the optimal extraction path and verifies every result.

```python
from bankstatementparser.hybrid import smart_ingest

result = smart_ingest("statement.pdf")
print(result.source_method)         # "deterministic" | "llm" | "vision"
print(result.verification.status)   # VERIFIED | DISCREPANCY | FAILED

# Review discrepancies interactively
# bankstatementparser --type review --input result.json
```

## Bulk Statement Processing

**Result:** Scan entire folder trees (hundreds of PDFs, XMLs, CSVs) with automatic cross-file deduplication in a single call.

```python
from bankstatementparser.hybrid import scan_and_ingest

batch = scan_and_ingest("statements/2026/", pattern="**/*.pdf")
print(f"Files: {len(batch.results)}, Unique txns: {batch.unique_count}")
```

## Treasury: MT940 to CAMT.053 Migration

**Result:** A single API call handles both MT940 and CAMT.053 during the SWIFT migration window (November 2025–November 2028), eliminating the need for separate parsing pipelines.

Treasury teams worldwide are migrating from MT940 to CAMT.053 ahead of the November 2027 SWIFT deadline. Bank Statement Parser handles both formats with a single API, making the transition seamless.

```python
from bankstatementparser import create_parser, detect_statement_format

# Process both MT940 and CAMT.053 with the same code
for file in daily_statement_files:
    fmt = detect_statement_format(file)
    parser = create_parser(file, fmt)
    df = parser.parse()
    load_to_treasury_system(df)
```

## Automated Reconciliation with Balance Verification

**Result:** Format-agnostic DataFrames with Golden Rule verification and deduplication catch errors and duplicates before they reach your ledger.

Parse bank statements, verify balances, and match against internal records automatically.

```python
from bankstatementparser import CamtParser, Deduplicator
from bankstatementparser.hybrid import verify_balance_multi_currency

parser = CamtParser("bank_statement.xml")
bank_txns = parser.parse()

# Verify balances per currency
verification = verify_balance_multi_currency(bank_txns)
for ccy, result in verification.items():
    assert result.status == "VERIFIED", f"{ccy} balance mismatch!"

# Deduplicate before reconciliation
dedup = Deduplicator()
result = dedup.deduplicate(dedup.from_dataframe(bank_txns))
clean_txns = result.unique_transactions

# Match against internal records
unmatched = reconcile(clean_txns, internal_ledger)
```

## Plaintext Accounting (hledger / beancount)

**Result:** Automatically ingest PDF bank statements and export categorised transactions to hledger or beancount journal format.

```python
from bankstatementparser.hybrid import smart_ingest
from bankstatementparser.enrichment import Categorizer
from bankstatementparser.export import to_hledger

result = smart_ingest("statement.pdf")
categorizer = Categorizer()
enriched = categorizer.categorize_batch(result.transactions)
journal = to_hledger(enriched, account="Assets:Bank:Checking")
```

## REST API Deployment

**Result:** Deploy Bank Statement Parser as a microservice that accepts statement files via HTTP and returns structured JSON.

```bash
# Start the API server
bankstatementparser-api --port 8000
```

```bash
# Ingest a statement
curl -X POST http://localhost:8000/ingest \
  -F "file=@statement.pdf"
```

## Compliance and Audit Pipelines

**Result:** Deterministic output, automatic PII redaction, and Golden Rule verification produce audit-ready logs that satisfy regulatory reproducibility requirements.

```python
from bankstatementparser import CamtParser

parser = CamtParser("statement.xml")

# Stream with PII redacted for audit logs
for txn in parser.parse_streaming(redact_pii=True):
    audit_log.write(txn)

# Export full data for secure internal processing
parser.export_csv("archive/statement.csv")
```

## SFTP-to-DataFrame Workflows

**Result:** Parse directly from bytes with zero disk I/O, fitting natively into SFTP and API-driven bank connectivity workflows.

```python
from bankstatementparser import CamtParser

xml_bytes = sftp_client.read("daily_statement.xml")
parser = CamtParser.from_bytes(xml_bytes, source_name="daily.xml")
df = parser.parse()
```

## Multi-Bank Consolidation

**Result:** Parallel parsing across HSBC (CAMT), Barclays (MT940), Revolut (CSV), Wise (OFX), and Chase (PDF) produces a single normalised dataset.

```python
from bankstatementparser import parse_files_parallel

results = parse_files_parallel([
    "hsbc/camt053.xml",
    "barclays/mt940.sta",
    "revolut/transactions.csv",
    "wise/statement.ofx",
])

all_transactions = pd.concat([r.transactions for r in results if r.status == "success"])
```

## Batch Processing with ZIP Archives

**Result:** Built-in ZIP bomb protection (100:1 ratio limit, 10 MB entry cap, encrypted entry rejection) lets you process monthly statement archives safely.

```python
from bankstatementparser import iter_secure_xml_entries, CamtParser

for entry in iter_secure_xml_entries("monthly_statements.zip"):
    parser = CamtParser.from_bytes(entry.xml_bytes, source_name=entry.source_name)
    df = parser.parse()
    save_to_warehouse(entry.source_name, df)
```

[Compare with alternatives ❯](/comparison/index.html) | [Plan your ISO 20022 migration ❯](/migration/index.html) | [Get started ❯](/getting-started/index.html)
