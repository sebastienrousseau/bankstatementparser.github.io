---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Sécurité de l'analyseur de relevé bancaire"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Analyseur de relevés bancaires. Tous droits réservés."
date: "Apr 11, 2026"
description: "Fonctionnalités de sécurité de Bank Statement Parser : protection XXE, renforcement des bombes ZIP, rédaction des informations personnelles, sécurité de la chaîne d'approvisionnement, sortie déterministe et versions signées."
download: ""
format-detection: "telephone=no"
hreflang: "fr"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/fr/securite/index.html"
image_alt: "Logo de l'analyseur de relevés bancaires, renforcez votre analyse financière avec une extraction transparente des données"
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "sécurité des relevés bancaires, rédaction des PII python, protection XXE, protection contre les bombes ZIP, sécurité de la chaîne d'approvisionnement SBOM, analyse déterministe, sécurité des données financières"
language: "fr-FR"
layout: "about"
locale: "fr_FR"
logo_alt: "Logo de l'analyseur de relevés bancaires, renforcez votre analyse financière avec une extraction transparente des données"
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Sécurité"
permalink: "https://bankstatementparser.com/fr/securite/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Comment nous protégeons vos données financières"
tags: "sécurité, pii, xxe, sbom, chaîne d'approvisionnement, déterministe"
theme_color: "rgb(73, 214, 251)"
title: "Sécurité de l'analyseur de relevés bancaires : protection des données et chaîne d'approvisionnement"
url: "https://bankstatementparser.com/fr/securite/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/fr/securite/rss.xml"
category: "Logiciel de finance, bibliothèque Python, traitement des données"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Fonctionnalités de sécurité de Bank Statement Parser : protection XXE, renforcement des bombes ZIP, rédaction des informations personnelles, sécurité de la chaîne d'approvisionnement, sortie déterministe et versions signées."
item_guid: "https://bankstatementparser.com/fr/securite/rss.xml"
item_link: "https://bankstatementparser.com/fr/securite/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Sécurité de l'analyseur de relevés bancaires : protection des données et chaîne d'approvisionnement"
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
apple-mobile-web-app-title: "Sécurité de l'analyseur de relevés bancaires : protection des données et chaîne d'approvisionnement"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Fonctionnalités de sécurité de Bank Statement Parser : protection XXE, renforcement des bombes ZIP, rédaction des informations personnelles, sécurité de la chaîne d'approvisionnement, sortie déterministe et versions signées."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logo de l'analyseur de relevés bancaires, renforcez votre analyse financière avec une extraction transparente des données"
twitter_site: "@wwdseb"
twitter_title: "Sécurité de l'analyseur de relevés bancaires : protection des données et chaîne d'approvisionnement"
twitter_url: "https://bankstatementparser.com/fr/securite/index.html"

# Humans.txt - The Humans.txt front matter (YAML).

author_website: "https://bankstatementparser.com"
author_twitter: "@wwdseb"
author_location: "London, UK"
thanks: "Merci d'avoir lu!"
site_last_updated: "2026-04-01"
site_standards: "HTML5, CSS3, RSS, Atom, JSON, XML, YAML, Markdown, TOML"
site_components: "Shokunin SSG, Shokunin CLI, Shokunin Templates, Shokunin Themes, Kaishi SSG, Kaishi CLI, Kaishi Templates, Kaishi Themes"
site_software: "Shokunin, Rust"

---

**En bref :** Bank Statement Parser traite toutes les données localement, masque les données personnelles par défaut, durcit l'analyse XML contre les attaques XXE, exécute les LLM localement via Ollama et livre des dépendances verrouillées par hash SHA-256 avec un SBOM CycloneDX.

## Sécurité par conception

Bank Statement Parser est conçu pour traiter des données financières sensibles. Chaque décision de conception privilégie la sécurité, la confidentialité et l'auditabilité.

## Zéro dépendance cloud

