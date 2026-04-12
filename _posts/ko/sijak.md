---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "검은 창문이 있는 흰색 건물"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/daniele-franchi-Vl6YuVBLEys.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 은행 명세서 파서. 모든 권리 보유."
date: "Apr 11, 2026"
description: "Python용 Bank 명세서 구문 분석기 시작: CAMT/PAIN.001/CSV/OFX/QFX/MT940 파일을 설치 및 구문 분석하고 스트리밍 또는 CLI 워크플로를 사용합니다."
download: ""
format-detection: "telephone=no"
hreflang: "ko"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/ko/sijak/index.html"
image_alt: "빠르고 정확한 금융 데이터 처리 및 통찰력 추출을 위해 설계된 강력한 Python 도구인 은행 계좌 명세서 파서의 로고."
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "은행 명세서 파서, 시작하기, Python, CAMT, PAIN.001, CSV, OFX, QFX, MT940, 금융 데이터"
language: "ko-KR"
layout: "start"
locale: "ko_KR"
logo_alt: "빠르고 정확한 금융 데이터 처리 및 통찰력 추출을 위해 설계된 강력한 Python 도구인 은행 계좌 명세서 파서의 로고."
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "시작하기"
permalink: "https://bankstatementparser.com/ko/sijak/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "은행 계좌 명세서 파서로 보안 애플리케이션 구축 시작"
tags: "은행, 명세서, 파서, Python, camt, pain001, csv, ofx, qfx, mt940, 스트리밍, cli"
theme_color: "rgb(73, 214, 251)"
title: "은행 명세서 파서: 설치 및 사용 가이드"
url: "https://bankstatementparser.com/ko/sijak/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/ko/sijak/rss.xml"
category: "금융 소프트웨어, Python 라이브러리, 개발자 가이드"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin (version 0.0.20)"
item_description: "Python용 Bank 명세서 구문 분석기 시작: CAMT/PAIN.001/CSV/OFX/QFX/MT940 파일을 설치 및 구문 분석하고 스트리밍 또는 CLI 워크플로를 사용합니다."
item_guid: "https://bankstatementparser.com/ko/sijak/rss.xml"
item_link: "https://bankstatementparser.com/ko/sijak/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "은행 명세서 파서: 설치 및 사용 가이드"
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
apple-mobile-web-app-title: "은행 명세서 파서: 설치 및 사용 가이드"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Bank 명세서 구문 분석기를 설치하고 사용하여 Python에서 CAMT, PAIN.001, CSV, OFX/QFX 및 MT940 파일을 구문 분석합니다."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "빠르고 정확한 금융 데이터 처리 및 통찰력 추출을 위해 설계된 강력한 Python 도구인 은행 계좌 명세서 파서의 로고."
twitter_site: "@wwdseb"
twitter_title: "은행 명세서 파서: 설치 및 사용 가이드"
twitter_url: "https://bankstatementparser.com/ko/sijak/index.html"

# Humans.txt - The Humans.txt front matter (YAML).

author_website: "https://bankstatementparser.com"
author_twitter: "@wwdseb"
author_location: "London, UK"
thanks: "읽어주셔서 감사합니다!"
site_last_updated: "2026-04-01"
site_standards: "HTML5, CSS3, RSS, Atom, JSON, XML, YAML, Markdown, TOML"
site_components: "Shokunin SSG, Shokunin CLI, Shokunin Templates, Shokunin Themes, Kaishi SSG, Kaishi CLI, Kaishi Templates, Kaishi Themes"
site_software: "Shokunin, Rust"

---

## 요구 사항

- Python 3.10~3.14
- 터미널 접근 (macOS, Linux 또는 WSL)

## 설치

```bash
# 코어 설치 (결정적 파서만)
pip install bankstatementparser
```

추가 기능을 위한 선택적 extras:

```bash
# 디지털 PDF용 텍스트-LLM 경로 (litellm + pypdf)
pip install 'bankstatementparser[hybrid]'

# 고정밀 테이블 추출 (pdfplumber 추가)
pip install 'bankstatementparser[hybrid-plus]'

# 스캔 PDF용 비전-LLM 경로 (pypdfium2 추가)
pip install 'bankstatementparser[hybrid-vision]'

# LLM 기반 트랜잭션 분류
pip install 'bankstatementparser[enrichment]'

# REST API 마이크로서비스 (FastAPI + uvicorn)
pip install 'bankstatementparser[api]'

# 선택적 Polars DataFrame 지원
pip install 'bankstatementparser[polars]'
```

## 빠른 시작

### 구조화된 형식 자동 감지 및 파싱

