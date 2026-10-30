# Migration Guide

This guide covers migrating existing financial parsing pipelines to **Bank Statement Parser** from cloud OCR APIs, single-format Python/Rust libraries, and earlier `0.0.x` releases.

---

## 1. Migrating from Cloud OCR & SaaS Aggregators (Ocrolus, AWS Textract, Plaid)

Cloud document APIs introduce per-page fees, network latency (`1–5 s` per document), and third-party data custody risks. Bank Statement Parser runs 100% in-process with zero outbound network calls.

| Capability | Cloud OCR / Aggregator API | Bank Statement Parser |
| :--- | :--- | :--- |
| **Execution Boundary** | External vendor cloud | Local process / air-gapped VPC |
| **Telemetry & Egress** | Vendor logs & request metadata | Zero telemetry (`0` network calls) |
| **Median Latency** | `1,200 ms - 4,500 ms` | `< 0.8 ms` (digital streams) |
| **Balance Verification** | Best-effort field extraction | Deterministic arithmetic proof (`opening + net == closing`) |

### Replacement Pattern (Python)

```python
# Before: External HTTP upload to cloud OCR endpoint
# response = requests.post("https://api.vendor.example/v1/parse", files={"file": open("statement.pdf", "rb")})

# After: Local deterministic extraction with arithmetic balance proof
from bankstatementparser import BankStatementParser

parser = BankStatementParser()
statement = parser.parse_file("statement.pdf")
assert statement.balance_verified is True
```

---

## 2. Migrating from Single-Format Python Libraries (`mt940`, `ofxparse`, `csv`)

Instead of maintaining separate dependencies and bespoke normalization glue for each banking standard, consolidate onto the unified `Statement` and `Transaction` schema:

| Legacy Library | Format Scope | Bank Statement Parser Equivalent |
| :--- | :--- | :--- |
| `mt940` / `swift-mt940` | SWIFT MT940 only | `BankStatementParser` (`MT940` + `MT942` + structured `:86:` tags) |
| `ofxparse` / `ofxtools` | OFX 1.x / 2.x | `BankStatementParser` (SGML `1.x` + XML `2.x` OFX/QFX) |
| `xml.etree` custom scripts | ISO 20022 XML | `CamtParser` (`camt.052`, `camt.053`, `camt.054`) & `Pain001Parser` |
| `pandas.read_csv` | Delimited CSV | Statistical dialect, date format, and decimal auto-detection |

---

## 3. Upgrading Documentation & Site Releases (`v0.0.5` to `v0.0.6`)

* **Canonical Theme (`Visage`)**: All layouts in `_layouts/` now inherit from `_layouts/base.html`, `_layouts/header.html`, and `_layouts/footer.html` using `{{#extends "base"}}` and `{{!content}}`.
* **Header Search Slot**: Top navigation embeds `<span data-ssg-search></span>` inside `#navMenu`, which `ssg 0.0.69` populates at build time with `#ssg-search-btn`.
* **Verification Gate**: Run `make verify` to execute SPDX header checks, frontmatter validation, WCAG 2.2 AAA contrast verification, property tests, and `ssg audit`.
