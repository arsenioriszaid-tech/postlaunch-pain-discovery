# PROTOKOL 1 — FUNNEL-FRICTION AUDIT (satu ask dihapus, trial→paid diukur)
Format HP: baca dari atas ke bawah, centang tiap kotak. Estimasi 30–60 mnt/hari.

## 1. Objective
Membuktikan/membunuh klaim: "satu permintaan pra-value yang mati menekan aktivasi; menghapusnya menaikkan trial→paid." Keluar dengan angka, bukan opini.

## 2. Hypothesis
Menghapus SATU ask pra-value yang **mati** (tidak memberi makan personalisasi maupun kualifikasi) menaikkan signup→aktivasi ≥20% relatif dan trial→paid ikut naik, diukur per segmen traffic. Ask **produktif** (komitmen, benih personalisasi, kualifikasi, retensi hilir) JANGAN disentuh — Yammer/dmgoi/Improvely membuktikan salah hapus = turun [227][228][230].

## 3. Inclusion / Exclusion
YA jika: produk live + alur signup/trial jelas; ≥30 signup/minggu (sinyal 14 hari); founder bisa ubah flow ATAU jalankan varian concierge manual; freeze perubahan lain selama tes.
TIDAK jika: <10 signup/minggu; traffic hanya dari satu ledakan launch; ada ganti harga/paket/launcing dalam 30 hari; ask yang diincar dipakai sales/CS untuk kualifikasi (tanya dulu).

## 4. Target metric, baseline, sampel minimum
- Primer: **trial→paid** (jika belum ada paid: signup→aktivasi/utilitas pertama).
- Sekunder: penyelesaian step yang diubah; trial→paid per segmen sumber traffic.
- Baseline: 7 hari pra-tes, catat per sumber (organik, referral, sosial, direct). Jangan campur.
- Sampel minimum realistis: **50 signup per varian** (total ~100). Di bawah itu: perpanjang 7 hari SEKALI, lalu stop dengan status NO-SIGNAL (bukan gagal).

## 5. Durasi (sinyal awal 7–14 hari)
H0–H7 baseline · H8–H21 tes (14 hari) · H22 baca aktivasi · H30–H45 baca paid (trial perlu matang). Keputusan lanjut/stop paling cepat H22 untuk aktivasi, H45 untuk paid.

## 6. Exact procedure (centang)
[ ] H0: pilih SATU ask. Uji mati-vs-produktif: "apakah jawaban ask ini mengubah apa yang user lihat/lakukan berikutnya, atau menyaring siapa yang layak?" Tidak → kandidat hapus. Tulis namanya: __________.
[ ] H0: bekukan SEMUA perubahan lain (copy, harga, email, ads). Satu variabel.
[ ] H0–H7: catat baseline per sumber (pakai schema §7).
[ ] H8: hapus/pindahkan ask ke PASCA-value (setelah user rasakan hasil pertama). Jika tidak bisa edit kode: varian concierge — layani 50% signup manual tanpa ask itu, catat manual.
[ ] H8–H21: catat harian, JANGAN intip tiap jam. Cek 2x/minggu.
[ ] H22: hitung lift relatif per segmen. H30–H45: hitung trial→paid.
[ ] Tulis keputusan (kill/continue) + tanggal. Selesai.

## 7. Tracking schema (satu baris per hari di catatan/lembar)
`tanggal | varian (A/B) | sumber | signup | selesai-step | aktivasi | paid (isi belakangan) | catatan (anomali: down, viral, dsb)`
Rumus: lift relatif = (varian − baseline) / baseline × 100%. Hitung PER SEGMEN, bukan gabungan (confounder sumber! [232]).

## 8. Kill / success / continue
- KILL: lift aktivasi <5% relatif, ATAU aktivasi naik tapi paid datar/turun (jebakan Yammer/Improvely), ATAU lift hilang di dalam segmen sumber. → stop, catat, jangan ulangi ask lain sebelum bedah sebab.
- SUCCESS → CONTINUE: lift aktivasi ≥20% relatif + arah paid positif dalam segmen. → permanenkan, lalu (dan hanya lalu) uji ask kedua.
- NO-SIGNAL: sampel <50/varian setelah perpanjangan → stop, catat sebagai no-signal.

## 9. Confounders (wajib cek sebelum klaim menang)
Campuran sumber berubah · musiman/hari-libur · perubahan bersamaan (langgar freeze) · efek novelty (minggu-1 tinggi lalu turun — minta 14 hari penuh) · maturasi trial (paid lag 2–4 minggu).

## 10. Economic signal (catat walau kecil)
Jam kerja × nilai jam kamu + biaya tool $0–50. Matematika ekspektasi: lift-aktivasi × trial→paid-baseline × ARPU × signup/bulan = Rp MRR/bulan potensial. Tulis angkanya — inilah "jejak uang" yang hilang di riset.
