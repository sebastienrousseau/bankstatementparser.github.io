# Changelog

All notable changes to this website are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project uses
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Fixed

- Merges to `main` reach the live site again. The Pages source is "GitHub
  Actions", but no workflow deployed, so nothing merged since 28 July 2026
  was published. CI now deploys the validated `docs/` tree after its checks
  pass on `main`, leaving out ssg's build caches.
- `scripts/validate-frontmatter.py` checks only the frontmatter block. It
  searched the whole file, so a page missing `title:` passed when its body
  mentioned "title:".

### Security

- CodeQL scans the JavaScript, Python and workflows on every change and
  weekly.
- Dependabot keeps the GitHub Actions and the Python test dependencies
  current.
- Every GitHub Action is pinned by commit SHA.
- Property-based (Hypothesis) tests fuzz the frontmatter validator in CI.
- `SECURITY.md` sets out supported versions, private reporting, the
  handling process and credit.

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

[Unreleased]: https://github.com/sebastienrousseau/bankstatementparser.github.io/compare/v0.0.2...HEAD
[0.0.2]: https://github.com/sebastienrousseau/bankstatementparser.github.io/compare/v0.0.1...v0.0.2
[0.0.1]: https://github.com/sebastienrousseau/bankstatementparser.github.io/releases/tag/v0.0.1
