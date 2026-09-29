---
name: "Bank Statement Parser"
short_name: "bankstatementparser"
title: "API Reference: Rust Crate & Python SDK Guide"
description: "Complete API reference for Bank Statement Parser in Rust and Python with parameter schemas, zero-copy buffers, balance proofs, and transaction stream examples."
keywords: "bankstatementparser API, Rust banking API, Python statement parser SDK"
author: "Sebastien Rousseau"
date: "2026-09-01"
language: "en-GB"
layout: "page"
permalink: "https://bankstatementparser.com/api/index.html"
logo: "https://cloudcdn.pro/bankstatementparser/v1/logos/bankstatementparser.svg"
banner: "https://cloudcdn.pro/stocks/images/quantum-computer-room-1200.webp"
banner_alt: "Bank Statement Parser — High-Throughput Financial Document Parsing Engine"
eyebrow: "Developer Reference"
headline: "API & SDK Reference"
lead: "Complete programming interfaces, types, and error handling for Rust, Python, and CLI pipelines."
---

Bank Statement Parser exposes deterministic, zero-allocation interfaces across both native Rust and PyO3-powered Python bindings. Every function executes strictly in-process with zero network telemetry, complete memory safety, and mathematical balance verification.

<div class="step-item">
<div class="step-header">
<span class="step-badge">01</span>
<h2 class="step-title">Rust Core Library Interface (lib.rs)</h2>
</div>
<p>Integrate the native Rust crate directly into your backend services for maximum CPU throughput, sub-millisecond document parsing, and zero heap duplication:</p>

<div class="terminal-box my-3">
<div class="terminal-bar">
<span class="terminal-dot dot-red"></span>
<span class="terminal-dot dot-yellow"></span>
<span class="terminal-dot dot-green"></span>
<span class="terminal-title">rust — crate interface</span>
</div>
<div class="terminal-body">
<div class="t-line"><span class="t-key">use</span> bankstatementparser::{Parser, Statement, Transaction};</div>
<div class="t-line"><span class="t-key">use</span> std::path::Path;</div>
<div class="t-line">&nbsp;</div>
<div class="t-line"><span class="t-comment">&#35; Configure thread-safe parser with dialect auto-detection</span></div>
<div class="t-line"><span class="t-key">let</span> parser = Parser::builder()</div>
<div class="t-line">&nbsp;&nbsp;&nbsp;&nbsp;.detect_dialects(<span class="t-val">true</span>)</div>
<div class="t-line">&nbsp;&nbsp;&nbsp;&nbsp;.strict_balance_validation(<span class="t-val">true</span>)</div>
<div class="t-line">&nbsp;&nbsp;&nbsp;&nbsp;.build();</div>
<div class="t-line">&nbsp;</div>
<div class="t-line"><span class="t-comment">&#35; Parse byte stream directly from memory or disk</span></div>
<div class="t-line"><span class="t-key">let</span> statement: Statement = parser.parse_file(Path::new(<span class="t-val">&quot;statement.pdf&quot;</span>))?;</div>
<div class="t-line">&nbsp;</div>
<div class="t-line"><span class="t-comment">&#35; Access verified balance invariants and transactions</span></div>
<div class="t-line">println!(<span class="t-val">&quot;Account IBAN: {}&quot;</span>, statement.account_id);</div>
<div class="t-line">println!(<span class="t-val">&quot;Closing Balance: {} {}&quot;</span>, statement.closing_balance, statement.currency);</div>
<div class="t-line"><span class="t-key">for</span> tx <span class="t-key">in</span> statement.transactions {</div>
<div class="t-line">&nbsp;&nbsp;&nbsp;&nbsp;println!(<span class="t-val">&quot;{} | {:&gt;10.2} | {}&quot;</span>, tx.date, tx.amount, tx.description);</div>
<div class="t-line">}</div>
</div>
</div>

<p>Core data types provided by the native crate:</p>

