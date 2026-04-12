---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Segurança do analisador de extrato bancário"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Analisador de extrato bancário. Todos os direitos reservados."
date: "Apr 11, 2026"
description: "Recursos de segurança do analisador de extrato bancário: proteção XXE, proteção de bomba ZIP, redação de PII, segurança da cadeia de suprimentos, saída determinística e construções assinadas."
download: ""
format-detection: "telephone=no"
hreflang: "pt"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/pt/seguranca/index.html"
image_alt: "Logotipo do analisador de extrato bancário, capacite sua análise financeira com extração contínua de dados"
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "segurança de extrato bancário, redação de PII python, proteção XXE, proteção contra bomba ZIP, segurança da cadeia de suprimentos SBOM, análise determinística, segurança de dados financeiros"
language: "pt-BR"
layout: "about"
locale: "pt_BR"
logo_alt: "Logotipo do analisador de extrato bancário, capacite sua análise financeira com extração contínua de dados"
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Segurança"
permalink: "https://bankstatementparser.com/pt/seguranca/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Como protegemos seus dados financeiros"
tags: "segurança, pii, xxe, sbom, cadeia de suprimentos, determinística"
theme_color: "rgb(73, 214, 251)"
title: "Segurança do analisador de extratos bancários: proteção de dados e cadeia de suprimentos"
url: "https://bankstatementparser.com/pt/seguranca/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/pt/seguranca/rss.xml"
category: "Software financeiro, biblioteca Python, processamento de dados"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Recursos de segurança do analisador de extrato bancário: proteção XXE, proteção de bomba ZIP, redação de PII, segurança da cadeia de suprimentos, saída determinística e construções assinadas."
item_guid: "https://bankstatementparser.com/pt/seguranca/rss.xml"
item_link: "https://bankstatementparser.com/pt/seguranca/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Segurança do analisador de extratos bancários: proteção de dados e cadeia de suprimentos"
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
apple-mobile-web-app-title: "Segurança do analisador de extratos bancários: proteção de dados e cadeia de suprimentos"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Recursos de segurança do analisador de extrato bancário: proteção XXE, proteção de bomba ZIP, redação de PII, segurança da cadeia de suprimentos, saída determinística e construções assinadas."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logotipo do analisador de extrato bancário, capacite sua análise financeira com extração contínua de dados"
twitter_site: "@wwdseb"
twitter_title: "Segurança do analisador de extratos bancários: proteção de dados e cadeia de suprimentos"
twitter_url: "https://bankstatementparser.com/pt/seguranca/index.html"

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

**TL;DR:** O Bank Statement Parser processa todos os dados localmente, redige PII por padrão, reforça a análise XML contra ataques XXE, roda LLMs localmente via Ollama e vem com dependências bloqueadas por hash SHA-256 e um CycloneDX SBOM.

## Segurança por Design

O Bank Statement Parser foi feito para processar dados financeiros sensíveis. Cada decisão de design prioriza segurança, privacidade e auditabilidade.

## Zero Dependência de Nuvem

Todo o processamento acontece localmente no seu runtime. Os parsers determinísticos fazem zero chamadas de rede. O pipeline híbrido de PDF usa Ollama para inferência LLM local — nenhum dado é enviado para APIs na nuvem. Os parsers XML são configurados explicitamente com `no_network=True`, `resolve_entities=False` e `load_dtd=False` para impedir qualquer acesso de saída.

## Redação de PII

Informações de identificação pessoal (nomes, IBANs, endereços postais) são automaticamente redadas na saída CLI e no modo de streaming. Isso vem ativado por padrão.

- **CLI**: Campos sensíveis aparecem como `***REDACTED***`
- **Streaming**: `parse_streaming(redact_pii=True)` (padrão)
- **Exportações**: CSV/JSON/Excel retêm dados completos para processamento posterior
- **Opt-in**: Use `--show-pii` ou `redact_pii=False` quando precisar de saída sem redação

## Segurança XML (Proteção XXE)

Toda análise XML usa `lxml` com configurações reforçadas:

- `resolve_entities=False` -- impede ataques de expansão de entidades XML
- `no_network=True` -- bloqueia todo acesso de saída à rede no parser
- `load_dtd=False` -- impede ataques baseados em DTD
- Remoção de namespace antes do processamento -- lida com qualquer variante CAMT.053 de forma segura

## Segurança de Arquivos ZIP

`iter_secure_xml_entries()` valida cada membro ZIP antes da extração:

- **Limite de tamanho de entrada**: 10 MB por entrada (configurável)
- **Limite de tamanho total**: 50 MB total descomprimido (configurável)
- **Limite de taxa de compressão**: padrão 100:1 -- detecta ZIP bombs
- **Rejeição de entradas criptografadas**: Entradas criptografadas são ignoradas com aviso
- **Sem gravação em disco**: Bytes XML passam direto para o parser via `from_bytes()`

## Prevenção de Travessia de Caminho

A validação de entrada bloqueia caminhos de arquivo perigosos:

- Bytes nulos, padrões de travessia de diretório (`../`) e links simbólicos são rejeitados
- Validação de extensão de arquivo contra formatos esperados
- Limites de tamanho de arquivo (padrão 100 MB, configurável)

## Verificação de Saldo (Golden Rule)

Toda extração de PDF é verificada com a equação: `opening balance + credits − debits == closing balance`. Os resultados são marcados como VERIFIED, DISCREPANCY ou FAILED. Discrepâncias podem ser revisadas interativamente com `--type review`.

## Saída Determinística

Para formatos estruturados (CAMT, PAIN.001, CSV, OFX, QFX, MT940), dado o mesmo arquivo de entrada, o parser produz saída idêntica em bytes a cada execução. Sem aleatoriedade, sem inferência de modelo, sem amostragem heurística. Isso é essencial para:

- **Reprodutibilidade de auditoria**: Execute o mesmo arquivo duas vezes e compare a saída
- **Conformidade regulatória**: Demonstre processamento consistente
- **Verificação de CI**: 718 testes impõem determinismo com 100% de cobertura de ramificação

## Segurança da Cadeia de Suprimentos

- **Dependências bloqueadas por hash SHA-256**: Cada pacote em `poetry.lock` tem hashes de arquivo verificados
- **CycloneDX SBOM**: Cada versão inclui uma lista de materiais de software
- **Procedência de build do GitHub**: Atestado vincula cada artefato ao seu commit de origem
- **Commits assinados**: Todos os commits são assinados por SSH e verificados no CI
- **Verificação de dependências**: `scripts/verify_locked_hashes.py` valida todos os hashes localmente

## Verifique Localmente

```bash
python -m pytest                          # 718 tests, 100% branch coverage
python scripts/verify_locked_hashes.py    # SHA-256 hash verification
git log --show-signature -1               # Verify commit signature
```
