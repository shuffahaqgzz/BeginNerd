# PF-02 — Product Requirements

**Trigger:** Pengguna meminta PRD, daftar kebutuhan fungsional/nonfungsional tingkat produk, prioritization, atau revisi requirement.

## Procedure
1. Inventaris sumber: Product Brief, kebutuhan existing, feedback/stakeholders, dokumen relevan. Jangan menimpa PRD brownfield yang masih valid.
2. Untuk setiap kebutuhan yang material, tulis: stable ID `REQUIREMENTS-001`, kebutuhan yang bisa dipahami pengguna, aktor/user goal, prioritas/criticality, asal informasi, kondisi/risiko, status dan acceptance.
3. Berikan acceptance criteria yang terobservasi dengan ID `ACCEPTANCE-CRITERIA-001`; termasuk error/negative scenarios yang relevan. Bedakan acceptance **planned** dari test **executed**.
4. Catat data dan personal/sensitive data yang akan diproses, hak akses dan high-level constraints; batasan detail security design adalah Phase 2.
5. Identifikasi constraints dari riset/reuse jika supplied (budget, license, hosting, existing components) tetapi **jangan memilih framework final atau memaksa research setiap fitur kecil**.
6. Jelaskan trade-off, cari konflik/duplikasi requirement, rekomendasikan prioritas, dan minta approval eksplisit atas keputusan material.
7. Update `PRODUCT.md` (Lean) atau `PRODUCT-REQUIREMENTS-DOC.md` (Structured); kaitkan REQUIREMENTS ↔ ACCEPTANCE. Status artefak tidak otomatis APPROVED.
8. Validasi kebutuhan kritis, konsistensi, dan open decisions sebelum handoff ke PF-03/PF-04.

## Avoid
- Requirement kabur seperti "sistem aman/cepat" tanpa kondisi yang bisa diterima dan dinilai.
- Menambah fitur dari asumsi agent tanpa persetujuan.
- Membuat task implementasi formal atau menganggap PRD telah menjadi izin coding.

## Completion
Requirement dan acceptance relevant dapat ditinjau; gap/unknown dinyatakan, bukan disembunyikan. PF-02 complete tidak otomatis G1 PASS.
