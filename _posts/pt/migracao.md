---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Guia de migração ISO 20022"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Analisador de extrato bancário. Todos os direitos reservados."
date: "Apr 01, 2026"
description: "Um guia prático para o cronograma de migração SWIFT ISO 20022 (2026-2028), transição MT940 para CAMT.053 e como o Bank Statement Parser ajuda as equipes de tesouraria a migrar."
download: ""
format-detection: "telephone=no"
hreflang: "pt"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/pt/migracao/index.html"
image_alt: "Logotipo do analisador de extrato bancário, capacite sua análise financeira com extração contínua de dados"
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "Migração ISO 20022, MT940 para CAMT.053, prazo SWIFT 2027, aposentadoria MT940 2028, migração de extrato bancário python, analisador CAMT.053, cronograma ISO 20022"
language: "pt-BR"
layout: "about"
locale: "pt_BR"
logo_alt: "Logotipo do analisador de extrato bancário, capacite sua análise financeira com extração contínua de dados"
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Guia de migração ISO 20022"
permalink: "https://bankstatementparser.com/pt/migracao/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Navegue no SWIFT MT para a transição ISO 20022"
tags: "iso20022,migração,mt940,camt053,rápido,linha do tempo"
theme_color: "rgb(73, 214, 251)"
title: "Guia de migração ISO 20022: Transição MT940 para CAMT.053"
url: "https://bankstatementparser.com/pt/migracao/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/pt/migracao/rss.xml"
category: "Software financeiro, biblioteca Python, processamento de dados"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Um guia prático para o cronograma de migração SWIFT ISO 20022 (2026-2028), transição MT940 para CAMT.053 e como o Bank Statement Parser ajuda as equipes de tesouraria a migrar."
item_guid: "https://bankstatementparser.com/pt/migracao/rss.xml"
item_link: "https://bankstatementparser.com/pt/migracao/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Guia de migração ISO 20022: Transição MT940 para CAMT.053"
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
apple-mobile-web-app-title: "Guia de migração ISO 20022: Transição MT940 para CAMT.053"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Um guia prático para o cronograma de migração SWIFT ISO 20022 (2026-2028), transição MT940 para CAMT.053 e como o Bank Statement Parser ajuda as equipes de tesouraria a migrar."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logotipo do analisador de extrato bancário, capacite sua análise financeira com extração contínua de dados"
twitter_site: "@wwdseb"
twitter_title: "Guia de migração ISO 20022: Transição MT940 para CAMT.053"
twitter_url: "https://bankstatementparser.com/pt/migracao/index.html"

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

**TL;DR:** SWIFT retirará o MT940 até novembro de 2028. O Bank Statement Parser lida com MT940 e CAMT.053 com uma única API, para que seu pipeline de análise funcione durante e depois da transição.

## Por que esta migração é importante

A SWIFT está retirando os formatos de mensagens MT legados em favor do padrão ISO 20022 mais rico. Para as equipes de tesouraria e finanças, isso significa que seus pipelines de processamento de extratos bancários devem evoluir de MT940 para CAMT.053 antes dos prazos rígidos.

## Cronograma de migração SWIFT

| Data | Marco | Impacto |
|---|---|---|
| **Novembro de 2025** | A coexistência MT-MX terminou para pagamentos transfronteiriços | As mensagens PACS agora são apenas ISO 20022 |
| **Novembro de 2026** | Endereços estruturados/híbridos obrigatórios; Multi-instrução MT101 rejeitada; Fase 1 de gerenciamento de caso | Os formatos de endereço devem estar em conformidade; algumas mensagens MT serão rejeitadas |
| **Final de 2026** | A inscrição começa para receber CAMT.052/.053/.054 | Instituições financeiras podem começar a receber declarações ISO nativas |
| **Novembro de 2027** | Todos os IFs devem receber o CAMT.053 nativamente | SWIFT para de converter o formato MT para ISO; seus sistemas devem analisar o CAMT diretamente |
| **Novembro de 2028** | MT940/MT942/MT950/MT900/MT910 totalmente aposentado | Os formatos de extrato legados não estão mais disponíveis; CAMT.052/.053/.054 são a única opção |

## O que muda no seu código

### Antes: Somente MT940

```python
from bankstatementparser import Mt940Parser

parser = Mt940Parser("statement.mt940")
df = parser.parse()
```

### Depois: ambos os formatos com detecção automática

```python
from bankstatementparser import create_parser, detect_statement_format

fmt = detect_statement_format("statement.xml")  # or .mt940
parser = create_parser("statement.xml", fmt)
df = parser.parse()  # Same DataFrame schema regardless of format
```

O`detect_statement_format()`função identifica se o arquivo é MT940, CAMT.053, PAIN.001 ou qualquer outro formato suportado. O`create_parser()`função retorna o analisador correto. Seu código downstream funciona de forma idêntica, independentemente do formato de origem.

## CAMT.053 vs MT940: Principais diferenças

| Recurso | MT940 | CAMT.053 |
|---|---|---|
| Riqueza de dados | Campos limitados | 3 a 5x mais dados por transação |
| Conjunto de caracteres | Limitado (conjunto de caracteres SWIFT) | Unicode completo |
| Estrutura | Texto simples com tags | XML com namespaces |
| Relatório de saldo | Somente abertura/fechamento | Vários tipos de saldo |
| Referências | Campo de referência único | Vários tipos de referência |
| Manuseio de moeda | Básico | Multi-moeda completa com taxas de câmbio |

## Como o analisador de extrato bancário ajuda

- **API unificada**: analise MT940 e CAMT.053 com o mesmo`parse()`método, produzindo esquemas DataFrame idênticos.
- **Detecção automática**: Não há necessidade de saber o formato com antecedência.`detect_statement_format()`identifica-o automaticamente.
- **Independente de namespace**: Lida com qualquer variante CAMT.053 (001.02, 001.04 ou wrappers específicos do banco) sem configuração.
- **Streaming**: processe arquivos CAMT grandes (50 MB+, 50K+ transações) com memória limitada.
- **Testes de migração**: execute os dois analisadores lado a lado no mesmo intervalo de datas para verificar a consistência da saída antes de alternar.

## Começando

```bash
pip install bankstatementparser
```

```python
from bankstatementparser import create_parser, detect_statement_format

# Works with MT940 today, CAMT.053 tomorrow
for file in bank_statement_files:
    fmt = detect_statement_format(file)
    parser = create_parser(file, fmt)
    df = parser.parse()
    process(df)  # Your code doesn't change
```

[Leia a documentação completa](/getting-started/index.html)

[Compare com alternativas ❯](/comparison/index.html) | [Veja casos de uso reais ❯](/use-cases/index.html)
