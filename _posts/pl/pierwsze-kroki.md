---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Biały budynek z czarnymi oknami"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/daniele-franchi-Vl6YuVBLEys.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Parser wyciągów bankowych. Wszelkie prawa zastrzeżone."
date: "Apr 01, 2026"
description: "Rozpocznij pracę z analizatorem wyciągów bankowych dla języka Python: zainstaluj, analizuj pliki CAMT/PAIN.001/CSV/OFX/QFX/MT940 i korzystaj ze strumieniowania lub przepływów pracy CLI."
download: ""
format-detection: "telephone=no"
hreflang: "pl"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/pl/pierwsze-kroki/index.html"
image_alt: "Logo Parsera wyciągów bankowych, potężnego narzędzia Pythona przeznaczonego do szybkiego i dokładnego przetwarzania danych finansowych i wydobywania spostrzeżeń."
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "parser wyciągów bankowych, pierwsze kroki, python, CAMT, PAIN.001, CSV, OFX, QFX, MT940, dane finansowe"
language: "pl-PL"
layout: "start"
locale: "pl_PL"
logo_alt: "Logo Parsera wyciągów bankowych, potężnego narzędzia Pythona przeznaczonego do szybkiego i dokładnego przetwarzania danych finansowych i wydobywania spostrzeżeń."
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Pierwsze kroki"
permalink: "https://bankstatementparser.com/pl/pierwsze-kroki/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Rozpocznij tworzenie bezpiecznych aplikacji za pomocą analizatora wyciągów bankowych"
tags: "bank, wyciąg, parser, python, camt, pain001, csv, ofx, qfx, mt940, przesyłanie strumieniowe, cli"
theme_color: "rgb(73, 214, 251)"
title: "Parser wyciągów bankowych: podręcznik instalacji i użytkowania"
url: "https://bankstatementparser.com/pl/pierwsze-kroki/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/pl/pierwsze-kroki/rss.xml"
category: "Oprogramowanie finansowe, biblioteka Pythona, przewodnik programisty"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Rozpocznij pracę z analizatorem wyciągów bankowych dla języka Python: zainstaluj, analizuj pliki CAMT/PAIN.001/CSV/OFX/QFX/MT940 i korzystaj ze strumieniowania lub przepływów pracy CLI."
item_guid: "https://bankstatementparser.com/pl/pierwsze-kroki/rss.xml"
item_link: "https://bankstatementparser.com/pl/pierwsze-kroki/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Parser wyciągów bankowych: podręcznik instalacji i użytkowania"
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
apple-mobile-web-app-title: "Parser wyciągów bankowych: podręcznik instalacji i użytkowania"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Zainstaluj i używaj Parsera wyciągów bankowych do analizowania plików CAMT, PAIN.001, CSV, OFX/QFX i MT940 w języku Python."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logo Parsera wyciągów bankowych, potężnego narzędzia Pythona przeznaczonego do szybkiego i dokładnego przetwarzania danych finansowych i wydobywania spostrzeżeń."
twitter_site: "@wwdseb"
twitter_title: "Parser wyciągów bankowych: podręcznik instalacji i użytkowania"
twitter_url: "https://bankstatementparser.com/pl/pierwsze-kroki/index.html"

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

## Wymagania

- Python 3.9 do 3.14
- Dostęp do terminala (macOS, Linux lub WSL)

## Zainstaluj

```bash
pip install bankstatementparser
```

W przypadku obsługi Polars DataFrame:

```bash
pip install bankstatementparser[polars]
```

## Szybki start

### Automatyczne wykrywanie i analizowanie dowolnego formatu

```python
from bankstatementparser import create_parser, detect_statement_format

fmt = detect_statement_format("transactions.ofx")
parser = create_parser("transactions.ofx", fmt)
df = parser.parse()  # pandas DataFrame
print(df.head())
```

To działa z`.xml`(CAMT/BÓL.001),`.csv`, `.ofx`, `.qfx`, `.mt940`, I`.sta`akta.

### Przeanalizuj CAMT.053

```python
from bankstatementparser import CamtParser

parser = CamtParser("statement.xml")
transactions = parser.parse()
```

### Przeanalizuj plik PAIN.001

```python
from bankstatementparser import Pain001Parser

parser = Pain001Parser("payment.xml")
payments = parser.parse()
```

## Przesyłanie strumieniowe dużych plików

W przypadku plików zawierających tysiące transakcji użyj przesyłania strumieniowego, aby ograniczyć pamięć:

```python
parser = CamtParser("large_statement.xml")
for transaction in parser.parse_streaming(redact_pii=True):
    process(transaction)  # Memory stays constant
```

## Analiza w pamięci

Analizuj bajty bez dyskowych operacji we/wy — przydatne w przepływach pracy SFTP lub API:

