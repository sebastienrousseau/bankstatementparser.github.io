# ADR 0001: Adopt Static Site Generator (SSG) with Skeletonic CSS

- Status: accepted
- Date: 2026-09-01

## Context

Bankstatementparser.com requires high-speed page loads, privacy-preserving static
hosting, zero runtime tracking, and WCAG 2.2 Level AAA accessibility compliance
for financial developers and security auditors.

## Decision

Migrate the website from legacy multi-folder setups to native Rust Static Site
Generator (ssg) compilation using Markdown `_posts/` and Tera `_layouts/` templates.
Adopt Skeletonic CSS and Apple HIG navigation patterns with self-hosted assets,
strict Content Security Policy (CSP), and Subresource Integrity (SRI) hashes.

## Consequences

Site compilation produces deterministic HTML, sitemaps, and feeds. Color contrast
and regression tests are automated in CI. Output files are generated from templates
and never edited manually.
