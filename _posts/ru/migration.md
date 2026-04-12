---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Руководство по переходу на ISO 20022"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Парсер банковских выписок. Все права защищены."
date: "Apr 11, 2026"
description: "Практическое руководство по срокам перехода на SWIFT ISO 20022 (2026–2028 гг.), переходу с MT940 на CAMT.053, а также по тому, как анализатор банковских выписок помогает командам казначейства мигрировать."
download: ""
format-detection: "telephone=no"
hreflang: "ru"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/ru/migration/index.html"
image_alt: "Логотип анализатора банковских выписок, расширяющий возможности вашего финансового анализа с помощью простого извлечения данных"
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "Миграция ISO 20022, MT940 на CAMT.053, крайний срок SWIFT 2027 г., прекращение использования MT940 2028 г., Python миграции банковских выписок, анализатор CAMT.053, временная шкала ISO 20022"
language: "ru-RU"
layout: "about"
locale: "ru_RU"
logo_alt: "Логотип анализатора банковских выписок, расширяющий возможности вашего финансового анализа с помощью простого извлечения данных"
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Руководство по переходу на ISO 20022"
permalink: "https://bankstatementparser.com/ru/migration/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Переход SWIFT MT на ISO 20022"
tags: "iso20022, миграция, mt940, camt053, Swift, временная шкала"
theme_color: "rgb(73, 214, 251)"
title: "Руководство по переходу на ISO 20022: переход с MT940 на CAMT.053"
url: "https://bankstatementparser.com/ru/migration/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/ru/migration/rss.xml"
category: "Программное обеспечение для финансов, библиотека Python, обработка данных"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Практическое руководство по срокам перехода на SWIFT ISO 20022 (2026–2028 гг.), переходу с MT940 на CAMT.053, а также по тому, как анализатор банковских выписок помогает командам казначейства мигрировать."
item_guid: "https://bankstatementparser.com/ru/migration/rss.xml"
item_link: "https://bankstatementparser.com/ru/migration/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Руководство по переходу на ISO 20022: переход с MT940 на CAMT.053"
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
apple-mobile-web-app-title: "Руководство по переходу на ISO 20022: переход с MT940 на CAMT.053"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Практическое руководство по срокам перехода на SWIFT ISO 20022 (2026–2028 гг.), переходу с MT940 на CAMT.053, а также по тому, как анализатор банковских выписок помогает командам казначейства мигрировать."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Логотип анализатора банковских выписок, расширяющий возможности вашего финансового анализа с помощью простого извлечения данных"
twitter_site: "@wwdseb"
twitter_title: "Руководство по переходу на ISO 20022: переход с MT940 на CAMT.053"
twitter_url: "https://bankstatementparser.com/ru/migration/index.html"

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

**Кратко:** SWIFT прекратит поддержку MT940 к ноябрю 2028 года. Bank Statement Parser работает и с MT940, и с CAMT.053 через единый API. Ваш pipeline разбора будет работать и во время перехода, и после него.

## Почему эта миграция важна

SWIFT отказывается от устаревших форматов сообщений MT в пользу более расширенного стандарта ISO 20022. Для казначейских и финансовых команд это означает, что ваши pipeline обработки банковских выписок должны перейти с MT940 на CAMT.053 до наступления жёстких сроков.

## График миграции SWIFT

| Дата | Веха | Вл��яние |
|---|---|---|
| **Ноябрь 2025** | Завершение сосуществования MT-MX для трансграничных платежей | Сообщения PACS теперь только в ISO 20022 |
| **Ноябрь 2026** | Структурированные/гибридные адреса обязательны; мультиинструкционные MT101 отклоняются; Фаза 1 управления делами | Форматы адресов должны соответствовать; некоторые MT-сообщения будут отклонены |
| **Конец 2026** | Начало подписки на получение CAMT.052/.053/.054 | Финансовые учреждения могут начать получать нативные ISO-выписки |
| **Ноябрь 2027** | Все финансовые учреждения должны принимать CAMT.053 нативно | SWIFT прекращает конвертацию MT в ISO; ваши системы должны разбирать CAMT напрямую |
| **Ноябрь 2028** | Полное прекращение MT940/MT942/MT950/MT900/MT910 | Устаревшие форматы выписок более не доступны; CAMT.052/.053/.054 — единственный вариант |

## Что меняется в вашем коде

### Раньше: только MT940

```python
from bankstatementparser import Mt940Parser

parser = Mt940Parser("statement.mt940")
df = parser.parse()
```

### Теперь: оба формата с автоопределением

```python
from bankstatementparser import create_parser, detect_statement_format

fmt = detect_statement_format("statement.xml")  # or .mt940
parser = create_parser("statement.xml", fmt)
df = parser.parse()  # Same DataFrame schema regardless of format
```

Функция `detect_statement_format()` определяет, является ли файл MT940, CAMT.053, PAIN.001 или другим поддерживаемым форматом. Функция `create_parser()` возвращает нужный парсер. Ваш последующий код работает одинаково независимо от исходного формата.

## CAMT.053 и MT940: ключевые различия

| Характеристика | MT940 | CAMT.053 |
|---|---|---|
| Полнота данных | Ограниченные поля | В 3–5 раз больше данных на транзакцию |
| Набор символов | Ограниченный (кодировка SWIFT) | Полный Unicode |
| Структура | Плоский текст с тегами | XML с пространствами имён |
| Отчётность по балансам | Только начальный/конечный | Несколько типов балансов |
| Ссылки | Одно поле ссылки | Несколько типов ссылок |
| Валюты | Базовая поддержка | Полная мультивалютность с обменными курсами |

## Как помогает Bank Statement Parser

- **Единый API**: разбор MT940, CAMT.053 и PDF-выписок с одним workflow, формирующим единообразный DataFrame.
- **Автоопределение**: не нужно заранее знать формат. `detect_statement_format()` определяет его автоматически.
- **Гибридный PDF-pipeline**: банки, предоставляющие только PDF-выписки в период перехода, обрабатываются через `smart_ingest()` с автоматической проверкой баланса.
- **Независимость от пространств имён**: работает с любым вариантом CAMT.053 (001.02, 001.04 или обёртки банков) без настройки.
- **Мультивалютная проверка**: `verify_balance_multi_currency()` проверяет Золотое правило по каждой группе валют — важно для мультивалютных CAMT-выписок.
- **Streaming**: обработка больших CAMT-файлов (50 МБ+, 50 000+ транзакций) с ограниченной памятью.
- **Экспорт в бухгалтерию**: прямой экспорт в журналы hledger или beancount для казначейского учёта.
- **Тестирование миграции**: параллельный запуск обоих парсеров на одном диапазоне дат для проверки согласованности результатов перед переключением.

## Начало работы

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

Для PDF-выписок от банков, ещё не предоставляющих структурированный CAMT-экспорт:

```python
from bankstatementparser.hybrid import smart_ingest

result = smart_ingest("statement.pdf")
assert result.verification.status == "VERIFIED"
```

[Читать полную документацию](/getting-started/index.html)

[Сравнить с альтернативами ❯](/comparison/index.html) | [Смотрите реальные сценарии использ��вания ❯](/use-cases/index.html)
