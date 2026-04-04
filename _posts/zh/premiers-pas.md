---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "白色的建筑，黑色的窗户"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/daniele-franchi-Vl6YuVBLEys.webp"
cdn: "https://cloudcdn.pro"
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 银行对账单解析器。版权所有。"
date: "Apr 01, 2026"
description: "开始使用 Python 银行对账单解析器：安装、解析 CAMT/PAIN.001/CSV/OFX/QFX/MT940 文件，并使用流式处理或 CLI 工作流程。"
download: ""
format-detection: "telephone=no"
hreflang: "zh"
icon: "https://cloudcdn.pro/bankstatementparser/images/favicon.ico"
id: "https://bankstatementparser.com/zh/premiers-pas/index.html"
image_alt: "银行对账单解析器的徽标，这是一款功能强大的 Python 工具，专为快速、准确的财务数据处理和见解提取而设计。"
image_height: "630"
image_width: "1200"
image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
keywords: "银行对账单解析器、入门、python、CAMT、PAIN.001、CSV、OFX、QFX、MT940、财务数据"
language: "zh-CN"
layout: "start"
locale: "zh_CN"
logo_alt: "银行对账单解析器的徽标，这是一款功能强大的 Python 工具，专为快速、准确的财务数据处理和见解提取而设计。"
logo_height: "44"
logo_width: "44"
logo: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
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
msapplication_tile_image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "安装并使用银行对账单解析器在 Python 中解析 CAMT、PAIN.001、CSV、OFX/QFX 和 MT940 文件。"
twitter_image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
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

＃＃ 要求

- Python 3.9 至 3.14
- 终端访问（macOS、Linux 或 WSL）

＃＃ 安装

```bash
pip install bankstatementparser
```

对于 Polars DataFrame 支持：

```bash
pip install bankstatementparser[polars]
```

## 快速入门

### 自动检测和解析任何格式

```python
from bankstatementparser import create_parser, detect_statement_format

fmt = detect_statement_format("transactions.ofx")
parser = create_parser("transactions.ofx", fmt)
df = parser.parse()  # pandas DataFrame
print(df.head())
```

这适用于`.xml`(CAMT/PAIN.001),`.csv`, `.ofx`, `.qfx`, `.mt940`， 和`.sta`文件。

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

## 流式传输大文件

对于具有数千个事务的文件，请使用流式传输来限制内存：

```python
parser = CamtParser("large_statement.xml")
for transaction in parser.parse_streaming(redact_pii=True):
    process(transaction)  # Memory stays constant
```

## 内存中解析

在没有磁盘 I/O 的情况下从字节进行解析——对于 SFTP 或 API 工作流程很有用：

```python
xml_bytes = download_from_sftp()
parser = CamtParser.from_bytes(xml_bytes, source_name="daily.xml")
transactions = parser.parse()
```

## 并行文件处理

同时解析多个文件：

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

## 重复数据删除

通过置信度分数检测精确的重复项和可疑匹配项：

```python
from bankstatementparser import CamtParser, Deduplicator

parser = CamtParser("statement.xml")
dedup = Deduplicator()
result = dedup.deduplicate(dedup.from_dataframe(parser.parse()))

print(f"Unique: {len(result.unique_transactions)}")
print(f"Exact duplicates: {len(result.exact_duplicates)}")
print(f"Suspected matches: {len(result.suspected_matches)}")
```

## 安全 ZIP 处理

使用内置安全检查（炸弹防护、加密条目拒绝）处理压缩的 XML 文件：

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

CLI 选项：

- `--type {camt,pain001}`-- 解析器类型
-`--input <path>`-- 输入文件
-`--output <csv_path>`-- 导出为 CSV
-`--streaming`-- 流式传输大文件
-`--show-pii`-- 显示敏感字段（默认情况下已编辑）
-`--max-size <MB>`-- 文件大小限制

## 本地开发设置

```bash
git clone https://github.com/sebastienrousseau/bankstatementparser.git
cd bankstatementparser
python3 -m venv .venv && source .venv/bin/activate
pip install poetry && poetry install --with dev
```

运行测试套件：

```bash
pytest
```

## API 参考

### 解析器类

| 班级 | 格式 | 进口 |
|---|---|---|
| `CamtParser` | CAMT.053 (ISO 20022) | `from bankstatementparser import CamtParser` |
| `Pain001Parser` | PAIN.001 (ISO 20022) | `from bankstatementparser import Pain001Parser` |
| `CsvStatementParser` | CSV | `from bankstatementparser import CsvStatementParser` |
| `OfxParser` | 氧氟沙星 | `from bankstatementparser import OfxParser` |
| `QfxParser` | QFX | `from bankstatementparser import QfxParser` |
| `Mt940Parser` | MT940 | `from bankstatementparser import Mt940Parser` |

### 实用函数

| 功能 | 目的 |
|---|---|
| `detect_statement_format(path)` | 自动检测文件格式 |
| `create_parser(path, fmt)` | 创建适当的解析器 |
| `parse_files_parallel(paths)` | 同时解析多个文件 |
| `iter_secure_xml_entries(zip_path)` | 安全地迭代 ZIP 条目 |

### 数据类

| 班级 | 目的 |
|---|---|
| `Deduplicator` | 检测重复交易 |
| `DeduplicationResult` | 具有唯一、精确和可疑匹配的结果 |
| `InputValidator` | 验证文件路径和格式 |
| `Transaction` | 规范化交易记录 |
| `FileResult` | 并行解析的结果 |
| `ZipXMLSource` | ZIP 成员包装 |

### 例外情况

| 例外 | 升起时 |
|---|---|
| `ParserError` | 解析失败 |
| `ExportError` | 导出失败（CSV/JSON/Excel） |
| `ValidationError` | 输入验证失败 |
| `ZipSecurityError` | ZIP 安全检查失败 |
