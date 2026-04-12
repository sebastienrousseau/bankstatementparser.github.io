---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "白色的建筑，黑色的窗户"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/daniele-franchi-Vl6YuVBLEys.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 银行对账单解析器。版权所有。"
date: "Apr 11, 2026"
description: "开始使用 Python 银行对账单解析器：安装、解析 CAMT/PAIN.001/CSV/OFX/QFX/MT940 文件，并使用流式处理或 CLI 工作流程。"
download: ""
format-detection: "telephone=no"
hreflang: "zh"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/zh/premiers-pas/index.html"
image_alt: "银行对账单解析器的徽标，这是一款功能强大的 Python 工具，专为快速、准确的财务数据处理和见解提取而设计。"
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "银行对账单解析器、入门、python、CAMT、PAIN.001、CSV、OFX、QFX、MT940、财务数据"
language: "zh-CN"
layout: "start"
locale: "zh_CN"
logo_alt: "银行对账单解析器的徽标，这是一款功能强大的 Python 工具，专为快速、准确的财务数据处理和见解提取而设计。"
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "入门"
permalink: "https://bankstatementparser.com/zh/premiers-pas/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "开始使用银行对账单解析器构建安全应用程序"
tags: "银行，语句，解析器，python，camt，pain001，csv，ofx，qfx，mt940，流媒体，cli"
theme_color: "rgb(73, 214, 251)"
title: "银行对账单解析器：安装和使用指南"
url: "https://bankstatementparser.com/zh/premiers-pas/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/zh/premiers-pas/rss.xml"
category: "财务软件、Python 库、开发人员指南"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "开始使用 Python 银行对账单解析器：安装、解析 CAMT/PAIN.001/CSV/OFX/QFX/MT940 文件，并使用流式处理或 CLI 工作流程。"
item_guid: "https://bankstatementparser.com/zh/premiers-pas/rss.xml"
item_link: "https://bankstatementparser.com/zh/premiers-pas/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "银行对账单解析器：安装和使用指南"
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
apple-mobile-web-app-title: "银行对账单解析器：安装和使用指南"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "安装并使用银行对账单解析器在 Python 中解析 CAMT、PAIN.001、CSV、OFX/QFX 和 MT940 文件。"
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "银行对账单解析器的徽标，这是一款功能强大的 Python 工具，专为快速、准确的财务数据处理和见解提取而设计。"
twitter_site: "@wwdseb"
twitter_title: "银行对账单解析器：安装和使用指南"
twitter_url: "https://bankstatementparser.com/zh/premiers-pas/index.html"

# Humans.txt - The Humans.txt front matter (YAML).

author_website: "https://bankstatementparser.com"
author_twitter: "@wwdseb"
author_location: "London, UK"
thanks: "感谢您的阅读！"
site_last_updated: "2026-04-01"
site_standards: "HTML5, CSS3, RSS, Atom, JSON, XML, YAML, Markdown, TOML"
site_components: "Shokunin SSG, Shokunin CLI, Shokunin Templates, Shokunin Themes, Kaishi SSG, Kaishi CLI, Kaishi Templates, Kaishi Themes"
site_software: "Shokunin, Rust"

---

## 系统要求

- Python 3.10 至 3.14
- 终端访问（macOS、Linux 或 WSL）

## 安装

```bash
# 核心安装（仅确定性解析器）
pip install bankstatementparser
```

可选扩展，提供额外功能：

```bash
# 文本 LLM 路径，用于数字 PDF（litellm + pypdf）
pip install 'bankstatementparser[hybrid]'

# 更高精度的表格提取（添加 pdfplumber）
pip install 'bankstatementparser[hybrid-plus]'

# 视觉 LLM 路径，用于扫描 PDF（添加 pypdfium2）
pip install 'bankstatementparser[hybrid-vision]'

# LLM 驱动的交易分类
pip install 'bankstatementparser[enrichment]'

# REST API 微服务（FastAPI + uvicorn）
pip install 'bankstatementparser[api]'

# 可选 Polars DataFrame 支持
pip install 'bankstatementparser[polars]'
```

