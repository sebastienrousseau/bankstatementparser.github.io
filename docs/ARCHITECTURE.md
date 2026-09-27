# Architecture

## System context

Bankstatementparser.com is a static documentation website for the Bank Statement
Parser financial document parsing engine. Authors edit Markdown content in
`_posts/` and Tera templates in `_layouts/`. The Static Site Generator (ssg)
0.0.63 compiles HTML, sitemaps, feeds, search indexes, and accessibility audits.
Deterministic post-build processing ensures valid entity encoding, canonical links,
and search indexing. GitHub Actions runs quality gates and deploys the generated
Pages artifact.

## Build flow

```text
_posts/ + _layouts/ + ssg.toml
              |
              v
          ssg 0.0.63
              |
              v
         public/ tree
              |
              v
     post-build optimization
              |
              v
    CI accessibility & lint gates
              |
              v
     GitHub Pages deployment
```

## Theme and design system

The site is built on the Skeletonic CSS layout engine with an Apple Human Interface
Guidelines (HIG) design system. It provides a sticky glass navigation bar, squircle
action buttons, responsive mobile drawer navigation, and accessible dark/light
theme auto-detection with zero visual flash. Color tokens are audited against
WCAG 2.2 Level AAA contrast ratios (at least 7.0:1 for text, 4.5:1 for headings).

## Security and privacy

The site adheres to zero-telemetry and privacy-first principles:

- No third-party tracking scripts, analytics cookies, or browser fingerprinting.
- Strict Content Security Policy (CSP) delivered via `<meta http-equiv>` and edge headers.
- Subresource Integrity (SRI) cryptographic digests on stylesheets and scripts.
- CycloneDX Software Bill of Materials (SBOM) and signed Git tags on release.

## Deployment and rollback

Releases are published using cryptographically signed, immutable Git tags. Rollback
is performed by redeploying a verified tag through the automated CI pipeline.
Output directories are generated from source and are not edited manually.
