---
name: "Bank Statement Parser"
short_name: "bankstatementparser"
title: "Supported Statement Formats: PDF, CSV, OFX, MT940, CAMT"
description: "Detailed format specifications for supported financial documents including text PDF, delimited CSV, OFX 1.x/2.x, SWIFT MT940, and canonical ISO 20022 CAMT.053."
keywords: "PDF bank statement, OFX format, MT940 parser, CAMT.053 XML, bank statement CSV dialect"
author: "Sebastien Rousseau"
date: "2026-09-01"
language: "en-GB"
layout: "page"
permalink: "https://bankstatementparser.com/formats/index.html"
logo: "https://cloudcdn.pro/bankstatementparser/v1/logos/bankstatementparser.svg"
banner: "https://cloudcdn.pro/stocks/images/quantum-computer-room-1200.webp"
banner_alt: "Bank Statement Parser — High-Throughput Financial Document Parsing Engine"
eyebrow: "Specifications Matrix"
headline: "Supported Statement Formats & Specifications"
lead: "Multi-standard document ingestion with deterministic schema normalization across PDF, CSV, OFX, MT940, and CAMT.053."
---



Bank Statement Parser features multi-standard document ingestion with deterministic schema normalization.

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
<td><strong>PDF (Digital)</strong></td>
<td>Adobe PDF 1.4 – 2.0</td>
<td>Direct layout text stream tokenizer</td>
<td>Opening/Closing balance checksum</td>
</tr>
<tr>
<td><strong>CSV</strong></td>
<td>RFC 4180 & Dialect Auto-Detect</td>
<td>Header & delimiter statistical inference</td>
<td>Column type & date format verification</td>
</tr>
<tr>
<td><strong>OFX</strong></td>
<td>Open Financial Exchange (1.02 & 2.x)</td>
<td>SGML & XML tree parser</td>
<td>OFX standard banking DTD</td>
</tr>
<tr>
<td><strong>QIF</strong></td>
<td>Quicken Interchange Format</td>
<td>Line-oriented token parser</td>
<td>Transaction code validation</td>
</tr>
<tr>
<td><strong>SWIFT MT940 / MT942</strong></td>
<td>SWIFT Standards Release 2026</td>
<td>Tag-based state machine parser</td>
<td>SWIFT field 60F/62F balance validation</td>
</tr>
<tr>
<td><strong>ISO 20022 CAMT.053</strong></td>
<td>Bank-to-Customer Statement (camt.053.001.08)</td>
<td>Zero-copy XML streaming parser</td>
<td>W3C XML Schema (XSD)</td>
</tr>
</tbody>
</table>
</div>
