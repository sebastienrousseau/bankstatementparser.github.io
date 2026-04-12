---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "ISO 20022 移行ガイド"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 銀行取引明細書パーサー。無断転載を禁じます。"
date: "Apr 11, 2026"
description: "SWIFT ISO 20022 移行タイムライン (2026 ～ 2028 年)、MT940 から CAMT.053 への移行、および Bank Statement Parser が財務チームの移行にどのように役立つかについての実践的なガイドです。"
download: ""
format-detection: "telephone=no"
hreflang: "ja"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/ja/migration/index.html"
image_alt: "Bank Statement Parser のロゴ、シームレスなデータ抽出で財務分析を強化"
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "ISO 20022 移行、MT940 から CAMT.053、SWIFT 期限 2027、MT940 廃止 2028、銀行取引明細書移行 Python、CAMT.053 パーサー、ISO 20022 タイムライン"
language: "ja-JP"
layout: "about"
locale: "ja_JP"
logo_alt: "Bank Statement Parser のロゴ、シームレスなデータ抽出で財務分析を強化"
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "ISO 20022 移行ガイド"
permalink: "https://bankstatementparser.com/ja/migration/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "SWIFT MT から ISO 20022 への移行をナビゲートする"
tags: "iso20022,移行,mt940,camt053,swift,タイムライン"
theme_color: "rgb(73, 214, 251)"
title: "ISO 20022 移行ガイド: MT940 から CAMT.053 への移行"
url: "https://bankstatementparser.com/ja/migration/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/ja/migration/rss.xml"
category: "財務ソフトウェア、Python ライブラリ、データ処理"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin (version 0.0.20)"
item_description: "SWIFT ISO 20022 移行タイムライン (2026 ～ 2028 年)、MT940 から CAMT.053 への移行、および Bank Statement Parser が財務チームの移行にどのように役立つかについての実践的なガイドです。"
item_guid: "https://bankstatementparser.com/ja/migration/rss.xml"
item_link: "https://bankstatementparser.com/ja/migration/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "ISO 20022 移行ガイド: MT940 から CAMT.053 への移行"
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
apple-mobile-web-app-title: "ISO 20022 移行ガイド: MT940 から CAMT.053 への移行"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "SWIFT ISO 20022 移行タイムライン (2026 ～ 2028 年)、MT940 から CAMT.053 への移行、および Bank Statement Parser が財務チームの移行にどのように役立つかについての実践的なガイドです。"
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Bank Statement Parser のロゴ、シームレスなデータ抽出で財務分析を強化"
twitter_site: "@wwdseb"
twitter_title: "ISO 20022 移行ガイド: MT940 から CAMT.053 への移行"
twitter_url: "https://bankstatementparser.com/ja/migration/index.html"

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

**TL;DR:** SWIFT は 2028 年 11 月までに MT940 を廃止します。Bank Statement Parser は MT940 と CAMT.053 の両方を単一の API で処理するため、解析パイプラインは移行中もその後も機能します。

## この移行が重要な理由

SWIFT は、より充実した ISO 20022 標準を支持して、レガシーの MT メッセージ形式を廃止します。財務チームにとって、これは銀行取引明細書処理パイプラインを期限までに MT940 から CAMT.053 へ進化させる必要があることを意味します。

## SWIFT 移行タイムライン

| 日付 | マイルストーン | 影響 |
|---|---|---|
| **2025 年 11 月** | クロスボーダー決済における MT-MX 共存が終了 | PACS メッセージは ISO 20022 のみに |
| **2026 年 11 月** | 構造化/ハイブリッドアドレスが必須。MT101 複数命令が拒否。ケースマネジメントフェーズ 1 | アドレス形式の準拠が必要。一部の MT メッセージが拒否される |
| **2026 年後半** | CAMT.052/.053/.054 受信のオプトイン開始 | 金融機関がネイティブ ISO 明細書の受信を開始可能 |
| **2027 年 11 月** | すべての FI が CAMT.053 をネイティブに受信する必要あり | SWIFT が MT 形式の ISO への変換を停止。システムが CAMT を直接解析する必要あり |
| **2028 年 11 月** | MT940/MT942/MT950/MT900/MT910 が完全廃止 | レガシー明細書形式は利用不可。CAMT.052/.053/.054 が唯一の選択肢 |

## コードの変更点

### 変更前: MT940 のみ

```python
from bankstatementparser import Mt940Parser

parser = Mt940Parser("statement.mt940")
df = parser.parse()
```

### 変更後: 自動検出で両方の形式に対応

```python
from bankstatementparser import create_parser, detect_statement_format

fmt = detect_statement_format("statement.xml")  # or .mt940
parser = create_parser("statement.xml", fmt)
df = parser.parse()  # Same DataFrame schema regardless of format
```

`detect_statement_format()` 関数がファイルが MT940、CAMT.053、PAIN.001、その他のサポート形式のいずれかを識別します。`create_parser()` 関数が適切なパーサーを返します。後続のコードはソース形式に関係なく同一に動作します。

## CAMT.053 vs MT940: 主な違い

| 特徴 | MT940 | CAMT.053 |
|---|---|---|
| データの豊富さ | 限られたフィールド | トランザクションあたり 3〜5 倍のデータ |
| 文字セット | 制限あり（SWIFT 文字セット） | 完全な Unicode |
| 構造 | タグ付きフラットテキスト | 名前空間付き XML |
| 残高レポート | 期首/期末のみ | 複数の残高タイプ |
| 参照情報 | 単一の参照フィールド | 複数の参照タイプ |
| 通貨の取り扱い | 基本的 | 為替レートを含む完全なマルチ通貨 |

## Bank Statement Parser がどのように役立つか

- **統合 API**: MT940、CAMT.053、PDF 明細書を同じワークフローで解析し、一貫した DataFrame 出力を生成します。
- **自動検出**: 事前に形式を知る必要はありません。`detect_statement_format()` が自動的に識別します。
- **ハイブリッド PDF パイプライン**: 移行中に構造化エクスポートを提供しない銀行の PDF 明細書を `smart_ingest()` が自動残高検証で処理します。
- **名前空間非依存**: 設定なしであらゆる CAMT.053 バリアント（001.02、001.04、銀行固有のラッパー）を処理します。
- **マルチ通貨検証**: `verify_balance_multi_currency()` が通貨グループごとにゴールデンルールを実行します。マルチ通貨 CAMT 明細書に不可欠です。
- **ストリーミング**: 制限されたメモリで大規模な CAMT ファイル（50 MB+、50K+ トランザクション）を処理します。
- **台帳エクスポート**: 財務会計用に hledger や beancount ジャーナル形式に直接エクスポートします。
- **移行テスト**: 切り替え前に、同じ日付範囲で両方のパーサーを並べて実行し、出力の一貫性を確認します。

## はじめる

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

構造化 CAMT エクスポートをまだ提供していない銀行の PDF 明細書の場合:

```python
from bankstatementparser.hybrid import smart_ingest

result = smart_ingest("statement.pdf")
assert result.verification.status == "VERIFIED"
```

[完全なドキュメントを読む](/getting-started/index.html)

[代替案と比較 ❯](/comparison/index.html) | [実際のユースケースを参照 ❯](/use-cases/index.html)
