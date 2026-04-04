---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "关于银行对账单解析器：功能、格式和性能"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 银行对账单解析器。版权所有。"
date: "Apr 01, 2026"
description: "Bank Statement Parser 是一个开源 Python 库，用于将 CAMT.053、PAIN.001、CSV、OFX、QFX 和 MT940 解析为 pandas DataFrame。 100% 本地、PII 修订、27K+ tx/s。"
download: ""
format-detection: "telephone=no"
hreflang: "zh"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/zh/a-propos/index.html"
image_alt: "银行对账单解析器徽标，通过无缝数据提取增强您的财务分析能力"
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "银行对账单解析器 python、CAMT.053 解析器、PAIN.001 解析器、ISO 20022 python 库、MT9​​40 解析器、OFX QFX 解析器、开源银行解析器、本地财务数据处理、PII 编辑银行、MT940 到 CAMT 迁移"
language: "zh-CN"
layout: "about"
locale: "zh_CN"
logo_alt: "银行对账单解析器徽标，通过无缝数据提取增强您的财务分析能力"
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "关于银行对账单解析器"
permalink: "https://bankstatementparser.com/zh/a-propos/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "一个图书馆。六种格式。零网络调用。"
tags: "银行,报表,解析器,财务,python,camt,pain001,csv,ofx,qfx,mt940"
theme_color: "rgb(73, 214, 251)"
title: "关于银行对账单解析器：功能、格式和性能"
url: "https://bankstatementparser.com/zh/a-propos/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/zh/a-propos/rss.xml"
category: "财务软件、Python 库、数据处理"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Bank Statement Parser 是一个开源 Python 库，用于将 CAMT.053、PAIN.001、CSV、OFX、QFX 和 MT940 解析为 pandas DataFrame。 100% 本地、PII 修订、27K+ tx/s。"
item_guid: "https://bankstatementparser.com/zh/a-propos/rss.xml"
item_link: "https://bankstatementparser.com/zh/a-propos/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "关于银行对账单解析器：功能、格式和性能"
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
apple-mobile-web-app-title: "关于银行对账单解析器：功能、格式和性能"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "开源Python库：将CAMT.053、PAIN.001、CSV、OFX、QFX、MT940解析为DataFrame。 100% 本地、PII 修订、27K+ tx/s。"
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "银行对账单解析器徽标，通过无缝数据提取增强您的财务分析能力"
twitter_site: "@wwdseb"
twitter_title: "关于银行对账单解析器：6 种格式、27K+ tx/s、100% 本地"
twitter_url: "https://bankstatementparser.com/zh/a-propos/index.html"

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

**TL;DR:** 银行对账单解析器是一个开源 Python 库，可将六种银行对账单格式（CAMT.053、PAIN.001、CSV、OFX、QFX、MT940）解析为 pandas DataFrame。 100% local processing, PII redaction by default, 27K+ tx/s throughput.

银行对账单解析器是一个开源 Python 库，可将六种格式的银行对账单解析为结构化的 pandas DataFrame。所有处理都在本地进行——零网络调用、确定性输出和自动 PII 编辑。

## 这是给谁的？

- **财务团队**从 MT940 迁移到 CAMT.053，他们需要一个在过渡期间同时处理新旧格式的解析器。
- **金融科技开发人员** 构建对账、报告或会计管道，他们想要单个依赖项，而不是将 mt940 + ofxparse + 自定义 CSV 逻辑拼接在一起。
- **合规团队**，需要默认 PII 修订和审计就绪、确定性输出，从不将数据发送到外部服务。
- 当本地开源工具可以完成这项工作时，**任何人** 拒绝将敏感财务数据发送到第三方 SaaS。

## 支持的格式

| 格式 | 标准 | 文件类型 | 解析器类 |
|---|---|---|---|
| CAMT.053 | ISO 20022 银行对客户声明 | `.xml` | `CamtParser` |
| 疼痛.001 | ISO 20022 学分转移启动 | `.xml` | `Pain001Parser` |
| CSV | 通用银行出口 | `.csv` | `CsvStatementParser` |
| 氧氟沙星 | 开放金融交易所 | `.ofx` | `OfxParser` |
| QFX | 加快金融交流 | `.qfx` | `QfxParser` |
| MT940 | SWIFT标准 | `.mt940`, `.sta` | `Mt940Parser` |

所有格式都会生成具有一致列名的标准化 pandas DataFrame，从而使下游处理与格式无关。

## 关键能力

- **格式自动检测**：`detect_statement_format()`标识格式；`create_parser()`实例化正确的解析器。
- **流式解析**：使用有限内存处理大文件（50 MB+、50K+ 事务）`parse_streaming()`。
- **并行处理**：同时解析多个文件`parse_files_parallel()`使用 ProcessPoolExecutor。
- **重复数据删除**：通过可解释的置信度分数检测精确的重复项和可疑匹配项。
- **内存中解析**：`from_string()`和`from_bytes()`适用于无磁盘 I/O 的 SFTP 和 API 工作流程。
- **安全 ZIP 处理**：`iter_secure_xml_entries()`具有压缩比限制、条目大小上限和加密条目拒绝。
- **导出**：CSV、JSON、Excel（`.xlsx`）和可选的 Polars 数据帧。

## 安全和隐私

- **PII 修订**：默认情况下，CLI 输出中会屏蔽名称、IBAN 和地址。选择加入`--show-pii`。
- **XXE保护**：XML解析使用`resolve_entities=False`, `no_network=True`, `load_dtd=False`。
- **ZIP 炸弹保护**：压缩比限制（默认为 100:1）、条目大小上限 (10 MB)、加密条目拒绝。
- **路径遍历预防**：危险模式阻止列表和符号链接解析。
- **供应链安全**：SHA-256 哈希锁定依赖项、CycloneDX SBOM、构建来源证明。

＃＃ 表现

| 公制 | 价值 |
|---|---|
| CAMT.053吞吐量 | 27,000+ 笔交易/秒 |
| PAIN.001吞吐量 | 52,000+ 笔交易/秒 |
| 每事务延迟 (CAMT) | 37微秒 |
| 每笔交易延迟 (PAIN.001) | 19微秒 |
| 获得第一个结果的时间 | < 2 毫秒 |
| 内存扩展（1K-50K tx） | 恒定（流） |
| 测试覆盖率 | 100%分支机构覆盖 |
| 测试 | 29 个测试文件中有 467 个 |

## 开始构建

[开始安装和示例❯][01]

[01]：/getting-started/index.html“入门”
 “GitHub 存储库”
