---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "銀行對帳單解析器變更日誌"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 銀行對帳單解析器。版權所有。"
date: "Apr 01, 2026"
description: "銀行對帳單解析器的發布歷史記錄和變更日誌。追蹤所有版本的新功能、改進和錯誤修復。"
download: ""
format-detection: "telephone=no"
hreflang: "zh-tw"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/zh-tw/journal-des-modifications/index.html"
image_alt: "銀行對帳單解析器徽標，透過無縫資料提取增強您的財務分析能力"
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "銀行對帳單解析器變更日誌、發行說明、版本歷史記錄、更新"
language: "zh-TW"
layout: "about"
locale: "zh_TW"
logo_alt: "銀行對帳單解析器徽標，透過無縫資料提取增強您的財務分析能力"
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "變更日誌"
permalink: "https://bankstatementparser.com/zh-tw/journal-des-modifications/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "發布歷史和新增內容"
tags: "變更日誌、發布、更新、版本、公告、博客"
theme_color: "rgb(73, 214, 251)"
title: "銀行對帳單解析器變更日誌"
url: "https://bankstatementparser.com/zh-tw/journal-des-modifications/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/zh-tw/journal-des-modifications/rss.xml"
category: "財務軟體、Python 庫、數據處理"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "銀行對帳單解析器的發布歷史記錄和變更日誌。追蹤所有版本的新功能、改進和錯誤修復。"
item_guid: "https://bankstatementparser.com/zh-tw/journal-des-modifications/rss.xml"
item_link: "https://bankstatementparser.com/zh-tw/journal-des-modifications/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "銀行對帳單解析器變更日誌"
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
apple-mobile-web-app-title: "銀行對帳單解析器變更日誌"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "銀行對帳單解析器的發布歷史記錄和變更日誌。追蹤所有版本的新功能、改進和錯誤修復。"
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "銀行對帳單解析器徽標，透過無縫資料提取增強您的財務分析能力"
twitter_site: "@wwdseb"
twitter_title: "銀行對帳單解析器變更日誌"
twitter_url: "https://bankstatementparser.com/zh-tw/journal-des-modifications/index.html"

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

關注銀行對帳單解析器的開發。透過 [RSS](/changelog/rss.xml) 訂閱或觀看 [GitHub 儲存庫](https://github.com/sebastienrousseau/bankstatementparser) 用於發布通知。

## v0.0.4 — 2026-03-15（最新）

- 新增了平行文件解析`parse_files_parallel()`使用 ProcessPoolExecutor。
- 為具有有限記憶體的大型 PAIN.001 檔案 (50 MB+) 添加了真正的串流。
- 效能最佳化：CAMT 吞吐量現已超過 27,000 tx/s，PAIN.001 超過 52,000 tx/s。
- 添加`Deduplicator`用於檢測精確重複項和與置信度分數的可疑匹配的類別。
- 添加`from_string()`和`from_bytes()`無需磁碟 I/O 的記憶體解析方法。
- 添加`iter_secure_xml_entries()`用於安全的 ZIP 存檔處理。
- 具有效能閾值強制執行的擴展 CI。

## v0.0.3 — 2025-11-20

- 新增了 CSV、OFX、QFX 和 MT940 解析器支援。
- 新增了格式自動偵測`detect_statement_format()`和`create_parser()`。
- 新增了 PII 編輯（在 CLI 和流模式下預設為啟用）。
- 新增了 CSV、JSON 和 Excel 的匯出幫助程式。
- 新增了可選的 Polars DataFrame 支援。
- 將測試套件擴展至 467 個測試，分支覆蓋率為 100%。

## v0.0.2 — 2025-06-10

- 新增了 PAIN.001 解析器（`Pain001Parser`) 用於 ISO 20022 學分轉移啟動文件。
- 新增了 CLI 介面（`python -m bankstatementparser.cli`）。
- 新增了串流模式`parse_streaming()`。
- 新增了輸入驗證和檔案大小限制。

## v0.0.1 — 2025-01-15

- 初始版本。
- CAMT.053 解析器（`CamtParser`) 適用於 ISO 20022 銀行對客戶報表。
- 大熊貓資料幀輸出。
- 基本 XML 安全強化（XXE 保護、no_network）。

在 [GitHub]( 上查看完整的提交歷史記錄https://github.com/sebastienrousseau/bankstatementparser/commits/main).

<腳本類型=“應用程式/ld+json”>
{
  “@上下文”：“https://schema.org「，
  "@type": "軟體應用程式",
  "name": "銀行對帳單解析器",
  "applicationCategory": "開發者應用程式",
  "operatingSystem": "跨平台",
  "軟體版本": "0.0.4",
  "發佈日期": "2026-03-15",
  "releaseNotes": "新增了平行檔案解析、PAIN.001 的真正串流、效能最佳化（27K+ tx/s CAMT、52K+ tx/s PAIN.001）、重複資料刪除器類別、記憶體中解析、安全 ZIP 處理。 ",
  “下載地址”：“https://pypi.org/project/bankstatementparser/「，
  “執照”： ”https://opensource.org/licenses/Apache-2.0「，
  「作者」：{
    "@type": "人",
    “姓名”：“塞巴斯蒂安·盧梭”
  }
}
</腳本>
