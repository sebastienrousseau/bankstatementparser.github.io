---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "銀行取引明細書パーサーの変更ログ"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 銀行取引明細書パーサー。無断転載を禁じます。"
date: "Apr 01, 2026"
description: "Bank Statement Parser のリリース履歴と変更ログ。すべてのバージョンにわたる新機能、改善点、バグ修正を追跡します。"
download: ""
format-detection: "telephone=no"
hreflang: "ja"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/ja/henkou-rireki/index.html"
image_alt: "Bank Statement Parser のロゴ、シームレスなデータ抽出で財務分析を強化"
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "銀行取引明細書パーサーの変更ログ、リリースノート、バージョン履歴、更新"
language: "ja-JP"
layout: "about"
locale: "ja_JP"
logo_alt: "Bank Statement Parser のロゴ、シームレスなデータ抽出で財務分析を強化"
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "変更履歴"
permalink: "https://bankstatementparser.com/ja/henkou-rireki/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "リリース履歴と新機能"
tags: "変更ログ、リリース、アップデート、バージョン、お知らせ、ブログ"
theme_color: "rgb(73, 214, 251)"
title: "銀行取引明細書パーサーの変更ログ"
url: "https://bankstatementparser.com/ja/henkou-rireki/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/ja/henkou-rireki/rss.xml"
category: "財務ソフトウェア、Python ライブラリ、データ処理"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin (version 0.0.20)"
item_description: "Bank Statement Parser のリリース履歴と変更ログ。すべてのバージョンにわたる新機能、改善点、バグ修正を追跡します。"
item_guid: "https://bankstatementparser.com/ja/henkou-rireki/rss.xml"
item_link: "https://bankstatementparser.com/ja/henkou-rireki/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "銀行取引明細書パーサーの変更ログ"
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
apple-mobile-web-app-title: "銀行取引明細書パーサーの変更ログ"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Bank Statement Parser のリリース履歴と変更ログ。すべてのバージョンにわたる新機能、改善点、バグ修正を追跡します。"
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Bank Statement Parser のロゴ、シームレスなデータ抽出で財務分析を強化"
twitter_site: "@wwdseb"
twitter_title: "銀行取引明細書パーサーの変更ログ"
twitter_url: "https://bankstatementparser.com/ja/henkou-rireki/index.html"

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

Bank Statement Parser の開発をフォローしてください。 [RSS](/changelog/rss.xml) 経由で購読するか、[GitHub リポジトリ](https://github.com/sebastienrousseau/bankstatementparser) リリース通知用。

## v0.0.4 — 2026-03-15 (最新)

- 並列ファイル解析を追加しました`parse_files_parallel()`ProcessPoolExecutor を使用します。
- メモリ制限のある大きな PAIN.001 ファイル (50 MB 以上) に対する真のストリーミングを追加しました。
- パフォーマンスの最適化: CAMT スループットは 27,000 tx/s を超え、PAIN.001 は 52,000 tx/s を超えています。
- 追加した`Deduplicator`完全な重複と疑わしい一致を信頼スコアで検出するためのクラス。
- 追加した`from_string()`そして`from_bytes()`ディスク I/O を使用しないメモリ内解析のメソッド。
- 追加した`iter_secure_xml_entries()`安全な ZIP アーカイブ処理用。
- パフォーマンスしきい値を強制する拡張 CI。

## v0.0.3 — 2025-11-20

- CSV、OFX、QFX、MT940 パーサーのサポートを追加しました。
- 形式の自動検出を追加しました`detect_statement_format()`そして`create_parser()`。
- PII 編集を追加しました (CLI およびストリーミング モードではデフォルトでオン)。
- CSV、JSON、Excel 用のエクスポート ヘルパーを追加しました。
- オプションの Polars DataFrame サポートを追加しました。
- テスト スイートを 100% ブランチ カバレッジの 467 テストに拡張しました。

## v0.0.2 — 2025-06-10

- PAIN.001 パーサーを追加 (`Pain001Parser`) ISO 20022 単位転送開始ファイル用。
- CLI インターフェースを追加 (`python -m bankstatementparser.cli`）。
- ストリーミングモードを追加しました`parse_streaming()`。
- 入力検証とファイル サイズ制限を追加しました。

## v0.0.1 — 2025-01-15

- 初期リリース。
- CAMT.053 パーサー (`CamtParser`) ISO 20022 の銀行から顧客への取引明細書用。
- パンダのデータフレーム出力。
- 基本的な XML セキュリティ強化 (XXE 保護、no_network)。

[GitHub]() で完全なコミット履歴を表示します。https://github.com/sebastienrousseau/bankstatementparser/commits/main).

<script type="application/ld+json">
{
  "@コンテキスト": "https://schema.org"、
  "@type": "ソフトウェアアプリケーション",
  "名前": "銀行取引明細書パーサー",
  "applicationCategory": "開発者アプリケーション",
  "operatingSystem": "クロスプラットフォーム",
  "ソフトウェアバージョン": "0.0.4",
  "公開日": "2026-03-15",
  "releaseNotes": "並列ファイル解析、PAIN.001 の真のストリーミング、パフォーマンスの最適化 (27K+ tx/s CAMT、52K+ tx/s PAIN.001)、Deduplicator クラス、メモリ内解析、安全な ZIP 処理を追加しました。",
  "ダウンロードURL": "https://pypi.org/project/bankstatementparser/"、
  「ライセンス」: "https://opensource.org/licenses/Apache-2.0"、
  「著者」: {
    "@type": "人",
    "名前": "セバスチャン・ルソー"
  }
}
</script>
