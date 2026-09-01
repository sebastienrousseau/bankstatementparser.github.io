---
name: "Bank Statement Parser"
short_name: "bankstatementparser"
title: "Bank Statement Parser: High-Throughput Financial Document Engine"
description: "High-throughput, privacy-first parser converting bank statements (PDF, CSV, OFX, MT940, CAMT.053) into validated JSON and ISO 20022 messages with zero telemetry."
keywords: "bank statement parser, PDF bank statement to CSV, OFX parser, MT940 to JSON, ISO 20022 parser, Rust financial parser, Python bank statement"
author: "Sebastien Rousseau"
date: "2026-09-01"
language: "en-GB"
layout: "index"
permalink: "https://bankstatementparser.com/"
logo: "https://cloudcdn.pro/bankstatementparser/v1/logos/bankstatementparser.svg"
banner: "https://cloudcdn.pro/stocks/images/quantum-computer-room-1200.webp"
banner_alt: "Bank Statement Parser — High-Throughput Financial Document Parsing Engine"
---

<section class="hero-editorial">
<div class="eyebrow-badge">
<span class="eyebrow-pulse"></span>
<span>Financial Document Engineering · Open Source · Rust & Python · Updated September 2026</span>
</div>
<h1>Parse any bank statement in milliseconds.<br>Zero cloud dependencies. Zero telemetry.</h1>
<p class="hero-lead">An open-source, high-throughput financial document parsing engine engineered in Rust with native Python bindings. Converts PDF, CSV, OFX, QIF, MT940, and CAMT.053 bank statements into validated, structured JSON and ISO 20022 transaction streams entirely on your own infrastructure.</p>
<div class="hero-actions">
<a href="/getting-started/index.html" class="btn-primary-quantum">Get Started (CLI & SDK) →</a>
<a href="/formats/index.html" class="btn-secondary-quantum">Explore Supported Formats</a>
</div>
</section>

<!-- SECTION 2: KEY STATS TICKER -->
<section class="clock-ticker-section my-5" aria-label="Performance Benchmarks">
<div class="row g-3">
<div class="col-md-4 col-lg-2-4">
<div class="stat-card">
<div class="stat-figure">10,000+</div>
<div class="stat-label">Pages per Minute</div>
<div class="stat-source">Multi-threaded Rust core · <a href="/benchmarks/index.html">Benchmark Report ↗</a></div>
</div>
</div>

<div class="col-md-4 col-lg-2-4">
<div class="stat-card">
<div class="stat-figure">&lt; 0.8 ms</div>
<div class="stat-label">Per-Statement Latency</div>
<div class="stat-source">Zero-allocation tokenizer · <a href="/benchmarks/index.html">Latency Specs ↗</a></div>
</div>
</div>

<div class="col-md-4 col-lg-2-4">
<div class="stat-card">
<div class="stat-figure">100%</div>
<div class="stat-label">Zero Telemetry</div>
<div class="stat-source">Air-gapped local processing · <a href="/security/index.html">Privacy Guarantee ↗</a></div>
</div>
</div>

<div class="col-md-6 col-lg-2-4">
<div class="stat-card">
<div class="stat-figure">14+ Formats</div>
<div class="stat-label">Multi-Standard Ingestion</div>
<div class="stat-source">PDF, CSV, OFX, MT940, CAMT · <a href="/formats/index.html">Format Matrix ↗</a></div>
</div>
</div>

<div class="col-md-6 col-lg-2-4">
<div class="stat-card">
<div class="stat-figure">Dual Apache/MIT</div>
<div class="stat-label">Open Source License</div>
<div class="stat-source">Enterprise-friendly · <a href="https://github.com/sebastienrousseau/bankstatementparser" target="_blank" rel="noopener noreferrer">GitHub Repo ↗</a></div>
</div>
</div>
</div>
</section>

<!-- SECTION 3: CORE CAPABILITIES BENTO GRID -->
<section class="my-5" aria-label="Core Capabilities">
<div class="text-center mb-4">
<h2 class="h3 fw-bold">Engineered for Sovereign Financial Infrastructure</h2>
<p class="text-muted">Built for corporate treasuries, fintech backends, reconciliation engines, and audit firms requiring deterministic extraction.</p>
</div>

