---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "ISO 20022 마이그레이션 가이드"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 은행 명세서 파서. 모든 권리 보유."
date: "Apr 11, 2026"
description: "SWIFT ISO 20022 마이그레이션 타임라인(2026-2028), MT940에서 CAMT.053으로의 전환, Bank 명세서 파서가 재무 팀의 마이그레이션을 돕는 방법에 대한 실무 가이드입니다."
download: ""
format-detection: "telephone=no"
hreflang: "ko"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/ko/migration/index.html"
image_alt: "은행 명세서 파서 로고, 원활한 데이터 추출로 재무 분석 강화"
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "ISO 20022 마이그레이션, MT940에서 CAMT.053으로, SWIFT 마감일 2027, MT940 만료 2028, 은행 명세서 마이그레이션 Python, CAMT.053 파서, ISO 20022 타임라인"
language: "ko-KR"
layout: "about"
locale: "ko_KR"
logo_alt: "은행 명세서 파서 로고, 원활한 데이터 추출로 재무 분석 강화"
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "ISO 20022 마이그레이션 가이드"
permalink: "https://bankstatementparser.com/ko/migration/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "SWIFT MT에서 ISO 20022 전환으로 이동"
tags: "iso20022,마이그레이션,mt940,camt053,swift,타임라인"
theme_color: "rgb(73, 214, 251)"
title: "ISO 20022 마이그레이션 가이드: MT940에서 CAMT.053으로 전환"
url: "https://bankstatementparser.com/ko/migration/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/ko/migration/rss.xml"
category: "금융 소프트웨어, Python 라이브러리, 데이터 처리"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin (version 0.0.20)"
item_description: "SWIFT ISO 20022 마이그레이션 타임라인(2026-2028), MT940에서 CAMT.053으로의 전환, Bank 명세서 파서가 재무 팀의 마이그레이션을 돕는 방법에 대한 실무 가이드입니다."
item_guid: "https://bankstatementparser.com/ko/migration/rss.xml"
item_link: "https://bankstatementparser.com/ko/migration/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "ISO 20022 마이그레이션 가이드: MT940에서 CAMT.053으로 전환"
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
apple-mobile-web-app-title: "ISO 20022 마이그레이션 가이드: MT940에서 CAMT.053으로 전환"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "SWIFT ISO 20022 마이그레이션 타임라인(2026-2028), MT940에서 CAMT.053으로의 전환, Bank 명세서 파서가 재무 팀의 마이그레이션을 돕는 방법에 대한 실무 가이드입니다."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "은행 명세서 파서 로고, 원활한 데이터 추출로 재무 분석 강화"
twitter_site: "@wwdseb"
twitter_title: "ISO 20022 마이그레이션 가이드: MT940에서 CAMT.053으로 전환"
twitter_url: "https://bankstatementparser.com/ko/migration/index.html"

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

**요약:** SWIFT는 2028년 11월까지 MT940을 폐기할 예정입니다. Bank Statement Parser는 단일 API로 MT940과 CAMT.053을 모두 처리하므로 파싱 파이프라인이 전환 기간과 그 이후에도 작동합니다.

## 이 마이그레이션이 중요한 이유

SWIFT는 더욱 풍부한 ISO 20022 표준을 위해 레거시 MT 메시지 형식을 폐기하고 있습니다. 재무팀에게 이는 확정 기한 전에 은행 명세서 처리 파이프라인을 MT940에서 CAMT.053으로 전환해야 함을 의미합니다.

## SWIFT 마이그레이션 타임라인

