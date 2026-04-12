---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Белое здание с черными окнами"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/daniele-franchi-Vl6YuVBLEys.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Парсер банковских выписок. Все права защищены."
date: "Apr 11, 2026"
description: "Начните работу с анализатором банковских выписок для Python: установите, анализируйте файлы CAMT/PAIN.001/CSV/OFX/QFX/MT940 и используйте потоковую передачу или рабочие процессы CLI."
download: ""
format-detection: "telephone=no"
hreflang: "ru"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/ru/premiers-pas/index.html"
image_alt: "Логотип Bank Statement Parser, мощного инструмента Python, предназначенного для быстрой и точной обработки финансовых данных и извлечения аналитической информации."
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "анализатор банковских выписок, начало работы, python, CAMT, PAIN.001, CSV, OFX, QFX, MT940, финансовые данные"
language: "ru-RU"
layout: "start"
locale: "ru_RU"
logo_alt: "Логотип Bank Statement Parser, мощного инструмента Python, предназначенного для быстрой и точной обработки финансовых данных и извлечения аналитической информации."
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Начиная"
permalink: "https://bankstatementparser.com/ru/premiers-pas/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Начните создавать безопасные приложения с помощью анализатора банковских выписок"
tags: "банк,заявление,парсер,python,camt,pain001,csv,ofx,qfx,mt940,потоковая передача,cli"
theme_color: "rgb(73, 214, 251)"
title: "Парсер банковских выписок: Руководство по установке и использованию"
url: "https://bankstatementparser.com/ru/premiers-pas/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/ru/premiers-pas/rss.xml"
category: "Программное обеспечение для финансов, библиотека Python, руководство для разработчиков"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Начните работу с анализатором банковских выписок для Python: установите, анализируйте файлы CAMT/PAIN.001/CSV/OFX/QFX/MT940 и используйте потоковую передачу или рабочие процессы CLI."
item_guid: "https://bankstatementparser.com/ru/premiers-pas/rss.xml"
item_link: "https://bankstatementparser.com/ru/premiers-pas/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Парсер банковских выписок: Руководство по установке и использованию"
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
apple-mobile-web-app-title: "Парсер банковских выписок: Руководство по установке и использованию"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Установите и используйте анализатор банковских выписок для анализа файлов CAMT, PAIN.001, CSV, OFX/QFX и MT940 на Python."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Логотип Bank Statement Parser, мощного инструмента Python, предназначенного для быстрой и точной обработки финансовых данных и извлечения аналитической информации."
twitter_site: "@wwdseb"
twitter_title: "Парсер банковских выписок: Руководство по установке и использованию"
twitter_url: "https://bankstatementparser.com/ru/premiers-pas/index.html"

# Humans.txt - The Humans.txt front matter (YAML).

author_website: "https://bankstatementparser.com"
author_twitter: "@wwdseb"
author_location: "London, UK"
thanks: "Спасибо за чтение!"
site_last_updated: "2026-04-01"
site_standards: "HTML5, CSS3, RSS, Atom, JSON, XML, YAML, Markdown, TOML"
site_components: "Shokunin SSG, Shokunin CLI, Shokunin Templates, Shokunin Themes, Kaishi SSG, Kaishi CLI, Kaishi Templates, Kaishi Themes"
site_software: "Shokunin, Rust"

---

## Требования

- Python 3.10–3.14
- Доступ к терминалу (macOS, Linux или WSL)

## Установка

```bash
# Базовая установка (только детерминированные парсеры)
pip install bankstatementparser
```

Дополнительные модули для расширенных возможностей:

```bash
# Text-LLM путь для цифровых PDF (litellm + pypdf)
pip install 'bankstatementparser[hybrid]'

# Более точное извлечение таблиц (добавляет pdfplumber)
pip install 'bankstatementparser[hybrid-plus]'

# Vision-LLM путь для сканированных PDF (добавляет pypdfium2)
pip install 'bankstatementparser[hybrid-vision]'

# Категоризация транзакций на основе LLM
pip install 'bankstatementparser[enrichment]'

# REST API микросервис (FastAPI + uvicorn)
pip install 'bankstatementparser[api]'

# Поддержка Polars DataFrame (опционально)
pip install 'bankstatementparser[polars]'
```

## Быстрый старт

### Автоопределение и разбор любого структурированного формата

