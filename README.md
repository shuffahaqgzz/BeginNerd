# BeginNerd — Guided Building Framework

**BeginNerd** membantu pemula dan tim campuran membangun aplikasi bersama AI coding agent melalui enam fase SDLC yang modular, dapat ditelusuri, dan berbasis bukti.

> **Status 27 Oktober 2026:** approved framework design = **6 fase / 32 workflow / 8 skill**. Di branch `main` setelah PR #9, **delapan paket skill memiliki source SKILL.md, references dan templates**. Status mereka adalah **SOURCE CANDIDATE**, bukan RUNTIME_VERIFIED. Fase 1 Product skill tetap **PARTIAL / NOT ACCEPTED** menurut laporan acceptance terakhir (4 PASS, 1 FAIL, 6 BLOCKED); Graphify/Hindsight dan full E2E belum terbukti. Source dan CI tidak boleh dipakai untuk klaim release v1.0 siap digunakan.

## Skill inventory

| Phase / type | Skill | Owned workflows |
|---|---|---|
| Companion | beginnerd-ask | Orientasi, navigasi, verified context, routing |
| Companion | beginnerd-setup | Onboarding, guidance preference, consented provider setup |
| Phase 1 — Product Foundation | beginnerd-product | PF-01–04 + G1 |
| Phase 2 — Solution Architecture | beginnerd-solution | SOLUTION-01–08 + G2 |
| Phase 3 — Planning & Control | beginnerd-plan | PLANNING-01–04 + Planning Readiness |
| Phase 4 — Development Foundation | beginnerd-foundation | FOUNDATION-01–05 + Foundation Readiness |
| Phase 5 — Implementation & QA | beginnerd-implement | IMPLEMENT-01–05 + Completion Check |
| Phase 6 — Release & Operations | beginnerd-release | RELEASE-01–03 and OPS-01–03 |

Satu skill entry point per fase menggunakan references internal (Hybrid Modular); pengguna boleh meminta satu workflow tanpa regenerasi seluruh proyek. Work Structure Brainstorming berada di PLANNING-02, bukan skill kesembilan.

## Quickstart — static source review (tidak menginstal skill)

Gunakan Python 3.11+ (atau versi yang kompatibel dengan syntax project ini), Git dan repo checkout pada commit/branch yang ingin diuji. Static checks tidak membutuhkan API keys atau provider access.

~~~bash
git clone https://github.com/shuffahaqgzz/BeginNerd.git
cd BeginNerd
python3 scripts/validate_repository.py
python3 scripts/build_portable_references.py --check
python3 scripts/validate_skill_packages.py
python3 -m unittest discover -s tests/contracts -p 'test_*.py' -v
~~~

**Status distribusi:** semua delapan skill source telah terintegrasi melalui PR #7 dan #9. Untuk evaluasi gunakan commit yang diketahui; checkout source `main` tidak membuktikan bahwa skill terpasang atau diaktifkan di Codex.

### Portable skill discovery dan penggunaan nyata

Installer awal mengikuti Agent Skills + Skills CLI; tidak ada installer npm BeginNerd khusus. Periksa installed skills dan metadata lebih dulu agar tidak memasang duplikat. Pada checkout branch yang tepat, periksa source references setiap paket; discovery melalui Skills CLI atau Codex harus diuji di runtime sendiri sebelum INSTALL/PROVIDER_VERIFIED dapat diklaim. Jangan otomatis memasang secara global atau overwrite local user modifications.

Panduan terkait: [Runtime Quickstart](docs/setup/QUICKSTART.md), [Packaging](docs/implementation/DISTRIBUTION-READINESS.md), [Skill Engineering Standard](docs/engineering/SKILL-ENGINEERING-AND-DISTRIBUTION-STANDARD.md).

## Governance dan bukti wajib

- **Explain Before Execute** → Contextual Learning → rekomendasi yang relevan → interview/approval untuk keputusan material.
- **Research First & Reuse First**. SOLUTION-06 memiliki technology research; PLANNING-02 mengubah approved decisions menjadi tasks.
- **Task decomposition formal hanya di PLANNING-02.** Executor/coordinator tidak boleh membuat task baru atau mengubah hierarchy sepihak.
- **Scoped Authorization.** Izin membuat/meninjau GitHub PR bukan izin deployment, host configuration, provider memory write atau secret administration.
- **Bounded Recovery.** Setiap perbaikan setelah verification failure memerlukan approval khusus; maksimum dua attempts per issue+baseline; kemudian HARD STOP/REVIEW_REQUIRED.
- **No Overclaim, No Overengineering, No Overrules, Least Authority.** Test PLANNED ≠ IMPLEMENTED ≠ EXECUTED ≠ PASS; documentation/CI static ≠ runtime acceptance.
- Graphify adalah knowledge provider, Hindsight persistent-memory provider ketika **benar-benar dipasang, diotorisasi dan diverifikasi**. Recall/retain perlu acknowledgement; tanpa itu MEMORY_SYNC_PENDING.

## Dokumen utama

[Framework Architecture](docs/architecture/FRAMEWORK-ARCHITECTURE.md) · [32 Workflow Registry](docs/workflows/WORKFLOW-REGISTRY.md) · [Decision Register](docs/decisions/DECISION-REGISTER.md) · [Agent Governance](docs/governance/AGENT-GOVERNANCE.md) · [Artifact & Readiness](docs/architecture/ARTIFACT-AND-READINESS-CONTRACT.md) · [Implementation Status](docs/implementation/STATUS.md).

[Validation Plan](docs/implementation/VALIDATION-PLAN.md) · [Real-World E2E Plan](docs/implementation/REAL-WORLD-E2E-VALIDATION.md) · [Framework Release Checklist](docs/implementation/FRAMEWORK-RELEASE-CHECKLIST.md).

## Open source, security dan kontribusi

Repository GitHub publik ini didistribusikan dengan [MIT License](LICENSE) sesuai keputusan Owner D2. Baca [Contributing](CONTRIBUTING.md), [Security Policy](SECURITY.md), [Publication Readiness](docs/implementation/PUBLICATION-READINESS.md) dan [Source Preview Notes](docs/releases/SOURCE-PREVIEW-2026-10-27.md). Copyright-holder notice dan lisensi komponen pihak ketiga tetap perlu ditinjau sebelum klaim rilis v1.0.

Jangan unggah secrets, private project memory, kredensial, log runtime yang belum disanitasi, atau provider tokens. Lihat [Security Disclosure](SECURITY.md). Gunakan branch/PR untuk kontribusi; tagging GitHub release, perubahan visibility/branch protection dan deployment memerlukan authorization tersendiri.

**Studi kasus real E2E A2 belum dipilih Owner.** Pengujian perilaku, integrasi server srv-test01, Graphify/Hindsight, browser dan release nyata harus dilakukan terpisah dan dibuktikan sebelum mendeklarasikan BeginNerd v1.0 RELEASE_READY.
