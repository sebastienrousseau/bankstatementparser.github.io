---
name: "Bank Statement Parser"
short_name: "bankstatementparser"
title: "Supported Statement Formats: PDF, CSV, OFX, MT940, CAMT, BAI2"
description: "Comprehensive format specifications for 8 structured financial formats: CAMT (052/053/054), PAIN.001, MT940, MT942, OFX/QFX, BAI2, CSV, and PDF statements."
keywords: "PDF bank statement, BAI2 parser, ISO 20022 CAMT.053, PAIN.001 credit transfer, SWIFT MT940 MT942, OFX QFX, Apache Parquet export"
author: "Sebastien Rousseau"
date: "2026-10-10"
language: "en-GB"
layout: "page"
permalink: "https://bankstatementparser.com/formats/index.html"
logo: "https://cloudcdn.pro/bankstatementparser/v1/logos/bankstatementparser.svg"
banner: "https://cloudcdn.pro/stocks/images/quantum-computer-room-1200.webp"
banner_alt: "Bank Statement Parser — High-Throughput Financial Document Parsing Engine"
eyebrow: "Specifications Matrix"
headline: "Supported Statement Formats & Specifications"
lead: "Deterministic multi-standard document ingestion with automated schema normalization across 8 financial formats, Parquet streaming, and ledger exports."
---

Bank Statement Parser provides deterministic, zero-telemetry ingestion and mathematical balance verification across eight primary banking standards worldwide. Every format is normalized into strongly-typed `Transaction` and `Statement` models ready for ERP integration, corporate treasury, automated reconciliation, and OLAP analytics.

<div class="table-responsive my-4">
<table class="visage-table">
<thead>
<tr>
<th>Format</th>
<th>Standard / Specification</th>
<th>Extraction Method</th>
<th>Validation Engine</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>PDF Statements</strong></td>
<td>Adobe PDF 1.4–2.0 (Vector &amp; Scanned)</td>
<td>Spatial coordinate tokenizer &amp; local OCR/vision fallback</td>
<td>Mathematical balance verification &amp; IBAN Mod-97 checksum</td>
</tr>
<tr>
<td><strong>CSV &amp; Delimited</strong></td>
<td>RFC 4180 with Dialect Auto-Detect</td>
<td>Statistical delimiter, decimal, and date header inference</td>
<td>Column type inference &amp; date format normalization</td>
</tr>
<tr>
<td><strong>BAI2 Cash Management</strong></td>
<td>Bank Administration Institute (BAI2)</td>
<td>Deterministic record state machine (Records 01–99)</td>
<td>Account status balance codes &amp; record 88 continuation validation</td>
</tr>
<tr>
<td><strong>SWIFT MT940</strong></td>
<td>SWIFT Standards Release 2026 (End-of-Day)</td>
<td>Tag-based state machine parser (:20:, :25:, :60F:, :61:, :62F:)</td>
<td>Opening/closing balance arithmetic (Fields 60F/62F)</td>
</tr>
<tr>
<td><strong>SWIFT MT942</strong></td>
<td>SWIFT Standards Release 2026 (Interim)</td>
<td>Intraday credit/debit transaction stream parser</td>
<td>Field 34F floor limit &amp; summary amount reconciliation</td>
</tr>
<tr>
<td><strong>ISO 20022 CAMT</strong></td>
<td>camt.052, camt.053, and camt.054 (v2–v12)</td>
<td>Zero-copy XML streaming parser</td>
<td>W3C XML Schema (XSD) &amp; opening/closing balance proofs</td>
</tr>
<tr>
<td><strong>ISO 20022 PAIN.001</strong></td>
<td>pain.001.001.03–11 (Customer Credit Transfer)</td>
<td>Deterministic XML payment initiation parser</td>
<td>Payment control sum &amp; transaction count verification</td>
</tr>
<tr>
<td><strong>OFX &amp; Quicken QFX</strong></td>
<td>Open Financial Exchange (1.02–2.2 SGML &amp; XML)</td>
<td>Robust tree parser with SGML unclosed-tag repair</td>
<td>Standard banking DTD &amp; transaction UID deduplication</td>
</tr>
</tbody>
</table>
</div>

<h2>1. ISO 20022 Messaging Standard (CAMT &amp; PAIN.001)</h2>

<p>ISO 20022 is the global standard for electronic data interchange between financial institutions. Bank Statement Parser supports canonical cash management messages (CAMT) and payment initiation instructions (PAIN.001) across all published versions (v2 through v12):</p>

<ul>
<li><strong>CAMT.053 (Bank-to-Customer Statement):</strong> Detailed end-of-day electronic account statement reporting opening balance, booked entries, batches, and closing available balance.</li>
<li><strong>CAMT.052 (Bank-to-Customer Account Report):</strong> Intraday or interim statement providing real-time cash position updates.</li>
<li><strong>CAMT.054 (Bank-to-Customer Debit/Credit Notification):</strong> Granular transaction-level debit or credit notifications used for instant settlement verification.</li>
<li><strong>PAIN.001 (Customer Credit Transfer Initiation):</strong> Payment instructions parsed for two-way automated reconciliation against incoming CAMT or MT940 statement postings.</li>
</ul>

<h2>2. SWIFT Telecommunication Formats (MT940 &amp; MT942)</h2>

<p>The parser provides native tag-based state machines for legacy SWIFT MT formats without reliance on regular expressions:</p>

