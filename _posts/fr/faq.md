---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Foire aux questions sur l'analyseur de relevés bancaires"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Analyseur de relevés bancaires. Tous droits réservés."
date: "Apr 11, 2026"
description: "Réponses aux questions courantes sur l'analyseur de relevés bancaires : confidentialité des données, rédaction des informations personnelles, performances, prise en charge ISO 20022, streaming, conformité et flux de travail de trésorerie."
download: ""
format-detection: "telephone=no"
hreflang: "fr"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/fr/faq/index.html"
image_alt: "Logo de Bank Statement Parser, un puissant outil Python conçu pour le traitement rapide et précis des données financières et l'extraction d'informations."
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "FAQ sur l'analyseur de relevés bancaires, questions sur l'analyseur CAMT, FAQ PAIN.001, FAQ Python ISO 20022, rédaction de PII bancaires, performances de l'analyseur bancaire, confidentialité des données financières, FAQ de l'analyseur MT940, analyseur de streaming Python, conformité des relevés bancaires"
language: "fr-FR"
layout: "faq"
locale: "fr_FR"
logo_alt: "Logo de Bank Statement Parser, un puissant outil Python conçu pour le traitement rapide et précis des données financières et l'extraction d'informations."
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "FAQ"
permalink: "https://bankstatementparser.com/fr/faq/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Questions courantes sur l'analyseur de relevés bancaires"
tags: "FAQ,banque,relevé,analyseur,confidentialité,conformité,performance,streaming,iso20022,python"
theme_color: "rgb(73, 214, 251)"
title: "FAQ sur l'analyseur de relevés bancaires : confidentialité, performances et utilisation"
url: "https://bankstatementparser.com/fr/faq/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/fr/faq/rss.xml"
category: "Logiciel financier, bibliothèque Python, FAQ"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Réponses aux questions courantes sur l'analyseur de relevés bancaires : confidentialité des données, rédaction des informations personnelles, performances, prise en charge ISO 20022, streaming, conformité et flux de travail de trésorerie."
item_guid: "https://bankstatementparser.com/fr/faq/rss.xml"
item_link: "https://bankstatementparser.com/fr/faq/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "FAQ sur l'analyseur de relevés bancaires : confidentialité, performances et utilisation"
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
apple-mobile-web-app-title: "FAQ sur l'analyseur de relevés bancaires : confidentialité, performances et utilisation"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Réponses aux questions courantes sur l'analyseur de relevés bancaires : confidentialité des données, rédaction des informations personnelles, performances, prise en charge ISO 20022 et flux de travail de trésorerie."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logo de Bank Statement Parser, un puissant outil Python conçu pour le traitement rapide et précis des données financières et l'extraction d'informations."
twitter_site: "@wwdseb"
twitter_title: "FAQ sur l'analyseur de relevés bancaires : confidentialité, performances et utilisation"
twitter_url: "https://bankstatementparser.com/fr/faq/index.html"

# Humans.txt - The Humans.txt front matter (YAML).

author_website: "https://bankstatementparser.com"
author_twitter: "@wwdseb"
author_location: "London, UK"
thanks: "Merci d'avoir lu!"
site_last_updated: "2026-04-01"
site_standards: "HTML5, CSS3, RSS, Atom, JSON, XML, YAML, Markdown, TOML"
site_components: "Shokunin SSG, Shokunin CLI, Shokunin Templates, Kaishi Templates, Kaishi Themes"
site_software: "Shokunin, Rust"

---

## Confidentialité des données et conformité

### Des données quittent-elles mon infrastructure ?

**Non — même pour l'extraction PDF.** Bank Statement Parser fonctionne comme une bibliothèque sans état. Tout le traitement — analyse, masquage des données personnelles, extraction d'archives — s'effectue dans la mémoire de votre environnement local. Le pipeline PDF hybride utilise Ollama pour l'inférence LLM locale — aucune API cloud. Les analyseurs XML sont durcis avec `no_network=True`, bloquant tout accès sortant au niveau de l'analyseur. Vos données financières ne quittent jamais votre environnement.

### Comment fonctionne le masquage des données personnelles ?

Les champs sensibles sont masqués avant d'atteindre votre logique applicative. L'analyseur identifie les noms des débiteurs, créanciers, IBAN et adresses postales, et les remplace par `***REDACTED***` dans la sortie console et le mode streaming.

