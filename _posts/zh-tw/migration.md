---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "ISO 20022 遷移指南"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 銀行對帳單解析器。版權所有。"
date: "Apr 11, 2026"
description: "有關 SWIFT ISO 20022 遷移時間表 (2026-2028)、MT940 到 CAMT.053 過渡以及銀行對帳單解析器如何幫助財務團隊遷移的實用指南。"
download: ""
format-detection: "telephone=no"
hreflang: "zh-tw"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/zh-tw/migration/index.html"
image_alt: "銀行對帳單解析器徽標，透過無縫資料提取增強您的財務分析能力"
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "ISO 20022 遷移、MT940 至 CAMT.053、SWIFT 截止日期 2027 年、MT940 2028 年停用、銀行對帳單遷移 python、CAMT.053 解析器、ISO 20022 時間表"
language: "zh-TW"
layout: "about"
locale: "zh_TW"
logo_alt: "銀行對帳單解析器徽標，透過無縫資料提取增強您的財務分析能力"
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "ISO 20022 遷移指南"
permalink: "https://bankstatementparser.com/zh-tw/migration/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "引導 SWIFT MT 向 ISO 20022 過渡"
tags: "ISO20022、遷移、mt940、camt053、swift、時間軸"
theme_color: "rgb(73, 214, 251)"
title: "ISO 20022 遷移指南：MT940 到 CAMT.053 過渡"
url: "https://bankstatementparser.com/zh-tw/migration/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/zh-tw/migration/rss.xml"
category: "財務軟體、Python 庫、數據處理"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "有關 SWIFT ISO 20022 遷移時間表 (2026-2028)、MT940 到 CAMT.053 過渡以及銀行對帳單解析器如何幫助財務團隊遷移的實用指南。"
item_guid: "https://bankstatementparser.com/zh-tw/migration/rss.xml"
item_link: "https://bankstatementparser.com/zh-tw/migration/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "ISO 20022 遷移指南：MT940 到 CAMT.053 過渡"
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
apple-mobile-web-app-title: "ISO 20022 遷移指南：MT940 到 CAMT.053 過渡"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "有關 SWIFT ISO 20022 遷移時間表 (2026-2028)、MT940 到 CAMT.053 過渡以及銀行對帳單解析器如何幫助財務團隊遷移的實用指南。"
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "銀行對帳單解析器徽標，透過無縫資料提取增強您的財務分析能力"
twitter_site: "@wwdseb"
twitter_title: "ISO 20022 遷移指南：MT940 到 CAMT.053 過渡"
twitter_url: "https://bankstatementparser.com/zh-tw/migration/index.html"

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

**TL;DR:** SWIFT 將在 2028 年 11 月前停用 MT940。Bank Statement Parser 使用單一 API 處理 MT940 和 CAMT.053，讓您的解析管線在過渡期間和之後都能正常運作。

## 為什麼這次遷移很重要

SWIFT 正在淘汰傳統 MT 訊息格式，轉向更豐富的 ISO 20022 標準。對於財務團隊而言，這意味著銀行對帳單處理管線必須在嚴格截止日期前從 MT940 演進至 CAMT.053。

## SWIFT 遷移時間表

| 日期 | 里程碑 | 影響 |
|---|---|---|
| **2025 年 11 月** | 跨境支付 MT 與 MX 共存結束 | PACS 訊息現在僅限 ISO 20022 |
| **2026 年 11 月** | 結構化/混合地址強制；MT101 多指令被拒絕；案件管理第一階段 | 地址格式必須合規；部分 MT 訊息將被拒絕 |
| **2026 年末** | 開始選擇接收 CAMT.052/.053/.054 | 金融機構可以開始接收原生 ISO 對帳單 |
| **2027 年 11 月** | 所有金融機構必須原生接收 CAMT.053 | SWIFT 停止將 MT 格式轉換為 ISO；您的系統必須直接解析 CAMT |
| **2028 年 11 月** | MT940/MT942/MT950/MT900/MT910 完全停用 | 舊版對帳單格式不再可用；CAMT.052/.053/.054 是唯一選擇 |

## 您的程式碼有何變化

### 之前：僅 MT940

```python
from bankstatementparser import Mt940Parser

parser = Mt940Parser("statement.mt940")
df = parser.parse()
```

### 之後：兩種格式搭配自動偵測

```python
from bankstatementparser import create_parser, detect_statement_format

fmt = detect_statement_format("statement.xml")  # or .mt940
parser = create_parser("statement.xml", fmt)
df = parser.parse()  # Same DataFrame schema regardless of format
```

`detect_statement_format()` 函式識別檔案是 MT940、CAMT.053、PAIN.001 或其他支援的格式。`create_parser()` 函式回傳對應的解析器。無論來源格式為何，您的下游程式碼運作方式完全相同。

## CAMT.053 與 MT940：主要差異

| 特性 | MT940 | CAMT.053 |
|---|---|---|
| 資料豐富度 | 欄位有限 | 每筆交易資料量增加 3-5 倍 |
| 字元集 | 有限（SWIFT 字元集） | 完整 Unicode |
| 結構 | 帶標籤的純文字 | 帶命名空間的 XML |
| 餘額報告 | 僅期初/期末 | 多種餘額類型 |
| 參考 | 單一參考欄位 | 多種參考類型 |
| 幣別處理 | 基本 | 完整多幣別含匯率 |

## Bank Statement Parser 如何協助

- **統一 API**：使用相同的工作流程解析 MT940、CAMT.053 及 PDF 對帳單，產生一致的 DataFrame 輸出。
- **自動偵測**：無需事先知道格式。`detect_statement_format()` 自動辨識。
- **混合 PDF 管線**：在過渡期間，僅提供 PDF 對帳單的銀行可透過 `smart_ingest()` 處理，自動餘額驗證。
- **命名空間無關**：無需配置即可處理任何 CAMT.053 變體（001.02、001.04 或銀行特定封裝）。
- **多幣別驗證**：`verify_balance_multi_currency()` 依幣別群組執行黃金法則——對多幣別 CAMT 對帳單至關重要。
- **串流處理**：使用固定記憶體處理大型 CAMT 檔案（50 MB+、50K+ 筆交易）。
- **帳本匯出**：直接匯出為 hledger 或 beancount 日記帳格式，用於財務記帳。
- **遷移測試**：在同一日期範圍並行執行兩個解析器，在切換前驗證輸出一致性。

## 開始使用

```bash
pip install bankstatementparser
```

```python
from bankstatementparser import create_parser, detect_statement_format

# Works with MT940 today, CAMT.053 tomorrow, PDF anytime
for file in bank_statement_files:
    fmt = detect_statement_format(file)
    parser = create_parser(file, fmt)
    df = parser.parse()
    process(df)  # Your code doesn't change
```

對於尚未提供結構化 CAMT 匯出的銀行 PDF 對帳單：

```python
from bankstatementparser.hybrid import smart_ingest

result = smart_ingest("statement.pdf")
assert result.verification.status == "VERIFIED"
```

[閱讀完整文件](/getting-started/index.html)

[與替代方案比較 ❯](/comparison/index.html) | [查看實際使用案例 ❯](/use-cases/index.html)