<div class="bento-grid">
<div class="bento-card bento-col-4">
<div>
<div class="bento-tag">Privacy & Security</div>
<h3 class="bento-title">Air-Gapped Local Computation</h3>
<p class="bento-desc">Financial statements contain sensitive account numbers, balances, and transaction histories. Bank Statement Parser never phones home, makes no external network calls, and runs entirely in local memory.</p>
</div>
<a href="/security/index.html" class="author-link">Read Security Architecture →</a>
</div>

<div class="bento-card bento-col-4">
<div>
<div class="bento-tag">Format Intelligence</div>
<h3 class="bento-title">Automatic Dialect Detection</h3>
<p class="bento-desc">Intelligent auto-detection for CSV delimiter variations, date formats (ISO, US, UK, European), debit/credit column layouts, and multi-currency transaction splits without fragile custom regex rules.</p>
</div>
<a href="/formats/index.html" class="author-link">Explore Format Dialects →</a>
</div>

<div class="bento-card bento-col-4">
<div>
<div class="bento-tag">Standardization</div>
<h3 class="bento-title">ISO 20022 & JSON Output</h3>
<p class="bento-desc">Normalize disparate bank statements directly into canonical ISO 20022 camt.053 XML envelopes or strongly-typed JSON schemas ready for ERP, GL, and accounting database ingestion.</p>
</div>
<a href="/architecture/index.html" class="author-link">View Output Schemas →</a>
</div>
</div>
</section>

<!-- SECTION 4: TERMINAL QUICKSTART -->
<section class="my-5" aria-label="Developer Quickstart">
<div class="card-surface p-4 p-md-5">
<div class="row align-items-center g-4">
<div class="col-lg-6">
<div class="eyebrow-badge">Developer Quickstart</div>
<h2 class="h3 fw-bold text-headline mb-3">Install via Cargo, Pip or Homebrew in Seconds</h2>
<p class="text-muted mb-4">Use as a blazing-fast command-line tool, an embedded Rust library in microservices, or a high-level Python package for data engineering pipelines.</p>
<div class="d-flex gap-3 flex-wrap">
<a href="/getting-started/index.html" class="btn-primary-quantum">Full Documentation →</a>
<a href="/api/index.html" class="btn-secondary-quantum">API Reference</a>
</div>
</div>
<div class="col-lg-6">
<div class="hero-visual-terminal">
<div class="terminal-header">
<span class="terminal-dot dot-red"></span>
<span class="terminal-dot dot-yellow"></span>
<span class="terminal-dot dot-green"></span>
<span class="terminal-title">bash — bankstatementparser</span>
</div>
<pre><code><span class="text-muted"># Install via Cargo (Rust)</span>
$ cargo install bankstatementparser

<span class="text-muted"># Or install via Pip (Python)</span>
$ pip install bankstatementparser

<span class="text-muted"># Parse a PDF statement to ISO 20022 JSON</span>
$ bankstatementparser --input statement.pdf --format json

<span class="text-muted"># Output:</span>
{
  "account_number": "GB82BARC20000012345678",
  "currency": "GBP",
  "opening_balance": 15420.50,
  "closing_balance": 18940.20,
  "transactions_count": 42,
  "status": "VALIDATED"
}</code></pre>
</div>
</div>
</div>
</div>
</section>

<!-- SECTION 5: USE CASES -->
<section class="my-5" aria-label="Use Cases">
<div class="text-center mb-4">
<h2 class="h3 fw-bold">Built for Mission-Critical Financial Workflows</h2>
<p class="text-muted">Eliminate manual statement keying, brittle spreadsheets, and opaque proprietary OCR APIs.</p>
</div>

<div class="bento-grid">
<div class="bento-card bento-col-4">
<div class="bento-tag">Corporate Treasury</div>
<h3 class="bento-title">Automated Bank Reconciliation</h3>
<p class="bento-desc">Ingest multi-bank end-of-day balances and transaction statements into treasury management systems (TMS) with sub-second turnaround.</p>
<a href="/use-cases/index.html" class="author-link">Treasury Playbook →</a>
</div>

