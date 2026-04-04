---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Безопасность парсера банковских выписок"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Парсер банковских выписок. Все права защищены."
date: "Apr 01, 2026"
description: "Функции безопасности анализатора банковских выписок: защита XXE, защита от бомб ZIP, редактирование личных данных, безопасность цепочки поставок, детерминированный вывод и подписанные сборки."
download: ""
format-detection: "telephone=no"
hreflang: "ru"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/ru/securite/index.html"
image_alt: "Логотип анализатора банковских выписок, расширяющий возможности вашего финансового анализа с помощью простого извлечения данных"
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "безопасность банковских выписок, Python для редактирования PII, защита XXE, защита от ZIP-бомбы, безопасность цепочки поставок SBOM, детерминированный анализ, безопасность финансовых данных"
language: "ru-RU"
layout: "about"
locale: "ru_RU"
logo_alt: "Логотип анализатора банковских выписок, расширяющий возможности вашего финансового анализа с помощью простого извлечения данных"
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Безопасность"
permalink: "https://bankstatementparser.com/ru/securite/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Как мы защищаем ваши финансовые данные"
tags: "безопасность,pii,xxe,sbom,цепочка поставок,детерминистический"
theme_color: "rgb(73, 214, 251)"
title: "Безопасность парсера банковских выписок: защита данных и цепочка поставок"
url: "https://bankstatementparser.com/ru/securite/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/ru/securite/rss.xml"
category: "Программное обеспечение для финансов, библиотека Python, обработка данных"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Функции безопасности анализатора банковских выписок: защита XXE, защита от бомб ZIP, редактирование личных данных, безопасность цепочки поставок, детерминированный вывод и подписанные сборки."
item_guid: "https://bankstatementparser.com/ru/securite/rss.xml"
item_link: "https://bankstatementparser.com/ru/securite/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Безопасность парсера банковских выписок: защита данных и цепочка поставок"
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
apple-mobile-web-app-title: "Безопасность парсера банковских выписок: защита данных и цепочка поставок"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Функции безопасности анализатора банковских выписок: защита XXE, защита от бомб ZIP, редактирование личных данных, безопасность цепочки поставок, детерминированный вывод и подписанные сборки."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Логотип анализатора банковских выписок, расширяющий возможности вашего финансового анализа с помощью простого извлечения данных"
twitter_site: "@wwdseb"
twitter_title: "Безопасность парсера банковских выписок: защита данных и цепочка поставок"
twitter_url: "https://bankstatementparser.com/ru/securite/index.html"

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

**TL;DR:** Bank Statement Parser не выполняет никаких сетевых вызовов, по умолчанию редактирует PII, усиливает синтаксический анализ XML от атак XXE и поставляется с зависимостями с хеш-блокировкой SHA-256 и SBOM CycloneDX.

## Безопасность по задумке

Парсер банковских выписок создан для обработки конфиденциальных финансовых данных. В каждом проектном решении приоритет отдается безопасности, конфиденциальности и возможности аудита.

## Нулевой доступ к сети

Вся обработка происходит локально в вашей среде выполнения. Библиотека не выполняет вызовов API, не использует облачных подключений и не собирает данные телеметрии. XML-парсеры явно настроены с помощью`no_network=True`, `resolve_entities=False`, и`load_dtd=False`для предотвращения любого исходящего доступа.

## Редактирование личных данных

Личная информация (имена, номера IBAN, почтовые адреса) автоматически редактируется в режиме вывода CLI и потоковой передачи. Это включено по умолчанию.

- **CLI**: чувствительные поля отображаются как`***REDACTED***`
- **Трансляция**:`parse_streaming(redact_pii=True)`(по умолчанию)
- **Экспорт**: CSV/JSON/Excel сохраняет полные данные для последующей обработки.
- **Принять**: используйте`--show-pii`или`redact_pii=False`когда вам нужен неотредактированный результат

## Безопасность XML (защита XXE)

Все виды использования синтаксического анализа XML`lxml`с усиленными настройками:

- `resolve_entities=False`-- предотвращает атаки расширения сущности XML
-`no_network=True`-- блокирует весь исходящий доступ к сети от парсера
-`load_dtd=False`-- предотвращает атаки на основе DTD
— Удаление пространства имен перед обработкой — безопасно обрабатывает любой вариант CAMT.053.

## Безопасность ZIP-архива

`iter_secure_xml_entries()`проверяет каждого члена ZIP перед извлечением:

- **Ограничение размера записи**: 10 МБ на каждую запись (настраивается).
- **Ограничение общего размера**: всего 50 МБ без сжатия (настраивается).
- **Предельная степень сжатия**: по умолчанию 100:1 – обнаруживает ZIP-бомбы.
- **Отклонение зашифрованной записи**: зашифрованные записи пропускаются с предупреждением.
- **Запись на диск не выполняется**: байты XML передаются непосредственно в анализатор через`from_bytes()`

## Предотвращение обхода пути

Проверка входных данных блокирует опасные пути к файлам:

- Нулевые байты, шаблоны обхода каталогов (`../`), а символические ссылки отклоняются
- Проверка расширения файла на соответствие ожидаемым форматам.
- Ограничения на размер файла (по умолчанию 100 МБ, настраивается)

## Детерминированный вывод

Учитывая один и тот же входной файл, синтаксический анализатор при каждом запуске выдает байтовые выходные данные. Никакой случайности, никакого модельного вывода, никакой эвристической выборки. Это критично для:

- **Воспроизводимость аудита**: дважды запустите один и тот же файл и сравните выходные данные.
- **Соответствие нормативным требованиям**: демонстрация последовательной обработки.
- **Проверка CI**: 467 тестов обеспечивают детерминизм со 100 % охватом ветвей.

## Безопасность цепочки поставок

- **Зависимости с хеш-блокировкой SHA-256**: каждый пакет в`poetry.lock`проверил хеши файлов
- **CycloneDX SBOM**: каждый выпуск включает в себя спецификацию программного обеспечения.
- **Происхождение сборки GitHub**: аттестация связывает каждый артефакт с исходной фиксацией.
- **Подписанные коммиты**: все коммиты подписаны по SSH и проверены в CI.
- **Проверка зависимостей**:`scripts/verify_locked_hashes.py`проверяет все хеши локально

## Проверить локально

```bash
python -m pytest                          # 467 tests, 100% branch coverage
python scripts/verify_locked_hashes.py    # SHA-256 hash verification
git log --show-signature -1               # Verify commit signature
```
