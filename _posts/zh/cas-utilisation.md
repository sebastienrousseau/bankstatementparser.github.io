---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "银行对账单解析器用例"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 银行对账单解析器。版权所有。"
date: "Apr 11, 2026"
description: "财务团队、金融科技开发人员和合规官员如何使用银行对账单解析器进行 MT940 到 CAMT 的迁移、对账、审计管道和多银行整合。"
download: ""
format-detection: "telephone=no"
hreflang: "zh"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/zh/cas-utilisation/index.html"
image_alt: "银行对账单解析器徽标，通过无缝数据提取增强您的财务分析能力"
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "银行对账单用例、财务 MT940 迁移、银行对账 Python、合规审计管道、多银行合并、SFTP 银行对账单处理"
language: "zh-CN"
layout: "about"
locale: "zh_CN"
logo_alt: "银行对账单解析器徽标，通过无缝数据提取增强您的财务分析能力"
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "使用案例"
permalink: "https://bankstatementparser.com/zh/cas-utilisation/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "实际应用"
tags: "用例、财务、对账、合规性、迁移"
theme_color: "rgb(73, 214, 251)"
title: "银行对账单解析器用例：财务、对账和合规性"
url: "https://bankstatementparser.com/zh/cas-utilisation/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/zh/cas-utilisation/rss.xml"
category: "财务软件、Python 库、数据处理"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "财务团队、金融科技开发人员和合规官员如何使用银行对账单解析器进行 MT940 到 CAMT 的迁移、对账、审计管道和多银行整合。"
item_guid: "https://bankstatementparser.com/zh/cas-utilisation/rss.xml"
item_link: "https://bankstatementparser.com/zh/cas-utilisation/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "银行对账单解析器用例：财务、对账和合规性"
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
apple-mobile-web-app-title: "银行对账单解析器用例：财务、对账和合规性"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "财务团队、金融科技开发人员和合规官员如何使用银行对账单解析器进行 MT940 到 CAMT 的迁移、对账、审计管道和多银行整合。"
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "银行对账单解析器徽标，通过无缝数据提取增强您的财务分析能力"
twitter_site: "@wwdseb"
twitter_title: "银行对账单解析器用例：财务、对账和合规性"
twitter_url: "https://bankstatementparser.com/zh/cas-utilisation/index.html"

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

Bank Statement Parser 处理真实的金融工作流：PDF 银行对账单摄取、MT940 到 CAMT 迁移、带余额校验的自动对账、合规管道、纯文本记账导出、REST API 部署、批量扫描和多银行合并。

## PDF 银行对账单摄取

**效果：** 解析数字和扫描的 PDF 银行对账单，自动余额校验——无需云端 API，数据不会离开您的机器。

混合 PDF 管道将每个 PDF 路由至最优提取路径，并验证每次结果。

```python
from bankstatementparser.hybrid import smart_ingest

result = smart_ingest("statement.pdf")
print(result.source_method)         # "deterministic" | "llm" | "vision"
print(result.verification.status)   # VERIFIED | DISCREPANCY | FAILED

# Review discrepancies interactively
# bankstatementparser --type review --input result.json
```

## 批量对账单处理

**效果：** 单次调用即可扫描整个文件夹树（数百个 PDF、XML、CSV），自动跨文件去重。

```python
from bankstatementparser.hybrid import scan_and_ingest

batch = scan_and_ingest("statements/2026/", pattern="**/*.pdf")
print(f"Files: {len(batch.results)}, Unique txns: {batch.unique_count}")
```

## 资金管理：MT940 到 CAMT.053 迁移

**效果：** 在 SWIFT 迁移窗口（2025 年 11 月至 2028 年 11 月）期间，单次 API 调用即可处理 MT940 和 CAMT.053，无需维护单独的解析管道。

全球资金管理团队正在 2027 年 11 月 SWIFT 截止日期前从 MT940 迁移到 CAMT.053。Bank Statement Parser 使用单一 API 处理两种格式，实现无缝过渡。

