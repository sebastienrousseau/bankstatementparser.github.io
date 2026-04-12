---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "銀行取引明細書パーサーのセキュリティ"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 銀行取引明細書パーサー。無断転載を禁じます。"
date: "Apr 11, 2026"
description: "Bank Statement Parser のセキュリティ機能: XXE 保護、ZIP 爆弾強化、PII 編集、サプライ チェーン セキュリティ、確定的出力、および署名済みビルド。"
download: ""
format-detection: "telephone=no"
hreflang: "ja"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/ja/security/index.html"
image_alt: "Bank Statement Parser のロゴ、シームレスなデータ抽出で財務分析を強化"
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "銀行取引明細書セキュリティ、PII 編集 Python、XXE 保護、ZIP 爆弾保護、サプライ チェーン セキュリティ SBOM、決定論的解析、金融データ セキュリティ"
language: "ja-JP"
layout: "about"
locale: "ja_JP"
logo_alt: "Bank Statement Parser のロゴ、シームレスなデータ抽出で財務分析を強化"
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "安全"
permalink: "https://bankstatementparser.com/ja/security/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "お客様の財務データをどのように保護するか"
tags: "セキュリティ、pii、xxe、sbom、サプライチェーン、決定論的"
theme_color: "rgb(73, 214, 251)"
title: "銀行取引明細書パーサーのセキュリティ: データ保護とサプライ チェーン"
url: "https://bankstatementparser.com/ja/security/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/ja/security/rss.xml"
category: "財務ソフトウェア、Python ライブラリ、データ処理"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin (version 0.0.20)"
item_description: "Bank Statement Parser のセキュリティ機能: XXE 保護、ZIP 爆弾強化、PII 編集、サプライ チェーン セキュリティ、確定的出力、および署名済みビルド。"
item_guid: "https://bankstatementparser.com/ja/security/rss.xml"
item_link: "https://bankstatementparser.com/ja/security/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "銀行取引明細書パーサーのセキュリティ: データ保護とサプライ チェーン"
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
apple-mobile-web-app-title: "銀行取引明細書パーサーのセキュリティ: データ保護とサプライ チェーン"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Bank Statement Parser のセキュリティ機能: XXE 保護、ZIP 爆弾強化、PII 編集、サプライ チェーン セキュリティ、確定的出力、および署名済みビルド。"
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Bank Statement Parser のロゴ、シームレスなデータ抽出で財務分析を強化"
twitter_site: "@wwdseb"
twitter_title: "銀行取引明細書パーサーのセキュリティ: データ保護とサプライ チェーン"
twitter_url: "https://bankstatementparser.com/ja/security/index.html"

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

**TL;DR:** Bank Statement Parser はすべてのデータをローカルで処理し、デフォルトで PII を秘匿化し、XXE 攻撃に対して XML 解析を強化し、LLM を Ollama 経由でローカル実行し、SHA-256 ハッシュロック依存関係と CycloneDX SBOM を同梱しています。

## 設計によるセキュリティ

Bank Statement Parser は、機密の財務データを処理するために構築されています。すべての設計上の決定は、セキュリティ、プライバシー、監査可能性を優先します。

## ゼロクラウド依存

すべての処理はランタイム内でローカルに行われます。確定的パーサーはネットワーク呼び出しを一切行いません。ハイブリッド PDF パイプラインは Ollama を使用してローカル LLM 推論を行います。クラウド API にデータが送信されることはありません。XML パーサーは `no_network=True`、`resolve_entities=False`、`load_dtd=False` で明示的に構成され、送信アクセスを防止します。

## PII 秘匿化

個人を特定できる情報（名前、IBAN、住所）は、CLI 出力およびストリーミングモードで自動的に秘匿化されます。デフォルトでオンです。

- **CLI**: 機密フィールドは `***REDACTED***` と表示されます
- **ストリーミング**: `parse_streaming(redact_pii=True)`（デフォルト）
- **エクスポート**: CSV/JSON/Excel は後続処理のために完全なデータを保持します
- **オプトイン**: 秘匿化されていない出力が必要な場合は `--show-pii` または `redact_pii=False` を使用します

## XML セキュリティ（XXE 保護）

すべての XML 解析は `lxml` の強化設定を使用します:

- `resolve_entities=False` -- XML エンティティ拡張攻撃を防止
- `no_network=True` -- パーサーからのすべての送信ネットワークアクセスをブロック
- `load_dtd=False` -- DTD ベースの攻撃を防止
- 処理前の名前空間除去 -- あらゆる CAMT.053 バリアントを安全に処理

## ZIP アーカイブのセキュリティ

`iter_secure_xml_entries()` は抽出前にすべての ZIP メンバーを検証します:

- **エントリサイズ上限**: エントリあたり 10 MB（構成可能）
- **合計サイズ上限**: 非圧縮で合計 50 MB（構成可能）
- **圧縮率制限**: デフォルト 100:1 -- ZIP 爆弾を検出
- **暗号化エントリの拒否**: 暗号化エントリは警告とともにスキップ
- **ディスク書き込みなし**: XML バイトは `from_bytes()` でパーサーに直接渡されます

## パストラバーサル防止

入力検証により危険なファイルパスをブロックします:

- Null バイト、ディレクトリトラバーサルパターン（`../`）、シンボリックリンクは拒否
- 想定される形式に対するファイル拡張子の検証
- ファイルサイズ制限（デフォルト 100 MB、構成可能）

## 残高検証（ゴールデンルール）

すべての PDF 抽出は `opening balance + credits − debits == closing balance` の式で検証されます。結果は VERIFIED、DISCREPANCY、FAILED とタグ付けされます。不一致は `--type review` でインタラクティブにレビューできます。

## 確定的出力

構造化形式（CAMT、PAIN.001、CSV、OFX、QFX、MT940）の場合、同じ入力ファイルを指定すると、パーサーは毎回バイト同一の出力を生成します。ランダム性、モデル推論、ヒューリスティックサンプリングはありません。これは以下の場面で重要です:

- **監査の再現性**: 同じファイルを 2 回実行し、出力を diff する
- **規制遵守**: 一貫した処理を実証する
- **CI 検証**: 718 テストが 100% ブランチカバレッジで確定性を強制

## サプライチェーンセキュリティ

- **SHA-256 ハッシュロック依存関係**: `poetry.lock` のすべてのパッケージでファイルハッシュを検証済み
- **CycloneDX SBOM**: すべてのリリースにソフトウェア部品表が含まれます
- **GitHub ビルド来歴**: アテステーションが各アーティファクトをソースコミットにリンク
- **署名付きコミット**: すべてのコミットは SSH 署名され、CI で検証されます
- **依存関係検証**: `scripts/verify_locked_hashes.py` がすべてのハッシュをローカルで検証

## ローカルで検証する

```bash
python -m pytest                          # 718 tests, 100% branch coverage
python scripts/verify_locked_hashes.py    # SHA-256 hash verification
git log --show-signature -1               # Verify commit signature
```
