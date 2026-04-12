---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "關於銀行對帳單解析器的常見問題"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 銀行對帳單解析器。版權所有。"
date: "Apr 11, 2026"
description: "有關銀行對帳單解析器的常見問題的解答：資料隱私、PII 編輯、效能、ISO 20022 支援、串流、合規性和財務工作流程。"
download: ""
format-detection: "telephone=no"
hreflang: "zh-tw"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/zh-tw/faq/index.html"
image_alt: "銀行對帳單解析器的徽標，這是一款功能強大的 Python 工具，專為快速、準確的財務資料處理和見解提取而設計。"
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "銀行對帳單解析器常見問題解答、CAMT 解析器問題、PAIN.001 常見問題解答、ISO 20022 python 常見問題解答、PII 編輯銀行、銀行解析器效能、金融資料隱私、MT940 解析器常見問題解答、串流解析器 python、銀行對合規性"
language: "zh-TW"
layout: "faq"
locale: "zh_TW"
logo_alt: "銀行對帳單解析器的徽標，這是一款功能強大的 Python 工具，專為快速、準確的財務資料處理和見解提取而設計。"
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "常問問題"
permalink: "https://bankstatementparser.com/zh-tw/faq/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "關於銀行對帳單解析器的常見問題"
tags: "常見問題、銀行、聲明、解析器、隱私、合規性、效能、串流媒體、iso20022、python"
theme_color: "rgb(73, 214, 251)"
title: "銀行對帳單解析器常見問題：隱私、效能和使用"
url: "https://bankstatementparser.com/zh-tw/faq/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/zh-tw/faq/rss.xml"
category: "財務軟體、Python 庫、常見問題解答"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "有關銀行對帳單解析器的常見問題的解答：資料隱私、PII 編輯、效能、ISO 20022 支援、串流、合規性和財務工作流程。"
item_guid: "https://bankstatementparser.com/zh-tw/faq/rss.xml"
item_link: "https://bankstatementparser.com/zh-tw/faq/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "銀行對帳單解析器常見問題：隱私、效能和使用"
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
apple-mobile-web-app-title: "銀行對帳單解析器常見問題：隱私、效能和使用"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "有關銀行對帳單解析器的常見問題的解答：資料隱私、PII 編輯、效能、ISO 20022 支援和財務工作流程。"
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "銀行對帳單解析器的徽標，這是一款功能強大的 Python 工具，專為快速、準確的財務資料處理和見解提取而設計。"
twitter_site: "@wwdseb"
twitter_title: "銀行對帳單解析器常見問題：隱私、效能和使用"
twitter_url: "https://bankstatementparser.com/zh-tw/faq/index.html"

# Humans.txt - The Humans.txt front matter (YAML).

author_website: "https://bankstatementparser.com"
author_twitter: "@wwdseb"
author_location: "London, UK"
thanks: "感謝您的閱讀！"
site_last_updated: "2026-04-01"
site_standards: "HTML5, CSS3, RSS, Atom, JSON, XML, YAML, Markdown, TOML"
site_components: "Shokunin SSG, Shokunin CLI, Shokunin Templates, Kaishi Templates, Kaishi Themes"
site_software: "Shokunin, Rust"

---

## 資料隱私與合規性

### 是否有任何資料會離開我的基礎設施？

**不會——即使是 PDF 擷取也不會。** Bank Statement Parser 以無狀態函式庫運作。所有處理——解析、PII 遮蔽、存檔擷取——都在本機執行時期記憶體中進行。混合 PDF 管線使用 Ollama 進行本機 LLM 推論——無雲端 API。XML 解析器以 `no_network=True` 進行強化，在解析器層級阻擋所有對外存取。您的財務資料不會離開您的環境。

### PII 遮蔽如何運作？

敏感欄位在到達您的應用程式邏輯前會被遮蔽。解析器識別借方名稱、貸方名稱、IBAN 及郵政地址，在主控台輸出和串流模式中替換為 `***REDACTED***`。

- **遮蔽功能在 CLI 輸出和串流模式下預設啟用**。
- **檔案匯出**（CSV、JSON、Excel）保留未遮蔽的資料以供下游處理。
- **選擇顯示**完整資料：CLI 使用 `--show-pii`，API 使用 `redact_pii=False`。

### 擷取過程是確定性的嗎？

**結構化格式——每次執行輸出位元組完全一致。** 給定相同的輸入檔案，確定性解析器（CAMT、PAIN.001、CSV、OFX、QFX、MT940）每次都產生相同的結果。無隨機性、無模型推論、無啟發式取樣。

對於混合 PDF 管線，基於 LLM 的擷取路徑在不同執行間可能產生微小差異。因此每次 PDF 擷取都透過**黃金法則**（`opening + credits − debits == closing`）驗證，標記的差異可以互動式審核。

