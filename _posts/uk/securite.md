---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Безпека аналізатора банківської виписки"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Парсер банківських виписок. Всі права захищені."
date: "Apr 01, 2026"
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

**TL;DR:** Парсер банківських виписок не здійснює мережевих викликів, редагує ідентифікаційну інформацію за замовчуванням, посилює синтаксичний аналіз XML проти атак XXE та постачається з хеш-блокованими залежностями SHA-256 і CycloneDX SBOM.

## Безпека за проектом

Парсер банківських виписок створено для обробки конфіденційних фінансових даних. Кожне дизайнерське рішення надає пріоритет безпеці, конфіденційності та можливості перевірки.

## Нульовий доступ до мережі

Уся обробка відбувається локально у вашому середовищі виконання. Бібліотека не здійснює викликів API, не з’єднується з хмарою та не збирає дані телеметрії. Синтаксичні аналізатори XML явно налаштовані за допомогою`no_network=True`, `resolve_entities=False`, і`load_dtd=False`щоб запобігти будь-якому вихідному доступу.

## Редакція ідентифікаційної інформації

Особиста інформація (імена, номери IBAN, поштові адреси) автоматично редагується в режимі виведення CLI та потокового режиму. Це ввімкнено за умовчанням.

- **CLI**: конфіденційні поля відображаються як`***REDACTED***`
- **Потокове передавання**:`parse_streaming(redact_pii=True)`(за умовчанням)
- **Експорт**: CSV/JSON/Excel зберігають повні дані для подальшої обробки
- **Увімкнути**: використовувати`--show-pii`або`redact_pii=False`коли вам потрібен невідредагований вихід

## Безпека XML (захист XXE)

Усі випадки аналізу XML`lxml`з посиленими налаштуваннями:

- `resolve_entities=False`-- запобігає атакам розширення об’єктів XML
-`no_network=True`-- блокує весь вихідний доступ до мережі від аналізатора
-`load_dtd=False`-- запобігає атакам на основі DTD
— Видалення простору імен перед обробкою — безпечно обробляє будь-який варіант CAMT.053

## Безпека архіву ZIP

`iter_secure_xml_entries()`перевіряє кожен член ZIP перед вилученням:

- **Обмеження розміру запису**: 10 МБ на запис (налаштовується)
- **Обмеження загального розміру**: загальна 50 МБ без стиснення (налаштовується)
- **Обмеження коефіцієнта стиснення**: 100:1 за замовчуванням -- виявляє бомби ZIP
- **Відхилення зашифрованого запису**: зашифровані записи пропускаються з попередженням
- **Немає записів на диск**: байти XML передаються безпосередньо до аналізатора через`from_bytes()`

## Запобігання проходженню шляху

Перевірка введених даних блокує небезпечні шляхи до файлів:

- Нульові байти, шаблони проходження каталогу (`../`), а символічні посилання відхиляються
— Перевірка розширення файлу щодо очікуваних форматів
- Обмеження розміру файлу (100 МБ за замовчуванням, налаштовується)

## Детермінований вихід

Враховуючи той самий вхідний файл, синтаксичний аналізатор видає байтно-ідентичний вихід кожного разу. Без випадковості, без моделювання, без евристичної вибірки. Це критично для:

- **Відтворюваність аудиту**: запустіть один і той самий файл двічі та виведіть різницю в результатах
- **Відповідність нормативним вимогам**: продемонструйте послідовну обробку
- **Перевірка CI**: 467 тестів забезпечують детермінізм зі 100% охопленням філій

## Безпека ланцюга поставок

- **Залежності з хеш-блокуванням SHA-256**: кожен пакет у`poetry.lock`має перевірені хеші файлів
- **CycloneDX SBOM**: кожен випуск містить опис матеріалів програмного забезпечення
- **Походження збірки GitHub**: атестація пов’язує кожен артефакт із його вихідним комітом.
- **Підписані коміти**: усі коміти підписані SSH і перевірені в CI
- **Перевірка залежності**:`scripts/verify_locked_hashes.py`перевіряє всі хеші локально

## Перевірити локально

```bash
python -m pytest                          # 467 tests, 100% branch coverage
python scripts/verify_locked_hashes.py    # SHA-256 hash verification
git log --show-signature -1               # Verify commit signature
```
