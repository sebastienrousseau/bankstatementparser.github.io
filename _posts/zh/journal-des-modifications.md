---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "银行对账单解析器变更日志"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/corporate-finance.webp"
cdn: "https://cloudcdn.pro"
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 银行对账单解析器。版权所有。"
date: "Apr 01, 2026"
description: "银行对账单解析器的发布历史记录和变更日志。跟踪所有版本的新功能、改进和错误修复。"
download: ""
format-detection: "telephone=no"
hreflang: "zh"
icon: "https://cloudcdn.pro/bankstatementparser/images/favicon.ico"
id: "https://bankstatementparser.com/zh/journal-des-modifications/index.html"
image_alt: "银行对账单解析器徽标，通过无缝数据提取增强您的财务分析能力"
image_height: "630"
image_width: "1200"
image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
keywords: "银行对账单解析器变更日志、发行说明、版本历史记录、更新"
language: "zh-CN"
layout: "about"
locale: "zh_CN"
logo_alt: "银行对账单解析器徽标，通过无缝数据提取增强您的财务分析能力"
logo_height: "44"
logo_width: "44"
logo: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "变更日志"
permalink: "https://bankstatementparser.com/zh/journal-des-modifications/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "发布历史和新增内容"
tags: "变更日志、发布、更新、版本、公告、博客"
theme_color: "rgb(73, 214, 251)"
title: "银行对账单解析器变更日志"
url: "https://bankstatementparser.com/zh/journal-des-modifications/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/zh/journal-des-modifications/rss.xml"
category: "财务软件、Python 库、数据处理"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "银行对账单解析器的发布历史记录和变更日志。跟踪所有版本的新功能、改进和错误修复。"
item_guid: "https://bankstatementparser.com/zh/journal-des-modifications/rss.xml"
item_link: "https://bankstatementparser.com/zh/journal-des-modifications/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "银行对账单解析器变更日志"
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
apple-mobile-web-app-title: "银行对账单解析器变更日志"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "银行对账单解析器的发布历史记录和变更日志。跟踪所有版本的新功能、改进和错误修复。"
twitter_image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
twitter_image_alt: "银行对账单解析器徽标，通过无缝数据提取增强您的财务分析能力"
twitter_site: "@wwdseb"
twitter_title: "银行对账单解析器变更日志"
twitter_url: "https://bankstatementparser.com/zh/journal-des-modifications/index.html"

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

关注银行对账单解析器的开发。通过 [RSS](/changelog/rss.xml) 订阅或观看 [GitHub 存储库](https://github.com/sebastienrousseau/bankstatementparser) 用于发布通知。

## v0.0.4 — 2026-03-15（最新）

- 添加了并行文件解析`parse_files_parallel()`使用 ProcessPoolExecutor。
- 为具有有限内存的大型 PAIN.001 文件 (50 MB+) 添加了真正的流式传输。
- 性能优化：CAMT 吞吐量现已超过 27,000 tx/s，PAIN.001 超过 52,000 tx/s。
- 添加`Deduplicator`用于检测精确重复项和与置信度分数的可疑匹配的类。
- 添加`from_string()`和`from_bytes()`无需磁盘 I/O 的内存解析方法。
- 添加`iter_secure_xml_entries()`用于安全的 ZIP 存档处理。
- 具有性能阈值强制执行的扩展 CI。

## v0.0.3 — 2025-11-20

- 添加了 CSV、OFX、QFX 和 MT940 解析器支持。
- 添加了格式自动检测`detect_statement_format()`和`create_parser()`。
- 添加了 PII 编辑（在 CLI 和流模式下默认启用）。
- 添加了 CSV、JSON 和 Excel 的导出帮助程序。
- 添加了可选的 Polars DataFrame 支持。
- 将测试套件扩展至 467 个测试，分支覆盖率为 100%。

## v0.0.2 — 2025-06-10

- 添加了 PAIN.001 解析器（`Pain001Parser`) 用于 ISO 20022 学分转移启动文件。
- 添加了 CLI 界面（`python -m bankstatementparser.cli`）。
- 添加了流媒体模式`parse_streaming()`。
- 添加了输入验证和文件大小限制。

## v0.0.1 — 2025-01-15

- 初始版本。
- CAMT.053 解析器（`CamtParser`) 适用于 ISO 20022 银行对客户报表。
- 大熊猫数据帧输出。
- 基本 XML 安全强化（XXE 保护、no_network）。

在 [GitHub]( 上查看完整的提交历史记录https://github.com/sebastienrousseau/bankstatementparser/commits/main).

<脚本类型=“应用程序/ld+json”>
{
  “@上下文”：“https://schema.org“，
  "@type": "软件应用程序",
  "name": "银行对账单解析器",
  "applicationCategory": "开发者应用程序",
  "operatingSystem": "跨平台",
  "软件版本": "0.0.4",
  "发布日期": "2026-03-15",
  "releaseNotes": "添加了并行文件解析、PAIN.001 的真正流式传输、性能优化（27K+ tx/s CAMT、52K+ tx/s PAIN.001）、重复数据删除器类、内存中解析、安全 ZIP 处理。",
  “下载地址”：“https://pypi.org/project/bankstatementparser/“，
  “执照”： ”https://opensource.org/licenses/Apache-2.0“，
  “作者”：{
    "@type": "人",
    “姓名”：“塞巴斯蒂安·卢梭”
  }
}
</脚本>
