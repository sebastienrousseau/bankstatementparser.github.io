---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Průvodce migrací ISO 20022"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023–2026 Analyzátor bankovních výpisů. Všechna práva vyhrazena."
date: "Apr 11, 2026"
description: "Praktický průvodce časovou osou migrace SWIFT ISO 20022 (2026–2028), přechodem z MT940 na CAMT.053 a tím, jak Parser bankovních výpisů pomáhá při migraci treasury týmům."
download: ""
format-detection: "telephone=no"
hreflang: "cs"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/cs/migration/index.html"
image_alt: "Logo analyzátoru bankovních výpisů, zdokonalte svou finanční analýzu pomocí bezproblémové extrakce dat"
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "Migrace ISO 20022, MT940 na CAMT.053, termín SWIFT 2027, vyřazení MT940 2028, python migrace bankovních výpisů, analyzátor CAMT.053, časová osa ISO 20022"
language: "cs-CZ"
layout: "about"
locale: "cs_CZ"
logo_alt: "Logo analyzátoru bankovních výpisů, zdokonalte svou finanční analýzu pomocí bezproblémové extrakce dat"
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Průvodce migrací ISO 20022"
permalink: "https://bankstatementparser.com/cs/migration/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Přejděte na přechod SWIFT MT na ISO 20022"
tags: "iso20022,migrace,mt940,camt053,swift,časová osa"
theme_color: "rgb(73, 214, 251)"
title: "Průvodce migrací ISO 20022: Přechod z MT940 na CAMT.053"
url: "https://bankstatementparser.com/cs/migration/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/cs/migration/rss.xml"
category: "Finanční software, Python Library, zpracování dat"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Praktický průvodce časovou osou migrace SWIFT ISO 20022 (2026–2028), přechodem z MT940 na CAMT.053 a tím, jak Parser bankovních výpisů pomáhá při migraci treasury týmům."
item_guid: "https://bankstatementparser.com/cs/migration/rss.xml"
item_link: "https://bankstatementparser.com/cs/migration/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Průvodce migrací ISO 20022: Přechod z MT940 na CAMT.053"
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
apple-mobile-web-app-title: "Průvodce migrací ISO 20022: Přechod z MT940 na CAMT.053"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Praktický průvodce časovou osou migrace SWIFT ISO 20022 (2026–2028), přechodem z MT940 na CAMT.053 a tím, jak Parser bankovních výpisů pomáhá při migraci treasury týmům."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logo analyzátoru bankovních výpisů, zdokonalte svou finanční analýzu pomocí bezproblémové extrakce dat"
twitter_site: "@wwdseb"
twitter_title: "Průvodce migrací ISO 20022: Přechod z MT940 na CAMT.053"
twitter_url: "https://bankstatementparser.com/cs/migration/index.html"

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

**TL;DR:** SWIFT vyřadí MT940 do listopadu 2028. Bank Statement Parser zpracovává jak MT940, tak CAMT.053 pomocí jediného API, takže váš pipeline funguje během přechodu i po něm.

## Proč na této migraci záleží

SWIFT přestává používat starší formáty zpráv MT ve prospěch bohatšího standardu ISO 20022. Pro treasury a finanční týmy to znamená, že vaše pipeline zpracování bankovních výpisů se musí vyvinout z MT940 na CAMT.053 před pevnými termíny.

## Časová osa migrace SWIFT

| Datum | Milník | Dopad |
|---|---|---|
| **Listopad 2025** | Koexistence MT-to-MX skončila pro přeshraniční platby | Zprávy PACS jsou nyní pouze ISO 20022 |
| **Listopad 2026** | Strukturované/hybridní adresy povinné; MT101 multi-instrukce odmítnuta; Case Management fáze 1 | Formáty adres musí vyhovovat; některé MT zprávy budou odmítnuty |
| **Konec 2026** | Začíná opt-in pro příjem CAMT.052/.053/.054 | Finanční instituce mohou začít přijímat nativní ISO výpisy |
| **Listopad 2027** | Všechny FI musí přijímat CAMT.053 nativně | SWIFT přestane převádět MT formát na ISO; vaše systémy musí parsovat CAMT přímo |
| **Listopad 2028** | MT940/MT942/MT950/MT900/MT910 plně vyřazeny | Starší formáty výpisů již nebudou dostupné; CAMT.052/.053/.054 jsou jedinou možností |

