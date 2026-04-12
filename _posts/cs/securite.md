---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Zabezpečení analyzátoru bankovních výpisů"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023–2026 Analyzátor bankovních výpisů. Všechna práva vyhrazena."
date: "Apr 11, 2026"
description: "Bezpečnostní funkce analyzátoru výpisů z účtu: ochrana XXE, zpevnění bomby ZIP, redakce PII, zabezpečení dodavatelského řetězce, deterministický výstup a podepsané sestavení."
download: ""
format-detection: "telephone=no"
hreflang: "cs"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/cs/securite/index.html"
image_alt: "Logo analyzátoru bankovních výpisů, zdokonalte svou finanční analýzu pomocí bezproblémové extrakce dat"
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "zabezpečení bankovních výpisů, PII redakční python, ochrana XXE, ochrana proti bombám ZIP, zabezpečení dodavatelského řetězce SBOM, deterministická analýza, zabezpečení finančních údajů"
language: "cs-CZ"
layout: "about"
locale: "cs_CZ"
logo_alt: "Logo analyzátoru bankovních výpisů, zdokonalte svou finanční analýzu pomocí bezproblémové extrakce dat"
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Zabezpečení"
permalink: "https://bankstatementparser.com/cs/securite/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Jak chráníme vaše finanční údaje"
tags: "zabezpečení,pii,xxe,sbom,dodavatelský řetězec,deterministický"
theme_color: "rgb(73, 214, 251)"
title: "Zabezpečení analyzátoru bankovních výpisů: Ochrana dat a dodavatelský řetězec"
url: "https://bankstatementparser.com/cs/securite/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/cs/securite/rss.xml"
category: "Finanční software, Python Library, zpracování dat"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Bezpečnostní funkce analyzátoru výpisů z účtu: ochrana XXE, zpevnění bomby ZIP, redakce PII, zabezpečení dodavatelského řetězce, deterministický výstup a podepsané sestavení."
item_guid: "https://bankstatementparser.com/cs/securite/rss.xml"
item_link: "https://bankstatementparser.com/cs/securite/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Zabezpečení analyzátoru bankovních výpisů: Ochrana dat a dodavatelský řetězec"
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
apple-mobile-web-app-title: "Zabezpečení analyzátoru bankovních výpisů: Ochrana dat a dodavatelský řetězec"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Bezpečnostní funkce analyzátoru výpisů z účtu: ochrana XXE, zpevnění bomby ZIP, redakce PII, zabezpečení dodavatelského řetězce, deterministický výstup a podepsané sestavení."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logo analyzátoru bankovních výpisů, zdokonalte svou finanční analýzu pomocí bezproblémové extrakce dat"
twitter_site: "@wwdseb"
twitter_title: "Zabezpečení analyzátoru bankovních výpisů: Ochrana dat a dodavatelský řetězec"
twitter_url: "https://bankstatementparser.com/cs/securite/index.html"

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

**TL;DR:** Bank Statement Parser zpracovává veškerá data lokálně, ve výchozím nastavení rediguje PII, zabezpečuje XML parsování proti XXE útokům, provozuje LLM lokálně přes Ollama a dodává se s SHA-256 hash-locked závislostmi a CycloneDX SBOM.

## Zabezpečení od návrhu

Bank Statement Parser je vytvořen pro zpracování citlivých finančních dat. Každé rozhodnutí upřednostňuje zabezpečení, soukromí a auditovatelnost.

## Nulová závislost na cloudu

Veškeré zpracování probíhá lokálně ve vašem runtime. Deterministické parsery neprovádějí žádná síťová volání. Hybridní PDF pipeline používá Ollama pro lokální LLM inferenci — žádná data nejsou odesílána do cloudových API. XML parsery jsou explicitně nakonfigurovány s `no_network=True`, `resolve_entities=False` a `load_dtd=False` pro prevenci jakéhokoli odchozího přístupu.

## Redakce PII

Osobně identifikovatelné informace (jména, IBANy, poštovní adresy) jsou automaticky redigovány ve výstupu CLI a režimu streamování. Toto je ve výchozím nastavení zapnuto.

- **CLI**: Citlivá pole se zobrazují jako `***REDACTED***`
- **Streaming**: `parse_streaming(redact_pii=True)` (výchozí)
- **Exporty**: CSV/JSON/Excel uchovávají úplná data pro následné zpracování
- **Zapnutí**: Použijte `--show-pii` nebo `redact_pii=False`, když potřebujete neredigovaný výstup

## Zabezpečení XML (ochrana proti XXE)

Veškeré XML parsování používá `lxml` se zabezpečeným nastavením:

- `resolve_entities=False` — zabraňuje útokům rozšířením XML entit
- `no_network=True` — blokuje veškerý odchozí síťový přístup z parseru
- `load_dtd=False` — zabraňuje útokům založeným na DTD
- Odstranění jmenných prostorů před zpracováním — bezpečně zpracuje jakoukoli variantu CAMT.053

## Zabezpečení ZIP archivů

`iter_secure_xml_entries()` validuje každý člen ZIP před extrakcí:

- **Limit velikosti záznamu**: 10 MB na záznam (konfigurovatelné)
- **Celkový limit velikosti**: 50 MB celkem nekomprimovaně (konfigurovatelné)
- **Limit kompresního poměru**: výchozí 100:1 — detekuje ZIP bomby
- **Odmítnutí šifrovaných záznamů**: Šifrované záznamy jsou přeskočeny s varováním
- **Žádné zápisy na disk**: XML bajty přecházejí přímo do parseru přes `from_bytes()`

## Prevence path traversal

Validace vstupu blokuje nebezpečné cesty k souborům:

- Nulové bajty, vzory procházení adresářů (`../`) a symbolické odkazy jsou odmítnuty
- Validace přípony souboru proti očekávaným formátům
- Limity velikosti souboru (100 MB výchozí, konfigurovatelné)

## Ověření zůstatku (Golden Rule)

Každá PDF extrakce je ověřena rovnicí: `opening balance + credits − debits == closing balance`. Výsledky jsou označeny jako VERIFIED, DISCREPANCY nebo FAILED. Nesrovnalosti lze zkontrolovat interaktivně pomocí `--type review`.

## Deterministický výstup

Pro strukturované formáty (CAMT, PAIN.001, CSV, OFX, QFX, MT940) při stejném vstupním souboru parser produkuje bajtově identický výstup při každém spuštění. Žádná náhodnost, žádná modelová inference, žádné heuristické vzorkování. To je klíčové pro:

- **Reprodukovatelnost auditu**: Spusťte stejný soubor dvakrát a porovnejte výstup
- **Regulační compliance**: Prokázání konzistentního zpracování
- **Ověření v CI**: 718 testů vynucuje determinismus se 100% pokrytím větví

## Zabezpečení dodavatelského řetězce

- **SHA-256 hash-locked závislosti**: Každý balíček v `poetry.lock` má ověřené hash souborů
- **CycloneDX SBOM**: Každé vydání obsahuje Software Bill of Materials
- **Původ sestavení na GitHubu**: Attestace spojuje každý artefakt s jeho zdrojovým commitem
- **Podepsané commity**: Všechny commity jsou SSH-podepsané a ověřené v CI
- **Ověření závislostí**: `scripts/verify_locked_hashes.py` validuje všechny hashe lokálně

## Ověření lokálně

```bash
python -m pytest                          # 718 tests, 100% branch coverage
python scripts/verify_locked_hashes.py    # SHA-256 hash verification
git log --show-signature -1               # Verify commit signature
```
