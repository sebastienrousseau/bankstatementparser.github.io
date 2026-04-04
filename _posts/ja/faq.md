---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Bank Statement Parser に関するよくある質問"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 銀行取引明細書パーサー。無断転載を禁じます。"
date: "Apr 01, 2026"
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

## データのプライバシーとコンプライアンス

### インフラストラクチャからデータが流出することはありますか?

**いいえ。** Bank Statement Parser はステートレス ライブラリとして動作します。すべての処理 (解析、PII 編集、アーカイブ抽出) はローカルのランタイム メモリ内で行われます。 API 呼び出し、クラウド サービス、テレメトリはありません。 XML パーサーは次のように強化されています。`no_network=True`、パーサー レベルですべての送信アクセスをブロックします。財務データが環境から離れることはありません。

### PII 編集はどのように機能しますか?

機密フィールドは、アプリケーション ロジックに到達する前にマスクされます。パーサーは債務者名、債権者名、IBAN、および住所を識別し、それらを次のように置き換えます。`***REDACTED***`コンソール出力とストリーミングモード。

- **リダクションは、CLI 出力およびストリーミング モードではデフォルトでオンになっています**。
- **ファイル エクスポート** (CSV、JSON、Excel) は、ダウンストリーム処理のために編集されていないデータを保持します。
- **オプトイン**して完全なデータを取得します`--show-pii`CLI または`redact_pii=False`APIで。

### 抽出プロセスは決定的ですか?

**はい -- 実行するたびにバイト同一の出力が得られます。** 同じ入力ファイルを指定すると、パーサーは毎回同じ結果を生成します。ランダム性、モデル推論、ヒューリスティック サンプリングはありません。 CI は、仮説によるプロパティベースのファジングを含む、分岐カバレッジ 100% の 467 のテストで決定論を強制します。

### プロジェクトはどのようなコンプライアンス基準に従っていますか?

プロジェクトは、完全なトレーサビリティを備えた ISO 13485 に準拠した文書を維持します。

- 重症度/確率スコアリングと残留リスク評価を備えた定量化された **リスク レジスタ**。
- 5 つのフェーズにわたる 19 のゲート ステップを含む **検証および検証計画**。
- 影響評価およびロールバック プロトコルを含む **変更管理手順**。
- リスク レベルと EOL 追跡を伴うすべての依存関係をカバーする **SOUP レジスタ**。
- 設計入力を実装および検証にマッピングする **トレーサビリティ マトリックス**。

すべてのリリースには、CycloneDX SBOM、SHA-256 チェックサム、および GitHub ビルド来歴証明書が含まれています。

## パフォーマンスとスケーラビリティ

### Bank Statement Parser の速度はどれくらいですか?

パフォーマンスのしきい値は、コミットごとに CI で検証されます。

| メトリック | 価値 |
|---|---|
| CAMT.053 スループット | 27,000+トランザクション/秒 |
| PAIN.001 スループット | 52,000+トランザクション/秒 |
| トランザクションごとのレイテンシー (CAMT) | 37マイクロ秒 |
| トランザクションごとのレイテンシー (PAIN.001) | 19マイクロ秒 |
| 最初の結果が得られるまでの時間 | < 2 ミリ秒 |

### 大きなファイルはどのように処理されますか?

**制限されたメモリを使用したスト​​リーミング -- ファイルあたり 50,000 トランザクションでテスト済み。**`parse_streaming()`XML ファイルを段階的に処理します。各トランザクションは辞書として生成されます。メモリの増大を防ぐために、要素は処理後にクリアされます。メモリはファイル サイズに応じて変化しません。50K トランザクション テスト (25 MB 以上) は、10K トランザクション テストの 2 倍未満のメモリを使用します。

50 MB を超えるファイル (たとえば、10 万回以上の支払いを伴うホスト間 PAIN.001 バッチ) の場合、パーサーはチャンクベースの名前空間ストリッピングを使用して一時ファイルをストリーミングします。完全なドキュメントがメモリにロードされることはありません。

### ZIP アーカイブはどのように安全に処理されますか?

`iter_secure_xml_entries()`抽出前に各メンバーを検証します。