## 快速入门

### 自动检测并解析任意结构化格式

```python
from bankstatementparser import create_parser, detect_statement_format

fmt = detect_statement_format("transactions.ofx")
parser = create_parser("transactions.ofx", fmt)
df = parser.parse()  # pandas DataFrame
print(df.head())
```

支持 `.xml`（CAMT/PAIN.001）、`.csv`、`.ofx`、`.qfx`、`.mt940` 和 `.sta` 文件。

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

### 解析 PDF 银行对账单（混合管道）

混合管道智能地将 PDF 路由至三条提取路径：

```python
from bankstatementparser.hybrid import smart_ingest

result = smart_ingest("statement.pdf")
print(result.source_method)         # "deterministic" | "llm" | "vision"
print(result.verification.status)   # VERIFIED | DISCREPANCY | FAILED
print(result.transactions)          # List of extracted transactions
```

每次提取均通过**黄金法则**校验：`opening + credits − debits == closing`。

## 流式处理大文件

对于包含大量交易的文件，使用流式处理保持内存有界：

```python
parser = CamtParser("large_statement.xml")
for transaction in parser.parse_streaming(redact_pii=True):
    process(transaction)  # Memory stays constant
```

## 内存解析

从字节直接解析，无需磁盘 I/O——适用于 SFTP 或 API 工作流：

```python
xml_bytes = download_from_sftp()
parser = CamtParser.from_bytes(xml_bytes, source_name="daily.xml")
transactions = parser.parse()
```

## 并行文件处理

并发解析多个文件：

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

## 批量目录扫描

处理整个文件夹树，自动去重：

```python
from bankstatementparser.hybrid import scan_and_ingest

batch = scan_and_ingest("statements/2026/", pattern="**/*.pdf")
print(f"Processed: {len(batch.results)} files")
print(f"Unique transactions: {batch.unique_count}")
```

## 去重

幂等交易哈希，安全支持增量摄取：

```python
from bankstatementparser import CamtParser, Deduplicator

parser = CamtParser("statement.xml")
dedup = Deduplicator()
result = dedup.deduplicate(dedup.from_dataframe(parser.parse()))

print(f"Unique: {len(result.unique_transactions)}")
print(f"Exact duplicates: {len(result.exact_duplicates)}")
print(f"Suspected matches: {len(result.suspected_matches)}")
```

## 交易分类（智能分类）

使用 LLM 驱动的分类自动归类交易：

```python
from bankstatementparser.enrichment import Categorizer

categorizer = Categorizer()
enriched = categorizer.categorize_batch(transactions)
for txn in enriched:
    print(f"{txn.description}: {txn.category}")
```

## 账本导出（hledger / beancount）

将交易导出为纯文本记账日记账格式：

```python
from bankstatementparser.export import to_hledger, to_beancount

journal = to_hledger(transactions, account="Assets:Bank:Checking")
beancount_journal = to_beancount(transactions, account="Assets:Bank:Checking")
```

## 多币种余额校验

按币种分组独立校验余额：

```python
from bankstatementparser.hybrid import verify_balance_multi_currency

results = verify_balance_multi_currency(transactions)
for currency, verification in results.items():
    print(f"{currency}: {verification.status}")
```

## REST API

部署为 FastAPI 微服务：

```bash
# 启动 API 服务器
bankstatementparser-api --port 8000

# 容器部署
bankstatementparser-api --host 0.0.0.0 --port 9000
```

端点：
- `POST /ingest` -- 解析银行对账单文件
- `GET /health` -- 健康检查

## 安全 ZIP 处理

使用内置安全检查（炸弹防护、加密条目拒绝）处理压缩的 XML 文件：

```python
from bankstatementparser import iter_secure_xml_entries, CamtParser

for entry in iter_secure_xml_entries("statements.zip"):
    parser = CamtParser.from_bytes(entry.xml_bytes, source_name=entry.source_name)
    print(f"{entry.source_name}: {len(parser.parse())} transactions")
```

