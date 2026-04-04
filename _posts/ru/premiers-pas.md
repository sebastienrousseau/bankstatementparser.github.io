---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Белое здание с черными окнами"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/daniele-franchi-Vl6YuVBLEys.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Парсер банковских выписок. Все права защищены."
date: "Apr 01, 2026"
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

- Питон 3.9–3.14
- Терминальный доступ (macOS, Linux или WSL)

## Установить

```bash
pip install bankstatementparser
```

Для поддержки Polars DataFrame:

```bash
pip install bankstatementparser[polars]
```

## Быстрый старт

### Автоматическое обнаружение и анализ любого формата

```python
from bankstatementparser import create_parser, detect_statement_format

fmt = detect_statement_format("transactions.ofx")
parser = create_parser("transactions.ofx", fmt)
df = parser.parse()  # pandas DataFrame
print(df.head())
```

Это работает с`.xml`(CAMT/PAIN.001),`.csv`, `.ofx`, `.qfx`, `.mt940`, и`.sta`файлы.

### Анализ CAMT.053

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

## Потоковая передача больших файлов

Для файлов с тысячами транзакций используйте потоковую передачу, чтобы ограничить память:

```python
parser = CamtParser("large_statement.xml")
for transaction in parser.parse_streaming(redact_pii=True):
    process(transaction)  # Memory stays constant
```

## Парсинг в памяти

Анализ байтов без дискового ввода-вывода — полезно для рабочих процессов SFTP или API:

```python
xml_bytes = download_from_sftp()
parser = CamtParser.from_bytes(xml_bytes, source_name="daily.xml")
transactions = parser.parse()
```

## Параллельная обработка файлов

Парсить несколько файлов одновременно:

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

## Дедупликация

Обнаружение точных дубликатов и предполагаемых совпадений с помощью оценок достоверности:

```python
from bankstatementparser import CamtParser, Deduplicator

parser = CamtParser("statement.xml")
dedup = Deduplicator()
result = dedup.deduplicate(dedup.from_dataframe(parser.parse()))

print(f"Unique: {len(result.unique_transactions)}")
print(f"Exact duplicates: {len(result.exact_duplicates)}")
print(f"Suspected matches: {len(result.suspected_matches)}")
```

## Безопасная обработка ZIP

Обработка сжатых XML-файлов с помощью встроенных проверок безопасности (защита от бомб, отклонение зашифрованного ввода):

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
```

## Использование CLI

```bash
# Parse and display
python -m bankstatementparser.cli --type camt --input statement.xml

# Export to CSV
python -m bankstatementparser.cli --type camt --input statement.xml --output transactions.csv

# Stream with PII visible
python -m bankstatementparser.cli --type camt --input statement.xml --streaming --show-pii
```

Опции CLI:

- `--type {camt,pain001}`-- тип парсера
-`--input <path>`-- входной файл
-`--output <csv_path>`-- экспорт в CSV
-`--streaming`-- потоковая передача больших файлов
-`--show-pii`-- показать чувствительные поля (по умолчанию отредактированы)
-`--max-size <MB>`-- ограничение размера файла

## Настройка локальной разработки

```bash
git clone https://github.com/sebastienrousseau/bankstatementparser.git
cd bankstatementparser
python3 -m venv .venv && source .venv/bin/activate
pip install poetry && poetry install --with dev
```

Запустите набор тестов:

```bash
pytest
```

## Справочник по API

### Классы парсера

| Сорт | Формат | Импорт |
|---|---|---|
| `CamtParser` | КАМТ.053 (ИСО 20022) | `from bankstatementparser import CamtParser` |
| `Pain001Parser` | ПЕЙН.001 (ИСО 20022) | `from bankstatementparser import Pain001Parser` |
| `CsvStatementParser` | CSV-файл | `from bankstatementparser import CsvStatementParser` |
| `OfxParser` | ОФКС | `from bankstatementparser import OfxParser` |
| `QfxParser` | QFX | `from bankstatementparser import QfxParser` |
| `Mt940Parser` | МТ940 | `from bankstatementparser import Mt940Parser` |

### Служебные функции

| Функция | Цель |
|---|---|
| `detect_statement_format(path)` | Автоматическое определение формата файла |
| `create_parser(path, fmt)` | Создайте соответствующий парсер |
| `parse_files_parallel(paths)` | Парсить несколько файлов одновременно |
| `iter_secure_xml_entries(zip_path)` | Безопасное повторение записей ZIP |

### Классы данных

| Сорт | Цель |
|---|---|
| `Deduplicator` | Обнаружение повторяющихся транзакций |
| `DeduplicationResult` | Результат с уникальными, точными и предполагаемыми совпадениями |
| `InputValidator` | Проверка путей и форматов файлов |
| `Transaction` | Нормализованная запись транзакции |
| `FileResult` | Результат параллельного анализа |
| `ZipXMLSource` | Оболочка члена ZIP |

### Исключения

| Исключение | Когда поднят |
|---|---|
| `ParserError` | Сбои разбора |
| `ExportError` | Ошибки экспорта (CSV/JSON/Excel) |
| `ValidationError` | Ошибки проверки ввода |
| `ZipSecurityError` | Сбои проверки безопасности ZIP |