```python
xml_bytes = download_from_sftp()
parser = CamtParser.from_bytes(xml_bytes, source_name="daily.xml")
transactions = parser.parse()
```

## Równoległe przetwarzanie plików

Analizuj wiele plików jednocześnie:

```python
from bankstatementparser import parse_files_parallel

results = parse_files_parallel([
    "statements/jan.xml",
    "statements/feb.xml",
    "statements/mar.xml",
])
for r in results:
    print(r.path, r.status, len(r.transactions), "rows")
```

## Deduplikacja

Wykrywaj dokładne duplikaty i podejrzane dopasowania za pomocą wskaźników zaufania:

```python
from bankstatementparser import CamtParser, Deduplicator

parser = CamtParser("statement.xml")
dedup = Deduplicator()
result = dedup.deduplicate(dedup.from_dataframe(parser.parse()))

print(f"Unique: {len(result.unique_transactions)}")
print(f"Exact duplicates: {len(result.exact_duplicates)}")
print(f"Suspected matches: {len(result.suspected_matches)}")
```

## Bezpieczne przetwarzanie ZIP

Przetwarzaj spakowane pliki XML z wbudowanymi kontrolami bezpieczeństwa (ochrona przed bombami, odrzucanie zaszyfrowanych wpisów):

```python
from bankstatementparser import iter_secure_xml_entries, CamtParser

for entry in iter_secure_xml_entries("statements.zip"):
    parser = CamtParser.from_bytes(entry.xml_bytes, source_name=entry.source_name)
    print(f"{entry.source_name}: {len(parser.parse())} transactions")
```

## Eksportuj

```python
parser = CamtParser("statement.xml")
parser.export_csv("output.csv")
parser.export_json("output.json")

# Polars (requires bankstatementparser[polars])
polars_df = parser.to_polars()
```

## Użycie interfejsu wiersza polecenia

```bash
# Parse and display
python -m bankstatementparser.cli --type camt --input statement.xml

# Export to CSV
python -m bankstatementparser.cli --type camt --input statement.xml --output transactions.csv

# Stream with PII visible
python -m bankstatementparser.cli --type camt --input statement.xml --streaming --show-pii
```

Opcje interfejsu wiersza polecenia:

- `--type {camt,pain001}`-- typ parsera
-`--input <path>`-- plik wejściowy
-`--output <csv_path>`-- eksport do CSV
-`--streaming`-- przesyłaj strumieniowo duże pliki
-`--show-pii`-- pokaż wrażliwe pola (domyślnie zredagowane)
-`--max-size <MB>`--limit rozmiaru pliku

## Konfiguracja rozwoju lokalnego

```bash
git clone https://github.com/sebastienrousseau/bankstatementparser.git
cd bankstatementparser
python3 -m venv .venv && source .venv/bin/activate
pip install poetry && poetry install --with dev
```

Uruchom zestaw testów:

```bash
pytest
```

## Dokumentacja API

### Klasy analizatora składni

| Klasa | Format | Import |
|---|---|---|
| `CamtParser` | CAMT.053 (ISO 20022) | `from bankstatementparser import CamtParser` |
| `Pain001Parser` | BÓL.001 (ISO 20022) | `from bankstatementparser import Pain001Parser` |
| `CsvStatementParser` | CSV | `from bankstatementparser import CsvStatementParser` |
| `OfxParser` | OFX | `from bankstatementparser import OfxParser` |
| `QfxParser` | QFX | `from bankstatementparser import QfxParser` |
| `Mt940Parser` | MT940 | `from bankstatementparser import Mt940Parser` |

### Funkcje użytkowe

| Funkcjonować | Zamiar |
|---|---|
| `detect_statement_format(path)` | Automatyczne wykrywanie formatu pliku |
| `create_parser(path, fmt)` | Utwórz odpowiedni analizator składni |
| `parse_files_parallel(paths)` | Analizuj wiele plików jednocześnie |
| `iter_secure_xml_entries(zip_path)` | Bezpiecznie iteruj wpisy ZIP |

### Klasy danych

| Klasa | Zamiar |
|---|---|
| `Deduplicator` | Wykrywaj duplikaty transakcji |
| `DeduplicationResult` | Wynik z unikalnymi, dokładnymi i podejrzanymi dopasowaniami |
| `InputValidator` | Sprawdź ścieżki i formaty plików |
| `Transaction` | Znormalizowany zapis transakcji |
| `FileResult` | Wynik analizy równoległej |
| `ZipXMLSource` | Opakowanie członka ZIP |

### Wyjątki

| Wyjątek | Kiedy podniesiony |
|---|---|
| `ParserError` | Błędy analizowania |
| `ExportError` | Błędy eksportu (CSV/JSON/Excel) |
| `ValidationError` | Błędy sprawdzania poprawności danych wejściowych |
| `ZipSecurityError` | Niepowodzenie kontroli zabezpieczeń ZIP |
