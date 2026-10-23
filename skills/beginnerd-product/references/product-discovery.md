# PF-01 — Product Discovery

**Trigger:** Ide produk belum jelas, target pengguna/masalah perlu diverifikasi, atau Product Brief perlu direvisi. Gunakan dalam Phase 1 saja.

## Inputs
Ide/masalah dari user; konteks existing/brownfield; tujuan bisnis; pengguna/aktor; batasan wilayah, bahasa, channel, privacy atau sumber data; keputusan dan sumber yang sudah disetujui bila ada.

## Procedure
1. Jelaskan secara singkat apa itu discovery dan manfaatnya; buat asumsi eksplisit, bukan fakta.
2. Temukan siapa pengguna yang terdampak, masalah yang dialami, cara kerja sekarang, konsekuensinya, dan mengapa solusi diperlukan. Ajukan pertanyaan kecil yang relevan; hindari survei panjang jika informasi cukup.
3. Bedakan **facts supplied**, **assumptions**, **hypotheses to validate**, dan **open decisions**. Jika brownfield, baca brief/repo existing sebelum menawarkan produk baru.
4. Rekomendasikan rumusan problem, target outcomes, batasan, dan indikator keberhasilan yang dapat diamati. Jangan membuat target angka atau deadline tanpa dasar.
5. Identifikasi *reuse context* (existing software/service, asset, lisensi, self-hosting, biaya, customisasi) sebagai constraint untuk PF-02 dan SOLUTION-06, **bukan keputusan teknologi final**.
6. Jelaskan opsi bila ada ambiguitas material; lakukan interview dan catat keputusan pengguna.
7. Hasilkan/update **Product Brief** dalam `PRODUCT.md` (Lean) atau `PRODUCT-BRIEF.md` (Structured). Baca aturan dokumentasi dan template hanya ketika output akan ditulis.
8. Periksa bahwa pengguna, masalah, outcome, scope awal, dan unresolved assumptions terpisah jelas.

## Verification / exit
- Problem, sasaran pengguna, outcome dan batasan diketahui atau diberi label `UNKNOWN`/`PENDING`.
- Pilihan material tidak diam-diam dianggap approved.
- Hasil relevan dapat dipakai PF-02; bila hanya PF-01 diminta, jangan membuat PRD/MVP/TRD otomatis.
