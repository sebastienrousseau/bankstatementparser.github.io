---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Безпека аналізатора банківської виписки"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Парсер банківських виписок. Всі права захищені."
date: "Apr 11, 2026"
description: "Функції безпеки аналізатора банківських виписок: захист XXE, захист від бомби ZIP, редагування ідентифікаційної інформації, безпека ланцюжка поставок, детермінований вихід і підписані збірки."
download: ""
format-detection: "telephone=no"
hreflang: "uk"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/uk/securite/index.html"
image_alt: "Логотип аналізатора банківських виписок, розширте можливості вашого фінансового аналізу за допомогою безперебійного вилучення даних"
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "безпека банківської виписки, Python редагування ідентифікаційної інформації, захист XXE, захист від бомби ZIP, безпека ланцюга поставок SBOM, детермінований аналіз, безпека фінансових даних"
language: "uk-UA"
layout: "about"
locale: "uk_UA"
logo_alt: "Логотип аналізатора банківських виписок, розширте можливості вашого фінансового аналізу за допомогою безперебійного вилучення даних"
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Безпека"
permalink: "https://bankstatementparser.com/uk/securite/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Як ми захищаємо ваші фінансові дані"
tags: "security,pii,xxe,sbom,supply-chain,deterministic"
theme_color: "rgb(73, 214, 251)"
title: "Безпека аналізатора банківської виписки: захист даних і ланцюг поставок"
url: "https://bankstatementparser.com/uk/securite/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/uk/securite/rss.xml"
category: "Фінансове програмне забезпечення, бібліотека Python, обробка даних"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Функції безпеки аналізатора банківських виписок: захист XXE, захист від бомби ZIP, редагування ідентифікаційної інформації, безпека ланцюжка поставок, детермінований вихід і підписані збірки."
item_guid: "https://bankstatementparser.com/uk/securite/rss.xml"
item_link: "https://bankstatementparser.com/uk/securite/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Безпека аналізатора банківської виписки: захист даних і ланцюг поставок"
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
apple-mobile-web-app-title: "Безпека аналізатора банківської виписки: захист даних і ланцюг поставок"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Функції безпеки аналізатора банківських виписок: захист XXE, захист від бомби ZIP, редагування ідентифікаційної інформації, безпека ланцюжка поставок, детермінований вихід і підписані збірки."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Логотип аналізатора банківських виписок, розширте можливості вашого фінансового аналізу за допомогою безперебійного вилучення даних"
twitter_site: "@wwdseb"
twitter_title: "Безпека аналізатора банківської виписки: захист даних і ланцюг поставок"
twitter_url: "https://bankstatementparser.com/uk/securite/index.html"

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

**Коротко:** Bank Statement Parser обробляє всі дані локально, приховує персональні дані за замовчуванням, захищає XML-аналіз від XXE-атак, запускає LLM локально через Ollama та постачається із SHA-256 hash-блокованими залежностями і CycloneDX SBOM.

## Безпека за дизайном

Bank Statement Parser створений для обробки конфіденційних фінансових даних. Кожне архітектурне рішення ставить безпеку, конфіденційність та перевірюваність на перше місце.

## Нульова залежність від хмари

Уся обробка відбувається локально у вашому середовищі виконання. Детерміністичні парсери не здійснюють жодних мережевих викликів. Гібридний PDF pipeline використовує Ollama для локального LLM-виведення — жодні дані не надсилаються до хмарних API. XML-парсери явно налаштовані з `no_network=True`, `resolve_entities=False` та `load_dtd=False` для запобігання будь-якому вихідному доступу.

## Приховування персональних даних

Персональна інформація (імена, IBAN, поштові адреси) автоматично приховується у CLI та streaming-режимі. Це увімкнено за замовчуванням.

- **CLI**: Конфіденційні поля відображаються як `***REDACTED***`
- **Streaming**: `parse_streaming(redact_pii=True)` (за замовчуванням)
- **Експорт**: CSV/JSON/Excel зберігають повні дані для подальшої обробки
- **Увімкнення**: Використовуйте `--show-pii` або `redact_pii=False`, коли потрібен повний вивід

## Безпека XML (захист від XXE)

Увесь XML-аналіз використовує `lxml` із захищеними налаштуваннями:

- `resolve_entities=False` -- запобігає атакам розширення XML-сутностей
- `no_network=True` -- блокує весь вихідний мережевий доступ парсера
- `load_dtd=False` -- запобігає атакам на основі DTD
- Видалення просторів імен перед обробкою -- безпечно працює з будь-яким варіантом CAMT.053

## Безпека ZIP-архівів

`iter_secure_xml_entries()` перевіряє кожний запис ZIP перед витягуванням:

- **Ліміт розміру запису**: 10 МБ на запис (налаштовується)
- **Ліміт загального розміру**: 50 МБ нестиснутих даних (налаштовується)
- **Обмеження коефіцієнта стиснення**: 100:1 за замовчуванням -- виявляє ZIP-бомби
- **Відхилення зашифрованих записів**: Зашифровані записи пропускаються з попередженням
- **Без записів на диск**: XML-байти передаються напряму до парсера через `from_bytes()`

## Захист від обходу шляхів

Валідація вхідних даних блокує небезпечні шляхи до файлів:

- Нульові байти, шаблони обходу каталогу (`../`) та символічні посилання відхиляються
- Перевірка розширення файлу щодо очікуваних форматів
- Ліміти розміру файлу (100 МБ за замовчуванням, налаштовується)

## Перевірка балансу (Золоте правило)

Кожне PDF-витягування перевіряється рівнянням: `opening balance + credits − debits == closing balance`. Результати позначаються як VERIFIED, DISCREPANCY або FAILED. Розбіжності можна переглянути інтерактивно через `--type review`.

## Детерміністичний результат

Для структурованих форматів (CAMT, PAIN.001, CSV, OFX, QFX, MT940) за умови однакового вхідного файлу парсер щоразу видає побайтово ідентичний результат. Без випадковості, без моделювання, без евристичної вибірки. Це критично для:

- **Відтворюваність аудиту**: Запустіть один файл двічі та порівняйте результати
- **Регуляторний комплаєнс**: Демонстрація стабільної обробки
- **Перевірка в CI**: 718 тестів забезпечують детермінізм зі 100% покриттям гілок

## Безпека ланцюга постачань

- **Залежності із SHA-256 hash-блокуванням**: Кожний пакет у `poetry.lock` має перевірені hash файлів
- **CycloneDX SBOM**: Кожний реліз містить Software Bill of Materials
- **Походження збірки GitHub**: Атестація зв’язує кожний артефакт із його вихідним комітом
- **Підписані коміти**: Усі коміти підписані SSH та перевірені в CI
- **Перевірка залежностей**: `scripts/verify_locked_hashes.py` перевіряє всі hash локально

## Перевірте локально

```bash
python -m pytest                          # 718 tests, 100% branch coverage
python scripts/verify_locked_hashes.py    # SHA-256 hash verification
git log --show-signature -1               # Verify commit signature
```
