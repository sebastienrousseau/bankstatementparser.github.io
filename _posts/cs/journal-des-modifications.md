---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Změnový protokol analyzátoru výpisů z účtu"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023–2026 Analyzátor bankovních výpisů. Všechna práva vyhrazena."
date: "Apr 11, 2026"
description: "Historie vydání a protokol změn pro analyzátor výpisů z účtu. Sledujte nové funkce, vylepšení a opravy chyb ve všech verzích."
download: ""
format-detection: "telephone=no"
hreflang: "cs"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/cs/journal-des-modifications/index.html"
image_alt: "Logo analyzátoru bankovních výpisů, zdokonalte svou finanční analýzu pomocí bezproblémové extrakce dat"
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "výpis změn analyzátoru bankovních výpisů, poznámky k vydání, historie verzí, aktualizace"
language: "cs-CZ"
layout: "about"
locale: "cs_CZ"
logo_alt: "Logo analyzátoru bankovních výpisů, zdokonalte svou finanční analýzu pomocí bezproblémové extrakce dat"
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Seznam změn"
permalink: "https://bankstatementparser.com/cs/journal-des-modifications/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Historie vydání a co je nového"
tags: "changelog, vydání, aktualizace, verze, oznámení, blog"
theme_color: "rgb(73, 214, 251)"
title: "Změnový protokol analyzátoru výpisů z účtu"
url: "https://bankstatementparser.com/cs/journal-des-modifications/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/cs/journal-des-modifications/rss.xml"
category: "Finanční software, Python Library, zpracování dat"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Historie vydání a protokol změn pro analyzátor výpisů z účtu. Sledujte nové funkce, vylepšení a opravy chyb ve všech verzích."
item_guid: "https://bankstatementparser.com/cs/journal-des-modifications/rss.xml"
item_link: "https://bankstatementparser.com/cs/journal-des-modifications/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Změnový protokol analyzátoru výpisů z účtu"
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
apple-mobile-web-app-title: "Změnový protokol analyzátoru výpisů z účtu"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Historie vydání a protokol změn pro analyzátor výpisů z účtu. Sledujte nové funkce, vylepšení a opravy chyb ve všech verzích."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logo analyzátoru bankovních výpisů, zdokonalte svou finanční analýzu pomocí bezproblémové extrakce dat"
twitter_site: "@wwdseb"
twitter_title: "Změnový protokol analyzátoru výpisů z účtu"
twitter_url: "https://bankstatementparser.com/cs/journal-des-modifications/index.html"

# Humans.txt - The Humans.txt front matter (YAML).

author_website: "https://bankstatementparser.com"
author_twitter: "@wwdseb"
author_location: "London, UK"
thanks: "Díky za přečtení!"
site_last_updated: "2026-04-01"
site_standards: "HTML5, CSS3, RSS, Atom, JSON, XML, YAML, Markdown, TOML"
site_components: "Shokunin SSG, Shokunin CLI, Shokunin Templates, Shokunin Themes, Kaishi SSG, Kaishi CLI, Kaishi Templates, Kaishi Themes"
site_software: "Shokunin, Rust"

---