- **Le masquage est activé par défaut** dans la sortie CLI et le mode streaming.
- **Les exports de fichiers** (CSV, JSON, Excel) conservent les données non masquées pour le traitement en aval.
- **Activez** l'affichage complet avec `--show-pii` en CLI ou `redact_pii=False` dans l'API.

### Le processus d'extraction est-il déterministe ?

**Oui pour les formats structurés — sortie identique octet par octet à chaque exécution.** Pour un même fichier d'entrée, les analyseurs déterministes (CAMT, PAIN.001, CSV, OFX, QFX, MT940) produisent le même résultat à chaque fois. Pas de hasard, pas d'inférence de modèle, pas d'échantillonnage heuristique.

Pour le pipeline PDF hybride, les voies d'extraction par LLM peuvent produire de légères variations entre les exécutions. C'est pourquoi chaque extraction PDF est vérifiée avec la **Règle d'or** (`opening + credits − debits == closing`) et les écarts signalés peuvent être revus de manière interactive.

L'intégration continue vérifie le déterminisme avec 718 tests à 100 % de couverture de branches, y compris du fuzzing basé sur les propriétés via Hypothesis.

### Quelles normes de conformité le projet suit-il ?

Le projet maintient une documentation alignée ISO 13485 avec traçabilité complète :

- Un **Registre des risques** quantifié avec notation de gravité/probabilité et évaluation du risque résiduel.
- Un **Plan de vérification et validation** avec 19 jalons contrôlés sur 5 phases.
- Une **Procédure de contrôle des changements** avec évaluation d'impact et protocoles de retour arrière.
- Un **Registre SOUP** couvrant toutes les dépendances avec niveaux de risque et suivi de fin de vie.
- Une **Matrice de traçabilité** reliant les entrées de conception à l'implémentation et à la vérification.

Chaque version inclut un SBOM CycloneDX, des sommes de contrôle SHA-256 et une attestation de provenance de build GitHub.

## Performance et évolutivité

### Quelle est la vitesse de Bank Statement Parser ?

Les seuils de performance sont validés en intégration continue à chaque commit :

| Métrique | Valeur |
|---|---|
| Débit CAMT.053 | 27 000+ transactions/seconde |
| Débit PAIN.001 | 52 000+ transactions/seconde |
| Latence par transaction (CAMT) | 37 microsecondes |
| Latence par transaction (PAIN.001) | 19 microsecondes |
| Temps jusqu'au premier résultat | < 2 ms |

La vitesse d'extraction PDF dépend de la voie choisie : déterministe (sous la seconde), text-LLM (secondes), vision-LLM (secondes par page).

### Comment les fichiers volumineux sont-ils gérés ?

**Streaming avec mémoire bornée — testé à 50 000 transactions par fichier.** Utilisez `parse_streaming()` pour traiter les fichiers XML de manière incrémentale. Chaque transaction est émise sous forme de dictionnaire ; les éléments sont libérés après traitement pour éviter la croissance de la mémoire. La mémoire ne croît pas avec la taille du fichier — le test à 50 000 transactions (25+ Mo) utilise moins de 2x la mémoire du test à 10 000 transactions.

Pour les fichiers de plus de 50 Mo (par exemple, des lots PAIN.001 host-to-host avec 100 000+ paiements), l'analyseur utilise le streaming via un fichier temporaire avec suppression des espaces de noms par blocs — le document complet n'est jamais chargé en mémoire.

### Comment les archives ZIP sont-elles traitées en toute sécurité ?

`iter_secure_xml_entries()` valide chaque membre avant l'extraction :

- **Plafond de taille d'entrée** (10 Mo par défaut par entrée)
- **Plafond de taille totale décompressée** (50 Mo par défaut)
- **Limite de taux de compression** (100:1 par défaut) pour prévenir les ZIP bombs
- **Rejet des entrées chiffrées**

Aucun fichier n'est écrit sur le disque. Les octets XML passent directement à l'analyseur via `from_bytes()`.

### Puis-je analyser plusieurs fichiers en parallèle ?

**Oui.** Utilisez `parse_files_parallel()` qui distribue le travail via un `ProcessPoolExecutor` :

```python
from bankstatementparser import parse_files_parallel

results = parse_files_parallel([
    "statements/jan.xml",
    "statements/feb.xml",
    "statements/mar.xml",
])
for r in results:
    print(r.path, r.status, len(r.transactions), "rows")
```

