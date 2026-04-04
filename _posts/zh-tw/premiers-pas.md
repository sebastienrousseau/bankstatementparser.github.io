---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "白色的建築，黑色的窗戶"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/daniele-franchi-Vl6YuVBLEys.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 銀行對帳單解析器。版權所有。"
date: "Apr 01, 2026"
description: "開始使用 Python 銀行對帳單解析器：安裝、解析 CAMT/PAIN.001/CSV/OFX/QFX/MT940 文件，並使用串流處理或 CLI 工作流程。"
download: ""
format-detection: "telephone=no"
hreflang: "zh-tw"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/zh-tw/premiers-pas/index.html"
image_alt: "銀行對帳單解析器的徽標，這是一款功能強大的 Python 工具，專為快速、準確的財務資料處理和見解提取而設計。"
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "銀行對帳單解析器、入門、python、CAMT、PAIN.001、CSV、OFX、QFX、MT940、財務數據"
language: "zh-TW"
layout: "start"
locale: "zh_TW"
logo_alt: "銀行對帳單解析器的徽標，這是一款功能強大的 Python 工具，專為快速、準確的財務資料處理和見解提取而設計。"
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "入門"
permalink: "https://bankstatementparser.com/zh-tw/premiers-pas/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "開始使用銀行對帳單解析器建立安全應用程式"
tags: "銀行，語句，解析器，python，camt，pain001，csv，ofx，qfx，mt940，串流媒體，cli"
theme_color: "rgb(73, 214, 251)"
title: "銀行對帳單解析器：安裝與使用指南"
url: "https://bankstatementparser.com/zh-tw/premiers-pas/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/zh-tw/premiers-pas/rss.xml"
category: "財務軟體、Python 庫、開發人員指南"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "開始使用 Python 銀行對帳單解析器：安裝、解析 CAMT/PAIN.001/CSV/OFX/QFX/MT940 文件，並使用串流處理或 CLI 工作流程。"
item_guid: "https://bankstatementparser.com/zh-tw/premiers-pas/rss.xml"
item_link: "https://bankstatementparser.com/zh-tw/premiers-pas/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "銀行對帳單解析器：安裝與使用指南"
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
apple-mobile-web-app-title: "銀行對帳單解析器：安裝與使用指南"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "安裝並使用銀行對帳單解析器在 Python 中解析 CAMT、PAIN.001、CSV、OFX/QFX 和 MT940 檔案。"
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "銀行對帳單解析器的徽標，這是一款功能強大的 Python 工具，專為快速、準確的財務資料處理和見解提取而設計。"
twitter_site: "@wwdseb"
twitter_title: "銀行對帳單解析器：安裝與使用指南"
twitter_url: "https://bankstatementparser.com/zh-tw/premiers-pas/index.html"

# Humans.txt - The Humans.txt front matter (YAML).

author_website: "https://bankstatementparser.com"
author_twitter: "@wwdseb"
author_location: "London, UK"
thanks: "感謝您的閱讀！"
site_last_updated: "2026-04-01"
site_standards: "HTML5, CSS3, RSS, Atom, JSON, XML, YAML, Markdown, TOML"
site_components: "Shokunin SSG, Shokunin CLI, Shokunin Templates, Shokunin Themes, Kaishi SSG, Kaishi CLI, Kaishi Templates, Kaishi Themes"
site_software: "Shokunin, Rust"

---

＃＃ 要求

- Python 3.9 至 3.14
- 終端存取（macOS、Linux 或 WSL）

＃＃ 安裝

```bash
pip install bankstatementparser
```

對於 Polars DataFrame 支援：

```bash
pip install bankstatementparser[polars]
```

## 快速入門

### 自動偵測並解析任何格式

```python
from bankstatementparser import create_parser, detect_statement_format

fmt = detect_statement_format("transactions.ofx")
parser = create_parser("transactions.ofx", fmt)
df = parser.parse()  # pandas DataFrame
print(df.head())
```

這適用於`.xml`(CAMT/PAIN.001),`.csv`, `.ofx`, `.qfx`, `.mt940`， 和`.sta`文件。

### 解析 CAMT.053

```python
from bankstatementparser import CamtParser

parser = CamtParser("statement.xml")
transactions = parser.parse()
```

### 解析 PAIN.001

```python
from bankstatementparser import Pain001Parser

parser = Pain001Parser("payment.xml")
payments = parser.parse()
```

## 串流大文件

對於具有數千個事務的文件，請使用串流傳輸來限制記憶體：