- **エントリ サイズの上限** (デフォルトはエントリあたり 10 MB)
- **非圧縮サイズの合計上限** (デフォルトは 50 MB)
- **圧縮率制限** (デフォルトは 100:1) で ZIP 爆弾を防止します
- **暗号化されたエントリの拒否**

ファイルはディスクに書き込まれません。 XML バイトは、次を介してパーサーに直接渡されます。`from_bytes()`.

### 複数のファイルを並行して解析できますか?

**はい。** 使用します`parse_files_parallel()`作業を全体に分散します`ProcessPoolExecutor`:

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

## サポートされている形式

### どの銀行取引明細書の形式がサポートされていますか?

| 形式 | 標準 | ファイルの種類 | パーサークラス |
|---|---|---|---|
| CAMT.053 | ISO 20022 銀行から顧客への声明 | `.xml` | `CamtParser` |
| ペイン.001 | ISO 20022 単位認定の開始 | `.xml` | `Pain001Parser` |
| CSV | 一般的な銀行の輸出 | `.csv` | `CsvStatementParser` |
| OFX | オープンな金融取引所 | `.ofx` | `OfxParser` |
| QFX | クイックン金融取引所 | `.qfx` | `QfxParser` |
| MT940 | SWIFT規格 | `.mt940`, `.sta` | `Mt940Parser` |

### パーサーは CAMT.053 の銀行固有の方言を処理しますか?

