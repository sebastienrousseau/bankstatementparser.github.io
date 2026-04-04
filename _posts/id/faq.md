---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Pertanyaan yang Sering Diajukan tentang Parser Laporan Bank"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/corporate-finance.webp"
cdn: "https://cloudcdn.pro"
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Pengurai Laporan Bank. Semua hak dilindungi undang-undang."
date: "Apr 01, 2026"
description: "Jawaban atas pertanyaan umum tentang Parser Laporan Bank: privasi data, redaksi PII, kinerja, dukungan ISO 20022, streaming, kepatuhan, dan alur kerja perbendaharaan."
download: ""
format-detection: "telephone=no"
hreflang: "id"
icon: "https://cloudcdn.pro/bankstatementparser/images/favicon.ico"
id: "https://bankstatementparser.com/id/faq/index.html"
image_alt: "Logo Parser Laporan Bank, alat Python canggih yang dirancang untuk pemrosesan data keuangan dan ekstraksi wawasan yang cepat dan akurat."
image_height: "630"
image_width: "1200"
image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
keywords: "FAQ parser laporan bank, pertanyaan parser CAMT, FAQ PAIN.001, FAQ python ISO 20022, perbankan redaksi PII, kinerja parser bank, privasi data keuangan, FAQ parser MT940, python parser streaming, kepatuhan laporan bank"
language: "id-ID"
layout: "faq"
locale: "id_ID"
logo_alt: "Logo Parser Laporan Bank, alat Python canggih yang dirancang untuk pemrosesan data keuangan dan ekstraksi wawasan yang cepat dan akurat."
logo_height: "44"
logo_width: "44"
logo: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
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
msapplication_tile_image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Jawaban atas pertanyaan umum tentang Parser Laporan Bank: privasi data, redaksi PII, kinerja, dukungan ISO 20022, dan alur kerja perbendaharaan."
twitter_image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
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

**Tidak.** Parser Laporan Bank beroperasi sebagai perpustakaan tanpa negara. Semua pemrosesan -- penguraian, redaksi PII, ekstraksi arsip -- terjadi dalam memori waktu proses lokal Anda. Tidak ada panggilan API, tidak ada layanan cloud, tidak ada telemetri. Parser XML diperkuat dengan`no_network=True`, memblokir semua akses keluar di tingkat parser. Data keuangan Anda tidak pernah meninggalkan lingkungan Anda.

### Bagaimana cara kerja redaksi PII?

Bidang sensitif ditutup sebelum mencapai logika aplikasi Anda. Parser mengidentifikasi nama debitur, nama kreditur, IBAN, dan alamat pos, menggantikannya dengan`***REDACTED***`dalam keluaran konsol dan mode streaming.

- **Redaksi diaktifkan secara default** dalam output CLI dan mode streaming.
- **Ekspor file** (CSV, JSON, Excel) menyimpan data yang belum disunting untuk pemrosesan hilir.
- **Ikut serta** untuk mendapatkan data lengkap dengan`--show-pii`di CLI atau`redact_pii=False`di API.

### Apakah proses ekstraksi bersifat deterministik?

**Ya -- output identik dengan byte pada setiap proses.** Dengan file input yang sama, parser menghasilkan hasil yang sama setiap saat. Tidak ada keacakan, tidak ada inferensi model, tidak ada pengambilan sampel heuristik. CI menerapkan determinisme dengan 467 pengujian pada cakupan cabang 100%, termasuk fuzzing berbasis properti melalui Hipotesis.

### Standar kepatuhan apa yang diikuti proyek ini?

Proyek ini memelihara dokumentasi yang selaras dengan ISO 13485 dengan kemampuan penelusuran penuh:

- **Daftar Risiko** yang terukur dengan penilaian tingkat keparahan/probabilitas dan penilaian risiko sisa.
- **Rencana Verifikasi dan Validasi** dengan 19 langkah tertutup dalam 5 fase.
- **Prosedur Kontrol Perubahan** dengan penilaian dampak dan protokol rollback.
- **Daftar SOUP** yang mencakup semua dependensi dengan tingkat risiko dan pelacakan EOL.
- Masukan desain pemetaan **Matriks Ketertelusuran** untuk implementasi dan verifikasi.

Setiap rilis mencakup CycloneDX SBOM, checksum SHA-256, dan pengesahan asal build GitHub.

## Performa dan Skalabilitas

### Seberapa cepat Pengurai Laporan Bank?

Ambang batas performa divalidasi di CI pada setiap penerapan:

| Metrik | Nilai |
|---|---|
| Keluaran CAMT.053 | 27.000+ transaksi/detik |
| Throughput PAIN.001 | 52.000+ transaksi/detik |
| Latensi per transaksi (CAMT) | 37 mikrodetik |
| Latensi per transaksi (PAIN.001) | 19 mikrodetik |
| Saatnya untuk hasil pertama | < 2 ms |

### Bagaimana cara menangani file besar?

