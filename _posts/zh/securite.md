---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "银行对账单解析器安全性"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/corporate-finance.webp"
cdn: "https://cloudcdn.pro"
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 银行对账单解析器。版权所有。"
date: "Apr 01, 2026"
description: "银行对账单解析器的安全功能：XXE 保护、ZIP 炸弹强化、PII 编辑、供应链安全、确定性输出和签名版本。"
download: ""
format-detection: "telephone=no"
hreflang: "zh"
icon: "https://cloudcdn.pro/bankstatementparser/images/favicon.ico"
id: "https://bankstatementparser.com/zh/securite/index.html"
image_alt: "银行对账单解析器徽标，通过无缝数据提取增强您的财务分析能力"
image_height: "630"
image_width: "1200"
image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
keywords: "银行对账单安全、PII 编辑 Python、XXE 保护、ZIP 炸弹保护、供应链安全 SBOM、确定性解析、金融数据安全"
language: "zh-CN"
layout: "about"
locale: "zh_CN"
logo_alt: "银行对账单解析器徽标，通过无缝数据提取增强您的财务分析能力"
logo_height: "44"
logo_width: "44"
logo: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "安全"
permalink: "https://bankstatementparser.com/zh/securite/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "我们如何保护您的财务数据"
tags: "安全、pii、xxe、sbom、供应链、确定性"
theme_color: "rgb(73, 214, 251)"
title: "银行对账单解析器安全性：数据保护和供应链"
url: "https://bankstatementparser.com/zh/securite/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/zh/securite/rss.xml"
category: "财务软件、Python 库、数据处理"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "银行对账单解析器的安全功能：XXE 保护、ZIP 炸弹强化、PII 编辑、供应链安全、确定性输出和签名版本。"
item_guid: "https://bankstatementparser.com/zh/securite/rss.xml"
item_link: "https://bankstatementparser.com/zh/securite/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "银行对账单解析器安全性：数据保护和供应链"
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
apple-mobile-web-app-title: "银行对账单解析器安全性：数据保护和供应链"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "银行对账单解析器的安全功能：XXE 保护、ZIP 炸弹强化、PII 编辑、供应链安全、确定性输出和签名版本。"
twitter_image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
twitter_image_alt: "银行对账单解析器徽标，通过无缝数据提取增强您的财务分析能力"
twitter_site: "@wwdseb"
twitter_title: "银行对账单解析器安全性：数据保护和供应链"
twitter_url: "https://bankstatementparser.com/zh/securite/index.html"

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

**TL;DR:** 银行对账单解析器进行零网络调用，默认情况下编辑 PII，针对 XXE 攻击强化 XML 解析，并附带 SHA-256 哈希锁定依赖项和 CycloneDX SBOM。

## 设计安全

银行对账单解析器专为处理敏感的财务数据而构建。每个设计决策都会优先考虑安全性、隐私性和可审核性。

## 零网络访问

所有处理都在运行时本地进行。该库进行零 API 调用、零云连接并收集零遥测数据。 XML 解析器显式配置为`no_network=True`, `resolve_entities=False`， 和`load_dtd=False`以防止任何出站访问。

## PII 编辑

个人身份信息（姓名、IBAN、邮政地址）会在 CLI 输出和流模式下自动编辑。默认情况下此功能处于启用状态。

- **CLI**：敏感字段显示为`***REDACTED***`
- **流媒体**：`parse_streaming(redact_pii=True)`（默认）
- **导出**：CSV/JSON/Excel 保留完整数据以供下游处理
- **选择加入**：使用`--show-pii`或者`redact_pii=False`当您需要未编辑的输出时

## XML 安全性（XXE 保护）

所有 XML 解析都使用`lxml`具有强化设置：

- `resolve_entities=False`-- 防止XML实体扩展攻击
-`no_network=True`-- 阻止解析器的所有出站网络访问
-`load_dtd=False`-- 防止基于 DTD 的攻击
- 处理前命名空间剥离——安全处理任何 CAMT.053 变体

## ZIP 存档安全

`iter_secure_xml_entries()`在提取之前验证每个 ZIP 成员：

- **条目大小上限**：每个条目 10 MB（可配置）
- **总大小上限**：未压缩总计 50 MB（可配置）
- **压缩比限制**：默认为 100:1 -- 检测 ZIP 炸弹
- **加密条目拒绝**：跳过加密条目并发出警告
- **无磁盘写入**：XML 字节通过直接传递到解析器`from_bytes()`

## 路径遍历预防

输入验证阻止危险文件路径：

- 空字节，目录遍历模式（`../`)，并且符号链接被拒绝
- 针对预期格式的文件扩展名验证
- 文件大小限制（默认 100 MB，可配置）

## 确定性输出

给定相同的输入文件，解析器每次运行都会生成字节相同的输出。没有随机性，没有模型推理，没有启发式采样。这对于以下方面至关重要：

- **审核重现性**：运行同一文件两次并比较输出
- **法规遵从性**：展示一致的处理
- **CI 验证**：467 项测试强制执行确定性，分支覆盖率为 100%

## 供应链安全

- **SHA-256 哈希锁定依赖项**：中的每个包`poetry.lock`已验证文件哈希值
- **CycloneDX SBOM**：每个版本都包含软件物料清单
- **GitHub 构建来源**：证明将每个工件链接到其源提交
- **签名提交**：所有提交均经过 SSH 签名并在 CI 中进行验证
- **依赖关系验证**：`scripts/verify_locked_hashes.py`在本地验证所有哈希值

## 本地验证

```bash
python -m pytest                          # 467 tests, 100% branch coverage
python scripts/verify_locked_hashes.py    # SHA-256 hash verification
git log --show-signature -1               # Verify commit signature
```
