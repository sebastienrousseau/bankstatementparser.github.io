---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Bezpieczeństwo analizatora wyciągów bankowych"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/corporate-finance.webp"
cdn: "https://cloudcdn.pro"
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Parser wyciągów bankowych. Wszelkie prawa zastrzeżone."
date: "Apr 01, 2026"
description: "Funkcje bezpieczeństwa Parsera wyciągów bankowych: ochrona XXE, wzmacnianie bomby ZIP, redagowanie danych osobowych, bezpieczeństwo łańcucha dostaw, dane wyjściowe deterministyczne i podpisane kompilacje."
download: ""
format-detection: "telephone=no"
hreflang: "pl"
icon: "https://cloudcdn.pro/bankstatementparser/images/favicon.ico"
id: "https://bankstatementparser.com/pl/bezpieczenstwo/index.html"
image_alt: "Logo analizatora wyciągów bankowych. Wzmocnij swoją analizę finansową dzięki płynnej ekstrakcji danych"
image_height: "630"
image_width: "1200"
image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
keywords: "bezpieczeństwo wyciągów bankowych, python redagujący dane osobowe, ochrona XXE, ochrona przed bombami ZIP, bezpieczeństwo łańcucha dostaw SBOM, analiza deterministyczna, bezpieczeństwo danych finansowych"
language: "pl-PL"
layout: "about"
locale: "pl_PL"
logo_alt: "Logo analizatora wyciągów bankowych. Wzmocnij swoją analizę finansową dzięki płynnej ekstrakcji danych"
logo_height: "44"
logo_width: "44"
logo: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Bezpieczeństwo"
permalink: "https://bankstatementparser.com/pl/bezpieczenstwo/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Jak chronimy Twoje dane finansowe"
tags: "bezpieczeństwo,pii,xxe,sbom,łańcuch dostaw,deterministyczny"
theme_color: "rgb(73, 214, 251)"
title: "Bezpieczeństwo analizatora wyciągów bankowych: ochrona danych i łańcuch dostaw"
url: "https://bankstatementparser.com/pl/bezpieczenstwo/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/pl/bezpieczenstwo/rss.xml"
category: "Oprogramowanie finansowe, biblioteka Python, przetwarzanie danych"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Funkcje bezpieczeństwa Parsera wyciągów bankowych: ochrona XXE, wzmacnianie bomby ZIP, redagowanie danych osobowych, bezpieczeństwo łańcucha dostaw, dane wyjściowe deterministyczne i podpisane kompilacje."
item_guid: "https://bankstatementparser.com/pl/bezpieczenstwo/rss.xml"
item_link: "https://bankstatementparser.com/pl/bezpieczenstwo/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Bezpieczeństwo analizatora wyciągów bankowych: ochrona danych i łańcuch dostaw"
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
apple-mobile-web-app-title: "Bezpieczeństwo analizatora wyciągów bankowych: ochrona danych i łańcuch dostaw"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Funkcje bezpieczeństwa Parsera wyciągów bankowych: ochrona XXE, wzmacnianie bomby ZIP, redagowanie danych osobowych, bezpieczeństwo łańcucha dostaw, dane wyjściowe deterministyczne i podpisane kompilacje."
twitter_image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logo analizatora wyciągów bankowych. Wzmocnij swoją analizę finansową dzięki płynnej ekstrakcji danych"
twitter_site: "@wwdseb"
twitter_title: "Bezpieczeństwo analizatora wyciągów bankowych: ochrona danych i łańcuch dostaw"
twitter_url: "https://bankstatementparser.com/pl/bezpieczenstwo/index.html"

# Humans.txt - The Humans.txt front matter (YAML).

author_website: "https://bankstatementparser.com"
author_twitter: "@wwdseb"
author_location: "London, UK"
thanks: "Dziękuję za przeczytanie!"
site_last_updated: "2026-04-01"
site_standards: "HTML5, CSS3, RSS, Atom, JSON, XML, YAML, Markdown, TOML"
site_components: "Shokunin SSG, Shokunin CLI, Shokunin Templates, Shokunin Themes, Kaishi SSG, Kaishi CLI, Kaishi Templates, Kaishi Themes"
site_software: "Shokunin, Rust"

---

**TL;DR:** Parser wyciągów bankowych nie wykonuje żadnych połączeń sieciowych, domyślnie redaguje dane PII, wzmacnia analizę XML przed atakami XXE i jest dostarczany z zależnościami z blokadą skrótu SHA-256 i SBOM CycloneDX.

## Bezpieczeństwo już w fazie projektowania

