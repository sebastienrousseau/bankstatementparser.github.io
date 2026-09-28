---
name: "Bank Statement Parser"
short_name: "bankstatementparser"
title: "Frequently Asked Questions (FAQ): Bank Statement Parser"
description: "Comprehensive technical answers regarding statement parsing throughput, zero-telemetry security, ISO 20022 schemas, and SDK deployment."
keywords: "bank statement parser FAQ, statement parser privacy, PDF statement extraction questions, ISO 20022 CAMT.053, MT940"
author: "Sebastien Rousseau"
date: "2026-09-01"
language: "en-GB"
layout: "faqs"
permalink: "https://bankstatementparser.com/faqs/index.html"
logo: "https://cloudcdn.pro/bankstatementparser/v1/logos/bankstatementparser.svg"
banner: "https://cloudcdn.pro/stocks/images/quantum-computer-room-1200.webp"
eyebrow: "Questions & Answers"
headline: "FAQs"
lead: "Comprehensive guidance covering specifications, zero-telemetry local execution, performance, and commercial licensing."
---

# Frequently Asked Questions

Comprehensive technical guidance covering high-throughput document parsing, zero-telemetry local execution, supported banking specifications, SDK integration, and enterprise compliance.

<div class="faq-container">
<div class="faq-search-box">
<span class="faq-search-icon" aria-hidden="true"></span>
<input type="search" class="faq-search-input" id="faqSearchInput" placeholder="Filter questions by keyword (e.g. OCR, Docker, ISO 20022, Python, Zero Telemetry)..." aria-label="Search frequently asked questions" />
</div>

<div class="faq-filter-pills" role="tablist" aria-label="FAQ Categories">
<button class="faq-pill active" data-filter="all" type="button">All Questions <span class="pill-count">16</span></button>
<button class="faq-pill" data-filter="architecture" type="button">Architecture &amp; Formats <span class="pill-count">4</span></button>
<button class="faq-pill" data-filter="security" type="button">Security &amp; Privacy <span class="pill-count">4</span></button>
<button class="faq-pill" data-filter="integration" type="button">Integration &amp; SDK <span class="pill-count">4</span></button>
<button class="faq-pill" data-filter="compliance" type="button">Compliance &amp; Enterprise <span class="pill-count">4</span></button>
</div>

<div class="faq-action-bar">
<span class="faq-count-label" id="faqCountLabel">Showing 16 of 16 questions</span>
<button type="button" class="faq-toggle-all-btn" id="faqToggleAllBtn" aria-expanded="false">
<span class="btn-text">Expand all</span>
<span class="chevron" aria-hidden="true"></span>
</button>
</div>

<div class="faq-list" id="faqList">
<details class="faq-card" data-category="architecture">
<summary class="faq-summary">
<span class="faq-question-wrap">
<span class="faq-category-badge">Architecture</span>
<span class="faq-question">How does Bank Statement Parser achieve sub-millisecond parsing throughput?</span>
</span>
<span class="faq-icon" aria-hidden="true"></span>
</summary>
<div class="faq-answer">
<p>Bank Statement Parser is engineered entirely in high-assurance native Rust with zero-copy stream processing, SIMD-accelerated string scanners, and direct memory layout mapping. By avoiding intermediate object allocations and skipping heavy browser engines or JVM runtimes, the tokenizer parses complex PDF text streams and multi-megabyte CSV files in under 0.8 ms per statement on standard multi-core hardware.</p>
</div>
</details>

