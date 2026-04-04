---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Przewodnik po migracji ISO 20022"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/corporate-finance.webp"
cdn: "https://cloudcdn.pro"
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Parser wyciągów bankowych. Wszelkie prawa zastrzeżone."
date: "Apr 01, 2026"
description: "Praktyczny przewodnik po harmonogramie migracji SWIFT ISO 20022 (2026–2028), przejściu z MT940 na CAMT.053 oraz o tym, jak Analizator wyciągów bankowych pomaga zespołom skarbowym w migracji."
download: ""
format-detection: "telephone=no"
hreflang: "pl"
icon: "https://cloudcdn.pro/bankstatementparser/images/favicon.ico"
id: "https://bankstatementparser.com/pl/migracja/index.html"
image_alt: "Logo analizatora wyciągów bankowych. Wzmocnij swoją analizę finansową dzięki płynnej ekstrakcji danych"
image_height: "630"
image_width: "1200"
image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
keywords: "Migracja ISO 20022, MT940 do CAMT.053, termin SWIFT 2027, wycofanie MT940 2028, migracja wyciągów bankowych w Pythonie, parser CAMT.053, oś czasu ISO 20022"
language: "pl-PL"
layout: "about"
locale: "pl_PL"
logo_alt: "Logo analizatora wyciągów bankowych. Wzmocnij swoją analizę finansową dzięki płynnej ekstrakcji danych"
logo_height: "44"
logo_width: "44"
logo: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Przewodnik po migracji ISO 20022"
permalink: "https://bankstatementparser.com/pl/migracja/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Przejdź do przejścia SWIFT MT na ISO 20022"
tags: "iso20022,migracja,mt940,camt053,swift,oś czasu"
theme_color: "rgb(73, 214, 251)"
title: "Przewodnik po migracji ISO 20022: Przejście z MT940 na CAMT.053"
url: "https://bankstatementparser.com/pl/migracja/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/pl/migracja/rss.xml"
category: "Oprogramowanie finansowe, biblioteka Python, przetwarzanie danych"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Praktyczny przewodnik po harmonogramie migracji SWIFT ISO 20022 (2026–2028), przejściu z MT940 na CAMT.053 oraz o tym, jak Analizator wyciągów bankowych pomaga zespołom skarbowym w migracji."
item_guid: "https://bankstatementparser.com/pl/migracja/rss.xml"
item_link: "https://bankstatementparser.com/pl/migracja/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Przewodnik po migracji ISO 20022: Przejście z MT940 na CAMT.053"
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
apple-mobile-web-app-title: "Przewodnik po migracji ISO 20022: Przejście z MT940 na CAMT.053"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Praktyczny przewodnik po harmonogramie migracji SWIFT ISO 20022 (2026–2028), przejściu z MT940 na CAMT.053 oraz o tym, jak Analizator wyciągów bankowych pomaga zespołom skarbowym w migracji."
twitter_image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logo analizatora wyciągów bankowych. Wzmocnij swoją analizę finansową dzięki płynnej ekstrakcji danych"
twitter_site: "@wwdseb"
twitter_title: "Przewodnik po migracji ISO 20022: Przejście z MT940 na CAMT.053"
twitter_url: "https://bankstatementparser.com/pl/migracja/index.html"

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

**TL;DR:** SWIFT wycofa MT940 do listopada 2028 r. Parser wyciągów bankowych obsługuje zarówno MT940, jak i CAMT.053 za pomocą jednego interfejsu API, więc potok analizowania działa podczas przejścia i po nim.

## Dlaczego ta migracja ma znaczenie

SWIFT wycofuje starsze formaty wiadomości MT na rzecz bogatszego standardu ISO 20022. Dla zespołów skarbowych i finansowych oznacza to, że procesy przetwarzania wyciągów bankowych muszą ewoluować z MT940 do CAMT.053 przed upływem sztywnych terminów.

