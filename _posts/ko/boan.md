---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "은행 명세서 파서 보안"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/corporate-finance.webp"
cdn: "https://cloudcdn.pro"
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 은행 명세서 파서. 모든 권리 보유."
date: "Apr 01, 2026"
description: "은행 명세서 파서의 보안 기능: XXE 보호, ZIP 폭탄 강화, PII 수정, 공급망 보안, 결정적 출력 및 서명된 빌드."
download: ""
format-detection: "telephone=no"
hreflang: "ko"
icon: "https://cloudcdn.pro/bankstatementparser/images/favicon.ico"
id: "https://bankstatementparser.com/ko/boan/index.html"
image_alt: "은행 명세서 파서 로고, 원활한 데이터 추출로 재무 분석 강화"
image_height: "630"
image_width: "1200"
image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
keywords: "은행 명세서 보안, PII 수정 Python, XXE 보호, ZIP 폭탄 보호, 공급망 보안 SBOM, 결정론적 구문 분석, 금융 데이터 보안"
language: "ko-KR"
layout: "about"
locale: "ko_KR"
logo_alt: "은행 명세서 파서 로고, 원활한 데이터 추출로 재무 분석 강화"
logo_height: "44"
logo_width: "44"
logo: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
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
msapplication_tile_image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "은행 명세서 파서의 보안 기능: XXE 보호, ZIP 폭탄 강화, PII 수정, 공급망 보안, 결정적 출력 및 서명된 빌드."
twitter_image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
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

**요약:** 은행 명세서 구문 분석기는 네트워크 호출이 전혀 없고 기본적으로 PII를 수정하며 XXE 공격에 대한 XML 구문 분석을 강화하고 SHA-256 해시 잠금 종속성 및 CycloneDX SBOM과 함께 제공됩니다.

## 보안을 위한 설계

은행 명세서 파서는 민감한 금융 데이터를 처리하기 위해 만들어졌습니다. 모든 디자인 결정은 보안, 개인 정보 보호 및 감사 가능성을 우선시합니다.

## 네트워크 액세스 제로

모든 처리는 런타임 내에서 로컬로 발생합니다. 라이브러리는 API 호출이 없고 클라우드 연결이 없으며 원격 측정을 수집하지 않습니다. XML 파서는 다음과 같이 명시적으로 구성됩니다.`no_network=True`, `resolve_entities=False`, 그리고`load_dtd=False`아웃바운드 액세스를 방지합니다.

## PII 수정

개인 식별 정보(이름, IBAN, 우편 주소)는 CLI 출력 및 스트리밍 모드에서 자동으로 수정됩니다. 이는 기본적으로 켜져 있습니다.

- **CLI**: 민감한 필드는 다음과 같이 표시됩니다.`***REDACTED***`
- **스트리밍**:`parse_streaming(redact_pii=True)`(기본)
- **내보내기**: CSV/JSON/Excel은 다운스트림 처리를 위해 전체 데이터를 유지합니다.
- **선택**: 사용`--show-pii`또는`redact_pii=False`수정되지 않은 출력이 필요한 경우

## XML 보안(XXE 보호)

모든 XML 구문 분석 사용`lxml`강화된 설정 사용:

- `resolve_entities=False`-- XML 엔터티 확장 공격을 방지합니다.
-`no_network=True`-- 파서의 모든 아웃바운드 네트워크 액세스를 차단합니다.
-`load_dtd=False`-- DTD 기반 공격 방지
- 처리 전 네임스페이스 제거 - 모든 CAMT.053 변형을 안전하게 처리합니다.

## ZIP 아카이브 보안

`iter_secure_xml_entries()`추출 전에 모든 ZIP 구성원의 유효성을 검사합니다.

- **항목 크기 한도**: 항목당 10MB(구성 가능)
- **총 크기 한도**: 비압축 총 50MB(구성 가능)
- **압축 비율 제한**: 기본값 100:1 -- ZIP 폭탄 감지
- **암호화된 항목 거부**: 암호화된 항목은 경고와 함께 건너뜁니다.
- **디스크 쓰기 없음**: XML 바이트는 다음을 통해 파서로 직접 전달됩니다.`from_bytes()`

## 경로 탐색 방지

입력 유효성 검사는 위험한 파일 경로를 차단합니다.

- Null 바이트, 디렉터리 탐색 패턴(`../`), 심볼릭 링크는 거부됩니다.
- 예상 형식에 대한 파일 확장자 유효성 검사
- 파일 크기 제한(기본값 100MB, 구성 가능)

## 결정적 출력

동일한 입력 파일이 주어지면 파서는 실행될 때마다 바이트와 동일한 출력을 생성합니다. 무작위성 없음, 모델 추론 없음, 경험적 샘플링 없음. 이는 다음과 같은 경우에 중요합니다.

- **재현성 감사**: 동일한 파일을 두 번 실행하고 출력을 비교합니다.
- **규정 준수**: 일관된 처리 입증
- **CI 검증**: 467개 테스트로 100% 분기 적용 범위로 결정성을 강화합니다.

## 공급망 보안

- **SHA-256 해시 잠금 종속성**:`poetry.lock`파일 해시를 확인했습니다
- **CycloneDX SBOM**: 모든 릴리스에는 소프트웨어 BOM이 포함되어 있습니다.
- **GitHub 빌드 출처**: 증명은 각 아티팩트를 소스 커밋에 연결합니다.
- **서명된 커밋**: 모든 커밋은 SSH로 서명되고 CI에서 확인됩니다.
- **종속성 확인**:`scripts/verify_locked_hashes.py`모든 해시를 로컬에서 검증합니다.

## 로컬에서 확인

```bash
python -m pytest                          # 467 tests, 100% branch coverage
python scripts/verify_locked_hashes.py    # SHA-256 hash verification
git log --show-signature -1               # Verify commit signature
```
