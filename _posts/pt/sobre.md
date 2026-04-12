---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Sobre o analisador de extrato bancário: recursos, formatos e desempenho"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Analisador de extrato bancário. Todos os direitos reservados."
date: "Apr 11, 2026"
description: "Bank Statement Parser é uma biblioteca Python de código aberto para analisar CAMT.053, PAIN.001, CSV, OFX, QFX e MT940 em DataFrames pandas. 100% local, redação de PII, mais de 27 mil tx/s."
download: ""
format-detection: "telephone=no"
hreflang: "pt"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/pt/sobre/index.html"
image_alt: "Logotipo do analisador de extrato bancário, capacite sua análise financeira com extração contínua de dados"
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "analisador de extrato bancário python, analisador CAMT.053, analisador PAIN.001, biblioteca python ISO 20022, analisador MT940, analisador OFX QFX, analisador de banco de código aberto, processamento de dados financeiros locais, banco de redação de PII, migração de MT940 para CAMT"
language: "pt-BR"
layout: "about"
locale: "pt_BR"
logo_alt: "Logotipo do analisador de extrato bancário, capacite sua análise financeira com extração contínua de dados"
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Sobre o analisador de extrato bancário"
permalink: "https://bankstatementparser.com/pt/sobre/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Uma biblioteca. Siete formatos. Zero chamadas de rede."
tags: "banco, extrato, analisador, finanças, python, camt, pain001, csv, ofx, qfx, mt940"
theme_color: "rgb(73, 214, 251)"
title: "Sobre o analisador de extrato bancário: recursos, formatos e desempenho"
url: "https://bankstatementparser.com/pt/sobre/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/pt/sobre/rss.xml"
category: "Software financeiro, biblioteca Python, processamento de dados"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Bank Statement Parser é uma biblioteca Python de código aberto para analisar CAMT.053, PAIN.001, CSV, OFX, QFX e MT940 em DataFrames pandas. 100% local, redação de PII, mais de 27 mil tx/s."
item_guid: "https://bankstatementparser.com/pt/sobre/rss.xml"
item_link: "https://bankstatementparser.com/pt/sobre/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Sobre o analisador de extrato bancário: recursos, formatos e desempenho"
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
apple-mobile-web-app-title: "Sobre o analisador de extrato bancário: recursos, formatos e desempenho"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Biblioteca Python de código aberto: analise CAMT.053, PAIN.001, CSV, OFX, QFX, MT940 em DataFrames. 100% local, redação de PII, mais de 27 mil tx/s."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logotipo do analisador de extrato bancário, capacite sua análise financeira com extração contínua de dados"
twitter_site: "@wwdseb"
twitter_title: "Sobre o analisador de extrato bancário: 7 formatos, 27K+ tx/s, 100% local"
twitter_url: "https://bankstatementparser.com/pt/sobre/index.html"

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

**TL;DR:** Bank Statement Parser é uma biblioteca Python de código aberto que analisa sete formatos de extrato bancário (CAMT.053, PAIN.001, CSV, OFX, QFX, MT940 e PDF) em DataFrames pandas. Pipeline híbrido de PDF com verificação de saldo, REST API, enriquecimento, exportação contábil, mais de 27 mil tx/s.

Bank Statement Parser é uma biblioteca Python de código aberto que analisa extratos bancários de sete formatos em DataFrames pandas estruturados. O núcleo determinístico processa formatos estruturados localmente, sem chamadas de rede. O pipeline híbrido de PDF opcional usa LLMs locais (via Ollama) para extratos digitais e digitalizados.

## Para Quem É?

- **Equipes de tesouraria** migrando de MT940 para CAMT.053 que precisam de um analisador que lide com formatos antigos e novos durante a transição, além de extratos em PDF de bancos que não oferecem exportações estruturadas.
- **Desenvolvedores fintech** criando pipelines de reconciliação, relatórios ou contabilidade que querem uma única dependência com verificação de saldo, categorização e exportação contábil integrados.
- **Equipes de conformidade** que precisam de redação de PII por padrão, saída determinística e verificação Golden Rule que sinaliza discrepâncias antes de chegarem ao livro-razão.
- **Usuários de contabilidade em texto simples** que querem ingestão automática de extratos bancários em PDF direto para journals hledger ou beancount.
- **Qualquer pessoa** que se recuse a enviar dados financeiros sensíveis para um SaaS de terceiros quando uma ferramenta local e de código aberto pode fazer o trabalho.

## Formatos Suportados

