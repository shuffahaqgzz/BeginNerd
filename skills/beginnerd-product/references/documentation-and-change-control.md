# Phase 1 — Adaptive Documentation & Change Control

## Artifact modes
**Lean** (default pada scope kecil, jika sesuai kebutuhan): satu `PRODUCT.md` dengan sections Discovery / Product Brief, Product Requirements, MVP, Technical Requirements, Decisions & G1. Jangan membuat empat dokumen terpisah bila informasi ringkas cukup.

**Structured** (scope/risiko lebih besar atau dipilih user):
- PF-01 → `PRODUCT-BRIEF.md`
- PF-02 → `PRODUCT-REQUIREMENTS-DOC.md`
- PF-03 → `MINIMUM-VIABLE-PRODUCT-SCOPE.md`
- PF-04 → `TECHNICAL-REQUIREMENTS-DOC.md`

Nama lama `PRD.md`, `MVP-SCOPE.md`, dan `TRD.md` adalah proposal historis, **bukan final default naming**. `PRODUCT-BRIEF.md` tidak diganti. `API-GUIDE.md` tidak menjadi Phase 1 mandatory artifact.

## Reuse & brownfield
Audit dokumen dan naming existing terlebih dahulu. Jika dokumen approved yang setara sudah ada, referensi/revisi secara terkendali; jangan menciptakan canonical parallel. Pilih mode berdasarkan kompleksitas, risiko dan kebutuhan user; jelaskan rekomendasi, terima override user dengan mencatat konsekuensi.

## Approval and revisions
1. Tentukan sumber canonical dan status: `DRAFT`, `IN_REVIEW`, `APPROVED`, `SUPERSEDED`.
2. Pertahankan stable IDs: `REQUIREMENTS-001`, `ACCEPTANCE-CRITERIA-001`, `TECHNICAL-REQUIREMENTS-001`; periksa collisions dan references.
3. Saat scope/requirement berubah, identifikasi artefak, MVP, technical/acceptance, dan keputusan terdampak.
4. Jelaskan change impact dan rekomendasi; interview untuk approval material. Jangan ubah keputusan yang sudah approved sepihak.
5. Rekam siapa/apa yang mengotorisasi (bila tersedia), evidence dan versi current; jika informasi approval belum ada, status tetap pending.
6. Jika menulis file/repo: izin khusus diperlukan; jika hanya menjawab, tampilkan draf siap review.

## Templates (read only when producing artifacts)
- Lean → `assets/product-lean-template.md`
- Structured brief → `assets/product-brief-template.md`
- Structured requirements → `assets/product-requirements-template.md`
- Structured MVP → `assets/mvp-scope-template.md`
- Structured technical requirements → `assets/technical-requirements-template.md`

Template adalah starter, bukan bukti acceptance. G1 status memerlukan kriteria di `references/g1-readiness.md`.

## H-03 — Controlled persistence, readback and workspace integrity

For any file write, check the actual consumer project instructions (for example AGENTS.md), inventory existing artifacts and select an explicitly authorized target. A private smoke directory is not automatically an application implementation workspace. User approval to persist a product document is not authorization to create application code, upload artifacts or publish a Site.

After writing an artifact:
1. **Read back the actual saved file**, not the proposed text in conversation.
2. Check canonical naming and status, IDs and bidirectional references where present, approved/proposed separation, open decisions with owners, planned-vs-executed test language, and readiness evidence.
3. Record precise path, file existence, stable content hash, readback timestamp and diff against prior artifact when available. A hash proves content at the observation time, not historical provenance.
4. For workspace isolation, compare a scoped **before-and-after inventory with content hashes** of relevant files and paths (including untracked and ignored content as permitted). The fact that `git status --short` lists the same untracked directories does **not** establish that their contents did not change.
5. If a baseline manifest is unavailable, state **UNVERIFIED** for unrelated-file preservation rather than asserting all other files unchanged.
6. Keep material changes PROPOSED until separately approved; approval to save a document is not approval of its new feature proposals.
7. Never copy secrets or private memory into test evidence. Save sanitized evidence only in an approved location.

A static document checker can catch missing/duplicate IDs and broken links, but cannot establish that user approval, real test execution, deployment readiness or full filesystem isolation occurred. Report those dimensions separately.
