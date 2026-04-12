---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Pertanyaan yang Sering Diajukan tentang Parser Laporan Bank"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Pengurai Laporan Bank. Semua hak dilindungi undang-undang."
date: "Apr 11, 2026"
description: "Jawaban atas pertanyaan umum tentang Parser Laporan Bank: privasi data, redaksi PII, kinerja, dukungan ISO 20022, streaming, kepatuhan, dan alur kerja perbendaharaan."
download: ""
format-detection: "telephone=no"
hreflang: "id"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/id/faq/index.html"
image_alt: "Logo Parser Laporan Bank, alat Python canggih yang dirancang untuk pemrosesan data keuangan dan ekstraksi wawasan yang cepat dan akurat."
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "FAQ parser laporan bank, pertanyaan parser CAMT, FAQ PAIN.001, FAQ python ISO 20022, perbankan redaksi PII, kinerja parser bank, privasi data keuangan, FAQ parser MT940, python parser streaming, kepatuhan laporan bank"
language: "id-ID"
layout: "faq"
locale: "id_ID"
logo_alt: "Logo Parser Laporan Bank, alat Python canggih yang dirancang untuk pemrosesan data keuangan dan ekstraksi wawasan yang cepat dan akurat."
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Pertanyaan Umum"
permalink: "https://bankstatementparser.com/id/faq/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Pertanyaan Umum Tentang Parser Laporan Bank"
tags: "faq,bank,pernyataan,parser,privasi,kepatuhan,kinerja,streaming,iso20022,python"
theme_color: "rgb(73, 214, 251)"
title: "FAQ Parser Laporan Bank: Privasi, Kinerja, dan Penggunaan"
url: "https://bankstatementparser.com/id/faq/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/id/faq/rss.xml"
category: "Perangkat Lunak Keuangan, Perpustakaan Python, FAQ"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Jawaban atas pertanyaan umum tentang Parser Laporan Bank: privasi data, redaksi PII, kinerja, dukungan ISO 20022, streaming, kepatuhan, dan alur kerja perbendaharaan."
item_guid: "https://bankstatementparser.com/id/faq/rss.xml"
item_link: "https://bankstatementparser.com/id/faq/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "FAQ Parser Laporan Bank: Privasi, Kinerja, dan Penggunaan"
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
apple-mobile-web-app-title: "FAQ Parser Laporan Bank: Privasi, Kinerja, dan Penggunaan"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Jawaban atas pertanyaan umum tentang Parser Laporan Bank: privasi data, redaksi PII, kinerja, dukungan ISO 20022, dan alur kerja perbendaharaan."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logo Parser Laporan Bank, alat Python canggih yang dirancang untuk pemrosesan data keuangan dan ekstraksi wawasan yang cepat dan akurat."
twitter_site: "@wwdseb"
twitter_title: "FAQ Parser Laporan Bank: Privasi, Kinerja, dan Penggunaan"
twitter_url: "https://bankstatementparser.com/id/faq/index.html"

# Humans.txt - The Humans.txt front matter (YAML).

author_website: "https://bankstatementparser.com"
author_twitter: "@wwdseb"
author_location: "London, UK"
thanks: "Terima kasih telah membaca!"
site_last_updated: "2026-04-01"
site_standards: "HTML5, CSS3, RSS, Atom, JSON, XML, YAML, Markdown, TOML"
site_components: "Shokunin SSG, Shokunin CLI, Shokunin Templates, Kaishi Templates, Kaishi Themes"
site_software: "Shokunin, Rust"

---

## Privasi dan Kepatuhan Data

### Apakah ada data yang keluar dari infrastruktur saya?

**Tidak — bahkan untuk ekstraksi PDF.** Bank Statement Parser beroperasi sebagai pustaka stateless. Semua pemrosesan -- penguraian, redaksi PII, ekstraksi arsip -- terjadi dalam memori runtime lokal Anda. Pipeline PDF hibrida menggunakan Ollama untuk inferensi LLM lokal — tanpa API cloud. Parser XML diperkuat dengan `no_network=True`, memblokir semua akses keluar di tingkat parser. Data keuangan Anda tidak pernah keluar dari lingkungan Anda.

### Bagaimana cara kerja redaksi PII?

