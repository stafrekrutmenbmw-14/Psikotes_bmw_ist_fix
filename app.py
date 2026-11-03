import streamlit as st
import pandas as pd
import os
from datetime import datetime

# Impor modul Subtes 1 - 6
from subtests.subtest_1_se import render_subtest_1_se
from subtests.subtest_2_wa import render_subtest_2_wa
from subtests.subtest_3_an import render_subtest_3_an
from subtests.subtest_4_ge import render_subtest_4_ge
from subtests.subtest_5_ra import render_subtest_5_ra
from subtests.subtest_6_zr import render_subtest_6_zr

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Portal Psikotes IST - PT Bumi Mas Wahyu",
    page_icon="🧠",
    layout="wide"
)

RESULTS_FILE = "rekap_ist_lengkap.csv"
ADMIN_PASSWORD = "adminbmw"

# --- KUNCI JAWABAN RESMI IST (SUBTES 1 - 3, 5, 6) ---
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
    112: "80", 113: "14", 114: "12", 115: "63", 116: "10"
}

# --- KUNCI KATA KUNCI GE (SUBTES 4: SKOR 2 DAN SKOR 1) ---
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
        if kw in ans_clean: return 2
    for kw in GE_KEYS.get(q_id, {}).get(1, []):
        if kw in ans_clean: return 1
    return 0

def calculate_scores():
    user_answers = st.session_state.get("answers", {})
    
    score_se = sum(1 for q_id in range(1, 21) if user_answers.get(q_id) == ANSWER_KEYS_MC.get(q_id))
    score_wa = sum(1 for q_id in range(21, 41) if user_answers.get(q_id) == ANSWER_KEYS_MC.get(q_id))
    score_an = sum(1 for q_id in range(41, 61) if user_answers.get(q_id) == ANSWER_KEYS_MC.get(q_id))
    score_ge = sum(calculate_ge_score(q_id, user_answers.get(q_id)) for q_id in range(61, 77))
    score_ra = sum(1 for q_id in range(77, 97) if str(user_answers.get(q_id, '')).strip() == ANSWER_KEYS_MC.get(q_id))
    score_zr = sum(1 for q_id in range(97, 117) if str(user_answers.get(q_id, '')).strip() == ANSWER_KEYS_MC.get(q_id))
    
    total_raw = score_se + score_wa + score_an + score_ge + score_ra + score_zr
    return {
        "Subtes_1_SE": score_se,
        "Subtes_2_WA": score_wa,
        "Subtes_3_AN": score_an,
        "Subtes_4_GE": score_ge,
        "Subtes_5_RA": score_ra,
        "Subtes_6_ZR": score_zr,
        "Total_Raw_Score": total_raw
    }

# --- SIDEBAR NAVIGASI SISTEM ---
st.sidebar.title("📌 Navigasi Sistem")
mode = st.sidebar.radio("Pilih Akses:", ["Portal Tes Pelamar", "Dashboard Admin HRD"])

if "page" not in st.session_state: st.session_state.page = "register"
if "current_subtest" not in st.session_state: st.session_state.current_subtest = 1
if "user_info" not in st.session_state: st.session_state.user_info = {}
if "answers" not in st.session_state: st.session_state.answers = {}
if "admin_logged_in" not in st.session_state: st.session_state.admin_logged_in = False
if "saved" not in st.session_state: st.session_state.saved = False

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
                        "nama": nama, "email": email, "no_hp": no_hp,
                        "posisi": posisi, "tanggal": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
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
            st.session_state.page = "result"
            st.rerun()

    elif st.session_state.page == "result":
        st.title("✅ Seluruh Subtes 1 - 6 Selesai")
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
            else: st.error("Kata sandi salah!")
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

            st.subheader("📋 Rekapitulasi Hasil IST Subtes 1 - 6")
            st.dataframe(df_display, use_container_width=True)

            csv_data = df_display.to_csv(index=False, sep=';', encoding='utf-8-sig').encode('utf-8-sig')
            st.download_button(
                label="📥 Unduh Rekap Hasil Ujian (Format Excel / CSV)",
                data=csv_data,
                file_name=f"rekap_ist_bmw_{datetime.now().strftime('%Y%m%d')}.csv",
                mime='text/csv'
            )
📄 2. Modul Subtes 4: subtests/subtest_4_ge.py (8 Menit, 16 Soal)
(Simpan di folder subtests/)
import streamlit as st
import streamlit.components.v1 as components
import time

