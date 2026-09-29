---
name: "Bank Statement Parser"
short_name: "bankstatementparser"
title: "Contributing Guide: Code Standards & Testing"
description: "Contributor guidelines for Bank Statement Parser covering Rust code conventions, mod-97 sample data verification, DCO signoffs, and automated test execution."
keywords: "contribute bank statement parser, open source financial contribution"
author: "Sebastien Rousseau"
date: "2026-09-01"
language: "en-GB"
layout: "page"
permalink: "https://bankstatementparser.com/contributing/index.html"
logo: "https://cloudcdn.pro/bankstatementparser/v1/logos/bankstatementparser.svg"
banner: "https://cloudcdn.pro/stocks/images/quantum-computer-room-1200.webp"
banner_alt: "Bank Statement Parser — High-Throughput Financial Document Parsing Engine"
eyebrow: "Community & Code"
headline: "Contributing to Bank Statement Parser"
lead: "Guidelines for bug reporting, code contributions, DCO sign-offs, and test-driven verification."
---

Thank you for your interest in contributing to Bank Statement Parser. We welcome contributions for new regional statement dialects, zero-copy performance optimizations, parser rulebook definitions, and documentation improvements.

<div class="step-item">
<div class="step-header">
<span class="step-badge">01</span>
<h2 class="step-title">Local Development Environment Setup</h2>
</div>
<p>Bank Statement Parser is built in Rust with companion Python bindings. Ensure you have the stable Rust toolchain and Python 3.10+ installed:</p>

<div class="terminal-box my-3">
<div class="terminal-bar">
<span class="terminal-dot dot-red"></span>
<span class="terminal-dot dot-yellow"></span>
<span class="terminal-dot dot-green"></span>
<span class="terminal-title">bash — clone &amp; setup</span>
</div>
<div class="terminal-body">
<div class="t-line"><span class="t-comment">&#35; Fork and clone repository</span></div>
<div class="t-line"><span class="t-prompt">$</span>git clone https://github.com/YOUR_USERNAME/bankstatementparser.git</div>
<div class="t-line"><span class="t-prompt">$</span>cd bankstatementparser</div>
<div class="t-line">&nbsp;</div>
<div class="t-line"><span class="t-comment">&#35; Build debug binary</span></div>
<div class="t-line"><span class="t-prompt">$</span>cargo build</div>
</div>
</div>
</div>

<div class="step-item">
<div class="step-header">
<span class="step-badge">02</span>
<h2 class="step-title">Test-Driven Verification &amp; Invariants</h2>
</div>
<p>Every pull request must pass the automated test suite, clippy linter checks, and formatting verification. 100% test coverage on new parsing dialects is required:</p>

<div class="terminal-box my-3">
<div class="terminal-bar">
<span class="terminal-dot dot-red"></span>
<span class="terminal-dot dot-yellow"></span>
<span class="terminal-dot dot-green"></span>
<span class="terminal-title">bash — test suite</span>
</div>
<div class="terminal-body">
<div class="t-line"><span class="t-comment">&#35; Execute full test suite across all dialects</span></div>
<div class="t-line"><span class="t-prompt">$</span>cargo test</div>
<div class="t-line">&nbsp;</div>
<div class="t-line"><span class="t-comment">&#35; Run strict Clippy linter with all features enabled</span></div>
<div class="t-line"><span class="t-prompt">$</span>cargo clippy --all-targets --all-features -- -D warnings</div>
<div class="t-line">&nbsp;</div>
<div class="t-line"><span class="t-comment">&#35; Verify formatting conforms to rustfmt</span></div>
<div class="t-line"><span class="t-prompt">$</span>cargo fmt --check</div>
</div>
</div>
</div>

<div class="step-item">
<div class="step-header">
<span class="step-badge">03</span>
<h2 class="step-title">Sample Data &amp; PII Sanitization Invariant</h2>
</div>
<p>To protect privacy and comply with data sovereignty regulations, never submit real-world bank statements containing Personally Identifiable Information (PII) or authentic account details:</p>

<div class="table-responsive my-3">
<table class="visage-table">
<thead>
<tr>
<th>Data Field</th>
<th>Invariant Requirement</th>
<th>Verification Method</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>IBAN Checksums</strong></td>
<td>Must use valid ISO 7064 Mod-97 test numbers</td>
<td>Verified by <code>test_sample_data_valid.rs</code></td>
</tr>
<tr>
<td><strong>SWIFT / BIC</strong></td>
<td>Structurally valid 8 or 11-char test BICs</td>
<td>ISO 9362 structural regex validation</td>
</tr>
<tr>
<td><strong>Customer PII</strong></td>
<td>Synthetic names, anonymized street addresses</td>
<td>Zero real customer records permitted</td>
</tr>
<tr>
<td><strong>Currencies</strong></td>
<td>Standard ISO 4217 currency identifiers (EUR, GBP, USD)</td>
<td>Matched against official currency table</td>
</tr>
</tbody>
</table>
</div>
</div>

<div class="step-item">
<div class="step-header">
<span class="step-badge">04</span>
<h2 class="step-title">Commit Standards, DCO &amp; Signing</h2>
</div>
<p>All contributions must follow Conventional Commits, be SSH/GPG signed, and carry a Developer Certificate of Origin (DCO) <code>Signed-off-by</code> trailer:</p>

<div class="terminal-box my-3">
<div class="terminal-bar">
<span class="terminal-dot dot-red"></span>
<span class="terminal-dot dot-yellow"></span>
<span class="terminal-dot dot-green"></span>
<span class="terminal-title">bash — commit conventions</span>
</div>
<div class="terminal-body">
<div class="t-line"><span class="t-comment">&#35; Commit with DCO sign-off (-s) and cryptographic signature (-S)</span></div>
<div class="t-line"><span class="t-prompt">$</span>git commit -s -S -m <span class="t-val">&quot;feat(dialect): add barclays corporate pdf extractor&quot;</span></div>
</div>
</div>
</div>
