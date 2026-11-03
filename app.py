import streamlit as st
import pandas as pd
import os
from datetime import datetime

# Impor modul Subtes 1 - 8 dari folder subtests
from subtests.subtest_1_se import render_subtest_1_se
from subtests.subtest_2_wa import render_subtest_2_wa
from subtests.subtest_3_an import render_subtest_3_an
from subtests.subtest_4_ge import render_subtest_4_ge
from subtests.subtest_5_ra import render_subtest_5_ra
from subtests.subtest_6_zr import render_subtest_6_zr
from subtests.subtest_7_fa import render_subtest_7_fa
from subtests.subtest_8_wu import render_subtest_8_wu

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Portal Psikotes IST - PT Bumi Mas Wahyu",
    page_icon="🧠",
    layout="wide"
)

RESULTS_FILE = "rekap_ist_lengkap.csv"
ADMIN_PASSWORD = "adminbmw"

# --- KUNCI JAWABAN RESMI IST (SUBTES 1-3, 5-8) ---
ANSWER_KEYS_MC = {
    # Subtes 1 (SE)
    1: "e) kewibawaan", 2: "c) boros", 3: "d) gempa bumi", 4: "d) khianat", 5: "d) kuku",
    6: "b) biasanya", 7: "c) lemak", 8: "a) lawan", 9: "e) hipotesis", 10: "b) sol",
    11: "c) kotak PPPK", 12: "d) 20", 13: "d) konservatif", 14: "e) selalu", 15: "c) 800",
    16: "a) kekuatan", 17: "b) biasanya", 18: "b) Bandung", 19: "c) kemungkinan menang", 20: "b) 130",

    # Subtes 2 (WA)
    21: "b) panah", 22: "b) memaki", 23: "d) isi", 24: "c) melepaskan", 25: "c) perjalanan",
    26: "c) tugas", 27: "c) payung", 28: "d) kasar", 29: "d) sepeda", 30: "a) biola",
    31: "e) lurus", 32: "a) jam", 33: "a) kebijaksanaan", 34: "b) berjalan", 35: "c) potret",
    36: "a) panjang", 37: "d) gunting", 38: "e) masyarakat", 39: "b) menasehati", 40: "c) bulu",

    # Subtes 3 (AN)
    41: "c) melupakan", 42: "e) sangkar", 43: "d) jalan raya", 44: "d) gelang", 45: "d) kubus",
    46: "a) menawarkan", 47: "d) tengik", 48: "b) sungai", 49: "e) pelindung", 50: "d) tukang emas",
    51: "c) nada", 52: "c) kelakar", 53: "c) suasana hati", 54: "c) sutra", 55: "d) panjang senar",
    56: "c) mutasi", 57: "c) es", 58: "d) dikikir", 59: "e) mikroskop", 60: "e) lautan api",

    # Subtes 5 (RA)
    77: "35", 78: "280", 79: "205", 80: "26", 81: "30",
    82: "70", 83: "45", 84: "50", 85: "84", 86: "78",
    87: "19", 88: "6", 89: "75", 90: "90", 91: "120",
    92: "17", 93: "36", 94: "5", 95: "48", 96: "1",

    # Subtes 6 (ZR)
    97: "27", 98: "25", 99: "27", 100: "15", 101: "46",
    102: "10", 103: "42", 104: "7", 105: "5", 106: "14",
    107: "8", 108: "14", 109: "45", 110: "63", 111: "12",
    112: "80", 113: "14", 114: "12", 115: "63", 116: "10",

    # Subtes 7 (FA - Pemilihan Bentuk)
    117: "a", 118: "c", 119: "d", 120: "b", 121: "d",
    122: "e", 123: "c", 124: "e", 125: "e", 126: "d",
    127: "d", 128: "b", 129: "d", 130: "c", 131: "b",
    132: "e", 133: "b", 134: "d", 135: "c", 136: "a",

    # Subtes 8 (WU - Benda Ruang)
    137: "a", 138: "c", 139: "d", 140: "e", 141: "a",
    142: "c", 143: "d", 144: "c", 145: "e", 146: "a",
    147: "b", 148: "d", 149: "e", 150: "b", 151: "d",
    152: "b", 153: "a", 154: "e", 155: "b", 156: "c"
}

