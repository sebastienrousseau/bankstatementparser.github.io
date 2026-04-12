---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Біла будівля з чорними вікнами"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/daniele-franchi-Vl6YuVBLEys.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Парсер банківських виписок. Всі права захищені."
date: "Apr 11, 2026"
description: "Почніть роботу з аналізатором банківських виписок для Python: установіть, проаналізуйте файли CAMT/PAIN.001/CSV/OFX/QFX/MT940 і використовуйте потокове передавання або робочі процеси CLI."
download: ""
format-detection: "telephone=no"
hreflang: "uk"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/uk/premiers-pas/index.html"
image_alt: "Логотип аналізатора банківських виписок, потужного інструменту Python, призначеного для швидкої й точної обробки фінансових даних і вилучення статистичних даних."
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "аналізатор банківських виписок, початок роботи, python, CAMT, PAIN.001, CSV, OFX, QFX, MT940, фінансові дані"
language: "uk-UA"
layout: "start"
locale: "uk_UA"
logo_alt: "Логотип аналізатора банківських виписок, потужного інструменту Python, призначеного для швидкої й точної обробки фінансових даних і вилучення статистичних даних."
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Початок роботи"
permalink: "https://bankstatementparser.com/uk/premiers-pas/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Почніть створювати безпечні програми за допомогою аналізатора банківських виписок"
tags: "банк,виписка,парсер,python,camt,pain001,csv,ofx,qfx,mt940,потокове передавання,cli"
theme_color: "rgb(73, 214, 251)"
title: "Парсер банківських виписок: посібник із встановлення та використання"
url: "https://bankstatementparser.com/uk/premiers-pas/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/uk/premiers-pas/rss.xml"
category: "Фінансове програмне забезпечення, бібліотека Python, посібник розробника"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Почніть роботу з аналізатором банківських виписок для Python: установіть, проаналізуйте файли CAMT/PAIN.001/CSV/OFX/QFX/MT940 і використовуйте потокове передавання або робочі процеси CLI."
item_guid: "https://bankstatementparser.com/uk/premiers-pas/rss.xml"
item_link: "https://bankstatementparser.com/uk/premiers-pas/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Парсер банківських виписок: посібник із встановлення та використання"
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
apple-mobile-web-app-title: "Парсер банківських виписок: посібник із встановлення та використання"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Установіть і використовуйте аналізатор банківських виписок для аналізу файлів CAMT, PAIN.001, CSV, OFX/QFX і MT940 у Python."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Логотип аналізатора банківських виписок, потужного інструменту Python, призначеного для швидкої й точної обробки фінансових даних і вилучення статистичних даних."
twitter_site: "@wwdseb"
twitter_title: "Парсер банківських виписок: посібник із встановлення та використання"
twitter_url: "https://bankstatementparser.com/uk/premiers-pas/index.html"

# Humans.txt - The Humans.txt front matter (YAML).

author_website: "https://bankstatementparser.com"
author_twitter: "@wwdseb"
author_location: "London, UK"
thanks: "Дякуємо за читання!"
site_last_updated: "2026-04-01"
site_standards: "HTML5, CSS3, RSS, Atom, JSON, XML, YAML, Markdown, TOML"
site_components: "Shokunin SSG, Shokunin CLI, Shokunin Templates, Shokunin Themes, Kaishi SSG, Kaishi CLI, Kaishi Templates, Kaishi Themes"
site_software: "Shokunin, Rust"

---

## Вимоги

- Python 3.10–3.14
- Доступ до терміналу (macOS, Linux або WSL)

## Встановлення

```bash
# Базове встановлення (тільки детерміністичні парсери)
pip install bankstatementparser
```

Додаткові модулі для розширених можливостей:

```bash
# Text-LLM path for digital PDFs (litellm + pypdf)
pip install ‘bankstatementparser[hybrid]’

# Higher-fidelity table extraction (adds pdfplumber)
pip install ‘bankstatementparser[hybrid-plus]’

# Vision-LLM path for scanned PDFs (adds pypdfium2)
pip install ‘bankstatementparser[hybrid-vision]’

# LLM-powered transaction categorisation
pip install ‘bankstatementparser[enrichment]’

# REST API microservice (FastAPI + uvicorn)
pip install ‘bankstatementparser[api]’

# Optional Polars DataFrame support
pip install ‘bankstatementparser[polars]’
```

## Швидкий старт

