"""
Model kuantitatif Laporan Studi Kasus 4
"Armada Banyak, Pengiriman Tetap Terlambat"
Bidang: Supply Chain & Distribution

Seluruh angka pada laporan dihitung dari modul ini agar konsisten dan dapat diaudit.
Data yang berasal langsung dari studi kasus diberi label SUMBER KASUS.
Angka lain adalah ASUMSI yang dinyatakan eksplisit pada laporan.
"""

# ----------------------------------------------------------------------------
# 1. PARAMETER DASAR  (SUMBER KASUS)
# ----------------------------------------------------------------------------
KASUS = {
    "kendaraan": 20,                 # unit
    "jarak_per_kendaraan_hari": 150,  # km
    "hari_operasi_bulan": 26,
    "konsumsi_km_per_liter": 10,
    "harga_bbm": 10_000,             # Rp/liter (harga simulasi pada kasus)
    "target_pengurangan_jarak": 0.15,
    "batas_investasi": 150_000_000,  # Rp
}

# ----------------------------------------------------------------------------
# 2. ASUMSI  (dinyatakan eksplisit, diberi kode A1..A10)
# ----------------------------------------------------------------------------
ASUMSI = {
    "A1_hari_operasi_tahun": 26 * 12,          # 312 hari
    "A2_stop_per_kendaraan": 8,                # titik pengiriman/kendaraan/hari
    "A3_biaya_non_bbm_per_km": 5_000,          # Rp/km (pengemudi + penyusutan + perawatan + asuransi)
    "A4_tingkat_keterlambatan": 0.05,          # 5% kiriman di luar komitmen waktu
    "A5_biaya_per_kejadian_terlambat": 100_000,
    "A6_jumlah_dispatcher": 2,
    "A7_biaya_dispatcher_bulan": 7_000_000,
    "A8_porsi_waktu_perencanaan": 0.40,
    "A9_porsi_stop_menunggu": 0.20,
    "A10_jam_tunggu_per_stop": 0.4,
    "A11_jam_kerja_pengemudi_hari": 10,
    "A12_biaya_pengemudi_bulan": 10_000_000,
    "A13_faktor_emisi_diesel": 2.68,           # kg CO2e/liter
    "A14_diskonto": 0.12,                      # biaya modal tahunan
    "A15_horizon_evaluasi": 3,                 # tahun
}


def annuity(rate: float, years: int) -> float:
    """Faktor anuitas nilai sekarang (PVIFA)."""
    return (1 - (1 + rate) ** -years) / rate


