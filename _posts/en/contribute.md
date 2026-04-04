---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "A blurry image of a ball of light in the dark"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/daniele-franchi-Vl6YuVBLEys.webp"
cdn: "https://cloudcdn.pro"
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Bank Statement Parser. All rights reserved."
date: "Apr 01, 2026"
description: "Would you like to join the project? We're always looking for people with skills in both developing and using open source software."
format-detection: "telephone=no"
form-id: ""
hreflang: "en"
icon: "https://cloudcdn.pro/bankstatementparser/images/favicon.ico"
id: "https://bankstatementparser.com/contribute/index.html"
image_alt: "Logo of Bank Statement Parser, a powerful Python tool designed for quick, accurate financial data processing and insights extraction."
image_height: "630"
image_width: "1200"
image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
keywords: "Contribute, developer, developer us form"
language: "en-GB"
layout: "link"
locale: "en_GB"
logo_alt: "Logo of Bank Statement Parser, a powerful Python tool designed for quick, accurate financial data processing and insights extraction."
logo_height: "44"
logo_width: "44"
logo: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Contribute"
permalink: "https://bankstatementparser.com/contribute/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Be a part of something bigger"
theme_color: "rgb(73, 214, 251)"
title: "Share Your Skills and Expertise by Contributing to Bank Statement Parser"
url: "https://bankstatementparser.com/contribute/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: https://bankstatementparser.com/contribute/rss.xml
category: "Software, Static Site Generator, Rust"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Would you like to join the project? We're always looking for people with skills in both developing and using open source software."
item_guid: https://bankstatementparser.com/contribute/rss.xml
item_link: https://bankstatementparser.com/contribute/rss.xml
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Share Your Skills and Expertise by Contributing to Bank Statement Parser"
last_build_date: "2026-04-01T00:00:00+00:00"
managing_editor: "contact@bankstatementparser.com"
pub_date: "2026-04-01T00:00:00+00:00"
ttl: "60"
type: "website"
webmaster: "contact@bankstatementparser.com"

# Apple - The Apple front matter (YAML).

apple_mobile_web_app_orientations: "portrait"
apple_touch_icon_sizes: "192x192"
apple-mobile-web-app-capable: "yes"
mobile-web-app-capable: "yes"
apple-mobile-web-app-status-bar-inset: "black"
apple-mobile-web-app-status-bar-style: "black-translucent"
apple-mobile-web-app-title: "Share Your Skills and Expertise by Contributing to Bank Statement Parser"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Would you like to join the project? We're always looking for people with skills in both developing and using open source software."
twitter_image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logo of Bank Statement Parser, a powerful Python tool designed for quick, accurate financial data processing and insights extraction."
twitter_site: "@wwdseb"
twitter_title: "Share Your Skills and Expertise by Contributing to Bank Statement Parser"
twitter_url: "https://bankstatementparser.com/contribute/index.html"

# Humans.txt - The Humans.txt front matter (YAML).

author_website: "https://bankstatementparser.com"
author_twitter: "@wwdseb"
author_location: "London, UK"
thanks: "Thanks for reading!"
site_last_updated: "2026-04-01"
site_standards: "HTML5, CSS3, RSS, Atom, JSON, XML, YAML, Markdown, TOML"
site_components: "Shokunin SSG, Shokunin CLI, Shokunin Templates, Shokunin Themes, Kaishi SSG, Kaishi CLI, Kaishi Templates, Kaishi Themes"
site_software: "Shokunin, Rust"

---

We welcome contributions from developers, technical writers, and anyone interested in improving bank statement parsing for the finance community.

## How to Contribute

### Report Issues

Found a bug or have a feature request? [Open an issue on GitHub](https://github.com/sebastienrousseau/bankstatementparser/issues). Please include:

- A clear description of the problem or suggestion.
- Steps to reproduce (for bugs).
- Your Python version and operating system.

### Submit Code

1. Fork the [repository](https://github.com/sebastienrousseau/bankstatementparser).
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Write tests for your changes (we require 100% branch coverage).
4. Run the test suite: `pytest`.
5. Submit a pull request with a clear description.

### Improve Documentation

Documentation improvements are always welcome. You can:

- Fix typos or clarify existing content.
- Add new usage examples to the [examples directory](https://github.com/sebastienrousseau/bankstatementparser/tree/main/examples).
- Improve docstrings in the source code.

## Development Setup

```bash
git clone https://github.com/sebastienrousseau/bankstatementparser.git
cd bankstatementparser
python3 -m venv .venv && source .venv/bin/activate
pip install poetry && poetry install --with dev
pytest  # Run the test suite
```

## Code Standards

- All code must pass `ruff` linting and `mypy` type checking.
- All commits must be signed.
- All pull requests must maintain 100% branch coverage.
- Follow the existing code style and patterns.

## Sponsor the Project

If Bank Statement Parser saves your team time, consider [sponsoring the project on GitHub](https://github.com/sponsors/sebastienrousseau). Your support helps us maintain and improve the library.