### Автовизначення та аналіз будь-якого структурованого формату

```python
from bankstatementparser import create_parser, detect_statement_format

fmt = detect_statement_format("transactions.ofx")
parser = create_parser("transactions.ofx", fmt)
df = parser.parse()  # pandas DataFrame
print(df.head())
```

Це працює з файлами `.xml` (CAMT/PAIN.001), `.csv`, `.ofx`, `.qfx`, `.mt940` та `.sta`.

### Аналіз CAMT.053

```python
from bankstatementparser import CamtParser

parser = CamtParser("statement.xml")
transactions = parser.parse()
```

### Аналіз PAIN.001

```python
from bankstatementparser import Pain001Parser

parser = Pain001Parser("payment.xml")
payments = parser.parse()
```

### Аналіз PDF банківських виписок (гібридний pipeline)

Гібридний pipeline інтелектуально маршрутизує PDF через три шляхи витягування:

```python
from bankstatementparser.hybrid import smart_ingest

result = smart_ingest("statement.pdf")
print(result.source_method)         # "deterministic" | "llm" | "vision"
print(result.verification.status)   # VERIFIED | DISCREPANCY | FAILED
print(result.transactions)          # List of extracted transactions
```

Кожне витягування перевіряється **Золотим правилом**: `opening + credits − debits == closing`.

## Streaming великих файлів

Для файлів із тисячами транзакцій використовуйте streaming для обмеження пам’яті:

```python
parser = CamtParser("large_statement.xml")
for transaction in parser.parse_streaming(redact_pii=True):
    process(transaction)  # Memory stays constant
```

## Аналіз у пам’яті

Аналіз із байтів без дискового введення-виведення — зручно для SFTP або API:

```python
xml_bytes = download_from_sftp()
parser = CamtParser.from_bytes(xml_bytes, source_name="daily.xml")
transactions = parser.parse()
```

## Паралельна обробка файлів

Аналізуйте кілька файлів одночасно:

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

## Масове сканування каталогів

Обробка цілих дерев каталогів з автоматичною дедуплікацією:

```python
from bankstatementparser.hybrid import scan_and_ingest

batch = scan_and_ingest("statements/2026/", pattern="**/*.pdf")
print(f"Processed: {len(batch.results)} files")
print(f"Unique transactions: {batch.unique_count}")
```

## Дедуплікація

Ідемпотентні hash транзакцій для безпечного інкрементального завантаження:

```python
from bankstatementparser import CamtParser, Deduplicator

parser = CamtParser("statement.xml")
dedup = Deduplicator()
result = dedup.deduplicate(dedup.from_dataframe(parser.parse()))

print(f"Unique: {len(result.unique_transactions)}")
print(f"Exact duplicates: {len(result.exact_duplicates)}")
print(f"Suspected matches: {len(result.suspected_matches)}")
```

## Категоризація транзакцій (збагачення)

Автоматична категоризація транзакцій за допомогою LLM:

```python
from bankstatementparser.enrichment import Categorizer

categorizer = Categorizer()
enriched = categorizer.categorize_batch(transactions)
for txn in enriched:
    print(f"{txn.description}: {txn.category}")
```

## Експорт у бухгалтерію (hledger / beancount)

Експорт транзакцій у формати plaintext-accounting:

```python
from bankstatementparser.export import to_hledger, to_beancount

journal = to_hledger(transactions, account="Assets:Bank:Checking")
beancount_journal = to_beancount(transactions, account="Assets:Bank:Checking")
```

## Мультивалютна перевірка балансу

Перевірка балансу незалежно для кожної групи валют:

```python
from bankstatementparser.hybrid import verify_balance_multi_currency

results = verify_balance_multi_currency(transactions)
for currency, verification in results.items():
    print(f"{currency}: {verification.status}")
```

## REST API

Розгортання як мікросервіс FastAPI:

```bash
# Start the API server
bankstatementparser-api --port 8000

# For container deployments
bankstatementparser-api --host 0.0.0.0 --port 9000
```

Ендпоінти:
- `POST /ingest` -- Аналіз файлу банківської виписки
- `GET /health` -- Перевірка стану

## Безпечна обробка ZIP

Обробка заархівованих XML-файлів із вбудованими перевірками безпеки (захист від бомб, відхилення зашифрованих записів):

