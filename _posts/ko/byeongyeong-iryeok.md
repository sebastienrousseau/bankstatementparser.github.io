---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "은행 명세서 파서 변경 내역"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 은행 명세서 파서. 모든 권리 보유."
date: "Apr 11, 2026"
description: "은행 계좌 명세서 파서의 출시 내역 및 변경 로그입니다. 모든 버전에서 새로운 기능, 개선 사항, 버그 수정을 추적하세요."
download: ""
format-detection: "telephone=no"
hreflang: "ko"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/ko/byeongyeong-iryeok/index.html"
image_alt: "은행 명세서 파서 로고, 원활한 데이터 추출로 재무 분석 강화"
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "은행 명세서 파서 변경 로그, 릴리스 노트, 버전 기록, 업데이트"
language: "ko-KR"
layout: "about"
locale: "ko_KR"
logo_alt: "은행 명세서 파서 로고, 원활한 데이터 추출로 재무 분석 강화"
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "변경 내역"
permalink: "https://bankstatementparser.com/ko/byeongyeong-iryeok/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "출시 내역 및 새로운 기능"
tags: "변경 로그, 릴리스, 업데이트, 버전, 공지 사항, 블로그"
theme_color: "rgb(73, 214, 251)"
title: "은행 명세서 파서 변경 내역"
url: "https://bankstatementparser.com/ko/byeongyeong-iryeok/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/ko/byeongyeong-iryeok/rss.xml"
category: "금융 소프트웨어, Python 라이브러리, 데이터 처리"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin (version 0.0.20)"
item_description: "은행 계좌 명세서 파서의 출시 내역 및 변경 로그입니다. 모든 버전에서 새로운 기능, 개선 사항, 버그 수정을 추적하세요."
item_guid: "https://bankstatementparser.com/ko/byeongyeong-iryeok/rss.xml"
item_link: "https://bankstatementparser.com/ko/byeongyeong-iryeok/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "은행 명세서 파서 변경 내역"
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
apple-mobile-web-app-title: "은행 명세서 파서 변경 내역"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "은행 계좌 명세서 파서의 출시 내역 및 변경 로그입니다. 모든 버전에서 새로운 기능, 개선 사항, 버그 수정을 추적하세요."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "은행 명세서 파서 로고, 원활한 데이터 추출로 재무 분석 강화"
twitter_site: "@wwdseb"
twitter_title: "은행 명세서 파서 변경 내역"
twitter_url: "https://bankstatementparser.com/ko/byeongyeong-iryeok/index.html"

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

