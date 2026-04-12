---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "O analyzátoru výpisů z účtu: Funkce, formáty a výkon"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023–2026 Analyzátor bankovních výpisů. Všechna práva vyhrazena."
date: "Apr 11, 2026"
description: "Bank Statement Parser je open-source Python knihovna pro analýzu CAMT.053, PAIN.001, CSV, OFX, QFX a MT940 do datových rámců pandas. 100% místní, redakce PII, 27K+ tx/s."
download: ""
format-detection: "telephone=no"
hreflang: "cs"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/cs/a-propos/index.html"
image_alt: "Logo analyzátoru bankovních výpisů, zdokonalte svou finanční analýzu pomocí bezproblémové extrakce dat"
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "analyzátor bankovních výpisů python, analyzátor CAMT.053, analyzátor PAIN.001, knihovna python ISO 20022, analyzátor MT940, analyzátor OFX QFX, analyzátor banky s otevřeným zdrojovým kódem, místní zpracování finančních dat, redakční bankovnictví PII, migrace MT940 na CAMT"
language: "cs-CZ"
layout: "about"
locale: "cs_CZ"
logo_alt: "Logo analyzátoru bankovních výpisů, zdokonalte svou finanční analýzu pomocí bezproblémové extrakce dat"
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "O analyzátoru bankovních výpisů"
permalink: "https://bankstatementparser.com/cs/a-propos/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Jedna knihovna. Šest formátů. Nulová síťová volání."
tags: "banka,výpis,analyzátor,finance,python,camt,pain001,csv,ofx,qfx,mt940"
theme_color: "rgb(73, 214, 251)"
title: "O analyzátoru výpisů z účtu: Funkce, formáty a výkon"
url: "https://bankstatementparser.com/cs/a-propos/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/cs/a-propos/rss.xml"
category: "Finanční software, Python Library, zpracování dat"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Bank Statement Parser je open-source Python knihovna pro analýzu CAMT.053, PAIN.001, CSV, OFX, QFX a MT940 do datových rámců pandas. 100% místní, redakce PII, 27K+ tx/s."
item_guid: "https://bankstatementparser.com/cs/a-propos/rss.xml"
item_link: "https://bankstatementparser.com/cs/a-propos/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "O analyzátoru výpisů z účtu: Funkce, formáty a výkon"
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
apple-mobile-web-app-title: "O analyzátoru výpisů z účtu: Funkce, formáty a výkon"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Open-source knihovna Pythonu: analyzujte CAMT.053, PAIN.001, CSV, OFX, QFX, MT940 do DataFrames. 100% místní, redakce PII, 27K+ tx/s."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logo analyzátoru bankovních výpisů, zdokonalte svou finanční analýzu pomocí bezproblémové extrakce dat"
twitter_site: "@wwdseb"
twitter_title: "O analyzátoru bankovních výpisů: 6 formátů, 27 000 + tx/s, 100 % místní"
twitter_url: "https://bankstatementparser.com/cs/a-propos/index.html"

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

**TL;DR:** Bank Statement Parser je open-source Python knihovna, která analyzuje sedm formátů bankovních výpisů (CAMT.053, PAIN.001, CSV, OFX, QFX, MT940 a PDF) do pandas DataFrames. Hybridní PDF pipeline s ověřením zůstatku, REST API, obohacení, export do účetnictví, propustnost 27K+ tx/s.

Bank Statement Parser je open-source Python knihovna, která analyzuje bankovní výpisy ze sedmi formátů do strukturovaných pandas DataFrames. Deterministické jádro zpracovává strukturované formáty lokálně bez síťových volání. Volitelný hybridní PDF pipeline směruje přes lokální LLM (prostřednictvím Ollama) pro digitální a naskenované výpisy.

## Pro koho je to určeno?

- **Treasury týmy** migrující z MT940 na CAMT.053, které potřebují parser zvládající oba formáty během přechodu, plus PDF výpisy od bank bez strukturovaných exportů.
- **Fintech vývojáři** budující pipeline pro odsouhlasení, reporting nebo účetnictví, kteří chtějí jedinou závislost s vestavěným ověřením zůstatku, kategorizací a exportem do účetnictví.
- **Compliance týmy**, které potřebují výchozí redakci PII, deterministický výstup a ověření Golden Rule, jež odhalí nesrovnalosti dříve, než se dostanou do účetní knihy.
- **Uživatelé plaintext-accounting**, kteří chtějí automatizované zpracování PDF bankovních výpisů přímo do hledger nebo beancount deníků.
- **Kdokoli**, kdo odmítá posílat citlivá finanční data třetí straně, když to zvládne lokální open-source nástroj.

## Podporované formáty

