---
name: "Bank Statement Parser"
short_name: "bankstatementparser"
title: "Getting Started with Bank Statement Parser: Installation & Quickstart"
description: "Installation instructions for Rust (Cargo), Python (Pip), Homebrew, and Docker alongside step-by-step CLI and API quickstarts."
keywords: "install bank statement parser, cargo bankstatementparser, pip bankstatementparser, CLI bank statement parser"
author: "Sebastien Rousseau"
date: "2026-09-01"
language: "en-GB"
layout: "page"
permalink: "https://bankstatementparser.com/getting-started/index.html"
logo: "https://cloudcdn.pro/bankstatementparser/v1/logos/bankstatementparser.svg"
banner: "https://cloudcdn.pro/stocks/images/quantum-computer-room-1200.webp"
banner_alt: "Bank Statement Parser — High-Throughput Financial Document Parsing Engine"
eyebrow: "Installation & Guide"
headline: "Getting Started with Bank Statement Parser"
lead: "Installation instructions for Rust, Python, Docker, and CLI alongside step-by-step extraction quickstarts."
---

Bank Statement Parser is an open-source, high-throughput financial document engine engineered in Rust with native Python bindings. Follow this guide to install the binary, process multi-format statement documents, or embed the SDK directly into your application stack.

<div class="install-grid">
<div class="install-card">
<div class="install-card-header">
<h2 class="install-card-title">Rust (Cargo)</h2>
<span class="install-card-tag">Crate v0.0.2</span>
</div>
<p class="install-card-desc">Native library integration and standalone CLI compiled directly from source for maximum CPU throughput.</p>
<pre><code>cargo install bankstatementparser</code></pre>
</div>

<div class="install-card">
<div class="install-card-header">
<h2 class="install-card-title">Python (Pip)</h2>
<span class="install-card-tag">PyPI Wheels</span>
</div>
<p class="install-card-desc">Pre-compiled PyO3 binary wheels for Linux, macOS (Apple Silicon and Intel), and Windows with zero compiler setup.</p>
<pre><code>pip install bankstatementparser</code></pre>
</div>

<div class="install-card">
<div class="install-card-header">
<h2 class="install-card-title">Docker Engine</h2>
<span class="install-card-tag">OCI Container</span>
</div>
<p class="install-card-desc">Minimal, non-root container image published on GitHub Container Registry for air-gapped CI/CD execution.</p>
<pre><code>docker pull ghcr.io/sebastienrousseau/bankstatementparser:latest</code></pre>
</div>

<div class="install-card">
<div class="install-card-header">
<h2 class="install-card-title">Homebrew Tap</h2>
<span class="install-card-tag">macOS &amp; Linux</span>
</div>
<p class="install-card-desc">Pre-built standalone CLI binary distributed via official Homebrew tap for immediate terminal workstation access.</p>
<pre><code>brew install sebastienrousseau/tap/bankstatementparser</code></pre>
</div>
</div>

<div class="step-item">
<div class="step-header">
<span class="step-badge">01</span>
<h2 class="step-title">Command Line Interface (CLI) Extraction</h2>
</div>
<p>The standalone binary provides fast parsing for individual bank statement files across digital PDF, CSV, OFX, and QIF formats, emitting standard JSON, CSV, or ISO 20022 CAMT.053 XML:</p>

```bash
# Extract statement PDF to standard JSON
bankstatementparser --input statement.pdf --output statement.json

# Convert OFX banking file to CSV
bankstatementparser --input statement.ofx --output statement.csv --format csv

# Transform PDF statement into ISO 20022 CAMT.053 XML
bankstatementparser --input statement.pdf --output statement.xml --format camt053
```

<p>For high-volume transaction processing, enable multi-threaded batch ingestion to parse entire directories in parallel:</p>

```bash
# Process all statements in a directory using 8 parallel worker threads
bankstatementparser --batch-dir ./statements/ --output-dir ./extracted_json/ --threads 8
```
</div>

<div class="step-item">
<div class="step-header">
<span class="step-badge">02</span>
<h2 class="step-title">Rust Library Integration</h2>
</div>
<p>Add the dependency to your <code>Cargo.toml</code>:</p>

```toml
[dependencies]
bankstatementparser = "0.0.2"
```

<p>Parse any statement into strongly-typed transaction structs with compile-time memory safety:</p>

```rust
use bankstatementparser::{Parser, StatementFormat};
use std::path::Path;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let parser = Parser::new();
    let statement = parser.parse_file(Path::new("statement.pdf"))?;

    println!("Account: {}", statement.account_id);
    println!("Balance: {} {}", statement.closing_balance, statement.currency);

    for tx in statement.transactions {
        println!("{} | {} | {}", tx.date, tx.amount, tx.description);
    }

    Ok(())
}
```
</div>

<div class="step-item">
<div class="step-header">
<span class="step-badge">03</span>
<h2 class="step-title">Python SDK Integration</h2>
</div>
<p>Extract and validate transaction records within your Python data science and finance workflows with zero native compilation:</p>

```python
from bankstatementparser import parse_statement

# Extract statements directly into typed Python objects
statement = parse_statement("statement.pdf")

print(f"Account: {statement.account_number}")
print(f"Closing Balance: {statement.closing_balance} {statement.currency}")

for tx in statement.transactions:
    print(f"{tx.booking_date} | {tx.amount} | {tx.description}")
```
</div>

<div class="step-item">
<div class="step-header">
<span class="step-badge">04</span>
<h2 class="step-title">Zero-Telemetry Execution Guarantees</h2>
</div>
<p>Every extraction pipeline executes exclusively within local process memory. Bank Statement Parser makes zero outbound network calls, transmits no analytical telemetry, and requires no external SaaS API keys:</p>

<div class="doc-visual-card">
<picture>
<source media="(max-width: 40rem)" srcset="https://cloudcdn.pro/stocks/images/quantum-computer-room-320.webp 320w, https://cloudcdn.pro/stocks/images/quantum-computer-room-640.webp 640w, https://cloudcdn.pro/stocks/images/quantum-computer-room-1200.webp 1200w" sizes="100vw">
<img src="https://cloudcdn.pro/stocks/images/quantum-computer-room-1200.webp" alt="High-throughput financial document engineering architecture" width="1200" height="675" loading="lazy" />
</picture>
<div class="doc-visual-caption">Air-gapped execution architecture: banking statements are tokenized and validated entirely within local memory with zero external telemetry.</div>
</div>
</div>
