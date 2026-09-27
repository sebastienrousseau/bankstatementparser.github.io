<!-- SPDX-License-Identifier: Apache-2.0 OR MIT -->

<p align="center">
  <img src="https://cloudcdn.pro/bankstatementparser/v1/logos/bankstatementparser.svg" alt="Bank Statement Parser logo" width="128" />
</p>

<h1 align="center">Bank Statement Parser</h1>

<p align="center">
  High-throughput financial document parsing engine converting multi-format bank statements (PDF, CSV, OFX, MT940, CAMT.053) into validated JSON and ISO 20022 messages with zero telemetry.
</p>

<p align="center">
  <a href="https://github.com/sebastienrousseau/bankstatementparser.github.io/actions"><img src="https://github.com/sebastienrousseau/bankstatementparser.github.io/workflows/CI/badge.svg?style=for-the-badge&logo=github" alt="Build" /></a>
  <a href="https://github.com/sebastienrousseau/bankstatementparser.github.io/releases"><img src="https://img.shields.io/badge/release-v0.0.2-fc8d62.svg?style=for-the-badge&color=fc8d62&logo=git" alt="Release: v0.0.2" /></a>
  <a href="https://bankstatementparser.com"><img src="https://img.shields.io/badge/docs-bankstatementparser.com-blue?style=for-the-badge&labelColor=555555&logo=googlechrome" alt="Docs" /></a>
  <a href="https://scorecard.dev/viewer/?uri=github.com/sebastienrousseau/bankstatementparser.github.io"><img src="https://img.shields.io/ossf-scorecard/github.com/sebastienrousseau/bankstatementparser.github.io?style=for-the-badge&label=OpenSSF%20Scorecard&logo=openssf" alt="OpenSSF Scorecard" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-Apache--2.0%20OR%20MIT-blue.svg?style=for-the-badge" alt="License: Apache-2.0 OR MIT" /></a>
  <a href="https://static-site-generator.com/"><img src="https://img.shields.io/badge/SSG-0.0.63-93450a.svg?style=for-the-badge&logo=rust" alt="Built with Rust SSG" /></a>
</p>

---

## Contents

**Getting started**

