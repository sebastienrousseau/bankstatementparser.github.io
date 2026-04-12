---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Bank Statement Parser に関するよくある質問"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 銀行取引明細書パーサー。無断転載を禁じます。"
date: "Apr 11, 2026"
description: "Bank Statement Parser に関するよくある質問への回答: データ プライバシー、PII 編集、パフォーマンス、ISO 20022 サポート、ストリーミング、コンプライアンス、財務ワークフロー。"
download: ""
format-detection: "telephone=no"
hreflang: "ja"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/ja/faq/index.html"
image_alt: "Bank Statement Parser のロゴ。迅速かつ正確な財務データ処理と洞察の抽出のために設計された強力な Python ツールです。"
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "銀行取引明細書パーサーの FAQ、CAMT パーサーの質問、PAIN.001 FAQ、ISO 20022 Python FAQ、PII 編集バンキング、銀行パーサーのパフォーマンス、財務データのプライバシー、MT940 パーサーの FAQ、ストリーミング パーサー Python、銀行取引明細書のコンプライアンス"
language: "ja-JP"
layout: "faq"
locale: "ja_JP"
logo_alt: "Bank Statement Parser のロゴ。迅速かつ正確な財務データ処理と洞察の抽出のために設計された強力な Python ツールです。"
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "よくある質問"
permalink: "https://bankstatementparser.com/ja/faq/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Bank Statement Parser に関するよくある質問"
tags: "FAQ、銀行、ステートメント、パーサー、プライバシー、コンプライアンス、パフォーマンス、ストリーミング、iso20022、Python"
theme_color: "rgb(73, 214, 251)"
title: "Bank Statement Parser FAQ: プライバシー、パフォーマンス、および使用法"
url: "https://bankstatementparser.com/ja/faq/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/ja/faq/rss.xml"
category: "財務ソフトウェア、Python ライブラリ、よくある質問"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin (version 0.0.20)"
item_description: "Bank Statement Parser に関するよくある質問への回答: データ プライバシー、PII 編集、パフォーマンス、ISO 20022 サポート、ストリーミング、コンプライアンス、財務ワークフロー。"
item_guid: "https://bankstatementparser.com/ja/faq/rss.xml"
item_link: "https://bankstatementparser.com/ja/faq/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Bank Statement Parser FAQ: プライバシー、パフォーマンス、および使用法"
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
apple-mobile-web-app-title: "Bank Statement Parser FAQ: プライバシー、パフォーマンス、および使用法"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Bank Statement Parser に関するよくある質問への回答: データ プライバシー、PII 編集、パフォーマンス、ISO 20022 サポート、財務ワークフロー。"
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Bank Statement Parser のロゴ。迅速かつ正確な財務データ処理と洞察の抽出のために設計された強力な Python ツールです。"
twitter_site: "@wwdseb"
twitter_title: "Bank Statement Parser FAQ: プライバシー、パフォーマンス、および使用法"
twitter_url: "https://bankstatementparser.com/ja/faq/index.html"

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

## データプライバシーとコンプライアンス

### インフラストラクチャからデータが流出することはありますか?

**いいえ — PDF 抽出においてもです。** Bank Statement Parser はステートレスライブラリとして動作します。すべての処理（解析、PII 秘匿化、アーカイブ抽出）はローカルのランタイムメモリ内で行われます。ハイブリッド PDF パイプラインは Ollama を使用してローカル LLM 推論を行います。クラウド API は使用しません。XML パーサーは `no_network=True` で強化されており、パーサーレベルですべての送信アクセスをブロックします。財務データが環境から離れることはありません。

### PII 秘匿化はどのように機能しますか?

機密フィールドは、アプリケーションロジックに到達する前にマスクされます。パーサーは債務者名、債権者名、IBAN、住所を識別し、コンソール出力およびストリーミングモードで `***REDACTED***` に置き換えます。

- **秘匿化は CLI 出力およびストリーミングモードでデフォルトでオンです**。
- **ファイルエクスポート**（CSV、JSON、Excel）は後続処理のために秘匿化されていないデータを保持します。
- **オプトイン**で完全なデータを取得するには、CLI で `--show-pii`、API で `redact_pii=False` を使用します。

