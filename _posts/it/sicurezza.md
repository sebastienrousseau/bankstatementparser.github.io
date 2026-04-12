---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Sicurezza del parser dell'estratto conto bancario"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Analizzatore di estratti conto bancari. Tutti i diritti riservati."
date: "Apr 11, 2026"
description: "Funzionalità di sicurezza dell'analizzatore di estratti conto: protezione XXE, rafforzamento della bomba ZIP, redazione PII, sicurezza della catena di fornitura, output deterministico e build firmate."
download: ""
format-detection: "telephone=no"
hreflang: "it"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/it/sicurezza/index.html"
image_alt: "Logo di Parser estratto conto, potenzia la tua analisi finanziaria con l'estrazione dei dati senza interruzioni"
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "sicurezza dell'estratto conto, Python per la redazione delle PII, protezione XXE, protezione ZIP bomb, sicurezza della catena di fornitura SBOM, analisi deterministica, sicurezza dei dati finanziari"
language: "it-IT"
layout: "about"
locale: "it_IT"
logo_alt: "Logo di Parser estratto conto, potenzia la tua analisi finanziaria con l'estrazione dei dati senza interruzioni"
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
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
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Funzionalità di sicurezza dell'analizzatore di estratti conto: protezione XXE, rafforzamento della bomba ZIP, redazione PII, sicurezza della catena di fornitura, output deterministico e build firmate."
twitter_image: "/images/logos/bankstatementparser.webp"
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

**In breve:** Bank Statement Parser elabora tutti i dati in locale, oscura i dati personali di default, protegge il parsing XML contro attacchi XXE, esegue i LLM localmente via Ollama e include dipendenze con hash SHA-256 bloccati e una SBOM CycloneDX.

## Sicurezza fin dalla progettazione

Bank Statement Parser è progettato per l'elaborazione di dati finanziari sensibili. Ogni decisione progettuale dà priorità a sicurezza, privacy e verificabilità.

## Zero dipendenze cloud

Tutta l'elaborazione avviene in locale nel proprio runtime. I parser deterministici non effettuano chiamate di rete. La pipeline PDF ibrida usa Ollama per l'inferenza LLM locale — nessun dato viene inviato ad API cloud. I parser XML sono configurati esplicitamente con `no_network=True`, `resolve_entities=False` e `load_dtd=False` per impedire qualsiasi accesso in uscita.

## Oscuramento PII

Le informazioni di identificazione personale (nomi, IBAN, indirizzi postali) vengono automaticamente oscurate nell'output CLI e in modalità streaming. Questa funzione è attiva di default.

- **CLI**: i campi sensibili appaiono come `***REDACTED***`
- **Streaming**: `parse_streaming(redact_pii=True)` (default)
- **Esportazioni**: CSV/JSON/Excel conservano i dati completi per l'elaborazione a valle
- **Attivazione**: usare `--show-pii` o `redact_pii=False` quando si necessita di output non oscurato

## Sicurezza XML (protezione XXE)

Tutto il parsing XML usa `lxml` con impostazioni protette:

- `resolve_entities=False` -- impedisce attacchi di espansione entità XML
- `no_network=True` -- blocca tutti gli accessi di rete in uscita dal parser
- `load_dtd=False` -- previene attacchi basati su DTD
- Rimozione dei namespace prima dell'elaborazione — gestisce qualsiasi variante CAMT.053 in sicurezza

## Sicurezza archivi ZIP

`iter_secure_xml_entries()` valida ogni membro ZIP prima dell'estrazione:

- **Dimensione massima per voce**: 10 MB per voce (configurabile)
- **Dimensione totale massima**: 50 MB totali non compressi (configurabile)
- **Limite del rapporto di compressione**: 100:1 di default — rileva le ZIP bomb
- **Rifiuto voci crittografate**: le voci crittografate vengono ignorate con un avviso
- **Nessuna scrittura su disco**: i byte XML passano direttamente al parser tramite `from_bytes()`

## Prevenzione path traversal

La validazione dell'input blocca i percorsi file pericolosi:

- Byte nulli, pattern di directory traversal (`../`) e link simbolici vengono rifiutati
- Validazione dell'estensione file rispetto ai formati previsti
- Limiti di dimensione file (100 MB di default, configurabile)

## Verifica del saldo (Golden Rule)

Ogni estrazione PDF viene verificata con l'equazione: `opening balance + credits − debits == closing balance`. I risultati sono classificati come VERIFIED, DISCREPANCY o FAILED. Le discrepanze possono essere riviste interattivamente con `--type review`.

## Output deterministico

Per i formati strutturati (CAMT, PAIN.001, CSV, OFX, QFX, MT940), dato lo stesso file di input, il parser produce un output identico byte per byte ad ogni esecuzione. Nessuna casualità, nessuna inferenza di modello, nessun campionamento euristico. Questo è fondamentale per:

- **Riproducibilità degli audit**: eseguire lo stesso file due volte e confrontare l'output
- **Conformità normativa**: dimostrare un'elaborazione coerente
- **Verifica CI**: 718 test garantiscono il determinismo con copertura branch al 100%

## Sicurezza della supply chain

- **Dipendenze con hash SHA-256 bloccati**: ogni pacchetto in `poetry.lock` ha hash dei file verificati
- **CycloneDX SBOM**: ogni release include una Software Bill of Materials
- **Provenienza build GitHub**: l'attestazione collega ogni artefatto al commit sorgente
- **Commit firmati**: tutti i commit sono firmati SSH e verificati in CI
- **Verifica delle dipendenze**: `scripts/verify_locked_hashes.py` valida tutti gli hash localmente

## Verifica in locale

```bash
python -m pytest                          # 718 tests, 100% branch coverage
python scripts/verify_locked_hashes.py    # SHA-256 hash verification
git log --show-signature -1               # Verify commit signature
```
