# Agent instructions

- Read `README.md`, `DEVELOPMENT.md`, and `/Users/seb/Code/REPO-STANDARD.md`
  before modifying this repository.
- Use locally installed `ssg` 0.0.63 for every build.
- Never edit generated output in `public/` directly. Source of truth is
  `_posts/` for content and `_layouts/` for Tera templates.
- Preserve WCAG 2.2 AAA accessibility, zero findings, and 100 Lighthouse
  scores on mobile and desktop.
- Run `make verify` before proposing or creating any commit.
- Work on a `feat/vX.Y.Z` branch with patch-only increments.
- Sign and DCO-sign off every commit (`git commit -S -s`).
- Do not publish, tag, release, or merge unless all required checks are green.