### 抽出プロセスは確定的ですか?

**構造化形式では「はい」— 実行するたびにバイト同一の出力が得られます。** 同じ入力ファイルを指定すると、確定的パーサー（CAMT、PAIN.001、CSV、OFX、QFX、MT940）は毎回同じ結果を生成します。ランダム性、モデル推論、ヒューリスティックサンプリングはありません。

ハイブリッド PDF パイプラインでは、LLM ベースの抽出パスで実行間にわずかな差異が生じる場合があります。そのため、すべての PDF 抽出は**ゴールデンルール**（`opening + credits − debits == closing`）で検証され、フラグされた不一致はインタラクティブにレビューできます。

CI は Hypothesis によるプロパティベースファジングを含む、100% ブランチカバレッジの 718 テストで確定性を強制します。

### プロジェクトはどのようなコンプライアンス基準に従っていますか?

プロジェクトは、完全なトレーサビリティを備えた ISO 13485 準拠のドキュメントを維持しています。

- 重大度/確率スコアリングと残留リスク評価を備えた定量化された**リスクレジスタ**。
- 5 フェーズにわたる 19 のゲートステップを含む**検証・妥当性確認計画**。
- 影響評価とロールバックプロトコルを含む**変更管理手順**。
- リスクレベルと EOL 追跡を伴うすべての依存関係をカバーする **SOUP レジスタ**。
- 設計入力を実装および検証にマッピングする**トレーサビリティマトリックス**。

すべてのリリースには CycloneDX SBOM、SHA-256 チェックサム、GitHub ビルド来歴証明書が含まれています。

## パフォーマンスとスケーラビリティ

### Bank Statement Parser の速度はどれくらいですか?

パフォーマンスしきい値は、コミットごとに CI で検証されます。

| 指標 | 値 |
|---|---|
| CAMT.053 スループット | 27,000+ トランザクション/秒 |
| PAIN.001 スループット | 52,000+ トランザクション/秒 |
| トランザクションあたりのレイテンシ（CAMT） | 37 マイクロ秒 |
| トランザクションあたりのレイテンシ（PAIN.001） | 19 マイクロ秒 |
| 最初の結果が得られるまでの時間 | < 2 ms |

PDF 抽出速度はルーティングパスによります: 確定的（1 秒未満）、テキスト LLM（数秒）、ビジョン LLM（ページあたり数秒）。

### 大きなファイルはどのように処理されますか?

**制限されたメモリでのストリーミング — ファイルあたり 50,000 トランザクションでテスト済みです。** `parse_streaming()` で XML ファイルを段階的に処理します。各トランザクションは辞書として生成され、処理後に要素がクリアされるためメモリの増加を防ぎます。メモリはファイルサイズに比例しません — 50K トランザクションテスト（25 MB+）は 10K トランザクションテストの 2 倍未満のメモリを使用します。

50 MB を超えるファイル（例: 100K+ 件の支払いを含むホスト間 PAIN.001 バッチ）の場合、パーサーはチャンクベースの名前空間ストリッピングで一時ファイルをストリーミングします。完全なドキュメントがメモリにロードされることはありません。

### ZIP アーカイブはどのように安全に処理されますか?

`iter_secure_xml_entries()` は抽出前に各メンバーを検証します。

- **エントリサイズ上限**（デフォルト: エントリあたり 10 MB）
- **非圧縮合計サイズ上限**（デフォルト: 50 MB）
- **圧縮率制限**（デフォルト: 100:1）で ZIP 爆弾を防止
- **暗号化エントリの拒否**

ファイルはディスクに書き込まれません。XML バイトは `from_bytes()` でパーサーに直接渡されます。

### 複数のファイルを並列で解析できますか?

**はい。** `parse_files_parallel()` が `ProcessPoolExecutor` に作業を分散します:

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

一括 PDF 取り込みには、`scan_and_ingest()` がフォルダツリー全体を自動重複排除で処理します。

## サポートされている形式

### どの銀行取引明細書形式がサポートされていますか?