<details class="faq-card" data-category="architecture">
<summary class="faq-summary">
<span class="faq-question-wrap">
<span class="faq-category-badge">Formats</span>
<span class="faq-question">Which bank statement standards and specifications are natively supported?</span>
</span>
<span class="faq-icon" aria-hidden="true"></span>
</summary>
<div class="faq-answer">
<p>The parser provides native, deterministic parsers for the primary banking standards worldwide:</p>
<ul>
<li><strong>PDF Statements:</strong> Digital PDF 1.4–2.0 native layout coordinate mapping and multi-column transaction extraction.</li>
<li><strong>CSV &amp; Delimited:</strong> RFC 4180 auto-detecting delimiters (comma, semicolon, tab), date ordering (DMY, MDY, YMD), and decimal notations.</li>
<li><strong>OFX / QFX:</strong> Open Financial Exchange SGML (1.x) and XML (2.x) banking and credit card formats.</li>
<li><strong>SWIFT MT940 / MT942:</strong> Tagged financial statement messages with field 61 sub-fields and balance reconciliation.</li>
<li><strong>ISO 20022 CAMT.053:</strong> XML cash management customer statement messages conforming to SEPA rulebooks.</li>
</ul>
</div>
</details>

<details class="faq-card" data-category="architecture">
<summary class="faq-summary">
<span class="faq-question-wrap">
<span class="faq-category-badge">Architecture</span>
<span class="faq-question">How are corrupted, malformed, or ambiguous statement entries handled?</span>
</span>
<span class="faq-icon" aria-hidden="true"></span>
</summary>
<div class="faq-answer">
<p>The engine implements strict deterministic error boundaries. When an ambiguous date format or corrupted record is encountered, the parser isolates the specific record rather than failing the entire document batch. It attaches a structured diagnostic warning to the output while verifying opening and closing balance arithmetic to alert compliance operators if amounts fail reconciliation.</p>
</div>
</details>

<details class="faq-card" data-category="architecture">
<summary class="faq-summary">
<span class="faq-question-wrap">
<span class="faq-category-badge">Formats</span>
<span class="faq-question">Does Bank Statement Parser support scanned paper statements using OCR?</span>
</span>
<span class="faq-icon" aria-hidden="true"></span>
</summary>
<div class="faq-answer">
<p>Yes. When compiled with the optional <code>--features ocr</code> flag, Bank Statement Parser leverages local, offline optical character recognition models. Scanned bitmap PDFs or image statements (TIFF, PNG) are converted to bounding-box coordinates and passed to the lexical tokenizer without transmitting any image data over the network.</p>
</div>
</details>

<details class="faq-card" data-category="security">
<summary class="faq-summary">
<span class="faq-question-wrap">
<span class="faq-category-badge">Security</span>
<span class="faq-question">Does Bank Statement Parser send financial documents or telemetry to remote servers?</span>
</span>
<span class="faq-icon" aria-hidden="true"></span>
</summary>
<div class="faq-answer">
<p><strong>Zero network egress, guaranteed.</strong> Bank Statement Parser is 100% self-contained and operates exclusively in local memory. It contains zero telemetry, zero analytics beacons, zero crash reporters, and zero background network calls. All document ingestion, tokenization, and schema validation execute strictly within your local process sandbox.</p>
</div>
</details>

<details class="faq-card" data-category="security">
<summary class="faq-summary">
<span class="faq-question-wrap">
<span class="faq-category-badge">Privacy</span>
<span class="faq-question">How can enterprise compliance teams verify zero-network egress in air-gapped environments?</span>
</span>
<span class="faq-icon" aria-hidden="true"></span>
</summary>
<div class="faq-answer">
<p>Security teams can verify our zero-egress guarantee through multiple standard controls: running the binary inside a network-isolated Linux namespace (<code>unshare -n</code>), deploying within a Docker container configured with <code>--network none</code>, or inspecting socket activity via <code>strace</code> / <code>lsof</code>. In all scenarios, zero socket binds or DNS resolutions occur.</p>
</div>
</details>

<details class="faq-card" data-category="security">
<summary class="faq-summary">
<span class="faq-question-wrap">
<span class="faq-category-badge">Security</span>
<span class="faq-question">Are bank statements or parsed transaction records cached or written to disk?</span>
</span>
<span class="faq-icon" aria-hidden="true"></span>
</summary>
<div class="faq-answer">
<p>No. Bank Statement Parser operates strictly in volatile memory. Statement byte buffers are allocated during stream processing and immediately scrubbed upon completion. No temporary files, swap caches, or intermediate scratch artifacts are written to persistent disk unless explicitly directed by the caller via the <code>--output</code> parameter.</p>
</div>
</details>