```python
from bankstatementparser import create_parser, detect_statement_format

fmt = detect_statement_format("transactions.ofx")
parser = create_parser("transactions.ofx", fmt)
df = parser.parse()  # pandas DataFrame
print(df.head())
```

`.xml` (CAMT/PAIN.001), `.csv`, `.ofx`, `.qfx`, `.mt940`, `.sta` 파일에서 작동합니다.

### CAMT.053 파싱

```python
from bankstatementparser import CamtParser

parser = CamtParser("statement.xml")
transactions = parser.parse()
```

### PAIN.001 파싱

```python
from bankstatementparser import Pain001Parser

parser = Pain001Parser("payment.xml")
payments = parser.parse()
```

### PDF 은행 명세서 파싱 (하이브리드 파이프라인)

하이브리드 파이프라인은 PDF를 3가지 추출 경로로 지능적으로 라우팅합니다.

```python
from bankstatementparser.hybrid import smart_ingest

result = smart_ingest("statement.pdf")
print(result.source_method)         # "deterministic" | "llm" | "vision"
print(result.verification.status)   # VERIFIED | DISCREPANCY | FAILED
print(result.transactions)          # List of extracted transactions
```

모든 추출 결과는 **Golden Rule**로 검증됩니다: `opening + credits − debits == closing`.

## 대용량 파일 스트리밍

수천 개의 트랜잭션이 포함된 파일의 경우 스트리밍을 사용하여 메모리를 제한합니다.

```python
parser = CamtParser("large_statement.xml")
for transaction in parser.parse_streaming(redact_pii=True):
    process(transaction)  # Memory stays constant
```

## 메모리 내 파싱

디스크 I/O 없이 바이트에서 파싱합니다. SFTP 또는 API 워크플로에 유용합니다.

```python
xml_bytes = download_from_sftp()
parser = CamtParser.from_bytes(xml_bytes, source_name="daily.xml")
transactions = parser.parse()
```

## 병렬 파일 처리

여러 파일을 동시에 파싱합니다.

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

## 대량 디렉토리 스캔

자동 중복 제거로 전체 폴더 트리를 처리합니다.

```python
from bankstatementparser.hybrid import scan_and_ingest

batch = scan_and_ingest("statements/2026/", pattern="**/*.pdf")
print(f"Processed: {len(batch.results)} files")
print(f"Unique transactions: {batch.unique_count}")
```

## 중복 제거

안전한 증분 수집을 위한 멱등성 트랜잭션 해시:

```python
from bankstatementparser import CamtParser, Deduplicator

parser = CamtParser("statement.xml")
dedup = Deduplicator()
result = dedup.deduplicate(dedup.from_dataframe(parser.parse()))

print(f"Unique: {len(result.unique_transactions)}")
print(f"Exact duplicates: {len(result.exact_duplicates)}")
print(f"Suspected matches: {len(result.suspected_matches)}")
```

## 트랜잭션 분류 (보강)

LLM 기반 분류를 사용하여 트랜잭션을 자동으로 분류합니다.

```python
from bankstatementparser.enrichment import Categorizer

categorizer = Categorizer()
enriched = categorizer.categorize_batch(transactions)
for txn in enriched:
    print(f"{txn.description}: {txn.category}")
```

## 원장 내보내기 (hledger / beancount)

트랜잭션을 일반 텍스트 회계 저널 형식으로 내보냅니다.

```python
from bankstatementparser.export import to_hledger, to_beancount

journal = to_hledger(transactions, account="Assets:Bank:Checking")
beancount_journal = to_beancount(transactions, account="Assets:Bank:Checking")
```

## 다중 통화 잔액 검증

통화 그룹별로 잔액을 독립적으로 검증합니다.

```python
from bankstatementparser.hybrid import verify_balance_multi_currency

results = verify_balance_multi_currency(transactions)
for currency, verification in results.items():
    print(f"{currency}: {verification.status}")
```

## REST API

FastAPI 마이크로서비스로 배포합니다.

```bash
# API 서버 시작
bankstatementparser-api --port 8000

# 컨테이너 배포용
bankstatementparser-api --host 0.0.0.0 --port 9000
```

엔드포인트:
- `POST /ingest` -- 은행 명세서 파일 파싱
- `GET /health` -- 헬스 체크

## 보안 ZIP 처리

내장 보안 검사(폭탄 방지, 암호화된 항목 거부)로 압축된 XML 파일을 처리합니다.

```python
from bankstatementparser import iter_secure_xml_entries, CamtParser

for entry in iter_secure_xml_entries("statements.zip"):
    parser = CamtParser.from_bytes(entry.xml_bytes, source_name=entry.source_name)
    print(f"{entry.source_name}: {len(parser.parse())} transactions")
```

