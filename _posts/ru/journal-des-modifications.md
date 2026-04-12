---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Журнал изменений парсера банковских выписок"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Парсер банковских выписок. Все права защищены."
date: "Apr 11, 2026"
description: "История выпусков и журнал изменений для анализатора банковских выписок. Отслеживайте новые функции, улучшения и исправления ошибок во всех версиях."
download: ""
format-detection: "telephone=no"
hreflang: "ru"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/ru/journal-des-modifications/index.html"
image_alt: "Логотип анализатора банковских выписок, расширяющий возможности вашего финансового анализа с помощью простого извлечения данных"
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "журнал изменений парсера банковских выписок, примечания к выпуску, история версий, обновления"
language: "ru-RU"
layout: "about"
locale: "ru_RU"
logo_alt: "Логотип анализатора банковских выписок, расширяющий возможности вашего финансового анализа с помощью простого извлечения данных"
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Журнал изменений"
permalink: "https://bankstatementparser.com/ru/journal-des-modifications/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "История выпусков и что нового"
tags: "журнал изменений,релизы,обновления,версии,объявления,блог"
theme_color: "rgb(73, 214, 251)"
title: "Журнал изменений парсера банковских выписок"
url: "https://bankstatementparser.com/ru/journal-des-modifications/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/ru/journal-des-modifications/rss.xml"
category: "Программное обеспечение для финансов, библиотека Python, обработка данных"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "История выпусков и журнал изменений для анализатора банковских выписок. Отслеживайте новые функции, улучшения и исправления ошибок во всех версиях."
item_guid: "https://bankstatementparser.com/ru/journal-des-modifications/rss.xml"
item_link: "https://bankstatementparser.com/ru/journal-des-modifications/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Журнал изменений парсера банковских выписок"
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
apple-mobile-web-app-title: "Журнал изменений парсера банковских выписок"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "История выпусков и журнал изменений для анализатора банковских выписок. Отслеживайте новые функции, улучшения и исправления ошибок во всех версиях."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Логотип анализатора банковских выписок, расширяющий возможности вашего финансового анализа с помощью простого извлечения данных"
twitter_site: "@wwdseb"
twitter_title: "Журнал изменений парсера банковских выписок"
twitter_url: "https://bankstatementparser.com/ru/journal-des-modifications/index.html"

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

Следите за развитием парсера банковских выписок. Подпишитесь через [RSS](/changelog/rss.xml) или посмотрите [репозиторий GitHub](https://github.com/sebastienrousseau/bankstatementparser) для уведомлений о выпуске.

## v0.0.8 — 2026-04-11 (Latest) — "Full Platform"

- Multi-currency balance verification — `verify_balance_multi_currency()` groups by currency, runs Golden Rule per group.
- hledger + beancount export — `to_hledger()` and `to_beancount()` in `bankstatementparser.export`.
- Bulk directory scanner — `scan_and_ingest()` scans folder trees, deduplicates across batch.
- Account mapping rules — `AccountMapper` with ordered regex rules from JSON config.
- REST API — FastAPI wrapper with `/ingest` and `/health` endpoints (`[api]` extra).

## v0.0.7 — 2026-04-08 — "Universal Vision"

- Direct Ollama bridge (`ollama_direct_completion`) — bypasses LiteLLM long-prompt hang.
- Strip mode (`VisionExtractor.strip_rows=True`) — splits dense pages into overlapping bands for small local models.
- Recommended vision model changed from `llava` to `minicpm-v`.

## v0.0.6 — 2026-04-08 — "Intelligence Layer"

- Dropped Python 3.9 support (now 3.10-3.14).
- Enrichment module (`Categorizer`, `EnrichedTransaction`, `DEFAULT_CATEGORY_SCHEMA`).
- Interactive review mode with `--type review` CLI command.
- Per-row bounding box extraction (`Transaction.source_bbox`).

## v0.0.5 — 2026-04-08 — "Universal Extraction"

- Hybrid PDF pipeline (`smart_ingest()`) with deterministic/text-LLM/vision-LLM routing.
- `LLMExtractor` for digital PDFs via LiteLLM.
- `VisionExtractor` for scanned PDFs via multimodal vision models.
- Golden Rule balance verification (`opening + credits - debits == closing`).
- Idempotent deduplication via `transaction_hash` (MD5 fingerprint).

## v0.0.4 — 15 марта 2026 г. (Последняя версия)

- Добавлен параллельный анализ файлов с помощью`parse_files_parallel()`с помощью ProcessPoolExecutor.
- Добавлена ​​настоящая потоковая передача для больших файлов PAIN.001 (50 МБ и более) с ограниченной памятью.
- Оптимизация производительности: пропускная способность CAMT теперь превышает 27 000 транзакций/с, PAIN.001 превышает 52 000 транзакций/с.
- Добавлен`Deduplicator`класс для обнаружения точных дубликатов и предполагаемых совпадений с оценкой достоверности.
- Добавлен`from_string()`и`from_bytes()`методы анализа в памяти без дискового ввода-вывода.
- Добавлен`iter_secure_xml_entries()`для безопасной обработки ZIP-архивов.
- Расширенный CI с соблюдением пороговых значений производительности.

## v0.0.3 — 20 ноября 2025 г.

- Добавлена ​​поддержка парсеров CSV, OFX, QFX и MT940.
- Добавлено автоопределение формата с`detect_statement_format()`и`create_parser()`.
- Добавлено редактирование личных данных (по умолчанию включено в интерфейсе командной строки и потоковом режиме).
— Добавлены помощники по экспорту для CSV, JSON и Excel.
- Добавлена ​​дополнительная поддержка Polars DataFrame.
- Расширен набор тестов до 718 тестов со 100% покрытием ветвей.

## v0.0.2 — 10.06.2025

- Добавлен парсер PAIN.001 (`Pain001Parser`) для файлов инициации кредитного перевода ISO 20022.
- Добавлен интерфейс CLI (`python -m bankstatementparser.cli`).
- Добавлен потоковый режим с`parse_streaming()`.
— Добавлена ​​проверка ввода и ограничения на размер файла.

## v0.0.1 — 15 января 2025 г.

- Первоначальный выпуск.
- Парсер CAMT.053 (`CamtParser`) для выписок банка клиенту по стандарту ISO 20022.
- вывод данных pandas DataFrame.
— Базовое усиление безопасности XML (защита XXE, no_network).

Полную историю коммитов можно просмотреть на [GitHub](https://github.com/sebastienrousseau/bankstatementparser/commits/main).

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Программное приложение",
  "name": "Парсер банковских выписок",
  "applicationCategory": "DeveloperApplication",
  "operatingSystem": "Кроссплатформенность",
  "версия программного обеспечения": "0.0.4",
  "datePublished": "15 марта 2026 г.",
  "releaseNotes": "Добавлен параллельный анализ файлов, настоящая потоковая передача для PAIN.001, оптимизация производительности (27 000+ транзакций/с CAMT, 52 000+ транзакций/с PAIN.001), класс дедупликатора, анализ в памяти, безопасная обработка ZIP.",
  "downloadUrl": "https://pypi.org/project/bankstatementparser/",
  "лицензия": "https://opensource.org/licenses/Apache-2.0",
  "автор": {
    "@type": "Человек",
    "name": "Себастьян Руссо"
  }
}
</скрипт>
