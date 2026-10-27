# G1 — Product Baseline Readiness Contract

**Trigger:** User meminta seluruh Product Foundation ditinjau atau siap handoff ke Phase 2. G1 adalah product readiness (design), bukan software implementation atau release gate.

## Evaluate against actual artifacts/evidence
- Product problem, tujuan, stakeholders/target users dan outcomes cukup jelas.
- Requirements kritis memiliki deskripsi, prioritas, stable IDs dan acceptance criteria.
- MVP scope menyebutkan apa yang termasuk, ditunda, dan dikecualikan, selaras dengan requirements.
- Technical requirements dan constraints relevan telah disusun dengan links yang sesuai; gap yang berdampak dicatat.
- Pilihan material dimengerti dan **secara eksplisit disetujui user**; ada decision/approval reference (bukan sekadar interpretasi agent).
- Artefak Lean atau Structured memiliki satu canonical sumber per keputusan dan tidak kontradiktif.
- Risiko, asumsi, blocker, deferred scope, serta ketidakpastian tetap terlihat dan memiliki owner/next review bila perlu.
- Tidak ada critical unresolved blocker yang membuat desain produk tidak layak dilanjutkan.

## Verdict
| Status | Meaning | Handoff |
|---|---|---|
| `PASS` | Semua kriteria relevan terpenuhi, evidence terhubung, keputusan material approved, tidak ada critical blockers | Product baseline siap digunakan Phase 2 |
| `PARTIAL` | Sebagian produk valid, tetapi approval/gap noncritical masih perlu penyelesaian | Jelaskan unblocked work dan gaps; jangan klaim baseline penuh APPROVED |
| `BLOCKED` | Critical gaps, keputusan material yang bertentangan atau high-risk blocker belum ditangani | Tahan handoff pada scope terdampak sampai ditinjau |

**Tidak boleh `PASS` karena template terisi atau dokumen ada.** Jika evidence tidak tersedia, tandai `UNVERIFIED` pada kriteria dan beri verdict agregat yang mencerminkan gap; jangan mengaku test dilakukan.

## Output review
Tampilkan matrix kriteria → artifact/section/ID → evidence/approval → status; daftar blocker/pending decisions; rekomendasi singkat; G1 verdict dan batas cakupan; handoff kepada `beginnerd-solution` jika sesuai.

Untuk pertanyaan PF-01/PF-02/PF-03/PF-04 yang berdiri sendiri, tidak wajib memaksakan G1 review.

## H-02/H-03 evidence refinement
A complete G1 review must distinguish **product clarity** from **solution feasibility** and **coding readiness**. Include an explicit status for each applicable critical requirement, approval evidence, negative/failure-state acceptance, cross-device/data consistency where relevant, and named owner for postponed feasibility validation. Do not silently create quantitative thresholds. Technical decision detail may be deferred to SOLUTION-03–07, but material product conflicts cannot be hidden in a generic "Phase 2" bucket.

If a document is persisted, use the read-back contents for the G1 matrix; existence or a static validator PASS is not G1 PASS. If G1 is PARTIAL, explain which Phase 2 exploration can proceed safely and what cannot begin until findings resolve. Never interpret a user's agreement with a product draft as authorization to code or deploy.

### H02-03 three-readiness separation
An absolute user assurance never overrides evidence. Show **G1 Product Baseline** (product clarity/acceptance/approval), **G2 Solution Feasibility** (Phase 2 design and research), and **Release / Operations Readiness** (Phase 5–6 runtime evidence) separately. Turn material unknowns into PROPOSED observable constraints with planned check, source and Owner. Do not convert a gap description into G1 PASS.