<details class="faq-card" data-category="security">
<summary class="faq-summary">
<span class="faq-question-wrap">
<span class="faq-category-badge">Supply Chain</span>
<span class="faq-question">How are release artifacts, dependencies, and SBOMs cryptographically verified?</span>
</span>
<span class="faq-icon" aria-hidden="true"></span>
</summary>
<div class="faq-answer">
<p>Every release includes a machine-readable CycloneDX Software Bill of Materials (SBOM) and SHA256 checksums recorded in <code>SHA256SUMS</code>. All Git release tags and binaries are signed using SSH maintainer keys published in <code>KEYS.asc</code>. You can verify any asset using <code>shasum -a 256 -c SHA256SUMS</code>.</p>
</div>
</details>

<details class="faq-card" data-category="integration">
<summary class="faq-summary">
<span class="faq-question-wrap">
<span class="faq-category-badge">Rust</span>
<span class="faq-question">How do I integrate Bank Statement Parser into an existing Rust application?</span>
</span>
<span class="faq-icon" aria-hidden="true"></span>
</summary>
<div class="faq-answer">
<p>Add the dependency to your <code>Cargo.toml</code>:</p>
<pre><code>[dependencies]&#10;bankstatementparser = &quot;0.0.2&quot;</code></pre>
<p>Then parse any statement file into strongly-typed structures:</p>
<pre><code>use bankstatementparser::Parser;&#10;use std::path::Path;&#10;fn main() -&gt; Result&lt;(), Box&lt;dyn std::error::Error&gt;&gt; {&#10;    let parser = Parser::new();&#10;    let statement = parser.parse_file(Path::new(&quot;statement.pdf&quot;))?;&#10;    println!(&quot;Account: {}, Balance: {}&quot;, statement.account_id, statement.closing_balance);&#10;    Ok(())&#10;}</code></pre>
</div>
</details>

<details class="faq-card" data-category="integration">
<summary class="faq-summary">
<span class="faq-question-wrap">
<span class="faq-category-badge">Python</span>
<span class="faq-question">Is there a native Python SDK, and does it require a local Rust toolchain?</span>
</span>
<span class="faq-icon" aria-hidden="true"></span>
</summary>
<div class="faq-answer">
<p>Pre-compiled binary wheels (compiled with PyO3 and Maturin) are distributed on PyPI for Linux, macOS (Apple Silicon and Intel), and Windows. No Rust compiler is required on your servers. Install via pip:</p>
<pre><code>pip install bankstatementparser</code></pre>
<p>And use it in Python:</p>
<pre><code>from bankstatementparser import parse_statement&#10;statement = parse_statement(&quot;statement.pdf&quot;)&#10;print(f&quot;Transactions parsed: {len(statement.transactions)}&quot;)</code></pre>
</div>
</details>

<details class="faq-card" data-category="integration">
<summary class="faq-summary">
<span class="faq-question-wrap">
<span class="faq-category-badge">Docker</span>
<span class="faq-question">Can I execute Bank Statement Parser as a containerized microservice or Docker image?</span>
</span>
<span class="faq-icon" aria-hidden="true"></span>
</summary>
<div class="faq-answer">
<p>Yes. Minimal, non-root container images are published on GitHub Container Registry. Mount your local statement directory to run extraction in an isolated container:</p>
<pre><code>docker run --rm -v $(pwd):/data ghcr.io/sebastienrousseau/bankstatementparser:latest --input /data/statement.pdf --format json</code></pre>
</div>
</details>

<details class="faq-card" data-category="integration">
<summary class="faq-summary">
<span class="faq-question-wrap">
<span class="faq-category-badge">Performance</span>
<span class="faq-question">How does parallel multi-threading scale across large statement directories?</span>
</span>
<span class="faq-icon" aria-hidden="true"></span>
</summary>
<div class="faq-answer">
<p>The CLI and SDK include a Rayon-based work-stealing parallel engine. Processing thousands of statement files scales linearly across available CPU threads without lock contention. Passing <code>--threads 8</code> allows 10,000 statements to be ingested, normalized, and validated in under 8.2 seconds.</p>
</div>
</details>

