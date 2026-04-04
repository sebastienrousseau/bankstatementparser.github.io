---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "黒い窓のある白い建物"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/daniele-franchi-Vl6YuVBLEys.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 銀行取引明細書パーサー。無断転載を禁じます。"
date: "Apr 01, 2026"
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

＃＃ 要件

- Python 3.9 ～ 3.14
- ターミナルアクセス (macOS、Linux、または WSL)

＃＃ インストール

```bash
pip install bankstatementparser
```

Polars DataFrame サポートの場合:

```bash
pip install bankstatementparser[polars]
```

## クイックスタート

### あらゆる形式を自動検出して解析

```python
from bankstatementparser import create_parser, detect_statement_format

fmt = detect_statement_format("transactions.ofx")
parser = create_parser("transactions.ofx", fmt)
df = parser.parse()  # pandas DataFrame
print(df.head())
```

これは、`.xml`(CAMT/ペイン.001)、`.csv`, `.ofx`, `.qfx`, `.mt940`、 そして`.sta`ファイル。

### CAMT.053 を解析する

```python
from bankstatementparser import CamtParser

parser = CamtParser("statement.xml")
transactions = parser.parse()
```

### PAIN.001を解析する

```python
from bankstatementparser import Pain001Parser

parser = Pain001Parser("payment.xml")
payments = parser.parse()
```

## 大きなファイルのストリーミング

数千のトランザクションを含むファイルの場合は、ストリーミングを使用してメモリの制限を維持します。

```python
parser = CamtParser("large_statement.xml")
for transaction in parser.parse_streaming(redact_pii=True):
    process(transaction)  # Memory stays constant
```

## インメモリ解析

ディスク I/O を使用せずにバイトから解析します -- SFTP または API ワークフローに役立ちます。

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

## 重複排除

信頼スコアを使用して、完全な重複と疑わしい一致を検出します。

```python
from bankstatementparser import CamtParser, Deduplicator

parser = CamtParser("statement.xml")
dedup = Deduplicator()
result = dedup.deduplicate(dedup.from_dataframe(parser.parse()))

print(f"Unique: {len(result.unique_transactions)}")
print(f"Exact duplicates: {len(result.exact_duplicates)}")
print(f"Suspected matches: {len(result.suspected_matches)}")
```

## 安全な ZIP 処理

組み込みのセキュリティ チェック (爆弾保護、暗号化されたエントリの拒否) を使用して、圧縮された XML ファイルを処理します。

```python
from bankstatementparser import iter_secure_xml_entries, CamtParser

for entry in iter_secure_xml_entries("statements.zip"):
    parser = CamtParser.from_bytes(entry.xml_bytes, source_name=entry.source_name)
    print(f"{entry.source_name}: {len(parser.parse())} transactions")
```

＃＃ 輸出

```python
parser = CamtParser("statement.xml")
parser.export_csv("output.csv")
parser.export_json("output.json")

# Polars (requires bankstatementparser[polars])
polars_df = parser.to_polars()
```

## CLI の使用法

```bash
# Parse and display
python -m bankstatementparser.cli --type camt --input statement.xml

# Export to CSV
python -m bankstatementparser.cli --type camt --input statement.xml --output transactions.csv

# Stream with PII visible
python -m bankstatementparser.cli --type camt --input statement.xml --streaming --show-pii
```

CLI オプション:

- `--type {camt,pain001}`-- パーサーの種類
-`--input <path>`-- 入力ファイル
-`--output <csv_path>`-- CSV にエクスポート
-`--streaming`-- 大きなファイルをストリームする
-`--show-pii`-- 機密フィールドを表示します (デフォルトでは編集されています)
-`--max-size <MB>`-- ファイルサイズ制限

## ローカル開発セットアップ

```bash
git clone https://github.com/sebastienrousseau/bankstatementparser.git
cd bankstatementparser
python3 -m venv .venv && source .venv/bin/activate
pip install poetry && poetry install --with dev
```

テスト スイートを実行します。

```bash
pytest
```

## API リファレンス

### パーサークラス

| クラス | 形式 | 輸入 |
|---|---|---|
| `CamtParser` | CAMT.053 (ISO 20022) | `from bankstatementparser import CamtParser` |
| `Pain001Parser` | 痛み.001 (ISO 20022) | `from bankstatementparser import Pain001Parser` |
| `CsvStatementParser` | CSV | `from bankstatementparser import CsvStatementParser` |
| `OfxParser` | OFX | `from bankstatementparser import OfxParser` |
| `QfxParser` | QFX | `from bankstatementparser import QfxParser` |
| `Mt940Parser` | MT940 | `from bankstatementparser import Mt940Parser` |

### ユーティリティ関数

| 関数 | 目的 |
|---|---|
| `detect_statement_format(path)` | ファイル形式を自動検出 |
| `create_parser(path, fmt)` | 適切なパーサーを作成する |
| `parse_files_parallel(paths)` | 複数のファイルを同時に解析する |
| `iter_secure_xml_entries(zip_path)` | ZIP エントリを安全に反復処理する |

### データクラス

| クラス | 目的 |
|---|---|
| `Deduplicator` | 重複したトランザクションを検出する |
| `DeduplicationResult` | 一意の一致、完全一致、および疑わしい一致を含む結果 |
| `InputValidator` | ファイルのパスと形式を検証する |
| `Transaction` | 正規化された取引記録 |
| `FileResult` | 並列解析の結果 |
| `ZipXMLSource` | ZIP メンバー ラッパー |

### 例外

| 例外 | 育てたとき |
|---|---|
| `ParserError` | 解析の失敗 |
| `ExportError` | エクスポートの失敗 (CSV/JSON/Excel) |
| `ValidationError` | 入力検証の失敗 |
| `ZipSecurityError` | ZIP セキュリティ チェックの失敗 |
