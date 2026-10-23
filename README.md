# BeginNerd

**BeginNerd** adalah framework **Guided Building** untuk membantu pengguna pemula dan tim campuran merencanakan, membangun, menguji, merilis, dan memelihara aplikasi bersama AI coding agent.

> **Status: FOUNDATION BOOTSTRAP / UNDER REVIEW.** Desain framework enam fase dan 32 workflow telah disetujui. Dua companion SKILL.md di sini merupakan starter implementation yang **belum diuji pada agent runtime aktual**. Enam lifecycle skills belum diimplementasikan.

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
- [Implementation status](docs/implementation/STATUS.md) dan [validation plan](docs/implementation/VALIDATION-PLAN.md).
- [Skills inventory](skills/README.md) dan [runtime quickstart](docs/setup/QUICKSTART.md).

## Verifikasi repository

Untuk meninjau branch bootstrap sebelum di-merge:

```bash
git clone https://github.com/shuffahaqgzz/BeginNerd.git
cd BeginNerd
git switch setup/framework-foundation-v1
python3 scripts/validate_repository.py
python3 -m unittest discover -s tests/contracts -p 'test_*.py' -v
```

Validator memeriksa kontrak statis dan inventaris. Skenario di [tests/behavioral/scenarios.json](tests/behavioral/scenarios.json) adalah **spesifikasi**, bukan hasil eksekusi agent. CI hijau tidak membuktikan kemampuan routing runtime atau Graphify/Hindsight yang benar-benar berfungsi.

## Prinsip

Explain Before Execute · Contextual Learning · Research Before Build · Reuse Before Reinvent · Explain → Interview → Approve → Record · Evidence-Based Completion · No Overclaim · No Overengineering · No Overrules · Scoped Authorization.

Pembagian task formal hanya melalui Planning (PLANNING-02). Remediasi setelah verification failure memerlukan approval eksplisit per upaya, maksimal dua upaya untuk masalah/baseline yang sama, lalu HARD STOP jika masih gagal.

## Governance, privasi, dan lisensi

Gunakan branch dan Pull Request; jangan menganggap persetujuan desain sebagai izin deployment. Rahasia, konfigurasi privat, dan memory aktual tidak boleh masuk repository public. Knowledge Provider **Graphify** dan Memory Provider **Hindsight** harus diverifikasi secara nyata dan mengikuti izin user serta scope proyek.

Lisensi belum ditetapkan pemilik; jangan mengasumsikan repository public berarti seluruh kode dapat digunakan ulang tanpa syarat.
