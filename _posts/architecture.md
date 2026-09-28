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
banner: "https://cloudcdn.pro/stocks/images/modern-corporate-office-with-technological-displays-1200.webp"
banner_alt: "Bank Statement Parser — Pipeline Architecture & High-Throughput Execution"
eyebrow: "Engine Internals"
headline: "Architecture & Pipeline Specifications"
lead: "High-throughput tokenization, deterministic stream parsing, and ISO 20022 message synthesis with zero runtime allocations."
---

Bank Statement Parser is architected around a deterministic, four-stage extraction and validation pipeline. Every stage executes in-process with zero outbound telemetry, zero heap allocation in the critical path, and strict mathematical balance verification before emitting ISO 20022 messages.

<h2>Four-Stage Processing Pipeline</h2>

<div class="process-grid my-4">
<article>
<b>01</b>
<h3>Stream Ingest</h3>
<p>Zero-copy memory mapping (<code>mmap</code>) of input statement bytes with instant magic-byte format detection (PDF, CSV, OFX, MT940, CAMT.053).</p>
<small>&lt; 0.2 ms Ingest Latency</small>
</article>
<article>
<b>02</b>
<h3>Layout Tokenizer</h3>
<p>Spatial coordinate mapping and multi-column tabular boundary reconstruction, preserving text flow across complex multi-page financial tables.</p>
<small>Zero Heap Allocations</small>
</article>
<article>
<b>03</b>
<h3>Field Normalizer</h3>
<p>Canonical standardization of 24 global date dialects, ISO 4217 currencies, and mod-97 IBAN checksum verification.</p>
<small>ISO 20022 BTC Mapping</small>
</article>
<article>
<b>04</b>
<h3>Schema Validator</h3>
<p>Mathematical invariant verification (<code>Opening + ΣCredits - ΣDebits = Closing</code>) before emitting validated JSON or ISO 20022 XML.</p>
<small>100% Invariant Check</small>
</article>
</div>

<h2>Deterministic Pipeline Execution Trace</h2>

<p>The trace below demonstrates the sub-millisecond execution lifecycle of the four-stage engine processing a multi-page PDF statement into validated ISO 20022 CAMT.053 XML:</p>

<div class="terminal-box my-4">
<div class="terminal-bar">
<span class="terminal-dot dot-red"></span>
<span class="terminal-dot dot-yellow"></span>
<span class="terminal-dot dot-green"></span>
<span class="terminal-title">pipeline-trace — bankstatementparser v0.0.2</span>
</div>
<div class="terminal-body">
<div class="t-line"><span class="t-prompt">$</span>bankstatementparser --input statement.pdf --trace --format camt053</div>
<div class="t-line"><span class="t-comment">[0.00ms] [ingest] Zero-copy mmap statement.pdf (142,896 bytes) • Magic: %PDF-1.7</span></div>
<div class="t-line"><span class="t-comment">[0.18ms] [tokenizer] Spatial scan complete: 4 tables detected, 128 transaction rows clustered</span></div>
<div class="t-line"><span class="t-comment">[0.45ms] [normalizer] Currency: GBP (ISO 4217) • Account: GB29BARC20000012345678 (mod-97 OK)</span></div>
<div class="t-line"><span class="t-comment">[0.72ms] [validator] Opening: 14,250.00 | Credits: +8,300.50 | Debits: -3,120.25 | Closing: 19,430.25</span></div>
<div class="t-line"><span class="t-comment">[0.89ms] [validator] Invariant Check: 14,250.00 + 5,180.25 == 19,430.25 [PASS: Delta = 0.0000]</span></div>
<div class="t-line"><span class="t-comment">[1.12ms] [synthesis] Emitted ISO 20022 camt.053.001.08 XML (42,810 bytes, schema valid)</span></div>
<div class="t-line"><span class="t-key">Status:</span> <span class="t-val">200 OK</span> • <span class="t-key">Latency:</span> <span class="t-val">1.12ms</span> • <span class="t-key">Memory:</span> <span class="t-val">1.4 MB</span> • <span class="t-key">Telemetry:</span> <span class="t-val">Zero Outbound</span></div>
</div>
</div>

<h2>Stage 1: Zero-Copy Stream Ingestion</h2>

<p>The ingestion subsystem interfaces directly with the host filesystem via memory-mapped files (<code>mmap</code>), bypassing kernel-to-userspace buffer duplication. Byte slices are analyzed using non-backtracking magic-byte sniffers:</p>

