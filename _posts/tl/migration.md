---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "ISO 20022 Migration Guide"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Bank Statement Parser. Lahat ng karapatan ay nakalaan."
date: "Apr 11, 2026"
description: "Isang praktikal na gabay sa SWIFT ISO 20022 migration timeline (2026-2028), MT940 hanggang CAMT.053 transition, at kung paano tinutulungan ng Bank Statement Parser ang mga treasury team na lumipat."
download: ""
format-detection: "telephone=no"
hreflang: "tl"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/tl/migration/index.html"
image_alt: "Logo ng Bank Statement Parser, Bigyan ang Iyong Pagsusuri sa Pananalapi gamit ang Seamless Data Extraction"
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "ISO 20022 migration, MT940 to CAMT.053, SWIFT deadline 2027, MT940 retirement 2028, bank statement migration python, CAMT.053 parser, ISO 20022 timeline"
language: "tl-PH"
layout: "about"
locale: "tl_PH"
logo_alt: "Logo ng Bank Statement Parser, Bigyan ang Iyong Pagsusuri sa Pananalapi gamit ang Seamless Data Extraction"
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "ISO 20022 Migration Guide"
permalink: "https://bankstatementparser.com/tl/migration/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "I-navigate ang SWIFT MT sa ISO 20022 Transition"
tags: "iso20022,migration,mt940,camt053,swift,timeline"
theme_color: "rgb(73, 214, 251)"
title: "ISO 20022 Migration Guide: MT940 hanggang CAMT.053 Transition"
url: "https://bankstatementparser.com/tl/migration/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/tl/migration/rss.xml"
category: "Software sa Pananalapi, Python Library, Pagproseso ng Data"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Isang praktikal na gabay sa SWIFT ISO 20022 migration timeline (2026-2028), MT940 hanggang CAMT.053 transition, at kung paano tinutulungan ng Bank Statement Parser ang mga treasury team na lumipat."
item_guid: "https://bankstatementparser.com/tl/migration/rss.xml"
item_link: "https://bankstatementparser.com/tl/migration/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "ISO 20022 Migration Guide: MT940 hanggang CAMT.053 Transition"
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
apple-mobile-web-app-title: "ISO 20022 Migration Guide: MT940 hanggang CAMT.053 Transition"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Isang praktikal na gabay sa SWIFT ISO 20022 migration timeline (2026-2028), MT940 hanggang CAMT.053 transition, at kung paano tinutulungan ng Bank Statement Parser ang mga treasury team na lumipat."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logo ng Bank Statement Parser, Bigyan ang Iyong Pagsusuri sa Pananalapi gamit ang Seamless Data Extraction"
twitter_site: "@wwdseb"
twitter_title: "ISO 20022 Migration Guide: MT940 hanggang CAMT.053 Transition"
twitter_url: "https://bankstatementparser.com/tl/migration/index.html"

# Humans.txt - The Humans.txt front matter (YAML).

author_website: "https://bankstatementparser.com"
author_twitter: "@wwdseb"
author_location: "London, UK"
thanks: "Salamat sa pagbabasa!"
site_last_updated: "2026-04-01"
site_standards: "HTML5, CSS3, RSS, Atom, JSON, XML, YAML, Markdown, TOML"
site_components: "Shokunin SSG, Shokunin CLI, Shokunin Templates, Shokunin Themes, Kaishi SSG, Kaishi CLI, Kaishi Templates, Kaishi Themes"
site_software: "Shokunin, Rust"

---

**TL;DR:** Iretiro ng SWIFT ang MT940 bago ang Nobyembre 2028. Pinangangasiwaan ng Bank Statement Parser ang MT940 at CAMT.053 gamit ang iisang API, kaya gumagana ang iyong parsing pipeline sa panahon ng transisyon at pagkatapos nito.

## Bakit Mahalaga ang Migration na Ito

Ihihinto ng SWIFT ang mga legacy na MT message format pabor sa mas mayamang ISO 20022 standard. Para sa mga treasury at finance team, nangangahulugan ito na ang iyong mga bank statement processing pipeline ay dapat mag-evolve mula MT940 patungong CAMT.053 bago ang mga matatag na deadline.

## SWIFT Migration Timeline

