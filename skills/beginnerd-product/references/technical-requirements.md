# PF-04 — Technical Requirements

**Trigger:** User meminta TRD, kebutuhan integrasi/data, quality attributes, NFR, kontrol keamanan yang harus dipenuhi oleh desain, atau kriteria teknis penerimaan.

## Procedure
1. Turunkan kebutuhan teknis dari `REQUIREMENTS-...`, acceptance, MVP scope, profil pengguna, data dan constraints existing.
2. Gunakan ID stabil `TECHNICAL-REQUIREMENTS-001`. Tulis requirement yang dapat diuji/diobservasi beserta sumber, alasan, criticality, acceptance/verification method **planned**, dan hubungan ke product requirement.
3. Cakup secara proporsional: data handling/retention, availability, accessibility, performance targets jika didukung, integrations, platform/channel, environment constraints, security/privacy dan interoperability. Jika nilai target belum disepakati, tulis `TBD` dan siapa yang memutuskan.
4. Identifikasi reuse/hosting/licensing/budget/maintenance constraints serta apa yang harus dievaluasi pada Phase 2. Tidak menetapkan vendor/library/framework final hanya karena familiar.
5. Lakukan consistency review: jika technical requirement bertabrakan dengan MVP/PRD, tampilkan impact dan minta keputusan owner sebelum mengubah baseline approved.
6. Hasilkan bagian `PRODUCT.md` (Lean) atau `TECHNICAL-REQUIREMENTS-DOC.md` (Structured). Catat keputusan, risiko, open items dan approval refs.
7. Serahkan technical constraints untuk SOLUTION-03–07 pada Phase 2; threat modeling dan pemilihan komponen dilaksanakan oleh pemilik desain solusi.

## Completion
- Technical requirements kritis ditelusuri ke kebutuhan produk.
- Acceptance/verification sudah direncanakan, **bukan** diklaim telah diuji.
- Tidak ada final technology selection atau design approval yang diam-diam dimasukkan sebagai hasil PF-04.

## H-02 — Measurable and beginner-safe PF-04 hardening

For every material technical requirement, capture the tuple **product requirement ID -> technical requirement ID -> observable condition / metric -> verification plan -> source or explicit assumption -> decision owner -> readiness status**. Keep verification PLANNED until executed evidence exists. A sentence such as "fast", "secure", "always available", or "zero cost" alone is not an acceptance threshold.

### Proportional coverage and edge cases
| Domain | Discover relevant question or risk (not a mandatory feature) | Example evidence / deferred ownership |
|---|---|---|
| Data and privacy | What data is stored, who may read/change/export/delete, retention/recovery? | Source/product requirement; access and recovery design belongs to Phase 2 |
| Failure and integrity | What happens on invalid input, unavailable network/service, retry or duplicate? | Observable success/failure behavior and error-state verification |
| Availability and consistency | Is access expected across devices, which writes/deletes must become visible, under what verified conditions? | Distinguish agreed behavior from invented sync-time SLO |
| Performance and scale | Is any latency, number of users, storage, bandwidth or capacity target actually decided? | If not, label TBD, owner and decision point; do not invent numbers |
| Accessibility and channels | Which devices, languages, input methods and accessibility needs apply? | Observable scenario on relevant client, without selecting UI framework |
| Integration and metadata | What provider/API dependency, access constraint, data quality, and fallback exist? | Research needed; do not promise third-party content extraction |
| Security | Data-level authorization, session lifecycle, lost-device access and incident consequences? | Product security requirements only; design, controls and threat analysis Phase 2 |
| Budget and license | Does "free" include operation, domain, email and future usage thresholds? | User-approved boundary, supplier research UNVERIFIED until documented |

**Critical versus design-deferred:** G1 can review whether a product-level critical requirement and its planned acceptance are clear, while still handing lower-level engineering choices to Phase 2. Do not use "belongs to Phase 2" to hide a critical product ambiguity. Conversely, G1 is not a vendor qualification gate; a cost feasibility finding may remain UNVERIFIED when explicitly assigned to Phase 2 and does not automatically block all unaffected analysis. If a hard product constraint is impossible or materially contradictory on available evidence, HOLD affected scope and report the conflict.

**Beginner interaction:** explain a behavior with one example, recommend a reasonable default, and ask only for material decisions a novice can actually make. Do not require the novice to decide algorithms, cryptography, cloud vendors, arbitrary uptime percentages or infrastructure limits. Record proposed values as PROPOSED/TBD rather than approved metrics.

**Validation before handoff:** check orphaned IDs, missing verification plans, source provenance, decided vs TBD thresholds, failure behavior for critical user journeys, unresolved conflicts, and explicit approval scope. Do not mark a technical requirement TESTED or a product G1 PASS based only on planned checks.