# ----------------------------------------------------------------------------
# 3. BASELINE OPERASIONAL
# ----------------------------------------------------------------------------
def hitung_baseline():
    k = KASUS
    a = ASUMSI
    hari_tahun = a["A1_hari_operasi_tahun"]

    km_hari = k["kendaraan"] * k["jarak_per_kendaraan_hari"]
    km_bulan = km_hari * k["hari_operasi_bulan"]
    km_tahun = km_hari * hari_tahun

    liter_tahun = km_tahun / k["konsumsi_km_per_liter"]
    biaya_bbm_tahun = liter_tahun * k["harga_bbm"]
    biaya_bbm_bulan = biaya_bbm_tahun / 12

    biaya_non_bbm_tahun = km_tahun * a["A3_biaya_non_bbm_per_km"]
    biaya_transport_tahun = biaya_bbm_tahun + biaya_non_bbm_tahun

    kiriman_hari = k["kendaraan"] * a["A2_stop_per_kendaraan"]
    kiriman_tahun = kiriman_hari * hari_tahun

    terlambat_tahun = kiriman_tahun * a["A4_tingkat_keterlambatan"]
    biaya_terlambat_tahun = terlambat_tahun * a["A5_biaya_per_kejadian_terlambat"]

    biaya_dispatcher_tahun = a["A6_jumlah_dispatcher"] * a["A7_biaya_dispatcher_bulan"] * 12
    biaya_perencanaan_tahun = biaya_dispatcher_tahun * a["A8_porsi_waktu_perencanaan"]

    tarif_jam_pengemudi = a["A12_biaya_pengemudi_bulan"] / (k["hari_operasi_bulan"] * a["A11_jam_kerja_pengemudi_hari"])
    jam_tunggu_hari = kiriman_hari * a["A9_porsi_stop_menunggu"] * a["A10_jam_tunggu_per_stop"]
    biaya_tunggu_tahun = jam_tunggu_hari * tarif_jam_pengemudi * hari_tahun

    # Potensi penghematan bila jarak turun sesuai target kasus (15%)
    km_hemat_target = km_tahun * k["target_pengurangan_jarak"]
    liter_hemat_target = km_hemat_target / k["konsumsi_km_per_liter"]
    rp_hemat_bbm_target = liter_hemat_target * k["harga_bbm"]
    km_baru = km_tahun - km_hemat_target
    km_per_kendaraan_baru = km_baru / k["kendaraan"] / hari_tahun
    kendaraan_setara = km_hemat_target / k["jarak_per_kendaraan_hari"] / hari_tahun
    co2_hemat = liter_hemat_target * a["A13_faktor_emisi_diesel"] / 1000  # ton
    nilai_kapasitas = km_hemat_target * a["A3_biaya_non_bbm_per_km"]

    return {
        "km_hari": km_hari,
        "km_bulan": km_bulan,
        "km_tahun": km_tahun,
        "liter_tahun": liter_tahun,
        "biaya_bbm_tahun": biaya_bbm_tahun,
        "biaya_bbm_bulan": biaya_bbm_bulan,
        "biaya_non_bbm_tahun": biaya_non_bbm_tahun,
        "biaya_transport_tahun": biaya_transport_tahun,
        "km_per_liter": k["konsumsi_km_per_liter"],
        "kiriman_hari": kiriman_hari,
        "kiriman_tahun": kiriman_tahun,
        "terlambat_tahun": terlambat_tahun,
        "biaya_terlambat_tahun": biaya_terlambat_tahun,
        "biaya_dispatcher_tahun": biaya_dispatcher_tahun,
        "biaya_perencanaan_tahun": biaya_perencanaan_tahun,
        "tarif_jam_pengemudi": tarif_jam_pengemudi,
        "jam_tunggu_hari": jam_tunggu_hari,
        "biaya_tunggu_tahun": biaya_tunggu_tahun,
        "km_hemat_target": km_hemat_target,
        "liter_hemat_target": liter_hemat_target,
        "rp_hemat_bbm_target": rp_hemat_bbm_target,
        "km_baru": km_baru,
        "km_per_kendaraan_baru": km_per_kendaraan_baru,
        "kendaraan_setara": kendaraan_setara,
        "co2_hemat_ton": co2_hemat,
        "nilai_kapasitas": nilai_kapasitas,
        "km_per_kiriman": km_tahun / kiriman_tahun,
        "bbm_per_kiriman_liter": liter_tahun / kiriman_tahun,
        "biaya_transport_per_kiriman": biaya_transport_tahun / kiriman_tahun,
    }


BASE = hitung_baseline()


# ----------------------------------------------------------------------------
# 4. BIAYA AKIBAT MASALAH (COST OF POOR PERFORMANCE)
# ----------------------------------------------------------------------------
def hitung_biaya_masalah():
    return {
        "bbm_berlebih": BASE["rp_hemat_bbm_target"],
        "keterlambatan": BASE["biaya_terlambat_tahun"],
        "waktu_tunggu": BASE["biaya_tunggu_tahun"],
        "perencanaan_manual": BASE["biaya_perencanaan_tahun"],
        "total": (BASE["rp_hemat_bbm_target"] + BASE["biaya_terlambat_tahun"]
                  + BASE["biaya_tunggu_tahun"] + BASE["biaya_perencanaan_tahun"]),
    }


COST = hitung_biaya_masalah()


# ----------------------------------------------------------------------------
# 5. ALTERNATIF SOLUSI – STRUKTUR BIAYA & MANFAAT
# ----------------------------------------------------------------------------
ALTERNATIF = {
    "A1": {
        "nama": "Perbaikan Prosedur dan Tata Kelola Rute",
        "capex": 25_000_000,
        "opex": 24_000_000,
        "p_bbm": 0.05,        # pengurangan jarak/BBM
        "p_terlambat": 0.15,
        "p_perencanaan": 0.20,
        "p_tunggu": 0.10,
    },
    "A2": {
        "nama": "Aplikasi Optimasi Rute + Bukti Pengiriman Digital (standalone)",
        "capex": 115_000_000,
        "opex": 93_000_000,
        "p_bbm": 0.10,
        "p_terlambat": 0.30,
        "p_perencanaan": 0.30,
        "p_tunggu": 0.15,
    },
    "A3": {
        "nama": "Platform Distribusi Terintegrasi (TMS + Telematika + ERP)",
        "capex": 330_000_000,
        "opex": 156_000_000,
        "p_bbm": 0.15,
        "p_terlambat": 0.35,
        "p_perencanaan": 0.50,
        "p_tunggu": 0.20,
    },
    "A4": {
        "nama": "Hybrid Bertahap: Tata Kelola + Optimasi Rute + ETA (Rekomendasi)",
        "capex": 125_000_000,
        "opex": 99_000_000,
        "p_bbm": 0.13,
        "p_terlambat": 0.30,
        "p_perencanaan": 0.35,
        "p_tunggu": 0.18,
    },
}


