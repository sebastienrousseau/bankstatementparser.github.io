---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "בניין לבן עם חלונות שחורים"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/daniele-franchi-Vl6YuVBLEys.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 מנתח חשבונות בנק. כֹּל הַזְכוּיוֹת שְׁמוּרוֹת."
date: "Apr 11, 2026"
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

- Python 3.10 עד 3.14
- גישה לטרמינל (macOS, Linux או WSL)

## התקנה

```bash
# התקנה בסיסית (מנתחים דטרמיניסטיים בלבד)
pip install bankstatementparser
```

תוספות אופציונליות ליכולות נוספות:

```bash
# נתיב Text-LLM לקבצי PDF דיגיטליים (litellm + pypdf)
pip install 'bankstatementparser[hybrid]'

# חילוץ טבלאות באיכות גבוהה יותר (מוסיף pdfplumber)
pip install 'bankstatementparser[hybrid-plus]'

# נתיב Vision-LLM לקבצי PDF סרוקים (מוסיף pypdfium2)
pip install 'bankstatementparser[hybrid-vision]'

# סיווג עסקאות מונע LLM
pip install 'bankstatementparser[enrichment]'

# שירות REST API (FastAPI + uvicorn)
pip install 'bankstatementparser[api]'

# תמיכה אופציונלית ב-Polars DataFrame
pip install 'bankstatementparser[polars]'
```

## התחלה מהירה

### זיהוי אוטומטי וניתוח כל פורמט מובנה

```python
from bankstatementparser import create_parser, detect_statement_format

fmt = detect_statement_format("transactions.ofx")
parser = create_parser("transactions.ofx", fmt)
df = parser.parse()  # pandas DataFrame
print(df.head())
```

עובד עם קבצי `.xml` (CAMT/PAIN.001), `.csv`, `.ofx`, `.qfx`, `.mt940` ו-`.sta`.

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

### ניתוח דפי חשבון PDF (Pipeline היברידי)

ה-pipeline ההיברידי מנתב קבצי PDF בצורה חכמה דרך שלושה נתיבי חילוץ:

```python
from bankstatementparser.hybrid import smart_ingest

result = smart_ingest("statement.pdf")
print(result.source_method)         # "deterministic" | "llm" | "vision"
print(result.verification.status)   # VERIFIED | DISCREPANCY | FAILED
print(result.transactions)          # List of extracted transactions
```

כל חילוץ מאומת באמצעות **כלל הזהב**: `opening + credits − debits == closing`.

## streaming קבצים גדולים

עבור קבצים עם אלפי עסקאות, השתמש ב-streaming לשמירה על זיכרון מוגבל:

```python
parser = CamtParser("large_statement.xml")
for transaction in parser.parse_streaming(redact_pii=True):
    process(transaction)  # Memory stays constant
```

## ניתוח בזיכרון

ניתוח מבתים ללא קלט/פלט דיסק -- שימושי לתהליכי SFTP או API:

```python
xml_bytes = download_from_sftp()
parser = CamtParser.from_bytes(xml_bytes, source_name="daily.xml")
transactions = parser.parse()
```

## עיבוד קבצים מקבילי

ניתוח מספר קבצים בו-זמנית:

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

## סריקת תיקיות בכמות גדולה

עיבוד עצי תיקיות שלמים עם מניעת כפילויות אוטומטית:

```python
from bankstatementparser.hybrid import scan_and_ingest

batch = scan_and_ingest("statements/2026/", pattern="**/*.pdf")
print(f"Processed: {len(batch.results)} files")
print(f"Unique transactions: {batch.unique_count}")
```

## מניעת כפילויות

hash עסקאות אידמפוטנטי לקליטה מצטברת בטוחה:

```python
from bankstatementparser import CamtParser, Deduplicator

parser = CamtParser("statement.xml")
dedup = Deduplicator()
result = dedup.deduplicate(dedup.from_dataframe(parser.parse()))

print(f"Unique: {len(result.unique_transactions)}")
print(f"Exact duplicates: {len(result.exact_duplicates)}")
print(f"Suspected matches: {len(result.suspected_matches)}")
```

## סיווג עסקאות (העשרה)

סיווג אוטומטי של עסקאות באמצעות LLM:

```python
from bankstatementparser.enrichment import Categorizer

categorizer = Categorizer()
enriched = categorizer.categorize_batch(transactions)
for txn in enriched:
    print(f"{txn.description}: {txn.category}")
```

## ייצוא ל-Ledger (hledger / beancount)

ייצוא עסקאות לפורמטים של חשבונאות בטקסט:

```python
from bankstatementparser.export import to_hledger, to_beancount

journal = to_hledger(transactions, account="Assets:Bank:Checking")
beancount_journal = to_beancount(transactions, account="Assets:Bank:Checking")
```

## אימות יתרה רב-מטבעי

אימות יתרות באופן עצמאי לכל קבוצת מטבע:

```python
from bankstatementparser.hybrid import verify_balance_multi_currency

results = verify_balance_multi_currency(transactions)
for currency, verification in results.items():
    print(f"{currency}: {verification.status}")
```

