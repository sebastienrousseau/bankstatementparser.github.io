---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "黒い窓のある白い建物"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/daniele-franchi-Vl6YuVBLEys.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 銀行取引明細書パーサー。無断転載を禁じます。"
date: "Apr 11, 2026"
description: "Bank Statement Parser for Python の使用を開始します。CAMT/PAIN.001/CSV/OFX/QFX/MT940 ファイルをインストール、解析し、ストリーミングまたは CLI ワークフローを使用します。"
download: ""
format-detection: "telephone=no"
hreflang: "ja"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/ja/hajimeni/index.html"
image_alt: "Bank Statement Parser のロゴ。迅速かつ正確な財務データ処理と洞察の抽出のために設計された強力な Python ツールです。"
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "銀行取引明細書パーサー、はじめに、Python、CAMT、PAIN.001、CSV、OFX、QFX、MT940、財務データ"
language: "ja-JP"
layout: "start"
locale: "ja_JP"
logo_alt: "Bank Statement Parser のロゴ。迅速かつ正確な財務データ処理と洞察の抽出のために設計された強力な Python ツールです。"
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "はじめる"
permalink: "https://bankstatementparser.com/ja/hajimeni/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Bank Statement Parser を使用して安全なアプリケーションの構築を開始する"
tags: "銀行、ステートメント、パーサー、Python、camt、pain001、csv、ofx、qfx、mt940、ストリーミング、cli"
theme_color: "rgb(73, 214, 251)"
title: "Bank Statement Parser: インストールと使用ガイド"
url: "https://bankstatementparser.com/ja/hajimeni/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/ja/hajimeni/rss.xml"
category: "財務ソフトウェア、Python ライブラリ、開発者ガイド"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin (version 0.0.20)"
item_description: "Bank Statement Parser for Python の使用を開始します。CAMT/PAIN.001/CSV/OFX/QFX/MT940 ファイルをインストール、解析し、ストリーミングまたは CLI ワークフローを使用します。"
item_guid: "https://bankstatementparser.com/ja/hajimeni/rss.xml"
item_link: "https://bankstatementparser.com/ja/hajimeni/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Bank Statement Parser: インストールと使用ガイド"
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
apple-mobile-web-app-title: "Bank Statement Parser: インストールと使用ガイド"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Bank Statement Parser をインストールして使用し、CAMT、PAIN.001、CSV、OFX/QFX、MT940 ファイルを Python で解析します。"
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Bank Statement Parser のロゴ。迅速かつ正確な財務データ処理と洞察の抽出のために設計された強力な Python ツールです。"
twitter_site: "@wwdseb"
twitter_title: "Bank Statement Parser: インストールと使用ガイド"
twitter_url: "https://bankstatementparser.com/ja/hajimeni/index.html"

# Humans.txt - The Humans.txt front matter (YAML).

author_website: "https://bankstatementparser.com"
author_twitter: "@wwdseb"
author_location: "London, UK"
thanks: "読んでいただきありがとうございます!"
site_last_updated: "2026-04-01"
site_standards: "HTML5, CSS3, RSS, Atom, JSON, XML, YAML, Markdown, TOML"
site_components: "Shokunin SSG, Shokunin CLI, Shokunin Templates, Shokunin Themes, Kaishi SSG, Kaishi CLI, Kaishi Templates, Kaishi Themes"
site_software: "Shokunin, Rust"

---

## 必要要件

- Python 3.10〜3.14
- ターミナルアクセス（macOS、Linux、または WSL）

## インストール

```bash
# コアインストール（確定的パーサーのみ）
pip install bankstatementparser
```

追加機能のオプションエクストラ:

```bash
# デジタル PDF 用のテキスト LLM パス（litellm + pypdf）
pip install 'bankstatementparser[hybrid]'

# 高精度テーブル抽出（pdfplumber 追加）
pip install 'bankstatementparser[hybrid-plus]'

# スキャン PDF 用のビジョン LLM パス（pypdfium2 追加）
pip install 'bankstatementparser[hybrid-vision]'

# LLM によるトランザクション分類
pip install 'bankstatementparser[enrichment]'

# REST API マイクロサービス（FastAPI + uvicorn）
pip install 'bankstatementparser[api]'

# オプションの Polars DataFrame サポート
pip install 'bankstatementparser[polars]'
```

## クイックスタート

### あらゆる構造化形式を自動検出して解析