<ul>
<li><strong>SWIFT MT940:</strong> The electronic bank statement message containing field :20: (Transaction Reference), :25: (Account Identification), :28C: (Statement/Sequence Number), :60F: (Opening Balance), :61: (Statement Line), :86: (Information to Account Owner), and :62F: (Closing Balance).</li>
<li><strong>SWIFT MT942:</strong> Interim transaction report tracking intraday movements with field :34F: minimum amount specification.</li>
<li><strong>Structured Field :86: Sub-Tag Parser:</strong> Automated extraction of German SEPA, EPC, and international structured tags including <code>/EREF/</code> (End-to-End Reference), <code>/PREF/</code> (Payment Reference), <code>/REMI/</code> (Remittance Info), <code>/IBAN/</code>, and <code>/BIC/</code>.</li>
</ul>

<h2>3. BAI2 Corporate Cash Management</h2>

<p>BAI2 is the North American standard created by the Bank Administration Institute for corporate account reporting. Bank Statement Parser deterministically parses the hierarchical record sequence:</p>

<ul>
<li><strong>Record 01:</strong> File Header (sender, receiver, creation date/time, file ID).</li>
<li><strong>Record 02:</strong> Group Header (ultimate receiver, originator, group status).</li>
<li><strong>Record 03:</strong> Account Identifier (account number, currency, type codes, status amounts).</li>
<li><strong>Record 16:</strong> Transaction Detail (type code, amount, funds availability, bank reference).</li>
<li><strong>Record 88:</strong> Continuation Record (extended remittance and transaction descriptions).</li>
<li><strong>Records 49, 98, 99:</strong> Account, Group, and File Trailer checksums ensuring zero record omission.</li>
</ul>

<h2>4. Open Financial Exchange (OFX &amp; QFX)</h2>

<p>Open Financial Exchange (OFX) and Quicken Financial Exchange (QFX) formats are widely used by retail and commercial banks across North America and Europe:</p>

<ul>
<li><strong>OFX 1.02–1.6:</strong> SGML-based format with unclosed tags and legacy header key-value blocks. The parser repairs malformed SGML tag hierarchies without memory buffering overhead.</li>
<li><strong>OFX 2.x:</strong> Clean W3C XML documents containing <code>BANKMSGSRSV1</code>, <code>STMTTRNRS</code>, and <code>STMTRS</code> aggregates.</li>
<li><strong>Transaction Deduplication:</strong> Unique <code>FITID</code> (Financial Institution Transaction ID) hashing prevents duplicate booking entries during multi-account batch ingestion.</li>
</ul>

<h2>5. Delimited CSV Statements</h2>

<p>CSV is the most ubiquitous yet least standardized financial format. Bank Statement Parser implements a statistical dialect inference engine that automatically determines:</p>

<ul>
<li><strong>Delimiter Detection:</strong> Comma (<code>,</code>), semicolon (<code>;</code>), tab (<code>\t</code>), or pipe (<code>|</code>).</li>
<li><strong>Date Formatting:</strong> ISO 8601 (<code>YYYY-MM-DD</code>), European (<code>DD/MM/YYYY</code>), and US (<code>MM/DD/YYYY</code>) formats inferred from semantic date distributions.</li>
<li><strong>Number &amp; Currency Notation:</strong> Automatic handling of periods vs. commas for thousand separators and decimal points (e.g. <code>1,234.56</code> vs. <code>1.234,56</code>).</li>
<li><strong>Amount Semantics:</strong> Automatic detection of unified signed amount columns or split Debit / Credit column layouts.</li>
</ul>

<h2>6. Digital and Scanned PDF Statements</h2>

<p>Financial institutions frequently deliver statements in PDF format. Bank Statement Parser provides a dual-mode engine for complete document recovery:</p>

<ul>
<li><strong>Digital / Vector PDFs:</strong> High-speed extraction directly from internal text streams and spatial coordinates, preserving table columns across multi-page boundaries with sub-millisecond execution.</li>
<li><strong>Scanned Image Statements:</strong> Optional local, offline OCR and vision fallback models parse bitmap PDFs (TIFF, PNG, scanned documents) into layout-aware bounding boxes without sending a single byte outside your private network.</li>
<li><strong>Forensics &amp; Tamper Verification:</strong> Automated PDF forensics check for font anomalies, metadata discrepancies, and hidden modification layers to detect altered statements.</li>
</ul>

<h2>7. Analytical &amp; Accounting Export Targets</h2>

<p>In addition to strongly-typed JSON and CSV, Bank Statement Parser supports industrial streaming analytics and plain-text accounting ledger pipelines:</p>

<ul>
<li><strong>Streaming Apache Parquet (<code>ParquetStreamWriter</code>):</strong> High-performance, columnar Parquet export with snappy or zstd compression. Supports streaming hundreds of thousands of transactions directly to disk or S3 with constant memory usage.</li>
<li><strong>Plain-Text Accounting (PTA):</strong> Native export formats for <code>hledger</code>, <code>beancount</code>, and <code>ledger-cli</code> double-entry bookkeeping systems.</li>
<li><strong>Pandas &amp; Polars DataFrames:</strong> Zero-copy integration into Polars and Pandas analytics pipelines via <code>bankstatementparser[parquet]</code> and <code>bankstatementparser[polars]</code> extras.</li>
</ul>