## REST API

פריסה כשירות FastAPI:

```bash
# הפעלת שרת ה-API
bankstatementparser-api --port 8000

# לפריסות בקונטיינר
bankstatementparser-api --host 0.0.0.0 --port 9000
```

Endpoints:
- `POST /ingest` -- ניתוח קובץ דף חשבון בנק
- `GET /health` -- בדיקת תקינות

## עיבוד ZIP מאובטח

עיבוד קבצי XML דחוסים עם בדיקות אבטחה מובנות (הגנת פצצות, דחיית ערכים מוצפנים):

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

# Excel
parser.camt_to_excel("output.xlsx")
```

## שימוש ב-CLI

```bash
# ניתוח פורמטים מובנים
bankstatementparser --type camt --input statement.xml
bankstatementparser --type pain001 --input payment.xml

# Pipeline היברידי ל-PDF
bankstatementparser --type ingest --input statement.pdf
bankstatementparser --type ingest --input statement.pdf --output ledger.csv

# מצב סקירה אינטראקטיבי
bankstatementparser --type review --input result.json
bankstatementparser --type review --input result.json --output reviewed.json

# ייצוא ל-CSV עם streaming
bankstatementparser --type camt --input statement.xml --output transactions.csv
bankstatementparser --type camt --input statement.xml --streaming --show-pii
```

אפשרויות CLI:

- `--type {camt,pain001,ingest,review}` -- סוג מנתח או מצב
- `--input <path>` -- קובץ קלט
- `--output <path>` -- קובץ ייצוא (CSV או JSON)
- `--streaming` -- streaming לקבצים גדולים
- `--show-pii` -- הצג שדות רגישים (מוסתרים כברירת מחדל)
- `--max-size <MB>` -- מגבלת גודל קובץ

## הגדרת פיתוח מקומי

```bash
git clone https://github.com/sebastienrousseau/bankstatementparser.git
cd bankstatementparser
python3 -m venv .venv && source .venv/bin/activate
pip install poetry && poetry install --with dev
make install-hooks   # pre-commit hook runs `make verify` before every commit
```

הרצת חבילת הבדיקות:

```bash
pytest
```

## הפניה ל-API

### מחלקות מנתח

| מחלקה | פורמט | ייבוא |
|---|---|---|
| `CamtParser` | CAMT.053 (ISO 20022) | `from bankstatementparser import CamtParser` |
| `Pain001Parser` | PAIN.001 (ISO 20022) | `from bankstatementparser import Pain001Parser` |
| `CsvStatementParser` | CSV | `from bankstatementparser import CsvStatementParser` |
| `OfxParser` | OFX | `from bankstatementparser import OfxParser` |
| `QfxParser` | QFX | `from bankstatementparser import QfxParser` |
| `Mt940Parser` | MT940 | `from bankstatementparser import Mt940Parser` |
| `smart_ingest()` | PDF (pipeline היברידי) | `from bankstatementparser.hybrid import smart_ingest` |

### פונקציות שירות

| פונקציה | מטרה |
|---|---|
| `detect_statement_format(path)` | זיהוי אוטומטי של פורמט קובץ |
| `create_parser(path, fmt)` | יצירת המנתח המתאים |
| `parse_files_parallel(paths)` | ניתוח מספר קבצים בו-זמנית |
| `iter_secure_xml_entries(zip_path)` | איטרציה מאובטחת על ערכי ZIP |
| `smart_ingest(path)` | חילוץ PDF היברידי עם אימות |
| `scan_and_ingest(dir, pattern)` | סריקת תיקיות בכמות גדולה |
| `verify_balance_multi_currency(txns)` | אימות יתרה לכל מטבע |
| `to_hledger(txns, account)` | ייצוא לפורמט יומן hledger |
| `to_beancount(txns, account)` | ייצוא לפורמט יומן beancount |

### מחלקות נתונים

| מחלקה | מטרה |
|---|---|
| `Deduplicator` | זיהוי עסקאות כפולות |
| `DeduplicationResult` | תוצאה עם התאמות ייחודיות, מדויקות וחשודות |
| `InputValidator` | אימות נתיבים ופורמטים של קבצים |
| `Transaction` | רשומת עסקה מנורמלת |
| `FileResult` | תוצאה מניתוח מקבילי |
| `ZipXMLSource` | עטיפת חבר ZIP |
| `IngestResult` | תוצאת pipeline היברידי עם אימות |
| `VerificationResult` | תוצאת אימות יתרה |
| `Categorizer` | סיווג עסקאות מונע LLM |
| `AccountMapper` | כללי מיפוי חשבונות מבוססי regex |

### חריגות

| חריגה | מתי מופעלת |
|---|---|
| `ParserError` | כשלים בניתוח |
| `ExportError` | כשלים בייצוא (CSV/JSON/Excel) |
| `ValidationError` | כשלים באימות קלט |
| `ZipSecurityError` | כשלים בבדיקות אבטחת ZIP |
