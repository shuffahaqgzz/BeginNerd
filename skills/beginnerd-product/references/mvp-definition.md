# PF-03 — MVP Definition

**Trigger:** Tentukan batas MVP, fitur release pertama, prioritas, inclusion/exclusion, dan deferred features.

## Procedure
1. Periksa Product Brief, requirements/acceptance aktif, target user dan outcome. Jika PF-02 belum lengkap, dapat membuat **proposal** scope dengan gaps jelas, bukan menyebutnya approved.
2. Bagi fitur menjadi **MVP essential**, **deferred/later**, dan **out of scope** menggunakan nilai validasi, risiko, dependensi tingkat capability, kapasitas dan batasan user.
3. Setiap MVP item harus merujuk ID `REQUIREMENTS-...` dan acceptance yang dapat diuji; jangan mengarang stable ID untuk existing requirements sebelum mengecek collision.
4. Jelaskan alasan trade-off: nilai minimal yang bisa dipakai/diuji, biaya, risiko serta apa yang *tidak* disediakan MVP.
5. Berikan rekomendasi best-fit beserta alternatif ringkas; interview pengguna tentang keputusan prioritas material, scope exclusions dan konsekuensinya.
6. Catat approval reference, asumsi, risiko dan perubahan; hasil `MINIMUM-VIABLE-PRODUCT-SCOPE.md` (Structured) atau bagian MVP di `PRODUCT.md` (Lean).
7. Cek bahwa scope tidak kontradiktif dengan requirement dan technical constraints. Konflik kritis dapat menghasilkan G1 PARTIAL/BLOCKED.

## Boundary
- Phase 1 menentukan **kemampuan dan urutan prioritas produk**, bukan release planning berisi work packages, milestone engineering, atau formal task decomposition (PLANNING-01/02).
- Jangan mengklaim validasi pasar atau penerimaan user test nyata hanya karena MVP didesain.
