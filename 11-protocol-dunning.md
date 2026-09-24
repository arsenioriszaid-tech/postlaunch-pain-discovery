# PROTOKOL 2 — DUNNING CONCIERGE (pemulihan pembayaran gagal manual)
Format HP: kerja 15–30 mnt/hari. Tanpa kode, tanpa tool baru. Butuh: akses dashboard Stripe + email pelanggan (milikmu atau kolaborator yang memberi izin).

## 1. Objective
Mengukur Rp MRR nyata yang pulih dari failed-payment manual dalam 14 hari (sinyal) / 30–60 hari (keputusan), dan membunuhnya jika biaya > hasil.

## 2. Hypothesis
≥10% dari nilai failed-payment bisa pulih manual (retry + email 3x + link update kartu) dengan biaya <50% dari nilai pulih. Acuan luar: involuntary 20–35% churn mikro [35][239][240]; dunning menaikkan recovery 25–35%→55–70% [35]; benchmark cancel-flow selamatkan 15–25% [196] — semua klaim vendor, jadi angka-angka ini TARGET UJI, bukan fakta.

## 3. Inclusion / Exclusion
YA jika: SaaS langganan <$25k MRR, Stripe (atau dashboard tunjukkan gagal-bayar), ≥50 pelanggan bayar, ≥10 event gagal-bayar per 14 hari, ada akses kirim email ke pelanggan (kolaborator wajib izin tertulis/terekam).
TIDAK jika: >$50k MRR (beli Churnkey saja), <20 payer, tanpa akses dashboard/email, Stripe auto-retry agresif sudah aktif tanpa bisa dibedakan (tabrakan atribusi).

## 4. Target metric, baseline, sampel minimum
- Primer: **recovery rate** = Rp pulih / Rp gagal-diupayakan; **Rp MRR pulih**.
- Sekunder: jam kerja total; alasan gagal dominan (expired/insufficient/declined).
- Baseline: 7 hari pra-tes — hitung event gagal + Rp berisiko + berapa pulih sendiri (tanpa apa-apa).
- Sampel minimum: **10 event gagal** dalam jendela. Kurang → perpanjang 7 hari SEKALI → tetap kurang = NO-SIGNAL, stop.

## 5. Durasi
H0–H7 baseline · H1–H14 eksekusi (jadwal §6) · H14 baca sinyal · H30/H60 keputusan. Maksimal sinyal awal 14 hari sesuai permintaan.

## 6. Exact procedure (centang harian)
[ ] H0: matikan/dokumentasikan retry otomatis yang tabrakan (atau catat sebagai confounder). Siapkan link update-kartu (customer portal Stripe).
[ ] Setiap event gagal: catat (schema §7), JANGAN email di jam yang sama dengan email sistem.
[ ] H+1: retry manual 1x + Email 1 (pendek, manusiawi — template A bawah).
[ ] H+3: Email 2 + link update kartu (template B).
[ ] H+7: Email 3 terakhir, tawarkan jeda/pause 1 bulan sebagai alternatif cancel (template C).
[ ] H+12: retry terakhir. H14: tutup buku sinyal.
[ ] Jangan lebih dari 3 email per pelanggan. Nada: bantu, bukan tagih.

Template A (H+1): subjek "pembayaran [produk] gagal — 1 menit perbaiki" · isi: "Halo [nama], pembayaran [paket RpX] tanggal [tgl] gagal ([alasan bank]). Akunmu tetap aktif sampai [tgl]. Perbarui di sini: [link]. Balas email ini kalau butuh bantuan."
Template B (H+3): "pengingat: akses [fitur] terhenti [tgl] jika belum diperbarui — [link]. Mau jeda 1 bulan? balas 'jeda'."
Template C (H+7, terakhir): "terakhir dari saya — perbarui [link] atau balas 'jeda'/'berhenti'. Kalau berhenti, boleh tahu satu alasan? (satu kalimat cukup)."

## 7. Tracking schema (satu baris per event)
`id | tgl-gagal | pelanggan | paket-Rp | alasan-bank | email1/2/3 (tgl) | retry (tgl+hasil) | status (pulih/gagal-menunggu/hilang) | tgl-pulih | menit-kerja`
Ringkasan: recovery-rate, Rp pulih, total menit, alasan dominan.

## 8. Kill / success / continue
- KILL: recovery <10% di H14, ATAU biaya (menit × nilai-jam) >50% Rp pulih, ATAU event <10 setelah perpanjangan. → stop. Klaim VH2b mati untuk segmen ini.
- SUCCESS → CONTINUE: recovery ≥25% ATAU Rp pulih ≥ 3x biaya → lanjut H60, lalu bandingkan vs harga Churnkey $250/bln [159]: jika Rp-pulih-manual > $250/bln-ekuivalen dengan jam wajar → ada ruang produk; jika tidak → tetap concierge.
- NO-SIGNAL: catat, jangan paksa.

## 9. Confounders
Retry otomatis Stripe yang ikut pulih (atribusi!) · email sistem lain di hari sama · gelombang expired massal (akhir tahun/ganti kartu massal) · founder juga menghubungi (ganda) · pelanggan musiman.

## 10. Economic signal (ini output paling berharga)
Biaya: total menit × nilai jam + $0 tool. Hasil: Rp pulih + alasan-gagal dominan + % yang pilih jeda vs bayar vs pergi. Tulis perbandingan: "manual RpX/jam-kerja vs Churnkey $250/bln". Satu angka ini = jejak WTP indie yang tidak ada di riset mana pun.
