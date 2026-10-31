# Changelog

All notable changes to this website are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project uses
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.0.8] - 2026-10-31

### Fixed

- Preserved `docs/_csp/` assets and emitted `.nojekyll` during GitHub Pages
  staging in `.github/workflows/ci.yml` and `scripts/post-build.py` so the
  extracted search widget stylesheet and script no longer return HTTP 404 in
  production.
- Embedded `#ssg-search-btn` and `#ssg-search-overlay` rules directly in
  `styles.css` and `_layouts/styles.css` to prevent unstyled SVG search icons
  and modal overlays from appearing in the page flow.
- Updated `.footer-grid` in `styles.css` and `_layouts/styles.css` from 3
  columns to 4 columns (`1.4fr 1fr 1fr 1fr`) to match the 4-column footer
  layout in `_layouts/footer.html`.

## [0.0.7] - 2026-10-30

### Fixed

- Resolved CodeQL code scanning alerts 41 and 42 (`py/empty-except`) in
  `scripts/post-build.py` by using `Path.unlink(missing_ok=True)` for optional
  news sitemap cleanup and failing fast on malformed `manifest.json` payloads.
- Removed broad `try ... except Exception` suppression in
  `scripts/validate_spdx_headers.py`.

## [0.0.6] - 2026-10-30

### Added

- Generated `llms-full.txt` alongside `llms.txt` in `scripts/post-build.py` to
  provide single-request full documentation context for AI coding agents.
- Added property-based and unit tests in `tests/test_frontmatter.py` covering
  `SOURCE_DATE_EPOCH` resolution, URL classification, and script-safe entity
  encoding.

### Changed

- `KEYS.asc` and `.github/allowed_signers` trust a second maintainer signing
  key, `SHA256:kIOPAavp1TCEauTr1tTIN3cv+tSs6F9m/4lZjuM9tqk` (rousseau-mbp-m1),
  so release tags can be signed on either maintainer machine.
