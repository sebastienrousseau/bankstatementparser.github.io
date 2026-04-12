---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "白色的建築，黑色的窗戶"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/daniele-franchi-Vl6YuVBLEys.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 銀行對帳單解析器。版權所有。"
date: "Apr 11, 2026"
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

## 系統需求

- Python 3.10 至 3.14
- 終端機存取（macOS、Linux 或 WSL）

## 安裝

```bash
# 核心安裝（僅確定性解析器）
pip install bankstatementparser
```

可選的額外功能套件：

```bash
# 文字 LLM 路徑，用於數位 PDF（litellm + pypdf）
pip install 'bankstatementparser[hybrid]'

# 更高精度的表格擷取（加入 pdfplumber）
pip install 'bankstatementparser[hybrid-plus]'

# 視覺 LLM 路徑，用於掃描 PDF（加入 pypdfium2）
pip install 'bankstatementparser[hybrid-vision]'

# LLM 驅動的交易分類
pip install 'bankstatementparser[enrichment]'

# REST API 微服務（FastAPI + uvicorn）
pip install 'bankstatementparser[api]'

# 可選的 Polars DataFrame 支援
pip install 'bankstatementparser[polars]'
```

## 快速入門

### 自動偵測並解析任何結構化格式

```python
from bankstatementparser import create_parser, detect_statement_format

fmt = detect_statement_format("transactions.ofx")
parser = create_parser("transactions.ofx", fmt)
df = parser.parse()  # pandas DataFrame
print(df.head())
```

適用於 `.xml`（CAMT/PAIN.001）、`.csv`、`.ofx`、`.qfx`、`.mt940` 及 `.sta` 檔案。

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

### 解析 PDF 銀行對帳單（混合管線）

混合管線會智慧地將 PDF 路由至三條擷取路徑：

```python
from bankstatementparser.hybrid import smart_ingest

result = smart_ingest("statement.pdf")
print(result.source_method)         # "deterministic" | "llm" | "vision"
print(result.verification.status)   # VERIFIED | DISCREPANCY | FAILED
print(result.transactions)          # List of extracted transactions
```

每次擷取都透過**黃金法則**進行驗證：`opening + credits − debits == closing`。

## 串流處理大型檔案

對於包含數千筆交易的檔案，使用串流處理以維持固定記憶體用量：

```python
parser = CamtParser("large_statement.xml")
for transaction in parser.parse_streaming(redact_pii=True):
    process(transaction)  # Memory stays constant
```

## 記憶體中解析

從位元組直接解析，無磁碟 I/O——適用於 SFTP 或 API 工作流程：

```python
xml_bytes = download_from_sftp()
parser = CamtParser.from_bytes(xml_bytes, source_name="daily.xml")
transactions = parser.parse()
```

## 平行檔案處理

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

## 批次目錄掃描

處理整個資料夾樹狀結構，自動去重：

```python
from bankstatementparser.hybrid import scan_and_ingest

batch = scan_and_ingest("statements/2026/", pattern="**/*.pdf")
print(f"Processed: {len(batch.results)} files")
print(f"Unique transactions: {batch.unique_count}")
```

## 去重

冪等交易雜湊，適用於安全的增量匯入：

```python
from bankstatementparser import CamtParser, Deduplicator

parser = CamtParser("statement.xml")
dedup = Deduplicator()
result = dedup.deduplicate(dedup.from_dataframe(parser.parse()))

print(f"Unique: {len(result.unique_transactions)}")
print(f"Exact duplicates: {len(result.exact_duplicates)}")
print(f"Suspected matches: {len(result.suspected_matches)}")
```

## 交易分類（增強）

使用 LLM 驅動的分類自動歸類交易：

```python
from bankstatementparser.enrichment import Categorizer

categorizer = Categorizer()
enriched = categorizer.categorize_batch(transactions)
for txn in enriched:
    print(f"{txn.description}: {txn.category}")
```

## 帳本匯出（hledger / beancount）

將交易匯出為純文字記帳日記帳格式：

```python
from bankstatementparser.export import to_hledger, to_beancount

journal = to_hledger(transactions, account="Assets:Bank:Checking")
beancount_journal = to_beancount(transactions, account="Assets:Bank:Checking")
```

## 多幣別餘額驗證

依幣別群組獨立驗證餘額：

```python
from bankstatementparser.hybrid import verify_balance_multi_currency

results = verify_balance_multi_currency(transactions)
for currency, verification in results.items():
    print(f"{currency}: {verification.status}")
```

## REST API

以 FastAPI 微服務部署：

```bash
# 啟動 API 伺服器
bankstatementparser-api --port 8000

# 容器部署
bankstatementparser-api --host 0.0.0.0 --port 9000
```