CI 透過 718 項測試在 100% 分支覆蓋率下強制確定性，包括透過 Hypothesis 進行基於屬性的模糊測試。

### 專案遵循哪些合規標準？

本專案維護符合 ISO 13485 的文件，具備完整可追溯性：

- 量化的**風險登記冊**，含嚴重性/機率評分及殘餘風險評估。
- **驗證與確認計畫**，涵蓋 5 個階段共 19 個門控步驟。
- **變更管控程序**，含影響評估及回滾協定。
- **SOUP 登記冊**，涵蓋所有相依性及其風險等級和 EOL 追蹤。
- **可追溯性矩陣**，將設計輸入對應至實作與驗證。

每個版本都包含 CycloneDX SBOM、SHA-256 校驗碼及 GitHub 建置來源證明。

## 效能與可擴展性

### Bank Statement Parser 有多快？

每次提交都會在 CI 中驗證效能閾值：

| 指標 | 數值 |
|---|---|
| CAMT.053 吞吐量 | 27,000+ 筆交易/秒 |
| PAIN.001 吞吐量 | 52,000+ 筆交易/秒 |
| 每筆交易延遲（CAMT） | 37 微秒 |
| 每筆交易延遲（PAIN.001） | 19 微秒 |
| 首次回傳結果時間 | < 2 ms |

PDF 擷取速度取決於路由路徑：確定性（亞秒級）、文字 LLM（數秒）、視覺 LLM（每頁數秒）。

### 如何處理大型檔案？

**串流處理搭配固定記憶體——已在每檔 50,000 筆交易下測試。** 使用 `parse_streaming()` 增量處理 XML 檔案。每筆交易產生為字典；處理後清除元素以防止記憶體成長。記憶體不隨檔案大小增長——50K 筆交易測試（25+ MB）使用的記憶體不到 10K 筆交易測試的 2 倍。

對於超過 50 MB 的檔案（例如含 100K+ 付款的主機對主機 PAIN.001 批次），解析器透過基於區塊的命名空間剝離臨時檔案進行串流——完整文件不會載入記憶體。

### ZIP 檔案如何安全處理？

`iter_secure_xml_entries()` 在擷取前驗證每個成員：

- **條目大小上限**（預設每個條目 10 MB）
- **未壓縮總大小上限**（預設 50 MB）
- **壓縮比限制**（預設 100:1）以防止 ZIP 炸彈
- **加密條目拒絕**

不會寫入任何檔案到磁碟。XML 位元組透過 `from_bytes()` 直接傳遞給解析器。

### 可以平行解析多個檔案嗎？

**可以。** 使用 `parse_files_parallel()`，它將工作分配至 `ProcessPoolExecutor`：

```python
from bankstatementparser import parse_files_parallel

results = parse_files_parallel([
    "statements/jan.xml",
    "statements/feb.xml",
    "statements/mar.xml",
])
for r in results:
    print(r.path, r.status, len(r.transactions), "rows")
```

批次 PDF 匯入可使用 `scan_and_ingest()`，處理整個資料夾樹狀結構並自動去重。

## 支援的格式

### 支援哪些銀行對帳單格式？

| 格式 | 標準 | 檔案類型 | 解析器/方法 |
|---|---|---|---|
| CAMT.053 | ISO 20022 銀行對客戶對帳單 | `.xml` | `CamtParser` |
| PAIN.001 | ISO 20022 貸記轉帳啟動 | `.xml` | `Pain001Parser` |
| CSV | 一般銀行匯出 | `.csv` | `CsvStatementParser` |
| OFX | Open Financial Exchange | `.ofx` | `OfxParser` |
| QFX | Quicken Financial Exchange | `.qfx` | `QfxParser` |
| MT940 | SWIFT 標準 | `.mt940`, `.sta` | `Mt940Parser` |
| PDF | 數位及掃描對帳單 | `.pdf` | `smart_ingest()` |

### 混合 PDF 管線如何運作？

混合管線（v0.0.5+）智慧地將 PDF 路由至三條擷取路徑：

- **路徑 A（確定性）**：直接解析結構化 PDF 表格——免費、最快、無需 LLM。
- **路徑 B（文字 LLM）**：透過本機 LLM（LiteLLM/Ollama）擷取複雜版面的數位 PDF。
- **路徑 C（視覺 LLM）**：使用多模態視覺模型處理掃描或影印的對帳單。

每次擷取都透過黃金法則（`opening + credits − debits == closing`）驗證。差異可透過 `--type review` 互動式審核。

### 解析器是否處理 CAMT.053 的銀行特定方言？

**是的——設計上與命名空間無關。** 解析器在處理前剝離 XML 命名空間，可處理任何 CAMT.053 變體（`camt.053.001.02`、`camt.053.001.04` 或專有銀行封裝），無需命名空間特定配置。XPath 查詢針對元素結構，而非命名空間 URI。