# --- KUNCI KATA KUNCI GE (SUBTES 4) ---
GE_KEYS = {
    61: {2: ["bunga", "kembang", "perdu"], 1: ["tumbuhan", "tumbuh-tumbuhan", "tangkai", "harum"]},
    62: {2: ["alat indera", "indera", "panca indera"], 1: ["organ", "alat tubuh"]},
    63: {2: ["hablur", "kristal", "zat arang"], 1: ["berkilauan", "mengkilat", "bening"]},
    64: {2: ["musim", "cuaca"], 1: []},
    65: {2: ["pembawa berita", "alat perhubungan"], 1: ["telekomunikasi", "perhubungan", "komunikasi"]},
    66: {2: ["alat optik", "optik"], 1: ["lensa"]},
    67: {2: ["alat pencernaan", "perut", "isi perut", "pencernaan makanan"], 1: ["jalan makanan"]},
    68: {2: ["jumlah", "kuantitas", "penyebut jumlah", "penyertaan jumlah"], 1: ["mengukur", "ukuran"]},
    69: {2: ["bibit", "bakal", "embrio", "alat pembiak", "permulaan penghidupan"], 1: ["sel", "pembiakan"]},
    70: {2: ["simbol", "lambang", "tanda"], 1: ["nama", "tanda pengenal"]},
    71: {2: ["makhluk", "organism", "makhluk hidup"], 1: ["tumbuh", "ilmu hayat", "biologi"]},
    72: {2: ["wadah", "tempat pengisi", "tempat penyimpan", "tempat"], 1: ["alat", "tempat sesuatu", "benda"]},
    73: {2: ["pengertian waktu", "batas"], 1: ["waktu", "lamanya", "masa", "saat"]},
    74: {2: ["kata sifat", "watak", "sifat karakter"], 1: ["sifat"]},
    75: {2: ["regulator harga", "pengertian ekonomi"], 1: ["dagang", "pembelian", "penjualan", "niaga", "jual beli"]},
    76: {2: ["pengertian ruang", "penyebut ruang"], 1: ["arah", "tempat", "ruang", "letak", "penunjuk tempat", "penentuan daerah"]}
}

def calculate_ge_score(q_id, user_ans):
    if not user_ans:
        return 0
    ans_clean = str(user_ans).strip().lower()
    for kw in GE_KEYS.get(q_id, {}).get(2, []):
        if kw in ans_clean:
            return 2
    for kw in GE_KEYS.get(q_id, {}).get(1, []):
        if kw in ans_clean:
            return 1
    return 0

def calculate_scores():
    user_answers = st.session_state.get("answers", {})
    
    score_se = sum(1 for q_id in range(1, 21) if user_answers.get(q_id) == ANSWER_KEYS_MC.get(q_id))
    score_wa = sum(1 for q_id in range(21, 41) if user_answers.get(q_id) == ANSWER_KEYS_MC.get(q_id))
    score_an = sum(1 for q_id in range(41, 61) if user_answers.get(q_id) == ANSWER_KEYS_MC.get(q_id))
    score_ge = sum(calculate_ge_score(q_id, user_answers.get(q_id)) for q_id in range(61, 77))
    score_ra = sum(1 for q_id in range(77, 97) if str(user_answers.get(q_id, '')).strip() == ANSWER_KEYS_MC.get(q_id))
    score_zr = sum(1 for q_id in range(97, 117) if str(user_answers.get(q_id, '')).strip() == ANSWER_KEYS_MC.get(q_id))
    score_fa = sum(1 for q_id in range(117, 137) if str(user_answers.get(q_id, '')).strip().lower() == ANSWER_KEYS_MC.get(q_id))
    score_wu = sum(1 for q_id in range(137, 157) if str(user_answers.get(q_id, '')).strip().lower() == ANSWER_KEYS_MC.get(q_id))
    
    total_raw = score_se + score_wa + score_an + score_ge + score_ra + score_zr + score_fa + score_wu
    return {
        "Subtes_1_SE": score_se,
        "Subtes_2_WA": score_wa,
        "Subtes_3_AN": score_an,
        "Subtes_4_GE": score_ge,
        "Subtes_5_RA": score_ra,
        "Subtes_6_ZR": score_zr,
        "Subtes_7_FA": score_fa,
        "Subtes_8_WU": score_wu,
        "Total_Raw_Score": total_raw
    }

# --- SIDEBAR NAVIGASI SISTEM ---
st.sidebar.title("📌 Navigasi Sistem")
mode = st.sidebar.radio("Pilih Akses:", ["Portal Tes Pelamar", "Dashboard Admin HRD"])

if "page" not in st.session_state:
    st.session_state.page = "register"
if "current_subtest" not in st.session_state:
    st.session_state.current_subtest = 1
if "user_info" not in st.session_state:
    st.session_state.user_info = {}
if "answers" not in st.session_state:
    st.session_state.answers = {}
if "admin_logged_in" not in st.session_state:
    st.session_state.admin_logged_in = False
if "saved" not in st.session_state:
    st.session_state.saved = False

