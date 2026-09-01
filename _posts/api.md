---
name: "Bank Statement Parser"
short_name: "bankstatementparser"
title: "API Reference: Rust Crate & Python Package"
description: "Complete API reference for bankstatementparser in Rust and Python with parameter definitions and code examples."
keywords: "bankstatementparser API, Rust banking API, Python statement parser SDK"
author: "Sebastien Rousseau"
date: "2026-09-01"
language: "en-GB"
layout: "page"
permalink: "https://bankstatementparser.com/api/index.html"
logo: "https://cloudcdn.pro/bankstatementparser/v1/logos/bankstatementparser.svg"
banner: "https://cloudcdn.pro/stocks/images/quantum-computer-room-1200.webp"
banner_alt: "Bank Statement Parser — High-Throughput Financial Document Parsing Engine"
---

# API Reference

Complete programmatic reference for integrating Bank Statement Parser into your application stack.

## Rust Crate (`bankstatementparser`)

```rust
use bankstatementparser::{Parser, Statement, Transaction};

let parser = Parser::builder()
    .detect_dialects(true)
    .strict_balance_validation(true)
    .build();

let statement: Statement = parser.parse_bytes(&pdf_bytes)?;
```

## Python SDK (`bankstatementparser`)

```python
from bankstatementparser import parse_statement, OutputFormat

# Parse directly from file path
statement = parse_statement("statement.pdf", format=OutputFormat.JSON)

# Access typed attributes
print(statement.account.iban)
print(statement.balances.closing)
for tx in statement.transactions:
    print(tx.date, tx.amount, tx.narrative)
```