은행 명세서 파서 개발을 따르십시오. [RSS](/changelog/rss.xml)를 통해 구독하거나 [GitHub 저장소](https://github.com/sebastienrousseau/bankstatementparser) 출시 알림용입니다.

## v0.0.8 — 2026-04-11 (Latest) — "Full Platform"

- Multi-currency balance verification — `verify_balance_multi_currency()` groups by currency, runs Golden Rule per group.
- hledger + beancount export — `to_hledger()` and `to_beancount()` in `bankstatementparser.export`.
- Bulk directory scanner — `scan_and_ingest()` scans folder trees, deduplicates across batch.
- Account mapping rules — `AccountMapper` with ordered regex rules from JSON config.
- REST API — FastAPI wrapper with `/ingest` and `/health` endpoints (`[api]` extra).

## v0.0.7 — 2026-04-08 — "Universal Vision"

- Direct Ollama bridge (`ollama_direct_completion`) — bypasses LiteLLM long-prompt hang.
- Strip mode (`VisionExtractor.strip_rows=True`) — splits dense pages into overlapping bands for small local models.
- Recommended vision model changed from `llava` to `minicpm-v`.

## v0.0.6 — 2026-04-08 — "Intelligence Layer"

- Dropped Python 3.9 support (now 3.10-3.14).
- Enrichment module (`Categorizer`, `EnrichedTransaction`, `DEFAULT_CATEGORY_SCHEMA`).
- Interactive review mode with `--type review` CLI command.
- Per-row bounding box extraction (`Transaction.source_bbox`).

## v0.0.5 — 2026-04-08 — "Universal Extraction"

- Hybrid PDF pipeline (`smart_ingest()`) with deterministic/text-LLM/vision-LLM routing.
- `LLMExtractor` for digital PDFs via LiteLLM.
- `VisionExtractor` for scanned PDFs via multimodal vision models.
- Golden Rule balance verification (`opening + credits - debits == closing`).
- Idempotent deduplication via `transaction_hash` (MD5 fingerprint).

## v0.0.4 — 2026-03-15

- 병렬 파일 구문 분석이 추가되었습니다.`parse_files_parallel()`ProcessPoolExecutor를 사용합니다.
- 메모리가 제한된 대용량 PAIN.001 파일(50MB 이상)에 대한 트루 스트리밍을 추가했습니다.
- 성능 최적화: CAMT 처리량은 이제 27,000tx/s를 초과하고 PAIN.001은 52,000tx/s를 초과합니다.
- 추가됨`Deduplicator`신뢰도 점수를 사용하여 정확한 중복 항목과 의심되는 항목을 검색하는 클래스입니다.
- 추가됨`from_string()`그리고`from_bytes()`디스크 I/O 없이 메모리 내 구문 분석을 위한 방법.
- 추가됨`iter_secure_xml_entries()`안전한 ZIP 아카이브 처리를 위해.
- 성능 임계값 적용을 통한 확장 CI.

## v0.0.3 — 2025-11-20

- CSV, OFX, QFX 및 MT940 파서 지원이 추가되었습니다.
- 형식 자동 감지 기능이 추가되었습니다.`detect_statement_format()`그리고`create_parser()`.
- PII 수정이 추가되었습니다(CLI 및 스트리밍 모드에서는 기본적으로 활성화됨).
- CSV, JSON, Excel용 내보내기 도우미가 추가되었습니다.
- 선택적인 Polars DataFrame 지원이 추가되었습니다.
- 100% 분기 적용 범위를 갖춘 718개 테스트로 테스트 모음을 확장했습니다.

## v0.0.2 — 2025-06-10

- PAIN.001 파서 추가(`Pain001Parser`) ISO 20022 학점 이전 시작 파일의 경우.
- CLI 인터페이스 추가(`python -m bankstatementparser.cli`).
- 스트리밍 모드가 추가되었습니다.`parse_streaming()`.
- 입력 유효성 검사 및 파일 크기 제한이 추가되었습니다.

## v0.0.1 — 2025-01-15

- 최초 출시.
- CAMT.053 파서(`CamtParser`) ISO 20022 은행-고객 명세서용.
- 팬더 DataFrame 출력.
- 기본 XML 보안 강화(XXE 보호, no_network).

[GitHub](에서 전체 커밋 내역을 확인하세요.https://github.com/sebastienrousseau/bankstatementparser/commits/main).

<스크립트 유형="application/ld+json">
{
  "@컨텍스트": "https://schema.org",
  "@type": "소프트웨어응용 프로그램",
  "name": "은행 명세서 파서",
  "applicationCategory": "DeveloperApplication",
  "operatingSystem": "교차 플랫폼",
  "소프트웨어버전": "0.0.4",
  "datePublished": "2026-04-11",
  "releaseNotes": "병렬 파일 구문 분석, PAIN.001에 대한 진정한 스트리밍, 성능 최적화(27K+ tx/s CAMT, 52K+ tx/s PAIN.001), 중복 제거기 클래스, 메모리 내 구문 분석, 보안 ZIP 처리가 추가되었습니다.",
  "다운로드 URL": "https://pypi.org/project/bankstatementparser/",
  "라이센스": "https://opensource.org/licenses/Apache-2.0",
  "저자": {
    "@type": "사람",
    "이름": "세바스티앙 루소"
  }
}
</script>