Bidang sensitif disamarkan sebelum mencapai logika aplikasi Anda. Parser mengidentifikasi nama debitur, nama kreditur, IBAN, dan alamat pos, menggantikannya dengan `***REDACTED***` dalam output konsol dan mode streaming.

- **Redaksi aktif secara default** dalam output CLI dan mode streaming.
- **Ekspor file** (CSV, JSON, Excel) menyimpan data tanpa redaksi untuk pemrosesan hilir.
- **Aktifkan** data lengkap dengan `--show-pii` di CLI atau `redact_pii=False` di API.

### Apakah proses ekstraksi bersifat deterministik?

**Ya untuk format terstruktur -- output identik byte pada setiap proses.** Dengan file input yang sama, parser deterministik (CAMT, PAIN.001, CSV, OFX, QFX, MT940) menghasilkan hasil yang sama setiap saat. Tidak ada keacakan, tidak ada inferensi model, tidak ada sampling heuristik.

Untuk pipeline PDF hibrida, jalur ekstraksi berbasis LLM mungkin menghasilkan variasi kecil antar proses. Oleh karena itu setiap ekstraksi PDF diverifikasi dengan **Golden Rule** (`opening + credits − debits == closing`) dan ketidaksesuaian yang ditandai dapat ditinjau secara interaktif.

CI menerapkan determinisme dengan 718 pengujian pada cakupan cabang 100%, termasuk fuzzing berbasis properti via Hypothesis.

### Standar kepatuhan apa yang diikuti proyek ini?

Proyek ini memelihara dokumentasi selaras ISO 13485 dengan kemampuan penelusuran penuh:

- **Daftar Risiko** terukur dengan penilaian tingkat keparahan/probabilitas dan penilaian risiko sisa.
- **Rencana Verifikasi dan Validasi** dengan 19 langkah terjaga dalam 5 fase.
- **Prosedur Kontrol Perubahan** dengan penilaian dampak dan protokol rollback.
- **Daftar SOUP** yang mencakup semua dependensi dengan tingkat risiko dan pelacakan EOL.
- **Matriks Ketertelusuran** yang memetakan masukan desain ke implementasi dan verifikasi.

Setiap rilis mencakup CycloneDX SBOM, checksum SHA-256, dan pengesahan provenance build GitHub.

## Performa dan Skalabilitas

### Seberapa cepat Bank Statement Parser?

Ambang batas performa divalidasi di CI pada setiap commit:

| Metrik | Nilai |
|---|---|
| Throughput CAMT.053 | 27.000+ transaksi/detik |
| Throughput PAIN.001 | 52.000+ transaksi/detik |
| Latensi per transaksi (CAMT) | 37 mikrodetik |
| Latensi per transaksi (PAIN.001) | 19 mikrodetik |
| Waktu ke hasil pertama | < 2 ms |

Kecepatan ekstraksi PDF bergantung pada jalur routing: deterministik (sub-detik), text-LLM (beberapa detik), vision-LLM (beberapa detik per halaman).

### Bagaimana cara menangani file besar?

**Streaming dengan memori terbatas -- diuji pada 50.000 transaksi per file.** Gunakan `parse_streaming()` untuk memproses file XML secara bertahap. Setiap transaksi dihasilkan sebagai dictionary; elemen dihapus setelah pemrosesan untuk mencegah pertumbuhan memori. Memori tidak bertambah seiring ukuran file -- pengujian 50K transaksi (25+ MB) menggunakan kurang dari 2x memori pengujian 10K transaksi.

Untuk file melebihi 50 MB (misalnya, batch PAIN.001 host-to-host dengan 100K+ pembayaran), parser mengalir melalui file sementara dengan stripping namespace berbasis chunk -- dokumen lengkap tidak pernah dimuat ke memori.

### Bagaimana arsip ZIP diproses dengan aman?

`iter_secure_xml_entries()` memvalidasi setiap anggota sebelum ekstraksi:

- **Batas ukuran entri** (default 10 MB per entri)
- **Total batas ukuran tidak terkompresi** (default 50 MB)
- **Batas rasio kompresi** (default 100:1) untuk mencegah bom ZIP
- **Penolakan entri terenkripsi**

Tidak ada file yang ditulis ke disk. Byte XML diteruskan langsung ke parser via `from_bytes()`.

