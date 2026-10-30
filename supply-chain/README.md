# Supply Chain & Provenance Policy

This directory documents the supply-chain controls enforced across `bankstatementparser.github.io`.

---

## 1. Pinned Build & CI Dependencies

* **GitHub Actions**: Every workflow under [`.github/workflows/`](../.github/workflows/) pins third-party actions to full 40-character commit SHAs.
* **Python Verification Environment**: Pinned with SHA-256 hashes in [`requirements/ci.txt`](../requirements/ci.txt).
* **Static Site Generator**: Deterministically built with `ssg --locked --version 0.0.69`.

---

## 2. Runtime Zero-Trust Posture

* **Content Security Policy (CSP)**: Enforced via `<meta http-equiv="Content-Security-Policy">` and edge headers (`docs/_headers`, `docs/.ssg/edge/vercel-headers.json`, `docs/.ssg/edge/wrangler-headers.toml`).
* **Subresource Integrity (SRI)**: Every fingerprinted CSS and JS asset carries a `sha384-` integrity attribute verified on every build.
* **SPDX License Compliance**: 100% of source files carry machine-readable `SPDX-FileCopyrightText` and `SPDX-License-Identifier: Apache-2.0 OR MIT` headers, enforced by [`scripts/validate_spdx_headers.py`](../scripts/validate_spdx_headers.py).
* **CycloneDX SBOM**: Emitted at [`docs/sbom.cdx.json`](../docs/sbom.cdx.json) on every build.