def show_live_timer_ge(seconds_remaining):
    components.html(f"""
    <div style="font-family: Arial, sans-serif; font-size: 20px; font-weight: bold; color: #d9534f; 
                background-color: #fdf7f7; padding: 10px 15px; border: 2px solid #d9534f; 
                border-radius: 8px; text-align: center; margin-bottom: 10px;">
        ⏱️ SISA WAKTU SUBTES 4 (GE): <span id="timer_display_ge">--:--</span>
    </div>
    <script>
        var timeLeft = {seconds_remaining};
        function updateDisplay() {{
            var m = Math.floor(timeLeft / 60);
            var s = timeLeft % 60;
            var displayM = m < 10 ? "0" + m : m;
            var displayS = s < 10 ? "0" + s : s;
            var elem = document.getElementById("timer_display_ge");
            if (elem) {{ elem.innerHTML = displayM + ":" + displayS; }}
            if (timeLeft <= 0) {{ if (elem) elem.innerHTML = "00:00 (WAKTU HABIS)"; }}
            else {{ timeLeft--; }}
        }}
        updateDisplay();
        setInterval(updateDisplay, 1000);
    </script>
    """, height=75)

def render_subtest_4_ge():
    if "step_ge" not in st.session_state:
        st.session_state.step_ge = "instruction"
    if "answers" not in st.session_state:
        st.session_state.answers = {}

    if st.session_state.step_ge == "instruction":
        st.title("📑 Petunjuk Subtes 04: GE (Kesamaan Kata)")
        st.info("💡 Bacalah seluruh petunjuk dan contoh di bawah ini. **Timer belum berjalan di halaman ini.**")
        st.markdown("""
        ### Aturan Pengerjaan:
        Ditentukan dua kata. Carilah **satu perkataan** yang meliputi pengertian kedua kata tadi! 
        Ketikkan jawaban Anda pada kolom yang telah disediakan.

        ---
        ### Contoh 01:
        **Ayam – Itik**  
        Perkataan *"burung"* dapat meliputi pengertian kedua kata itu.  
        **Jawaban:** **burung**

        ---
        ### Contoh 02:
        **Gaun – Celana**  
        Perkataan *"pakaian"* dapat meliputi pengertian kedua kata itu.  
        **Jawaban:** **pakaian**
        """)
        st.markdown("---")
        if st.button("Mulai Kerjakan Subtes 4 🚀", type="primary"):
            st.session_state.step_ge = "test"
            st.session_state.start_time_ge = time.time()
            st.rerun()

    elif st.session_state.step_ge == "test":
        st.title("🧠 Subtes 04: GE (Kesamaan Kata)")
        
        # Alokasi resmi Subtes 4 GE = 8 Menit (480 Detik)
        elapsed = int(time.time() - st.session_state.start_time_ge)
        remaining = max(0, 480 - elapsed)
        show_live_timer_ge(remaining)

        if remaining == 0:
            st.warning("⏰ Waktu Subtes 4 telah habis!")
            if st.button("Lanjut ke Subtes 5 (RA) ➔"):
                st.session_state.current_subtest = 5
                st.rerun()
            st.stop()

        questions_ge = [
            {"id": 61, "no": "61", "q": "mawar – melati"},
            {"id": 62, "no": "62", "q": "mata – telinga"},
            {"id": 63, "no": "63", "q": "gula – intan"},
            {"id": 64, "no": "64", "q": "hujan – salju"},
            {"id": 65, "no": "65", "q": "pengantar surat – telepon"},
            {"id": 66, "no": "66", "q": "kamera – kacamata"},
            {"id": 67, "no": "67", "q": "lambung – usus"},
            {"id": 68, "no": "68", "q": "banyak – sedikit"},
            {"id": 69, "no": "69", "q": "telur – benih"},
            {"id": 70, "no": "70", "q": "bendera – lencana"},
            {"id": 71, "no": "71", "q": "rumput – gajah"},
            {"id": 72, "no": "72", "q": "ember – kantong"},
            {"id": 73, "no": "73", "q": "awal – akhir"},
            {"id": 74, "no": "74", "q": "kikir – boros"},
            {"id": 75, "no": "75", "q": "penawaran – permintaan"},
            {"id": 76, "no": "76", "q": "atas – bawah"}
        ]

        with st.form("form_subtest_4"):
            for q in questions_ge:
                st.markdown(f"**Soal {q['no']}.** {q['q']}")
                st.session_state.answers[q['id']] = st.text_input(
                    f"Jawaban Kesamaan Kata No. {q['no']}:", 
                    key=f"ge_{q['id']}"
                )
                st.markdown("---")

            if st.form_submit_button("Simpan & Lanjut ke Subtes 5 (RA) ➔"):
                st.session_state.current_subtest = 5
                st.rerun()
