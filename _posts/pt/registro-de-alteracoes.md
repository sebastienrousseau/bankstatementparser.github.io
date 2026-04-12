---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Log de alterações do analisador de extrato bancário"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Analisador de extrato bancário. Todos os direitos reservados."
date: "Apr 11, 2026"
description: "Histórico de lançamento e changelog do Bank Statement Parser. Acompanhe novos recursos, melhorias e correções de bugs em todas as versões."
download: ""
format-detection: "telephone=no"
hreflang: "pt"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/pt/registro-de-alteracoes/index.html"
image_alt: "Logotipo do analisador de extrato bancário, capacite sua análise financeira com extração contínua de dados"
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "changelog do analisador de extrato bancário, notas de versão, histórico de versões, atualizações"
language: "pt-BR"
layout: "about"
locale: "pt_BR"
logo_alt: "Logotipo do analisador de extrato bancário, capacite sua análise financeira com extração contínua de dados"
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Registro de alterações"
permalink: "https://bankstatementparser.com/pt/registro-de-alteracoes/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Histórico de lançamentos e novidades"
tags: "changelog, lançamentos, atualizações, versões, anúncios, blog"
theme_color: "rgb(73, 214, 251)"
title: "Log de alterações do analisador de extrato bancário"
url: "https://bankstatementparser.com/pt/registro-de-alteracoes/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/pt/registro-de-alteracoes/rss.xml"
category: "Software financeiro, biblioteca Python, processamento de dados"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Histórico de lançamento e changelog do Bank Statement Parser. Acompanhe novos recursos, melhorias e correções de bugs em todas as versões."
item_guid: "https://bankstatementparser.com/pt/registro-de-alteracoes/rss.xml"
item_link: "https://bankstatementparser.com/pt/registro-de-alteracoes/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Log de alterações do analisador de extrato bancário"
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
apple-mobile-web-app-title: "Log de alterações do analisador de extrato bancário"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Histórico de lançamento e changelog do Bank Statement Parser. Acompanhe novos recursos, melhorias e correções de bugs em todas as versões."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logotipo do analisador de extrato bancário, capacite sua análise financeira com extração contínua de dados"
twitter_site: "@wwdseb"
twitter_title: "Log de alterações do analisador de extrato bancário"
twitter_url: "https://bankstatementparser.com/pt/registro-de-alteracoes/index.html"

# Humans.txt - The Humans.txt front matter (YAML).

author_website: "https://bankstatementparser.com"
author_twitter: "@wwdseb"
author_location: "London, UK"
thanks: "Obrigado por ler!"
site_last_updated: "2026-04-01"
site_standards: "HTML5, CSS3, RSS, Atom, JSON, XML, YAML, Markdown, TOML"
site_components: "Shokunin SSG, Shokunin CLI, Shokunin Templates, Shokunin Themes, Kaishi SSG, Kaishi CLI, Kaishi Templates, Kaishi Themes"
site_software: "Shokunin, Rust"

---

Acompanhe o desenvolvimento do Analisador de Extratos Bancários. Assine via [RSS](/changelog/rss.xml) ou assista ao [repositório GitHub](https://github.com/sebastienrousseau/bankstatementparser) para notificações de lançamento.

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

## v0.0.4 — 15/03/2026

- Adicionada análise paralela de arquivos com`parse_files_parallel()`usando ProcessPoolExecutor.
- Adicionado streaming verdadeiro para arquivos PAIN.001 grandes (50 MB+) com memória limitada.
- Otimizações de desempenho: a taxa de transferência CAMT agora excede 27.000 tx/s, PAIN.001 excede 52.000 tx/s.
- Adicionado`Deduplicator`classe para detectar duplicatas exatas e suspeitas de correspondências com pontuações de confiança.
- Adicionado`from_string()`e`from_bytes()`métodos para análise na memória sem E/S de disco.
- Adicionado`iter_secure_xml_entries()`para processamento seguro de arquivos ZIP.
- CI estendido com aplicação de limite de desempenho.

## v0.0.3 — 20/11/2025

- Adicionado suporte ao analisador CSV, OFX, QFX e MT940.
- Adicionada detecção automática de formato com`detect_statement_format()`e`create_parser()`.
- Adicionada redação de PII (ativada por padrão na CLI e no modo de streaming).
- Adicionados auxiliares de exportação para CSV, JSON e Excel.
- Adicionado suporte opcional para Polars DataFrame.
- Conjunto de testes expandido para 718 testes com cobertura de 100% das filiais.

## v0.0.2 — 10/06/2025

- Adicionado analisador PAIN.001 (`Pain001Parser`) para arquivos de início de transferência de créditos ISO 20022.
- Adicionada interface CLI (`python -m bankstatementparser.cli`).
- Adicionado modo de streaming com`parse_streaming()`.
- Adicionados limites de validação de entrada e tamanho de arquivo.

## v0.0.1 — 15/01/2025

- Lançamento inicial.
- Analisador CAMT.053 (`CamtParser`) para extratos de banco para cliente ISO 20022.
- saída do DataFrame do pandas.
- Fortalecimento básico de segurança XML (proteção XXE, no_network).

Veja o histórico completo de commits no [GitHub](https://github.com/sebastienrousseau/bankstatementparser/commits/main).

<script type="application/ld+json">
{
  "@contexto": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "Analisador de extrato bancário",
  "applicationCategory": "DesenvolvedorAplicativo",
  "operatingSystem": "Crossplataforma",
  "softwareVersion": "0.0.8",
  "data de publicação": "15/03/2026",
  "releaseNotes": "Adicionada análise paralela de arquivos, streaming verdadeiro para PAIN.001, otimizações de desempenho (27K+ tx/s CAMT, 52K+ tx/s PAIN.001), classe Deduplicator, análise na memória, processamento ZIP seguro.",
  "downloadUrl": "https://pypi.org/project/bankstatementparser/",
  "licença": "https://opensource.org/licenses/Apache-2.0",
  "autor": {
    "@type": "Pessoa",
    "nome": "Sébastien Rousseau"
  }
}
</script>
