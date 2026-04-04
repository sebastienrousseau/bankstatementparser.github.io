---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Jurnalul modificărilor analizatorului extras de cont"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/corporate-finance.webp"
cdn: "https://cloudcdn.pro"
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Analizator extras de cont. Toate drepturile rezervate."
date: "Apr 01, 2026"
description: "Istoricul lansărilor și jurnalul de modificări pentru Analizor extras de cont. Urmăriți noile funcții, îmbunătățiri și remedieri de erori în toate versiunile."
download: ""
format-detection: "telephone=no"
hreflang: "ro"
icon: "https://cloudcdn.pro/bankstatementparser/images/favicon.ico"
id: "https://bankstatementparser.com/ro/jurnal-modificari/index.html"
image_alt: "Sigla Analizor extras de cont bancar, împuterniciți-vă analiza financiară cu extragerea fără întreruperi a datelor"
image_height: "630"
image_width: "1200"
image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
keywords: "Jurnalul de modificări pentru analizatorul extrasului de cont bancar, note de lansare, istoricul versiunilor, actualizări"
language: "ro-RO"
layout: "about"
locale: "ro_RO"
logo_alt: "Sigla Analizor extras de cont bancar, împuterniciți-vă analiza financiară cu extragerea fără întreruperi a datelor"
logo_height: "44"
logo_width: "44"
logo: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Jurnalul modificărilor"
permalink: "https://bankstatementparser.com/ro/jurnal-modificari/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Istoricul lansărilor și Noutăți"
tags: "jurnal de modificări, lansări, actualizări, versiuni, anunțuri, blog"
theme_color: "rgb(73, 214, 251)"
title: "Jurnalul modificărilor analizatorului extras de cont"
url: "https://bankstatementparser.com/ro/jurnal-modificari/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/ro/jurnal-modificari/rss.xml"
category: "Software pentru finanțe, Biblioteca Python, Procesarea datelor"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Istoricul lansărilor și jurnalul de modificări pentru Analizor extras de cont. Urmăriți noile funcții, îmbunătățiri și remedieri de erori în toate versiunile."
item_guid: "https://bankstatementparser.com/ro/jurnal-modificari/rss.xml"
item_link: "https://bankstatementparser.com/ro/jurnal-modificari/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Jurnalul modificărilor analizatorului extras de cont"
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
apple-mobile-web-app-title: "Jurnalul modificărilor analizatorului extras de cont"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Istoricul lansărilor și jurnalul de modificări pentru Analizor extras de cont. Urmăriți noile funcții, îmbunătățiri și remedieri de erori în toate versiunile."
twitter_image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
twitter_image_alt: "Sigla Analizor extras de cont bancar, împuterniciți-vă analiza financiară cu extragerea fără întreruperi a datelor"
twitter_site: "@wwdseb"
twitter_title: "Jurnalul modificărilor analizatorului extras de cont"
twitter_url: "https://bankstatementparser.com/ro/jurnal-modificari/index.html"

# Humans.txt - The Humans.txt front matter (YAML).

author_website: "https://bankstatementparser.com"
author_twitter: "@wwdseb"
author_location: "London, UK"
thanks: "Multumesc pentru lectura!"
site_last_updated: "2026-04-01"
site_standards: "HTML5, CSS3, RSS, Atom, JSON, XML, YAML, Markdown, TOML"
site_components: "Shokunin SSG, Shokunin CLI, Shokunin Templates, Shokunin Themes, Kaishi SSG, Kaishi CLI, Kaishi Templates, Kaishi Themes"
site_software: "Shokunin, Rust"

---

Urmăriți dezvoltarea analizei extrasului de cont. Abonați-vă prin [RSS](/changelog/rss.xml) sau urmăriți [repozitivul GitHub](https://github.com/sebastienrousseau/bankstatementparser) pentru notificări de lansare.

## v0.0.4 — 2026-03-15 (cel mai recent)

- S-a adăugat analiza paralelă a fișierelor cu`parse_files_parallel()`folosind ProcessPoolExecutor.
- S-a adăugat fluxul real pentru fișiere mari PAIN.001 (50 MB+) cu memorie limitată.
- Optimizări de performanță: debitul CAMT depășește acum 27.000 tx/s, PAIN.001 depășește 52.000 tx/s.
- Adăugat`Deduplicator`clasă pentru detectarea dublurilor exacte și a potrivirilor suspecte cu scoruri de încredere.
- Adăugat`from_string()`şi`from_bytes()`metode pentru analizarea în memorie fără I/O pe disc.
- Adăugat`iter_secure_xml_entries()`pentru procesarea securizată a arhivei ZIP.
- CI extins cu aplicarea pragului de performanță.

## v0.0.3 — 2025-11-20

- S-a adăugat suport pentru analizatorul CSV, OFX, QFX și MT940.
- A fost adăugată detectarea automată a formatului cu`detect_statement_format()`şi`create_parser()`.
- S-a adăugat redarea PII (activată implicit în modul CLI și streaming).
- S-au adăugat ajutoare de export pentru CSV, JSON și Excel.
- S-a adăugat suport opțional Polars DataFrame.
- Suita de teste extinsă la 467 de teste cu acoperire de 100% a ramurilor.

## v0.0.2 — 2025-06-10

- S-a adăugat analizatorul PAIN.001 (`Pain001Parser`) pentru dosarele de inițiere a transferului de credite ISO 20022.
- S-a adăugat interfață CLI (`python -m bankstatementparser.cli`).
- S-a adăugat modul de streaming cu`parse_streaming()`.
- S-au adăugat validarea intrării și limitele de dimensiune a fișierului.

## v0.0.1 — 2025-01-15

- Lansare inițială.
- Analizor CAMT.053 (`CamtParser`) pentru extrasele de cont de la bancă la client conform ISO 20022.
- ieșire Pandas DataFrame.
- Întărirea securității XML de bază (protecție XXE, no_network).

Vizualizați istoricul complet al comitărilor pe [GitHub](https://github.com/sebastienrousseau/bankstatementparser/commits/main).

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Aplicație software",
  "name": "Analizator extras de cont",
  "applicationCategory": "DeveloperApplication",
  "operatingSystem": "Merce platformă",
  „softwareVersion”: „0.0.4”,
  "datePublished": "2026-03-15",
  "releaseNotes": "Adăugat parsare paralelă a fișierelor, streaming real pentru PAIN.001, optimizări ale performanței (27K+ tx/s CAMT, 52K+ tx/s PAIN.001), clasa Deduplicator, analizare în memorie, procesare ZIP sigură.",
  "downloadUrl": "https://pypi.org/project/bankstatementparser/",
  "licență": "https://opensource.org/licenses/Apache-2.0",
  „autor”: {
    „@type”: „Persoană”,
    „nume”: „Sebastien Rousseau”
  }
}
</script>
