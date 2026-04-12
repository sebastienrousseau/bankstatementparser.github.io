---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Panduan Migrasi ISO 20022"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Pengurai Laporan Bank. Semua hak dilindungi undang-undang."
date: "Apr 11, 2026"
description: "Panduan praktis mengenai garis waktu migrasi SWIFT ISO 20022 (2026-2028), transisi MT940 ke CAMT.053, dan bagaimana Bank Statement Parser membantu tim treasury melakukan migrasi."
download: ""
format-detection: "telephone=no"
hreflang: "id"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/id/migration/index.html"
image_alt: "Logo Pengurai Laporan Bank, Berdayakan Analisis Keuangan Anda dengan Ekstraksi Data yang Mulus"
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "Migrasi ISO 20022, MT940 ke CAMT.053, batas waktu SWIFT 2027, penghentian MT940 2028, python migrasi laporan bank, parser CAMT.053, garis waktu ISO 20022"
language: "id-ID"
layout: "about"
locale: "id_ID"
logo_alt: "Logo Pengurai Laporan Bank, Berdayakan Analisis Keuangan Anda dengan Ekstraksi Data yang Mulus"
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Panduan Migrasi ISO 20022"
permalink: "https://bankstatementparser.com/id/migration/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Navigasikan SWIFT MT ke Transisi ISO 20022"
tags: "iso20022,migrasi,mt940,camt053,cepat,garis waktu"
theme_color: "rgb(73, 214, 251)"
title: "Panduan Migrasi ISO 20022: Transisi MT940 ke CAMT.053"
url: "https://bankstatementparser.com/id/migration/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/id/migration/rss.xml"
category: "Perangkat Lunak Keuangan, Perpustakaan Python, Pemrosesan Data"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Panduan praktis mengenai garis waktu migrasi SWIFT ISO 20022 (2026-2028), transisi MT940 ke CAMT.053, dan bagaimana Bank Statement Parser membantu tim treasury melakukan migrasi."
item_guid: "https://bankstatementparser.com/id/migration/rss.xml"
item_link: "https://bankstatementparser.com/id/migration/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Panduan Migrasi ISO 20022: Transisi MT940 ke CAMT.053"
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
apple-mobile-web-app-title: "Panduan Migrasi ISO 20022: Transisi MT940 ke CAMT.053"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Panduan praktis mengenai garis waktu migrasi SWIFT ISO 20022 (2026-2028), transisi MT940 ke CAMT.053, dan bagaimana Bank Statement Parser membantu tim treasury melakukan migrasi."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logo Pengurai Laporan Bank, Berdayakan Analisis Keuangan Anda dengan Ekstraksi Data yang Mulus"
twitter_site: "@wwdseb"
twitter_title: "Panduan Migrasi ISO 20022: Transisi MT940 ke CAMT.053"
twitter_url: "https://bankstatementparser.com/id/migration/index.html"

# Humans.txt - The Humans.txt front matter (YAML).

author_website: "https://bankstatementparser.com"
author_twitter: "@wwdseb"
author_location: "London, UK"
thanks: "Terima kasih telah membaca!"
site_last_updated: "2026-04-01"
site_standards: "HTML5, CSS3, RSS, Atom, JSON, XML, YAML, Markdown, TOML"
site_components: "Shokunin SSG, Shokunin CLI, Shokunin Templates, Shokunin Themes, Kaishi SSG, Kaishi CLI, Kaishi Templates, Kaishi Themes"
site_software: "Shokunin, Rust"

---

**TL;DR:** SWIFT akan menghentikan MT940 pada November 2028. Bank Statement Parser menangani MT940 dan CAMT.053 dengan satu API, sehingga pipeline parsing Anda berfungsi selama transisi dan setelahnya.

## Mengapa Migrasi Ini Penting

SWIFT menghentikan format pesan MT lama demi standar ISO 20022 yang lebih kaya. Untuk tim perbendaharaan dan keuangan, ini berarti pipeline pemrosesan laporan bank Anda harus berevolusi dari MT940 ke CAMT.053 sebelum tenggat waktu final.

## Garis Waktu Migrasi SWIFT