Pour l'ingestion PDF en masse, utilisez `scan_and_ingest()` qui traite des arborescences complètes avec déduplication automatique.

## Formats pris en charge

### Quels formats de relevés bancaires sont pris en charge ?

| Format | Standard | Types de fichiers | Analyseur / Méthode |
|---|---|---|---|
| CAMT.053 | ISO 20022 Relevé banque-client | `.xml` | `CamtParser` |
| PAIN.001 | ISO 20022 Initiation de virement | `.xml` | `Pain001Parser` |
| CSV | Exports bancaires génériques | `.csv` | `CsvStatementParser` |
| OFX | Open Financial Exchange | `.ofx` | `OfxParser` |
| QFX | Quicken Financial Exchange | `.qfx` | `QfxParser` |
| MT940 | Standard SWIFT | `.mt940`, `.sta` | `Mt940Parser` |
| PDF | Relevés numériques et scannés | `.pdf` | `smart_ingest()` |

### Comment fonctionne le pipeline PDF hybride ?

Le pipeline hybride (v0.0.5+) achemine les PDF de manière intelligente via trois voies d'extraction :

- **Voie A (Déterministe)** : tableaux PDF structurés analysés directement — gratuit, le plus rapide, aucun LLM requis.
- **Voie B (Text-LLM)** : PDF numériques avec mises en page complexes extraits via un LLM local (LiteLLM/Ollama).
- **Voie C (Vision-LLM)** : relevés scannés ou photocopiés traités avec des modèles de vision multimodaux.

Chaque extraction est vérifiée avec la Règle d'or (`opening + credits − debits == closing`). Les écarts peuvent être revus de manière interactive avec `--type review`.

### L'analyseur gère-t-il les dialectes CAMT.053 spécifiques aux banques ?

**Oui — indépendant des espaces de noms par conception.** L'analyseur supprime les espaces de noms XML avant le traitement, gérant toute variante CAMT.053 (`camt.053.001.02`, `camt.053.001.04` ou enveloppes propriétaires) sans configuration spécifique. Les requêtes XPath ciblent la structure des éléments, pas les URI d'espaces de noms.

Pour les banques qui enveloppent CAMT dans une enveloppe personnalisée, utilisez `from_string()` ou `from_bytes()` pour fournir directement le document interne.

### Puis-je mapper des en-têtes CSV personnalisés vers le schéma standard ?

**Oui — normalisation automatique, zéro configuration.** `CsvStatementParser` reconnaît les variantes d'en-têtes courantes : `"Date"`, `"Transaction Date"`, `"Booking Date"` sont tous mappés vers le champ `date`. `"Amount"`, `"Value"`, `"Sum"` sont mappés vers `amount`. Les colonnes crédit/débit séparées (par exemple, `"Credit"` et `"Debit"`) sont détectées et combinées automatiquement en un montant signé unique.

### Quel est le format de sortie ?

Tous les analyseurs produisent des DataFrames pandas standardisés avec des types de colonnes cohérents :

| Format | Colonnes principales |
|---|---|
| **CAMT** | `Amount`, `Currency`, `DrCr`, `Debtor`, `Creditor`, `Reference`, `ValDt`, `BookgDt`, `AccountId` |
| **PAIN.001** | `PmtInfId`, `PmtMtd`, `InstdAmt`, `Currency`, `CdtrNm`, `EndToEndId`, `MsgId`, `CreDtTm`, `NbOfTxs` |
| **CSV/OFX/QFX/MT940** | `date`, `description`, `amount` (normalisé) |

Vous pouvez aussi exporter en CSV, JSON, Excel, DataFrames Polars, journal hledger ou beancount.

## PDF et fonctionnalités LLM

### Quels modèles LLM le pipeline hybride prend-il en charge ?

Le pipeline utilise LiteLLM comme couche d'abstraction de modèles, avec un pont direct vers Ollama pour les prompts de vision. Modèles recommandés :

- **Extraction de texte** : tout modèle compatible LiteLLM (local ou distant).
- **Extraction par vision** : `ollama/minicpm-v` (recommandé) pour les PDF scannés.
- **Catégorisation** : tout modèle compatible LiteLLM.

