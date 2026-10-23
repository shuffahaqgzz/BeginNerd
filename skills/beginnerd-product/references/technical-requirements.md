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