```python
from bankstatementparser import create_parser, detect_statement_format

fmt = detect_statement_format("transactions.ofx")
parser = create_parser("transactions.ofx", fmt)
df = parser.parse()  # pandas DataFrame
print(df.head())
```

`.xml`（CAMT/PAIN.001）、`.csv`、`.ofx`、`.qfx`、`.mt940`、`.sta` ファイルに対応しています。

### CAMT.053 を解析する

```python
from bankstatementparser import CamtParser

parser = CamtParser("statement.xml")
transactions = parser.parse()
```

### PAIN.001 を解析する

```python
from bankstatementparser import Pain001Parser

parser = Pain001Parser("payment.xml")
payments = parser.parse()
```

### PDF 銀行取引明細書を解析する（ハイブリッドパイプライン）

ハイブリッドパイプラインは、PDF を 3 つの抽出パスにインテリジェントに振り分けます。

```python
from bankstatementparser.hybrid import smart_ingest

result = smart_ingest("statement.pdf")
print(result.source_method)         # "deterministic" | "llm" | "vision"
print(result.verification.status)   # VERIFIED | DISCREPANCY | FAILED
print(result.transactions)          # List of extracted transactions
```

すべての抽出は**ゴールデンルール**で検証されます: `opening + credits − debits == closing`

## 大きなファイルのストリーミング

数千のトランザクションを含むファイルでは、ストリーミングを使用してメモリを制限内に保ちます。

```python
parser = CamtParser("large_statement.xml")
for transaction in parser.parse_streaming(redact_pii=True):
    process(transaction)  # Memory stays constant
```

## メモリ内解析

ディスク I/O なしでバイトから解析します。SFTP や API ワークフローに便利です。

```python
xml_bytes = download_from_sftp()
parser = CamtParser.from_bytes(xml_bytes, source_name="daily.xml")
transactions = parser.parse()
```

## 並列ファイル処理

複数のファイルを同時に解析します。

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

## 一括ディレクトリスキャン

フォルダツリー全体を自動重複排除で処理します。

```python
from bankstatementparser.hybrid import scan_and_ingest

batch = scan_and_ingest("statements/2026/", pattern="**/*.pdf")
print(f"Processed: {len(batch.results)} files")
print(f"Unique transactions: {batch.unique_count}")
```

## 重複排除

べき等なトランザクションハッシュで安全なインクリメンタル取り込みを実現します。

```python
from bankstatementparser import CamtParser, Deduplicator

parser = CamtParser("statement.xml")
dedup = Deduplicator()
result = dedup.deduplicate(dedup.from_dataframe(parser.parse()))

print(f"Unique: {len(result.unique_transactions)}")
print(f"Exact duplicates: {len(result.exact_duplicates)}")
print(f"Suspected matches: {len(result.suspected_matches)}")
```

## トランザクション分類（エンリッチメント）

LLM による自動トランザクション分類を行います。

```python
from bankstatementparser.enrichment import Categorizer

categorizer = Categorizer()
enriched = categorizer.categorize_batch(transactions)
for txn in enriched:
    print(f"{txn.description}: {txn.category}")
```

## 台帳エクスポート（hledger / beancount）

トランザクションをプレーンテキスト会計のジャーナル形式にエクスポートします。

```python
from bankstatementparser.export import to_hledger, to_beancount

journal = to_hledger(transactions, account="Assets:Bank:Checking")
beancount_journal = to_beancount(transactions, account="Assets:Bank:Checking")
```

## マルチ通貨残高検証

通貨グループごとに残高を独立して検証します。

```python
from bankstatementparser.hybrid import verify_balance_multi_currency

results = verify_balance_multi_currency(transactions)
for currency, verification in results.items():
    print(f"{currency}: {verification.status}")
```

## REST API

FastAPI マイクロサービスとしてデプロイします。

```bash
# API サーバーの起動
bankstatementparser-api --port 8000

# コンテナデプロイ用
bankstatementparser-api --host 0.0.0.0 --port 9000
```

エンドポイント:
- `POST /ingest` -- 銀行取引明細書ファイルを解析する
- `GET /health` -- ヘルスチェック

## 安全な ZIP 処理

組み込みのセキュリティチェック（爆弾保護、暗号化エントリ拒否）で ZIP 形式の XML ファイルを処理します。

```python
from bankstatementparser import iter_secure_xml_entries, CamtParser

for entry in iter_secure_xml_entries("statements.zip"):
    parser = CamtParser.from_bytes(entry.xml_bytes, source_name=entry.source_name)
    print(f"{entry.source_name}: {len(parser.parse())} transactions")
```