Tous les modèles peuvent fonctionner à 100 % en local via Ollama — aucune clé API requise.

### Qu'est-ce que la vérification par la Règle d'or ?

Chaque extraction PDF est vérifiée avec l'équation : `opening balance + credits − debits == closing balance`. Les résultats sont étiquetés comme :

- **VERIFIED** : les soldes correspondent exactement.
- **DISCREPANCY** : les soldes ne correspondent pas — revue recommandée.
- **FAILED** : la vérification n'a pas pu être effectuée (données de solde manquantes).

### Puis-je catégoriser les transactions automatiquement ?

**Oui.** Le module d'enrichissement (v0.0.6+) propose une catégorisation des transactions par LLM :

```python
from bankstatementparser.enrichment import Categorizer

categorizer = Categorizer()
enriched = categorizer.categorize_batch(transactions)
```

Le schéma par défaut utilise 13 catégories compatibles Plaid. Vous pouvez fournir votre propre schéma de catégories.

### Puis-je exporter vers hledger ou beancount ?

**Oui** (v0.0.8+). Exportez les transactions au format journal de comptabilité en texte brut avec mappage de comptes :

```python
from bankstatementparser.export import to_hledger, to_beancount

journal = to_hledger(transactions, account="Assets:Bank:Checking")
```

## Flux de travail de trésorerie

### Comment l'analyseur gère-t-il les relevés multi-devises ?

**Chaque transaction conserve sa devise d'origine — aucune conversion implicite.** Le champ `Currency` est extrait de l'attribut XML `Ccy` pour chaque transaction. Les relevés multi-devises restent tels quels. La méthode `get_account_balances()` renvoie les soldes d'ouverture et de clôture par compte avec les codes devise d'origine.

Depuis la v0.0.8, `verify_balance_multi_currency()` regroupe les transactions par devise et exécute la Règle d'or indépendamment par groupe — utile pour les comptes contenant plusieurs devises.

### L'analyseur prend-il en charge les formats sortants et entrants ?

**Oui.** `Pain001Parser` gère les fichiers d'initiation de virement ISO 20022 PAIN.001 (paiements sortants). `CamtParser` gère les fichiers de relevé banque-client CAMT.053 (reporting entrant). Les deux prennent en charge le streaming, le masquage des données personnelles et l'export en CSV, JSON, Excel, hledger et beancount. Utilisez `detect_statement_format()` pour identifier le format automatiquement.

### Que se passe-t-il quand une écriture de transaction est malformée ?

Le comportement dépend du mode d'analyse :

- **`parse()` (mode batch)** — Les entrées malformées sans champs obligatoires (`Amount`, `Currency` ou `CdtDbtInd`) sont ignorées avec un avertissement dans le journal. Le reste du relevé est analysé normalement.
- **`parse_streaming()` (mode streaming)** — Les erreurs d'analyse se propagent immédiatement sous forme d'exceptions. Aucune perte silencieuse de données. Ce comportement fail-fast est intentionnel pour les flux financiers où chaque transaction doit être comptabilisée.
- **`smart_ingest()` (PDF hybride)** — Les erreurs d'extraction sont capturées dans le `IngestResult` avec le statut de vérification, permettant une revue interactive.

### Comment fonctionne la déduplication ?

Chaque transaction se voit attribuer un `transaction_hash` idempotent (empreinte MD5) basé sur ses champs clés. Cela permet une ingestion incrémentale fiable — le retraitement du même fichier produit les mêmes hash, donc les doublons sont détectés automatiquement.

```python
from bankstatementparser import CamtParser, Deduplicator

parser = CamtParser("statement.xml")
dedup = Deduplicator()
result = dedup.deduplicate(dedup.from_dataframe(parser.parse()))

print(f"Unique: {len(result.unique_transactions)}")
print(f"Exact duplicates: {len(result.exact_duplicates)}")
print(f"Suspected matches: {len(result.suspected_matches)}")
```

## Installation et compatibilité

### Comment installer Bank Statement Parser ?

```bash
# Core install (deterministic parsers only)
pip install bankstatementparser

# PDF hybrid pipeline
pip install 'bankstatementparser[hybrid]'         # Text-LLM path
pip install 'bankstatementparser[hybrid-vision]'   # Vision-LLM path

# Extras
pip install 'bankstatementparser[enrichment]'      # Transaction categorisation
pip install 'bankstatementparser[api]'             # REST API microservice
pip install 'bankstatementparser[polars]'          # Polars DataFrame support
```