端點：
- `POST /ingest` -- 解析銀行對帳單檔案
- `GET /health` -- 健康檢查

## 安全 ZIP 處理

使用內建安全檢查（炸彈防護、加密條目拒絕）處理壓縮的 XML 檔案：

```python
from bankstatementparser import iter_secure_xml_entries, CamtParser

for entry in iter_secure_xml_entries("statements.zip"):
    parser = CamtParser.from_bytes(entry.xml_bytes, source_name=entry.source_name)
    print(f"{entry.source_name}: {len(parser.parse())} transactions")
```

## 匯出

```python
parser = CamtParser("statement.xml")
parser.export_csv("output.csv")
parser.export_json("output.json")

# Polars (requires bankstatementparser[polars])
polars_df = parser.to_polars()

# Excel
parser.camt_to_excel("output.xlsx")
```

## CLI 用法

```bash
# 解析結構化格式
bankstatementparser --type camt --input statement.xml
bankstatementparser --type pain001 --input payment.xml

# 混合 PDF 管線
bankstatementparser --type ingest --input statement.pdf
bankstatementparser --type ingest --input statement.pdf --output ledger.csv

# 互動式審核模式
bankstatementparser --type review --input result.json
bankstatementparser --type review --input result.json --output reviewed.json

# 以串流方式匯出為 CSV
bankstatementparser --type camt --input statement.xml --output transactions.csv
bankstatementparser --type camt --input statement.xml --streaming --show-pii
```

CLI 選項：

- `--type {camt,pain001,ingest,review}` -- 解析器類型或模式
- `--input <path>` -- 輸入檔案
- `--output <path>` -- 匯出檔案（CSV 或 JSON）
- `--streaming` -- 串流處理大型檔案
- `--show-pii` -- 顯示敏感欄位（預設已遮蔽）
- `--max-size <MB>` -- 檔案大小限制

## 本機開發設定

```bash
git clone https://github.com/sebastienrousseau/bankstatementparser.git
cd bankstatementparser
python3 -m venv .venv && source .venv/bin/activate
pip install poetry && poetry install --with dev
make install-hooks   # pre-commit hook runs `make verify` before every commit
```

執行測試套件：

```bash
pytest
```

## API 參考

### 解析器類別

| 類別 | 格式 | 匯入方式 |
|---|---|---|
| `CamtParser` | CAMT.053 (ISO 20022) | `from bankstatementparser import CamtParser` |
| `Pain001Parser` | PAIN.001 (ISO 20022) | `from bankstatementparser import Pain001Parser` |
| `CsvStatementParser` | CSV | `from bankstatementparser import CsvStatementParser` |
| `OfxParser` | OFX | `from bankstatementparser import OfxParser` |
| `QfxParser` | QFX | `from bankstatementparser import QfxParser` |
| `Mt940Parser` | MT940 | `from bankstatementparser import Mt940Parser` |
| `smart_ingest()` | PDF（混合管線） | `from bankstatementparser.hybrid import smart_ingest` |

### 工具函式

| 函式 | 用途 |
|---|---|
| `detect_statement_format(path)` | 自動偵測檔案格式 |
| `create_parser(path, fmt)` | 建立對應的解析器 |
| `parse_files_parallel(paths)` | 同時解析多個檔案 |
| `iter_secure_xml_entries(zip_path)` | 安全地迭代 ZIP 條目 |
| `smart_ingest(path)` | 混合 PDF 擷取並驗證 |
| `scan_and_ingest(dir, pattern)` | 批次目錄掃描 |
| `verify_balance_multi_currency(txns)` | 依幣別驗證餘額 |
| `to_hledger(txns, account)` | 匯出為 hledger 日記帳格式 |
| `to_beancount(txns, account)` | 匯出為 beancount 日記帳格式 |

### 資料類別

| 類別 | 用途 |
|---|---|
| `Deduplicator` | 偵測重複交易 |
| `DeduplicationResult` | 包含唯一、精確及可疑匹配的結果 |
| `InputValidator` | 驗證檔案路徑及格式 |
| `Transaction` | 標準化交易記錄 |
| `FileResult` | 平行解析的結果 |
| `ZipXMLSource` | ZIP 成員封裝 |
| `IngestResult` | 混合管線結果（含驗證） |
| `VerificationResult` | 餘額驗證結果 |
| `Categorizer` | LLM 驅動的交易分類 |
| `AccountMapper` | 正規表示式帳戶對應規則 |

### 例外

| 例外 | 觸發時機 |
|---|---|
| `ParserError` | 解析失敗 |
| `ExportError` | 匯出失敗（CSV/JSON/Excel） |
| `ValidationError` | 輸入驗證失敗 |
| `ZipSecurityError` | ZIP 安全檢查失敗 |