<details class="faq-card" data-category="compliance">
<summary class="faq-summary">
<span class="faq-question-wrap">
<span class="faq-category-badge">Licensing</span>
<span class="faq-question">Can Bank Statement Parser be embedded in commercial enterprise software?</span>
</span>
<span class="faq-icon" aria-hidden="true"></span>
</summary>
<div class="faq-answer">
<p>Yes. The project is dual-licensed under the <strong>Apache License 2.0</strong> and the <strong>MIT License</strong>. You are permitted to select either license, enabling full commercial use, private modification, and closed-source redistribution without copyleft obligations.</p>
</div>
</details>

<details class="faq-card" data-category="compliance">
<summary class="faq-summary">
<span class="faq-question-wrap">
<span class="faq-category-badge">ISO 20022</span>
<span class="faq-question">How does the validation engine verify ISO 20022 CAMT.053 schemas and balance proofs?</span>
</span>
<span class="faq-icon" aria-hidden="true"></span>
</summary>
<div class="faq-answer">
<p>During extraction, every account IBAN is verified against ISO 7064 Mod-97 checksums, and bank identifiers are validated against ISO 9362 BIC structures. The engine enforces double-entry arithmetic proofs (<code>Opening Balance + Credits - Debits == Closing Balance</code>). If a balance mismatch is detected, a deterministic reconciliation discrepancy record is emitted.</p>
</div>
</details>

<details class="faq-card" data-category="compliance">
<summary class="faq-summary">
<span class="faq-question-wrap">
<span class="faq-category-badge">Enterprise</span>
<span class="faq-question">Is custom bank statement dialect or bespoke layout template mapping supported?</span>
</span>
<span class="faq-icon" aria-hidden="true"></span>
</summary>
<div class="faq-answer">
<p>Yes. In addition to native parsers for major global banking institutions, Bank Statement Parser supports external YAML/JSON configuration files. Treasury teams can define custom table coordinates, regular expression transaction anchors, and date/currency mappings without modifying the underlying engine.</p>
</div>
</details>

<details class="faq-card" data-category="compliance">
<summary class="faq-summary">
<span class="faq-question-wrap">
<span class="faq-category-badge">Support</span>
<span class="faq-question">What enterprise support options, service level agreements (SLAs), and custom integrations are available?</span>
</span>
<span class="faq-icon" aria-hidden="true"></span>
</summary>
<div class="faq-answer">
<p>We provide institutional support agreements including custom bank dialect model training, prioritized issue response SLAs, dedicated security audit consultations, and bespoke ERP/TMS integration adapters. Inquire via our <a href="/contact/index.html">Contact Page</a>.</p>
</div>
</details>
</div>

<div class="faq-no-results" id="faqNoResults" role="status" aria-live="polite">
<div class="faq-no-results-icon" aria-hidden="true"></div>
<h2>No matching questions found</h2>
<p>Try searching for broader terms such as &ldquo;Docker&rdquo;, &ldquo;ISO 20022&rdquo;, &ldquo;Python&rdquo;, or &ldquo;OCR&rdquo;.</p>
<button type="button" class="faq-reset-btn" id="faqResetBtn">Reset search &amp; filters</button>
</div>

<div class="faq-help-card">
<div class="faq-help-icon" aria-hidden="true"></div>
<div class="faq-help-content">
<h2>Have a question not listed here?</h2>
<p>Our core engineering team and community stewards are available to assist. Explore the documentation guides, join our GitHub community discussions, or contact our solutions engineers directly.</p>
<div class="faq-help-actions">
<a href="/getting-started/index.html" class="primary">Getting Started Guide</a>
<a href="https://github.com/sebastienrousseau/bankstatementparser/discussions" class="secondary" target="_blank" rel="noopener">GitHub Discussions</a>
<a href="/contact/index.html" class="secondary">Contact Support</a>
</div>
</div>
</div>
</div>