對於將 CAMT 包裝在自訂信封中的銀行，使用 `from_string()` 或 `from_bytes()` 直接送入內部文件。

### 可以將自訂 CSV 欄位標題對應到標準架構嗎？

**可以——自動標準化，零配置。** `CsvStatementParser` 識別常見的標頭變化：`"Date"`、`"Transaction Date"`、`"Booking Date"` 全部對應到 `date` 欄位。`"Amount"`、`"Value"`、`"Sum"` 對應到 `amount`。分離的貸方/借方欄（例如 `"Credit"` 和 `"Debit"`）會被自動偵測並合併為單一帶正負號的金額。

### 輸出格式是什麼？

所有解析器都產生具有一致欄位類型的標準化 pandas DataFrame：

| 格式 | 主要欄位 |
|---|---|
| **CAMT** | `Amount`, `Currency`, `DrCr`, `Debtor`, `Creditor`, `Reference`, `ValDt`, `BookgDt`, `AccountId` |
| **PAIN.001** | `PmtInfId`, `PmtMtd`, `InstdAmt`, `Currency`, `CdtrNm`, `EndToEndId`, `MsgId`, `CreDtTm`, `NbOfTxs` |
| **CSV/OFX/QFX/MT940** | `date`, `description`, `amount`（標準化） |

您也可以匯出為 CSV、JSON、Excel、Polars DataFrame、hledger 或 beancount 日記帳格式。

## PDF 與 LLM 功能

### 混合管線支援哪些 LLM 模型？

管線使用 LiteLLM 作為模型抽象層，並透過直接 Ollama 橋接處理視覺提示。建議模型：

- **文字擷取**：任何 LiteLLM 相容模型（本機或遠端）。
- **視覺擷取**：`ollama/minicpm-v`（建議）用於掃描 PDF。
- **分類**：任何 LiteLLM 相容模型。

所有模型都可透過 Ollama 100% 在本機執行——無需 API 金鑰。

### 什麼是黃金法則驗證？

每次 PDF 擷取都透過以下公式驗證：`opening balance + credits − debits == closing balance`。結果標記為：

- **VERIFIED**：餘額完全吻合。
- **DISCREPANCY**：餘額不符——建議審核。
- **FAILED**：無法執行驗證（缺少餘額資料）。

### 可以自動分類交易嗎？

**可以。** 增強模組（v0.0.6+）提供 LLM 驅動的交易分類：

```python
from bankstatementparser.enrichment import Categorizer

categorizer = Categorizer()
enriched = categorizer.categorize_batch(transactions)
```

預設架構使用 13 種 Plaid 相容類別。您可以提供自訂的類別架構。

### 可以匯出為 hledger 或 beancount 嗎？

**可以**（v0.0.8+）。將交易匯出為純文字記帳日記帳格式，支援帳戶對應：

```python
from bankstatementparser.export import to_hledger, to_beancount

journal = to_hledger(transactions, account="Assets:Bank:Checking")
```

## 財務工作流程

### 解析器如何處理多幣別對帳單？

**每筆交易保留其原始幣別——無隱式轉換。** `Currency` 欄位從 XML 的 `Ccy` 屬性逐筆擷取。多幣別對帳單維持原樣。`get_account_balances()` 方法回傳每個帳戶的期初和期末餘額及原始幣別代碼。

自 v0.0.8 起，`verify_balance_multi_currency()` 依幣別分組交易，並對每個群組獨立執行黃金法則——適用於持有多種幣別的帳戶。

### 解析器是否支援傳出和傳入格式？

**是的。** `Pain001Parser` 處理 ISO 20022 PAIN.001 貸記轉帳啟動檔案（傳出付款）。`CamtParser` 處理 CAMT.053 銀行對客戶對帳單檔案（傳入報告）。兩者都支援串流、PII 遮蔽，以及匯出至 CSV、JSON、Excel、hledger 和 beancount。使用 `detect_statement_format()` 自動辨識格式。

### 當交易條目格式錯誤時會發生什麼？

行為取決於解析模式：

- **`parse()`（批次模式）** -- 缺少必填欄位（`Amount`、`Currency` 或 `CdtDbtInd`）的格式錯誤條目會被跳過並記錄警告。其餘對帳單正常解析。
- **`parse_streaming()`（串流模式）** -- 解析錯誤立即作為例外傳播。無靜默資料遺失。此快速失敗行為是為每筆交易都必須核對的財務工作流程而設計。
- **`smart_ingest()`（混合 PDF）** -- 擷取錯誤會記錄在 `IngestResult` 中並附帶驗證狀態，允許互動式審核。

### 去重如何運作？

每筆交易會根據其關鍵欄位分配一個冪等的 `transaction_hash`（MD5 指紋）。這使得增量匯入安全——重新處理相同檔案會產生相同的雜湊，因此重複項會被自動偵測。

