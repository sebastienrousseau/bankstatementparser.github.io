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
---

# Getting Started with Bank Statement Parser

Bank Statement Parser is distributed as a standalone command-line binary (CLI), a high-assurance Rust crate, and a native Python package.

## 1. Installation

### Option A: Install via Cargo (Rust)
```bash
cargo install bankstatementparser
```

### Option B: Install via Pip (Python)
```bash
pip install bankstatementparser
```

### Option C: Run via Docker
```bash
docker pull ghcr.io/sebastienrousseau/bankstatementparser:latest
docker run --rm -v $(pwd):/data ghcr.io/sebastienrousseau/bankstatementparser:latest --input /data/statement.pdf
```

---

## 2. Command Line Interface (CLI) Usage

### Parse a Single Statement
```bash
# Extract to standard JSON
bankstatementparser --input statement.pdf --output statement.json

# Extract to CSV
bankstatementparser --input statement.ofx --output statement.csv --format csv

# Extract to ISO 20022 CAMT.053 XML
bankstatementparser --input statement.pdf --output statement.xml --format camt053
```

### Batch Directory Processing
```bash
# Process all PDFs in a directory using multi-core parallel extraction
bankstatementparser --batch-dir ./statements/ --output-dir ./extracted_json/ --threads 8
```

---

## 3. Rust Library Integration

Add the dependency to your `Cargo.toml`:
```toml
[dependencies]
bankstatementparser = "0.0.1"
```

Parse in Rust:
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

---

## 4. Python SDK Usage

```python
from bankstatementparser import parse_statement

statement = parse_statement("statement.pdf")

print(f"Account: {statement.account_number}")
print(f"Closing Balance: {statement.closing_balance} {statement.currency}")

for tx in statement.transactions:
    print(f"{tx.booking_date} | {tx.amount} | {tx.description}")
```