```python
parser = CamtParser("large_statement.xml")
for transaction in parser.parse_streaming(redact_pii=True):
    process(transaction)  # Memory stays constant
```

## 記憶體中解析

在沒有磁碟 I/O 的情況下從位元組進行解析——對於 SFTP 或 API 工作流程很有用：

```python
xml_bytes = download_from_sftp()
parser = CamtParser.from_bytes(xml_bytes, source_name="daily.xml")
transactions = parser.parse()
```

## 平行文件處理

同時解析多個檔案：

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

## 重複資料刪除

透過置信度分數檢測精確的重複項和可疑匹配項：

```python
from bankstatementparser import CamtParser, Deduplicator

parser = CamtParser("statement.xml")
dedup = Deduplicator()
result = dedup.deduplicate(dedup.from_dataframe(parser.parse()))

print(f"Unique: {len(result.unique_transactions)}")
print(f"Exact duplicates: {len(result.exact_duplicates)}")
print(f"Suspected matches: {len(result.suspected_matches)}")
```

## 安全 ZIP 處理

使用內建安全檢查（炸彈防護、加密條目拒絕）處理壓縮的 XML 檔案：

```python
from bankstatementparser import iter_secure_xml_entries, CamtParser

for entry in iter_secure_xml_entries("statements.zip"):
    parser = CamtParser.from_bytes(entry.xml_bytes, source_name=entry.source_name)
    print(f"{entry.source_name}: {len(parser.parse())} transactions")
```

＃＃ 出口

```python
parser = CamtParser("statement.xml")
parser.export_csv("output.csv")
parser.export_json("output.json")

# Polars (requires bankstatementparser[polars])
polars_df = parser.to_polars()
```

## CLI 用法

```bash
# Parse and display
python -m bankstatementparser.cli --type camt --input statement.xml

# Export to CSV
python -m bankstatementparser.cli --type camt --input statement.xml --output transactions.csv

# Stream with PII visible
python -m bankstatementparser.cli --type camt --input statement.xml --streaming --show-pii
```

CLI 選項：

- `--type {camt,pain001}`-- 解析器類型
-`--input <path>`-- 輸入檔
-`--output <csv_path>`-- 匯出為 CSV
-`--streaming`-- 串流大檔案
-`--show-pii`-- 顯示敏感欄位（預設已編輯）
-`--max-size <MB>`-- 檔案大小限制

## 本機開發設定

```bash
git clone https://github.com/sebastienrousseau/bankstatementparser.git
cd bankstatementparser
python3 -m venv .venv && source .venv/bin/activate
pip install poetry && poetry install --with dev
```

運行測試套件：

```bash
pytest
```

## API 參考

### 解析器類別

| 班級 | 格式 | 進口 |
|---|---|---|
| `CamtParser` | CAMT.053 (ISO 20022) | `from bankstatementparser import CamtParser` |
| `Pain001Parser` | PAIN.001 (ISO 20022) | `from bankstatementparser import Pain001Parser` |
| `CsvStatementParser` | CSV | `from bankstatementparser import CsvStatementParser` |
| `OfxParser` | 氧氟沙星 | `from bankstatementparser import OfxParser` |
| `QfxParser` | QFX | `from bankstatementparser import QfxParser` |
| `Mt940Parser` | MT940 | `from bankstatementparser import Mt940Parser` |

### 實用函數

| 功能 | 目的 |
|---|---|
| `detect_statement_format(path)` | 自動檢測文件格式 |
| `create_parser(path, fmt)` | 建立適當的解析器 |
| `parse_files_parallel(paths)` | 同時解析多個文件 |
| `iter_secure_xml_entries(zip_path)` | 安全地迭代 ZIP 條目 |

### 資料類

| 班級 | 目的 |
|---|---|
| `Deduplicator` | 偵測重複交易 |
| `DeduplicationResult` | 具有唯一、精確和可疑匹配的結果 |
| `InputValidator` | 驗證文件路徑和格式 |
| `Transaction` | 標準化交易記錄 |
| `FileResult` | 並行解析的結果 |
| `ZipXMLSource` | ZIP 會員包裝 |

### 例外情況

| 例外 | 升起時 |
|---|---|
| `ParserError` | 解析失敗 |
| `ExportError` | 匯出失敗（CSV/JSON/Excel） |
| `ValidationError` | 輸入驗證失敗 |
| `ZipSecurityError` | ZIP 安全檢查失敗 |