**はい -- 設計により名前空間に依存しません。** パーサーは処理前に XML 名前空間を除去し、CAMT.053 バリアント (`camt.053.001.02`, `camt.053.001.04`、または独自の銀行ラッパー）、名前空間固有の構成は必要ありません。 XPath は、名前空間 URI ではなく、ターゲット要素の構造をクエリします。

CAMT をカスタム エンベロープでラップする銀行の場合は、次を使用します。`from_string()`または`from_bytes()`内側の原稿を直接給紙します。

### カスタム CSV 列ヘッダーを標準スキーマにマップできますか?

**はい -- 自動正規化、設定不要。**`CsvStatementParser`一般的なヘッダーのバリエーションを認識します。`"Date"`, `"Transaction Date"`, `"Booking Date"`すべてはにマップされます`date`分野。`"Amount"`, `"Value"`, `"Sum"`にマップします`amount`。貸方/借方列を分割する (例:`"Credit"`そして`"Debit"`) が検出され、単一の符号付き金額に自動的に結合されます。

### 出力形式は何ですか?

すべてのパーサーは、一貫した列タイプを持つ標準化されたパンダ データフレームを生成します。

| 形式 | キーカラム |
|---|---|
| **カムト** | `Amount`, `Currency`, `DrCr`, `Debtor`, `Creditor`, `Reference`, `ValDt`, `BookgDt`, `AccountId` |
| **痛み.001** | `PmtInfId`, `PmtMtd`, `InstdAmt`, `Currency`, `CdtrNm`, `EndToEndId`, `MsgId`, `CreDtTm`, `NbOfTxs` |
| **CSV/OFX/QFX/MT940** | `date`, `description`, `amount`(正規化された) |

CSV、JSON、Excel にエクスポートしたり、Polars DataFrame に変換したりすることもできます。

## 財務ワークフロー

### パーサーは複数通貨ステートメントをどのように処理しますか?

**各トランザクションは元の通貨を保持し、暗黙的な変換は行われません。**`Currency`フィールドは XML から抽出されます`Ccy`トランザクションごとの属性。複数通貨の明細はそのまま残ります。の`get_account_balances()`このメソッドは、元の通貨コードを使用して口座ごとの期首残高と期末残高を返します。通貨間の調整は下流のロジックに委ねられ、為替レートのソースを制御します。

### パーサーは送信形式と受信形式の両方をサポートしていますか?

**はい。**`Pain001Parser`ISO 20022 PAIN.001 クレジット転送開始ファイル (送金) を処理します。`CamtParser`CAMT.053 銀行から顧客への取引明細書ファイル (受信レポート) を処理します。どちらもストリーミング、PII 編集、CSV、JSON、Excel へのエクスポートをサポートしています。使用`detect_statement_format()`フォーマットを自動的に識別します。

### トランザクション エントリの形式が正しくない場合はどうなりますか?

動作は解析モードによって異なります。

- **`parse()`(バッチ モード)** -- 不正な形式のエントリに必須フィールドがありません (`Amount`, `Currency`、 または`CdtDbtInd`) は警告ログとともにスキップされます。ステートメントの残りの部分は通常どおり解析されます。
- **`parse_streaming()`(ストリーミング モード)** -- 解析エラーは例外として直ちに伝播します。サイレントデータ損失はありません。このフェイルファスト動作は、すべてのトランザクションを考慮する必要がある財務ワークフローを意図したものです。

### 重複排除はどのように機能しますか?

の`Deduplicator`クラスは、説明可能な信頼スコアを使用して完全な重複と疑わしい一致を検出します。

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
pip install bankstatementparser
```

オプションの Polars DataFrame サポートの場合:

```bash
pip install bankstatementparser[polars]
```

### どのバージョンの Python がサポートされていますか?

Python 3.9 ～ 3.14。すべてのバージョンは CI でテストされ、ブランチ カバレッジ 100% で 467 のテストが行​​われます。

### 依存関係とは何ですか?

ライブラリには 5 つの直接依存関係があります。

- `lxml`-- セキュリティ強化による XML 解析
-`pandas`-- DataFrame とデータ操作
-`openpyxl`-- Excel エクスポート
-`pydantic`-- データ検証とモデル
-`defusedxml`-- XXE 保護

すべての依存関係には SHA-256 ハッシュロックされたバージョンがあります。 CycloneDX SBOM は、すべてのランタイム コンポーネントをマッピングします。

### macOS、Linux、Windows で動作しますか?

**はい。** このライブラリは、macOS、Linux、および Windows (WSL 経由) で動作します。プラットフォーム固有の依存関係はありません。

## 再現性とセキュリティ

### 再現性を確認するにはどうすればよいですか?

```bash
python -m pytest                              # 467 tests, 100% branch coverage
python scripts/verify_locked_hashes.py        # SHA-256 hash verification
git log --show-signature -1                   # Verify commit signature
```

### どのようなセキュリティ保護が組み込まれていますか?

- **XXE 保護**:`resolve_entities=False`, `no_network=True`, `load_dtd=False`
- **ZIP 爆弾保護**: 圧縮率の制限、エントリ サイズの上限、暗号化されたエントリの拒否
- **パストラバーサル防止**: 危険なパターンのブロックリストとシンボリックリンクの解決
- **入力検証**: ファイル サイズ制限 (デフォルトは 100 MB)、拡張子/形式検証
- **サプライ チェーン**: SHA-256 ハッシュロックされた依存関係、CycloneDX SBOM、ビルド来歴証明書
- **署名済みコミット**: CI で強制されます

### Bank Statement Parser は pyiso20022 とどう違うのですか?

pyiso20022 は、ISO XML スキーマから Python データクラスを生成する広範な ISO 20022 ツールキットです。スキーマ検証により、幅広い ISO 20022 メッセージ タイプ (PACS、PAIN、CAMT、ADMI) をカバーします。 Bank Statement Parser は、ストリーミング サポート、PII 編集、重複排除、および非 ISO 形式 (CSV、OFX、QFX、MT940) を含む 6 つの形式にわたる統合 API を備えた銀行取引明細書解析専用に構築されています。実稼働グレードのセキュリティを備えた銀行取引明細書を DataFrame に解析する必要がある場合は、Bank Statement Parser を使用します。完全な ISO 20022 メッセージ カタログを操作する必要がある場合は、pyiso20022 を使用してください。

### SWIFT ISO 20022 の移行期限はいつですか?

SWIFT は、段階的な移行タイムラインを公開しています。

- **2026 年 11 月**: 構造化アドレスとハイブリッド アドレスが必須になります。 MT101 の複数命令メッセージは拒否されます。ケース管理フェーズ 1 が始まります。
- **2027 年 11 月**: すべての金融機関は CAMT.053 明細書をネイティブに受信できる必要があります。 SWIFT は MT から ISO 形式への変換を停止します。
- **2028 年 11 月**: MT940、MT942、MT950、MT900、および MT910 は完全に廃止されます。これらは、CAMT.052、CAMT.053、および CAMT.054 の同等のものに置き換えられます。

Bank Statement Parser は、従来の MT940 形式と最新の CAMT.053/PAIN.001 形式の両方をサポートしているため、移行期間に最適です。