| 形式 | 標準 | ファイルの種類 | パーサー/メソッド |
|---|---|---|---|
| CAMT.053 | ISO 20022 銀行対顧客明細書 | `.xml` | `CamtParser` |
| PAIN.001 | ISO 20022 送金指図 | `.xml` | `Pain001Parser` |
| CSV | 一般的な銀行エクスポート | `.csv` | `CsvStatementParser` |
| OFX | Open Financial Exchange | `.ofx` | `OfxParser` |
| QFX | Quicken Financial Exchange | `.qfx` | `QfxParser` |
| MT940 | SWIFT 標準 | `.mt940`, `.sta` | `Mt940Parser` |
| PDF | デジタルおよびスキャン明細書 | `.pdf` | `smart_ingest()` |

### ハイブリッド PDF パイプラインはどのように動作しますか?

ハイブリッドパイプライン（v0.0.5+）は PDF を 3 つの抽出パスにインテリジェントに振り分けます。

- **パス A（確定的）**: 構造化 PDF テーブルを直接解析します。無料で最速、LLM 不要です。
- **パス B（テキスト LLM）**: 複雑なレイアウトのデジタル PDF をローカル LLM（LiteLLM/Ollama）で抽出します。
- **パス C（ビジョン LLM）**: スキャンやコピーされた明細書をマルチモーダルビジョンモデルで処理します。

すべての抽出はゴールデンルール（`opening + credits − debits == closing`）で検証されます。不一致は `--type review` でインタラクティブにレビューできます。

### パーサーは CAMT.053 の銀行固有の方言を処理しますか?

**はい — 設計上名前空間に依存しません。** パーサーは処理前に XML 名前空間を除去し、あらゆる CAMT.053 バリアント（`camt.053.001.02`、`camt.053.001.04`、または独自の銀行ラッパー）を名前空間固有の設定なしで処理します。XPath クエリは名前空間 URI ではなく要素構造を対象とします。

CAMT をカスタムエンベロープでラップする銀行の場合は、`from_string()` または `from_bytes()` で内部ドキュメントを直接渡してください。

### カスタム CSV 列ヘッダーを標準スキーマにマップできますか?

**はい — 自動正規化、設定不要です。** `CsvStatementParser` は一般的なヘッダーのバリエーションを認識します: `"Date"`、`"Transaction Date"`、`"Booking Date"` はすべて `date` フィールドにマップされます。`"Amount"`、`"Value"`、`"Sum"` は `amount` にマップされます。貸方/借方の分割列（例: `"Credit"` と `"Debit"`）は検出され、単一の符号付き金額に自動結合されます。

### 出力形式は何ですか?

すべてのパーサーは、一貫した列タイプを持つ標準化された pandas DataFrame を生成します。

| 形式 | 主要カラム |
|---|---|
| **CAMT** | `Amount`, `Currency`, `DrCr`, `Debtor`, `Creditor`, `Reference`, `ValDt`, `BookgDt`, `AccountId` |
| **PAIN.001** | `PmtInfId`, `PmtMtd`, `InstdAmt`, `Currency`, `CdtrNm`, `EndToEndId`, `MsgId`, `CreDtTm`, `NbOfTxs` |
| **CSV/OFX/QFX/MT940** | `date`, `description`, `amount`（正規化済み） |

CSV、JSON、Excel、Polars DataFrame、hledger、beancount ジャーナル形式にもエクスポートできます。

## PDF と LLM の機能

### ハイブリッドパイプラインはどの LLM モデルをサポートしていますか?

パイプラインはモデル抽象化レイヤーとして LiteLLM を使用し、ビジョンプロンプト用に直接 Ollama ブリッジを備えています。推奨モデル:

- **テキスト抽出**: LiteLLM 互換の任意のモデル（ローカルまたはリモート）。
- **ビジョン抽出**: `ollama/minicpm-v`（推奨）。スキャン PDF 向けです。
- **分類**: LiteLLM 互換の任意のモデル。

すべてのモデルは Ollama 経由で 100% ローカル実行可能です。API キーは不要です。

### ゴールデンルール検証とは何ですか?

すべての PDF 抽出は `opening balance + credits − debits == closing balance` の式で検証されます。結果は以下のようにタグ付けされます:

