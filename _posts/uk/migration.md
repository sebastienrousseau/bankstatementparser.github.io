---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Посібник з переходу на ISO 20022"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/corporate-finance.webp"
cdn: "https://cloudcdn.pro"
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Парсер банківських виписок. Всі права захищені."
date: "Apr 01, 2026"
description: "Практичний посібник із графіка переходу на SWIFT ISO 20022 (2026–2028), переходу MT940 на CAMT.053 і того, як Parser банківських виписок допомагає командам казначейства перейти."
download: ""
format-detection: "telephone=no"
hreflang: "uk"
icon: "https://cloudcdn.pro/bankstatementparser/images/favicon.ico"
id: "https://bankstatementparser.com/uk/migration/index.html"
image_alt: "Логотип аналізатора банківських виписок, розширте можливості вашого фінансового аналізу за допомогою безперебійного вилучення даних"
image_height: "630"
image_width: "1200"
image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
keywords: "Перехід на ISO 20022, MT940 на CAMT.053, кінцевий термін SWIFT 2027, припинення використання MT940 2028, Python міграції банківської виписки, синтаксичний аналізатор CAMT.053, хронологія ISO 20022"
language: "uk-UA"
layout: "about"
locale: "uk_UA"
logo_alt: "Логотип аналізатора банківських виписок, розширте можливості вашого фінансового аналізу за допомогою безперебійного вилучення даних"
logo_height: "44"
logo_width: "44"
logo: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Посібник з переходу на ISO 20022"
permalink: "https://bankstatementparser.com/uk/migration/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Перейдіть у SWIFT MT до ISO 20022"
tags: "iso20022,міграція,mt940,camt053,swift,хронологія"
theme_color: "rgb(73, 214, 251)"
title: "Посібник із переходу на ISO 20022: перехід від MT940 до CAMT.053"
url: "https://bankstatementparser.com/uk/migration/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/uk/migration/rss.xml"
category: "Фінансове програмне забезпечення, бібліотека Python, обробка даних"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Практичний посібник із графіка переходу на SWIFT ISO 20022 (2026–2028), переходу MT940 на CAMT.053 і того, як Parser банківських виписок допомагає командам казначейства перейти."
item_guid: "https://bankstatementparser.com/uk/migration/rss.xml"
item_link: "https://bankstatementparser.com/uk/migration/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Посібник із переходу на ISO 20022: перехід від MT940 до CAMT.053"
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
apple-mobile-web-app-title: "Посібник із переходу на ISO 20022: перехід від MT940 до CAMT.053"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Практичний посібник із графіка переходу на SWIFT ISO 20022 (2026–2028), переходу MT940 на CAMT.053 і того, як Parser банківських виписок допомагає командам казначейства перейти."
twitter_image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
twitter_image_alt: "Логотип аналізатора банківських виписок, розширте можливості вашого фінансового аналізу за допомогою безперебійного вилучення даних"
twitter_site: "@wwdseb"
twitter_title: "Посібник із переходу на ISO 20022: перехід від MT940 до CAMT.053"
twitter_url: "https://bankstatementparser.com/uk/migration/index.html"

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

**TL;DR:** SWIFT припинить використання MT940 до листопада 2028 року. Парсер банківських виписок обробляє як MT940, так і CAMT.053 за допомогою єдиного API, тож ваш конвеєр синтаксичного аналізу працює під час переходу та після нього.

## Чому ця міграція важлива

SWIFT припиняє використання застарілих форматів повідомлень MT на користь розширеного стандарту ISO 20022. Для казначейських і фінансових команд це означає, що ваші канали обробки банківських виписок повинні перейти з MT940 на CAMT.053 до настання жорстких термінів.

## Графік переходу на SWIFT

| Дата | Віха | Вплив |
|---|---|---|
| **Листопад 2025** | Припинено співіснування MT-MX для транскордонних платежів | Повідомлення PACS тепер лише ISO 20022 |
| **Листопад 2026** | Обов’язкові структуровані/гібридні адреси; Мультикоманду MT101 відхилено; Управління справами Фаза 1 | Формати адрес мають відповідати; деякі повідомлення MT будуть відхилені |
| **Кінець 2026** | Починається згода на отримання CAMT.052/.053/.054 | Фінансові установи можуть почати отримувати власні звіти ISO |
| **Листопад 2027** | Усі FI повинні отримати CAMT.053 нативно | SWIFT припиняє конвертувати формат MT в ISO; ваші системи повинні безпосередньо аналізувати CAMT |
| **Листопад 2028** | MT940/MT942/MT950/MT900/MT910 повністю виведено з експлуатації | Застарілі формати виписок більше не доступні; CAMT.052/.053/.054 є єдиним варіантом |

## Що зміниться у вашому коді

### Раніше: лише MT940

```python
from bankstatementparser import Mt940Parser

parser = Mt940Parser("statement.mt940")
df = parser.parse()
```

### Після: обидва формати з автоматичним визначенням

```python
from bankstatementparser import create_parser, detect_statement_format

fmt = detect_statement_format("statement.xml")  # or .mt940
parser = create_parser("statement.xml", fmt)
df = parser.parse()  # Same DataFrame schema regardless of format
```

The`detect_statement_format()`функція визначає, чи файл має формат MT940, CAMT.053, PAIN.001 чи будь-який інший підтримуваний формат. The`create_parser()`функція повертає правильний аналізатор. Ваш вихідний код працює однаково незалежно від вихідного формату.

## CAMT.053 проти MT940: ключові відмінності

| Особливість | MT940 | CAMT.053 |
|---|---|---|
| Насиченість даними | Обмежені поля | У 3-5 разів більше даних за транзакцію |
| Набір символів | Обмежено (набір символів SWIFT) | Повний Юнікод |
| Структура | Плоский текст з тегами | XML із просторами імен |
| Балансова звітність | Тільки відкриття/закриття | Кілька типів балансу |
| Список літератури | Єдине поле посилання | Кілька типів посилань |
| Обробка валюти | Базовий | Повна мультивалютність з обмінними курсами |

## Чим допомагає аналізатор банківських виписок

- **Уніфікований API**: аналізуйте MT940 і CAMT.053 за допомогою одного і того ж`parse()`метод, створюючи ідентичні схеми DataFrame.
- **Автовизначення**: не потрібно знати формат заздалегідь.`detect_statement_format()`ідентифікує його автоматично.
- **Незалежність від простору імен**: обробляє будь-який варіант CAMT.053 (001.02, 001.04 або обгортки для конкретного банку) без налаштування.
- **Потокове передавання**: обробляйте великі файли CAMT (50 МБ+, 50K+ транзакцій) з обмеженою пам’яттю.
- **Тестування міграції**: запустіть обидва парсери паралельно в той самий діапазон дат, щоб перевірити узгодженість вихідних даних перед перемиканням.

## Початок роботи

```bash
pip install bankstatementparser
```

```python
from bankstatementparser import create_parser, detect_statement_format

# Works with MT940 today, CAMT.053 tomorrow
for file in bank_statement_files:
    fmt = detect_statement_format(file)
    parser = create_parser(file, fmt)
    df = parser.parse()
    process(df)  # Your code doesn't change
```

[Прочитайте повну документацію](/getting-started/index.html)

[Порівняйте з альтернативами ❯](/comparison/index.html) | [Перегляньте приклади використання в реальному світі ❯](/use-cases/index.html)
