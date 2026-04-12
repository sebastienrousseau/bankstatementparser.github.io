---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "银行对账单解析器安全性"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 银行对账单解析器。版权所有。"
date: "Apr 11, 2026"
description: "银行对账单解析器的安全功能：XXE 保护、ZIP 炸弹强化、PII 编辑、供应链安全、确定性输出和签名版本。"
download: ""
format-detection: "telephone=no"
hreflang: "zh"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/zh/securite/index.html"
image_alt: "银行对账单解析器徽标，通过无缝数据提取增强您的财务分析能力"
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "银行对账单安全、PII 编辑 Python、XXE 保护、ZIP 炸弹保护、供应链安全 SBOM、确定性解析、金融数据安全"
language: "zh-CN"
layout: "about"
locale: "zh_CN"
logo_alt: "银行对账单解析器徽标，通过无缝数据提取增强您的财务分析能力"
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
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
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "银行对账单解析器的安全功能：XXE 保护、ZIP 炸弹强化、PII 编辑、供应链安全、确定性输出和签名版本。"
twitter_image: "/images/logos/bankstatementparser.webp"
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

**简述：** Bank Statement Parser 在本地处理所有数据，默认脱敏 PII，加固 XML 解析以防御 XXE 攻击，通过 Ollama 在本地运行 LLM，并附带 SHA-256 哈希锁定依赖和 CycloneDX SBOM。

## 安全设计

Bank Statement Parser 专为处理敏感财务数据而构建。每个设计决策都优先考虑安全性、隐私性和可审计性。

## 零云端依赖

所有处理在本地运行时中进行。确定性解析器不发起任何网络调用。混合 PDF 管道使用 Ollama 进行本地 LLM 推理——不向云端 API 发送数据。XML 解析器显式配置为 `no_network=True`、`resolve_entities=False` 和 `load_dtd=False`，以防止任何出站访问。

## PII 脱敏

个人身份信息（姓名、IBAN、邮政地址）在 CLI 输出和流模式下自动脱敏。默认开启。

- **CLI**：敏感字段显示为 `***REDACTED***`
- **流式处理**：`parse_streaming(redact_pii=True)`（默认）
- **导出**：CSV/JSON/Excel 保留完整数据以供下游处理
- **选择显示**：需要未脱敏输出时使用 `--show-pii` 或 `redact_pii=False`

## XML 安全（XXE 防护）

所有 XML 解析使用带加固设置的 `lxml`：

- `resolve_entities=False` -- 防止 XML 实体扩展攻击
- `no_network=True` -- 阻止解析器的所有出站网络访问
- `load_dtd=False` -- 防止基于 DTD 的攻击
- 处理前剥离命名空间——安全处理任何 CAMT.053 变体

## ZIP 归档安全

`iter_secure_xml_entries()` 在提取前验证每个 ZIP 成员：

- **条目大小上限**：每个条目 10 MB（可配置）
- **总大小上限**：未压缩总计 50 MB（可配置）
- **压缩比限制**：默认 100:1——检测 ZIP 炸弹
- **加密条目拒绝**：跳过加密条目并发出警告
- **无磁盘写入**：XML 字节通过 `from_bytes()` 直接传递给解析器

## 路径遍历防护

输入验证阻止危险文件路径：

- 空字节、目录遍历模式（`../`）和符号链接均被拒绝
- 文件扩展名按预期格式验证
- 文件大小限制（默认 100 MB，可配置）

## 余额校验（黄金法则）

每次 PDF 提取均通过以下等式验证：`期初余额 + 贷方 − 借方 == 期末余额`。结果标记为 VERIFIED、DISCREPANCY 或 FAILED。差异可通过 `--type review` 进行交互式审查。

## 确定性输出

对于结构化格式（CAMT、PAIN.001、CSV、OFX、QFX、MT940），给定相同的输入文件，解析器每次运行产生字节一致的输出。无随机性，无模型推理，无启发式采样。这对以下方面至关重要：

- **审计可重现性**：运行同一文件两次并对比输出
- **监管合规**：证明处理一致性
- **CI 验证**：718 项测试强制确保确定性，100% 分支覆盖率

## 供应链安全

- **SHA-256 哈希锁定依赖**：`poetry.lock` 中的每个包均有已验证的文件哈希
- **CycloneDX SBOM**：每个版本包含软件物料清单
- **GitHub 构建来源**：证明将每个构件链接到其源提交
- **签名提交**：所有提交均经 SSH 签名并在 CI 中验证
- **依赖验证**：`scripts/verify_locked_hashes.py` 在本地验证所有哈希

## 本地验证

```bash
python -m pytest                          # 718 tests, 100% branch coverage
python scripts/verify_locked_hashes.py    # SHA-256 hash verification
git log --show-signature -1               # Verify commit signature
```