```python
from bankstatementparser import create_parser, detect_statement_format

fmt = detect_statement_format("transactions.ofx")
parser = create_parser("transactions.ofx", fmt)
df = parser.parse()  # pandas DataFrame
print(df.head())
```

Работает с файлами `.xml` (CAMT/PAIN.001), `.csv`, `.ofx`, `.qfx`, `.mt940` и `.sta`.

### Разбор CAMT.053

```python
from bankstatementparser import CamtParser

parser = CamtParser("statement.xml")
transactions = parser.parse()
```

### Разбор PAIN.001

```python
from bankstatementparser import Pain001Parser

parser = Pain001Parser("payment.xml")
payments = parser.parse()
```

### Разбор PDF-выписок (гибридный pipeline)

Гибридный pipeline автоматически направляет PDF по оптимальному пути извлечения:

```python
from bankstatementparser.hybrid import smart_ingest

result = smart_ingest("statement.pdf")
print(result.source_method)         # "deterministic" | "llm" | "vision"
print(result.verification.status)   # VERIFIED | DISCREPANCY | FAILED
print(result.transactions)          # List of extracted transactions
```

Каждое извлечение проверяется **Золотым правилом**: `opening + credits − debits == closing`.

## Потоковый разбор больших файлов

Для файлов с тысячами транзакций используйте streaming для ограничения памяти:

```python
parser = CamtParser("large_statement.xml")
for transaction in parser.parse_streaming(redact_pii=True):
    process(transaction)  # Memory stays constant
```

## Разбор в памяти

Разбор из байтов без дискового ввода-вывода — подходит для SFTP и API-сценариев:

```python
xml_bytes = download_from_sftp()
parser = CamtParser.from_bytes(xml_bytes, source_name="daily.xml")
transactions = parser.parse()
```

## Параллельная обработка файлов

Разбор нескольких файлов одновременно:

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

## Массовое сканирование каталогов

Обработка деревьев каталогов с автоматической дедупликацией:

```python
from bankstatementparser.hybrid import scan_and_ingest

batch = scan_and_ingest("statements/2026/", pattern="**/*.pdf")
print(f"Processed: {len(batch.results)} files")
print(f"Unique transactions: {batch.unique_count}")
```

## Дедупликация

Идемпотентные hash транзакций для безопасной инкрементальной загрузки:

```python
from bankstatementparser import CamtParser, Deduplicator

parser = CamtParser("statement.xml")
dedup = Deduplicator()
result = dedup.deduplicate(dedup.from_dataframe(parser.parse()))

print(f"Unique: {len(result.unique_transactions)}")
print(f"Exact duplicates: {len(result.exact_duplicates)}")
print(f"Suspected matches: {len(result.suspected_matches)}")
```

## Категоризация транзакций (обогащение)

Автоматическая категоризация транзакций с помощью LLM:

```python
from bankstatementparser.enrichment import Categorizer

categorizer = Categorizer()
enriched = categorizer.categorize_batch(transactions)
for txn in enriched:
    print(f"{txn.description}: {txn.category}")
```

## Экспорт в бухгалтерию (hledger / beancount)

Экспорт транзакций в форматы plaintext-accounting:

```python
from bankstatementparser.export import to_hledger, to_beancount

journal = to_hledger(transactions, account="Assets:Bank:Checking")
beancount_journal = to_beancount(transactions, account="Assets:Bank:Checking")
```

## Мультивалютная проверка баланса

Независимая проверка баланса по каждой группе валют:

```python
from bankstatementparser.hybrid import verify_balance_multi_currency

results = verify_balance_multi_currency(transactions)
for currency, verification in results.items():
    print(f"{currency}: {verification.status}")
```

## REST API

Развёртывание как микросервис FastAPI:

```bash
# Start the API server
bankstatementparser-api --port 8000

# For container deployments
bankstatementparser-api --host 0.0.0.0 --port 9000
```

Эндпоинты:
- `POST /ingest` -- Разбор файла банковской выписки
- `GET /health` -- Проверка состояния

## Безопасная обработка ZIP

Обработка ZIP-архивов XML со встроенными проверками безопасности (защита от бомб, отклонение зашифрованных записей):

```python
from bankstatementparser import iter_secure_xml_entries, CamtParser

for entry in iter_secure_xml_entries("statements.zip"):
    parser = CamtParser.from_bytes(entry.xml_bytes, source_name=entry.source_name)
    print(f"{entry.source_name}: {len(parser.parse())} transactions")
```