- [Install](#install) — build prerequisites and tooling
- [Requirements](#requirements) — toolchain floor, platforms
- [Quick Start](#quick-start) — compile and preview the static site

**The Bank Statement Parser ecosystem**

- [The Bank Statement Parser ecosystem](#the-bank-statement-parser-ecosystem) — core engine, CLI, Python SDK, and documentation portal

**Library reference**

- [Capabilities at a glance](#capabilities-at-a-glance) — static site architecture and web standards
- [Ecosystem comparison](#ecosystem-comparison) — design and accessibility comparison
- [Benchmarks](#benchmarks) — compilation speed and WCAG audit scores
- [Features](#features) — site capabilities and security features
- [Configuration](#configuration) — SSG manifest and layout configuration
- [Examples](#examples) — runnable development workflows

**Operational**

- [When not to use Bank Statement Parser](#when-not-to-use-bank-statement-parser) — limitations
- [Development](#development) — make targets, validation, and quality gates
- [Security](#security) — Subresource Integrity (SRI) and CSP enforcement
- [Documentation](#documentation) — all reference docs
- [Stability guarantees](#stability-guarantees) — versioning discipline and WCAG AAA compliance
- [License](#license)

---

## Install

### As a Static Site Generator project

Ensure `ssg` (Static Site Generator) and Python are installed:

```bash
# Install the Rust static site generator
cargo install ssg

# Clone the documentation repository
git clone https://github.com/sebastienrousseau/bankstatementparser.github.io.git
cd bankstatementparser.github.io
```

Optional audit tooling includes `html-validate`, `pa11y-ci`, and `@lhci/cli` for CI conformance testing:

```bash
npm install -g html-validate pa11y-ci @lhci/cli
```

---

## Requirements

- **Rust Toolchain**: Rust 1.75+ (for compiling `ssg` static site generator).
- **Node.js**: Node 20+ (for HTML validation and accessibility CI suites).
- **Python**: Python 3.12+ (for contrast ratios and regression testing).
- **Target Platforms**: Linux, macOS, Windows (cross-platform static deployment).

---

## Quick Start

```bash
# Build the complete site using Rust SSG and post-build optimization
make build

# Run WCAG 2.2 Level AAA and regression test suites
make audit

# Serve locally for preview
python3 -m http.server 8000 --directory docs
```

Navigate to `http://localhost:8000` to inspect the generated documentation portal.

---

## The Bank Statement Parser ecosystem

The `bankstatementparser` suite provides end-to-end tooling for financial document extraction, verification, and web distribution:

| Component | Purpose | Use case |
| :--- | :--- | :--- |
| [bankstatementparser](https://github.com/sebastienrousseau/bankstatementparser) | Core Rust engine & Python bindings | Financial document parsing (PDF, CSV, OFX, MT940, CAMT.053) |
| [bankstatementparser-cli](https://github.com/sebastienrousseau/bankstatementparser) | Standalone CLI binary | Batch file transformation and terminal automation |
| [bankstatementparser.github.io](https://github.com/sebastienrousseau/bankstatementparser.github.io) | Static documentation portal | Sovereign, zero-telemetry documentation and architectural guides |

---

## Capabilities at a glance

| Area | Capability | Status |
| :--- | :--- | :--- |
| Static Generation | Rust SSG v0.0.63 + Tera template compilation | Active |
| Accessibility | 100% WCAG 2.2 Level AAA compliance (>= 7.0:1 contrast) | Verified |
| Content Security | Strict Content-Security-Policy (CSP) with zero inline scripts | Enforced |
| Integrity | SHA-384 Subresource Integrity (SRI) on all scripts and styles | Active |
| Search Engine | Client-side zero-telemetry indexing via `search-index.json` | Active |
| Feeds & Syndication | Atom, RSS 2.0, JSON Feed, Sitemap, and CycloneDX SBOM | Automated |

---

## Ecosystem comparison

| Project | Zero Telemetry | WCAG 2.2 AAA | Subresource Integrity | Fast Native SSG |
| :--- | :---: | :---: | :---: | :---: |
| **Bank Statement Parser Web** | **Yes** | **Yes (17.8:1 worst)** | **Yes (SHA-384)** | **Yes (Rust SSG)** |
| Docusaurus | No (Default telemetry) | Partial (AA) | No | No (Node.js) |
| GitBook / Cloud Docs | No (Third-party hosted) | Partial (AA) | No | No (Proprietary SaaS) |

---

## Benchmarks

Audit and regression suites are executed continuously on every commit:

| Scenario | Result | Environment |
| :--- | ---: | :--- |
| Full Site Compilation (20 Pages) | < 2.0s | Rust `ssg` 0.0.63, 32 plugins |
| Worst Light Mode Contrast Ratio | 17.79:1 | WCAG 2.2 AAA (Threshold >= 7.0:1) |
| Worst Dark Mode Contrast Ratio | 8.08:1 | WCAG 2.2 AAA (Threshold >= 7.0:1) |
| Lighthouse Performance / A11y | 100 / 100 | Clean ECMAScript, zero heavy runtimes |

---

## Features

- **Rust Static Site Generator (SSG)**: Markdown content parsing and Tera template compilation with sub-second page generation.
- **Apple HIG Design Philosophy**: Responsive glass-morphism sticky header, squircle buttons, and smooth contrast-mode toggling.
- **Subresource Integrity (SRI)**: SHA-384 cryptographic digests enforced across all assets.
- **Zero Third-Party Tracking**: Completely self-hosted static assets on high-assurance edge CDN (`cloudcdn.pro`).
- **Offline PWA Readiness**: Manifest generation and offline fallback routes.
- **AI Integration Manifests**: Machine-readable `llms.txt`, `llms-full.txt`, and Agent API documentation.

---

## Configuration

Site configuration is governed by `config/ssg.json` and `ssg.toml`:

```json
{
  "title": "Bank Statement Parser",
  "description": "High-throughput, privacy-first parser converting bank statements into validated JSON and ISO 20022 messages.",
  "cdn": "https://cloudcdn.pro"
}
```

Template layouts reside in `_layouts/` with Markdown articles under `_posts/`. Compiled web assets are mirrored to `docs/` for GitHub Pages distribution.

---

## Examples

### Local Compilation & Contrast Verification

```bash
# Compile Markdown content and layout templates into public/ and docs/
make build

# Run mathematical color contrast verification
make contrast

# Run Markdown frontmatter schema validator
make validate
```

---

## When not to use Bank Statement Parser

- **Dynamic Server-Side Applications**: This repository produces purely static, pre-rendered HTML/CSS/JS. It does not include a dynamic backend database or runtime server.
- **In-Browser Statement Decryption**: The documentation portal explains and distributes the parser; actual statement extraction is performed locally via the Rust CLI or Python package to ensure zero data leakage.

---

## Development

```bash
# Run complete verification suite
make audit

# Run HTML5 and WCAG structural validation
npx html-validate "docs/**/*.html"

# Run color contrast compliance check
python3 audit/contrast.py
```

All pull requests must pass HTML validation, contrast analysis, and structural self-hosting guardrails before merging.

---

## Security

Every deployment enforces strict cryptographic and architectural controls:

- **Strict Content Security Policy**: Eliminates unsafe script evaluation and restricts asset loading.
- **Air-Gapped Operation**: Zero outbound analytics, telemetry, or external tracking beacons.
- **Supply Chain Assurance**: CycloneDX SBOM generated on every build (`docs/sbom.cdx.json`).

Report vulnerabilities according to [`SECURITY.md`](SECURITY.md).

---

## Documentation

- [Getting Started Guide](https://bankstatementparser.com/getting-started/index.html)
- [Supported Formats Matrix](https://bankstatementparser.com/formats/index.html)
- [Pipeline Architecture](https://bankstatementparser.com/architecture/index.html)
- [Performance Benchmarks](https://bankstatementparser.com/benchmarks/index.html)
- [Zero-Telemetry Security](https://bankstatementparser.com/security/index.html)
- [API & SDK Reference](https://bankstatementparser.com/api/index.html)
- [Release Changelog](https://bankstatementparser.com/changelog/index.html)
- [Contributing Guidelines](https://bankstatementparser.com/contributing/index.html)
- [WCAG AAA Accessibility Statement](https://bankstatementparser.com/accessibility/index.html)

---

## Stability guarantees

Versions follow strict Semantic Versioning (`0.0.1` -> `0.0.2` -> ...), advancing incrementally per user repository conventions. The layout, visual contrast, and WCAG AAA compliance are regression-tested on every release.

---

## License

Dual-licensed under [Apache-2.0](LICENSE-APACHE) OR [MIT](LICENSE-MIT), at your option. See [LICENSE](LICENSE).
