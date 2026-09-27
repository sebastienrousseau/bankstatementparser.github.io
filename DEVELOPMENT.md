# Development

## Prerequisites

- Rust and `ssg` 0.0.63: `cargo install ssg --locked --version 0.0.63`
- Python 3.10 or later
- Node.js 20 or later

## Build and test

```sh
make build      # compile static site with ssg and post-build optimization
make test       # run regression tests
make audit      # run WCAG AAA checks and SSG audit
make lint       # verify README, release versions, notes, and SPDX headers
make verify     # run all gates: lint, test, audit
make serve      # serve compiled site locally from public/
```

`make serve` serves the generated `public/` tree at <http://127.0.0.1:8000/>.

## Commit policy

Create a `feat/vX.Y.Z` branch, increment strictly by `0.0.1`, sign the commit
cryptographically with SSH, and include a DCO sign-off:

```sh
git commit -S -s
```