## Harmonogram migracji SWIFT

| Data | Kamień milowy | Uderzenie |
|---|---|---|
| **Listopad 2025** | Zakończono współistnienie MT-MX w przypadku płatności transgranicznych | Komunikaty PACS są teraz dostępne wyłącznie w formacie ISO 20022 |
| **Listopad 2026** | Adresy strukturalne/hybrydowe obowiązkowe; Odrzucono wiele instrukcji MT101; Faza zarządzania przypadkami 1 | Formaty adresów muszą być zgodne; niektóre wiadomości MT zostaną odrzucone |
| **Koniec 2026 r.** | Rozpoczyna się rejestracja na otrzymywanie CAMT.052/.053/.054 | Instytucje finansowe mogą zacząć otrzymywać natywne wyciągi ISO |
| **Listopad 2027** | Wszystkie FI muszą otrzymać natywnie CAMT.053 | SWIFT przestaje konwertować format MT na ISO; Twoje systemy muszą bezpośrednio analizować CAMT |
| **Listopad 2028** | MT940/MT942/MT950/MT900/MT910 całkowicie wycofane | Starsze formaty wyciągów nie są już dostępne; Jedyną opcją są CAMT.052/.053/.054 |

## Jakie zmiany w Twoim kodzie

### Przed: tylko MT940

```python
from bankstatementparser import Mt940Parser

parser = Mt940Parser("statement.mt940")
df = parser.parse()
```

### Po: oba formaty z funkcją automatycznego wykrywania

```python
from bankstatementparser import create_parser, detect_statement_format

fmt = detect_statement_format("statement.xml")  # or .mt940
parser = create_parser("statement.xml", fmt)
df = parser.parse()  # Same DataFrame schema regardless of format
```

The`detect_statement_format()`funkcja określa, czy plik ma format MT940, CAMT.053, PAIN.001, czy inny obsługiwany format. The`create_parser()`funkcja zwraca poprawny parser. Twój kod źródłowy działa identycznie niezależnie od formatu źródłowego.

## CAMT.053 vs MT940: Kluczowe różnice

| Funkcja | MT940 | CAMT.053 |
|---|---|---|
| Bogactwo danych | Ograniczone pola | 3-5 razy więcej danych na transakcję |
| Zestaw znaków | Ograniczone (zestaw znaków SWIFT) | Pełny Unicode |
| Struktura | Płaski tekst ze znacznikami | XML z przestrzeniami nazw |
| Raportowanie salda | Tylko otwieranie/zamykanie | Wiele typów sald |
| Referencje | Pojedyncze pole referencyjne | Wiele typów odwołań |
| Obsługa walut | Podstawowy | Pełna wielowalutowość z kursami wymiany |

## Jak analizator wyciągów bankowych pomaga

- **Ujednolicony interfejs API**: Analizuj zarówno MT940, jak i CAMT.053 za pomocą tego samego`parse()`metodę, tworząc identyczne schematy DataFrame.
- **Automatyczne wykrywanie**: Nie ma potrzeby wcześniejszej znajomości formatu.`detect_statement_format()`identyfikuje go automatycznie.
- **Niezależny od przestrzeni nazw**: Obsługuje każdy wariant CAMT.053 (001.02, 001.04 lub opakowania specyficzne dla banku) bez konfiguracji.
- **Przesyłanie strumieniowe**: Przetwarzaj duże pliki CAMT (ponad 50 MB, ponad 50 tys. transakcji) przy ograniczonej pamięci.
- **Testowanie migracji**: Uruchom oba parsery obok siebie w tym samym zakresie dat, aby sprawdzić spójność danych wyjściowych przed przełączeniem.

## Pierwsze kroki

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

[Przeczytaj pełną dokumentację](/getting-started/index.html)

[Porównaj z alternatywami ❯](/comparison/index.html) | [Zobacz rzeczywiste przypadki użycia ❯](/use-cases/index.html)
