# BeginNerd

**Start with a vibe. Build with a plan. Learn along the way.**

*Guided Building for anyone building software with an AI coding agent.*

**Your agent, your stack, your project.** BeginNerd follows the open [Agent Skills](https://agentskills.io) format—not a Codex-only plugin. Bring it to **Claude Code, Codex, Cursor, OpenCode, Hermes Agent**, or another harness that knows how to load `SKILL.md`.

[Install](#mulai-di-agent-pilihanmu) · [Meet the skills](#kenalan-sama-skills-nya) · [How it works](#kenapa-beginnerd) · [Compatibility guide](docs/setup/MULTI-HARNESS-ADOPTION.md)

[![Static checks](https://github.com/shuffahaqgzz/BeginNerd/actions/workflows/validate.yml/badge.svg)](https://github.com/shuffahaqgzz/BeginNerd/actions/workflows/validate.yml) [![MIT](https://img.shields.io/badge/license-MIT-24292f)](LICENSE)

## Punya ide. Terus?

Kamu bilang ke AI, *"bikinin aplikasi ini."* Lima menit kemudian ada kode. Tapi siapa yang bakal pakai? Fitur mana yang benar-benar penting? Kenapa pilih teknologi itu? Dan kalau aplikasinya error, mulai cek dari mana?

**BeginNerd dibuat buat menjembatani ide dan aplikasi yang benar-benar bisa kamu pahami.**

Bukan AI yang mengambil alih semua keputusan. Bukan kursus yang mengharuskan kamu jago coding dulu. Ini kumpulan skill untuk membantu agent **bertanya, menjelaskan, merekomendasikan, merencanakan, membangun, dan memverifikasi**—dengan kamu tetap memegang kendali.

## Mulai di agent pilihanmu

BeginNerd tidak punya installer khusus. Pakai [Skills CLI](https://github.com/vercel-labs/skills) untuk menemukan dan memasang skill ke harness yang didukung. CLI saat ini membutuhkan **Node.js 22.20+**.

**Lihat dulu skill yang tersedia** (belum menginstal):

```bash
npx skills@latest add shuffahaqgzz/BeginNerd --list
```

**Pasang secara interaktif** ke agent yang kamu gunakan:

```bash
npx skills@latest add shuffahaqgzz/BeginNerd
```

Mau menentukan agent langsung? **Pilih satu baris**, bukan jalankan semuanya:

| Kamu pakai | Opsi Skills CLI |
| --- | --- |
| Claude Code | `-a claude-code` |
| Codex | `-a codex` |
| Cursor | `-a cursor` |
| OpenCode | `-a opencode` |
| Hermes Agent | `-a hermes-agent` |

Contohnya, untuk OpenCode:

```bash
npx skills@latest add shuffahaqgzz/BeginNerd -a opencode
```

Skills CLI memasang ke **project** secara default; opsi, jalur, dan cara agent memuatnya bisa berbeda. Jangan memasang paket yang sama dua kali lewat sistem plugin dan Skills CLI. Cek instalasi existing sebelum menimpa konfigurasi atau skill buatanmu.

**Lebih suka Hermes native?** Hermes punya Skills Hub dan GitHub taps sendiri:

```bash
hermes skills tap add shuffahaqgzz/BeginNerd
hermes skills search beginnerd
hermes skills install shuffahaqgzz/BeginNerd/beginnerd-ask
```

Ini **alternatif**, bukan langkah tambahan setelah instalasi lewat Skills CLI. Untuk project-local skills Hermes, review dulu repo-nya lalu gunakan `hermes skills trust` ketika diperlukan. Panduan [multi-harness adoption](docs/setup/MULTI-HARNESS-ADOPTION.md) menjelaskan perbedaan keduanya dan cara setup harness lain.

## Coba ngobrol dengan BeginNerd

Nggak perlu menghafal semua workflow. Di agent pilihanmu, mulai saja dengan:

> "Gue punya ide aplikasi, tapi belum tahu mulai dari mana. Bantu gue cari kebutuhan yang paling penting pakai BeginNerd."

Atau ketika masuk ke project yang sudah ada:

> "Gunakan beginnerd-ask. Cek dulu konteks project ini, terus jelaskan langkah berikutnya. Jangan bikin ulang hal yang sudah ada."

`beginnerd-setup` bisa membantu memilih gaya pendampingan saat pertama kali. Graphify dan Hindsight hanya digunakan bila tersedia, dikonfigurasi, dan diizinkan; skill tidak otomatis memasang provider atau mengaktifkan memory.

## Kenalan sama skills-nya

**Dua companion** yang bisa menemani dari fase mana pun:

- [`beginnerd-ask`](skills/beginnerd-ask/SKILL.md) — "Gue harus mulai dari mana?" Memahami posisi project dan mengarahkan ke workflow yang tepat.
- [`beginnerd-setup`](skills/beginnerd-setup/SKILL.md) — Memilih cara dibimbing, mengecek instalasi existing, dan mengatur knowledge/memory bila disetujui.

**Enam lifecycle skills**, dari ide sampai aplikasi dipelihara:

| Skill | Pertanyaan yang dibantu |
| --- | --- |
| [`beginnerd-product`](skills/beginnerd-product/SKILL.md) | Sebenarnya mau bikin apa, buat siapa, dan apa isi MVP-nya? |
| [`beginnerd-solution`](skills/beginnerd-solution/SKILL.md) | Flow, desain, teknologi, data, dan keamanannya seperti apa? |
| [`beginnerd-plan`](skills/beginnerd-plan/SKILL.md) | Mana yang dikerjakan dulu, dan kapan kita tahu sudah selesai? |
| [`beginnerd-foundation`](skills/beginnerd-foundation/SKILL.md) | Repo, environment, tools, dan agent sudah siap? |
| [`beginnerd-implement`](skills/beginnerd-implement/SKILL.md) | Bagaimana mengerjakan task yang disetujui dan menguji hasilnya? |
| [`beginnerd-release`](skills/beginnerd-release/SKILL.md) | Bagaimana merilis, memantau, dan merawat aplikasi secara terkendali? |

Kamu **nggak harus mengulang enam fase** setiap kali memperbaiki bug kecil. Pilih pekerjaan yang relevan. BeginNerd membantu menjaga konteks dan keputusan sebelumnya.

## Kenapa BeginNerd?

**Understand before building.** Jangan buru-buru bikin sesuatu yang masalahnya belum dipahami.

**Recommend, don't overwhelm.** Agent boleh punya opsi, tapi kamu nggak perlu dihujani jargon.

**Research & reuse first.** Kalau solusi yang cocok sudah ada, nggak harus membuat semuanya dari nol.

**Build while learning.** Belajar melalui keputusan dan pekerjaan yang sedang kamu lakukan, bukan teori yang terpisah.

**Verify, don't just generate.** Kode yang tampak selesai belum tentu berfungsi. Pengujian dan bukti tetap penting.

Itulah **Guided Building**. Kamu tetap pegang setir; agent membantu menavigasi.

## Bekerja di platform lain, bukan berarti semua sudah teruji

Kedelapan skill menggunakan direktori `SKILL.md` beserta references dan templates yang bisa dipindahkan. **Format portable dan dukungan installer tidak sama dengan runtime acceptance.** Cara aktivasi, izin tools, fitur MCP, memory, dan sandbox dapat berbeda antar harness.

Saat ini BeginNerd dipublikasikan sebagai **public source preview**: source dan pemeriksaan statis tersedia, sementara tes penggunaan nyata lintas-harness serta Graphify/Hindsight end-to-end masih perlu diverifikasi. Lihat [compatibility & test matrix](docs/setup/MULTI-HARNESS-ADOPTION.md) atau [implementation status](docs/implementation/STATUS.md) untuk batas klaimnya.

## Mau lihat detailnya?

[Multi-harness setup](docs/setup/MULTI-HARNESS-ADOPTION.md) · [Quickstart](docs/setup/QUICKSTART.md) · [6 phases](docs/architecture/FRAMEWORK-ARCHITECTURE.md) · [32 workflows](docs/workflows/WORKFLOW-REGISTRY.md) · [Governance](docs/governance/AGENT-GOVERNANCE.md)

Open source under the [MIT License](LICENSE). Baca [Contributing](CONTRIBUTING.md) untuk ikut membantu dan [Security](SECURITY.md) untuk melaporkan masalah keamanan.