- **VERIFIED**: 残高が一致します。
- **DISCREPANCY**: 残高が一致しません — レビューを推奨します。
- **FAILED**: 検証を実行できませんでした（残高データが不足）。

### トランザクションを自動分類できますか?

**はい。** エンリッチメントモジュール（v0.0.6+）が LLM によるトランザクション分類を提供します:

```python
from bankstatementparser.enrichment import Categorizer

categorizer = Categorizer()
enriched = categorizer.categorize_batch(transactions)
```

デフォルトスキーマは 13 の Plaid 互換カテゴリを使用します。独自のカテゴリスキーマも指定できます。

### hledger や beancount にエクスポートできますか?

**はい**（v0.0.8+）。アカウントマッピング付きでプレーンテキスト会計ジャーナル形式にエクスポートします:

```python
from bankstatementparser.export import to_hledger, to_beancount

journal = to_hledger(transactions, account="Assets:Bank:Checking")
```

## 財務ワークフロー

### パーサーはマルチ通貨明細書をどのように処理しますか?

**各トランザクションは元の通貨を保持します — 暗黙的な変換は行いません。** `Currency` フィールドは XML の `Ccy` 属性からトランザクションごとに抽出されます。マルチ通貨明細書はそのまま残ります。`get_account_balances()` メソッドは、元の通貨コードで口座ごとの期首残高と期末残高を返します。

v0.0.8 以降、`verify_balance_multi_currency()` はトランザクションを通貨ごとにグループ化し、各グループで独立してゴールデンルールを実行します。複数通貨を保有する口座に便利です。

### パーサーは送信形式と受信形式の両方をサポートしていますか?

**はい。** `Pain001Parser` は ISO 20022 PAIN.001 送金指図ファイル（送金）を処理します。`CamtParser` は CAMT.053 銀行対顧客明細書ファイル（受信レポート）を処理します。どちらもストリーミング、PII 秘匿化、CSV、JSON、Excel、hledger、beancount へのエクスポートをサポートします。`detect_statement_format()` でフォーマットを自動的に識別します。

### トランザクションエントリの形式が不正な場合はどうなりますか?

動作は解析モードによって異なります:

- **`parse()`（バッチモード）** -- 必須フィールド（`Amount`、`Currency`、`CdtDbtInd`）がないエントリは警告ログとともにスキップされます。明細書の残りは通常どおり解析されます。
- **`parse_streaming()`（ストリーミングモード）** -- 解析エラーは例外として即座に伝播します。サイレントデータ損失はありません。このフェイルファスト動作は、すべてのトランザクションを考慮する必要がある財務ワークフローを意図しています。
- **`smart_ingest()`（ハイブリッド PDF）** -- 抽出エラーは `IngestResult` に検証ステータスとともに記録され、インタラクティブレビューが可能です。

### 重複排除はどのように機能しますか?

各トランザクションには、主要フィールドに基づくべき等な `transaction_hash`（MD5 フィンガープリント）が割り当てられます。これにより安全なインクリメンタル取り込みが可能になります。同じファイルを再処理しても同じハッシュが生成されるため、重複が自動的に検出されます。

```python
from bankstatementparser import CamtParser, Deduplicator

parser = CamtParser("statement.xml")
dedup = Deduplicator()
result = dedup.deduplicate(dedup.from_dataframe(parser.parse()))

print(f"Unique: {len(result.unique_transactions)}")
print(f"Exact duplicates: {len(result.exact_duplicates)}")
print(f"Suspected matches: {len(result.suspected_matches)}")
```

## インストールと互換性

### Bank Statement Parser をインストールするにはどうすればよいですか?

```bash
# コアインストール（確定的パーサーのみ）
pip install bankstatementparser

# PDF ハイブリッドパイプライン
pip install 'bankstatementparser[hybrid]'         # テキスト LLM パス
pip install 'bankstatementparser[hybrid-vision]'   # ビジョン LLM パス

# エクストラ
pip install 'bankstatementparser[enrichment]'      # トランザクション分類
pip install 'bankstatementparser[api]'             # REST API マイクロサービス
pip install 'bankstatementparser[polars]'          # Polars DataFrame サポート
```