| Formát | Standard | Typy souborů | Parser/Metoda |
|---|---|---|---|
| CAMT.053 | ISO 20022 Bank-to-Customer Statement | `.xml` | `CamtParser` |
| PAIN.001 | ISO 20022 Credit Transfer Initiation | `.xml` | `Pain001Parser` |
| CSV | Generické bankovní exporty | `.csv` | `CsvStatementParser` |
| OFX | Open Financial Exchange | `.ofx` | `OfxParser` |
| QFX | Quicken Financial Exchange | `.qfx` | `QfxParser` |
| MT940 | Standard SWIFT | `.mt940`, `.sta` | `Mt940Parser` |
| PDF | Digitální a naskenované výpisy | `.pdf` | `smart_ingest()` |

Všechny formáty produkují normalizované pandas DataFrames s konzistentními názvy sloupců, což činí následné zpracování nezávislým na formátu.

## Klíčové funkce

- **Hybridní PDF pipeline**: `smart_ingest()` směruje PDF třemi cestami — deterministická extrakce tabulek, text-LLM nebo vision-LLM — s automatickým ověřením zůstatku Golden Rule.
- **Automatická detekce formátu**: `detect_statement_format()` identifikuje formát; `create_parser()` vytvoří správný parser.
- **Ověření zůstatku**: Kontrola Golden Rule (`opening + credits − debits == closing`) se stavem VERIFIED/DISCREPANCY/FAILED.
- **Multi-měnové ověření**: `verify_balance_multi_currency()` seskupuje transakce podle měny pro nezávislé ověření.
- **REST API**: FastAPI mikroservis s endpointy `/ingest` a `/health` pro produkční nasazení.
- **Obohacení**: LLM kategorizace transakcí s připojitelnými schématy (výchozí 13 kategorií Plaid).
- **Interaktivní kontrola**: Procházení nesrovnalostí s akcemi accept/edit/skip/delete přes `--type review`.
- **Export do účetnictví**: `to_hledger()` a `to_beancount()` pro plaintext-accounting workflows.
- **Hromadné skenování**: `scan_and_ingest()` zpracovává adresářové stromy s automatickou deduplikací napříč soubory.
- **Mapování účtů**: Regex mapovací pravidla účtů z JSON konfigurace pro export do účetnictví.
- **Streaming parsing**: Zpracování velkých souborů (50 MB+, 50K+ transakcí) s omezenou pamětí pomocí `parse_streaming()`.
- **Paralelní zpracování**: Parsování více souborů současně pomocí `parse_files_parallel()` s ProcessPoolExecutor.
- **Deduplikace**: Idempotentní `transaction_hash` (MD5 fingerprint) pro bezpečné inkrementální zpracování.
- **Parsování v paměti**: `from_string()` a `from_bytes()` pro SFTP a API workflows bez diskových I/O.
- **Bezpečné zpracování ZIP**: `iter_secure_xml_entries()` s limity kompresního poměru, omezením velikosti záznamů a odmítnutím šifrovaných záznamů.
- **Export**: CSV, JSON, Excel (`.xlsx`), Polars DataFrames, hledger a beancount deníky.

## Zabezpečení a soukromí

- **Redakce PII**: Jména, IBANy a adresy jsou ve výstupu CLI ve výchozím nastavení maskovány. Zapněte zobrazení pomocí `--show-pii`.
- **Ochrana proti XXE**: XML parsování používá `resolve_entities=False`, `no_network=True`, `load_dtd=False`.
- **Ochrana proti ZIP bombám**: Limity kompresního poměru (výchozí 100:1), omezení velikosti záznamů (10 MB), odmítnutí šifrovaných záznamů.
- **Prevence path traversal**: Blocklist nebezpečných vzorů a rozlišení symbolických odkazů.
- **Zabezpečení dodavatelského řetězce**: SHA-256 hash-locked závislosti, CycloneDX SBOM, attestace o původu sestavení.
- **Pouze lokální LLM**: Hybridní PDF pipeline používá Ollama pro lokální inferenci — žádná data neodcházejí do cloudových API.

## Výkon

| Metrika | Hodnota |
|---|---|
| Propustnost CAMT.053 | 27 000+ tx/s |
| Propustnost PAIN.001 | 52 000+ tx/s |
| Latence na transakci (CAMT) | 37 mikrosekund |
| Latence na transakci (PAIN.001) | 19 mikrosekund |
| Čas do prvního výsledku | < 2 ms |
| Škálování paměti (1K–50K tx) | Konstantní (streaming) |
| Pokrytí testy | 100% pokrytí větví |
| Testy | 718 v 29 testovacích souborech |

## Začněte tvořit

[Začněte s instalací a příklady ❯][01]

[01]: /getting-started/index.html "Začínáme"
