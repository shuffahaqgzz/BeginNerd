---
name: beginnerd-product
description: Gunakan untuk menemukan kebutuhan produk aplikasi, menyusun Product Brief dan Product Requirements, menentukan MVP Scope, mendefinisikan Technical Requirements, atau menilai G1 Product Baseline Readiness. Dukung pengguna pemula lewat penjelasan, interview, rekomendasi, dan approval tanpa mengambil alih desain teknologi atau implementasi.
---

# BeginNerd Product — Phase 1 Product Foundation

## Ownership
Skill ini memiliki **PF-01 Product Discovery**, **PF-02 Product Requirements**, **PF-03 MVP Definition**, **PF-04 Technical Requirements**, dan evaluasi **G1 Product Baseline Readiness**. Empat workflow adalah tanggung jawab internal satu skill Hybrid Modular, bukan empat skill baru.

## Kapan digunakan
- Ide aplikasi masih kabur atau perlu disepakati masalah dan target pengguna → PF-01.
- Pengguna ingin membuat/meninjau kebutuhan, user stories, acceptance criteria → PF-02.
- Pengguna ingin menentukan fitur minimum untuk MVP atau apa yang ditunda → PF-03.
- Pengguna perlu mendokumentasikan batasan non-fungsional, data, integrasi atau kebutuhan teknis → PF-04.
- Pengguna meminta validasi apakah product baseline siap dilanjutkan ke Solution Design → G1.
- Permintaan seluruh Phase 1 → jalankan PF-01 sampai PF-04 sesuai dependensi dan cek G1. Bila hanya satu workflow diminta, jangan memaksa dokumen lain.

## Prosedur umum
1. **Explain Before Execute.** Jelaskan tujuan, hasil, batasan dan istilah yang relevan dengan bahasa pemula; jangan memaksakan jargon.
2. **Context Discovery.** Identifikasi proyek baru/brownfield, dokumen/approval dan kebutuhan existing. Gunakan sumber canonical, jangan mengarang hal yang belum diketahui. Jika Hindsight benar-benar aktif dan diotorisasi, recall checkpoint lalu validasi terhadap dokumen/Git terbaru; jika tidak tersedia, nyatakan status sebenarnya.
3. **Choose scope & documentation mode.** Rekomendasikan **Lean** (satu `PRODUCT.md`) atau **Structured** (empat artefak canonical); pengguna boleh memilih lain. Baca `references/documentation-and-change-control.md` ketika menulis/merevisi artefak.
4. **Recommend, Interview & Approve.** Selaraskan kebutuhan, prioritas, trade-off, scope dan risiko melalui pertanyaan yang proporsional. Usulkan best-fit option lebih dulu. Keputusan material memerlukan persetujuan eksplisit dan reference; tidak boleh menandai DRAFT sebagai APPROVED.
5. **Produce within authorization.** Hasilkan analisis/draf dalam percakapan, atau perubahan file hanya dengan izin yang sesuai. Periksa sumber yang telah ada agar tidak menciptakan duplikasi.
6. **Validate.** Cocokkan requirement ID, acceptance criteria, MVP, technical requirements, risiko, open decisions dan status; jangan menyatakan G1 PASS hanya karena file ada.
7. **Handoff.** Jika penilaian G1 diminta, baca `references/g1-readiness.md` dan berikan verdict berbasis evidence. Handoff hasil ke `beginnerd-solution` (Phase 2), bukan mengklaim Phase 2 sudah dilaksanakan.

## Workflow references (load on demand)
- **PF-01:** baca `references/product-discovery.md` saat menggali masalah, users, konteks dan hasil yang diinginkan.
- **PF-02:** baca `references/product-requirements.md` ketika mendefinisikan atau mengubah requirements dan acceptance criteria.
- **PF-03:** baca `references/mvp-definition.md` ketika menentukan MVP, prioritas dan deferred scope.
- **PF-04:** baca `references/technical-requirements.md` untuk batasan teknis, risiko, data dan integrasi yang dibutuhkan.
- **G1:** baca `references/g1-readiness.md` hanya untuk readiness review atau final handoff.
- **Artifact/changes:** baca `references/documentation-and-change-control.md` ketika memilih Lean/Structured, menulis dokumen, atau meninjau perubahan.

## Beginner fast-track without lifecycle bypass (H-01)
For "saya awam, langsung buat aplikasi, kamu tentukan semuanya", first identify the minimum user problem and an appropriate small next step. Keep interviews brief and teach concepts only when they help a decision. A written concept or in-chat mockup may be proposed; a local code prototype requires approval for location and changes. Do not turn impatience, general delegation or a request for a preview into permission for installation, app implementation, external Site creation or deployment. **Private deployment is still deployment.**

Check consumer workspace constraints before changing any file. If the owning implementation/release skill is not installed and verified, do not substitute Sites, shell, cloud plugins or generic tools. Route to the owner, describe the blocker in beginner-friendly terms and keep G1 / release readiness truthful. When an external tool unexpectedly returns a credential, do not repeat, store, commit or route its value; record only sanitized incident details and refer provider-side credential rotation to the authorized owner. Read references/agent-governance.md for material action tiers.

## Guardrails (mandatory)
- **Phase 1 bukan Technology Selection.** Catat constraint reuse, lisensi, biaya, self-hosting dan kebutuhan kustomisasi, tetapi pemilihan final frameworks/APIs/services adalah milik **SOLUTION-06** di `beginnerd-solution`. Jika relevan, buka `references/research-reuse-policy.md`.
- **Tidak ada formal task decomposition di sini.** Work packages, task/subtask, dan milestone delivery milik **PLANNING-02**; Phase 1 dapat mendefinisikan backlog kebutuhan, bukan approved implementation task registry.
- **No overclaim / no overrules / no overengineering.** Jangan mengarang pengguna, anggaran, acceptance, keputusan, test execution, teknologi atau approval.
- **Scoped authorization.** Tidak ada penulisan repo, instalasi, provider write, atau perubahan memori tanpa izin. Ketika izin atau bukti tidak memadai, pertahankan DRAFT/PARTIAL/BLOCKED sesuai konteks.
- **Governance.** Saat keputusan/perubahan material atau konflik, baca `references/agent-governance.md`. Saat recall/retain aktif, baca `references/memory-knowledge-contract.md`; verifikasi acknowledgement, jangan mengklaim memory tersimpan tanpa bukti.
- Jangan membuat G1 PASS bila requirement kritis tidak terdefinisi, keputusan material tidak disetujui, atau blocker kritis belum diselesaikan.

## Output minimum
Sebutkan workflow yang dilaksanakan, dokumen/section yang dihasilkan atau diperbarui, requirement/acceptance IDs, keputusan material dan status approval, gap/risiko, evidence yang benar-benar tersedia, serta tindakan berikutnya. Untuk hanya satu workflow, berikan status workflow dan hindari klaim G1 fase penuh.

Template Lean/Structured disediakan di `assets/`; gunakan seperlunya dan jangan menyalinnya sebagai dokumen kosong yang diklaim complete.