## 내보내기

```python
parser = CamtParser("statement.xml")
parser.export_csv("output.csv")
parser.export_json("output.json")

# Polars (requires bankstatementparser[polars])
polars_df = parser.to_polars()

# Excel
parser.camt_to_excel("output.xlsx")
```

## CLI 사용법

```bash
# 구조화된 형식 파싱
bankstatementparser --type camt --input statement.xml
bankstatementparser --type pain001 --input payment.xml

# 하이브리드 PDF 파이프라인
bankstatementparser --type ingest --input statement.pdf
bankstatementparser --type ingest --input statement.pdf --output ledger.csv

# 대화형 검토 모드
bankstatementparser --type review --input result.json
bankstatementparser --type review --input result.json --output reviewed.json

# 스트리밍으로 CSV 내보내기
bankstatementparser --type camt --input statement.xml --output transactions.csv
bankstatementparser --type camt --input statement.xml --streaming --show-pii
```

CLI 옵션:

- `--type {camt,pain001,ingest,review}` -- 파서 유형 또는 모드
- `--input <path>` -- 입력 파일
- `--output <path>` -- 내보내기 파일 (CSV 또는 JSON)
- `--streaming` -- 대용량 파일 스트리밍
- `--show-pii` -- 민감한 필드 표시 (기본적으로 마스킹됨)
- `--max-size <MB>` -- 파일 크기 제한

## 로컬 개발 설정

```bash
git clone https://github.com/sebastienrousseau/bankstatementparser.git
cd bankstatementparser
python3 -m venv .venv && source .venv/bin/activate
pip install poetry && poetry install --with dev
make install-hooks   # pre-commit hook runs `make verify` before every commit
```

테스트 스위트 실행:

```bash
pytest
```

## API 레퍼런스

### 파서 클래스

| 클래스 | 형식 | Import |
|---|---|---|
| `CamtParser` | CAMT.053 (ISO 20022) | `from bankstatementparser import CamtParser` |
| `Pain001Parser` | PAIN.001 (ISO 20022) | `from bankstatementparser import Pain001Parser` |
| `CsvStatementParser` | CSV | `from bankstatementparser import CsvStatementParser` |
| `OfxParser` | OFX | `from bankstatementparser import OfxParser` |
| `QfxParser` | QFX | `from bankstatementparser import QfxParser` |
| `Mt940Parser` | MT940 | `from bankstatementparser import Mt940Parser` |
| `smart_ingest()` | PDF (하이브리드 파이프라인) | `from bankstatementparser.hybrid import smart_ingest` |

### 유틸리티 함수

| 함수 | 용도 |
|---|---|
| `detect_statement_format(path)` | 파일 형식 자동 감지 |
| `create_parser(path, fmt)` | 적절한 파서 생성 |
| `parse_files_parallel(paths)` | 여러 파일 동시 파싱 |
| `iter_secure_xml_entries(zip_path)` | ZIP 항목 안전하게 반복 |
| `smart_ingest(path)` | 검증 포함 하이브리드 PDF 추출 |
| `scan_and_ingest(dir, pattern)` | 대량 디렉토리 스캔 |
| `verify_balance_multi_currency(txns)` | 통화별 잔액 검증 |
| `to_hledger(txns, account)` | hledger 저널 형식으로 내보내기 |
| `to_beancount(txns, account)` | beancount 저널 형식으로 내보내기 |

### 데이터 클래스

| 클래스 | 용도 |
|---|---|
| `Deduplicator` | 중복 트랜잭션 감지 |
| `DeduplicationResult` | 고유, 정확한 중복, 의심되는 일치 결과 |
| `InputValidator` | 파일 경로 및 형식 검증 |
| `Transaction` | 정규화된 트랜잭션 레코드 |
| `FileResult` | 병렬 파싱 결과 |
| `ZipXMLSource` | ZIP 멤버 래퍼 |
| `IngestResult` | 검증 포함 하이브리드 파이프라인 결과 |
| `VerificationResult` | 잔액 검증 결과 |
| `Categorizer` | LLM 기반 트랜잭션 분류 |
| `AccountMapper` | 정규식 기반 계정 매핑 규칙 |

### 예외

| 예외 | 발생 시점 |
|---|---|
| `ParserError` | 파싱 실패 |
| `ExportError` | 내보내기 실패 (CSV/JSON/Excel) |
| `ValidationError` | 입력 유효성 검사 실패 |
| `ZipSecurityError` | ZIP 보안 검사 실패 |
