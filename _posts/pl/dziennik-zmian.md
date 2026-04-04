---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Dziennik zmian analizatora wyciągów bankowych"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Parser wyciągów bankowych. Wszelkie prawa zastrzeżone."
date: "Apr 01, 2026"
description: "Historia wydań i dziennik zmian dla Parsera wyciągów bankowych. Śledź nowe funkcje, ulepszenia i poprawki błędów we wszystkich wersjach."
download: ""
format-detection: "telephone=no"
hreflang: "pl"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/pl/dziennik-zmian/index.html"
image_alt: "Logo analizatora wyciągów bankowych. Wzmocnij swoją analizę finansową dzięki płynnej ekstrakcji danych"
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "Dziennik zmian analizatora wyciągów bankowych, informacje o wersji, historia wersji, aktualizacje"
language: "pl-PL"
layout: "about"
locale: "pl_PL"
logo_alt: "Logo analizatora wyciągów bankowych. Wzmocnij swoją analizę finansową dzięki płynnej ekstrakcji danych"
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Dziennik zmian"
permalink: "https://bankstatementparser.com/pl/dziennik-zmian/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Historia wydań i nowości"
tags: "dziennik zmian, wydania, aktualizacje, wersje, ogłoszenia, blog"
theme_color: "rgb(73, 214, 251)"
title: "Dziennik zmian analizatora wyciągów bankowych"
url: "https://bankstatementparser.com/pl/dziennik-zmian/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/pl/dziennik-zmian/rss.xml"
category: "Oprogramowanie finansowe, biblioteka Python, przetwarzanie danych"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Historia wydań i dziennik zmian dla Parsera wyciągów bankowych. Śledź nowe funkcje, ulepszenia i poprawki błędów we wszystkich wersjach."
item_guid: "https://bankstatementparser.com/pl/dziennik-zmian/rss.xml"
item_link: "https://bankstatementparser.com/pl/dziennik-zmian/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Dziennik zmian analizatora wyciągów bankowych"
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
apple-mobile-web-app-title: "Dziennik zmian analizatora wyciągów bankowych"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Historia wydań i dziennik zmian dla Parsera wyciągów bankowych. Śledź nowe funkcje, ulepszenia i poprawki błędów we wszystkich wersjach."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logo analizatora wyciągów bankowych. Wzmocnij swoją analizę finansową dzięki płynnej ekstrakcji danych"
twitter_site: "@wwdseb"
twitter_title: "Dziennik zmian analizatora wyciągów bankowych"
twitter_url: "https://bankstatementparser.com/pl/dziennik-zmian/index.html"

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

Śledź rozwój analizatora wyciągów bankowych. Subskrybuj przez [RSS](/changelog/rss.xml) lub obejrzyj [repozytorium GitHub](https://github.com/sebastienrousseau/bankstatementparser) dla powiadomień o wydaniu.

## v0.0.4 — 2026-03-15 (najnowszy)

- Dodano równoległe analizowanie plików za pomocą`parse_files_parallel()`przy użyciu ProcessPoolExecutora.
- Dodano prawdziwe przesyłanie strumieniowe dla dużych plików PAIN.001 (50 MB+) z ograniczoną pamięcią.
- Optymalizacja wydajności: przepustowość CAMT przekracza obecnie 27 000 tx/s, PAIN.001 przekracza 52 000 tx/s.
- Dodano`Deduplicator`klasa do wykrywania dokładnych duplikatów i podejrzanych dopasowań z wynikami zaufania.
- Dodano`from_string()`I`from_bytes()`metody analizowania w pamięci bez operacji we/wy dysku.
- Dodano`iter_secure_xml_entries()`do bezpiecznego przetwarzania archiwum ZIP.
— Rozszerzony CI z egzekwowaniem progów wydajności.

## v0.0.3 — 20.11.2025

— Dodano obsługę analizatora CSV, OFX, QFX i MT940.
- Dodano automatyczne wykrywanie formatu za pomocą`detect_statement_format()`I`create_parser()`.
- Dodano redakcję PII (domyślnie włączona w trybie CLI i trybie przesyłania strumieniowego).
- Dodano pomocników eksportu dla CSV, JSON i Excel.
— Dodano opcjonalną obsługę Polars DataFrame.
- Rozszerzony zestaw testów do 467 testów ze 100% pokryciem gałęzi.

## v0.0.2 — 2025-06-10

- Dodano parser PAIN.001 (`Pain001Parser`) dla plików inicjowania polecenia przelewu ISO 20022.
- Dodano interfejs CLI (`python -m bankstatementparser.cli`).
- Dodano tryb przesyłania strumieniowego z`parse_streaming()`.
- Dodano sprawdzanie poprawności danych wejściowych i ograniczenia rozmiaru pliku.

## v0.0.1 — 15.01.2025

- Pierwsze wydanie.
- Parser CAMT.053 (`CamtParser`) w przypadku wyciągów bankowych dla klientów zgodnych z normą ISO 20022.
- wyjście DataFrame pand.
- Podstawowe wzmocnienie bezpieczeństwa XML (ochrona XXE, no_network).

Wyświetl pełną historię zatwierdzeń w [GitHub](https://github.com/sebastienrousseau/bankstatementparser/commits/main).

<script type="application/ld+json">
{
  „@kontekst”: „https://schema.org",
  "@type": "Aplikacja oprogramowania",
  "name": "Parser wyciągów bankowych",
  "applicationCategory": "Aplikacja programisty",
  "operatingSystem": "Wieloplatformowy",
  "Wersja oprogramowania": "0.0.4",
  "datePublished": "2026-03-15",
  "releaseNotes": "Dodano równoległe analizowanie plików, prawdziwe przesyłanie strumieniowe dla PAIN.001, optymalizacje wydajności (27K+ tx/s CAMT, 52K+ tx/s PAIN.001), klasa deduplikatora, analizowanie w pamięci, bezpieczne przetwarzanie ZIP.",
  "adres pobierania": "https://pypi.org/project/bankstatementparser/",
  "licencja": "https://opensource.org/licenses/Apache-2.0",
  „autor”: {
    "@typ": "Osoba",
    "imię": "Sebastien Rousseau"
  }
}
</skrypt>