### Bisakah saya mengurai banyak file secara paralel?

**Ya.** Gunakan `parse_files_parallel()` yang mendistribusikan pekerjaan di `ProcessPoolExecutor`:

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

Untuk ingesti PDF massal, gunakan `scan_and_ingest()` yang memproses seluruh pohon folder dengan deduplikasi otomatis.

## Format yang Didukung

### Format laporan bank apa yang didukung?

| Format | Standar | Jenis File | Parser/Metode |
|---|---|---|---|
| CAMT.053 | ISO 20022 Bank-to-Customer Statement | `.xml` | `CamtParser` |
| PAIN.001 | ISO 20022 Credit Transfer Initiation | `.xml` | `Pain001Parser` |
| CSV | Ekspor bank umum | `.csv` | `CsvStatementParser` |
| OFX | Open Financial Exchange | `.ofx` | `OfxParser` |
| QFX | Quicken Financial Exchange | `.qfx` | `QfxParser` |
| MT940 | Standar SWIFT | `.mt940`, `.sta` | `Mt940Parser` |
| PDF | Laporan digital dan hasil pindai | `.pdf` | `smart_ingest()` |

### Bagaimana cara kerja pipeline PDF hibrida?

Pipeline hibrida (v0.0.5+) secara cerdas merutekan PDF melalui tiga jalur ekstraksi:

- **Jalur A (Deterministik)**: Tabel PDF terstruktur diurai langsung — gratis, tercepat, tanpa LLM.
- **Jalur B (Text-LLM)**: PDF digital dengan tata letak kompleks diekstrak via LLM lokal (LiteLLM/Ollama).
- **Jalur C (Vision-LLM)**: Laporan hasil pindai atau fotokopi diproses dengan model vision multimodal.

Setiap ekstraksi diverifikasi dengan Golden Rule (`opening + credits − debits == closing`). Ketidaksesuaian dapat ditinjau secara interaktif dengan `--type review`.

### Apakah parser menangani dialek khusus bank CAMT.053?

**Ya -- namespace-agnostic secara desain.** Parser menghapus namespace XML sebelum diproses, menangani varian CAMT.053 apa pun (`camt.053.001.02`, `camt.053.001.04`, atau pembungkus bank proprietary) tanpa konfigurasi khusus namespace. Query XPath menargetkan struktur elemen, bukan URI namespace.

Untuk bank yang membungkus CAMT dalam amplop khusus, gunakan `from_string()` atau `from_bytes()` untuk memasukkan dokumen bagian dalam secara langsung.

### Bisakah saya memetakan header kolom CSV khusus ke skema standar?

**Ya -- normalisasi otomatis, tanpa konfigurasi.** `CsvStatementParser` mengenali variasi header umum: `"Date"`, `"Transaction Date"`, `"Booking Date"` semua dipetakan ke field `date`. `"Amount"`, `"Value"`, `"Sum"` dipetakan ke `amount`. Kolom kredit/debit terpisah (misalnya `"Credit"` dan `"Debit"`) terdeteksi dan digabungkan menjadi satu jumlah bertanda secara otomatis.

### Apa format outputnya?

Semua parser menghasilkan pandas DataFrames standar dengan tipe kolom konsisten:

| Format | Kolom Utama |
|---|---|
| **CAMT** | `Amount`, `Currency`, `DrCr`, `Debtor`, `Creditor`, `Reference`, `ValDt`, `BookgDt`, `AccountId` |
| **PAIN.001** | `PmtInfId`, `PmtMtd`, `InstdAmt`, `Currency`, `CdtrNm`, `EndToEndId`, `MsgId`, `CreDtTm`, `NbOfTxs` |
| **CSV/OFX/QFX/MT940** | `date`, `description`, `amount` (dinormalisasi) |

Anda juga dapat mengekspor ke CSV, JSON, Excel, Polars DataFrames, hledger, atau format jurnal beancount.

## Fitur PDF dan LLM

### Model LLM apa yang didukung pipeline hibrida?

Pipeline menggunakan LiteLLM sebagai lapisan abstraksi model, dengan bridge Ollama langsung untuk prompt vision. Model yang direkomendasikan:

- **Ekstraksi teks**: Model apa pun yang kompatibel LiteLLM (lokal atau remote).
- **Ekstraksi vision**: `ollama/minicpm-v` (direkomendasikan) untuk PDF hasil pindai.
- **Kategorisasi**: Model apa pun yang kompatibel LiteLLM.

Semua model dapat berjalan 100% lokal via Ollama — tanpa API key.

### Apa itu verifikasi Golden Rule?

Setiap ekstraksi PDF diverifikasi dengan persamaan: `opening balance + credits − debits == closing balance`. Hasilnya ditandai sebagai:

- **VERIFIED**: Saldo cocok persis.
- **DISCREPANCY**: Saldo tidak cocok — tinjauan disarankan.
- **FAILED**: Verifikasi tidak dapat dilakukan (data saldo tidak lengkap).

### Bisakah saya mengkategorikan transaksi secara otomatis?

**Ya.** Modul enrichment (v0.0.6+) menyediakan kategorisasi transaksi berbasis LLM:

```python
from bankstatementparser.enrichment import Categorizer

categorizer = Categorizer()
enriched = categorizer.categorize_batch(transactions)
```

Skema default menggunakan 13 kategori kompatibel Plaid. Anda dapat menyediakan skema kategori Anda sendiri.

### Bisakah saya mengekspor ke hledger atau beancount?

**Ya** (v0.0.8+). Ekspor transaksi ke format jurnal plaintext-accounting dengan pemetaan akun:

```python
from bankstatementparser.export import to_hledger, to_beancount

journal = to_hledger(transactions, account="Assets:Bank:Checking")
```

## Alur Kerja Perbendaharaan

### Bagaimana parser menangani laporan multi-mata uang?

**Setiap transaksi mempertahankan mata uang aslinya -- tanpa konversi implisit.** Field `Currency` diekstraksi dari atribut XML `Ccy` per transaksi. Laporan multi-mata uang tetap apa adanya. Metode `get_account_balances()` mengembalikan saldo pembukaan dan penutupan per akun dengan kode mata uang asli.

Sejak v0.0.8, `verify_balance_multi_currency()` mengelompokkan transaksi per mata uang dan menjalankan Golden Rule secara independen per kelompok — berguna untuk akun yang menyimpan beberapa mata uang.

### Apakah parser mendukung format keluar dan masuk?

**Ya.** `Pain001Parser` menangani file inisiasi transfer kredit ISO 20022 PAIN.001 (pembayaran keluar). `CamtParser` menangani file laporan bank-ke-pelanggan CAMT.053 (pelaporan masuk). Keduanya mendukung streaming, redaksi PII, dan ekspor ke CSV, JSON, Excel, hledger, dan beancount. Gunakan `detect_statement_format()` untuk mengidentifikasi format secara otomatis.

### Apa yang terjadi bila entri transaksi salah format?

Perilaku bergantung pada mode penguraian:

- **`parse()` (mode batch)** -- Entri yang salah format tanpa field wajib (`Amount`, `Currency`, atau `CdtDbtInd`) dilewati dengan log peringatan. Sisa laporan diurai secara normal.
- **`parse_streaming()` (mode streaming)** -- Kesalahan penguraian langsung menyebar sebagai exception. Tidak ada kehilangan data diam-diam. Perilaku fail-fast ini disengaja untuk alur kerja keuangan di mana setiap transaksi harus dipertanggungjawabkan.
- **`smart_ingest()` (PDF hibrida)** -- Kesalahan ekstraksi ditangkap dalam `IngestResult` dengan status verifikasi, memungkinkan tinjauan interaktif.

### Bagaimana cara kerja deduplikasi?

Setiap transaksi diberi `transaction_hash` idempoten (fingerprint MD5) berdasarkan field kuncinya. Ini memungkinkan ingesti inkremental yang aman — memproses ulang file yang sama menghasilkan hash yang sama, sehingga duplikat terdeteksi otomatis.

```python
from bankstatementparser import CamtParser, Deduplicator

parser = CamtParser("statement.xml")
dedup = Deduplicator()
result = dedup.deduplicate(dedup.from_dataframe(parser.parse()))

print(f"Unique: {len(result.unique_transactions)}")
print(f"Exact duplicates: {len(result.exact_duplicates)}")
print(f"Suspected matches: {len(result.suspected_matches)}")
```

## Instalasi dan Kompatibilitas

