---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Bank Statement Parser Changelog"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/corporate-finance.webp"
cdn: "https://cloudcdn.pro"
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Bank Statement Parser. Lahat ng karapatan ay nakalaan."
date: "Apr 01, 2026"
description: "History ng release at changelog para sa Bank Statement Parser. Subaybayan ang mga bagong feature, pagpapahusay, at pag-aayos ng bug sa lahat ng bersyon."
download: ""
format-detection: "telephone=no"
hreflang: "tl"
icon: "https://cloudcdn.pro/bankstatementparser/images/favicon.ico"
id: "https://bankstatementparser.com/tl/journal-des-modifications/index.html"
image_alt: "Logo ng Bank Statement Parser, Bigyan ang Iyong Pagsusuri sa Pananalapi gamit ang Seamless Data Extraction"
image_height: "630"
image_width: "1200"
image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
keywords: "bank statement parser changelog, mga tala sa paglabas, kasaysayan ng bersyon, mga update"
language: "tl-PH"
layout: "about"
locale: "tl_PH"
logo_alt: "Logo ng Bank Statement Parser, Bigyan ang Iyong Pagsusuri sa Pananalapi gamit ang Seamless Data Extraction"
logo_height: "44"
logo_width: "44"
logo: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Changelog"
permalink: "https://bankstatementparser.com/tl/journal-des-modifications/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Kasaysayan ng Paglabas at Ano ang Bago"
tags: "changelog,release,update,bersyon,anunsyo,blog"
theme_color: "rgb(73, 214, 251)"
title: "Bank Statement Parser Changelog"
url: "https://bankstatementparser.com/tl/journal-des-modifications/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/tl/journal-des-modifications/rss.xml"
category: "Software sa Pananalapi, Python Library, Pagproseso ng Data"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "History ng release at changelog para sa Bank Statement Parser. Subaybayan ang mga bagong feature, pagpapahusay, at pag-aayos ng bug sa lahat ng bersyon."
item_guid: "https://bankstatementparser.com/tl/journal-des-modifications/rss.xml"
item_link: "https://bankstatementparser.com/tl/journal-des-modifications/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Bank Statement Parser Changelog"
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
apple-mobile-web-app-title: "Bank Statement Parser Changelog"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "History ng release at changelog para sa Bank Statement Parser. Subaybayan ang mga bagong feature, pagpapahusay, at pag-aayos ng bug sa lahat ng bersyon."
twitter_image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logo ng Bank Statement Parser, Bigyan ang Iyong Pagsusuri sa Pananalapi gamit ang Seamless Data Extraction"
twitter_site: "@wwdseb"
twitter_title: "Bank Statement Parser Changelog"
twitter_url: "https://bankstatementparser.com/tl/journal-des-modifications/index.html"

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

Sundin ang Bank Statement Parser development. Mag-subscribe sa pamamagitan ng [RSS](/changelog/rss.xml) o panoorin ang [GitHub repository](https://github.com/sebastienrousseau/bankstatementparser) para sa mga abiso sa pagpapalabas.

## v0.0.4 — 2026-03-15 (Pinakabago)

- Idinagdag ang parallel na pag-parse ng file sa`parse_files_parallel()`gamit ang ProcessPoolExecutor.
- Nagdagdag ng totoong streaming para sa malalaking PAIN.001 na file (50 MB+) na may bounded memory.
- Mga pag-optimize ng performance: Ang throughput ng CAMT ay lumampas na ngayon sa 27,000 tx/s, ang PAIN.001 ay lumampas sa 52,000 tx/s.
- Idinagdag`Deduplicator`klase para sa pag-detect ng mga eksaktong duplicate at pinaghihinalaang mga tugma na may mga marka ng kumpiyansa.
- Idinagdag`from_string()`at`from_bytes()`mga pamamaraan para sa in-memory na pag-parse nang walang disk I/O.
- Idinagdag`iter_secure_xml_entries()`para sa secure na pagpoproseso ng ZIP archive.
- Pinalawak na CI na may pagpapatupad ng threshold ng pagganap.

## v0.0.3 — 2025-11-20

- Nagdagdag ng suporta sa CSV, OFX, QFX, at MT940 parser.
- Nagdagdag ng format na auto-detection gamit ang`detect_statement_format()`at`create_parser()`.
- Nagdagdag ng PII redaction (naka-on bilang default sa CLI at streaming mode).
- Nagdagdag ng mga katulong sa pag-export para sa CSV, JSON, at Excel.
- Nagdagdag ng opsyonal na suporta sa Polars DataFrame.
- Pinalawak na test suite sa 467 na pagsubok na may 100% branch coverage.

## v0.0.2 — 2025-06-10

- Nagdagdag ng PAIN.001 parser (`Pain001Parser`) para sa ISO 20022 na mga file ng pagsisimula ng paglilipat ng kredito.
- Idinagdag ang interface ng CLI (`python -m bankstatementparser.cli`).
- Nagdagdag ng streaming mode na may`parse_streaming()`.
- Nagdagdag ng pagpapatunay ng input at mga limitasyon sa laki ng file.

## v0.0.1 — 2025-01-15

- Paunang paglabas.
- CAMT.053 parser (`CamtParser`) para sa ISO 20022 bank-to-customer statement.
- Pandas DataFrame output.
- Basic XML security hardening (XXE protection, no_network).

Tingnan ang buong kasaysayan ng commit sa [GitHub](https://github.com/sebastienrousseau/bankstatementparser/commits/main).

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "Bank Statement Parser",
  "applicationCategory": "DeveloperApplication",
  "operatingSystem": "Cross-platform",
  "softwareVersion": "0.0.4",
  "datePublished": "2026-03-15",
  "releaseNotes": "Idinagdag ang parallel na pag-parse ng file, totoong streaming para sa PAIN.001, mga pag-optimize ng pagganap (27K+ tx/s CAMT, 52K+ tx/s PAIN.001), klase ng Deduplicator, in-memory na pag-parse, secure na pagproseso ng ZIP.",
  "downloadUrl": "https://pypi.org/project/bankstatementparser/",
  "lisensya": "https://opensource.org/licenses/Apache-2.0",
  "may-akda": {
    "@type": "Tao",
    "pangalan": "Sebastien Rousseau"
  }
}
</script>
