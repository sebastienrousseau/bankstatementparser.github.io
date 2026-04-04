---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Guida alla migrazione ISO 20022"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Analizzatore di estratti conto bancari. Tutti i diritti riservati."
date: "Apr 01, 2026"
description: "Una guida pratica alla cronologia della migrazione SWIFT ISO 20022 (2026-2028), alla transizione da MT940 a CAMT.053 e al modo in cui Bank Statement Parser aiuta i team di tesoreria a migrare."
download: ""
format-detection: "telephone=no"
hreflang: "it"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/it/migration/index.html"
image_alt: "Logo di Parser estratto conto, potenzia la tua analisi finanziaria con l'estrazione dei dati senza interruzioni"
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "Migrazione ISO 20022, da MT940 a CAMT.053, scadenza SWIFT 2027, ritiro MT940 2028, migrazione estratto conto Python, parser CAMT.053, sequenza temporale ISO 20022"
language: "it-IT"
layout: "about"
locale: "it_IT"
logo_alt: "Logo di Parser estratto conto, potenzia la tua analisi finanziaria con l'estrazione dei dati senza interruzioni"
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Guida alla migrazione ISO 20022"
permalink: "https://bankstatementparser.com/it/migration/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Naviga nella transizione da SWIFT MT a ISO 20022"
tags: "iso20022,migrazione,mt940,camt053,veloce,sequenza temporale"
theme_color: "rgb(73, 214, 251)"
title: "Guida alla migrazione ISO 20022: transizione da MT940 a CAMT.053"
url: "https://bankstatementparser.com/it/migration/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/it/migration/rss.xml"
category: "Software finanziario, libreria Python, elaborazione dati"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin (version 0.0.20)"
item_description: "Una guida pratica alla cronologia della migrazione SWIFT ISO 20022 (2026-2028), alla transizione da MT940 a CAMT.053 e al modo in cui Bank Statement Parser aiuta i team di tesoreria a migrare."
item_guid: "https://bankstatementparser.com/it/migration/rss.xml"
item_link: "https://bankstatementparser.com/it/migration/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Guida alla migrazione ISO 20022: transizione da MT940 a CAMT.053"
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
apple-mobile-web-app-title: "Guida alla migrazione ISO 20022: transizione da MT940 a CAMT.053"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Una guida pratica alla cronologia della migrazione SWIFT ISO 20022 (2026-2028), alla transizione da MT940 a CAMT.053 e al modo in cui Bank Statement Parser aiuta i team di tesoreria a migrare."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logo di Parser estratto conto, potenzia la tua analisi finanziaria con l'estrazione dei dati senza interruzioni"
twitter_site: "@wwdseb"
twitter_title: "Guida alla migrazione ISO 20022: transizione da MT940 a CAMT.053"
twitter_url: "https://bankstatementparser.com/it/migration/index.html"

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

**TL;DR:** SWIFT ritirerà MT940 entro novembre 2028. Bank Statement Parser gestisce sia MT940 che CAMT.053 con un'unica API, quindi la pipeline di analisi funziona durante e dopo la transizione.

## Perché questa migrazione è importante

SWIFT sta ritirando i formati di messaggi MT legacy a favore del più ricco standard ISO 20022. Per i team di tesoreria e finanza, ciò significa che le pipeline di elaborazione degli estratti conto bancari devono evolversi da MT940 a CAMT.053 prima delle scadenze rigide.

## Cronologia della migrazione SWIFT

| Data | Pietra miliare | Impatto |
|---|---|---|
| **Novembre 2025** | La coesistenza MT-MX è terminata per i pagamenti transfrontalieri | I messaggi PACS ora sono solo ISO 20022 |
| **Novembre 2026** | Indirizzi strutturati/ibridi obbligatori; Multiistruzione MT101 rifiutata; Fase di gestione del caso 1 | I formati degli indirizzi devono essere conformi; alcuni messaggi MT verranno rifiutati |
| **Fine 2026** | Inizia l'attivazione per ricevere CAMT.052/.053/.054 | Gli istituti finanziari possono iniziare a ricevere dichiarazioni ISO native |
| **Novembre 2027** | Tutti gli FI devono ricevere CAMT.053 nativamente | SWIFT interrompe la conversione del formato MT in ISO; i tuoi sistemi devono analizzare direttamente CAMT |
| **Novembre 2028** | MT940/MT942/MT950/MT900/MT910 completamente in pensione | I formati di dichiarazione legacy non sono più disponibili; CAMT.052/.053/.054 sono l'unica opzione |

## Cosa cambia per il tuo codice

### Prima: solo MT940

```python
from bankstatementparser import Mt940Parser

parser = Mt940Parser("statement.mt940")
df = parser.parse()
```

### Dopo: entrambi i formati con rilevamento automatico

```python
from bankstatementparser import create_parser, detect_statement_format

fmt = detect_statement_format("statement.xml")  # or .mt940
parser = create_parser("statement.xml", fmt)
df = parser.parse()  # Same DataFrame schema regardless of format
```

IL`detect_statement_format()`La funzione identifica se il file è MT940, CAMT.053, PAIN.001 o qualsiasi altro formato supportato. IL`create_parser()`la funzione restituisce il parser corretto. Il tuo codice downstream funziona in modo identico indipendentemente dal formato sorgente.

## CAMT.053 vs MT940: differenze chiave

| Caratteristica | MT940 | CAMT.053 |
|---|---|---|
| Ricchezza di dati | Campi limitati | 3-5 volte più dati per transazione |
| Set di caratteri | Limitato (set di caratteri SWIFT) | Unicode completo |
| Struttura | Testo piatto con tag | XML con spazi dei nomi |
| Reporting del saldo | Solo apertura/chiusura | Diversi tipi di equilibrio |
| Riferimenti | Campo di riferimento unico | Tipi di riferimento multipli |
| Gestione valutaria | Di base | Multivaluta completa con tassi di cambio |

## Come aiuta il parser dell'estratto conto

- **API unificata**: analizza sia MT940 che CAMT.053 con lo stesso`parse()`metodo, producendo schemi DataFrame identici.
- **Rilevamento automatico**: non è necessario conoscere il formato in anticipo.`detect_statement_format()`lo identifica automaticamente.
- **Indipendente dallo spazio dei nomi**: gestisce qualsiasi variante CAMT.053 (001.02, 001.04 o wrapper specifici della banca) senza configurazione.
- **Streaming**: elabora file CAMT di grandi dimensioni (50 MB+, 50.000+ transazioni) con memoria limitata.
- **Test di migrazione**: esegui entrambi i parser fianco a fianco nello stesso intervallo di date per verificare la coerenza dell'output prima del passaggio.

## Iniziare

```bash
pip install bankstatementparser
```

```python
from bankstatementparser import create_parser, detect_statement_format

# Works with MT940 today, CAMT.053 tomorrow
for file in bank_statement_files:
    fmt = detect_statement_format(file)
    parser = create_parser(file, fmt)
    df = parser.parse()
    process(df)  # Your code doesn't change
```

[Leggi la documentazione completa](/getting-started/index.html)

[Confronta con alternative ❯](/comparison/index.html) | [Vedi casi d'uso reali ❯](/use-cases/index.html)