- Upgraded CI workflows to Node.js 24 (npm 11) and `ssg` 0.0.69, and bumped
  GitHub Actions and `hypothesis` (`6.170.8`) dependencies (#38, #39, #41, #42).
- Refactored `scripts/post-build.py` and `_layouts/main.js` into modular
  functions adhering strictly to complexity ceilings, removing 40 unused legacy
  template files.

### Fixed

- `KEYS.asc` is now in OpenSSH allowed-signers format, so
  `git -c gpg.ssh.allowedSignersFile=KEYS.asc tag -v <tag>` verifies release
  tags. It previously held a bare public-key line that Git rejected as
  "invalid key". `KEYS.md` documents the command and lists each key's
  fingerprint.
- `scripts/post-build.py` now honours `SOURCE_DATE_EPOCH` when emitting
  `<lastmod>` in `sitemap.xml`, ensuring reproducible builds across arbitrary
  dates.
- Fixed unquoted dictionary keys in `scripts/release_notes.py`
  (`first_release_changes`) and hardened template Content Security Policy
  headers by removing `'unsafe-inline'`.

## [0.0.5] - 2026-10-11

### Changed

- Upgraded SSG compiler pin in release automation to v0.0.67.
- Standardized release workflow build and audit sequencing to ensure byte-for-byte
  reproducible release archives.

### Fixed

- Resolved CodeQL code scanning alert 39 (py/bad-tag-filter) in
  `scripts/post-build.py` by permitting whitespace and attributes in closing
  script tags.

## [0.0.4] - 2026-10-11

### Added

- Injected Schema.org `BreadcrumbList` structured data across all subpages to
  enable hierarchical rich snippets in Google search results.

### Changed

- Standardized `sitemap.xml` generation to strictly emit canonical directory
  permalinks without `index.html` suffixes, eliminating Google Search Console
  redirect and alternate page warnings.
- Unified OpenGraph (`og:url`), international hreflang (`hreflang="en"`), and
  canonical URLs across all layouts and markdown frontmatter to trailing slashes.
- Upgraded `robots.txt` distribution across `public/` and `docs/` build targets.

### Fixed

- Eliminated soft-404 indexing errors in Google Search Console by tagging `404/`
  and `offline/` with `<meta name="robots" content="noindex, follow">`,
  excluding them from `sitemap.xml`, and disallowing them in `robots.txt`.

## [0.0.3] - 2026-10-10

### Added

- Documented complete support across all 8 structured banking formats:
  CAMT (052/053/054), PAIN.001, MT940, MT942, OFX/QFX, BAI2, CSV, and PDF.
- Documented Apache Parquet streaming (`ParquetStreamWriter`) and batch export
  alongside plain-text ledger accounting models (hledger, beancount, ledger-cli).
- Generative Engine Optimization (GEO) architecture with direct-answer BLUF
  headers, structured entity graphs, and voice-search FAQ cards.
- Documented two-way bank reconciliation (`reconcile_payments_and_statements`),
  treasury analytics (`analyze_statement_transactions`), and PDF forensics.

### Changed

- Upgraded compilation and audit pipeline to the latest local SSG generator.
- The footer reads "© 2026 Sebastien Rousseau. Bank Statement Parser.",
  with the name linked to https://sebastienrousseau.com/ (`rel="author"`),
  across all layouts.

### Fixed

- Merges to `main` reach the live site again. The Pages source is "GitHub
  Actions", but no workflow deployed, so nothing merged since 28 July 2026
  was published. CI now deploys the validated `docs/` tree after its checks
  pass on `main`, leaving out ssg's build caches.
- `scripts/validate-frontmatter.py` checks only the frontmatter block. It
  searched the whole file, so a page missing `title:` passed when its body
  mentioned "title:".
- `/.well-known/security.txt` and `/security.txt` are published. The
  build left an empty `security.txt` and no `.well-known` copy, and the
  source's `Canonical:` named the old github.io address. The build now
  writes both paths from the one source, and the regression test fails if
  either is missing a required field.
- The Pages artifact includes `.well-known/`. The upload action drops
  dot-folders by default, so `/.well-known/security.txt` stayed 404 after
  the first deploy; the deploy now fails if it is missing.

### Security

- CodeQL also scans the GitHub Actions workflows, and ignores the
  generated `public/` and `docs/` trees.
- Dependabot also keeps the Python test dependencies current.
- Every GitHub Action is pinned by commit SHA.
- Property-based (Hypothesis) tests fuzz the frontmatter validator in CI.

## [0.0.2] - 2026-09-27

### Added

- Repository Gold Standard compliance: added `DEVELOPMENT.md`, `CODE_OF_CONDUCT.md`,
  `CONTRIBUTING.md`, `GOVERNANCE.md`, `SUPPORT.md`, `CITATION.cff`, `KEYS.asc`,
  `KEYS.md`, `DCO.txt`, and `.compliance.yml`.
- Established `docs/` root documentation containing `docs/ARCHITECTURE.md`,
  `docs/packaging.md`, `docs/adr/`, and release highlights in `docs/releases/`.
- Rebuilt `README.md` in strict adherence to `/Users/seb/Code/README-TEMPLATE.md`
  and gated layout conformance with `scripts/validate_readme.py`.
- Automated release workflow (`.github/workflows/release.yml`) with reproducible
  archive packaging (`scripts/release_backfill.py`), CycloneDX SBOM generation,
  and formatted GitHub release composition (`scripts/release_notes.py`).
- Added OpenSSF Scorecard and DCO verification workflows in `.github/workflows/`.
- Developer tooling configuration: `.editorconfig` and `.pre-commit-config.yaml`.

### Changed

- Updated static output directory to `public/` and upgraded SSG compilation to 0.0.63.

## [0.0.1] - 2026-09-01

### Added

- Migrated bankstatementparser.com to native Rust Static Site Generator (ssg)
  compilation with Skeletonic CSS and Apple HIG navigation (#4).
- WCAG 2.1 AAA accessibility contrast tokens and full keyboard navigation.
- Subresource Integrity (SRI) and Content Security Policy (CSP) security headers.
- Self-hosted asset delivery and zero third-party telemetry (#1).
- Dual licensing under Apache-2.0 OR MIT (#2, #3).

[Unreleased]: https://github.com/sebastienrousseau/bankstatementparser.github.io/compare/v0.0.6...HEAD
[0.0.6]: https://github.com/sebastienrousseau/bankstatementparser.github.io/compare/v0.0.5...v0.0.6
[0.0.5]: https://github.com/sebastienrousseau/bankstatementparser.github.io/compare/v0.0.4...v0.0.5
[0.0.4]: https://github.com/sebastienrousseau/bankstatementparser.github.io/compare/v0.0.3...v0.0.4
[0.0.3]: https://github.com/sebastienrousseau/bankstatementparser.github.io/compare/v0.0.2...v0.0.3
[0.0.2]: https://github.com/sebastienrousseau/bankstatementparser.github.io/compare/v0.0.1...v0.0.2
[0.0.1]: https://github.com/sebastienrousseau/bankstatementparser.github.io/releases/tag/v0.0.1
