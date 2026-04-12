---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Безопасность парсера банковских выписок"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Парсер банковских выписок. Все права защищены."
date: "Apr 11, 2026"
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

**Кратко:** Bank Statement Parser обрабатывает все данные локально, маскирует PII по умолчанию, защищает XML-парсинг от XXE-атак, запускает LLM локально через Ollama и поставляется с SHA-256 hash-lock зависимостей и CycloneDX SBOM.

## Безопасность по задумке

Bank Statement Parser создан для обработки конфиденциальных финансовых данных. Каждое проектное решение ставит на первое место безопасность, конфиденциальность и возможность аудита.

## Нулевая зависимость от облака

Вся обработка происходит локально в вашей среде выполнения. Детерминированные парсеры не совершают сетевых вызовов. Гибридный PDF-pipeline использует Ollama для локального инференса LLM — данные не отправляются в облачные API. XML-парсеры явно настроены с `no_network=True`, `resolve_entities=False` и `load_dtd=False` для предотвращения любого исходящего доступа.

## Маскирование PII

Персональные данные (имена, IBAN, почтовые адреса) автоматически маскируются в выводе CLI и потоковом режиме. Это включено по умолчанию.

- **CLI**: конфиденциальные поля показываются как `***REDACTED***`
- **Streaming**: `parse_streaming(redact_pii=True)` (по умолчанию)
- **Экспорт**: CSV/JSON/Excel сохраняют полные данные для дальнейшей обработки
- **Показать данные**: используйте `--show-pii` или `redact_pii=False`, когда нужен немаскированный вывод

## Безопасность XML (защита от XXE)

Весь XML-парсинг использует `lxml` с усиленными настройками:

- `resolve_entities=False` -- предотвращает атаки расширения XML-сущностей
- `no_network=True` -- блокирует весь исходящий сетевой доступ из парсера
- `load_dtd=False` -- предотвращает DTD-атаки
- Удаление пространств имён перед обработкой -- безопасная работа с любым вариантом CAMT.053

## Безопасность ZIP-архивов

`iter_secure_xml_entries()` проверяет каждую запись ZIP перед извлечением:

- **Лимит размера записи**: 10 МБ на запись (настраивается)
- **Лимит общего размера**: 50 МБ несжатого объёма (настраивается)
- **Лимит степени сжатия**: 100:1 по умолчанию -- обнаруживает ZIP-бомбы
- **Отклонение зашифрованных записей**: зашифрованные записи пропускаются с предупреждением
- **Без записи на диск**: XML-байты передаются напрямую в парсер через `from_bytes()`

## Предотвращение обхода путей

Валидация ввода блокирует опасные пути к файлам:

- Нулевые байты, шаблоны обхода каталогов (`../`) и символические ссылки отклоняются
- Валидация расширения файла по ожидаемым форматам
- Ограничение размера файла (100 МБ по умолчанию, настраивается)

## Проверка баланса (Золотое правило)

Каждое извлечение из PDF проверяется уравнением: `opening balance + credits − debits == closing balance`. Результаты размечаются как VERIFIED, DISCREPANCY или FAILED. Расхождения можно просмотреть в интерактивном режиме через `--type review`.

## Детерминированный вывод

Для структурированных форматов (CAMT, PAIN.001, CSV, OFX, QFX, MT940) при одинаковом входном файле парсер каждый раз выдаёт побайтово идентичный результат. Без случайности, без инференса модели, без эвристической выборки. Это критично для:

- **Воспроизводимость аудита**: запустите один файл дважды и сравните результат
- **Соответствие нормативам**: демонстрация стабильной обработки
- **Проверка в CI**: 718 тестов обеспечивают детерминизм со 100% покрытием ветвей

## Безопасность цепочки поставок

- **SHA-256 hash-lock зависимостей**: каждый пакет в `poetry.lock` имеет проверенные hash файлов
- **CycloneDX SBOM**: каждый релиз включает спецификацию программного обеспечения
- **Аттестация происхождения сборки GitHub**: связывает каждый артефакт с исходным коммитом
- **Подписанные коммиты**: все коммиты подписаны SSH и проверены в CI
- **Проверка зависимостей**: `scripts/verify_locked_hashes.py` проверяет все hash локально

## Проверьте локально

```bash
python -m pytest                          # 718 tests, 100% branch coverage
python scripts/verify_locked_hashes.py    # SHA-256 hash verification
git log --show-signature -1               # Verify commit signature
```