### Bagaimana cara menginstal Bank Statement Parser?

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

### Versi Python mana yang didukung?

Python 3.10 hingga 3.14. Dukungan Python 3.9 dihentikan di v0.0.6 (EOL 2025-10-31). Semua versi diuji di CI dengan 718 pengujian pada cakupan cabang 100%.

### Apa saja dependensinya?

Pustaka inti memiliki 5 dependensi langsung:

- `lxml` -- Penguraian XML dengan penguatan keamanan
- `pandas` -- DataFrames dan manipulasi data
- `openpyxl` -- Ekspor Excel
- `pydantic` -- Validasi data dan model
- `defusedxml` -- Perlindungan XXE

Ekstra opsional menambahkan: `litellm`, `pypdf`, `pdfplumber`, `pypdfium2`, `fastapi`, `uvicorn`, `polars`.

Semua dependensi memiliki versi hash-lock SHA-256. CycloneDX SBOM memetakan setiap komponen runtime.

### Apakah ini berfungsi di macOS, Linux, dan Windows?

**Ya.** Pustaka berfungsi di macOS, Linux, dan Windows (via WSL). Tidak memiliki dependensi khusus platform.

### Apakah ada REST API?

**Ya** (v0.0.8+). Instal dengan `pip install 'bankstatementparser[api]'` dan jalankan:

```bash
bankstatementparser-api --port 8000
```

Endpoint: `POST /ingest` (parsing laporan) dan `GET /health` (pemeriksaan kesehatan).

## Reproduksibilitas dan Keamanan

### Bagaimana cara memverifikasi reproduktifitas?

```bash
python -m pytest                              # 718 tests, 100% branch coverage
python scripts/verify_locked_hashes.py        # SHA-256 hash verification
git log --show-signature -1                   # Verify commit signature
```

### Perlindungan keamanan apa yang tersedia?

- **Perlindungan XXE**: `resolve_entities=False`, `no_network=True`, `load_dtd=False`
- **Perlindungan Bom ZIP**: Batas rasio kompresi, batas ukuran entri, penolakan entri terenkripsi
- **Pencegahan Path Traversal**: Daftar blokir pola berbahaya dan resolusi symlink
- **Validasi Input**: Batas ukuran file (default 100 MB), validasi ekstensi/format
- **Rantai Pasokan**: Dependensi dikunci hash SHA-256, CycloneDX SBOM, pengesahan provenance build
- **Commit Bertanda Tangan**: Diberlakukan di CI
- **LLM Lokal**: Pipeline PDF hibrida menggunakan Ollama — tanpa panggilan API cloud

### Bagaimana Bank Statement Parser dibandingkan dengan pyiso20022?

pyiso20022 adalah toolkit ISO 20022 luas yang menghasilkan dataclass Python dari skema ISO XML. Ini mencakup berbagai jenis pesan ISO 20022 (PACS, PAIN, CAMT, ADMI) dengan validasi skema. Bank Statement Parser dibuat khusus untuk penguraian laporan bank dengan dukungan PDF hibrida, verifikasi saldo, pengayaan, ekspor ledger, dan API terpadu di tujuh format termasuk format non-ISO (CSV, OFX, QFX, MT940, PDF). Jika Anda perlu mengurai laporan bank ke dalam DataFrames dengan keamanan tingkat produksi, gunakan Bank Statement Parser. Jika Anda perlu bekerja dengan katalog pesan ISO 20022 lengkap, gunakan pyiso20022.

### Kapan tenggat waktu migrasi SWIFT ISO 20022?

SWIFT telah menerbitkan garis waktu migrasi bertahap:

- **November 2026**: Alamat terstruktur dan hibrida menjadi wajib. Pesan multi-instruksi MT101 akan ditolak. Manajemen Kasus Fase 1 dimulai.
- **November 2027**: Semua lembaga keuangan harus dapat menerima laporan CAMT.053 secara native. SWIFT akan berhenti mengonversi MT ke format ISO.
- **November 2028**: Pensiun penuh MT940, MT942, MT950, MT900, dan MT910. Ini akan digantikan oleh padanan CAMT.052, CAMT.053, dan CAMT.054.

Bank Statement Parser mendukung format MT940 lama dan format CAMT.053/PAIN.001 modern, sehingga ideal untuk masa transisi.