<div class="table-responsive my-3">
<table class="visage-table">
<thead>
<tr>
<th>Type / Symbol</th>
<th>Signature</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>Parser</code></td>
<td><code>struct Parser</code></td>
<td>Thread-safe parser engine supporting zero-copy byte slice and file ingestion.</td>
</tr>
<tr>
<td><code>ParserBuilder</code></td>
<td><code>struct ParserBuilder</code></td>
<td>Configures parallel threads, balance invariants, and dialect heuristics.</td>
</tr>
<tr>
<td><code>Statement</code></td>
<td><code>struct Statement</code></td>
<td>Normalized document model containing account ID, balances, currency, and transactions.</td>
</tr>
<tr>
<td><code>Transaction</code></td>
<td><code>struct Transaction</code></td>
<td>Individual ledger item with booking date, value date, signed amount, and narrative.</td>
</tr>
<tr>
<td><code>StatementFormat</code></td>
<td><code>enum StatementFormat</code></td>
<td>Output target variants: <code>Json</code>, <code>Csv</code>, <code>Ofx</code>, <code>Qif</code>, and <code>Camt053</code>.</td>
</tr>
</tbody>
</table>
</div>
</div>

<div class="step-item">
<div class="step-header">
<span class="step-badge">02</span>
<h2 class="step-title">Python SDK Interface (PyO3)</h2>
</div>
<p>Pre-compiled binary wheels for Linux, macOS, and Windows provide native Rust speed directly inside Python data science, pandas, and web application workflows:</p>

<div class="terminal-box my-3">
<div class="terminal-bar">
<span class="terminal-dot dot-red"></span>
<span class="terminal-dot dot-yellow"></span>
<span class="terminal-dot dot-green"></span>
<span class="terminal-title">python — sdk quickstart</span>
</div>
<div class="terminal-body">
<div class="t-line"><span class="t-key">from</span> bankstatementparser <span class="t-key">import</span> parse_statement, parse_bytes, OutputFormat</div>
<div class="t-line">&nbsp;</div>
<div class="t-line"><span class="t-comment">&#35; Parse statement file directly into structured Python objects</span></div>
<div class="t-line">statement = parse_statement(<span class="t-val">&quot;statement.pdf&quot;</span>, format=OutputFormat.JSON)</div>
<div class="t-line">&nbsp;</div>
<div class="t-line"><span class="t-comment">&#35; Inspect normalized metadata and verified balances</span></div>
<div class="t-line">print(<span class="t-val">f&quot;Account Number: {statement.account_number}&quot;</span>)</div>
<div class="t-line">print(<span class="t-val">f&quot;Closing Balance: {statement.closing_balance} {statement.currency}&quot;</span>)</div>
<div class="t-line">&nbsp;</div>
<div class="t-line"><span class="t-comment">&#35; Iterate over strongly typed transaction records</span></div>
<div class="t-line"><span class="t-key">for</span> tx <span class="t-key">in</span> statement.transactions:</div>
<div class="t-line">&nbsp;&nbsp;&nbsp;&nbsp;print(<span class="t-val">f&quot;{tx.booking_date} | {tx.amount:&gt;10.2f} {statement.currency} | {tx.description}&quot;</span>)</div>
</div>
</div>

<p>High-level methods exported by the Python module:</p>

<div class="table-responsive my-3">
<table class="visage-table">
<thead>
<tr>
<th>Function / Attribute</th>
<th>Signature</th>
<th>Return Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>parse_statement</code></td>
<td><code>(path: str | Path, format: OutputFormat)</code></td>
<td><code>StatementRecord</code></td>
<td>Parses statement file on disk with dialect detection.</td>
</tr>
<tr>
<td><code>parse_bytes</code></td>
<td><code>(data: bytes, format: OutputFormat)</code></td>
<td><code>StatementRecord</code></td>
<td>Parses in-memory byte buffers from cloud storage or HTTP uploads.</td>
</tr>
<tr>
<td><code>OutputFormat</code></td>
<td><code>Enum: JSON, CSV, CAMT053, OFX</code></td>
<td><code>Enum</code></td>
<td>Specifies destination formatting dialect for output synthesis.</td>
</tr>
<tr>
<td><code>validate_invariants</code></td>
<td><code>(statement: StatementRecord)</code></td>
<td><code>bool</code></td>
<td>Validates arithmetic balance equation across all transaction items.</td>
</tr>
</tbody>
</table>
</div>
</div>

