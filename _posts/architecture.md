---
name: "Bank Statement Parser"
short_name: "bankstatementparser"
title: "Internal Architecture: Tokenization, Normalization & Validation"
description: "Architectural deep-dive into the four-stage parsing pipeline powering Bank Statement Parser."
keywords: "statement parsing pipeline, document tokenizer, financial data normalization, ISO 20022 validator"
author: "Sebastien Rousseau"
date: "2026-09-01"
language: "en-GB"
layout: "page"
permalink: "https://bankstatementparser.com/architecture/index.html"
logo: "https://cloudcdn.pro/bankstatementparser/v1/logos/bankstatementparser.svg"
banner: "https://cloudcdn.pro/stocks/images/quantum-computer-room-1200.webp"
banner_alt: "Bank Statement Parser — High-Throughput Financial Document Parsing Engine"
---

# Architecture & Pipeline Specifications

Bank Statement Parser implements a deterministic, four-stage extraction and validation pipeline.

```
+------------------+     +-------------------+     +---------------------+     +--------------------+
| 1. Stream Ingest | --> | 2. Layout Tokenizer| --> | 3. Field Normalizer | --> | 4. Schema Validator|
| (PDF/CSV/OFX)    |     | (Spatial Extraction)|    | (Date/Amount/IBAN)  |     | (JSON / ISO 20022) |
+------------------+     +-------------------+     +---------------------+     +--------------------+
```

1. **Stream Ingestion:** Zero-copy memory mapping of input statement bytes.
2. **Layout Tokenization:** Spatial bounding-box and tabular coordinate mapping.
3. **Field Normalization:** Canonical standardization of transaction codes, currencies, and dates.
4. **Schema Validation:** Mathematical checksum balance verification.
