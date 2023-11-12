---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "A white building with black windows"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/daniele-franchi-Vl6YuVBLEys.webp"
cdn: "https://kura.pro"
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023 Bank Statement Parser. All rights reserved."
date: "Nov 12, 2023"
description: "Welcome to the Bank Statement Parser User Guide. Get started with our Python library for easy CAMT and SEPA file parsing and streamline your financial analysis."
download: ""
format-detection: "telephone=no"
hreflang: "en"
icon: "https://kura.pro/shokunin/images/favicon.ico"
id: "https://bankstatementparser.com/getting-started/index.html"
image_alt: "Logo of Bank Statement Parser, a powerful Python tool designed for quick, accurate financial data processing and insights extraction."
image_height: "100vh"
image_width: "100vw"
image: "https://kura.pro/bankstatementparser/images/logos/bankstatementparser.webp"
keywords: "bank statement parser, financial analysis, CAMT, SEPA, parsing, automation, efficiency, accuracy, decision-making, workflow"
language: "en-GB"
layout: "start"
locale: "en_GB"
logo_alt: "Logo of Bank Statement Parser, a powerful Python tool designed for quick, accurate financial data processing and insights extraction."
logo_height: "44"
logo_width: "44"
logo: "https://kura.pro/bankstatementparser/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Getting Started"
permalink: "https://bankstatementparser.com/getting-started/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Start Building Secure Applications with Bank Statement Parser"
tags: "bank, statement, parser, finance, analysis, CAMT, SEPA, automation, decision, workflow"
theme_color: "rgb(73, 214, 251)"
title: "Bank Statement Parser: Installation Prerequisites"
url: "https://bankstatementparser.com"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/getting-started/rss.xml"
category: "Software, Static Site Generator, Rust"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Welcome to the Bank Statement Parser User Guide. Get started with our Python library for easy CAMT and SEPA file parsing and streamline your financial analysis."
item_guid: "https://bankstatementparser.com/getting-started/rss.xml"
item_link: "https://bankstatementparser.com/getting-started/rss.xml"
item_pub_date: "2023-11-12T18:21:18+00:00"
item_title: "Bank Statement Parser: Installation Prerequisites"
last_build_date: "2023-11-12T18:21:18+00:00"
managing_editor: "contact@bankstatementparser.com"
pub_date: "2023-11-12T18:21:18+00:00"
ttl: "60"
type: "website"
webmaster: "contact@bankstatementparser.com"

# Apple - The Apple front matter (YAML).

apple_mobile_web_app_orientations: "portrait"
apple_touch_icon_sizes: "192x192"
apple-mobile-web-app-capable: "yes"
apple-mobile-web-app-status-bar-inset: "black"
apple-mobile-web-app-status-bar-style: "black-translucent"
apple-mobile-web-app-title: "Bank Statement Parser: Installation Prerequisites"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "https://kura.pro/bankstatementparser/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary"
twitter_creator: "@wwdseb"
twitter_description: "Welcome to the Bank Statement Parser User Guide. Get started with our Python library for easy CAMT and SEPA file parsing and streamline your financial analysis."
twitter_image: "https://kura.pro/bankstatementparser/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logo of Bank Statement Parser, a powerful Python tool designed for quick, accurate financial data processing and insights extraction."
twitter_site: "@wwdseb"
twitter_title: "Bank Statement Parser: Installation Prerequisites"
twitter_url: "https://bankstatementparser.com/getting-started/index.html"

# Humans.txt - The Humans.txt front matter (YAML).

author_website: "https://bankstatementparser.com"
author_twitter: "@wwdseb"
author_location: "London, UK"
thanks: "Thanks for reading!"
site_last_updated: "2023-10-25"
site_standards: "HTML5, CSS3, RSS, Atom, JSON, XML, YAML, Markdown, TOML"
site_components: "Shokunin SSG, Shokunin CLI, Shokunin Templates, Shokunin Themes, Kaishi SSG, Kaishi CLI, Kaishi Templates, Kaishi Themes"
site_software: "Shokunin, Rust"

---