<div class="step-item">
<div class="step-header">
<span class="step-badge">03</span>
<h2 class="step-title">Deterministic Error Handling &amp; Diagnostics</h2>
</div>
<p>All processing pipelines isolate corrupt documents, unsupported regional dialects, and balance arithmetic discrepancies into typed error exceptions without panics or unhandled crashes:</p>

<div class="terminal-box my-3">
<div class="terminal-bar">
<span class="terminal-dot dot-red"></span>
<span class="terminal-dot dot-yellow"></span>
<span class="terminal-dot dot-green"></span>
<span class="terminal-title">python — error handling</span>
</div>
<div class="terminal-body">
<div class="t-line"><span class="t-key">from</span> bankstatementparser <span class="t-key">import</span> parse_statement</div>
<div class="t-line"><span class="t-key">from</span> bankstatementparser.exceptions <span class="t-key">import</span> (</div>
<div class="t-line">&nbsp;&nbsp;&nbsp;&nbsp;BalanceMismatchError,</div>
<div class="t-line">&nbsp;&nbsp;&nbsp;&nbsp;UnsupportedDialectError,</div>
<div class="t-line">&nbsp;&nbsp;&nbsp;&nbsp;CorruptedDocumentError,</div>
<div class="t-line">)</div>
<div class="t-line">&nbsp;</div>
<div class="t-line"><span class="t-key">try</span>:</div>
<div class="t-line">&nbsp;&nbsp;&nbsp;&nbsp;statement = parse_statement(<span class="t-val">&quot;statement.pdf&quot;</span>)</div>
<div class="t-line"><span class="t-key">except</span> BalanceMismatchError <span class="t-key">as</span> exc:</div>
<div class="t-line">&nbsp;&nbsp;&nbsp;&nbsp;<span class="t-comment">&#35; Arithmetic discrepancy: opening + sum(credits) - sum(debits) != closing</span></div>
<div class="t-line">&nbsp;&nbsp;&nbsp;&nbsp;print(<span class="t-val">f&quot;Audit failed: expected delta {exc.expected_delta}, found {exc.actual_delta}&quot;</span>)</div>
<div class="t-line"><span class="t-key">except</span> UnsupportedDialectError <span class="t-key">as</span> exc:</div>
<div class="t-line">&nbsp;&nbsp;&nbsp;&nbsp;<span class="t-comment">&#35; Document signature unrecognized</span></div>
<div class="t-line">&nbsp;&nbsp;&nbsp;&nbsp;print(<span class="t-val">f&quot;Unsupported bank layout: {exc.detected_signature}&quot;</span>)</div>
<div class="t-line"><span class="t-key">except</span> CorruptedDocumentError <span class="t-key">as</span> exc:</div>
<div class="t-line">&nbsp;&nbsp;&nbsp;&nbsp;print(<span class="t-val">f&quot;Malformed file stream: {exc.details}&quot;</span>)</div>
</div>
</div>
</div>

<div class="step-item">
<div class="step-header">
<span class="step-badge">04</span>
<h2 class="step-title">Zero-Telemetry Execution Guarantees</h2>
</div>
<p>Bank Statement Parser makes zero outbound network calls, transmits no analytical telemetry, and requires no external SaaS API keys. Sensitive financial documents and banking statements remain strictly confined within your own compute environment.</p>

<div class="doc-visual-card">
<picture>
<source media="(max-width: 40rem)" srcset="https://cloudcdn.pro/stocks/images/quantum-computer-room-320.webp 320w, https://cloudcdn.pro/stocks/images/quantum-computer-room-640.webp 640w, https://cloudcdn.pro/stocks/images/quantum-computer-room-1200.webp 1200w" sizes="100vw">
<img src="https://cloudcdn.pro/stocks/images/quantum-computer-room-1200.webp" alt="Air-gapped high-throughput financial document engineering architecture" width="1200" height="675" loading="lazy" />
</picture>
<div class="doc-visual-caption">Air-gapped execution architecture: banking statements are tokenized and validated entirely within local memory with zero external telemetry.</div>
</div>
</div>
