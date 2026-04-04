---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Sécurité de l'analyseur de relevé bancaire"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Analyseur de relevés bancaires. Tous droits réservés."
date: "Apr 01, 2026"
description: "Fonctionnalités de sécurité de Bank Statement Parser : protection XXE, renforcement des bombes ZIP, rédaction des informations personnelles, sécurité de la chaîne d'approvisionnement, sortie déterministe et versions signées."
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
title: "Sécurité de l'analyseur de relevés bancaires : protection des données et chaîne d'approvisionnement"
url: "https://bankstatementparser.com/fr/securite/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/fr/securite/rss.xml"
category: "Logiciel de finance, bibliothèque Python, traitement des données"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Fonctionnalités de sécurité de Bank Statement Parser : protection XXE, renforcement des bombes ZIP, rédaction des informations personnelles, sécurité de la chaîne d'approvisionnement, sortie déterministe et versions signées."
item_guid: "https://bankstatementparser.com/fr/securite/rss.xml"
item_link: "https://bankstatementparser.com/fr/securite/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Sécurité de l'analyseur de relevés bancaires : protection des données et chaîne d'approvisionnement"
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
apple-mobile-web-app-title: "Sécurité de l'analyseur de relevés bancaires : protection des données et chaîne d'approvisionnement"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Fonctionnalités de sécurité de Bank Statement Parser : protection XXE, renforcement des bombes ZIP, rédaction des informations personnelles, sécurité de la chaîne d'approvisionnement, sortie déterministe et versions signées."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logo de l'analyseur de relevés bancaires, renforcez votre analyse financière avec une extraction transparente des données"
twitter_site: "@wwdseb"
twitter_title: "Sécurité de l'analyseur de relevés bancaires : protection des données et chaîne d'approvisionnement"
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

**TL;DR :** Bank Statement Parser n'effectue aucun appel réseau, supprime les informations personnelles par défaut, renforce l'analyse XML contre les attaques XXE et est livré avec des dépendances verrouillées par hachage SHA-256 et un SBOM CycloneDX.

## La sécurité dès la conception

Bank Statement Parser est conçu pour traiter des données financières sensibles. Chaque décision de conception donne la priorité à la sécurité, à la confidentialité et à l’auditabilité.

## Zéro accès au réseau

Tout le traitement s'effectue localement au sein de votre environnement d'exécution. La bibliothèque n'effectue aucun appel d'API, aucune connexion au cloud et ne collecte aucune télémétrie. Les analyseurs XML sont explicitement configurés avec`no_network=True`, `resolve_entities=False`, et`load_dtd=False`pour empêcher tout accès sortant.

## Rédaction des informations personnelles

Les informations personnelles identifiables (noms, IBAN, adresses postales) sont automatiquement rédigées en sortie CLI et en mode streaming. Ceci est activé par défaut.

- **CLI** : les champs sensibles s'affichent comme`***REDACTED***`
- **Streaming**:`parse_streaming(redact_pii=True)`(défaut)
- **Exportations** : CSV/JSON/Excel conservent toutes les données pour le traitement en aval
- **Opt-in** : Utiliser`--show-pii`ou`redact_pii=False`quand vous avez besoin d'une sortie non expurgée

## Sécurité XML (Protection XXE)

Toutes les utilisations de l'analyse XML`lxml`avec des réglages renforcés :

- `resolve_entities=False`-- empêche les attaques par expansion d'entité XML
-`no_network=True`-- bloque tout accès réseau sortant depuis l'analyseur
-`load_dtd=False`-- empêche les attaques basées sur DTD
- Suppression de l'espace de noms avant le traitement - gère toute variante CAMT.053 en toute sécurité

## Sécurité des archives ZIP

`iter_secure_xml_entries()`valide chaque membre ZIP avant l'extraction :

- **Plafond de taille d'entrée** : 10 Mo par entrée (configurable)
- **Taille maximale** : 50 Mo au total non compressé (configurable)
- **Limite du taux de compression** : 100:1 par défaut -- détecte les bombes ZIP
- **Rejet d'entrée cryptée** : les entrées cryptées sont ignorées avec un avertissement
- **Aucune écriture sur disque** : les octets XML sont transmis directement à l'analyseur via`from_bytes()`

## Prévention des traversées de chemin

La validation des entrées bloque les chemins de fichiers dangereux :

- Octets nuls, modèles de parcours de répertoire (`../`), et les liens symboliques sont rejetés
- Validation des extensions de fichiers par rapport aux formats attendus
- Limites de taille de fichier (100 Mo par défaut, configurable)

## Sortie déterministe

Étant donné le même fichier d’entrée, l’analyseur produit une sortie identique en octets à chaque exécution. Pas de hasard, pas d'inférence de modèle, pas d'échantillonnage heuristique. Ceci est essentiel pour :

- **Reproductibilité de l'audit** : exécutez le même fichier deux fois et comparez la sortie
- **Conformité réglementaire** : démontrer un traitement cohérent
- **Vérification CI** : 467 tests appliquent le déterminisme avec une couverture de branches à 100 %

## Sécurité de la chaîne d'approvisionnement

- **Dépendances verrouillées par hachage SHA-256** : chaque package dans`poetry.lock`a vérifié les hachages de fichiers
- **CycloneDX SBOM** : chaque version comprend une nomenclature logicielle
- **Provenance du build GitHub** : l'attestation relie chaque artefact à son commit source
- **Commits signés** : tous les commits sont signés SSH et vérifiés dans CI
- **Vérification des dépendances** :`scripts/verify_locked_hashes.py`valide tous les hachages localement

## Vérifier localement

```bash
python -m pytest                          # 467 tests, 100% branch coverage
python scripts/verify_locked_hashes.py    # SHA-256 hash verification
git log --show-signature -1               # Verify commit signature
```