```python
from bankstatementparser import create_parser, detect_statement_format

# Process both MT940 and CAMT.053 with the same code
for file in daily_statement_files:
    fmt = detect_statement_format(file)
    parser = create_parser(file, fmt)
    df = parser.parse()
    load_to_treasury_system(df)
```

## 带余额校验的自动对账

**效果：** 格式无关的 DataFrame 配合黄金法则校验和去重，在错误和重复项到达账本之前即予以捕获。

自动解析银行对账单、校验余额并与内部记录匹配。

```python
from bankstatementparser import CamtParser, Deduplicator
from bankstatementparser.hybrid import verify_balance_multi_currency

parser = CamtParser("bank_statement.xml")
bank_txns = parser.parse()

# Verify balances per currency
verification = verify_balance_multi_currency(bank_txns)
for ccy, result in verification.items():
    assert result.status == "VERIFIED", f"{ccy} balance mismatch!"

# Deduplicate before reconciliation
dedup = Deduplicator()
result = dedup.deduplicate(dedup.from_dataframe(bank_txns))
clean_txns = result.unique_transactions

# Match against internal records
unmatched = reconcile(clean_txns, internal_ledger)
```

## 纯文本记账（hledger / beancount）

**效果：** 自动摄取 PDF 银行对账单，导出分类后的交易到 hledger 或 beancount 日记账格式。

```python
from bankstatementparser.hybrid import smart_ingest
from bankstatementparser.enrichment import Categorizer
from bankstatementparser.export import to_hledger

result = smart_ingest("statement.pdf")
categorizer = Categorizer()
enriched = categorizer.categorize_batch(result.transactions)
journal = to_hledger(enriched, account="Assets:Bank:Checking")
```

## REST API 部署

**效果：** 将 Bank Statement Parser 部署为微服务，通过 HTTP 接收对账单文件并返回结构化 JSON。

```bash
# Start the API server
bankstatementparser-api --port 8000
```

```bash
# Ingest a statement
curl -X POST http://localhost:8000/ingest \
  -F "file=@statement.pdf"
```

## 合规与审计管道

**效果：** 确定性输出、自动 PII 脱敏和黄金法则校验，生成满足监管可重复性要求的审计就绪日志。

```python
from bankstatementparser import CamtParser

parser = CamtParser("statement.xml")

# Stream with PII redacted for audit logs
for txn in parser.parse_streaming(redact_pii=True):
    audit_log.write(txn)

# Export full data for secure internal processing
parser.export_csv("archive/statement.csv")
```

## SFTP 到 DataFrame 工作流

**效果：** 直接从字节解析，零磁盘 I/O，原生适配 SFTP 和 API 驱动的银行连接工作流。

```python
from bankstatementparser import CamtParser

xml_bytes = sftp_client.read("daily_statement.xml")
parser = CamtParser.from_bytes(xml_bytes, source_name="daily.xml")
df = parser.parse()
```

## 多银行合并

**效果：** 并行解析 HSBC（CAMT）、Barclays（MT940）、Revolut（CSV）、Wise（OFX）和 Chase（PDF），生成单一标准化数据集。

```python
from bankstatementparser import parse_files_parallel

results = parse_files_parallel([
    "hsbc/camt053.xml",
    "barclays/mt940.sta",
    "revolut/transactions.csv",
    "wise/statement.ofx",
])

all_transactions = pd.concat([r.transactions for r in results if r.status == "success"])
```

## 使用 ZIP 档案批处理

**效果：** 内置 ZIP 炸弹防护（100:1 压缩比限制、10 MB 条目上限、加密条目拒绝），安全处理月度对账单归档。

```python
from bankstatementparser import iter_secure_xml_entries, CamtParser

for entry in iter_secure_xml_entries("monthly_statements.zip"):
    parser = CamtParser.from_bytes(entry.xml_bytes, source_name=entry.source_name)
    df = parser.parse()
    save_to_warehouse(entry.source_name, df)
```

[与替代方案比较 ❯](/comparison/index.html) | [规划 ISO 20022 迁移 ❯](/migration/index.html) | [开始使用 ❯](/getting-started/index.html)