**Streaming dengan memori terbatas -- diuji pada 50.000 transaksi per file.** Penggunaan`parse_streaming()`untuk memproses file XML secara bertahap. Setiap transaksi dihasilkan sebagai kamus; elemen dihapus setelah pemrosesan untuk mencegah pertumbuhan memori. Memori tidak disesuaikan dengan ukuran file -- pengujian transaksi 50K (25+ MB) menggunakan kurang dari 2x memori pengujian transaksi 10K.

Untuk file yang melebihi 50 MB (misalnya, kumpulan PAIN.001 host-ke-host dengan pembayaran 100K+), parser mengalir melalui file sementara dengan pengupasan namespace berbasis potongan -- dokumen lengkap tidak pernah dimuat ke dalam memori.

### Bagaimana arsip ZIP diproses dengan aman?

`iter_secure_xml_entries()`memvalidasi setiap anggota sebelum ekstraksi:

- **Batas ukuran entri** (default 10 MB per entri)
- **Total batas ukuran yang tidak dikompresi** (default 50 MB)
- **Batas rasio kompresi** (default 100:1) untuk mencegah bom ZIP
- **Penolakan entri terenkripsi**

Tidak ada file yang ditulis ke disk. XML byte diteruskan langsung ke parser melalui`from_bytes()`.

### Bisakah saya mengurai banyak file secara paralel?

**Ya.** Gunakan`parse_files_parallel()`yang mendistribusikan pekerjaan di a`ProcessPoolExecutor`:

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

## Format yang Didukung

### Format laporan bank apa yang didukung?

| Format | Standar | Jenis File | Kelas Parser |
|---|---|---|---|
| CAMT.053 | Pernyataan Bank-ke-Pelanggan ISO 20022 | `.xml` | `CamtParser` |
| SAKIT.001 | Inisiasi Transfer Kredit ISO 20022 | `.xml` | `Pain001Parser` |
| CSV | Ekspor bank umum | `.csv` | `CsvStatementParser` |
| OFX | Buka Pertukaran Keuangan | `.ofx` | `OfxParser` |
| QFX | Mempercepat Pertukaran Keuangan | `.qfx` | `QfxParser` |
| MT940 | standar SWIFT | `.mt940`, `.sta` | `Mt940Parser` |

### Apakah parser menangani dialek khusus bank CAMT.053?

**Ya -- namespace-agnostic berdasarkan desain.** Parser menghapus namespace XML sebelum diproses, menangani varian CAMT.053 (`camt.053.001.02`, `camt.053.001.04`, atau pembungkus bank berpemilik) tanpa konfigurasi khusus namespace. XPath menanyakan struktur elemen target, bukan URI namespace.

Untuk bank yang membungkus CAMT dalam amplop khusus, gunakan`from_string()`atau`from_bytes()`untuk memasukkan dokumen bagian dalam secara langsung.

### Bisakah saya memetakan header kolom CSV khusus ke skema standar?

**Ya -- normalisasi otomatis, konfigurasi nol.**`CsvStatementParser`mengenali variasi header yang umum:`"Date"`, `"Transaction Date"`, `"Booking Date"`semua peta ke`date`bidang.`"Amount"`, `"Value"`, `"Sum"`peta ke`amount`. Pisahkan kolom kredit/debit (mis.,`"Credit"`Dan`"Debit"`) terdeteksi dan digabungkan menjadi satu jumlah yang ditandatangani secara otomatis.

### Apa format keluarannya?

Semua parser menghasilkan DataFrame panda standar dengan tipe kolom yang konsisten:

| Format | Kolom Kunci |
|---|---|
| **CAMT** | `Amount`, `Currency`, `DrCr`, `Debtor`, `Creditor`, `Reference`, `ValDt`, `BookgDt`, `AccountId` |
| **RASA SAKIT.001** | `PmtInfId`, `PmtMtd`, `InstdAmt`, `Currency`, `CdtrNm`, `EndToEndId`, `MsgId`, `CreDtTm`, `NbOfTxs` |
| **CSV/OFX/QFX/MT940** | `date`, `description`, `amount`(dinormalisasi) |

Anda juga dapat mengekspor ke CSV, JSON, Excel, atau mengonversi ke Polars DataFrames.

## Alur Kerja Perbendaharaan

### Bagaimana cara parser menangani pernyataan multi-mata uang?

**Setiap transaksi mempertahankan mata uang aslinya -- tidak ada konversi implisit.** The`Currency`bidang diekstraksi dari XML`Ccy`atribut per transaksi. Laporan multi-mata uang tetap apa adanya. Itu`get_account_balances()`metode mengembalikan saldo pembukaan dan penutupan per akun dengan kode mata uang asli. Rekonsiliasi lintas mata uang diserahkan pada logika hilir Anda, di mana Anda mengontrol sumber nilai tukar.

### Apakah parser mendukung format keluar dan masuk?

