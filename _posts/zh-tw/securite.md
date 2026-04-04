---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "銀行對帳單解析器安全性"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 銀行對帳單解析器。版權所有。"
date: "Apr 01, 2026"
description: "銀行對帳單解析器的安全功能：XXE 保護、ZIP 炸彈強化、PII 編輯、供應鏈安全、確定性輸出和簽名版本。"
download: ""
format-detection: "telephone=no"
hreflang: "zh-tw"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/zh-tw/securite/index.html"
image_alt: "銀行對帳單解析器徽標，透過無縫資料提取增強您的財務分析能力"
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "銀行對帳單安全、PII 編輯 Python、XXE 保護、ZIP 炸彈保護、供應鏈安全 SBOM、確定性解析、金融資料安全"
language: "zh-TW"
layout: "about"
locale: "zh_TW"
logo_alt: "銀行對帳單解析器徽標，透過無縫資料提取增強您的財務分析能力"
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "安全"
permalink: "https://bankstatementparser.com/zh-tw/securite/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "我們如何保護您的財務數據"
tags: "安全、pii、xxe、sbom、供應鏈、確定性"
theme_color: "rgb(73, 214, 251)"
title: "銀行對帳單解析器安全性：資料保護與供應鏈"
url: "https://bankstatementparser.com/zh-tw/securite/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/zh-tw/securite/rss.xml"
category: "財務軟體、Python 庫、數據處理"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "銀行對帳單解析器的安全功能：XXE 保護、ZIP 炸彈強化、PII 編輯、供應鏈安全、確定性輸出和簽名版本。"
item_guid: "https://bankstatementparser.com/zh-tw/securite/rss.xml"
item_link: "https://bankstatementparser.com/zh-tw/securite/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "銀行對帳單解析器安全性：資料保護與供應鏈"
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
apple-mobile-web-app-title: "銀行對帳單解析器安全性：資料保護與供應鏈"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "銀行對帳單解析器的安全功能：XXE 保護、ZIP 炸彈強化、PII 編輯、供應鏈安全、確定性輸出和簽名版本。"
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "銀行對帳單解析器徽標，透過無縫資料提取增強您的財務分析能力"
twitter_site: "@wwdseb"
twitter_title: "銀行對帳單解析器安全性：資料保護與供應鏈"
twitter_url: "https://bankstatementparser.com/zh-tw/securite/index.html"

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

**TL;DR:** 銀行對帳單解析器進行零網路調用，預設會編輯 PII，針對 XXE 攻擊強化 XML 解析，並附帶 SHA-256 哈希鎖定依賴項和 CycloneDX SBOM。

## 設計安全

銀行對帳單解析器專為處理敏感的財務資料而建置。每個設計決策都會優先考慮安全性、隱私性和可審核性。

## 零網路訪問

所有處理都在運行時本地進行。該函式庫進行零 API 呼叫、零雲連接並收集零遙測資料。 XML 解析器明確配置為`no_network=True`, `resolve_entities=False`， 和`load_dtd=False`以防止任何出站訪問。

## PII 編輯

個人識別資訊（姓名、IBAN、郵政地址）會在 CLI 輸出和流模式下自動編輯。預設此功能處於啟用狀態。

- **CLI**：敏感欄位顯示為`***REDACTED***`
- **串流媒體**：`parse_streaming(redact_pii=True)`(預設)
- **匯出**：CSV/JSON/Excel 保留完整資料以供下游處理
- **選擇加入**：使用`--show-pii`或者`redact_pii=False`當您需要未編輯的輸出時

## XML 安全性（XXE 保護）

所有 XML 解析都使用`lxml`具有強化設定：

- `resolve_entities=False`-- 防止XML實體擴充攻擊
-`no_network=True`-- 阻止解析器的所有出站網路訪問
-`load_dtd=False`-- 防止基於 DTD 的攻擊
- 處理前命名空間剝離－安全處理任何 CAMT.053 變體

## ZIP 檔案安全

`iter_secure_xml_entries()`在提取之前驗證每個 ZIP 成員：

- **條目大小上限**：每個條目 10 MB（可設定）
- **總大小上限**：未壓縮總計 50 MB（可設定）
- **壓縮比限制**：預設為 100:1 -- 偵測 ZIP 炸彈
- **加密條目拒絕**：跳過加密條目並發出警告
- **無磁碟寫入**：XML 位元組透過直接傳遞到解析器`from_bytes()`

## 路徑遍歷預防

輸入驗證以阻止危險檔案路徑：

- 空字節，目錄遍歷模式（`../`)，且符號連結被拒絕
- 針對預期格式的檔案副檔名驗證
- 檔案大小限制（預設 100 MB，可配置）

## 確定性輸出

給定相同的輸入文件，解析器每次運行都會產生與位元組相同的輸出。沒有隨機性，沒有模型推理，沒有啟發式取樣。這對於以下方面至關重要：

- **審核重現性**：運行同一文件兩次並比較輸出
- **法規遵循**：展示一致的處理
- **CI 驗證**：467 項測試強制執行確定性，分支覆蓋率為 100%

## 供應鏈安全

- **SHA-256 雜湊鎖定相依性**：中的每個套件`poetry.lock`已驗證文件哈希值
- **CycloneDX SBOM**：每個版本都包含軟體物料清單
- **GitHub 建置來源**：證明將每個工件連結到其來源提交
- **簽名提交**：所有提交均經過 SSH 簽署並在 CI 中進行驗證
- **依賴關係驗證**：`scripts/verify_locked_hashes.py`在本地驗證所有哈希值

## 本機驗證

```bash
python -m pytest                          # 467 tests, 100% branch coverage
python scripts/verify_locked_hashes.py    # SHA-256 hash verification
git log --show-signature -1               # Verify commit signature
```
