---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Sicurezza del parser dell'estratto conto bancario"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/corporate-finance.webp"
cdn: "https://cloudcdn.pro"
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Analizzatore di estratti conto bancari. Tutti i diritti riservati."
date: "Apr 01, 2026"
description: "Funzionalità di sicurezza dell'analizzatore di estratti conto: protezione XXE, rafforzamento della bomba ZIP, redazione PII, sicurezza della catena di fornitura, output deterministico e build firmate."
download: ""
format-detection: "telephone=no"
hreflang: "it"
icon: "https://cloudcdn.pro/bankstatementparser/images/favicon.ico"
id: "https://bankstatementparser.com/it/sicurezza/index.html"
image_alt: "Logo di Parser estratto conto, potenzia la tua analisi finanziaria con l'estrazione dei dati senza interruzioni"
image_height: "630"
image_width: "1200"
image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
keywords: "sicurezza dell'estratto conto, Python per la redazione delle PII, protezione XXE, protezione ZIP bomb, sicurezza della catena di fornitura SBOM, analisi deterministica, sicurezza dei dati finanziari"
language: "it-IT"
layout: "about"
locale: "it_IT"
logo_alt: "Logo di Parser estratto conto, potenzia la tua analisi finanziaria con l'estrazione dei dati senza interruzioni"
logo_height: "44"
logo_width: "44"
logo: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Sicurezza"
permalink: "https://bankstatementparser.com/it/sicurezza/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Come proteggiamo i tuoi dati finanziari"
tags: "sicurezza,pii,xxe,sbom,catena di fornitura,deterministico"
theme_color: "rgb(73, 214, 251)"
title: "Sicurezza del parser dell'estratto conto: protezione dei dati e catena di fornitura"
url: "https://bankstatementparser.com/it/sicurezza/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/it/sicurezza/rss.xml"
category: "Software finanziario, libreria Python, elaborazione dati"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin (version 0.0.20)"
item_description: "Funzionalità di sicurezza dell'analizzatore di estratti conto: protezione XXE, rafforzamento della bomba ZIP, redazione PII, sicurezza della catena di fornitura, output deterministico e build firmate."
item_guid: "https://bankstatementparser.com/it/sicurezza/rss.xml"
item_link: "https://bankstatementparser.com/it/sicurezza/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Sicurezza del parser dell'estratto conto: protezione dei dati e catena di fornitura"
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
apple-mobile-web-app-title: "Sicurezza del parser dell'estratto conto: protezione dei dati e catena di fornitura"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Funzionalità di sicurezza dell'analizzatore di estratti conto: protezione XXE, rafforzamento della bomba ZIP, redazione PII, sicurezza della catena di fornitura, output deterministico e build firmate."
twitter_image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logo di Parser estratto conto, potenzia la tua analisi finanziaria con l'estrazione dei dati senza interruzioni"
twitter_site: "@wwdseb"
twitter_title: "Sicurezza del parser dell'estratto conto: protezione dei dati e catena di fornitura"
twitter_url: "https://bankstatementparser.com/it/sicurezza/index.html"

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

**TL;DR:** Bank Statement Parser non effettua chiamate di rete, oscura le informazioni personali per impostazione predefinita, rafforza l'analisi XML contro gli attacchi XXE e viene fornito con dipendenze con blocco hash SHA-256 e una SBOM CycloneDX.

## Sicurezza fin dalla progettazione

Bank Statement Parser è progettato per l'elaborazione di dati finanziari sensibili. Ogni decisione progettuale dà priorità alla sicurezza, alla privacy e alla verificabilità.

## Accesso alla rete zero

Tutta l'elaborazione avviene localmente all'interno del runtime. La libreria non effettua chiamate API, non effettua connessioni cloud e non raccoglie dati di telemetria. I parser XML sono configurati esplicitamente con`no_network=True`, `resolve_entities=False`, E`load_dtd=False`per impedire qualsiasi accesso in uscita.

## Redazione PII

Le informazioni di identificazione personale (nomi, IBAN, indirizzi postali) vengono automaticamente oscurate nell'output CLI e nella modalità streaming. Questo è attivo per impostazione predefinita.

- **CLI**: i campi sensibili vengono visualizzati come`***REDACTED***`
- **Streaming**:`parse_streaming(redact_pii=True)`(predefinito)
- **Esportazioni**: CSV/JSON/Excel conservano i dati completi per l'elaborazione a valle
- **Attivazione**: utilizzo`--show-pii`O`redact_pii=False`quando hai bisogno di output non oscurato

## Sicurezza XML (protezione XXE)

Tutti gli usi di analisi XML`lxml`con impostazioni rafforzate:

- `resolve_entities=False`-- impedisce attacchi di espansione di entità XML
-`no_network=True`-- blocca tutti gli accessi alla rete in uscita dal parser
-`load_dtd=False`-- previene gli attacchi basati su DTD
- Rimozione dello spazio dei nomi prima dell'elaborazione: gestisce qualsiasi variante CAMT.053 in modo sicuro

## Sicurezza dell'archivio ZIP

`iter_secure_xml_entries()`convalida ogni membro ZIP prima dell'estrazione:

- **Limite massimo per le dimensioni della voce**: 10 MB per voce (configurabile)
- **Limite massimo di dimensione totale**: 50 MB totali non compressi (configurabile)
- **Limite del rapporto di compressione**: 100:1 predefinito -- rileva le bombe ZIP
- **Rifiuto della voce crittografata**: le voci crittografate vengono ignorate con un avviso
- **Nessuna scrittura su disco**: i byte XML passano direttamente al parser tramite`from_bytes()`

## Prevenzione dell'attraversamento del percorso

La convalida dell'input blocca i percorsi di file pericolosi:

- Byte nulli, modelli di attraversamento delle directory (`../`) e i collegamenti simbolici vengono rifiutati
- Convalida dell'estensione del file rispetto ai formati previsti
- Limiti di dimensione del file (100 MB predefiniti, configurabili)

## Uscita deterministica

Dato lo stesso file di input, il parser produce un output identico in byte ad ogni esecuzione. Nessuna casualità, nessuna inferenza del modello, nessun campionamento euristico. Questo è fondamentale per:

- **Riproducibilità del controllo**: esegui lo stesso file due volte e confronta l'output
- **Conformità normativa**: dimostrare un'elaborazione coerente
- **Verifica CI**: 467 test applicano il determinismo con una copertura delle filiali del 100%.

## Sicurezza della catena di fornitura

- **Dipendenze con blocco hash SHA-256**: ogni pacchetto in`poetry.lock`ha verificato gli hash dei file
- **CycloneDX SBOM**: ogni versione include una distinta materiali del software
- **Provenienza build GitHub**: l'attestazione collega ogni artefatto al relativo commit di origine
- **Commit firmati**: tutti i commit sono firmati SSH e verificati in CI
- **Verifica della dipendenza**:`scripts/verify_locked_hashes.py`convalida tutti gli hash localmente

## Verifica localmente

```bash
python -m pytest                          # 467 tests, 100% branch coverage
python scripts/verify_locked_hashes.py    # SHA-256 hash verification
git log --show-signature -1               # Verify commit signature
```
