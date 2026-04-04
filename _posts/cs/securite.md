---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Zabezpečení analyzátoru bankovních výpisů"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023–2026 Analyzátor bankovních výpisů. Všechna práva vyhrazena."
date: "Apr 01, 2026"
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

**TL;DR:** Analyzátor výpisů z účtu neprovádí žádná síťová volání, ve výchozím nastavení rediguje PII, zpevňuje analýzu XML proti útokům XXE a dodává se se závislostmi se SHA-256 hash-locked a CycloneDX SBOM.

## Zabezpečení podle návrhu

Bank Statement Parser je vytvořen pro zpracování citlivých finančních dat. Každé rozhodnutí o návrhu upřednostňuje zabezpečení, soukromí a auditovatelnost.

## Nulový přístup k síti

Veškeré zpracování probíhá lokálně v rámci vašeho běhového prostředí. Knihovna neprovádí žádná volání API, žádná cloudová připojení a shromažďuje nulovou telemetrii. Analyzátory XML jsou explicitně nakonfigurovány pomocí`no_network=True`, `resolve_entities=False`a`load_dtd=False`aby se zabránilo jakémukoli odchozímu přístupu.

## Redakce PII

Osobně identifikovatelné informace (jména, IBAN, poštovní adresy) jsou automaticky redigovány ve výstupu CLI a režimu streamování. Toto je ve výchozím nastavení zapnuto.

- **CLI**: Citlivá pole se zobrazují jako`***REDACTED***`
- **Streamování**:`parse_streaming(redact_pii=True)`(výchozí)
- **Exporty**: CSV/JSON/Excel uchovávají úplná data pro následné zpracování
- **Přihlášení**: Použijte`--show-pii`nebo`redact_pii=False`když potřebujete nezreagovaný výstup

## Zabezpečení XML (ochrana XXE)

Všechna použití analýzy XML`lxml`s kaleným nastavením:

- `resolve_entities=False`- zabraňuje útokům na rozšíření entity XML
-`no_network=True`-- blokuje veškerý odchozí síťový přístup z analyzátoru
-`load_dtd=False`-- zabraňuje útokům založeným na DTD
- Odstranění jmenného prostoru před zpracováním - bezpečně zpracuje jakoukoli variantu CAMT.053

## Zabezpečení archivu ZIP

`iter_secure_xml_entries()`ověřuje každého člena ZIP před extrakcí:

- **Omezení velikosti položky**: 10 MB na položku (lze konfigurovat)
- **Celkový limit velikosti**: celkem 50 MB nekomprimováno (lze konfigurovat)
- **Limit kompresního poměru**: výchozí 100:1 – detekuje bomby ZIP
- **Odmítnutí šifrovaného záznamu**: Zašifrované záznamy jsou přeskočeny s varováním
- **Žádné zápisy na disk**: Byty XML přecházejí přímo do analyzátoru přes`from_bytes()`

## Prevence procházení cesty

Ověření vstupu blokuje nebezpečné cesty k souborům:

- Nulové bajty, vzory procházení adresářů (`../`) a symbolické odkazy jsou odmítnuty
- Ověření přípony souboru proti očekávaným formátům
- Limity velikosti souboru (100 MB výchozí, konfigurovatelné)

## Deterministický výstup

Vzhledem ke stejnému vstupnímu souboru vytváří analyzátor při každém spuštění výstup identický s byty. Žádná náhodnost, žádná modelová inference, žádné heuristické vzorkování. To je kritické pro:

- **Reprodukovatelnost auditu**: Spusťte dvakrát stejný soubor a porovnejte výstup
- **Shoda s předpisy**: Prokázat konzistentní zpracování
- **Ověření CI**: 467 testů prosazuje determinismus se 100% pokrytím větví

## Zabezpečení dodavatelského řetězce

- **SHA-256 hash-locked dependency**: Každý balíček v`poetry.lock`ověřil hash souboru
- **CycloneDX SBOM**: Každá verze obsahuje Software Bill of Materials
- **Původ sestavení GitHubu**: Atestace spojuje každý artefakt s jeho zdrojovým odevzdáním
- **Podepsané commity**: Všechny commity jsou podepsané SSH a ověřené v CI
- **Ověření závislosti**:`scripts/verify_locked_hashes.py`ověřuje všechny hash lokálně

## Ověřit lokálně

```bash
python -m pytest                          # 467 tests, 100% branch coverage
python scripts/verify_locked_hashes.py    # SHA-256 hash verification
git log --show-signature -1               # Verify commit signature
```