**Ya.**`Pain001Parser`menangani file inisiasi transfer kredit ISO 20022 PAIN.001 (pembayaran keluar).`CamtParser`menangani file laporan bank-ke-pelanggan CAMT.053 (pelaporan masuk). Keduanya mendukung streaming, redaksi PII, dan ekspor ke CSV, JSON, dan Excel. Menggunakan`detect_statement_format()`untuk mengidentifikasi format secara otomatis.

### Apa yang terjadi bila entri transaksi salah format?

Perilaku bergantung pada mode penguraian:

- **`parse()`(mode batch)** -- Entri yang salah formatnya tidak berisi kolom yang wajib diisi (`Amount`, `Currency`, atau`CdtDbtInd`) dilewati dengan log peringatan. Pernyataan lainnya diurai secara normal.
- **`parse_streaming()`(mode streaming)** -- Kesalahan penguraian langsung menyebar sebagai pengecualian. Tidak ada kehilangan data secara diam-diam. Perilaku gagal-cepat ini disengaja untuk alur kerja keuangan di mana setiap transaksi harus dipertanggungjawabkan.

### Bagaimana cara kerja deduplikasi?

Itu`Deduplicator`kelas mendeteksi duplikat persis dan dugaan kecocokan dengan skor keyakinan yang dapat dijelaskan:

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

### Bagaimana cara menginstal Pengurai Laporan Bank?

```bash
pip install bankstatementparser
```

Untuk dukungan opsional Polars DataFrame:

```bash
pip install bankstatementparser[polars]
```

### Versi Python manakah yang didukung?

Python 3.9 hingga 3.14. Semua versi diuji di CI dengan 467 pengujian pada cakupan cabang 100%.

### Apa saja dependensinya?

Perpustakaan memiliki 5 dependensi langsung:

- `lxml`-- Penguraian XML dengan penguatan keamanan
-`pandas`-- DataFrames dan manipulasi data
-`openpyxl`- Ekspor Excel
-`pydantic`-- Validasi data dan model
-`defusedxml`-- Perlindungan XXE

Semua dependensi memiliki versi hash-lock SHA-256. CycloneDX SBOM memetakan setiap komponen runtime.

### Apakah ini berfungsi di MacOS, Linux, dan Windows?

**Ya.** Pustaka berfungsi di macOS, Linux, dan Windows (melalui WSL). Itu tidak memiliki ketergantungan khusus platform.

## Reproduksibilitas dan Keamanan

### Bagaimana cara memverifikasi reproduktifitas?

```bash
python -m pytest                              # 467 tests, 100% branch coverage
python scripts/verify_locked_hashes.py        # SHA-256 hash verification
git log --show-signature -1                   # Verify commit signature
```

### Perlindungan keamanan apa yang ada di dalamnya?

- **Perlindungan XXE**:`resolve_entities=False`, `no_network=True`, `load_dtd=False`
- **Perlindungan Bom ZIP**: Batas rasio kompresi, batas ukuran entri, penolakan entri terenkripsi
- **Pencegahan Traversal Jalur**: Daftar blokir pola berbahaya dan resolusi symlink
- **Validasi Input**: Batas ukuran file (default 100 MB), validasi ekstensi/format
- **Rantai Pasokan**: Dependensi yang dikunci hash SHA-256, CycloneDX SBOM, pengesahan asal pembuatan
- **Komitmen yang Ditandatangani**: Diberlakukan di CI

### Bagaimana Parser Laporan Bank dibandingkan dengan pyiso20022?

pyiso20022 adalah toolkit ISO 20022 luas yang menghasilkan kelas data Python dari skema ISO XML. Ini mencakup berbagai jenis pesan ISO 20022 (PACS, PAIN, CAMT, ADMI) dengan validasi skema. Parser Laporan Bank dibuat khusus untuk penguraian laporan bank dengan dukungan streaming, redaksi PII, deduplikasi, dan API terpadu dalam enam format termasuk format non-ISO (CSV, OFX, QFX, MT940). Jika Anda perlu mengurai laporan bank ke dalam DataFrames dengan keamanan tingkat produksi, gunakan Pengurai Laporan Bank. Jika Anda perlu bekerja dengan katalog pesan ISO 20022 lengkap, gunakan pyiso20022.

### Kapan batas waktu migrasi SWIFT ISO 20022?

SWIFT telah menerbitkan garis waktu migrasi bertahap:

- **November 2026**: Alamat terstruktur dan hibrid menjadi wajib. Pesan multi-instruksi MT101 akan ditolak. Manajemen Kasus Fase 1 dimulai.
- **November 2027**: Semua lembaga keuangan harus dapat menerima laporan CAMT.053 secara asli. SWIFT akan berhenti mengonversi MT ke format ISO.
- **November 2028**: Pensiun penuh MT940, MT942, MT950, MT900, dan MT910. Ini akan digantikan oleh yang setara dengan CAMT.052, CAMT.053, dan CAMT.054.

Parser Laporan Bank mendukung format MT940 lama dan format CAMT.053/PAIN.001 modern, sehingga ideal untuk masa transisi.

