---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Журнал змін аналізатора банківської виписки"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Парсер банківських виписок. Всі права захищені."
date: "Apr 01, 2026"
description: "Історія випусків і журнал змін для аналізатора банківських виписок. Відстежуйте нові функції, покращення та виправлення помилок у всіх версіях."
download: ""
format-detection: "telephone=no"
hreflang: "uk"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/uk/journal-des-modifications/index.html"
image_alt: "Логотип аналізатора банківських виписок, розширте можливості вашого фінансового аналізу за допомогою безперебійного вилучення даних"
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "журнал змін парсера банківської виписки, примітки до випуску, історія версій, оновлення"
language: "uk-UA"
layout: "about"
locale: "uk_UA"
logo_alt: "Логотип аналізатора банківських виписок, розширте можливості вашого фінансового аналізу за допомогою безперебійного вилучення даних"
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Журнал змін"
permalink: "https://bankstatementparser.com/uk/journal-des-modifications/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Історія випусків і що нового"
tags: "журнал змін, випуски, оновлення, версії, оголошення, блог"
theme_color: "rgb(73, 214, 251)"
title: "Журнал змін аналізатора банківської виписки"
url: "https://bankstatementparser.com/uk/journal-des-modifications/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/uk/journal-des-modifications/rss.xml"
category: "Фінансове програмне забезпечення, бібліотека Python, обробка даних"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Історія випусків і журнал змін для аналізатора банківських виписок. Відстежуйте нові функції, покращення та виправлення помилок у всіх версіях."
item_guid: "https://bankstatementparser.com/uk/journal-des-modifications/rss.xml"
item_link: "https://bankstatementparser.com/uk/journal-des-modifications/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Журнал змін аналізатора банківської виписки"
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
apple-mobile-web-app-title: "Журнал змін аналізатора банківської виписки"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Історія випусків і журнал змін для аналізатора банківських виписок. Відстежуйте нові функції, покращення та виправлення помилок у всіх версіях."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Логотип аналізатора банківських виписок, розширте можливості вашого фінансового аналізу за допомогою безперебійного вилучення даних"
twitter_site: "@wwdseb"
twitter_title: "Журнал змін аналізатора банківської виписки"
twitter_url: "https://bankstatementparser.com/uk/journal-des-modifications/index.html"

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

Слідкуйте за розвитком аналізатора банківських виписок. Підпишіться через [RSS](/changelog/rss.xml) або перегляньте [репозиторій GitHub](https://github.com/sebastienrousseau/bankstatementparser) для повідомлень про випуск.

## v0.0.4 — 2026-03-15 (Остання версія)

— Додано паралельний аналіз файлів за допомогою`parse_files_parallel()`за допомогою ProcessPoolExecutor.
— Додано справжнє потокове передавання для великих файлів PAIN.001 (50 МБ+) з обмеженою пам’яттю.
— Оптимізація продуктивності: пропускна спроможність CAMT тепер перевищує 27 000 tx/s, PAIN.001 перевищує 52 000 tx/s.
- Додано`Deduplicator`клас для виявлення точних дублікатів і підозрюваних збігів з балами достовірності.
- Додано`from_string()`і`from_bytes()`методи аналізу в пам'яті без дискового введення-виведення.
- Додано`iter_secure_xml_entries()`для безпечної обробки ZIP-архіву.
- Розширений CI із застосуванням порогового значення продуктивності.

## v0.0.3 — 2025-11-20

— Додано підтримку парсерів CSV, OFX, QFX і MT940.
— Додано автоматичне визначення формату за допомогою`detect_statement_format()`і`create_parser()`.
— Додано редагування ідентифікаційної інформації (увімкнено за замовчуванням у CLI та потоковому режимі).
— Додано помічники експорту для CSV, JSON і Excel.
— Додано додаткову підтримку Polars DataFrame.
— Розширено набір тестів до 467 тестів із 100% покриттям філій.

## v0.0.2 — 2025-06-10

— Додано аналізатор PAIN.001 (`Pain001Parser`) для файлів ініціації кредитного переказу ISO 20022.
— Додано інтерфейс CLI (`python -m bankstatementparser.cli`).
— Додано потоковий режим з`parse_streaming()`.
— Додано перевірку введення та обмеження розміру файлу.

## v0.0.1 — 2025-01-15

- Початковий випуск.
- аналізатор CAMT.053 (`CamtParser`) для виписок між банками та клієнтами згідно з ISO 20022.
- Вивід pandas DataFrame.
— Базове посилення безпеки XML (захист XXE, no_network).

Переглянути повну історію комітів на [GitHub](https://github.com/sebastienrousseau/bankstatementparser/commits/main).

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Програмне забезпечення",
  "name": "Аналізатор банківської виписки",
  "applicationCategory": "Програма розробника",
  "operatingSystem": "Кросплатформенність",
  "softwareVersion": "0.0.4",
  "datePublished": "2026-03-15",
  "releaseNotes": "Додано паралельний аналіз файлів, справжнє потокове передавання для PAIN.001, оптимізацію продуктивності (27K+ tx/s CAMT, 52K+ tx/s PAIN.001), клас дедуплікатора, синтаксичний аналіз у пам’яті, безпечну обробку ZIP.",
  "Url-адреса завантаження": "https://pypi.org/project/bankstatementparser/",
  "ліцензія": "https://opensource.org/licenses/Apache-2.0",
  "автор": {
    "@type": "Особа",
    "name": "Себастьян Руссо"
  }
}
</script>
