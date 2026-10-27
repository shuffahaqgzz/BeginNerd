# BeginNerd — Companion Skill Packaging & Installation Readiness

**Scope:** Installable source packaging untuk `beginnerd-ask`, `beginnerd-setup`, dan `beginnerd-product` yang sudah merged. Lima lifecycle skills berikutnya belum installable. Target Codex CLI pada `srv-test01`; runtime Phase 1 PARTIAL.

## Langkah aman untuk assessment
Mulai dengan inventory, tanpa mengubah instalasi agent:

```bash
# Kebutuhan dan path aktual harus diverifikasi pada mesin target
node --version
npx skills@latest add shuffahaqgzz/BeginNerd --list
npx skills@latest ls -g
```

`--list` tidak memasang skill, tetapi `npx` dapat mengunduh CLI ke npm cache. Jangan salah menganggap perintah ini sama sekali tanpa efek filesystem/network.

**Expected discoverable from main**: `beginnerd-ask`, `beginnerd-setup`, `beginnerd-product`. Actual source parity on `srv-test01` must be reverified.

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
npx skills@latest ls -g  # periksa daftar skill global yang terpasang
npx skills@latest update -g  # Hanya untuk instalasi global; perlu approval
```

`check` dan `update` sebaiknya diverifikasi terhadap CLI versi terpasang. Untuk me-rollback, simpan inventory dan versi sumber yang diketahui baik, lalu lakukan pemulihan yang disetujui; jangan hapus direktori skill yang mungkin berisi user modifications tanpa review.

## Status
- Portable files & CI: bukti hanya berlaku jika PR lulus dan disetujui.
- Skills CLI actual discovery/install: NOT EXECUTED.
- Runtime invocation: NOT EXECUTED.
- Graphify/Hindsight integration: UNVERIFIED.
- Issue #2 tetap OPEN untuk validasi runtime.

## Phase 1 product candidate (in separate PR)
`beginnerd-product` has merged via PR #4/#6. Three installable source skill directories now exist; runtime Product acceptance remains PARTIAL. Verify discovery/source parity on `srv-test01`, do not duplicate installed skills, request project-scoped runtime-write authorization and capture behavioral evaluation before any runtime-verified claim.
