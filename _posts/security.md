---
name: "Bank Statement Parser"
short_name: "bankstatementparser"
title: "Security Architecture: Zero Telemetry, Air-Gapped & Memory Safe"
description: "Detailed security specifications, zero-telemetry architecture, memory safety guarantees, and CycloneDX SBOM provenance."
keywords: "zero telemetry parser, air gapped bank statement parser, memory safe financial software, CycloneDX SBOM"
author: "Sebastien Rousseau"
date: "2026-09-01"
language: "en-GB"
layout: "page"
permalink: "https://bankstatementparser.com/security/index.html"
logo: "https://cloudcdn.pro/bankstatementparser/v1/logos/bankstatementparser.svg"
banner: "https://cloudcdn.pro/stocks/images/quantum-computer-room-1200.webp"
banner_alt: "Bank Statement Parser — High-Throughput Financial Document Parsing Engine"
---

# Security Architecture & Trust Guarantees

Financial statement data requires the highest level of confidentiality and privacy assurance.

## Core Security Pillars

### 1. 100% Zero-Telemetry Guarantee
Bank Statement Parser contains no analytics SDKs, no tracking pixels, and no remote crash reporters. The binary makes zero outbound network calls, making it ideal for air-gapped sovereign environments.

### 2. Rust Memory Safety
Engineered in 100% safe Rust without unverified unsafe pointer arithmetic. Immune to buffer overflows, dangling pointers, and memory corruption vulnerabilities common in legacy C/C++ parsers.

### 3. Subresource Integrity & Supply Chain Provenance
Every release build is signed using Sigstore Cosign and accompanied by a CycloneDX Software Bill of Materials (SBOM) for verifiable dependency auditing.