def hitung_finansial(alt: dict, diskonto=None, tahun=None):
    diskonto = ASUMSI["A14_diskonto"] if diskonto is None else diskonto
    tahun = ASUMSI["A15_horizon_evaluasi"] if tahun is None else tahun

    manfaat = {
        "bbm": alt["p_bbm"] * BASE["rp_hemat_bbm_target"] / KASUS["target_pengurangan_jarak"],
        "keterlambatan": alt["p_terlambat"] * BASE["biaya_terlambat_tahun"],
        "perencanaan": alt["p_perencanaan"] * BASE["biaya_perencanaan_tahun"],
        "tunggu": alt["p_tunggu"] * BASE["biaya_tunggu_tahun"],
    }
    total_manfaat = sum(manfaat.values())
    arus_neto = total_manfaat - alt["opex"]
    pvifa = annuity(diskonto, tahun)
    npv = -alt["capex"] + arus_neto * pvifa
    payback = alt["capex"] / arus_neto if arus_neto > 0 else float("inf")
    total_neto = arus_neto * tahun - alt["capex"]
    roi = total_neto / alt["capex"]
    return {
        "manfaat": manfaat,
        "total_manfaat": total_manfaat,
        "arus_neto": arus_neto,
        "npv": npv,
        "pvifa": pvifa,
        "payback_tahun": payback,
        "payback_bulan": payback * 12,
        "roi_3th": roi,
        "total_neto_3th": total_neto,
        "rasio_manfaat_biaya": (total_manfaat * pvifa) / (alt["capex"] + alt["opex"] * pvifa),
        "kelebihan_anggaran": alt["capex"] - KASUS["batas_investasi"],
    }


FIN = {k: hitung_finansial(v) for k, v in ALTERNATIF.items()}


# ----------------------------------------------------------------------------
# 6. MATRIKS PENILAIAN (SKOR 1-5)
# ----------------------------------------------------------------------------
KRITERIA = [
    ("Dampak terhadap efisiensi jarak dan biaya", 0.25),
    ("Kualitas layanan dan visibilitas (OTIF/ETA)", 0.20),
    ("Kepatuhan terhadap batas investasi Rp150 juta", 0.15),
    ("Kelayakan implementasi dalam 90 hari", 0.15),
    ("Fleksibilitas operasional dan penerimaan pengguna", 0.15),
    ("Skalabilitas dan kesiapan integrasi data", 0.10),
]

SKOR = {
    "A1": [2, 2, 5, 5, 4, 2],
    "A2": [4, 4, 3, 4, 3, 3],
    "A3": [5, 5, 1, 1, 2, 5],
    "A4": [4, 4, 4, 3, 4, 4],
}


def skor_terbobot(kode):
    return sum(s * w for s, (_, w) in zip(SKOR[kode], KRITERIA))


SKOR_AKHIR = {k: skor_terbobot(k) for k in SKOR}

# Uji ketahanan: skenario bobot alternatif
BOBOT_SKENARIO = {
    "Basis (25/20/15/15/15/10)": [0.25, 0.20, 0.15, 0.15, 0.15, 0.10],
    "Bobot sama (16,7% per kriteria)": [1 / 6] * 6,
    "Bobot hasil diperbesar (K1 35%, K2 25%)": [0.35, 0.25, 0.15, 0.10, 0.10, 0.05],
    "Bobot eksekusi diperbesar (K3, K4, K5 = 20%)": [0.20, 0.15, 0.20, 0.20, 0.20, 0.05],
}

# Pemetaan ulang skor per skenario (skor tiap alternatif harus dihitung ulang
# karena urutan kriteria pada SKOR selalu [K1..K6])
SKENARIO_BOBOT_HASIL = {}
for nama, bobot in BOBOT_SKENARIO.items():
    SKENARIO_BOBOT_HASIL[nama] = {
        k: sum(s * w for s, w in zip(SKOR[k], bobot)) for k in SKOR
    }


# ----------------------------------------------------------------------------
# 7. ANALISIS SENSITIVITAS (TORNADO) UNTUK ALTERNATIF TERPILIH
# ----------------------------------------------------------------------------
def npv_a4(p_bbm=0.13, p_terlambat=0.30, opex_mult=1.0, p_tunggu=0.18, capex_mult=1.0):
    alt = dict(ALTERNATIF["A4"])
    alt.update(p_bbm=p_bbm, p_terlambat=p_terlambat, p_tunggu=p_tunggu,
               opex=ALTERNATIF["A4"]["opex"] * opex_mult,
               capex=ALTERNATIF["A4"]["capex"] * capex_mult)
    return hitung_finansial(alt)["npv"]


NPV_BASE = npv_a4()

