---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "בניין לבן עם חלונות שחורים"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/daniele-franchi-Vl6YuVBLEys.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 מנתח חשבונות בנק. כֹּל הַזְכוּיוֹת שְׁמוּרוֹת."
date: "Apr 01, 2026"
description: "התחל עם מנתח חשבונות בנק עבור Python: התקן, נתח קבצי CAMT/PAIN.001/CSV/OFX/QFX/MT940 והשתמש בזרימות עבודה בסטרימינג או ב-CLI."
download: ""
format-detection: "telephone=no"
hreflang: "he"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/he/getting-started/index.html"
image_alt: "הלוגו של Bank Statement Parser, כלי Python רב עוצמה המיועד לעיבוד נתונים פיננסיים מהירים ומדויקים וחילוץ תובנות."
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "מנתח דפי בנק, תחילת העבודה, python, CAMT, PAIN.001, CSV, OFX, QFX, MT940, נתונים פיננסיים"
language: "he-IL"
layout: "start"
locale: "he_IL"
logo_alt: "הלוגו של Bank Statement Parser, כלי Python רב עוצמה המיועד לעיבוד נתונים פיננסיים מהירים ומדויקים וחילוץ תובנות."
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "תחילת העבודה"
permalink: "https://bankstatementparser.com/he/getting-started/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "התחל לבנות יישומים מאובטחים עם מנתח חשבונות בנק"
tags: "bank,statement,parser,python,camt,pain001,csv,ofx,qfx,mt940,streaming,cli"
theme_color: "rgb(73, 214, 251)"
title: "מנתח חשבונות בנק: מדריך התקנה ושימוש"
url: "https://bankstatementparser.com/he/getting-started/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/he/getting-started/rss.xml"
category: "תוכנת פיננסים, ספריית פייתון, מדריך למפתחים"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "התחל עם מנתח חשבונות בנק עבור Python: התקן, נתח קבצי CAMT/PAIN.001/CSV/OFX/QFX/MT940 והשתמש בזרימות עבודה בסטרימינג או ב-CLI."
item_guid: "https://bankstatementparser.com/he/getting-started/rss.xml"
item_link: "https://bankstatementparser.com/he/getting-started/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "מנתח חשבונות בנק: מדריך התקנה ושימוש"
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
apple-mobile-web-app-title: "מנתח חשבונות בנק: מדריך התקנה ושימוש"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "התקן והשתמש ב-Bank Statement Parser כדי לנתח קבצי CAMT, PAIN.001, CSV, OFX/QFX ו-MT940 ב-Python."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "הלוגו של Bank Statement Parser, כלי Python רב עוצמה המיועד לעיבוד נתונים פיננסיים מהירים ומדויקים וחילוץ תובנות."
twitter_site: "@wwdseb"
twitter_title: "מנתח חשבונות בנק: מדריך התקנה ושימוש"
twitter_url: "https://bankstatementparser.com/he/getting-started/index.html"

# Humans.txt - The Humans.txt front matter (YAML).

author_website: "https://bankstatementparser.com"
author_twitter: "@wwdseb"
author_location: "London, UK"
thanks: "תודה שקראת!"
site_last_updated: "2026-04-01"
site_standards: "HTML5, CSS3, RSS, Atom, JSON, XML, YAML, Markdown, TOML"
site_components: "Shokunin SSG, Shokunin CLI, Shokunin Templates, Shokunin Themes, Kaishi SSG, Kaishi CLI, Kaishi Templates, Kaishi Themes"
site_software: "Shokunin, Rust"

---

## דרישות

- Python 3.9 עד 3.14
- גישה למסוף (macOS, Linux או WSL)

## התקן

```bash
pip install bankstatementparser
```

לתמיכה ב-Polars DataFrame:

```bash
pip install bankstatementparser[polars]
```

## התחלה מהירה

### זיהוי וניתוח אוטומטי של כל פורמט

```python
from bankstatementparser import create_parser, detect_statement_format

fmt = detect_statement_format("transactions.ofx")
parser = create_parser("transactions.ofx", fmt)
df = parser.parse()  # pandas DataFrame
print(df.head())
```

זה עובד עם`.xml`(CAMT/PAIN.001),`.csv`, `.ofx`, `.qfx`, `.mt940`, ו`.sta`קבצים.

### ניתוח CAMT.053

```python
from bankstatementparser import CamtParser

parser = CamtParser("statement.xml")
transactions = parser.parse()
```

### ניתוח PAIN.001

```python
from bankstatementparser import Pain001Parser

parser = Pain001Parser("payment.xml")
payments = parser.parse()
```

## הזרמת קבצים גדולים

עבור קבצים עם אלפי עסקאות, השתמש בסטרימינג כדי לשמור על זיכרון מוגבל:

