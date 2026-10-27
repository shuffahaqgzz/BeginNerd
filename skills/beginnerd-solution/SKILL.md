---
name: beginnerd-solution
description: Pandu desain Phase 2 BeginNerd meliputi user flow, application navigation, arsitektur sistem/domain, database, API dan integrasi, riset serta pemilihan teknologi, keamanan, UI/design system dan G2. Aktifkan untuk keputusan tentang rancangan aplikasi, bukan untuk membuat task, coding atau deployment.
---

# BeginNerd Solution — Phase 2 (SOLUTION-01–08)

**Owner:** desain solusi dan keputusan arsitektur, bukan eksekusi kode atau release. Jalankan workflow yang diminta saja; full-phase review hanya bila relevan.

## Standard operating contract
1. **Explain Before Execute** tujuan, keluaran, opsi, risiko dan tradeoffs dengan bahasa sesuai pengalaman user. Gunakan Contextual Learning.
2. **Discover & reconcile** sumber canonical: G1, approved requirements, MVP, technical constraints, existing code/docs jika brownfield. G1 PARTIAL membatasi pekerjaan ke area yang tidak terblokir; tidak otomatis dianggap G1 PASS.
3. **Session continuity:** Hindsight recall awal sesi jika benar-benar aktif/terotorisasi, verifikasi terhadap Git/docs, retain perubahan material dan checkpoint sebelum handoff dengan acknowledgement. Jika gagal, catat MEMORY_SYNC_PENDING. Graphify mendukung hubungan knowledge, tidak menggantikan canonical docs. Baca references/memory-knowledge-contract.md.
4. **Route dan load hanya reference relevan:** SOLUTION-01 references/user-flow.md; SOLUTION-02 references/application-navigation.md; SOLUTION-03 references/system-architecture.md; SOLUTION-04 references/database-data-design.md; SOLUTION-05 references/api-integration.md; SOLUTION-06 references/technology-selection.md; SOLUTION-07 references/security-architecture.md; SOLUTION-08 references/ui-design.md.
5. **Implementasi strategi desain:** Adaptive Visual Review untuk experience/UI; Best-Fit Recommendation untuk system/technology; Adaptive Security Baseline dengan Basic/Application/Enhanced berdasarkan risiko aplikasi, bukan skill pengguna. SOLUTION-06 adalah owner utama Research-First & Reuse-First.
6. **Material approval:** Explain → Interview → Approve → Record untuk architecture, cost, security risk, provider, data/privacy dan material UX decisions. Jangan menandai PROPOSED sebagai APPROVED.
7. **Produce proportional artifacts:** Lean satu SOLUTION-BLUEPRINT.md bila cukup; Structured menurut kompleksitas. Untuk perubahan file, baca references/document-control.md dan dapatkan path-scoped authorization, lakukan readback. Tanpa izin, hasilkan draft dalam chat.
8. **Validate & handoff:** traceability requirement→design→planned tests, konsistensi UX/navigation/system/data/API/security, sumber riset, approver dan blockers. Untuk assessment G2 eksplisit baca references/g2-readiness.md; PASS harus berbasis evidence.

## Immutable boundaries
- Formal work package/task/subtask/milestone decomposition hanya PLANNING-02. Jangan menciptakannya di Phase 2.
- Jangan install dependency, ubah config/provider, melakukan coding, membuat Sites atau deploy di Phase 2 sebagai jalan pintas.
- Tool availability bukan authorization. Terapkan No Overclaim, No Overengineering, No Overrules dan Least Authority: references/agent-governance.md.
- Critical security gap tidak dapat memperoleh G2 PASS hanya karena risk acceptance tanpa kontrol efektif.
- Jangan mengarang vendor prices, benchmarks, license compliance, deployment evidence, security certification, metrics atau user approval. Jika tidak terbukti tulis UNVERIFIED.
- Research/reuse policy di references/research-reuse-policy.md; sumber readiness di references/artifact-readiness-contract.md.

## Output minimum
Workflow IDs, source/requirement links, desain dan alternatifnya, evidence yang terverifikasi, keputusan PROPOSED/APPROVED, risiko dan owners, planned tests, G2 scoped verdict hanya bila dinilai, dan handoff ke Planning untuk scope siap. Retain dengan acknowledgement jika memory memang tersedia.
