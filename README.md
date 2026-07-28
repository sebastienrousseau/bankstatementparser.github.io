# bankstatementparser.com — official website 🌍

Marketing and documentation site for the **bankstatementparser** suite —
open-source Python tooling that parses bank statements across CAMT
(ISO 20022), PAIN.001, MT940/MT942, BAI2, OFX/QFX, CSV and PDF into one
auditable `Transaction` model.

The site promotes the published packages:

- [`bankstatementparser`](https://pypi.org/project/bankstatementparser/) — the core parser.
- [`bankstatementparser-loader-bai2`](https://pypi.org/project/bankstatementparser-loader-bai2/) — BAI2 loader.
- [`bankstatementparser-loader-mt942`](https://pypi.org/project/bankstatementparser-loader-mt942/) — SWIFT MT942 loader.
- [`bankstatementparser-writer-xlsx`](https://pypi.org/project/bankstatementparser-writer-xlsx/) — Excel writer.
- [`bankstatementparser-lsp`](https://pypi.org/project/bankstatementparser-lsp/) — Language Server.
- [`bankstatementparser-mcp`](https://pypi.org/project/bankstatementparser-mcp/) — MCP server.

## Design goals

- **Zero third-party dependencies at runtime** — no CDN, web fonts,
  analytics or trackers. Every asset is self-hosted, which is what makes the
  strict Content-Security-Policy and the privacy posture possible.
- **WCAG 2.1 AAA** — all colour pairs are verified to at least 7:1 contrast
  in both light and dark themes (see `audit/`). Full keyboard control,
  visible focus, skip link, semantic landmarks, reduced-motion support.
- **SEO-complete** — per-page canonical, Open Graph, Twitter, JSON-LD
  (`Organization`, `WebSite`, `SoftwareApplication`, `BreadcrumbList`,
  `FAQPage`, `Article`, `HowTo`), `sitemap.xml`, `robots.txt`, `rss.xml`,
  `manifest.json` and `humans.txt`.

## Architecture

A **dependency-free static site** — no build step. The deployable site lives
entirely in [`docs/`](./docs) and is served as-is by GitHub Pages (Settings →
Pages → *Deploy from a branch* → `main` / `/docs`), Netlify, or Cloudflare
Pages.

## Local preview

```shell
npx serve docs
```

## Quality checks

```shell
npx html-validate "docs/**/*.html"   # config in .htmlvalidate.json
python3 audit/contrast.py            # WCAG AAA contrast proof
```

CI (`.github/workflows/ci.yml`) runs both on every push and pull request,
plus structure/self-hosting guardrails.

## Licence

Content and code are released under the [Apache License 2.0](./LICENSE),
matching the bankstatementparser suite.