```python
parser = CamtParser("large_statement.xml")
for transaction in parser.parse_streaming(redact_pii=True):
    process(transaction)  # Memory stays constant
```

## ניתוח בזיכרון

ניתוח מבתים ללא קלט/פלט דיסק -- שימושי עבור זרימות עבודה של SFTP או API:

```python
xml_bytes = download_from_sftp()
parser = CamtParser.from_bytes(xml_bytes, source_name="daily.xml")
transactions = parser.parse()
```

## עיבוד קבצים מקביל

נתח קבצים מרובים במקביל:

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

## מניעת כפילויות

זהה כפילויות מדויקות והתאמות חשודות עם ציוני ביטחון:

```python
from bankstatementparser import CamtParser, Deduplicator

parser = CamtParser("statement.xml")
dedup = Deduplicator()
result = dedup.deduplicate(dedup.from_dataframe(parser.parse()))

print(f"Unique: {len(result.unique_transactions)}")
print(f"Exact duplicates: {len(result.exact_duplicates)}")
print(f"Suspected matches: {len(result.suspected_matches)}")
```

## עיבוד ZIP מאובטח

עבד קובצי XML מכווץ עם בדיקות אבטחה מובנות (הגנה על פצצות, דחיית כניסה מוצפנת):

```python
from bankstatementparser import iter_secure_xml_entries, CamtParser

for entry in iter_secure_xml_entries("statements.zip"):
    parser = CamtParser.from_bytes(entry.xml_bytes, source_name=entry.source_name)
    print(f"{entry.source_name}: {len(parser.parse())} transactions")
```

## ייצוא

```python
parser = CamtParser("statement.xml")
parser.export_csv("output.csv")
parser.export_json("output.json")

# Polars (requires bankstatementparser[polars])
polars_df = parser.to_polars()
```

## שימוש ב-CLI

```bash
# Parse and display
python -m bankstatementparser.cli --type camt --input statement.xml

# Export to CSV
python -m bankstatementparser.cli --type camt --input statement.xml --output transactions.csv

# Stream with PII visible
python -m bankstatementparser.cli --type camt --input statement.xml --streaming --show-pii
```

אפשרויות CLI:

- `--type {camt,pain001}`-- סוג מנתח
-`--input <path>`-- קובץ קלט
-`--output <csv_path>`-- ייצא ל-CSV
-`--streaming`-- הזרמת קבצים גדולים
-`--show-pii`-- הצג שדות רגישים (מוכן כברירת מחדל)
-`--max-size <MB>`-- מגבלת גודל הקובץ

## הגדרת פיתוח מקומי

```bash
git clone https://github.com/sebastienrousseau/bankstatementparser.git
cd bankstatementparser
python3 -m venv .venv && source .venv/bin/activate
pip install poetry && poetry install --with dev
```

הפעל את חבילת הבדיקה:

```bash
pytest
```

## הפניה ל-API

### כיתות מנתח

| מַחלָקָה | פוּרמָט | יְבוּא |
|---|---|---|
| `CamtParser` | CAMT.053 (ISO 20022) | `from bankstatementparser import CamtParser` |
| `Pain001Parser` | PAIN.001 (ISO 20022) | `from bankstatementparser import Pain001Parser` |
| `CsvStatementParser` | CSV | `from bankstatementparser import CsvStatementParser` |
| `OfxParser` | OFX | `from bankstatementparser import OfxParser` |
| `QfxParser` | QFX | `from bankstatementparser import QfxParser` |
| `Mt940Parser` | MT940 | `from bankstatementparser import Mt940Parser` |

### פונקציות שירות

| פוּנקצִיָה | מַטָרָה |
|---|---|
| `detect_statement_format(path)` | זיהוי אוטומטי של פורמט קובץ |
| `create_parser(path, fmt)` | צור את המנתח המתאים |
| `parse_files_parallel(paths)` | נתח קבצים מרובים בו-זמנית |
| `iter_secure_xml_entries(zip_path)` | חזר על ערכי ZIP בצורה מאובטחת |

### כיתות נתונים

| מַחלָקָה | מַטָרָה |
|---|---|
| `Deduplicator` | זיהוי עסקאות כפולות |
| `DeduplicationResult` | תוצאה עם התאמות ייחודיות, מדויקות וחשודות |
| `InputValidator` | אמת נתיבים ופורמטים של קבצים |
| `Transaction` | רשומת עסקה מנורמלת |
| `FileResult` | תוצאה מניתוח מקביל |
| `ZipXMLSource` | עטיפת חבר ZIP |

### חריגים

| חֲרִיגָה | כאשר גדלו |
|---|---|
| `ParserError` | כשלים בניתוח |
| `ExportError` | כשלים בייצוא (CSV/JSON/Excel) |
| `ValidationError` | כשלים באימות קלט |
| `ZipSecurityError` | כשלים בבדיקת אבטחה ZIP |
