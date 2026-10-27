# BeginNerd — Skill Engineering & Distribution Standard v1.0

**Status:** MERGED IMPLEMENTATION STANDARD v1.0 (PR #3); bukan keputusan arsitektur baru maupun bukti runtime-ready. **Parent baseline:** BN-DEC-009, 8 skill target (2 companion + 6 lifecycle), 32 workflow. **Tracking:** Issue #2, Paket 01.

## Hierarki acuan
1. **Agent Skills Specification** — format dan metadata `SKILL.md`, path references, progressive disclosure: https://agentskills.io/specification
2. **Agent Skills authoring & evaluations** — best practices, description triggering, with/without-skill evaluation: https://agentskills.io/skill-creation/best-practices ; https://agentskills.io/skill-creation/optimizing-descriptions ; https://agentskills.io/skill-creation/evaluating-skills
3. **Matt Pocock skills** — rujukan implementasi/perilaku modular, `skills.sh` installer dan plugin marketplace; bukan sumber governance BeginNerd: https://github.com/mattpocock/skills
4. **BN-DEC-approved contracts** — sumber otoritatif keputusan BeginNerd, phase ownership, approval dan Hindsight/Graphify continuity. Jika contoh eksternal bertentangan, jangan diam-diam mengganti keputusan yang sudah approved.

## 1. Spesifikasi skill
- Tiap skill yang **ditawarkan untuk instalasi** harus mempunyai `skills/<name>/SKILL.md` dengan YAML frontmatter `name` dan `description` yang valid.
- `name`: huruf kecil, angka, dash; panjang 1–64, tanpa dash awal/akhir atau ganda, sama dengan nama direktori. `description`: 1–1024 karakter; menjelaskan kapan/untuk apa skill dipakai.
- `compatibility` opsional (maks. 500 karakter). `license`, `metadata`, `allowed-tools` adalah field opsional; jangan mengasumsikan vendor mendukung semuanya. Jangan menyatakan lisensi BeginNerd sampai Owner memilihnya.
- `SKILL.md` berisi instruksi inti dan dapat dibaca tanpa seluruh source repository. Target authoring: kurang dari 500 baris dan kurang dari 5.000 token (guideline, bukan hard spec).
- Buat references terarah: tulis *kapan* harus dibaca, bukan instruksi membacanya semua. Hindari link dari skill ke `../../docs` atau file `AGENTS.md` milik repository sumber sebagai **hard dependency**.
- Jika perlu instruksi proyek konsumen, baca file existing milik proyek konsumen jika ada. Bila tidak ada, jangan memaksakan scaffolding oleh companion skill.

## 2. Kewenangan & invocation
- `beginnerd-ask`: penjelasan, recovery verified context dan routing. Tidak mengubah scope/plan atau mengeksekusi tugas milik lifecycle.
- `beginnerd-setup`: onboarding, preferences, existing-state inventory, setup terotorisasi, verifikasi provider. Tidak otomatis menulis konfigurasi ketika dipanggil, tidak menjadi `beginnerd-foundation`.
- beginnerd-product remains Phase 1 with PARTIAL runtime acceptance. The five later lifecycle SKILL.md packages are now present on `main` **as source candidates**, not runtime-verified skills. Do not claim runtime readiness or add placeholder skills merely to reach a count.
- User-invoked / model-invoked dan vendor-specific metadata diputuskan berdasarkan runtime compatibility serta evaluation. Format standar netral terhadap harness.
- Scoped authorization, No Overclaim, research/reuse-first, PLANNING-02-only formal decomposition dan maksimum dua remediasi terotorisasi tetap wajib.

## 3. Packaging portability
- Instalasi `skills CLI` dapat menyalin **satu direktori skill**, tanpa `docs/` canonical root. Oleh karena itu setiap companion harus memuat minimum references yang dibutuhkan secara **self-contained**.
- Source of truth adalah `docs/governance/AGENT-GOVERNANCE.md`, `docs/governance/MEMORY-KNOWLEDGE-CONTRACT.md`, dan `docs/workflows/WORKFLOW-REGISTRY.md`.
- scripts/build_portable_references.py kini mereplikasi **6 sumber canonical menjadi 38 reference snapshots** pada delapan skill packages, dengan Git blob SHA provenance dan pemeriksaan stale snapshot. Source docs tetap authoritative, bukan salinan mandiri dengan aturan baru.
- Gunakan `python3 scripts/build_portable_references.py --write` setelah canonical docs berubah, review diff, dan commit bersama. CI menjalankan `--check` agar snapshot stale langsung gagal.
- Pengguna yang menginstal individual skill menggunakan snapshot terpasang pada versinya. Pembaruan sumber canonical hanya berlaku setelah skill diperbarui. Snapshot bukan bukti bahwa repository saat runtime selalu tersedia.

## 4. Validation berlapis
| Stage | Evidence minimum | Batas klaim |
|---|---|---|
| Metadata/static | `validate_skill_packages.py`, `validate_repository.py`, CI | Menguji flat frontmatter subset & file package. **Bukan** parser YAML formal lengkap |
| Source parity | portable references `--check`, isolated package tests | Menemukan stale/missing reference; **bukan** runtime discovery |
| Upstream conformance | `skills-ref validate <skill>` dari sumber **agentskills/agentskills** yang diverifikasi jika tersedia | Reference demo, bukan sertifikasi keamanan/portabilitas; jangan mengandalkan paket PyPI acak |
| Discovery | `npx skills@latest add shuffahaqgzz/BeginNerd --list` pada environment test | Membuktikan skill terdeteksi saja; `npx` dapat memakai network/npm cache |
| Installation | Scope/target dipilih dan diotorisasi; preexisting installations diperiksa; before/after inventory | Membuktikan files dipasang, **bukan** dipanggil dengan benar |
| Activation | Positive/negative trigger cases dan near-misses pada runtime fresh | Menguji pemilihan/false trigger; bukan proof eksekusi workflow |
| Behavioral & E2E | Source scenario registry (currently 67 cases); with-skill/without-skill, trace/evidence and honest per-case status | User experience, governance, Hindsight/Graphify memerlukan tes provider sebenarnya |

### Format status
`DESIGNED`, `STATIC_PASS`, `DISCOVERY_VERIFIED`, `INSTALLED`, `RUNTIME_VERIFIED`, `PROVIDER_VERIFIED`, `RELEASE_READY` adalah **dimensi berbeda**, bukan urutan kelulusan otomatis. Untuk acceptance, gunakan PASS/PARTIAL/BLOCKED/UNVERIFIED berdasarkan evidence nyata. Jangan menutup Paket 01 hanya karena CI PASS.

## 5. Distribusi
- **Tahap awal:** inspect current installations, versions and project/global scopes before Skills CLI discovery. `main` now includes all eight source candidates following PR #9; actual installed copies must be checked independently. Project-scoped install and fresh-session verification require separate approval; no new BeginNerd npm installer.
- **Tahap berikut:** native plugin manifests dan release/versioning setelah portable install & runtime invocation terbukti, dengan approval Owner. Hindari plugin + skills CLI ganda pada runtime sama.
- Jangan membuat `package.json`, marketplace manifest, symlink installer, auto-update, publikasi npm atau release tag hanya untuk mengklaim distribusi sebelum compatibility diuji.
- Update/uninstall harus diuji bersama versi pinned, scope isolasi, idempotensi dan rollback, bukan mengasumsikan CLI selalu bekerja.

## Updated 27 October 2026 — eight source candidates, not eight runtime passes

Source packaging sekarang mencakup 8 skill (2 companion + 6 lifecycle), 32 workflow references dan offline advisory checkers Phase 5/6. Skenario activation/behavioral untuk seluruh 8 skills ditambahkan dengan execution_status NOT_EXECUTED sampai evidence langsung tersedia. Validator mencakup self-contained copies and generated snapshots, **tidak membuktikan runtime**. Read-only JSON authorization checkers tidak menggantikan host/provider-side enforcement. Owner A2 menunda real study case, sehingga v1.0 RELEASE_READY dan E2E remain unverified.

## 6. Exit criteria dari persiapan ke runtime validation
- Setiap satu dari delapan source skill kandidat memiliki references yang resolvable tanpa repository root; package validation is not runtime approval.
- Validator contract dan isolated copies lulus di CI.
- Activation cases nyata tersedia sebagai spesifikasi dengan label NOT_EXECUTED.
- Source provenance, approval boundary, provider consent dan perbedaan status sudah terdokumentasi.
- V01–V02 actual installed-skill comparison yang BLOCKED masih perlu diselesaikan; jangan melompati V03–V10.

**Tidak ada skill baru, workflow baru, release, instalasi runtime, atau perubahan BN-DEC dalam standard ini.**