| Formato | Padrão | Tipos de arquivo | Parser/Método |
|---|---|---|---|
| CAMT.053 | ISO 20022 Extrato Banco-para-Cliente | `.xml` | `CamtParser` |
| PAIN.001 | ISO 20022 Iniciação de Transferência de Crédito | `.xml` | `Pain001Parser` |
| CSV | Exportações bancárias genéricas | `.csv` | `CsvStatementParser` |
| OFX | Open Financial Exchange | `.ofx` | `OfxParser` |
| QFX | Quicken Financial Exchange | `.qfx` | `QfxParser` |
| MT940 | Padrão SWIFT | `.mt940`, `.sta` | `Mt940Parser` |
| PDF | Extratos digitais e digitalizados | `.pdf` | `smart_ingest()` |

Todos os formatos produzem DataFrames pandas normalizados com nomes de colunas consistentes, tornando o processamento posterior independente do formato.

## Principais Recursos

- **Pipeline Híbrido de PDF**: `smart_ingest()` roteia PDFs por três caminhos — extração determinística de tabelas, text-LLM ou vision-LLM — com verificação automática de saldo pela Golden Rule.
- **Detecção Automática de Formato**: `detect_statement_format()` identifica o formato; `create_parser()` instancia o analisador correto.
- **Verificação de Saldo**: Verificação Golden Rule (`opening + credits − debits == closing`) com status VERIFIED/DISCREPANCY/FAILED.
- **Verificação Multimoeda**: `verify_balance_multi_currency()` agrupa transações por moeda para verificação independente.
- **REST API**: Microsserviço FastAPI com endpoints `/ingest` e `/health` para implantações em produção.
- **Enriquecimento**: Categorização de transações via LLM com schemas configuráveis (padrão Plaid de 13 categorias).
- **Revisão Interativa**: Navegue por discrepâncias com ações aceitar/editar/pular/excluir via `--type review`.
- **Exportação Contábil**: `to_hledger()` e `to_beancount()` para fluxos de trabalho de contabilidade em texto simples.
- **Varredura em Massa**: `scan_and_ingest()` processa árvores de pastas com deduplicação automática entre arquivos.
- **Mapeamento de Contas**: Regras de mapeamento de contas baseadas em regex a partir de configuração JSON para exportação contábil.
- **Análise via Streaming**: Processe arquivos grandes (50 MB+, 50K+ transações) com memória limitada usando `parse_streaming()`.
- **Processamento Paralelo**: Analise vários arquivos simultaneamente com `parse_files_parallel()` usando ProcessPoolExecutor.
- **Deduplicação**: `transaction_hash` idempotente (fingerprint MD5) para ingestão incremental segura.
- **Análise em Memória**: `from_string()` e `from_bytes()` para fluxos de trabalho SFTP e API sem E/S de disco.
- **Processamento ZIP Seguro**: `iter_secure_xml_entries()` com limites de taxa de compressão, limites de tamanho de entrada e rejeição de entradas criptografadas.
- **Exportação**: CSV, JSON, Excel (`.xlsx`), DataFrames Polars, journals hledger e beancount.

## Segurança e Privacidade

- **Redação de PII**: Nomes, IBANs e endereços são mascarados por padrão na saída CLI. Ative com `--show-pii`.
- **Proteção XXE**: A análise XML usa `resolve_entities=False`, `no_network=True`, `load_dtd=False`.
- **Proteção contra ZIP Bomb**: Limites de taxa de compressão (padrão 100:1), limites de tamanho de entrada (10 MB), rejeição de entradas criptografadas.
- **Prevenção de Travessia de Caminho**: Lista de bloqueio de padrões perigosos e resolução de links simbólicos.
- **Segurança da Cadeia de Suprimentos**: Dependências bloqueadas por hash SHA-256, CycloneDX SBOM, atestado de procedência de build.
- **Apenas LLMs Locais**: O pipeline híbrido de PDF usa Ollama para inferência local — nenhum dado é enviado para APIs na nuvem.

## Desempenho

| Métrica | Valor |
|---|---|
| Throughput CAMT.053 | 27.000+ tx/s |
| Throughput PAIN.001 | 52.000+ tx/s |
| Latência por transação (CAMT) | 37 microssegundos |
| Latência por transação (PAIN.001) | 19 microssegundos |
| Tempo para o primeiro resultado | < 2 ms |
| Escala de memória (1K-50K tx) | Constante (streaming) |
| Cobertura de testes | 100% de cobertura de ramificação |
| Testes | 718 em 29 arquivos de teste |

## Comece Agora

[Comece com a instalação e exemplos ❯][01]

[01]: /getting-started/index.html "Primeiros passos"
 "Repositório GitHub"
