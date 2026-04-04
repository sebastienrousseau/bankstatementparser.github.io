---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Ändringslogg för kontoutdrag Parser"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Bank Statement Parser. Alla rättigheter reserverade."
date: "Apr 01, 2026"
description: "Utgivningshistorik och ändringslogg för Bank Statement Parser. Spåra nya funktioner, förbättringar och buggfixar i alla versioner."
download: ""
format-detection: "telephone=no"
hreflang: "sv"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/sv/journal-des-modifications/index.html"
image_alt: "Logotyp för Bank Statement Parser, styrka din finansiella analys med sömlös dataextraktion"
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "ändringslogg för kontoutdragsparser, release notes, versionshistorik, uppdateringar"
language: "sv-SE"
layout: "about"
locale: "sv_SE"
logo_alt: "Logotyp för Bank Statement Parser, styrka din finansiella analys med sömlös dataextraktion"
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Ändringslogg"
permalink: "https://bankstatementparser.com/sv/journal-des-modifications/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Releasehistorik och vad som är nytt"
tags: "ändringslogg, releaser, uppdateringar, versioner, meddelanden, blogg"
theme_color: "rgb(73, 214, 251)"
title: "Ändringslogg för kontoutdrag Parser"
url: "https://bankstatementparser.com/sv/journal-des-modifications/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/sv/journal-des-modifications/rss.xml"
category: "Finansprogram, Python-bibliotek, databehandling"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Utgivningshistorik och ändringslogg för Bank Statement Parser. Spåra nya funktioner, förbättringar och buggfixar i alla versioner."
item_guid: "https://bankstatementparser.com/sv/journal-des-modifications/rss.xml"
item_link: "https://bankstatementparser.com/sv/journal-des-modifications/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Ändringslogg för kontoutdrag Parser"
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
apple-mobile-web-app-title: "Ändringslogg för kontoutdrag Parser"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Utgivningshistorik och ändringslogg för Bank Statement Parser. Spåra nya funktioner, förbättringar och buggfixar i alla versioner."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logotyp för Bank Statement Parser, styrka din finansiella analys med sömlös dataextraktion"
twitter_site: "@wwdseb"
twitter_title: "Ändringslogg för kontoutdrag Parser"
twitter_url: "https://bankstatementparser.com/sv/journal-des-modifications/index.html"

# Humans.txt - The Humans.txt front matter (YAML).

author_website: "https://bankstatementparser.com"
author_twitter: "@wwdseb"
author_location: "London, UK"
thanks: "Tack för att du läste!"
site_last_updated: "2026-04-01"
site_standards: "HTML5, CSS3, RSS, Atom, JSON, XML, YAML, Markdown, TOML"
site_components: "Shokunin SSG, Shokunin CLI, Shokunin Templates, Shokunin Themes, Kaishi SSG, Kaishi CLI, Kaishi Templates, Kaishi Themes"
site_software: "Shokunin, Rust"

---

Följ utvecklingen av Bank Statement Parser. Prenumerera via [RSS](/changelog/rss.xml) eller titta på [GitHub-arkivet](https://github.com/sebastienrousseau/bankstatementparser) för releasemeddelanden.

## v0.0.4 — 2026-03-15 (senast)

- Lade till parallell filanalys med`parse_files_parallel()`med ProcessPoolExecutor.
- Lagt till sann streaming för stora PAIN.001-filer (50 MB+) med begränsat minne.
- Prestandaoptimeringar: CAMT-genomströmningen överstiger nu 27 000 tx/s, PAIN.001 överstiger 52 000 tx/s.
- Tillagd`Deduplicator`klass för att upptäcka exakta dubbletter och misstänkta matchningar med konfidenspoäng.
- Tillagd`from_string()`och`from_bytes()`metoder för in-memory parsing utan disk I/O.
- Tillagd`iter_secure_xml_entries()`för säker ZIP-arkivbehandling.
- Utökad CI med upprätthållande av prestationströskel.

## v0.0.3 — 2025-11-20

- Lade till CSV, OFX, QFX och MT940 parserstöd.
- Lade till format automatisk upptäckt med`detect_statement_format()`och`create_parser()`.
- Tillagd PII-redigering (på som standard i CLI och streamingläge).
- Lade till exporthjälpmedel för CSV, JSON och Excel.
- Tillagt valfritt Polars DataFrame-stöd.
- Utökad testsvit till 467 tester med 100 % grentäckning.

## v0.0.2 — 2025-06-10

- Lade till PAIN.001 parser (`Pain001Parser`) för ISO 20022 initieringsfiler för kreditöverföring.
- Tillagt CLI-gränssnitt (`python -m bankstatementparser.cli`).
- Lade till streamingläge med`parse_streaming()`.
- Lade till indatavalidering och filstorleksgränser.

## v0.0.1 — 2025-01-15

- Första release.
- CAMT.053 parser (`CamtParser`) för ISO 20022 bank-till-kund-utdrag.
- pandas DataFrame-utgång.
- Grundläggande XML-säkerhetshärdning (XXE-skydd, inget_nätverk).

Se den fullständiga historiken på [GitHub](https://github.com/sebastienrousseau/bankstatementparser/commits/main).

<script type="application/ld+json">
{
  "@kontext": "https://schema.org",
  "@type": "Programprogram",
  "name": "Bankutdragstolkare",
  "applicationCategory": "Utvecklarapplikation",
  "operatingSystem": "Platsöverskridande",
  "softwareVersion": "0.0.4",
  "datePublished": "2026-03-15",
  "releaseNotes": "Lade till parallell filanalys, sann streaming för PAIN.001, prestandaoptimeringar (27K+ tx/s CAMT, 52K+ tx/s PAIN.001), Deduplicator-klass, in-memory parsing, säker ZIP-bearbetning.",
  "downloadUrl": "https://pypi.org/project/bankstatementparser/",
  "licens": "https://opensource.org/licenses/Apache-2.0",
  "författare": {
    "@type": "Person",
    "name": "Sebastien Rousseau"
  }
}
</script>