### どのバージョンの Python がサポートされていますか?

Python 3.10〜3.14。Python 3.9 のサポートは v0.0.6 で廃止されました（EOL 2025-10-31）。すべてのバージョンは CI で 100% ブランチカバレッジの 718 テストでテストされています。

### 依存関係は何ですか?

コアライブラリには 5 つの直接依存関係があります:

- `lxml` -- セキュリティ強化付き XML 解析
- `pandas` -- DataFrame とデータ操作
- `openpyxl` -- Excel エクスポート
- `pydantic` -- データ検証とモデル
- `defusedxml` -- XXE 保護

オプションのエクストラとして `litellm`、`pypdf`、`pdfplumber`、`pypdfium2`、`fastapi`、`uvicorn`、`polars` が追加されます。

すべての依存関係は SHA-256 ハッシュロックされたバージョンを持ちます。CycloneDX SBOM がすべてのランタイムコンポーネントをマッピングします。

### macOS、Linux、Windows で動作しますか?

**はい。** ライブラリは macOS、Linux、Windows（WSL 経由）で動作します。プラットフォーム固有の依存関係はありません。

### REST API はありますか?

**はい**（v0.0.8+）。`pip install 'bankstatementparser[api]'` でインストールし、以下を実行します:

```bash
bankstatementparser-api --port 8000
```

エンドポイント: `POST /ingest`（明細書を解析）と `GET /health`（ヘルスチェック）。

## 再現性とセキュリティ

### 再現性を確認するにはどうすればよいですか?

```bash
python -m pytest                              # 718 tests, 100% branch coverage
python scripts/verify_locked_hashes.py        # SHA-256 hash verification
git log --show-signature -1                   # Verify commit signature
```

### どのようなセキュリティ保護が組み込まれていますか?

- **XXE 保護**: `resolve_entities=False`、`no_network=True`、`load_dtd=False`
- **ZIP 爆弾保護**: 圧縮率制限、エントリサイズ上限、暗号化エントリ拒否
- **パストラバーサル防止**: 危険パターンのブロックリストとシンボリックリンク解決
- **入力検証**: ファイルサイズ制限（デフォルト 100 MB）、拡張子/形式検証
- **サプライチェーン**: SHA-256 ハッシュロック依存関係、CycloneDX SBOM、ビルド来歴証明書
- **署名済みコミット**: CI で強制
- **ローカル LLM**: ハイブリッド PDF パイプラインは Ollama を使用 — クラウド API 呼び出しなし

### Bank Statement Parser は pyiso20022 とどう違いますか?

pyiso20022 は ISO XML スキーマから Python データクラスを生成する汎用 ISO 20022 ツールキットです。スキーマ検証により幅広い ISO 20022 メッセージタイプ（PACS、PAIN、CAMT、ADMI）をカバーします。Bank Statement Parser は、ハイブリッド PDF サポート、残高検証、エンリッチメント、台帳エクスポート、CSV・OFX・QFX・MT940・PDF を含む 7 形式にわたる統合 API を備えた銀行取引明細書解析の専用ツールです。本番グレードのセキュリティで銀行取引明細書を DataFrame に解析する必要がある場合は Bank Statement Parser を使用してください。完全な ISO 20022 メッセージカタログを操作する必要がある場合は pyiso20022 を使用してください。

### SWIFT ISO 20022 の移行期限はいつですか?

SWIFT は段階的な移行タイムラインを公開しています:

- **2026 年 11 月**: 構造化アドレスとハイブリッドアドレスが必須になります。MT101 の複数命令メッセージは拒否されます。ケースマネジメントフェーズ 1 が開始されます。
- **2027 年 11 月**: すべての金融機関が CAMT.053 明細書をネイティブに受信できる必要があります。SWIFT は MT から ISO 形式への変換を停止します。
- **2028 年 11 月**: MT940、MT942、MT950、MT900、MT910 が完全に廃止されます。これらは CAMT.052、CAMT.053、CAMT.054 に置き換えられます。

Bank Statement Parser はレガシーの MT940 形式と最新の CAMT.053/PAIN.001 形式の両方をサポートしているため、移行期間に最適です。