Sledujte vývoj analyzátoru výpisů z účtu. Přihlaste se k odběru přes [RSS](/changelog/rss.xml) nebo sledujte [úložiště GitHub](https://github.com/sebastienrousseau/bankstatementparser) pro oznámení o vydání.

## v0.0.8 — 2026-04-11 (Latest) — "Full Platform"

- Multi-currency balance verification — `verify_balance_multi_currency()` groups by currency, runs Golden Rule per group.
- hledger + beancount export — `to_hledger()` and `to_beancount()` in `bankstatementparser.export`.
- Bulk directory scanner — `scan_and_ingest()` scans folder trees, deduplicates across batch.
- Account mapping rules — `AccountMapper` with ordered regex rules from JSON config.
- REST API — FastAPI wrapper with `/ingest` and `/health` endpoints (`[api]` extra).

## v0.0.7 — 2026-04-08 — "Universal Vision"

- Direct Ollama bridge (`ollama_direct_completion`) — bypasses LiteLLM long-prompt hang.
- Strip mode (`VisionExtractor.strip_rows=True`) — splits dense pages into overlapping bands for small local models.
- Recommended vision model changed from `llava` to `minicpm-v`.

## v0.0.6 — 2026-04-08 — "Intelligence Layer"

- Dropped Python 3.9 support (now 3.10-3.14).
- Enrichment module (`Categorizer`, `EnrichedTransaction`, `DEFAULT_CATEGORY_SCHEMA`).
- Interactive review mode with `--type review` CLI command.
- Per-row bounding box extraction (`Transaction.source_bbox`).

## v0.0.5 — 2026-04-08 — "Universal Extraction"

- Hybrid PDF pipeline (`smart_ingest()`) with deterministic/text-LLM/vision-LLM routing.
- `LLMExtractor` for digital PDFs via LiteLLM.
- `VisionExtractor` for scanned PDFs via multimodal vision models.
- Golden Rule balance verification (`opening + credits - debits == closing`).
- Idempotent deduplication via `transaction_hash` (MD5 fingerprint).

## v0.0.4 — 2026-03-15

- Přidána paralelní analýza souborů s`parse_files_parallel()`pomocí ProcessPoolExecutor.
- Přidáno skutečné streamování pro velké soubory PAIN.001 (50 MB+) s omezenou pamětí.
- Optimalizace výkonu: propustnost CAMT nyní přesahuje 27 000 tx/s, PAIN.001 přesahuje 52 000 tx/s.
- Přidáno`Deduplicator`třída pro detekci přesných duplikátů a podezřelých shod se skóre spolehlivosti.
- Přidáno`from_string()`a`from_bytes()`metody pro analýzu v paměti bez diskových I/O.
- Přidáno`iter_secure_xml_entries()`pro bezpečné zpracování ZIP archivu.
- Rozšířená CI s prosazením prahu výkonu.

## v0.0.3 — 20. 11. 2025

- Přidána podpora analyzátoru CSV, OFX, QFX a MT940.
- Přidána automatická detekce formátu s`detect_statement_format()`a`create_parser()`.
- Přidána redakce PII (ve výchozím nastavení zapnutá v režimu CLI a streamování).
- Přidáni pomocníci pro export pro CSV, JSON a Excel.
- Přidána volitelná podpora Polar DataFrame.
- Rozšířená sada testů na 718 testů se 100% pokrytím větví.

## v0.0.2 — 2025-06-10

- Přidán analyzátor PAIN.001 (`Pain001Parser`) pro soubory zahájení převodu kreditu ISO 20022.
- Přidáno rozhraní CLI (`python -m bankstatementparser.cli`).
- Přidán režim streamování s`parse_streaming()`.
- Přidáno ověření vstupu a omezení velikosti souboru.

## v0.0.1 — 2025-01-15

- První vydání.
- analyzátor CAMT.053 (`CamtParser`) pro výpisy mezi bankami a zákazníky podle ISO 20022.
- výstup datového rámce pandas.
- Základní posílení zabezpečení XML (ochrana XXE, no_network).

Zobrazit celou historii odevzdání na [GitHub](https://github.com/sebastienrousseau/bankstatementparser/commits/main).

<script type="application/ld+json">
{
  "@kontext": "https://schema.org",
  "@type": "Softwarová aplikace",
  "name": "Parser bankovních výpisů",
  "applicationCategory": "Aplikace pro vývojáře",
  "operační systém": "Více platforem",
  "softwareVersion": "0.0.8",
  "datePublished": "2026-04-11",
  "releaseNotes": "Přidána paralelní analýza souborů, skutečné streamování pro PAIN.001, optimalizace výkonu (27K+ tx/s CAMT, 52K+ tx/s PAIN.001), třída deduplikátoru, analýza v paměti, bezpečné zpracování ZIP.",
  "downloadUrl": "https://pypi.org/project/bankstatementparser/",
  "licence": "https://opensource.org/licenses/Apache-2.0",
  "autor": {
    "@type": "Osoba",
    "name": "Sebastien Rousseau"
  }
}
</script>
