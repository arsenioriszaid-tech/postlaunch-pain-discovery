# H0 PACK — DUNNING GUIDEJAR (kirim 1 pesan, catat, tunggu)

## VERIFIKASI SILANG (cross-check 24 Sep 2026 — baca ini dulu)
| Klaim di pesan | Status | Sumber |
|---|---|---|
| "$5K+ MRR" | ✅ AMAN (konservatif) | Milestone founder sendiri: $5K Des 2025 [320], $5.7K Jan 2026 [299]; tracker: $5.1K flat [321] |
| "solo" | ✅ | Profil + postingan IH berulang "solo founder" [261][328] |
| Stripe (untuk H0, bukan pesan) | ✅ | TrustMRR: data ditarik via read-only API provider, bukan self-report [323][324][326]; halaman GuideJar: "verified with Stripe API key", update 22 Sep 2026 [322] |
| Founder aktif/terjangkau | ✅ kanal ADA, ⚠️ respons tak pasti | IH @Shrivatz aktif [328]; ARRfounder build-in-public [299]; X ~2.8k followers (via halaman TrustMRR); produk shipping Mar 2026 (Voice Cloning) [327] |
| PulseMRR $5.1K/235 subs | ⚠️ TURUNAN — PulseMRR eksplisit TIDAK verifikasi sendiri, datanya dari TrustMRR [325]. Jangan kutip sebagai sumber independen. Angka 235 subs = dari sini, pakai dengan flag. |
| Last-30d $5.9K→$8.2K→$7.5K (berubah tiap crawl) | ⚠️ FLUKTUATIF — ini revenue-30-hari (termasuk one-off/trial), BUKAN MRR. Jangan pernah tulis angka ini sebagai "MRR". Pesan hanya klaim "$5K+ MRR" — benar di semua snapshot. |
| "churn remains a challenge" | ✅ kata founder sendiri Jan 2026 [299] — JANGAN pakai di pesan pertama (terdengar menguntit); simpan untuk follow-up jika dia bertanya "kenapa saya?" |

Status H0 message: LOLOS — setiap kata faktual terverifikasi. Satu-satunya klaim dinamis (MRR kini) dibatasi "$5K+" yang didukung 4 sumber independen.

## H0 checklist (HP, 15 menit)
[ ] Kirim PESAN 1 (bawah) ke Shri via X DM @shri_vatz ATAU reply publik di thread terbarunya (pilih SATU kanal).
[ ] Catat tanggal kirim: __________.
[ ] Jika 4 hari tanpa respons: kirim PENGINGAT (bawah). Setelah itu STOP total — lanjut ke T2 KeepTheScore.
[ ] Jika YA: minta 3 angka (berapa failed-payment/14 hari? retry otomatis aktif? boleh akses dashboard read-only + kirim email atas namanya?) → isi baseline → mulai H1–H14 per `11-protocol-dunning.md`.
[ ] Jika TIDAK: catat alasan (1 baris) → pindah T2. Penolakan = data (WTP negatif parsial).

## PESAN 1 (copy-paste, Inggris, ≤100 kata)
> Hi Shri — congrats on $5K+ MRR, solo. I'm running a tiny experiment across micro-SaaS: free manual failed-payment recovery for 14 days (I check Stripe fails, retry + send max 3 polite emails per customer under your name, you keep 100% recovered). Costs you ~15 min total (read-only dashboard access + permission). Happy to share all numbers either way. Interested? If not, no worries at all.

## PENGINGAT (H+4, sekali saja)
> Quick bump in case this got buried — happy with a yes/no either way. 🙂

## Yang TIDAK boleh
- Jangan follow-up lebih dari 1x. Jangan tawarkan bayaran/jasa lain. Jangan sebut "AI agent/produk". Jangan kirim dari akun anonim — pakai identitasmu sendiri.
- Saya (Hermes) TIDAK mengirim apa pun — pengiriman = tanganmu.

## Baseline yang diminta jika YA (isi sebelum H1)
`prosesor | subs-aktif | gagal-bayar/14hr (event + Rp) | retry-otomatis (ya/tidak) | akses (dashboard/email) | mulai-tgl`
File catat harian: `evidence/guidejar-log.csv` (schema = protokol §7).
