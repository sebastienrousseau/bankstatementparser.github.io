---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Seguridad del analizador de extractos bancarios"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Analizador de extractos bancarios. Reservados todos los derechos."
date: "Apr 01, 2026"
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

**TL;DR:** Bank Statement Parser no realiza llamadas de red, redacta PII de forma predeterminada, refuerza el análisis XML contra ataques XXE y se envía con dependencias SHA-256 bloqueadas con hash y un SBOM CycloneDX.

## Seguridad por diseño

Bank Statement Parser está diseñado para procesar datos financieros confidenciales. Cada decisión de diseño prioriza la seguridad, la privacidad y la auditabilidad.

## Acceso cero a la red

Todo el procesamiento ocurre localmente dentro de su tiempo de ejecución. La biblioteca no realiza llamadas API, cero conexiones a la nube y no recopila telemetría. Los analizadores XML están configurados explícitamente con`no_network=True`, `resolve_entities=False`, y`load_dtd=False`para impedir cualquier acceso saliente.

## Redacción de PII

La información de identificación personal (nombres, IBAN, direcciones postales) se redacta automáticamente en el modo de salida y transmisión CLI. Esto está activado de forma predeterminada.

- **CLI**: los campos sensibles se muestran como`***REDACTED***`
- **Transmisión**:`parse_streaming(redact_pii=True)`(por defecto)
- **Exportaciones**: CSV/JSON/Excel conservan todos los datos para el procesamiento posterior
- **Aceptar**: utilizar`--show-pii`o`redact_pii=False`cuando necesitas resultados sin editar

## Seguridad XML (Protección XXE)

Todos los usos del análisis XML`lxml`con ajustes reforzados:

- `resolve_entities=False`-- previene ataques de expansión de entidades XML
-`no_network=True`-- bloquea todo el acceso a la red saliente desde el analizador
-`load_dtd=False`-- previene ataques basados en DTD
- Eliminación del espacio de nombres antes del procesamiento: maneja cualquier variante de CAMT.053 de forma segura

## Seguridad del archivo ZIP

`iter_secure_xml_entries()`valida cada miembro ZIP antes de la extracción:

- **Límite de tamaño de entrada**: 10 MB por entrada (configurable)
- **Límite de tamaño total**: 50 MB en total sin comprimir (configurable)
- **Límite de relación de compresión**: 100:1 predeterminado: detecta bombas ZIP
- **Rechazo de entrada cifrada**: las entradas cifradas se omiten con una advertencia
- **Sin escrituras en disco**: los bytes XML pasan directamente al analizador a través de`from_bytes()`

## Prevención de cruce de caminos

La validación de entrada bloquea rutas de archivos peligrosas:

- Bytes nulos, patrones de recorrido de directorio (`../`), y los enlaces simbólicos se rechazan
- Validación de extensión de archivo frente a formatos esperados.
- Límites de tamaño de archivo (100 MB predeterminado, configurable)

## Salida determinista

Dado el mismo archivo de entrada, el analizador produce una salida de bytes idénticos en cada ejecución. Sin aleatoriedad, sin inferencia de modelo, sin muestreo heurístico. Esto es fundamental para:

- **Reproducibilidad de la auditoría**: ejecute el mismo archivo dos veces y diferencie el resultado
- **Cumplimiento normativo**: demostrar un procesamiento coherente
- **Verificación de CI**: 467 pruebas aplican el determinismo con una cobertura de sucursales del 100 %

## Seguridad de la cadena de suministro

- **Dependencias con bloqueo hash SHA-256**: cada paquete en`poetry.lock`ha verificado hashes de archivos
- **CycloneDX SBOM**: cada versión incluye una lista de materiales del software
- **Procedencia de la compilación de GitHub**: la certificación vincula cada artefacto con su confirmación de origen
- **Confirmaciones firmadas**: todas las confirmaciones están firmadas por SSH y verificadas en CI
- **Verificación de dependencia**:`scripts/verify_locked_hashes.py`valida todos los hashes localmente

## Verificar localmente

```bash
python -m pytest                          # 467 tests, 100% branch coverage
python scripts/verify_locked_hashes.py    # SHA-256 hash verification
git log --show-signature -1               # Verify commit signature
```
