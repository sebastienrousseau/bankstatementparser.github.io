---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Bankutdrag Parser Security"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Bank Statement Parser. Alla rättigheter reserverade."
date: "Apr 01, 2026"
description: "Säkerhetsfunktioner i Bank Statement Parser: XXE-skydd, ZIP-bombhärdning, PII-redaktion, leveranskedjans säkerhet, deterministisk utdata och signerade builds."
download: ""
format-detection: "telephone=no"
hreflang: "sv"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/sv/securite/index.html"
image_alt: "Logotyp för Bank Statement Parser, styrka din finansiella analys med sömlös dataextraktion"
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "kontoutdragssäkerhet, PII-redigeringspython, XXE-skydd, ZIP-bombskydd, leveranskedjans säkerhet SBOM, deterministisk analys, finansiell datasäkerhet"
language: "sv-SE"
layout: "about"
locale: "sv_SE"
logo_alt: "Logotyp för Bank Statement Parser, styrka din finansiella analys med sömlös dataextraktion"
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Säkerhet"
permalink: "https://bankstatementparser.com/sv/securite/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Hur vi skyddar dina ekonomiska uppgifter"
tags: "säkerhet,pii,xxe,sbom,försörjningskedja,deterministisk"
theme_color: "rgb(73, 214, 251)"
title: "Bank Statement Parser Security: Dataskydd och leveranskedja"
url: "https://bankstatementparser.com/sv/securite/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/sv/securite/rss.xml"
category: "Finansprogram, Python-bibliotek, databehandling"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Säkerhetsfunktioner i Bank Statement Parser: XXE-skydd, ZIP-bombhärdning, PII-redaktion, leveranskedjans säkerhet, deterministisk utdata och signerade builds."
item_guid: "https://bankstatementparser.com/sv/securite/rss.xml"
item_link: "https://bankstatementparser.com/sv/securite/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Bank Statement Parser Security: Dataskydd och leveranskedja"
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
apple-mobile-web-app-title: "Bank Statement Parser Security: Dataskydd och leveranskedja"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Säkerhetsfunktioner i Bank Statement Parser: XXE-skydd, ZIP-bombhärdning, PII-redaktion, leveranskedjans säkerhet, deterministisk utdata och signerade builds."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logotyp för Bank Statement Parser, styrka din finansiella analys med sömlös dataextraktion"
twitter_site: "@wwdseb"
twitter_title: "Bank Statement Parser Security: Dataskydd och leveranskedja"
twitter_url: "https://bankstatementparser.com/sv/securite/index.html"

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

**TL;DR:** Bank Statement Parser gör noll nätverksanrop, redigerar PII som standard, hårdnar XML-analys mot XXE-attacker och levereras med SHA-256 hash-låsta beroenden och en CycloneDX SBOM.

## Security by Design

Bank Statement Parser är byggd för att bearbeta känslig finansiell data. Varje designbeslut prioriterar säkerhet, integritet och revisionsbarhet.

## Noll nätverksåtkomst

All bearbetning sker lokalt inom din körtid. Biblioteket gör noll API-anrop, noll molnanslutningar och samlar in noll telemetri. XML-tolkare är uttryckligen konfigurerade med`no_network=True`, `resolve_entities=False`, och`load_dtd=False`för att förhindra all utgående åtkomst.

## PII-redaktion

Personligt identifierbar information (namn, IBAN, postadresser) redigeras automatiskt i CLI-utdata och streaming-läge. Detta är på som standard.

- **CLI**: Känsliga fält visas som`***REDACTED***`
- **Streaming**:`parse_streaming(redact_pii=True)`(standard)
- **Export**: CSV/JSON/Excel behåller fullständiga data för nedströmsbehandling
- **Opt-in**: Använd`--show-pii`eller`redact_pii=False`när du behöver oredigerad utdata

## XML-säkerhet (XXE-skydd)

Alla användningsområden för XML-tolkning`lxml`med härdade inställningar:

- `resolve_entities=False`-- förhindrar attacker av XML-entitetsexpansion
-`no_network=True`-- blockerar all utgående nätverksåtkomst från parsern
-`load_dtd=False`-- förhindrar DTD-baserade attacker
- Avlägsning av namnutrymme före bearbetning - hanterar alla CAMT.053-varianter säkert

## ZIP Archive Security

`iter_secure_xml_entries()`validerar varje ZIP-medlem innan extrahering:

- **Entréstorlekstak**: 10 MB per post (konfigurerbar)
- **Totalt storlekstak**: 50 MB totalt okomprimerat (konfigurerbart)
- **Kompressionsförhållandegräns**: 100:1 standard - upptäcker ZIP-bomber
- **Krypterad postavvisning**: Krypterade poster hoppas över med en varning
- **Ingen diskskrivning**: XML-bytes skickas direkt till parsern via`from_bytes()`

## Förebyggande av vägpassering

Indatavalidering blockerar farliga filsökvägar:

- Nullbyte, kataloggenomgångsmönster (`../`), och symboliska länkar avvisas
- Verifiering av filtillägg mot förväntade format
- Filstorleksgränser (100 MB standard, konfigurerbar)

## Deterministisk utdata

Med samma indatafil producerar parsern byte-identisk utdata varje körning. Ingen slumpmässighet, ingen modellinferens, ingen heuristisk sampling. Detta är avgörande för:

- **Reproducerbarhet för granskning**: Kör samma fil två gånger och ändra resultatet
- **Föreskriftsefterlevnad**: Demonstrera konsekvent bearbetning
- **CI-verifiering**: 467 tester framtvingar determinism med 100 % filialtäckning

## Supply Chain Security

- **SHA-256 hash-låsta beroenden**: Varje paket in`poetry.lock`har verifierat filhashar
- **CycloneDX SBOM**: Varje utgåva inkluderar en mjukvarulista
- **GitHub-byggets ursprung**: Attestation länkar varje artefakt till dess källförpliktelse
- **Signerade commits**: Alla commits är SSH-signerade och verifierade i CI
- **Verifiering av beroende**:`scripts/verify_locked_hashes.py`validerar alla hashs lokalt

## Verifiera lokalt

```bash
python -m pytest                          # 467 tests, 100% branch coverage
python scripts/verify_locked_hashes.py    # SHA-256 hash verification
git log --show-signature -1               # Verify commit signature
```
