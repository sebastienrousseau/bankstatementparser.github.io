---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Registro modifiche parser estratto conto"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/corporate-finance.webp"
cdn: "https://cloudcdn.pro"
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Analizzatore di estratti conto bancari. Tutti i diritti riservati."
date: "Apr 01, 2026"
description: "Cronologia delle versioni e registro delle modifiche per Parser estratto conto bancario. Tieni traccia di nuove funzionalità, miglioramenti e correzioni di bug in tutte le versioni."
download: ""
format-detection: "telephone=no"
hreflang: "it"
icon: "https://cloudcdn.pro/bankstatementparser/images/favicon.ico"
id: "https://bankstatementparser.com/it/changelog/index.html"
image_alt: "Logo di Parser estratto conto, potenzia la tua analisi finanziaria con l'estrazione dei dati senza interruzioni"
image_height: "630"
image_width: "1200"
image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
keywords: "Registro delle modifiche del parser dell'estratto conto, note di rilascio, cronologia delle versioni, aggiornamenti"
language: "it-IT"
layout: "about"
locale: "it_IT"
logo_alt: "Logo di Parser estratto conto, potenzia la tua analisi finanziaria con l'estrazione dei dati senza interruzioni"
logo_height: "44"
logo_width: "44"
logo: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Registro delle modifiche"
permalink: "https://bankstatementparser.com/it/changelog/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Cronologia delle versioni e novità"
tags: "log delle modifiche, rilasci, aggiornamenti, versioni, annunci, blog"
theme_color: "rgb(73, 214, 251)"
title: "Registro modifiche parser estratto conto"
url: "https://bankstatementparser.com/it/changelog/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/it/changelog/rss.xml"
category: "Software finanziario, libreria Python, elaborazione dati"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin (version 0.0.20)"
item_description: "Cronologia delle versioni e registro delle modifiche per Parser estratto conto bancario. Tieni traccia di nuove funzionalità, miglioramenti e correzioni di bug in tutte le versioni."
item_guid: "https://bankstatementparser.com/it/changelog/rss.xml"
item_link: "https://bankstatementparser.com/it/changelog/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Registro modifiche parser estratto conto"
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
apple-mobile-web-app-title: "Registro modifiche parser estratto conto"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Cronologia delle versioni e registro delle modifiche per Parser estratto conto bancario. Tieni traccia di nuove funzionalità, miglioramenti e correzioni di bug in tutte le versioni."
twitter_image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logo di Parser estratto conto, potenzia la tua analisi finanziaria con l'estrazione dei dati senza interruzioni"
twitter_site: "@wwdseb"
twitter_title: "Registro modifiche parser estratto conto"
twitter_url: "https://bankstatementparser.com/it/changelog/index.html"

# Humans.txt - The Humans.txt front matter (YAML).

author_website: "https://bankstatementparser.com"
author_twitter: "@wwdseb"
author_location: "London, UK"
thanks: "Grazie per aver letto!"
site_last_updated: "2026-04-01"
site_standards: "HTML5, CSS3, RSS, Atom, JSON, XML, YAML, Markdown, TOML"
site_components: "Shokunin SSG, Shokunin CLI, Shokunin Templates, Shokunin Themes, Kaishi SSG, Kaishi CLI, Kaishi Templates, Kaishi Themes"
site_software: "Shokunin, Rust"

---

Segui lo sviluppo del parser estratto conto bancario. Iscriviti tramite [RSS](/changelog/rss.xml) o guarda il [repository GitHub](https://github.com/sebastienrousseau/bankstatementparser) per le notifiche di rilascio.

## v0.0.4 — 15-03-2026 (più recente)

- Aggiunta l'analisi di file paralleli con`parse_files_parallel()`utilizzando ProcessPoolExecutor.
- Aggiunto il vero streaming per file PAIN.001 di grandi dimensioni (50 MB+) con memoria limitata.
- Ottimizzazioni delle prestazioni: il throughput CAMT ora supera 27.000 tx/s, PAIN.001 supera 52.000 tx/s.
- Aggiunto`Deduplicator`classe per rilevare duplicati esatti e corrispondenze sospette con punteggi di confidenza.
- Aggiunto`from_string()`E`from_bytes()`metodi per l'analisi in memoria senza I/O del disco.
- Aggiunto`iter_secure_xml_entries()`per l'elaborazione sicura dell'archivio ZIP.
- CI estesa con applicazione della soglia prestazionale.

## v0.0.3 — 20/11/2025

- Aggiunto il supporto per parser CSV, OFX, QFX e MT940.
- Aggiunto rilevamento automatico del formato con`detect_statement_format()`E`create_parser()`.
- Aggiunta la redazione PII (attiva per impostazione predefinita nella CLI e in modalità streaming).
- Aggiunti aiutanti di esportazione per CSV, JSON ed Excel.
- Aggiunto il supporto opzionale Polars DataFrame.
- Suite di test estesa a 467 test con copertura delle filiali del 100%.

## v0.0.2 — 10/06/2025

- Aggiunto il parser PAIN.001 (`Pain001Parser`) per i file di avvio del bonifico ISO 20022.
- Aggiunta interfaccia CLI (`python -m bankstatementparser.cli`).
- Aggiunta la modalità streaming con`parse_streaming()`.
- Aggiunta la convalida dell'input e i limiti delle dimensioni dei file.

## v0.0.1 — 15-01-2025

- Rilascio iniziale.
- Analizzatore CAMT.053 (`CamtParser`) per gli estratti conto banca-cliente ISO 20022.
- Uscita DataFrame di Panda.
- Rafforzamento della sicurezza XML di base (protezione XXE, no_network).

Visualizza la cronologia completa dei commit su [GitHub](https://github.com/sebastienrousseau/bankstatementparser/commits/main).

<script type="application/ld+json">
{
  "@contesto": "https://schema.org",
  "@type": "ApplicazioneSoftware",
  "name": "Paser estratto conto",
  "applicationCategory": "ApplicazioneSviluppatore",
  "operatingSystem": "Multipiattaforma",
  "versionesoftware": "0.0.4",
  "dataPubblicazione": "2026-03-15",
  "releaseNotes": "Aggiunta analisi di file paralleli, streaming reale per PAIN.001, ottimizzazioni delle prestazioni (27.000+ tx/s CAMT, 52.000+ tx/s PAIN.001), classe deduplicatore, analisi in memoria, elaborazione ZIP sicura.",
  "Url download": "https://pypi.org/project/bankstatementparser/",
  "licenza": "https://opensource.org/licenses/Apache-2.0",
  "autore": {
    "@type": "Persona",
    "nome": "Sebastien Rousseau"
  }
}
</script>