## エクスポート

```python
parser = CamtParser("statement.xml")
parser.export_csv("output.csv")
parser.export_json("output.json")

# Polars (requires bankstatementparser[polars])
polars_df = parser.to_polars()

# Excel
parser.camt_to_excel("output.xlsx")
```

## CLI の使用法

```bash
# 構造化形式の解析
bankstatementparser --type camt --input statement.xml
bankstatementparser --type pain001 --input payment.xml

# ハイブリッド PDF パイプライン
bankstatementparser --type ingest --input statement.pdf
bankstatementparser --type ingest --input statement.pdf --output ledger.csv

# インタラクティブレビューモード
bankstatementparser --type review --input result.json
bankstatementparser --type review --input result.json --output reviewed.json

# ストリーミングで CSV にエクスポート
bankstatementparser --type camt --input statement.xml --output transactions.csv
bankstatementparser --type camt --input statement.xml --streaming --show-pii
```

CLI オプション:

- `--type {camt,pain001,ingest,review}` -- パーサータイプまたはモード
- `--input <path>` -- 入力ファイル
- `--output <path>` -- エクスポートファイル（CSV または JSON）
- `--streaming` -- 大きなファイルをストリームする
- `--show-pii` -- 機密フィールドを表示する（デフォルトでは秘匿化済み）
- `--max-size <MB>` -- ファイルサイズ制限

## ローカル開発セットアップ

```bash
git clone https://github.com/sebastienrousseau/bankstatementparser.git
cd bankstatementparser
python3 -m venv .venv && source .venv/bin/activate
pip install poetry && poetry install --with dev
make install-hooks   # pre-commit hook runs `make verify` before every commit
```

テストスイートを実行します:

```bash
pytest
```

## API リファレンス

### パーサークラス

| クラス | 形式 | インポート |
|---|---|---|
| `CamtParser` | CAMT.053 (ISO 20022) | `from bankstatementparser import CamtParser` |
| `Pain001Parser` | PAIN.001 (ISO 20022) | `from bankstatementparser import Pain001Parser` |
| `CsvStatementParser` | CSV | `from bankstatementparser import CsvStatementParser` |
| `OfxParser` | OFX | `from bankstatementparser import OfxParser` |
| `QfxParser` | QFX | `from bankstatementparser import QfxParser` |
| `Mt940Parser` | MT940 | `from bankstatementparser import Mt940Parser` |
| `smart_ingest()` | PDF（ハイブリッドパイプライン） | `from bankstatementparser.hybrid import smart_ingest` |

### ユーティリティ関数

| 関数 | 目的 |
|---|---|
| `detect_statement_format(path)` | ファイル形式を自動検出 |
| `create_parser(path, fmt)` | 適切なパーサーを作成する |
| `parse_files_parallel(paths)` | 複数のファイルを同時に解析する |
| `iter_secure_xml_entries(zip_path)` | ZIP エントリを安全に反復処理する |
| `smart_ingest(path)` | 検証付きハイブリッド PDF 抽出 |
| `scan_and_ingest(dir, pattern)` | 一括ディレクトリスキャン |
| `verify_balance_multi_currency(txns)` | 通貨ごとの残高検証 |
| `to_hledger(txns, account)` | hledger ジャーナル形式にエクスポート |
| `to_beancount(txns, account)` | beancount ジャーナル形式にエクスポート |

### データクラス

| クラス | 目的 |
|---|---|
| `Deduplicator` | 重複トランザクションを検出する |
| `DeduplicationResult` | 一意、完全一致、疑わしい一致を含む結果 |
| `InputValidator` | ファイルパスと形式を検証する |
| `Transaction` | 正規化された取引レコード |
| `FileResult` | 並列解析の結果 |
| `ZipXMLSource` | ZIP メンバーラッパー |
| `IngestResult` | 検証付きハイブリッドパイプライン結果 |
| `VerificationResult` | 残高検証の結果 |
| `Categorizer` | LLM によるトランザクション分類 |
| `AccountMapper` | 正規表現ベースのアカウントマッピングルール |

### 例外

| 例外 | 発生条件 |
|---|---|
| `ParserError` | 解析の失敗 |
| `ExportError` | エクスポートの失敗（CSV/JSON/Excel） |
| `ValidationError` | 入力検証の失敗 |
| `ZipSecurityError` | ZIP セキュリティチェックの失敗 |
