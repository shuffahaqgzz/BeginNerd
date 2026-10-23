# BeginNerd — Companion Skill Packaging & Installation Readiness

**Scope:** Installable *source packaging* untuk `beginnerd-ask` dan `beginnerd-setup`. Kode/enforcement lifecycle enam fase masih desain. Target runtime awal: Codex CLI pada `srv-test01`.

## Langkah aman untuk assessment
Mulai dengan inventory, tanpa mengubah instalasi agent:

```bash
# Kebutuhan dan path aktual harus diverifikasi pada mesin target
node --version
npx skills@latest add shuffahaqgzz/BeginNerd --list
npx skills@latest ls -g
```

`--list` tidak memasang skill, tetapi `npx` dapat mengunduh CLI ke npm cache. Jangan salah menganggap perintah ini sama sekali tanpa efek filesystem/network.

**Expected discoverable**: `beginnerd-ask` dan `beginnerd-setup` saja. Tidak mengklaim output sudah diuji di `srv-test01`.

## Controlled installation (belum diotorisasi/diuji dalam sesi ini)
Setelah membandingkan preexisting skills, memeriksa konfigurasi, menetapkan target scope, dan memperoleh otorisasi:

```bash
# Jalankan dari consumer-project bila ingin instalasi project-scoped
npx skills@latest add shuffahaqgzz/BeginNerd \
  --skill beginnerd-ask --skill beginnerd-setup -a codex
```

Instalasi global `-g` adalah perubahan user-wide; minta izin eksplisit sebelum penggunaan. Hindari menduplikasi skill lewat native plugin dan Skills CLI sekaligus. Jangan memakai `-y` sebelum scope/diff disetujui.

## Setelah instalasi
- Verifikasi lokasi discovery aktual Codex; jangan menebak path jika versi runtime berbeda.
- Pastikan kedua direktori memuat `SKILL.md` dan `references/` termasuk generated governance snapshots; uji root-independent lookup.
- Periksa invocation melalui sesi baru dan 22 behavioral scenarios; lihat `tests/activation/queries.json` untuk positive/negative triggers.
- Hindsight activation, retain dan Graphify retrieval **tidak diaktifkan oleh installer**. Lanjutkan melalui `beginnerd-setup` dengan explicit consent dan disposable project test scope.
- Rekam versi source, hash, before/after diffs, test evidence, rollback, dan status jujur.

## Update dan rollback
```bash
npx skills@latest check
npx skills@latest update -g  # Hanya untuk instalasi global; perlu approval
```

`check` dan `update` sebaiknya diverifikasi terhadap CLI versi terpasang. Untuk me-rollback, simpan inventory dan versi sumber yang diketahui baik, lalu lakukan pemulihan yang disetujui; jangan hapus direktori skill yang mungkin berisi user modifications tanpa review.

## Status
- Portable files & CI: bukti hanya berlaku jika PR lulus dan disetujui.
- Skills CLI actual discovery/install: NOT EXECUTED.
- Runtime invocation: NOT EXECUTED.
- Graphify/Hindsight integration: UNVERIFIED.
- Issue #2 tetap OPEN untuk validasi runtime.