| Tanggal | Tonggak Pencapaian | Dampak |
|---|---|---|
| **November 2025** | Koeksistensi MT-ke-MX berakhir untuk pembayaran lintas batas | Pesan PACS sekarang hanya ISO 20022 |
| **November 2026** | Alamat terstruktur/hibrida wajib; multi-instruksi MT101 ditolak; Manajemen Kasus Fase 1 | Format alamat harus patuh; beberapa pesan MT akan ditolak |
| **Akhir 2026** | Opt-in dimulai untuk menerima CAMT.052/.053/.054 | Lembaga keuangan dapat mulai menerima laporan ISO native |
| **November 2027** | Semua FI harus menerima CAMT.053 secara native | SWIFT berhenti mengonversi format MT ke ISO; sistem Anda harus mengurai CAMT langsung |
| **November 2028** | MT940/MT942/MT950/MT900/MT910 pensiun sepenuhnya | Format laporan lama tidak lagi tersedia; CAMT.052/.053/.054 satu-satunya pilihan |

## Apa yang Berubah pada Kode Anda

### Sebelumnya: Hanya MT940

```python
from bankstatementparser import Mt940Parser

parser = Mt940Parser("statement.mt940")
df = parser.parse()
```

### Setelah: Kedua Format dengan Deteksi Otomatis

```python
from bankstatementparser import create_parser, detect_statement_format

fmt = detect_statement_format("statement.xml")  # or .mt940
parser = create_parser("statement.xml", fmt)
df = parser.parse()  # Same DataFrame schema regardless of format
```

Fungsi `detect_statement_format()` mengidentifikasi apakah file tersebut MT940, CAMT.053, PAIN.001, atau format lain yang didukung. Fungsi `create_parser()` mengembalikan parser yang tepat. Kode hilir Anda berfungsi identik tanpa memandang format sumber.

## CAMT.053 vs MT940: Perbedaan Utama

| Fitur | MT940 | CAMT.053 |
|---|---|---|
| Kekayaan data | Field terbatas | 3-5x lebih banyak data per transaksi |
| Set karakter | Terbatas (charset SWIFT) | Unicode penuh |
| Struktur | Teks datar dengan tag | XML dengan namespace |
| Pelaporan saldo | Pembukaan/penutupan saja | Berbagai jenis saldo |
| Referensi | Satu field referensi | Berbagai jenis referensi |
| Penanganan mata uang | Dasar | Multi-mata uang penuh dengan nilai tukar |

## Bagaimana Bank Statement Parser Membantu

- **API Terpadu**: Parsing MT940, CAMT.053, dan laporan PDF dengan alur kerja yang sama, menghasilkan output DataFrame konsisten.
- **Deteksi otomatis**: Tidak perlu mengetahui format terlebih dahulu. `detect_statement_format()` mengidentifikasinya secara otomatis.
- **Pipeline PDF hibrida**: Bank yang hanya menyediakan laporan PDF selama transisi ditangani oleh `smart_ingest()` dengan verifikasi saldo otomatis.
- **Namespace-agnostic**: Menangani varian CAMT.053 apa pun (001.02, 001.04, atau wrapper khusus bank) tanpa konfigurasi.
- **Verifikasi multi-mata uang**: `verify_balance_multi_currency()` menjalankan Golden Rule per kelompok mata uang — penting untuk laporan CAMT multi-mata uang.
- **Streaming**: Proses file CAMT besar (50 MB+, 50K+ transaksi) dengan memori terbatas.
- **Ekspor ledger**: Ekspor langsung ke format jurnal hledger atau beancount untuk akuntansi treasury.
- **Pengujian migrasi**: Jalankan kedua parser berdampingan pada rentang tanggal yang sama untuk memverifikasi konsistensi output sebelum beralih.

## Memulai

```bash
pip install bankstatementparser
```

```python
from bankstatementparser import create_parser, detect_statement_format

# Works with MT940 today, CAMT.053 tomorrow, PDF anytime
for file in bank_statement_files:
    fmt = detect_statement_format(file)
    parser = create_parser(file, fmt)
    df = parser.parse()
    process(df)  # Your code doesn't change
```

Untuk laporan PDF dari bank yang belum menawarkan ekspor CAMT terstruktur:

```python
from bankstatementparser.hybrid import smart_ingest

result = smart_ingest("statement.pdf")
assert result.verification.status == "VERIFIED"
```

[Baca dokumentasi selengkapnya](/getting-started/index.html)

[Bandingkan dengan alternatif ❯](/comparison/index.html) | [Lihat kasus penggunaan nyata ❯](/use-cases/index.html)
