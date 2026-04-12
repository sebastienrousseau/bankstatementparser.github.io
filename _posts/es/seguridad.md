---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Seguridad del analizador de extractos bancarios"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Analizador de extractos bancarios. Reservados todos los derechos."
date: "Apr 11, 2026"
description: "Funciones de seguridad de Bank Statement Parser: protección XXE, protección contra bombas ZIP, redacción de PII, seguridad de la cadena de suministro, salida determinista y compilaciones firmadas."
download: ""
format-detection: "telephone=no"
hreflang: "es"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/es/seguridad/index.html"
image_alt: "Logotipo del analizador de extractos bancarios: potencie su análisis financiero con una extracción de datos perfecta"
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "seguridad de extractos bancarios, redacción de PII en Python, protección XXE, protección contra bombas ZIP, seguridad de la cadena de suministro SBOM, análisis determinista, seguridad de datos financieros"
language: "es-ES"
layout: "about"
locale: "es_ES"
logo_alt: "Logotipo del analizador de extractos bancarios: potencie su análisis financiero con una extracción de datos perfecta"
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Seguridad"
permalink: "https://bankstatementparser.com/es/seguridad/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Cómo protegemos sus datos financieros"
tags: "seguridad,pii,xxe,sbom,cadena de suministro,determinista"
theme_color: "rgb(73, 214, 251)"
title: "Seguridad del analizador de extractos bancarios: protección de datos y cadena de suministro"
url: "https://bankstatementparser.com/es/seguridad/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/es/seguridad/rss.xml"
category: "Software financiero, biblioteca Python, procesamiento de datos"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Funciones de seguridad de Bank Statement Parser: protección XXE, protección contra bombas ZIP, redacción de PII, seguridad de la cadena de suministro, salida determinista y compilaciones firmadas."
item_guid: "https://bankstatementparser.com/es/seguridad/rss.xml"
item_link: "https://bankstatementparser.com/es/seguridad/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Seguridad del analizador de extractos bancarios: protección de datos y cadena de suministro"
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
apple-mobile-web-app-title: "Seguridad del analizador de extractos bancarios: protección de datos y cadena de suministro"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Funciones de seguridad de Bank Statement Parser: protección XXE, protección contra bombas ZIP, redacción de PII, seguridad de la cadena de suministro, salida determinista y compilaciones firmadas."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logotipo del analizador de extractos bancarios: potencie su análisis financiero con una extracción de datos perfecta"
twitter_site: "@wwdseb"
twitter_title: "Seguridad del analizador de extractos bancarios: protección de datos y cadena de suministro"
twitter_url: "https://bankstatementparser.com/es/seguridad/index.html"

# Humans.txt - The Humans.txt front matter (YAML).

author_website: "https://bankstatementparser.com"
author_twitter: "@wwdseb"
author_location: "London, UK"
thanks: "¡Gracias por leer!"
site_last_updated: "2026-04-01"
site_standards: "HTML5, CSS3, RSS, Atom, JSON, XML, YAML, Markdown, TOML"
site_components: "Shokunin SSG, Shokunin CLI, Shokunin Templates, Shokunin Themes, Kaishi SSG, Kaishi CLI, Kaishi Templates, Kaishi Themes"
site_software: "Shokunin, Rust"

---

**TL;DR:** Bank Statement Parser procesa todos los datos de forma local, redacta PII por defecto, refuerza el análisis XML contra ataques XXE, ejecuta LLMs localmente vía Ollama y se distribuye con dependencias SHA-256 bloqueadas con hash y un SBOM CycloneDX.

## Seguridad por diseño

Bank Statement Parser está diseñado para procesar datos financieros sensibles. Cada decisión de diseño prioriza la seguridad, la privacidad y la auditabilidad.

## Cero dependencia de la nube

Todo el procesamiento ocurre localmente dentro de su entorno de ejecución. Los analizadores deterministas no realizan llamadas de red. El pipeline híbrido para PDF usa Ollama para inferencia local de LLM — ningún dato se envía a APIs en la nube. Los analizadores XML están configurados explícitamente con `no_network=True`, `resolve_entities=False` y `load_dtd=False` para impedir cualquier acceso saliente.

## Redacción de PII

La información de identificación personal (nombres, IBANs, direcciones postales) se redacta automáticamente en la salida CLI y en modo streaming. Esto está activado por defecto.

- **CLI**: Los campos sensibles se muestran como `***REDACTED***`
- **Streaming**: `parse_streaming(redact_pii=True)` (por defecto)
- **Exportaciones**: CSV/JSON/Excel conservan todos los datos para procesamiento posterior
- **Activar**: Use `--show-pii` o `redact_pii=False` cuando necesite datos sin redactar

## Seguridad XML (protección XXE)

Todo el análisis XML usa `lxml` con ajustes reforzados:

- `resolve_entities=False` -- previene ataques de expansión de entidades XML
- `no_network=True` -- bloquea todo acceso de red saliente desde el analizador
- `load_dtd=False` -- previene ataques basados en DTD
- Eliminación de namespaces antes del procesamiento — maneja cualquier variante de CAMT.053 de forma segura

## Seguridad de archivos ZIP

`iter_secure_xml_entries()` valida cada miembro ZIP antes de la extracción:

- **Límite de tamaño de entrada**: 10 MB por entrada (configurable)
- **Límite de tamaño total**: 50 MB total sin comprimir (configurable)
- **Límite de ratio de compresión**: 100:1 por defecto — detecta ZIP bombs
- **Rechazo de entradas cifradas**: Las entradas cifradas se omiten con una advertencia
- **Sin escrituras en disco**: Los bytes XML pasan directamente al analizador vía `from_bytes()`

## Prevención de cruce de rutas

La validación de entrada bloquea rutas de archivo peligrosas:

- Bytes nulos, patrones de recorrido de directorio (`../`) y enlaces simbólicos se rechazan
- Validación de extensión de archivo frente a formatos esperados
- Límites de tamaño de archivo (100 MB por defecto, configurable)

## Verificación de saldo (Regla de Oro)

Cada extracción de PDF se verifica con la ecuación: `opening balance + credits − debits == closing balance`. Los resultados se etiquetan como VERIFIED, DISCREPANCY o FAILED. Las discrepancias pueden revisarse de forma interactiva con `--type review`.

## Salida determinista

Para formatos estructurados (CAMT, PAIN.001, CSV, OFX, QFX, MT940), dado el mismo archivo de entrada, el analizador produce una salida byte a byte idéntica en cada ejecución. Sin aleatoriedad, sin inferencia de modelo, sin muestreo heurístico. Esto es fundamental para:

- **Reproducibilidad de auditoría**: Ejecute el mismo archivo dos veces y compare la salida
- **Cumplimiento normativo**: Demostrar procesamiento coherente
- **Verificación de CI**: 718 pruebas imponen determinismo con cobertura de ramas del 100%

## Seguridad de la cadena de suministro

- **Dependencias con bloqueo hash SHA-256**: Cada paquete en `poetry.lock` tiene hashes de archivo verificados
- **CycloneDX SBOM**: Cada versión incluye una lista de materiales del software
- **Procedencia de compilación de GitHub**: La certificación vincula cada artefacto con su commit de origen
- **Commits firmados**: Todos los commits están firmados con SSH y verificados en CI
- **Verificación de dependencias**: `scripts/verify_locked_hashes.py` valida todos los hashes localmente

## Verificar localmente

```bash
python -m pytest                          # 718 tests, 100% branch coverage
python scripts/verify_locked_hashes.py    # SHA-256 hash verification
git log --show-signature -1               # Verify commit signature
```