| 날짜 | 주요 이정표 | 영향 |
|---|---|---|
| **2025년 11월** | 국경 간 결제에 대한 MT-MX 공존 종료 | PACS 메시지는 이제 ISO 20022 전용입니다 |
| **2026년 11월** | 구조화/하이브리드 주소 필수; MT101 다중 명령 거부; 사례 관리 1단계 | 주소 형식이 준수해야 하며 일부 MT 메시지가 거부됩니다 |
| **2026년 후반** | CAMT.052/.053/.054 수신 옵트인 시작 | 금융 기관이 네이티브 ISO 명세서 수신을 시작할 수 있습니다 |
| **2027년 11월** | 모든 금융 기관은 CAMT.053을 네이티브로 수신해야 합니다 | SWIFT가 MT에서 ISO 형식으로의 변환을 중단합니다. 시스템이 CAMT를 직접 파싱해야 합니다 |
| **2028년 11월** | MT940/MT942/MT950/MT900/MT910 완전 폐기 | 레거시 명세서 형식을 더 이상 사용할 수 없습니다. CAMT.052/.053/.054만 유일한 옵션입니다 |

## 코드 변경 사항

### 이전: MT940 전용

```python
from bankstatementparser import Mt940Parser

parser = Mt940Parser("statement.mt940")
df = parser.parse()
```

### 이후: 자동 감지를 통한 양쪽 형식 지원

```python
from bankstatementparser import create_parser, detect_statement_format

fmt = detect_statement_format("statement.xml")  # or .mt940
parser = create_parser("statement.xml", fmt)
df = parser.parse()  # Same DataFrame schema regardless of format
```

`detect_statement_format()` 함수는 파일이 MT940, CAMT.053, PAIN.001 또는 기타 지원 형식인지 식별합니다. `create_parser()` 함수는 올바른 파서를 반환합니다. 다운스트림 코드는 소스 형식에 관계없이 동일하게 작동합니다.

## CAMT.053 vs MT940: 주요 차이점

| 특징 | MT940 | CAMT.053 |
|---|---|---|
| 데이터 풍부함 | 제한된 필드 | 트랜잭션당 3~5배 더 많은 데이터 |
| 문자 집합 | 제한적 (SWIFT 문자 집합) | 전체 유니코드 |
| 구조 | 태그가 포함된 플랫 텍스트 | 네임스페이스가 있는 XML |
| 잔액 보고 | 시작/마감만 | 다양한 잔액 유형 |
| 참조 | 단일 참조 필드 | 다양한 참조 유형 |
| 통화 처리 | 기본적 | 환율이 포함된 완전한 다중 통화 |

## Bank Statement Parser의 도움

- **통합 API**: MT940, CAMT.053, PDF 명세서를 동일한 워크플로로 파싱하며 일관된 DataFrame 출력을 생성합니다.
- **자동 감지**: 형식을 미리 알 필요가 없습니다. `detect_statement_format()`이 자동으로 식별합니다.
- **하이브리드 PDF 파이프라인**: 전환 중 PDF 전용 명세서를 제공하는 은행은 자동 잔액 검증이 포함된 `smart_ingest()`로 처리됩니다.
- **네임스페이스 독립적**: 설정 없이 모든 CAMT.053 변형(001.02, 001.04 또는 은행별 래퍼)을 처리합니다.
- **다중 통화 검증**: `verify_balance_multi_currency()`가 통화 그룹별로 Golden Rule을 실행합니다 — 다중 통화 CAMT 명세서에 필수적입니다.
- **스트리밍**: 제한된 메모리로 대규모 CAMT 파일(50MB+, 50K+ 트랜잭션)을 처리합니다.
- **원장 내보내기**: 재무 회계를 위해 hledger 또는 beancount 저널 형식으로 직접 내보냅니다.
- **마이그레이션 테스트**: 동일한 날짜 범위에서 두 파서를 나란히 실행하여 전환 전 출력 일관성을 확인합니다.

## 시작하기

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

아직 구조화된 CAMT 내보내기를 제공하지 않는 은행의 PDF 명세서의 경우:

```python
from bankstatementparser.hybrid import smart_ingest

result = smart_ingest("statement.pdf")
assert result.verification.status == "VERIFIED"
```

[전체 문서 읽기](/getting-started/index.html)

[대안과 비교 ❯](/comparison/index.html) | [실제 사용 사례 보기 ❯](/use-cases/index.html)