SENSITIVITAS = [
    # (label, npv_rendah, npv_tinggi, nilai_rendah, nilai_tinggi)
    ("Pengurangan jarak/BBM (10% vs 15%)", npv_a4(p_bbm=0.10), npv_a4(p_bbm=0.15), "10%", "15%"),
    ("Penurunan keterlambatan (15% vs 40%)", npv_a4(p_terlambat=0.15), npv_a4(p_terlambat=0.40), "15%", "40%"),
    ("Biaya operasional sistem (-30% vs +30%)", npv_a4(opex_mult=1.3), npv_a4(opex_mult=0.7), "+30%", "-30%"),
    ("Penurunan waktu tunggu (8% vs 28%)", npv_a4(p_tunggu=0.08), npv_a4(p_tunggu=0.28), "8%", "28%"),
    ("Capex aktual (+20% vs -10%)", npv_a4(capex_mult=1.2), npv_a4(capex_mult=0.9), "+20%", "-10%"),
]
SENSITIVITAS.sort(key=lambda r: abs(r[2] - r[1]), reverse=True)

# Titik pulang pokok (break-even): arus neto minimum agar NPV = 0
BEP_ARUS_NETO = ALTERNATIF["A4"]["capex"] / annuity(ASUMSI["A14_diskonto"], ASUMSI["A15_horizon_evaluasi"])
BEP_MANFAAT = BEP_ARUS_NETO + ALTERNATIF["A4"]["opex"]
BEP_REALISASI = BEP_MANFAAT / FIN["A4"]["total_manfaat"]

# Skenario pesimistis gabungan
SKENARIO = {
    "Optimis": npv_a4(p_bbm=0.15, p_terlambat=0.40, opex_mult=0.9, p_tunggu=0.25),
    "Basis": NPV_BASE,
    "Pesimistis": npv_a4(p_bbm=0.10, p_terlambat=0.20, opex_mult=1.15, p_tunggu=0.12),
}


# ----------------------------------------------------------------------------
# 8. UTILITAS FORMAT ANGKA INDONESIA
# ----------------------------------------------------------------------------
def rp(x, desimal=0):
    return "Rp" + f"{x:,.{desimal}f}".replace(",", "X").replace(".", ",").replace("X", ".")


def juta(x, desimal=1):
    return f"Rp{x/1e6:,.{desimal}f}".replace(",", "X").replace(".", ",").replace("X", ".") + " jt"


def angka(x, desimal=0):
    return f"{x:,.{desimal}f}".replace(",", "X").replace(".", ",").replace("X", ".")


def persen(x, desimal=1):
    return f"{x*100:,.{desimal}f}".replace(".", ",") + "%"


if __name__ == "__main__":
    print("=" * 78)
    print("BASELINE")
    print("=" * 78)
    for k, v in BASE.items():
        print(f"{k:32s} {v:>18,.2f}")
    print("\n" + "=" * 78)
    print("BIAYA AKIBAT MASALAH (Rp/tahun)")
    print("=" * 78)
    for k, v in COST.items():
        print(f"{k:32s} {v:>18,.0f}")
    print(f"{'porsi thd belanja BBM':32s} {COST['total']/BASE['biaya_bbm_tahun']*100:>17,.1f}%")
    print(f"{'porsi thd biaya transport':32s} {COST['total']/BASE['biaya_transport_tahun']*100:>17,.1f}%")
    print("\n" + "=" * 78)
    print("FINANSIAL PER ALTERNATIF")
    print("=" * 78)
    for k, f in FIN.items():
        print(f"\n{k}  {ALTERNATIF[k]['nama']}")
        for kk, vv in f["manfaat"].items():
            print(f"   manfaat {kk:16s} {vv:>16,.0f}")
        print(f"   total manfaat      {f['total_manfaat']:>16,.0f}")
        print(f"   arus neto/tahun    {f['arus_neto']:>16,.0f}")
        print(f"   NPV 3 th @12%      {f['npv']:>16,.0f}")
        print(f"   payback (bulan)    {f['payback_bulan']:>16,.1f}")
        print(f"   ROI 3 tahun        {f['roi_3th']*100:>15,.0f}%")
        print(f"   B/C ratio          {f['rasio_manfaat_biaya']:>16,.2f}")
    print("\n" + "=" * 78)
    print("SKOR TERBOBOT")
    print("=" * 78)
    for k, v in SKOR_AKHIR.items():
        print(f"{k}: {v:.2f}   skor {SKOR[k]}")
    print("\n" + "=" * 78)
    print("SENSITIVITAS A4 (NPV basis = %.0f)" % NPV_BASE)
    print("=" * 78)
    for r in SENSITIVITAS:
        print(f"{r[0]:52s} {r[2]:>14,.0f} .. {r[1]:>14,.0f}")
    print("\nSkenario:")
    for k, v in SKENARIO.items():
        print(f"  {k:14s} NPV = {v:>16,.0f}")
