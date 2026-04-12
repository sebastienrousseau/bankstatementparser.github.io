---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Посібник з переходу на ISO 20022"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Парсер банківських виписок. Всі права захищені."
date: "Apr 11, 2026"
description: "Практичний посібник із графіка переходу на SWIFT ISO 20022 (2026–2028), переходу MT940 на CAMT.053 і того, як Parser банківських виписок допомагає командам казначейства перейти."
download: ""
format-detection: "telephone=no"
hreflang: "uk"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/uk/migration/index.html"
image_alt: "Логотип аналізатора банківських виписок, розширте можливості вашого фінансового аналізу за допомогою безперебійного вилучення даних"
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "Перехід на ISO 20022, MT940 на CAMT.053, кінцевий термін SWIFT 2027, припинення використання MT940 2028, Python міграції банківської виписки, синтаксичний аналізатор CAMT.053, хронологія ISO 20022"
language: "uk-UA"
layout: "about"
locale: "uk_UA"
logo_alt: "Логотип аналізатора банківських виписок, розширте можливості вашого фінансового аналізу за допомогою безперебійного вилучення даних"
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
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
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Практичний посібник із графіка переходу на SWIFT ISO 20022 (2026–2028), переходу MT940 на CAMT.053 і того, як Parser банківських виписок допомагає командам казначейства перейти."
twitter_image: "/images/logos/bankstatementparser.webp"
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

**Коротко:** SWIFT припинить MT940 до листопада 2028 року. Bank Statement Parser обробляє і MT940, і CAMT.053 через єдиний API, тому ваш pipeline аналізу працюватиме під час переходу та після нього.

## Чому ця міграція важлива

SWIFT припиняє підтримку застарілих форматів повідомлень MT на користь розширеного стандарту ISO 20022. Для казначейських та фінансових команд це означає, що ваші pipeline обробки банківських виписок повинні перейти з MT940 на CAMT.053 до жорстких дедлайнів.

## Графік міграції SWIFT

| Дата | Етап | Вплив |
|---|---|---|
| **Листопад 2025** | Припинено співіснування MT-MX для транскордонних платежів | Повідомлення PACS тепер тільки ISO 20022 |
| **Листопад 2026** | Обов’язкові структуровані/гібридні адреси; MT101 з кількома інструкціями відхиляється; Фаза 1 Case Management | Формати адрес мають відповідати; деякі MT-повідомлення будуть відхилені |
| **Кінець 2026** | Початок opt-in для отримання CAMT.052/.053/.054 | Фінансові установи можуть почати отримувати нативні ISO-виписки |
| **Листопад 2027** | Усі фінансові установи мають отримувати CAMT.053 нативно | SWIFT припиняє конвертацію MT у формат ISO; ваші системи мають аналізувати CAMT напряму |
| **Листопад 2028** | MT940/MT942/MT950/MT900/MT910 повністю припинені | Застарілі формати виписок більше недоступні; CAMT.052/.053/.054 — єдиний варіант |

## Що зміниться у вашому коді

### До: тільки MT940

```python
from bankstatementparser import Mt940Parser

parser = Mt940Parser("statement.mt940")
df = parser.parse()
```

### Після: обидва формати з автовизначенням

```python
from bankstatementparser import create_parser, detect_statement_format

fmt = detect_statement_format("statement.xml")  # or .mt940
parser = create_parser("statement.xml", fmt)
df = parser.parse()  # Same DataFrame schema regardless of format
```

Функція `detect_statement_format()` визначає, чи файл має формат MT940, CAMT.053, PAIN.001 або інший підтримуваний формат. Функція `create_parser()` повертає потрібний парсер. Ваш подальший код працює однаково незалежно від вхідного формату.

## CAMT.053 проти MT940: ключові відмінності

| Характеристика | MT940 | CAMT.053 |
|---|---|---|
| Насиченість даними | Обмежені поля | У 3–5 разів більше даних на транзакцію |
| Набір символів | Обмежений (набір символів SWIFT) | Повний Unicode |
| Структура | Плоский текст з тегами | XML з просторами імен |
| Звітність за балансом | Тільки початковий/кінцевий | Кілька типів балансу |
| Посилання | Одне поле посилання | Кілька типів посилань |
| Обробка валют | Базова | Повна мультивалютність з обмінними курсами |

## Як допомагає Bank Statement Parser

- **Єдиний API**: Аналізуйте MT940, CAMT.053 та PDF-виписки в одному робочому процесі зі стабільним DataFrame-виводом.
- **Автовизначення**: Не потрібно знати формат заздалегідь. `detect_statement_format()` визначає його автоматично.
- **Гібридний PDF pipeline**: Банки, що надають тільки PDF-виписки під час переходу, обслуговуються через `smart_ingest()` з автоматичною перевіркою балансу.
- **Незалежність від просторів імен**: Обробляє будь-який варіант CAMT.053 (001.02, 001.04 або банківські обгортки) без конфігурації.
- **Мультивалютна перевірка**: `verify_balance_multi_currency()` виконує Золоте правило для кожної групи валют — важливо для мультивалютних CAMT-виписок.
- **Streaming**: Обробка великих CAMT-файлів (50 МБ+, 50K+ транзакцій) з обмеженою пам’яттю.
- **Експорт у бухгалтерію**: Експорт напряму у формат hledger або beancount для казначейського обліку.
- **Тестування міграції**: Запустіть обидва парсери паралельно на однаковий період, щоб перевірити узгодженість результатів перед переключенням.

## Початок роботи

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
    process(df)  # Your code doesn’t change
```

Для PDF-виписок від банків, що ще не пропонують структурований CAMT-експорт:

```python
from bankstatementparser.hybrid import smart_ingest

result = smart_ingest("statement.pdf")
assert result.verification.status == "VERIFIED"
```

[Прочитайте повну документацію](/getting-started/index.html)

[Порівняйте з альтернативами ❯](/comparison/index.html) | [Перегляньте реальні сценарії використання ❯](/use-cases/index.html)
