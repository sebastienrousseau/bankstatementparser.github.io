---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "은행 명세서 파서 보안"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 은행 명세서 파서. 모든 권리 보유."
date: "Apr 11, 2026"
description: "은행 명세서 파서의 보안 기능: XXE 보호, ZIP 폭탄 강화, PII 수정, 공급망 보안, 결정적 출력 및 서명된 빌드."
download: ""
format-detection: "telephone=no"
hreflang: "ko"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/ko/boan/index.html"
image_alt: "은행 명세서 파서 로고, 원활한 데이터 추출로 재무 분석 강화"
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "은행 명세서 보안, PII 수정 Python, XXE 보호, ZIP 폭탄 보호, 공급망 보안 SBOM, 결정론적 구문 분석, 금융 데이터 보안"
language: "ko-KR"
layout: "about"
locale: "ko_KR"
logo_alt: "은행 명세서 파서 로고, 원활한 데이터 추출로 재무 분석 강화"
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "보안"
permalink: "https://bankstatementparser.com/ko/boan/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "귀하의 금융 데이터를 보호하는 방법"
tags: "보안,pii,xxe,sbom,공급망,결정론적"
theme_color: "rgb(73, 214, 251)"
title: "은행 명세서 파서 보안: 데이터 보호 및 공급망"
url: "https://bankstatementparser.com/ko/boan/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/ko/boan/rss.xml"
category: "금융 소프트웨어, Python 라이브러리, 데이터 처리"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin (version 0.0.20)"
item_description: "은행 명세서 파서의 보안 기능: XXE 보호, ZIP 폭탄 강화, PII 수정, 공급망 보안, 결정적 출력 및 서명된 빌드."
item_guid: "https://bankstatementparser.com/ko/boan/rss.xml"
item_link: "https://bankstatementparser.com/ko/boan/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "은행 명세서 파서 보안: 데이터 보호 및 공급망"
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
apple-mobile-web-app-title: "은행 명세서 파서 보안: 데이터 보호 및 공급망"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "은행 명세서 파서의 보안 기능: XXE 보호, ZIP 폭탄 강화, PII 수정, 공급망 보안, 결정적 출력 및 서명된 빌드."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "은행 명세서 파서 로고, 원활한 데이터 추출로 재무 분석 강화"
twitter_site: "@wwdseb"
twitter_title: "은행 명세서 파서 보안: 데이터 보호 및 공급망"
twitter_url: "https://bankstatementparser.com/ko/boan/index.html"

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

**요약:** Bank Statement Parser는 모든 데이터를 로컬에서 처리하고, 기본적으로 PII를 마스킹하며, XXE 공격에 대해 XML 파싱을 강화하고, Ollama를 통해 LLM을 로컬에서 실행하며, SHA-256 해시 잠금 종속성 및 CycloneDX SBOM과 함께 제공됩니다.

## 보안 중심 설계

Bank Statement Parser는 민감한 금융 데이터를 처리하기 위해 만들어졌습니다. 모든 설계 결정은 보안, 프라이버시, 감사 가능성을 최우선으로 합니다.

## 클라우드 종속성 제로

모든 처리는 런타임 내에서 로컬로 이루어집니다. 결정적 파서는 네트워크 호출을 하지 않습니다. 하이브리드 PDF 파이프라인은 로컬 LLM 추론을 위해 Ollama를 사용하며 클라우드 API로 데이터를 전송하지 않습니다. XML 파서는 아웃바운드 접근을 방지하기 위해 `no_network=True`, `resolve_entities=False`, `load_dtd=False`로 명시적으로 설정됩니다.

## PII 마스킹

개인 식별 정보(이름, IBAN, 우편 주소)는 CLI 출력 및 스트리밍 모드에서 자동으로 마스킹됩니다. 기본적으로 활성화되어 있습니다.

- **CLI**: 민감한 필드는 `***REDACTED***`로 표시됩니다
- **스트리밍**: `parse_streaming(redact_pii=True)` (기본값)
- **내보내기**: CSV/JSON/Excel은 다운스트림 처리를 위해 전체 데이터를 유지합니다
- **선택적 표시**: 마스킹되지 않은 출력이 필요할 때 `--show-pii` 또는 `redact_pii=False`를 사용합니다

## XML 보안 (XXE 보호)

모든 XML 파싱은 강화된 설정의 `lxml`을 사용합니다.

- `resolve_entities=False` -- XML 엔터티 확장 공격을 방지합니다
- `no_network=True` -- 파서의 모든 아웃바운드 네트워크 접근을 차단합니다
- `load_dtd=False` -- DTD 기반 공격을 방지합니다
- 처리 전 네임스페이스 제거 -- 모든 CAMT.053 변형을 안전하게 처리합니다

## ZIP 아카이브 보안

`iter_secure_xml_entries()`가 추출 전에 모든 ZIP 멤버의 유효성을 검사합니다.

- **항목 크기 한도**: 항목당 10MB (설정 가능)
- **총 크기 한도**: 압축 해제 후 총 50MB (설정 가능)
- **압축 비율 제한**: 기본값 100:1 -- ZIP 폭탄 감지
- **암호화된 항목 거부**: 암호화된 항목은 경고와 함께 건너뜁니다
- **디스크 쓰기 없음**: XML 바이트는 `from_bytes()`를 통해 파서에 직접 전달됩니다

## 경로 탐색 방지

입력 유효성 검사가 위험한 파일 경로를 차단합니다.

- Null 바이트, 디렉토리 탐색 패턴(`../`), 심볼릭 링크는 거부됩니다
- 예상 형식에 대한 파일 확장자 유효성 검사
- 파일 크기 제한 (기본값 100MB, 설정 가능)

## 잔액 검증 (Golden Rule)

모든 PDF 추출은 다음 수식으로 검증됩니다: `opening balance + credits − debits == closing balance`. 결과는 VERIFIED, DISCREPANCY 또는 FAILED로 태그됩니다. 불일치는 `--type review`로 대화형 검토가 가능합니다.

## 결정적 출력

구조화된 형식(CAMT, PAIN.001, CSV, OFX, QFX, MT940)의 경우 동일한 입력 파일이 주어지면 파서는 매 실행마다 바이트 단위로 동일한 출력을 생성합니다. 무작위성, 모델 추론, 경험적 샘플링이 없습니다. 이것은 다음 항목에 필수적입니다:

- **감사 재현성**: 동일한 파일을 두 번 실행하고 출력을 비교합니다
- **규제 컴플라이언스**: 일관된 처리를 증명합니다
- **CI 검증**: 718개 테스트가 100% 브랜치 커버리지로 결정성을 보장합니다

## 공급망 보안

- **SHA-256 해시 잠금 종속성**: `poetry.lock`의 모든 패키지에 파일 해시가 검증되어 있습니다
- **CycloneDX SBOM**: 모든 릴리스에 소프트웨어 BOM이 포함됩니다
- **GitHub 빌드 출처**: 증명이 각 아티팩트를 소스 커밋에 연결합니다
- **서명된 커밋**: 모든 커밋은 SSH로 서명되고 CI에서 검증됩니다
- **종속성 검증**: `scripts/verify_locked_hashes.py`가 모든 해시를 로컬에서 검증합니다

## 로컬에서 확인

```bash
python -m pytest                          # 718 tests, 100% branch coverage
python scripts/verify_locked_hashes.py    # SHA-256 hash verification
git log --show-signature -1               # Verify commit signature
```