Parser wyciągów bankowych jest przeznaczony do przetwarzania wrażliwych danych finansowych. Przy każdej decyzji projektowej priorytetem jest bezpieczeństwo, prywatność i możliwość kontroli.

## Zerowy dostęp do sieci

Całe przetwarzanie odbywa się lokalnie w środowisku wykonawczym. Biblioteka nie wykonuje żadnych wywołań API, żadnych połączeń z chmurą i zbiera żadnych danych telemetrycznych. Parsery XML są jawnie skonfigurowane za pomocą`no_network=True`, `resolve_entities=False`, I`load_dtd=False`aby uniemożliwić dostęp wychodzący.

## Redakcja dotycząca informacji umożliwiających identyfikację

Informacje umożliwiające identyfikację (nazwiska, numery IBAN, adresy pocztowe) są automatycznie redagowane w trybie CLI i trybie przesyłania strumieniowego. Ta opcja jest domyślnie włączona.

- **CLI**: Wrażliwe pola są wyświetlane jako`***REDACTED***`
- **Przesyłanie strumieniowe**:`parse_streaming(redact_pii=True)`(domyślny)
- **Eksport**: CSV/JSON/Excel zachowuje pełne dane do dalszego przetwarzania
- **Zgoda**: Użyj`--show-pii`Lub`redact_pii=False`kiedy potrzebujesz niezredagowanych wyników

## Bezpieczeństwo XML (ochrona XXE)

Wszystkie zastosowania analizowania XML`lxml`z ustawieniami hartowanymi:

- `resolve_entities=False`-- zapobiega atakom polegającym na rozszerzaniu jednostek XML
-`no_network=True`-- blokuje cały wychodzący dostęp sieciowy z parsera
-`load_dtd=False`-- zapobiega atakom opartym na DTD
- Usuwanie przestrzeni nazw przed przetwarzaniem - bezpiecznie obsługuje każdy wariant CAMT.053

## Bezpieczeństwo archiwum ZIP

`iter_secure_xml_entries()`sprawdza każdego członka ZIP przed ekstrakcją:

- **Ograniczenie rozmiaru wpisu**: 10 MB na wpis (konfigurowalne)
- **Całkowity limit rozmiaru**: łącznie 50 MB bez kompresji (konfigurowalne)
- **Limit współczynnika kompresji**: domyślnie 100:1 — wykrywa bomby ZIP
- **Odrzucenie wpisu zaszyfrowanego**: Wpisy zaszyfrowane są pomijane z ostrzeżeniem
- **Żaden zapis na dysku**: Bajty XML przesyłane są bezpośrednio do parsera poprzez`from_bytes()`

## Zapobieganie przechodzeniu ścieżki

Sprawdzanie poprawności danych wejściowych blokuje niebezpieczne ścieżki plików:

- Bajty zerowe, wzorce poruszania się po katalogach (`../`), a dowiązania symboliczne są odrzucane
- Sprawdzanie rozszerzeń plików względem oczekiwanych formatów
- Limity rozmiaru plików (domyślnie 100 MB, konfigurowalne)

## Deterministyczne wyjście

Biorąc pod uwagę ten sam plik wejściowy, parser generuje dane wyjściowe o identycznych bajtach przy każdym uruchomieniu. Żadnej losowości, żadnego wnioskowania o modelu, żadnego próbkowania heurystycznego. Ma to kluczowe znaczenie dla:

- **Kontrola odtwarzalności**: Uruchom ten sam plik dwa razy i porównaj wyniki
- **Zgodność z przepisami**: Wykazanie spójnego przetwarzania
- **Weryfikacja CI**: 467 testów wymusza determinizm przy 100% pokryciu gałęzi

## Bezpieczeństwo łańcucha dostaw

- **Zależności z blokadą skrótu SHA-256**: Każdy pakiet w`poetry.lock`zweryfikował skróty plików
- **CycloneDX SBOM**: Każde wydanie zawiera zestawienie materiałów oprogramowania
- **Pochodzenie kompilacji GitHub**: Poświadczenie łączy każdy artefakt z jego zatwierdzeniem źródłowym
- **Podpisane zatwierdzenia**: Wszystkie zatwierdzenia są podpisane przez SSH i zweryfikowane w CI
- **Weryfikacja zależności**:`scripts/verify_locked_hashes.py`sprawdza wszystkie skróty lokalnie

## Sprawdź lokalnie

```bash
python -m pytest                          # 467 tests, 100% branch coverage
python scripts/verify_locked_hashes.py    # SHA-256 hash verification
git log --show-signature -1               # Verify commit signature
```
