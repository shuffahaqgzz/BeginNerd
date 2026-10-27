# Contributing to BeginNerd

Terima kasih sudah membantu mengembangkan BeginNerd. Repository ini sedang menjalani implementasi dan acceptance runtime bertahap; **jangan menganggap seluruh skills telah teruji atau siap deployment**.

## Kontrak kontribusi
- Usulkan perubahan melalui branch terpisah dan Pull Request; jangan push langsung ke `main` atau mengaktifkan auto-merge tanpa persetujuan maintainer.
- Pertahankan approved design: enam fase, delapan skill boundaries, 32 workflow responsibilities, dan ownership PLANNING-02 atas formal task decomposition.
- Pastikan setiap perubahan memiliki alasan, batas scope, dampak pada docs/tests, evidence, dan status kesiapan yang jujur.
- Research First / Reuse First; jangan instal dependency duplikat atau mengganti design baseline sepihak.
- Jangan commit secret, token, private memory, credential, data pengguna, atau evidence runtime yang belum disanitasi.

## Validasi lokal (static, bukan runtime)
```bash
python3 scripts/validate_repository.py
python3 scripts/build_portable_references.py --check
python3 scripts/validate_skill_packages.py
python3 -m unittest discover -s tests/contracts -p 'test_*.py' -v
```
Pengujian skill pada Codex/Graphify/Hindsight hanya boleh diklaim PASS berdasarkan execution trace, scope authorization, attempted actions dan evidence yang dapat direview; CI statis saja tidak cukup.

## Jenis perubahan
Perbaikan dokumentasi/source/kontrak diperbolehkan melalui PR terarah. Perubahan material pada requirements, architecture, work structure, integration, deployment, atau risk acceptance harus mengikuti approved decision ownership, scoped authorization, dan review.

## Perubahan dan lisensi
Dengan berkontribusi, Anda harus memiliki hak atas kontribusi tersebut dan memahami bahwa kontribusi yang diterima di repository ini didistribusikan di bawah [MIT License](LICENSE). Komponen pihak ketiga tetap tunduk pada lisensinya. Tidak ada CLA atau DCO tambahan yang diwajibkan dalam file ini.

## Laporan kerentanan
Hindari memublikasikan exploit, token, atau kelemahan yang belum diperbaiki dalam issue/PR publik. Kanal disclosure privat perlu ditetapkan dan dikonfirmasi maintainer sebelum siap-rilis; lihat `docs/implementation/PUBLICATION-READINESS.md`.