```python
from bankstatementparser import iter_secure_xml_entries, CamtParser

for entry in iter_secure_xml_entries("statements.zip"):
    parser = CamtParser.from_bytes(entry.xml_bytes, source_name=entry.source_name)
    print(f"{entry.source_name}: {len(parser.parse())} transactions")
```

## Експорт

```python
parser = CamtParser("statement.xml")
parser.export_csv("output.csv")
parser.export_json("output.json")

# Polars (requires bankstatementparser[polars])
polars_df = parser.to_polars()

# Excel
parser.camt_to_excel("output.xlsx")
```

## Використання CLI

```bash
# Parse structured formats
bankstatementparser --type camt --input statement.xml
bankstatementparser --type pain001 --input payment.xml

# Hybrid PDF pipeline
bankstatementparser --type ingest --input statement.pdf
bankstatementparser --type ingest --input statement.pdf --output ledger.csv

# Interactive review mode
bankstatementparser --type review --input result.json
bankstatementparser --type review --input result.json --output reviewed.json

# Export to CSV with streaming
bankstatementparser --type camt --input statement.xml --output transactions.csv
bankstatementparser --type camt --input statement.xml --streaming --show-pii
```

Параметри CLI:

- `--type {camt,pain001,ingest,review}` -- тип парсера або режим
- `--input <path>` -- вхідний файл
- `--output <path>` -- файл експорту (CSV або JSON)
- `--streaming` -- streaming великих файлів
- `--show-pii` -- показати конфіденційні поля (приховані за замовчуванням)
- `--max-size <MB>` -- обмеження розміру файлу

## Налаштування локальної розробки

```bash
git clone https://github.com/sebastienrousseau/bankstatementparser.git
cd bankstatementparser
python3 -m venv .venv && source .venv/bin/activate
pip install poetry && poetry install --with dev
make install-hooks   # pre-commit hook runs `make verify` before every commit
```

Запуск тестів:

```bash
pytest
```

## Довідник API

### Класи парсерів

| Клас | Формат | Імпорт |
|---|---|---|
| `CamtParser` | CAMT.053 (ISO 20022) | `from bankstatementparser import CamtParser` |
| `Pain001Parser` | PAIN.001 (ISO 20022) | `from bankstatementparser import Pain001Parser` |
| `CsvStatementParser` | CSV | `from bankstatementparser import CsvStatementParser` |
| `OfxParser` | OFX | `from bankstatementparser import OfxParser` |
| `QfxParser` | QFX | `from bankstatementparser import QfxParser` |
| `Mt940Parser` | MT940 | `from bankstatementparser import Mt940Parser` |
| `smart_ingest()` | PDF (гібридний pipeline) | `from bankstatementparser.hybrid import smart_ingest` |

### Допоміжні функції

| Функція | Призначення |
|---|---|
| `detect_statement_format(path)` | Автовизначення формату файлу |
| `create_parser(path, fmt)` | Створення відповідного парсера |
| `parse_files_parallel(paths)` | Паралельний аналіз кількох файлів |
| `iter_secure_xml_entries(zip_path)` | Безпечна ітерація записів ZIP |
| `smart_ingest(path)` | Гібридне витягування з PDF з перевіркою |
| `scan_and_ingest(dir, pattern)` | Масове сканування каталогів |
| `verify_balance_multi_currency(txns)` | Перевірка балансу за валютою |
| `to_hledger(txns, account)` | Експорт у формат hledger |
| `to_beancount(txns, account)` | Експорт у формат beancount |

### Класи даних

| Клас | Призначення |
|---|---|
| `Deduplicator` | Виявлення дублікатів транзакцій |
| `DeduplicationResult` | Результат з унікальними, точними та ймовірними збігами |
| `InputValidator` | Валідація шляхів та форматів файлів |
| `Transaction` | Нормалізований запис транзакції |
| `FileResult` | Результат паралельного аналізу |
| `ZipXMLSource` | Обгортка запису ZIP |
| `IngestResult` | Результат гібридного pipeline з перевіркою |
| `VerificationResult` | Результат перевірки балансу |
| `Categorizer` | Категоризація транзакцій за допомогою LLM |
| `AccountMapper` | Правила маппінгу рахунків на основі regex |

### Винятки

| Виняток | Коли виникає |
|---|---|
| `ParserError` | Помилки аналізу |
| `ExportError` | Помилки експорту (CSV/JSON/Excel) |
| `ValidationError` | Помилки валідації вхідних даних |
| `ZipSecurityError` | Помилки перевірки безпеки ZIP |
