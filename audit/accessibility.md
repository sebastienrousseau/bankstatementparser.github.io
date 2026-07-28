# Accessibility & compliance audit — bankstatementparser.com

This site targets **WCAG 2.1 level AAA**. The notes below are reproducible
offline; the browser-driven audits (Lighthouse, WAVE) require Chrome and
should be run against the deployed site.

## Colour contrast (WCAG 1.4.6 Contrast Enhanced, AAA)

AAA requires **≥ 7:1** for normal text. Every foreground/background pair in
the design system was computed with the WCAG relative-luminance formula. All
pairs clear **7:1** (worst pair 7.09:1).

### Light theme (bg `#ffffff`, surface `#eef2f6`)

| Role | Colour | On background | On surface |
|------|--------|---------------|------------|
| Body text | `#14181f` | 17.8:1 | — |
| Muted text | `#41474f` | 9.4:1 | 8.3:1 |
| Brand / links | `#1c4e9e` | 7.98:1 | 7.09:1 |
| Primary button text | `#ffffff` on `#173f86` | 10.0:1 | — |

### Dark theme (bg `#0d1117`, surface `#161c26`)

| Role | Colour | On background | On surface |
|------|--------|---------------|------------|
| Body text | `#e8eef4` | 16.2:1 | — |
| Muted text | `#aeb9c5` | 9.5:1 | 8.6:1 |
| Brand / links | `#82b4ff` | 8.9:1 | 8.1:1 |
| Primary button text | `#0d1117` on `#82b4ff` | 8.9:1 | — |

Reproduce: `python3 audit/contrast.py`

## Structure & interaction

- **Landmarks**: one `<header>`, one `<main id="main">`, one `<footer>` per
  page; `<nav aria-label>` on primary nav and breadcrumbs.
- **Headings**: single `<h1>` per page, no skipped levels.
- **Keyboard**: skip link, visible `:focus-visible` outline (AAA-contrast),
  Escape closes the mobile menu, no keyboard traps.
- **Motion**: `prefers-reduced-motion` disables transitions and smooth scroll.
- **Themes**: honours `prefers-color-scheme`; a persisted toggle overrides it,
  set before first paint (no flash).
- **Forms**: every control has an associated `<label>`; hints via
  `aria-describedby`.
- **Colour independence**: links are underlined, not colour-only.

## HTML validation

```shell
npx html-validate "docs/**/*.html"   # config: .htmlvalidate.json
```

Extends `html-validate:recommended` plus WCAG rules; the whole `docs/` tree
passes with zero errors.

## Privacy / best practices

- No cookies, analytics, web fonts, CDN or third-party requests.
- Strict `Content-Security-Policy` on every page (`default-src 'self'`), plus
  a `_headers` file (nosniff, no-referrer, Permissions-Policy, HSTS,
  `frame-ancestors 'none'`).

## What still needs a browser

Lighthouse and WAVE need a Chromium engine, unavailable in the build sandbox
(musl/Alpine). Run them against the deployed URL:

```shell
npx lighthouse https://bankstatementparser.com/ --preset=desktop --view
```

The site is engineered to score 100 across Performance, Accessibility, Best
Practices and SEO: single small same-origin CSS, deferred JS, no layout
shift, complete meta/structured data, and AAA contrast.