![Bank Statement Parser:  Setup and Usage Guide](https://kura.pro/stock/images/banners/christoph-duschl-CE_TvPHF3lA.webp).class=\"img-fluid fade-in p-3\"

## System Requirements

Before beginning, ensure your system meets the following criteria:

- Python 3.6 or newer installed.
- Command-line interface (CLI) access, such as Terminal or Command Prompt.

## Installation

### Create a Virtual Environment

We recommend creating a virtual environment to install the Bank Statement Parser. This will ensure that the package is installed in an isolated environment and will not affect other projects.

![Bank Statement Parser: Installation Prerequisites](https://kura.pro/stock/images/banners/adrien-olichon-3137055.webp).class=\"w-25 fade-in py-0 px-3 float-start\"

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Installing the Bank Statement Parser

Install `bankstatementparser` with just one command:

```bash
pip install bankstatementparser
```

### Installing Dependencies

Open your CLI and navigate to the library's directory, then execute the following:

```bash
pip install -r requirements.txt
```

![divider][divider].class=\"m-10 w-100\"

## Get the Source Code on GitHub

You can access the source code for the Bank Statement Parser by downloading releases, browsing or even contributing to its development on [GitHub ⧉][01]. You can also [report issues][02] and [request new features][02], which we will review and address as soon as possible.

![divider][divider].class=\"m-10 w-100\"

## Usage

### CAMT Files

![Bank Statement Parser:  Usage](https://kura.pro/stock/images/banners/airam-datoon-12303543.webp).class=\"w-25 fade-in py-2 px-3 float-end\"

```python
from bankstatementparser import CamtParser

# Initialize the parser with the CAMT file path
camt_parser = CamtParser('path/to/camt/file.xml')

# Parse the file and get the results
results = camt_parser.parse()
```

### PAIN.001 Files

```python
from bankstatementparser import Pain001Parser

# Initialize the parser with the PAIN.001 file path
pain_parser = Pain001Parser('path/to/pain/file.xml')

# Parse the file and get the results
results = pain_parser.parse()
```

![divider][divider].class=\"m-10 w-100\"

## Command Line Interface (CLI) Guide

Leverage the CLI for quick parsing tasks with the following commands:

### Basic Command

```bash
python cli.py --type <file_type> --input <input_file> [--output <output_file>]
```

- `--type`: Type of the bank statement file. Currently supported types are "camt" and "pain001".
- `--input`: Path to the bank statement file.
- `--output`: (Optional) Path to save the parsed data. If not provided, data is printed to the console.

### Examples for CAMT Files

1. Parse a CAMT file and print the results to the console:

   ```bash
   python cli.py --type camt --input path/to/camt/camt_file.xml
   ```

   Using the test data:

   ```bash
   python ./bankstatementparser/cli.py --type camt --input ./tests/test_data/camt.053.001.02.xml
   ```

2. Parse a CAMT file and save the results to a CSV file:

   ```bash
   python cli.py --type camt --input path/to/camt/file.xml --output path/to/output/file.csv
   ```

   Using the test data:

   ```bash
   python ./bankstatementparser/cli.py --type camt --input ./tests/test_data/camt.053.001.02.xml --output ./tests/test_data/camt_file.csv
   ```

### Examples for PAIN.001 Files

1. Parse a PAIN.001.001.03 file and print the results to the console:

```bash
python cli.py --type pain001 --input path/to/pain.001.001.03.xml
```

Using the test data:

```bash
python ./bankstatementparser/cli.py --type pain001 --input ./tests/test_data/pain.001.001.03.xml
```

2. Parse a PAIN.001.001.03 file and save the results to a CSV file:

```bash
python cli.py --type pain001 --input path/to/pain.001.001.03.xml --output path/to/output/file.csv
```

Using the test data:

```bash
python ./bankstatementparser/cli.py --type pain001 --input ./tests/test_data/pain.001.001.03.xml --output ./tests/test_data/pain_file.csv
```

[01]: https://github.com/sebastienrousseau/bankstatementparser "Bank Statement Parser on GitHub"
[02]: https://github.com/sebastienrousseau/bankstatementparser/issues "Bank Statement Parser Issues"

[divider]: https://kura.pro/common/images/elements/divider.svg "Divider"