### Quelles versions de Python sont prises en charge ?

Python 3.10 à 3.14. Le support de Python 3.9 a été abandonné en v0.0.6 (fin de vie le 31/10/2025). Toutes les versions sont testées en intégration continue avec 718 tests à 100 % de couverture de branches.

### Quelles sont les dépendances ?

La bibliothèque principale a 5 dépendances directes :

- `lxml` -- Analyse XML avec durcissement de sécurité
- `pandas` -- DataFrames et manipulation de données
- `openpyxl` -- Export Excel
- `pydantic` -- Validation de données et modèles
- `defusedxml` -- Protection XXE

Les extras optionnels ajoutent : `litellm`, `pypdf`, `pdfplumber`, `pypdfium2`, `fastapi`, `uvicorn`, `polars`.

Toutes les dépendances ont des versions verrouillées par hash SHA-256. Le SBOM CycloneDX cartographie chaque composant d'exécution.

### Fonctionne-t-il sur macOS, Linux et Windows ?

**Oui.** La bibliothèque fonctionne sur macOS, Linux et Windows (via WSL). Elle n'a aucune dépendance spécifique à une plateforme.

### Existe-t-il une API REST ?

**Oui** (v0.0.8+). Installez avec `pip install 'bankstatementparser[api]'` et lancez :

```bash
bankstatementparser-api --port 8000
```

Endpoints : `POST /ingest` (analyser un relevé) et `GET /health` (vérification de l'état).

## Reproductibilité et sécurité

### Comment vérifier la reproductibilité ?

```bash
python -m pytest                              # 718 tests, 100% branch coverage
python scripts/verify_locked_hashes.py        # SHA-256 hash verification
git log --show-signature -1                   # Verify commit signature
```

### Quelles protections de sécurité sont intégrées ?

- **Protection XXE** : `resolve_entities=False`, `no_network=True`, `load_dtd=False`
- **Protection contre les ZIP bombs** : limites de taux de compression, plafonds de taille d'entrée, rejet des entrées chiffrées
- **Prévention de la traversée de chemin** : liste de blocage de motifs dangereux et résolution des liens symboliques
- **Validation des entrées** : limites de taille de fichier (100 Mo par défaut), validation d'extension/format
- **Chaîne d'approvisionnement** : dépendances verrouillées par hash SHA-256, SBOM CycloneDX, attestation de provenance de build
- **Commits signés** : imposés en intégration continue
- **LLM locaux** : le pipeline PDF hybride utilise Ollama — aucun appel API cloud

### Comment Bank Statement Parser se compare-t-il à pyiso20022 ?

pyiso20022 est une boîte à outils ISO 20022 généraliste qui génère des dataclasses Python à partir des schémas XML ISO. Il couvre une large gamme de types de messages ISO 20022 (PACS, PAIN, CAMT, ADMI) avec validation de schéma. Bank Statement Parser est conçu spécifiquement pour l'analyse de relevés bancaires avec support PDF hybride, vérification du solde, enrichissement, export comptable et une API unifiée sur sept formats, y compris des formats non-ISO (CSV, OFX, QFX, MT940, PDF). Si vous devez analyser des relevés bancaires en DataFrames avec une sécurité de niveau production, utilisez Bank Statement Parser. Si vous devez travailler avec le catalogue complet des messages ISO 20022, utilisez pyiso20022.

### Quelles sont les échéances de migration SWIFT ISO 20022 ?

SWIFT a publié un calendrier de migration par phases :

- **Novembre 2026** : les adresses structurées et hybrides deviennent obligatoires. Les messages MT101 multi-instructions seront rejetés. La Phase 1 de gestion des cas commence.
- **Novembre 2027** : toutes les institutions financières doivent pouvoir recevoir nativement les relevés CAMT.053. SWIFT cessera de convertir les MT au format ISO.
- **Novembre 2028** : retrait complet des MT940, MT942, MT950, MT900 et MT910. Ceux-ci seront remplacés par leurs équivalents CAMT.052, CAMT.053 et CAMT.054.

Bank Statement Parser prend en charge à la fois le format ancien MT940 et les formats modernes CAMT.053/PAIN.001, ce qui en fait un choix idéal pour la période de transition.