<div class="bento-card bento-col-4">
<div class="bento-tag">Fintech & Lending</div>
<h3 class="bento-title">Borrower Cashflow Underwriting</h3>
<p class="bento-desc">Extract, verify, and calculate debt-service coverage ratios (DSCR) and revenue velocity from 24 months of borrower bank statements instantly.</p>
<a href="/use-cases/index.html" class="author-link">Underwriting Workflows →</a>
</div>

<div class="bento-card bento-col-4">
<div class="bento-tag">Audit & Compliance</div>
<h3 class="bento-title">Forensic AML & Audit Verification</h3>
<p class="bento-desc">Detect statement tampering, verify arithmetic checksums between opening/closing balances, and extract counterparty IBANs for sanctions screening.</p>
<a href="/use-cases/index.html" class="author-link">Audit Guidelines →</a>
</div>
</div>
</section>

<!-- SECTION 6: QUESTIONS? ANSWERS. (APPLE AT WORK ACCORDION) -->
<section class="my-5" aria-label="Frequently Asked Questions">
<div class="apple-faq-section">
<div class="apple-faq-header">
<h2 class="apple-faq-title">Questions? Answers.</h2>
<button type="button" class="apple-faq-expand-btn" id="faqExpandAllBtn" aria-expanded="false">
<span class="apple-faq-btn-text">Expand all</span>
<svg class="apple-faq-expand-chevron" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg>
</button>
</div>

<div class="apple-faq-list">
<details class="apple-faq-item">
<summary class="apple-faq-summary">
<span class="apple-faq-question">Does Bank Statement Parser send data to the cloud or any external server?</span>
<span class="apple-faq-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg></span>
</summary>
<div class="apple-faq-body">
<p>No. Bank Statement Parser is 100% self-contained and operates entirely on your local machine or private cloud server. It contains zero analytics, zero telemetry, and zero outbound network calls, ensuring complete compliance with GDPR, HIPAA, GLBA, and banking confidentiality regulations.</p>
</div>
</details>

<details class="apple-faq-item">
<summary class="apple-faq-summary">
<span class="apple-faq-question">Which bank statement file formats are supported?</span>
<span class="apple-faq-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg></span>
</summary>
<div class="apple-faq-body">
<p>Bank Statement Parser supports text-based and digital PDFs, CSV files (with automatic delimiter and header detection), Open Financial Exchange (OFX 1.x & 2.x), Quicken Interchange Format (QIF), SWIFT MT940/MT942 messages, and ISO 20022 CAMT.053 XML statements.</p>
</div>
</details>

<details class="apple-faq-item">
<summary class="apple-faq-summary">
<span class="apple-faq-question">How does the parser handle scanned or image-based PDFs?</span>
<span class="apple-faq-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg></span>
</summary>
<div class="apple-faq-body">
<p>For vector and digital PDFs, the engine extracts structured text streams directly with zero loss. For scanned image statements, the optional local OCR module utilizes deterministic optical layout parsing with zero external cloud API dependencies.</p>
</div>
</details>

<details class="apple-faq-item">
<summary class="apple-faq-summary">
<span class="apple-faq-question">Is the project open source and available for commercial use?</span>
<span class="apple-faq-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg></span>
</summary>
<div class="apple-faq-body">
<p>Yes. Bank Statement Parser is dual-licensed under the Apache-2.0 and MIT open-source licenses. You can freely integrate it into commercial SaaS products, enterprise backends, and internal financial pipelines.</p>
</div>
</details>
</div>
</div>
</section>

<!-- SECTION 7: TAKE THE NEXT STEP -->
<section class="card-surface p-4 p-md-5 my-5 text-center" aria-label="Conversion Next Steps">
<h2 class="h2 fw-bold text-headline mb-3">Integrate High-Performance Statement Parsing Today</h2>
<p class="text-muted fs-5 mb-4 max-w-2xl mx-auto">Get started in minutes with the Rust CLI or Python package:</p>
<div class="d-flex justify-content-center gap-3 flex-wrap">
<a href="/getting-started/index.html" class="btn-primary-quantum">Install Bank Statement Parser →</a>
<a href="https://github.com/sebastienrousseau/bankstatementparser" target="_blank" rel="noopener noreferrer" class="btn-secondary-quantum">View on GitHub (Stars & Code) ↗</a>
<a href="/contact/index.html" class="btn-secondary-quantum">Contact for Custom Formats</a>
</div>
</section>
