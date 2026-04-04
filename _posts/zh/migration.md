---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "ISO 20022 迁移指南"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 银行对账单解析器。版权所有。"
date: "Apr 01, 2026"
description: "有关 SWIFT ISO 20022 迁移时间表 (2026-2028)、MT940 到 CAMT.053 过渡以及银行对账单解析器如何帮助财务团队迁移的实用指南。"
download: ""
format-detection: "telephone=no"
hreflang: "zh"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/zh/migration/index.html"
image_alt: "银行对账单解析器徽标，通过无缝数据提取增强您的财务分析能力"
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "ISO 20022 迁移、MT940 到 CAMT.053、SWIFT 截止日期 2027 年、MT940 2028 年停用、银行对账单迁移 python、CAMT.053 解析器、ISO 20022 时间表"
language: "zh-CN"
layout: "about"
locale: "zh_CN"
logo_alt: "银行对账单解析器徽标，通过无缝数据提取增强您的财务分析能力"
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "ISO 20022 迁移指南"
permalink: "https://bankstatementparser.com/zh/migration/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "引导 SWIFT MT 向 ISO 20022 过渡"
tags: "ISO20022、迁移、mt940、camt053、swift、时间线"
theme_color: "rgb(73, 214, 251)"
title: "ISO 20022 迁移指南：MT940 到 CAMT.053 过渡"
url: "https://bankstatementparser.com/zh/migration/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/zh/migration/rss.xml"
category: "财务软件、Python 库、数据处理"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "有关 SWIFT ISO 20022 迁移时间表 (2026-2028)、MT940 到 CAMT.053 过渡以及银行对账单解析器如何帮助财务团队迁移的实用指南。"
item_guid: "https://bankstatementparser.com/zh/migration/rss.xml"
item_link: "https://bankstatementparser.com/zh/migration/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "ISO 20022 迁移指南：MT940 到 CAMT.053 过渡"
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
apple-mobile-web-app-title: "ISO 20022 迁移指南：MT940 到 CAMT.053 过渡"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "有关 SWIFT ISO 20022 迁移时间表 (2026-2028)、MT940 到 CAMT.053 过渡以及银行对账单解析器如何帮助财务团队迁移的实用指南。"
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "银行对账单解析器徽标，通过无缝数据提取增强您的财务分析能力"
twitter_site: "@wwdseb"
twitter_title: "ISO 20022 迁移指南：MT940 到 CAMT.053 过渡"
twitter_url: "https://bankstatementparser.com/zh/migration/index.html"

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

**TL;DR：** SWIFT 将在 2028 年 11 月之前停用 MT940。银行对账单解析器使用单个 API 处理 MT940 和 CAMT.053，因此您的解析管道在过渡期间和之后都可以正常工作。

## 为什么这次迁移很重要

SWIFT 正在淘汰传统的 MT 报文格式，转而采用更丰富的 ISO 20022 标准。对于财务和财务团队来说，这意味着您的银行对账单处理流程必须在严格的截止日期之前从 MT940 发展到 CAMT.053。

## SWIFT 迁移时间表

| 日期 | 里程碑 | 影响 |
|---|---|---|
| **2025 年 11 月** | 跨境支付 MT 与 MX 共存结束 | PACS 消息现在仅限 ISO 20022 |
| **2026 年 11 月** | 结构化/混合地址强制； MT101多指令被拒绝；案例管理第一阶段 | 地址格式必须符合；部分MT消息会被拒绝 |
| **2026 年末** | 开始选择接收 CAMT.052/.053/.054 | 金融机构可以开始接收本地 ISO 声明 |
| **2027 年 11 月** | 所有金融机构必须本地接收 CAMT.053 | SWIFT 停止将 MT 格式转换为 ISO；您的系统必须直接解析 CAMT |
| **2028 年 11 月** | MT940/MT942/MT950/MT900/MT910全面退役 | 旧的报表格式不再可用； CAMT.052/.053/.054 是唯一的选择 |

## 您的代码有何变化

### 之前：仅限 MT940

```python
from bankstatementparser import Mt940Parser

parser = Mt940Parser("statement.mt940")
df = parser.parse()
```

### 之后：两种格式均具有自动检测功能

```python
from bankstatementparser import create_parser, detect_statement_format

fmt = detect_statement_format("statement.xml")  # or .mt940
parser = create_parser("statement.xml", fmt)
df = parser.parse()  # Same DataFrame schema regardless of format
```

这`detect_statement_format()`函数识别文件是否为 MT940、CAMT.053、PAIN.001 或任何其他支持的格式。这`create_parser()`函数返回正确的解析器。无论源格式如何，下游代码的工作方式都是相同的。

## CAMT.053 与 MT940：主要区别

| 特征 | MT940 | CAMT.053 |
|---|---|---|
| 数据丰富度 | 领域有限 | 每笔交易的数据量增加 3-5 倍 |
| 字符集 | 有限（SWIFT 字符集） | 完整的统一码 |
| 结构 | 带标签的平面文本 | 带有命名空间的 XML |
| 余额报告 | 仅打开/关闭 | 多种余额类型 |
| 参考 | 单一参考字段 | 多种参考类型 |
| 货币处理 | 基本的 | 完整的多币种和汇率 |

## 银行对账单解析器如何提供帮助

- **统一 API**：使用相同的方法解析 MT940 和 CAMT.053`parse()`方法，生成相同的 DataFrame 模式。
- **自动检测**：无需提前知道格式。`detect_statement_format()`自动识别它。
- **与命名空间无关**：无需配置即可处理任何 CAMT.053 变体（001.02、001.04 或银行特定的包装器）。
- **流式处理**：使用有限内存处理大型 CAMT 文件（50 MB+、50K+ 事务）。
- **迁移测试**：在同一日期范围内并行运行两个解析器，以在切换之前验证输出一致性。

＃＃ 入门

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

[阅读完整文档](/getting-started/index.html)

[与替代方案比较❯](/comparison/index.html) | [查看真实用例❯](/use-cases/index.html)