if mode == "Portal Tes Pelamar":
    if st.session_state.page == "register":
        st.title("🏛️ PT Bumi Mas Wahyu")
        st.subheader("Portal Psikotes Online - IST (Intelligenz-Struktur-Test)")
        st.info("Mohon isi data diri Anda dengan lengkap sebelum memulai ujian.")

        with st.form("form_registrasi_awal"):
            nama = st.text_input("Nama Lengkap:")
            email = st.text_input("Alamat Email:")
            no_hp = st.text_input("Nomor WhatsApp / HP:")
            posisi = st.text_input("Posisi yang Dilamar:", placeholder="Contoh: Staff Closing / Admin HR / Arsitek")

            btn_start = st.form_submit_button("Mulai Tes IST 🚀", type="primary")

            if btn_start:
                if not nama or not email or not no_hp or not posisi:
                    st.error("⚠️ Mohon isi seluruh data diri secara lengkap!")
                else:
                    st.session_state.user_info = {
                        "nama": nama,
                        "email": email,
                        "no_hp": no_hp,
                        "posisi": posisi,
                        "tanggal": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    }
                    st.session_state.page = "test"
                    st.session_state.current_subtest = 1
                    st.rerun()

    elif st.session_state.page == "test":
        st.caption(
            f"👤 Kandidat: **{st.session_state.user_info.get('nama', '')}** | "
            f"💼 Posisi: **{st.session_state.user_info.get('posisi', '')}**"
        )
        st.markdown("---")

        if st.session_state.current_subtest == 1:
            render_subtest_1_se()
        elif st.session_state.current_subtest == 2:
            render_subtest_2_wa()
        elif st.session_state.current_subtest == 3:
            render_subtest_3_an()
        elif st.session_state.current_subtest == 4:
            render_subtest_4_ge()
        elif st.session_state.current_subtest == 5:
            render_subtest_5_ra()
        elif st.session_state.current_subtest == 6:
            render_subtest_6_zr()
        elif st.session_state.current_subtest == 7:
            render_subtest_7_fa()
        elif st.session_state.current_subtest == 8:
            render_subtest_8_wu()
        elif st.session_state.current_subtest == 9:
            st.session_state.page = "result"
            st.rerun()

    elif st.session_state.page == "result":
        st.title("✅ Ujian Psikotes IST Selesai")
        st.success(f"Terima kasih **{st.session_state.user_info.get('nama', '')}**, jawaban Anda telah disimpan.")

        if not st.session_state.saved:
            scores = calculate_scores()
            record = {**st.session_state.user_info, **scores}
            df_new = pd.DataFrame([record])

            if os.path.exists(RESULTS_FILE):
                df_old = pd.read_csv(RESULTS_FILE, sep=';')
                df_final = pd.concat([df_old, df_new], ignore_index=True)
            else:
                df_final = df_new

            df_final.to_csv(RESULTS_FILE, index=False, sep=';', encoding='utf-8-sig')
            st.session_state.saved = True

        st.info("Data hasil ujian telah disinkronkan langsung ke Dashboard Rekrutmen HRD PT Bumi Mas Wahyu.")

elif mode == "Dashboard Admin HRD":
    st.title("🔐 Dashboard Rekrutmen HRD - PT Bumi Mas Wahyu")

    if not st.session_state.admin_logged_in:
        pwd = st.text_input("Masukkan Kata Sandi Admin HRD:", type="password")
        if st.button("Login HRD"):
            if pwd == ADMIN_PASSWORD:
                st.session_state.admin_logged_in = True
                st.rerun()
            else:
                st.error("Kata sandi salah!")
    else:
        st.sidebar.button("Logout Admin", on_click=lambda: st.session_state.update({"admin_logged_in": False}))

        if not os.path.exists(RESULTS_FILE):
            st.warning("Belum ada data kandidat yang menyelesaikan tes.")
        else:
            df_results = pd.read_csv(RESULTS_FILE, sep=';')
            col1, col2 = st.columns(2)
            col1.metric("Total Kandidat Tes", len(df_results))
            if "Total_Raw_Score" in df_results.columns:
                col2.metric("Rata-rata Skor Mentah", f"{df_results['Total_Raw_Score'].mean():.1f}")

            st.markdown("---")
            posisi_filter = st.selectbox("Filter Berdasarkan Posisi:", ["Semua Posisi"] + list(df_results["posisi"].unique()))
            df_display = df_results[df_results["posisi"] == posisi_filter] if posisi_filter != "Semua Posisi" else df_results

            st.subheader("📋 Rekapitulasi Hasil IST Subtes 1 - 8")
            st.dataframe(df_display, use_container_width=True)

            csv_data = df_display.to_csv(index=False, sep=';', encoding='utf-8-sig').encode('utf-8-sig')
            st.download_button(
                label="📥 Unduh Rekap Hasil Ujian (Format Excel / CSV)",
                data=csv_data,
                file_name=f"rekap_ist_bmw_{datetime.now().strftime('%Y%m%d')}.csv",
                mime='text/csv'
            )