## Экспорт

```python
parser = CamtParser("statement.xml")
parser.export_csv("output.csv")
parser.export_json("output.json")

# Polars (requires bankstatementparser[polars])
polars_df = parser.to_polars()

# Excel
parser.camt_to_excel("output.xlsx")
```

## Использование CLI

```bash
# Разбор структурированных форматов
bankstatementparser --type camt --input statement.xml
bankstatementparser --type pain001 --input payment.xml

# Гибридный PDF-pipeline
bankstatementparser --type ingest --input statement.pdf
bankstatementparser --type ingest --input statement.pdf --output ledger.csv

# Интерактивный режим просмотра
bankstatementparser --type review --input result.json
bankstatementparser --type review --input result.json --output reviewed.json

# Экспорт в CSV с потоковым режимом
bankstatementparser --type camt --input statement.xml --output transactions.csv
bankstatementparser --type camt --input statement.xml --streaming --show-pii
```

Опции CLI:

- `--type {camt,pain001,ingest,review}` -- тип парсера или режим
- `--input <path>` -- входной файл
- `--output <path>` -- файл экспорта (CSV или JSON)
- `--streaming` -- потоковый режим для больших файлов
- `--show-pii` -- показать конфиденциальные поля (по умолчанию замаскированы)
- `--max-size <MB>` -- ограничение размера файла

## Настройка локальной разработки

```bash
git clone https://github.com/sebastienrousseau/bankstatementparser.git
cd bankstatementparser
python3 -m venv .venv && source .venv/bin/activate
pip install poetry && poetry install --with dev
make install-hooks   # pre-commit hook runs `make verify` before every commit
```

Запуск тестов:

```bash
pytest
```

## Справочник API

### Классы парсеров

| Класс | Формат | Импорт |
|---|---|---|
| `CamtParser` | CAMT.053 (ISO 20022) | `from bankstatementparser import CamtParser` |
| `Pain001Parser` | PAIN.001 (ISO 20022) | `from bankstatementparser import Pain001Parser` |
| `CsvStatementParser` | CSV | `from bankstatementparser import CsvStatementParser` |
| `OfxParser` | OFX | `from bankstatementparser import OfxParser` |
| `QfxParser` | QFX | `from bankstatementparser import QfxParser` |
| `Mt940Parser` | MT940 | `from bankstatementparser import Mt940Parser` |
| `smart_ingest()` | PDF (гибридный pipeline) | `from bankstatementparser.hybrid import smart_ingest` |

### Вспомогательные функции

| Функция | Назначение |
|---|---|
| `detect_statement_format(path)` | Автоопределение формата файла |
| `create_parser(path, fmt)` | Создание нужного парсера |
| `parse_files_parallel(paths)` | Параллельный разбор нескольких файлов |
| `iter_secure_xml_entries(zip_path)` | Безопасный перебор записей ZIP |
| `smart_ingest(path)` | Гибридное извлечение из PDF с проверкой |
| `scan_and_ingest(dir, pattern)` | Массовое сканирование каталогов |
| `verify_balance_multi_currency(txns)` | Проверка баланса по валютам |
| `to_hledger(txns, account)` | Экспорт в формат журнала hledger |
| `to_beancount(txns, account)` | Экспорт в формат журнала beancount |

### Классы данных

| Класс | Назначение |
|---|---|
| `Deduplicator` | Обнаружение дублей транзакций |
| `DeduplicationResult` | Результат с уникальными, точными и предполагаемыми совпадениями |
| `InputValidator` | Валидация путей и форматов файлов |
| `Transaction` | Нормализованная запись транзакции |
| `FileResult` | Результат параллельного разбора |
| `ZipXMLSource` | Обёртка для записи ZIP |
| `IngestResult` | Результат гибридного pipeline с проверкой |
| `VerificationResult` | Результат проверки баланса |
| `Categorizer` | Категоризация транзакций на основе LLM |
| `AccountMapper` | Правила маппинга счетов на основе регулярных выражений |

### Исключения

| Исключение | Когда возникает |
|---|---|
| `ParserError` | Ошибки разбора |
| `ExportError` | Ошибки экспорта (CSV/JSON/Excel) |
| `ValidationError` | Ошибки валидации ввода |
| `ZipSecurityError` | Ошибки проверки безопасности ZIP |