## 导出

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
# 解析结构化格式
bankstatementparser --type camt --input statement.xml
bankstatementparser --type pain001 --input payment.xml

# 混合 PDF 管道
bankstatementparser --type ingest --input statement.pdf
bankstatementparser --type ingest --input statement.pdf --output ledger.csv

# 交互式审查模式
bankstatementparser --type review --input result.json
bankstatementparser --type review --input result.json --output reviewed.json

# 导出为 CSV 并使用流式处理
bankstatementparser --type camt --input statement.xml --output transactions.csv
bankstatementparser --type camt --input statement.xml --streaming --show-pii
```

CLI 选项：

- `--type {camt,pain001,ingest,review}` -- 解析器类型或模式
- `--input <path>` -- 输入文件
- `--output <path>` -- 导出文件（CSV 或 JSON）
- `--streaming` -- 流式处理大文件
- `--show-pii` -- 显示敏感字段（默认已脱敏）
- `--max-size <MB>` -- 文件大小限制

## 本地开发设置

```bash
git clone https://github.com/sebastienrousseau/bankstatementparser.git
cd bankstatementparser
python3 -m venv .venv && source .venv/bin/activate
pip install poetry && poetry install --with dev
make install-hooks   # pre-commit hook runs `make verify` before every commit
```

运行测试套件：

```bash
pytest
```

## API 参考

### 解析器类

| 类 | 格式 | 导入 |
|---|---|---|
| `CamtParser` | CAMT.053 (ISO 20022) | `from bankstatementparser import CamtParser` |
| `Pain001Parser` | PAIN.001 (ISO 20022) | `from bankstatementparser import Pain001Parser` |
| `CsvStatementParser` | CSV | `from bankstatementparser import CsvStatementParser` |
| `OfxParser` | OFX | `from bankstatementparser import OfxParser` |
| `QfxParser` | QFX | `from bankstatementparser import QfxParser` |
| `Mt940Parser` | MT940 | `from bankstatementparser import Mt940Parser` |
| `smart_ingest()` | PDF（混合管道） | `from bankstatementparser.hybrid import smart_ingest` |

### 工具函数

| 函数 | 用途 |
|---|---|
| `detect_statement_format(path)` | 自动检测文件格式 |
| `create_parser(path, fmt)` | 创建对应解析器 |
| `parse_files_parallel(paths)` | 并发解析多个文件 |
| `iter_secure_xml_entries(zip_path)` | 安全迭代 ZIP 条目 |
| `smart_ingest(path)` | 混合 PDF 提取与校验 |
| `scan_and_ingest(dir, pattern)` | 批量目录扫描 |
| `verify_balance_multi_currency(txns)` | 按币种余额校验 |
| `to_hledger(txns, account)` | 导出为 hledger 日记账格式 |
| `to_beancount(txns, account)` | 导出为 beancount 日记账格式 |

### 数据类

| 类 | 用途 |
|---|---|
| `Deduplicator` | 检测重复交易 |
| `DeduplicationResult` | 包含唯一、精确重复和疑似匹配的结果 |
| `InputValidator` | 验证文件路径和格式 |
| `Transaction` | 标准化交易记录 |
| `FileResult` | 并行解析结果 |
| `ZipXMLSource` | ZIP 成员包装器 |
| `IngestResult` | 混合管道结果（含校验） |
| `VerificationResult` | 余额校验结果 |
| `Categorizer` | LLM 驱动的交易分类 |
| `AccountMapper` | 基于正则表达式的账户映射规则 |

### 异常

| 异常 | 触发场景 |
|---|---|
| `ParserError` | 解析失败 |
| `ExportError` | 导出失败（CSV/JSON/Excel） |
| `ValidationError` | 输入验证失败 |
| `ZipSecurityError` | ZIP 安全检查失败 |
