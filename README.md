# BeginNerd

**BeginNerd** adalah framework **Guided Building** untuk membantu pengguna pemula dan tim campuran merencanakan, membangun, menguji, merilis, dan memelihara aplikasi bersama AI coding agent.

> **Status: FOUNDATION MERGED; PHASE 1 PRODUCT SKILL IN IMPLEMENTATION REVIEW.** Desain enam fase dan 32 workflow telah disetujui. Dua companion skills dapat ditemukan dan menurut laporan pengguna telah digunakan secara dasar pada Codex; Graphify/Hindsight belum lolos integrasi. Pada branch implementasi ini, `beginnerd-product` mempunyai entry point dan references **sebagai kandidat skill ketiga**, bukan runtime PASS. Lima lifecycle skills lainnya belum diimplementasikan.

## Arsitektur target

| Jenis | Skill | Tanggung jawab |
|---|---|---|
| Companion | beginnerd-ask | Menjelaskan, memulihkan dan memverifikasi konteks, mengarahkan ke workflow yang tepat |
| Companion | beginnerd-setup | First-use onboarding, pilihan guidance, konfigurasi terotorisasi Graphify/Hindsight |
| Phase 1 | beginnerd-product | Product Foundation (4 workflows) |
| Phase 2 | beginnerd-solution | UX & Solution Architecture (8 workflows) |
| Phase 3 | beginnerd-plan | Planning & Control (4 workflows) |
| Phase 4 | beginnerd-foundation | Development Foundation (5 workflows) |
| Phase 5 | beginnerd-implement | Implementation & QA (5 workflows) |
| Phase 6 | beginnerd-release | Release & Operations (6 workflows) |

Delapan nama skill adalah target framework; direktori lifecycle sengaja hanya berisi kontrak boundary sampai implementasi benar-benar dilakukan dan diuji.

## Dokumentasi canonical

- [Arsitektur framework](docs/architecture/FRAMEWORK-ARCHITECTURE.md) — enam fase dan quality/readiness checks.
- [Artifact & readiness contract](docs/architecture/ARTIFACT-AND-READINESS-CONTRACT.md) — dokumen, keterlacakan dan bukti fase.
- [Workflow registry](docs/workflows/WORKFLOW-REGISTRY.md) — 32 IDs, owner dan tanggung jawab.
- [Decision register](docs/decisions/DECISION-REGISTER.md) dan [detail keputusan BN-DEC-009](docs/decisions/BN-DEC-009-APPROVED-DETAILS.md) — approved design serta provenance gaps.
- [Agent governance](docs/governance/AGENT-GOVERNANCE.md) — approval, no-overclaim, batas remediasi.
- [Memory & knowledge](docs/governance/MEMORY-KNOWLEDGE-CONTRACT.md) — Graphify, Hindsight, session continuity.
- [Research & reuse](docs/governance/RESEARCH-REUSE-POLICY.md) dan [work structure](docs/governance/WORK-STRUCTURE-POLICY.md).
- [Implementation status](docs/implementation/STATUS.md), [validation plan](docs/implementation/VALIDATION-PLAN.md), dan [Phase 1 product implementation contract](docs/implementation/PHASE-1-PRODUCT-IMPLEMENTATION-CONTRACT.md).
- [Skills inventory](skills/README.md) dan [runtime quickstart](docs/setup/QUICKSTART.md).

## Verifikasi repository dan packaging

Untuk memeriksa baseline dari `main` atau branch PR yang ditinjau:

```bash
git clone https://github.com/shuffahaqgzz/BeginNerd.git
cd BeginNerd
python3 scripts/validate_repository.py
python3 scripts/build_portable_references.py --check
python3 scripts/validate_skill_packages.py
python3 -m unittest discover -s tests/contracts -p 'test_*.py' -v
```

Target distribusi branch ini: `beginnerd-ask`, `beginnerd-setup`, dan kandidat `beginnerd-product` (tiga skill jika PR di-merge). Lima lifecycle skills berikutnya masih berupa kontrak desain. [Skill Engineering Standard](docs/engineering/SKILL-ENGINEERING-AND-DISTRIBUTION-STANDARD.md) dan [Distribution Readiness](docs/implementation/DISTRIBUTION-READINESS.md) menerangkan batas validasi, installation scope, serta persyaratan izin.

Validator memeriksa kontrak statis, snapshots dan inventaris; penggunaan pada runtime tetap memerlukan pengujian. Discovery tiga skill melalui Skills CLI harus diverifikasi setelah commit target terintegrasi; dua companion sudah berhasil discovery dan basic invocation menurut laporan pengguna. Skenario di [tests/behavioral/scenarios.json](tests/behavioral/scenarios.json) serta [activation queries](tests/activation/queries.json) adalah **spesifikasi**, bukan hasil eksekusi agent. CI hijau tidak membuktikan kemampuan routing runtime atau Graphify/Hindsight yang benar-benar berfungsi.

## Prinsip

Explain Before Execute · Contextual Learning · Research Before Build · Reuse Before Reinvent · Explain → Interview → Approve → Record · Evidence-Based Completion · No Overclaim · No Overengineering · No Overrules · Scoped Authorization.

Pembagian task formal hanya melalui Planning (PLANNING-02). Remediasi setelah verification failure memerlukan approval eksplisit per upaya, maksimal dua upaya untuk masalah/baseline yang sama, lalu HARD STOP jika masih gagal.

## Governance, privasi, dan lisensi

Gunakan branch dan Pull Request; jangan menganggap persetujuan desain sebagai izin deployment. Rahasia, konfigurasi privat, dan memory aktual tidak boleh masuk repository public. Knowledge Provider **Graphify** dan Memory Provider **Hindsight** harus diverifikasi secara nyata dan mengikuti izin user serta scope proyek.

Lisensi belum ditetapkan pemilik; jangan mengasumsikan repository public berarti seluruh kode dapat digunakan ulang tanpa syarat.