```python
from bankstatementparser import CamtParser, Deduplicator

parser = CamtParser("statement.xml")
dedup = Deduplicator()
result = dedup.deduplicate(dedup.from_dataframe(parser.parse()))

print(f"Unique: {len(result.unique_transactions)}")
print(f"Exact duplicates: {len(result.exact_duplicates)}")
print(f"Suspected matches: {len(result.suspected_matches)}")
```

## 安裝與相容性

### 如何安裝 Bank Statement Parser？

```bash
# 核心安裝（僅確定性解析器）
pip install bankstatementparser

# PDF 混合管線
pip install 'bankstatementparser[hybrid]'         # 文字 LLM 路徑
pip install 'bankstatementparser[hybrid-vision]'   # 視覺 LLM 路徑

# 額外功能
pip install 'bankstatementparser[enrichment]'      # 交易分類
pip install 'bankstatementparser[api]'             # REST API 微服務
pip install 'bankstatementparser[polars]'          # Polars DataFrame 支援
```

### 支援哪些 Python 版本？

Python 3.10 至 3.14。Python 3.9 支援在 v0.0.6 中移除（EOL 2025-10-31）。所有版本在 CI 中以 718 項測試達 100% 分支覆蓋率進行測試。

### 有哪些相依性？

核心函式庫有 5 個直接相依性：

- `lxml` -- XML 解析與安全強化
- `pandas` -- DataFrame 與資料操作
- `openpyxl` -- Excel 匯出
- `pydantic` -- 資料驗證與模型
- `defusedxml` -- XXE 保護

可選額外套件新增：`litellm`、`pypdf`、`pdfplumber`、`pypdfium2`、`fastapi`、`uvicorn`、`polars`。

所有相依性都有 SHA-256 雜湊鎖定版本。CycloneDX SBOM 對應每個執行時期元件。

### 可以在 macOS、Linux 和 Windows 上執行嗎？

**可以。** 此函式庫適用於 macOS、Linux 和 Windows（透過 WSL）。無平台特定相依性。

### 有 REST API 嗎？

**有**（v0.0.8+）。安裝 `pip install 'bankstatementparser[api]'` 後執行：

```bash
bankstatementparser-api --port 8000
```

端點：`POST /ingest`（解析對帳單）和 `GET /health`（健康檢查）。

## 可再現性與安全性

### 如何驗證可再現性？

```bash
python -m pytest                              # 718 tests, 100% branch coverage
python scripts/verify_locked_hashes.py        # SHA-256 hash verification
git log --show-signature -1                   # Verify commit signature
```

### 內建了哪些安全保護？

- **XXE 保護**：`resolve_entities=False`、`no_network=True`、`load_dtd=False`
- **ZIP 炸彈保護**：壓縮比限制、條目大小上限、加密條目拒絕
- **路徑遍歷防護**：危險模式阻擋清單及符號連結解析
- **輸入驗證**：檔案大小限制（預設 100 MB）、副檔名/格式驗證
- **供應鏈**：SHA-256 雜湊鎖定相依性、CycloneDX SBOM、建置來源證明
- **簽署提交**：在 CI 中強制執行
- **本機 LLM**：混合 PDF 管線使用 Ollama——無雲端 API 呼叫

### Bank Statement Parser 與 pyiso20022 比較如何？

pyiso20022 是一個廣泛的 ISO 20022 工具包，可從 ISO XML 架構產生 Python dataclass。它涵蓋廣泛的 ISO 20022 訊息類型（PACS、PAIN、CAMT、ADMI）及架構驗證。Bank Statement Parser 專為銀行對帳單解析而建構，具備混合 PDF 支援、餘額驗證、交易增強、帳本匯出，以及跨七種格式（含非 ISO 格式：CSV、OFX、QFX、MT940、PDF）的統一 API。如果您需要將銀行對帳單解析為具備正式環境安全等級的 DataFrame，請使用 Bank Statement Parser。如果您需要使用完整的 ISO 20022 訊息目錄，請使用 pyiso20022。

### SWIFT ISO 20022 遷移截止日期為何？

SWIFT 發布了分階段遷移時間表：

- **2026 年 11 月**：結構化及混合地址成為強制要求。MT101 多指令訊息將被拒絕。案件管理第一階段開始。
- **2027 年 11 月**：所有金融機構必須能夠原生接收 CAMT.053 對帳單。SWIFT 將停止將 MT 格式轉換為 ISO 格式。
- **2028 年 11 月**：MT940、MT942、MT950、MT900 及 MT910 完全停用。這些將由 CAMT.052、CAMT.053 及 CAMT.054 對等項取代。

Bank Statement Parser 同時支援傳統 MT940 格式及現代 CAMT.053/PAIN.001 格式，是過渡時期的理想選擇。

