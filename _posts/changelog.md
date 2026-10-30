---
name: "Bank Statement Parser"
short_name: "bankstatementparser"
title: "Changelog & Semantic Version History: Release Notes"
description: "Comprehensive release notes and semantic versioning history for Bank Statement Parser, detailing new format dialects, performance fixes, and security patches."
keywords: "bankstatementparser changelog, release history, semantic versioning"
author: "Sebastien Rousseau"
date: "2026-09-01"
language: "en-GB"
layout: "page"
permalink: "https://bankstatementparser.com/changelog/"
logo: "https://cloudcdn.pro/bankstatementparser/v1/logos/bankstatementparser.svg"
banner: "https://cloudcdn.pro/stocks/images/quantum-computer-room-1200.webp"
banner_alt: "Bank Statement Parser — High-Throughput Financial Document Parsing Engine"
eyebrow: "Release History"
headline: "Changelog"
lead: "Deterministic versioning history, security audits, and functional enhancements across every release."
---



All notable changes to **Bank Statement Parser** are documented in this file following strict Semantic Versioning.

## [0.0.6] - 2026-10-30
### Added
- Generated `llms-full.txt` alongside `llms.txt` for single-request LLM and coding agent ingestion.
- Expanded property-based test coverage for deterministic `SOURCE_DATE_EPOCH` builds and URL classification.
### Changed
- Trusted second maintainer SSH signing key (`rousseau-mbp-m1`) in `KEYS.asc` and `.github/allowed_signers`.
- Upgraded CI to Node.js 24 and `ssg` 0.0.69, and pruned 40 unused legacy template files.
### Fixed
- Reformatted `KEYS.asc` into valid OpenSSH allowed-signers format and honoured `SOURCE_DATE_EPOCH` in `sitemap.xml` generation.

## [0.0.5] - 2026-10-11
### Changed
- Upgraded SSG compiler pin in release automation and standardized build and audit sequencing for byte-for-byte reproducible release archives.
### Fixed
- Resolved CodeQL alert 39 in `scripts/post-build.py` by permitting whitespace and attributes in closing script tags.

## [0.0.4] - 2026-10-11
### Added
- Injected Schema.org `BreadcrumbList` structured data across all subpages.
### Changed
- Standardized `sitemap.xml` and canonical permalinks to trailing directory slashes and excluded `404/` and `offline/` utility routes.

## [0.0.3] - 2026-10-10
### Added
- Expanded format specifications covering all 8 banking formats: CAMT (052/053/054), PAIN.001, MT940, MT942, OFX/QFX, BAI2, CSV, and PDF.
- Documented Apache Parquet streaming (`ParquetStreamWriter`) and batch export alongside plain-text ledger models (hledger, beancount, ledger-cli).
- Implemented Generative Engine Optimization (GEO) architecture with direct-answer BLUF headers and entity-based knowledge graphs.
- Documented two-way bank reconciliation (`reconcile_payments_and_statements`), treasury analytics, and PDF forensics.
### Changed
- Upgraded Static Site Generator (SSG) compilation and audit pipeline to the latest local version.
- Linked copyright notice directly to author Sebastien Rousseau at https://sebastienrousseau.com/ across all layouts.

## [0.0.2] - 2026-09-27
### Fixed
- Fixed CSS entity escape sequence for `.hr-blurred:after` in base layout template.
- Rebuilt native static site generator assets and synced release version metadata.

## [0.0.1] - 2026-09-01
### Added
- Initial release of the Bank Statement Parser documentation portal.
- Static Site Generator (SSG) native compilation pipeline.
- Multi-format support specifications (PDF, CSV, OFX, QIF, MT940, CAMT.053).
- WCAG 2.2 Level AAA compliant design system.
- Zero-telemetry security documentation and CycloneDX SBOM provenance.
