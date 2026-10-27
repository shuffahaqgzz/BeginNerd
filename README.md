# BeginNerd

**Start with a vibe. Build with a plan. Learn along the way.**

*Guided Building for vibe coders, beginner developers, and anyone who wants to build with AI without getting lost along the way.*

[Get started](#mulai-pakai-beginnerd) · [Meet the skills](#skill-nya-apa-aja) · [Why BeginNerd](#kenapa-beginnerd) · [Docs](#mau-ngulik-lebih-jauh)

[![Static checks](https://github.com/shuffahaqgzz/BeginNerd/actions/workflows/validate.yml/badge.svg)](https://github.com/shuffahaqgzz/BeginNerd/actions/workflows/validate.yml) [![MIT License](https://img.shields.io/badge/license-MIT-24292f)](LICENSE)

## Punya ide. Terus?

Kamu buka AI coding agent, ketik *"bikinin aplikasi ini"*, lalu kode mulai bermunculan.

Tapi siapa penggunanya? Fitur mana yang penting? Kenapa pakai teknologi itu? Dan gimana kamu tahu aplikasinya **benar-benar bekerja**?

**BeginNerd ada buat bagian yang sering kelewat itu.**

Ini kumpulan [Agent Skills](https://agentskills.io) yang menemani proses bikin aplikasi: dari ide yang masih acak, jadi kebutuhan yang jelas, desain yang masuk akal, pekerjaan yang bisa diikuti, sampai pengujian dan release.

Bukan autopilot yang mengambil semua keputusan. Bukan juga kursus programming yang harus kamu tamatkan sebelum mulai. Kamu tetap yang menentukan arah; agent membantu menjelaskan pilihan, memberi rekomendasi, dan mengerjakan hal yang sudah disepakati.

## Mulai pakai BeginNerd

Pakai **Codex**? Kamu bisa mulai dari project yang ingin dibangun. Butuh Node.js untuk menjalankan [Skills CLI](https://github.com/vercel-labs/skills) (versi CLI saat ini membutuhkan Node.js 22.20+).

**1. Lihat dulu skill yang tersedia**

```bash
npx skills@latest add shuffahaqgzz/BeginNerd --list
```

**2. Tambahkan ke project Codex-mu**

```bash
npx skills@latest add shuffahaqgzz/BeginNerd -a codex
```

Pilih skill yang ingin dipasang saat diminta. Instalasi default bersifat **project-scoped**, bukan global. Kalau sebelumnya sudah memasang BeginNerd, periksa dulu supaya tidak membuat salinan ganda atau menimpa konfigurasi yang kamu ubah sendiri.

**3. Ajak agent ngobrol**

> "Gue punya ide aplikasi, tapi belum tahu mulai dari mana. Pakai BeginNerd buat bantu gue nemuin kebutuhan paling penting dulu."

Atau kalau sudah ada project:

> "Pakai beginnerd-ask. Cek project yang ada dan kasih tahu langkah masuk akal berikutnya. Jangan ulang dari awal kalau nggak perlu."

Mulai pertama kali? Minta `beginnerd-setup` membantu memilih gaya pendampingan dan memeriksa konfigurasi existing. Graphify dan Hindsight **tidak otomatis aktif** hanya karena skill sudah dipasang; setup provider memerlukan izin dan verifikasi tersendiri.

## Skill-nya apa aja?

**Dua teman buat mulai dan nggak tersesat:**

- [`beginnerd-ask`](skills/beginnerd-ask/SKILL.md) — "Sekarang gue harus ngapain?" Cari posisi project dan skill yang tepat.
- [`beginnerd-setup`](skills/beginnerd-setup/SKILL.md) — Pilih cara kamu ingin dibimbing, cek skill yang terpasang, dan siapkan knowledge/memory kalau diizinkan.

**Enam skill untuk perjalanan bikin aplikasi:**

| Skill | Bantu kamu menjawab |
| --- | --- |
| [`beginnerd-product`](skills/beginnerd-product/SKILL.md) | Apa yang mau dibangun, buat siapa, dan apa yang masuk MVP? |
| [`beginnerd-solution`](skills/beginnerd-solution/SKILL.md) | Pengalaman pengguna dan sistemnya sebaiknya bekerja seperti apa? |
| [`beginnerd-plan`](skills/beginnerd-plan/SKILL.md) | Kita kerjain apa dulu, dan gimana membuktikan tiap bagian selesai? |
| [`beginnerd-foundation`](skills/beginnerd-foundation/SKILL.md) | Repo, environment, dan coding agent sudah siap dipakai? |
| [`beginnerd-implement`](skills/beginnerd-implement/SKILL.md) | Gimana membangun dan mengetes pekerjaan yang sudah disetujui? |
| [`beginnerd-release`](skills/beginnerd-release/SKILL.md) | Apa yang diperlukan untuk merilis, memantau, dan merawat aplikasi? |

Nggak harus menjalankan enam fase setiap kali mau memperbaiki bug kecil. BeginNerd bisa membantu **satu langkah yang memang kamu butuhkan**, dengan tetap menjaga keputusan project sebelumnya.

## Kenapa BeginNerd?

**Understand before building.** Jangan buru-buru menghasilkan kode untuk masalah yang belum dipahami.

**Recommend, don't overwhelm.** Agent boleh punya banyak opsi; tugasnya membantu kamu memilih, bukan melempar semua jargon sekaligus.

**Build while learning.** Kamu belajar dari keputusan dan pekerjaan yang benar-benar sedang kamu lakukan.

**Verify, don't just generate.** Kode yang dihasilkan belum tentu bekerja. Tests, hasil nyata, dan feedback tetap penting.

Itulah yang kami sebut **Guided Building**.

Ada dua kebiasaan lain yang kami pertahankan: **research before building** dan **reuse before reinventing**. Kalau project sudah punya solusi yang cocok, nggak perlu membangun ulang hanya karena AI bisa.

## Masih berkembang, dan itu sengaja kami jelaskan

BeginNerd saat ini adalah **public source preview**. Delapan skill dan 32 workflow sudah tersedia di repository, serta pemeriksaan source otomatis sudah berjalan. Tapi pengujian perilaku lengkap di Codex, integrasi Graphify/Hindsight, dan studi kasus end-to-end masih dalam proses validasi.

Artinya kamu bisa **membaca, mencoba, mengutak-atik, dan ikut berkontribusi** sekarang—tanpa perlu menganggap semua jalur sudah production-proven.

Lihat [status implementasi](docs/implementation/STATUS.md) dan [rencana validasi nyata](docs/implementation/REAL-WORLD-E2E-VALIDATION.md) kalau ingin tahu mana yang sudah terbukti dan mana yang masih terbuka.

## Mau ngulik lebih jauh?

- [Cara setup dan verifikasi](docs/setup/QUICKSTART.md)
- [Cara kerja enam fase](docs/architecture/FRAMEWORK-ARCHITECTURE.md)
- [Workflow yang tersedia](docs/workflows/WORKFLOW-REGISTRY.md)
- [Kenapa agent punya batas kewenangan](docs/governance/AGENT-GOVERNANCE.md)

BeginNerd adalah open source dengan [MIT License](LICENSE). Kalau mau bantu memperbaiki skill, contoh, atau dokumentasi, lihat [Contributing](CONTRIBUTING.md). Untuk masalah keamanan, baca [Security Policy](SECURITY.md).

**Start small. Build something. Learn along the way.**