<ul>
<li><strong>PDF Documents:</strong> Validates file header prefix <code>%PDF-</code> and reads the cross-reference table (<code>xref</code>) directly from the trailer offset.</li>
<li><strong>OFX Streams:</strong> Sniffs <code>OFXHEADER</code> SGML tags or XML prologue <code>&lt;?xml version="1.0"</code> to branch into streaming parser trees.</li>
<li><strong>SWIFT MT940 / MT942:</strong> Checks for field delimiter sequences (<code>:20:</code>, <code>:25:</code>, <code>:28C:</code>) to route into deterministic line tokenizers.</li>
<li><strong>CSV Delimited Files:</strong> Evaluates entropy across candidate delimiters (comma, semicolon, tab, pipe) over the first 50 rows to infer column geometry without full-file scans.</li>
</ul>

<h2>Stage 2: Spatial Layout Tokenization</h2>

<p>For unstructured formats such as digital PDF statements, standard text extraction destroys critical vertical alignment. Bank Statement Parser utilizes a deterministic coordinate-clustering engine:</p>

<ul>
<li><strong>Glyph Extraction:</strong> Maps character matrices, font bounding boxes, and baseline coordinates from content stream operators (<code>BT</code>, <code>ET</code>, <code>Tj</code>, <code>TJ</code>, <code>Tm</code>).</li>
<li><strong>Row Clustering:</strong> Groups glyphs with overlapping vertical tolerances into discrete lines, preventing footnote and header collision.</li>
<li><strong>Column Geometric Alignment:</strong> Computes vertical whitespace gutters to delineate Booking Date, Value Date, Narrative, Amount, and Running Balance columns.</li>
<li><strong>Multi-line Narrative Stitching:</strong> Heuristically associates wrapped description text back to the initiating transaction row.</li>
</ul>

<figure class="my-4">
<img src="https://cloudcdn.pro/stocks/images/modern-corporate-office-with-technological-displays-1200.webp" alt="Bank Statement Parser — Pipeline Architecture and High-Throughput Engine" width="1200" height="600" style="width:100%; height:auto; border-radius:8px; border:1px solid var(--vi-line);" />
<figcaption class="text-center mt-2 text-muted"><small>High-assurance statement parsing: zero-copy memory mapping, deterministic tokenization, and ISO 20022 message synthesis.</small></figcaption>
</figure>

<h2>Stage 3: Field Normalization &amp; Standard Mapping</h2>

<p>Extracted raw string tokens are converted into strongly-typed canonical primitives:</p>

<ul>
<li><strong>Date Canonicalization:</strong> Resolves 24 regional date formats (including <code>DD/MM/YYYY</code>, <code>MM/DD/YYYY</code>, <code>YYYY-MM-DD</code>, and multi-lingual month names) into ISO 8601 UTC timestamps.</li>
<li><strong>Monetary Amounts:</strong> Parses European period/comma inversion (e.g., <code>1.234,56</code> vs <code>1,234.56</code>), preserving scale as exact 64-bit fixed-point integers to eliminate IEEE 754 floating-point rounding drift.</li>
<li><strong>Account &amp; Bank Identifiers:</strong> Verifies ISO 13616 International Bank Account Numbers (IBAN) using mod-97 arithmetic (ISO 7064) and validates ISO 9362 Business Identifier Codes (BIC).</li>
<li><strong>Transaction Code Classification:</strong> Maps proprietary transaction labels to standardized ISO 20022 Bank Transaction Codes (BTC), distinguishing card settlements, direct debits, credit transfers, and fee deductions.</li>
</ul>

<h2>Stage 4: Mathematical Validation &amp; Schema Synthesis</h2>

<p>Before any extracted statement is emitted, the engine evaluates strict balance invariants to guarantee data integrity:</p>

<div class="terminal-box my-4">
<div class="terminal-bar">
<span class="terminal-dot dot-red"></span>
<span class="terminal-dot dot-yellow"></span>
<span class="terminal-dot dot-green"></span>
<span class="terminal-title">mathematical-invariant — balance check</span>
</div>
<div class="terminal-body">
<div class="t-line"><span class="t-key">Invariant Equation:</span> Opening_Balance + Sum(Credits) - Sum(Debits) == Closing_Balance</div>
<div class="t-line"><span class="t-comment">&#35; If Delta != 0.00, extraction fails with explicit discrepancy error and line offset</span></div>
</div>
</div>

<p>Upon invariant satisfaction, the engine streams the normalized data tree into target schemas:</p>

<ul>
<li><strong>ISO 20022 CAMT.053:</strong> Generates conforming <code>camt.053.001.08</code> Bank-to-Customer Statement XML messages ready for direct core banking and treasury ingest.</li>
<li><strong>Canonical JSON:</strong> Emits clean, strongly-typed JSON with ISO 8601 dates and exact decimal numbers for downstream API consumption.</li>
<li><strong>Reconciliation CSV:</strong> Serializes standardized transaction rows with consistent column headers for enterprise ERP systems.</li>
</ul>