| Petsa | Milestone | Epekto |
|---|---|---|
| **Nobyembre 2025** | Natapos ang MT-to-MX coexistence para sa mga cross-border na pagbabayad | Ang mga PACS message ay ISO 20022 na lamang |
| **Nobyembre 2026** | Mandatory ang mga structured/hybrid address; tinatanggihan ang MT101 multi-instruction; Case Management Phase 1 | Dapat sumunod ang mga address format; ilang MT message ay tatanggihan |
| **Huling bahagi ng 2026** | Magsisimula ang opt-in para sa pagtanggap ng CAMT.052/.053/.054 | Maaaring magsimulang tumanggap ang mga institusyong pinansyal ng mga native na ISO statement |
| **Nobyembre 2027** | Lahat ng FI ay dapat makatanggap ng CAMT.053 nang native | Ihihinto ng SWIFT ang pag-convert ng MT format sa ISO; dapat direktang i-parse ng iyong mga system ang CAMT |
| **Nobyembre 2028** | MT940/MT942/MT950/MT900/MT910 ganap na nagretiro | Hindi na available ang mga legacy statement format; CAMT.052/.053/.054 ang tanging opsyon |

## Anong mga Pagbabago para sa Iyong Code

### Bago: MT940 Lamang

```python
from bankstatementparser import Mt940Parser

parser = Mt940Parser("statement.mt940")
df = parser.parse()
```

### Pagkatapos: Parehong Format na may Auto-Detection

```python
from bankstatementparser import create_parser, detect_statement_format

fmt = detect_statement_format("statement.xml")  # or .mt940
parser = create_parser("statement.xml", fmt)
df = parser.parse()  # Same DataFrame schema regardless of format
```

Kinikilala ng `detect_statement_format()` function kung ang file ay MT940, CAMT.053, PAIN.001, o anumang iba pang sinusuportahang format. Ibinabalik ng `create_parser()` function ang tamang parser. Gumagana ang iyong downstream code nang magkapareho anuman ang source format.

## CAMT.053 vs MT940: Mga Pangunahing Pagkakaiba

| Tampok | MT940 | CAMT.053 |
|---|---|---|
| Kayamanan ng data | Limitadong mga field | 3-5x na mas maraming data bawat transaksyon |
| Character set | Limitado (SWIFT charset) | Buong Unicode |
| Istruktura | Flat text na may mga tag | XML na may mga namespace |
| Pag-uulat ng balanse | Opening/closing lamang | Maramihang uri ng balanse |
| Mga sanggunian | Isang reference field | Maramihang uri ng reference |
| Paghawak ng currency | Basic | Buong multi-currency na may mga exchange rate |

## Paano Nakakatulong ang Bank Statement Parser

- **Unified API**: I-parse ang MT940, CAMT.053, at mga PDF statement gamit ang parehong workflow, na gumagawa ng consistent na DataFrame output.
- **Auto-detection**: Hindi kailangang malaman ang format nang maaga. Awtomatikong kinikilala ito ng `detect_statement_format()`.
- **Hybrid PDF pipeline**: Pinangangasiwaan ng `smart_ingest()` ang mga bangko na nagbibigay ng PDF-only na statement sa panahon ng transisyon, na may awtomatikong beripikasyon ng balanse.
- **Namespace-agnostic**: Pinangangasiwaan ang anumang CAMT.053 variant (001.02, 001.04, o bank-specific na wrapper) nang walang configuration.
- **Multi-currency na beripikasyon**: Pinapatakbo ng `verify_balance_multi_currency()` ang Golden Rule sa bawat currency group — mahalaga para sa multi-currency na CAMT statement.
- **Streaming**: Iproseso ang malalaking CAMT file (50 MB+, 50K+ na transaksyon) na may bounded memory.
- **Ledger export**: Direktang i-export sa hledger o beancount journal format para sa treasury accounting.
- **Pagsusuri sa migration**: Patakbuhin ang parehong parser nang magkatabi sa parehong date range upang i-verify ang consistency ng output bago lumipat.

## Pagsisimula

```bash
pip install bankstatementparser
```

```python
from bankstatementparser import create_parser, detect_statement_format

# Works with MT940 today, CAMT.053 tomorrow, PDF anytime
for file in bank_statement_files:
    fmt = detect_statement_format(file)
    parser = create_parser(file, fmt)
    df = parser.parse()
    process(df)  # Your code doesn't change
```

Para sa mga PDF statement mula sa mga bangko na hindi pa nag-aalok ng structured na CAMT export:

```python
from bankstatementparser.hybrid import smart_ingest

result = smart_ingest("statement.pdf")
assert result.verification.status == "VERIFIED"
```

[Basahin ang buong dokumentasyon](/getting-started/index.html)

[Ihambing sa mga alternatibo ❯](/comparison/index.html) | [Tingnan ang mga real-world use case ❯](/use-cases/index.html)