Tout le traitement s'effectue localement dans votre environnement d'exécution. Les analyseurs déterministes ne font aucun appel réseau. Le pipeline PDF hybride utilise Ollama pour l'inférence LLM locale — aucune donnée n'est envoyée vers des API cloud. Les analyseurs XML sont explicitement configurés avec `no_network=True`, `resolve_entities=False` et `load_dtd=False` pour bloquer tout accès sortant.

## Masquage des données personnelles

Les informations personnellement identifiables (noms, IBAN, adresses postales) sont automatiquement masquées dans la sortie CLI et le mode streaming. Cette protection est activée par défaut.

- **CLI** : les champs sensibles affichent `***REDACTED***`
- **Streaming** : `parse_streaming(redact_pii=True)` (par défaut)
- **Exports** : CSV/JSON/Excel conservent les données complètes pour le traitement en aval
- **Affichage complet** : utilisez `--show-pii` ou `redact_pii=False` quand vous avez besoin de la sortie non masquée

## Sécurité XML (protection XXE)

Toute l'analyse XML utilise `lxml` avec des paramètres durcis :

- `resolve_entities=False` -- empêche les attaques par expansion d'entités XML
- `no_network=True` -- bloque tout accès réseau sortant depuis l'analyseur
- `load_dtd=False` -- empêche les attaques basées sur les DTD
- Suppression des espaces de noms avant traitement -- gère toute variante CAMT.053 en toute sécurité

## Sécurité des archives ZIP

`iter_secure_xml_entries()` valide chaque membre ZIP avant l'extraction :

- **Plafond de taille d'entrée** : 10 Mo par entrée (configurable)
- **Plafond de taille totale** : 50 Mo décompressés au total (configurable)
- **Limite de taux de compression** : 100:1 par défaut -- détecte les ZIP bombs
- **Rejet des entrées chiffrées** : les entrées chiffrées sont ignorées avec un avertissement
- **Aucune écriture sur le disque** : les octets XML passent directement à l'analyseur via `from_bytes()`

## Prévention de la traversée de chemin

La validation des entrées bloque les chemins de fichiers dangereux :

- Les octets nuls, les motifs de traversée de répertoire (`../`) et les liens symboliques sont rejetés
- Validation de l'extension de fichier par rapport aux formats attendus
- Limites de taille de fichier (100 Mo par défaut, configurable)

## Vérification du solde (Règle d'or)

Chaque extraction PDF est vérifiée avec l'équation : `opening balance + credits − debits == closing balance`. Les résultats sont étiquetés VERIFIED, DISCREPANCY ou FAILED. Les écarts peuvent être revus de manière interactive avec `--type review`.

## Sortie déterministe

Pour les formats structurés (CAMT, PAIN.001, CSV, OFX, QFX, MT940), pour un même fichier d'entrée, l'analyseur produit une sortie identique octet par octet à chaque exécution. Pas de hasard, pas d'inférence de modèle, pas d'échantillonnage heuristique. Cela est essentiel pour :

- **Reproductibilité des audits** : exécutez le même fichier deux fois et comparez la sortie
- **Conformité réglementaire** : démontrez un traitement cohérent
- **Vérification CI** : 718 tests imposent le déterminisme avec 100 % de couverture de branches

## Sécurité de la chaîne d'approvisionnement

- **Dépendances verrouillées par hash SHA-256** : chaque package dans `poetry.lock` a des hash de fichiers vérifiés
- **SBOM CycloneDX** : chaque version inclut une nomenclature logicielle
- **Provenance de build GitHub** : l'attestation relie chaque artefact à son commit source
- **Commits signés** : tous les commits sont signés par SSH et vérifiés en CI
- **Vérification des dépendances** : `scripts/verify_locked_hashes.py` valide tous les hash localement

## Vérifiez localement

```bash
python -m pytest                          # 718 tests, 100% branch coverage
python scripts/verify_locked_hashes.py    # SHA-256 hash verification
git log --show-signature -1               # Verify commit signature
```