## Co se změní ve vašem kódu

### Před: Pouze MT940

```python
from bankstatementparser import Mt940Parser

parser = Mt940Parser("statement.mt940")
df = parser.parse()
```

### Po: Oba formáty s automatickou detekcí

```python
from bankstatementparser import create_parser, detect_statement_format

fmt = detect_statement_format("statement.xml")  # or .mt940
parser = create_parser("statement.xml", fmt)
df = parser.parse()  # Same DataFrame schema regardless of format
```

Funkce `detect_statement_format()` identifikuje, zda je soubor MT940, CAMT.053, PAIN.001 nebo jiný podporovaný formát. Funkce `create_parser()` vrátí správný parser. Váš následný kód funguje identicky bez ohledu na zdrojový formát.

## CAMT.053 vs MT940: Klíčové rozdíly

| Vlastnost | MT940 | CAMT.053 |
|---|---|---|
| Bohatost dat | Omezená pole | 3–5x více dat na transakci |
| Znaková sada | Omezená (znaková sada SWIFT) | Plné Unicode |
| Struktura | Plochý text se značkami | XML s jmennými prostory |
| Reportování zůstatku | Pouze počáteční/konečný | Více typů zůstatků |
| Reference | Jedno referenční pole | Více typů referencí |
| Práce s měnami | Základní | Plná multi-měna se směnnými kurzy |

## Jak Bank Statement Parser pomáhá

- **Jednotné API**: Parsujte MT940, CAMT.053 a PDF výpisy stejným workflow s konzistentním DataFrame výstupem.
- **Automatická detekce**: Není třeba znát formát předem. `detect_statement_format()` jej identifikuje automaticky.
- **Hybridní PDF pipeline**: Banky poskytující během přechodu pouze PDF výpisy jsou obslouženy pomocí `smart_ingest()` s automatickým ověřením zůstatku.
- **Nezávislost na jmenných prostorech**: Zvládá jakoukoli variantu CAMT.053 (001.02, 001.04 nebo bankovně specifické wrappery) bez konfigurace.
- **Multi-měnové ověření**: `verify_balance_multi_currency()` provádí Golden Rule pro každou měnovou skupinu — nezbytné pro multi-měnové CAMT výpisy.
- **Streaming**: Zpracování velkých CAMT souborů (50 MB+, 50K+ transakcí) s omezenou pamětí.
- **Export do účetnictví**: Export přímo do formátu hledger nebo beancount deníku pro treasury účetnictví.
- **Testování migrace**: Spusťte oba parsery vedle sebe na stejném období, abyste ověřili konzistenci výstupu před přepnutím.

## Začínáme

```bash
pip install bankstatementparser
```

```python
from bankstatementparser import create_parser, detect_statement_format

# Works with MT940 today, CAMT.053 tomorrow, PDF anytime
for file in bank_statement_files:
    fmt = detect_statement_format(file)
    parser = create_parser(file, fmt)
    df = parser.parse()
    process(df)  # Your code doesn't change
```

Pro PDF výpisy od bank, které zatím nenabízejí strukturované CAMT exporty:

```python
from bankstatementparser.hybrid import smart_ingest

result = smart_ingest("statement.pdf")
assert result.verification.status == "VERIFIED"
```

[Přečtěte si celou dokumentaci](/getting-started/index.html)

[Porovnejte s alternativami ❯](/comparison/index.html) | [Podívejte se na reálné případy použití ❯](/use-cases/index.html)
