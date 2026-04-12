---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "銀行對帳單解析器安全性"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 銀行對帳單解析器。版權所有。"
date: "Apr 11, 2026"
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

**TL;DR:** Bank Statement Parser 在本機處理所有資料，預設遮蔽 PII，針對 XXE 攻擊強化 XML 解析，透過 Ollama 在本機執行 LLM，並附帶 SHA-256 雜湊鎖定相依性及 CycloneDX SBOM。

## 安全設計

Bank Statement Parser 專為處理敏感財務資料而建構。每個設計決策都優先考慮安全性、隱私性和可稽核性。

## 零雲端依賴

所有處理在本機執行時期內完成。確定性解析器零網路呼叫。混合 PDF 管線使用 Ollama 進行本機 LLM 推論——不會將資料傳送至雲端 API。XML 解析器明確配置為 `no_network=True`、`resolve_entities=False` 及 `load_dtd=False`，以防止任何對外存取。

## PII 遮蔽

個人識別資訊（姓名、IBAN、郵政地址）在 CLI 輸出和串流模式下自動遮蔽。此功能預設啟用。

- **CLI**：敏感欄位顯示為 `***REDACTED***`
- **串流**：`parse_streaming(redact_pii=True)`（預設）
- **匯出**：CSV/JSON/Excel 保留完整資料以供下游處理
- **選擇顯示**：使用 `--show-pii` 或 `redact_pii=False` 取得未遮蔽的輸出

## XML 安全性（XXE 保護）

所有 XML 解析使用 `lxml` 搭配強化設定：

- `resolve_entities=False` -- 防止 XML 實體擴展攻擊
- `no_network=True` -- 阻擋解析器的所有對外網路存取
- `load_dtd=False` -- 防止基於 DTD 的攻擊
- 處理前剝離命名空間——安全處理任何 CAMT.053 變體

## ZIP 檔案安全

`iter_secure_xml_entries()` 在擷取前驗證每個 ZIP 成員：

- **條目大小上限**：每個條目 10 MB（可配置）
- **總大小上限**：未壓縮總計 50 MB（可配置）
- **壓縮比限制**：預設 100:1 -- 偵測 ZIP 炸彈
- **加密條目拒絕**：跳過加密條目並發出警告
- **無磁碟寫入**：XML 位元組透過 `from_bytes()` 直接傳遞給解析器

## 路徑遍歷防護

輸入驗證阻擋危險檔案路徑：

- 空位元組、目錄遍歷模式（`../`）及符號連結被拒絕
- 針對預期格式的檔案副檔名驗證
- 檔案大小限制（預設 100 MB，可配置）

## 餘額驗證（黃金法則）

每次 PDF 擷取都透過以下公式驗證：`opening balance + credits − debits == closing balance`。結果標記為 VERIFIED、DISCREPANCY 或 FAILED。差異可透過 `--type review` 互動式審核。

## 確定性輸出

對於結構化格式（CAMT、PAIN.001、CSV、OFX、QFX、MT940），給定相同的輸入檔案，解析器每次執行都產生位元組完全一致的輸出。無隨機性、無模型推論、無啟發式取樣。這對以下方面至關重要：

- **稽核可再現性**：執行同一檔案兩次並比對輸出
- **法規合規**：展示一致的處理流程
- **CI 驗證**：718 項測試強制確定性，100% 分支覆蓋率

## 供應鏈安全

- **SHA-256 雜湊鎖定相依性**：`poetry.lock` 中的每個套件都有已驗證的檔案雜湊
- **CycloneDX SBOM**：每個版本都包含軟體物料清單
- **GitHub 建置來源**：證明將每個產出物連結至其來源提交
- **簽署提交**：所有提交均經 SSH 簽署並在 CI 中驗證
- **相依性驗證**：`scripts/verify_locked_hashes.py` 在本機驗證所有雜湊值

## 本機驗證

```bash
python -m pytest                          # 718 tests, 100% branch coverage
python scripts/verify_locked_hashes.py    # SHA-256 hash verification
git log --show-signature -1               # Verify commit signature
```
