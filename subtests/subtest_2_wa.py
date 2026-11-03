import streamlit as st
import streamlit.components.v1 as components
import time

def show_live_timer_wa(seconds_remaining):
    components.html(f"""
    <div style="font-family: Arial, sans-serif; font-size: 20px; font-weight: bold; color: #d9534f; 
                background-color: #fdf7f7; padding: 10px 15px; border: 2px solid #d9534f; 
                border-radius: 8px; text-align: center; margin-bottom: 10px;">
        ⏱️ SISA WAKTU SUBTES 2 (WA): <span id="timer_display_wa">--:--</span>
    </div>
    <script>
        var timeLeft = {seconds_remaining};
        function updateDisplay() {{
            var m = Math.floor(timeLeft / 60);
            var s = timeLeft % 60;
            var displayM = m < 10 ? "0" + m : m;
            var displayS = s < 10 ? "0" + s : s;
            var elem = document.getElementById("timer_display_wa");
            if (elem) {{ elem.innerHTML = displayM + ":" + displayS; }}
            if (timeLeft <= 0) {{ if (elem) elem.innerHTML = "00:00 (WAKTU HABIS)"; }}
            else {{ timeLeft--; }}
        }}
        updateDisplay();
        setInterval(updateDisplay, 1000);
    </script>
    """, height=75)

def render_subtest_2_wa():
    if "step_wa" not in st.session_state:
        st.session_state.step_wa = "instruction"
    if "answers" not in st.session_state:
        st.session_state.answers = {}

    # TAHAP 1: INSTRUKSI & SELURUH CONTOH (TANPA TIMER)
    if st.session_state.step_wa == "instruction":
        st.title("📑 Petunjuk Subtes 02: WA (Mencari Kata Berbeda)")
        st.info("💡 Bacalah seluruh petunjuk dan contoh di bawah ini. **Timer belum berjalan di halaman ini.**")
        st.markdown("""
        ### Aturan Pengerjaan:
        Ditentukan 5 (lima) kata pada setiap soal. Pada 4 dari 5 kata itu terdapat suatu kesamaan. 
        Carilah 1 (satu) kata kelima yang **TIDAK memiliki kesamaan** dengan keempat kata lainnya!

        ---
        ### Contoh 01:
        * a) meja
        * b) kursi
        * c) burung
        * d) lemari
        * e) tempat tidur

        **Penjelasan:** a), b), d), dan e) adalah perabot rumah (*meubel*), sedangkan **c) burung** bukan perabot rumah.  
        **Jawaban yang benar:** **c) burung**

        ---
        ### Contoh 02:
        * a) duduk
        * b) berbaring
        * c) berdiri
        * d) berjalan
        * e) berjongkok

        **Penjelasan:** a), b), c), dan e) menunjukkan keadaan tidak bergerak, sedangkan **d) berjalan** menunjukkan keadaan bergerak.  
        **Jawaban yang benar:** **d) berjalan**
        """)
        st.markdown("---")
        if st.button("Mulai Kerjakan Subtes 2 🚀", type="primary"):
            st.session_state.step_wa = "test"
            st.session_state.start_time_wa = time.time()
            st.rerun()

    # TAHAP 2: PENGERJAAN SOAL (TIMER 6 MENIT BERJALAN)
    elif st.session_state.step_wa == "test":
        st.title("🧠 Subtes 02: WA (Mencari Kata Berbeda)")
        
        elapsed = int(time.time() - st.session_state.start_time_wa)
        remaining = max(0, 360 - elapsed)
        show_live_timer_wa(remaining)

        if remaining == 0:
            st.warning("⏰ Waktu Subtes 2 telah habis!")
            if st.button("Lanjut ke Subtes 3 (AN) ➔"):
                st.session_state.current_subtest = 3
                st.rerun()
            st.stop()

        questions_wa = [
            {"id": 21, "no": "21", "q": "Pilihlah satu kata yang tidak memiliki kesamaan:", "options": ["a) lingkaran", "b) panah", "c) elips", "d) busur", "e) lengkungan"]},
            {"id": 22, "no": "22", "q": "Pilihlah satu kata yang tidak memiliki kesamaan:", "options": ["a) mengetuk", "b) memaki", "c) menjahit", "d) menggergaji", "e) memukul"]},
            {"id": 23, "no": "23", "q": "Pilihlah satu kata yang tidak memiliki kesamaan:", "options": ["a) lebar", "b) keliling", "c) luas", "d) isi", "e) panjang"]},
            {"id": 24, "no": "24", "q": "Pilihlah satu kata yang tidak memiliki kesamaan:", "options": ["a) mengikat", "b) menyatukan", "c) melepaskan", "d) mengaitkan", "e) melekatkan"]},
            {"id": 25, "no": "25", "q": "Pilihlah satu kata yang tidak memiliki kesamaan:", "options": ["a) arah", "b) timur", "c) perjalanan", "d) tujuan", "e) selatan"]},
            {"id": 26, "no": "26", "q": "Pilihlah satu kata yang tidak memiliki kesamaan:", "options": ["a) jarak", "b) perpisahan", "c) tugas", "d) batas", "e) perceraian"]},
            {"id": 27, "no": "27", "q": "Pilihlah satu kata yang tidak memiliki kesamaan:", "options": ["a) saringan", "b) kelambu", "c) payung", "d) tapisan", "e) jala"]},
            {"id": 28, "no": "28", "q": "Pilihlah satu kata yang tidak memiliki kesamaan:", "options": ["a) putih", "b) pucat", "c) buram", "d) kasar", "e) berkilauan"]},
            {"id": 29, "no": "29", "q": "Pilihlah satu kata yang tidak memiliki kesamaan:", "options": ["a) otobis", "b) pesawat terbang", "c) sepeda motor", "d) sepeda", "e) kapal api"]},
            {"id": 30, "no": "30", "q": "Pilihlah satu kata yang tidak memiliki kesamaan:", "options": ["a) biola", "b) seruling", "c) klarinet", "d) terompet", "e) saxophon"]},
            {"id": 31, "no": "31", "q": "Pilihlah satu kata yang tidak memiliki kesamaan:", "options": ["a) bergelombang", "b) kasar", "c) berduri", "d) licin", "e) lurus"]},
            {"id": 32, "no": "32", "q": "Pilihlah satu kata yang tidak memiliki kesamaan:", "options": ["a) jam", "b) kompas", "c) penunjuk jalan", "d) bintang pari", "e) arah"]},
            {"id": 33, "no": "33", "q": "Pilihlah satu kata yang tidak memiliki kesamaan:", "options": ["a) kebijaksanaan", "b) pendidikan", "c) perencanaan", "d) penempatan", "e) pengerahan"]},
            {"id": 34, "no": "34", "q": "Pilihlah satu kata yang tidak memiliki kesamaan:", "options": ["a) bermotor", "b) berjalan", "c) berlayar", "d) bersepeda", "e) berkuda"]},
            {"id": 35, "no": "35", "q": "Pilihlah satu kata yang tidak memiliki kesamaan:", "options": ["a) gambar", "b) lukisan", "c) potret", "d) patung", "e) ukiran"]},
            {"id": 36, "no": "36", "q": "Pilihlah satu kata yang tidak memiliki kesamaan:", "options": ["a) panjang", "b) lonjong", "c) runcing", "d) bulat", "e) bersudut"]},
            {"id": 37, "no": "37", "q": "Pilihlah satu kata yang tidak memiliki kesamaan:", "options": ["a) kunci", "b) palang pintu", "c) gerendel", "d) gunting", "e) obeng"]},
            {"id": 38, "no": "38", "q": "Pilihlah satu kata yang tidak memiliki kesamaan:", "options": ["a) jembatan", "b) batas", "c) perkawinan", "d) pagar", "e) masyarakat"]},
            {"id": 39, "no": "39", "q": "Pilihlah satu kata yang tidak memiliki kesamaan:", "options": ["a) mengetam", "b) menasehati", "c) mengasah", "d) melicinkan", "e) menggosok"]},
            {"id": 40, "no": "40", "q": "Pilihlah satu kata yang tidak memiliki kesamaan:", "options": ["a) batu", "b) baja", "c) bulu", "d) karet", "e) kayu"]}
        ]

        with st.form("form_subtest_2"):
            for q in questions_wa:
                st.markdown(f"**Soal {q['no']}.** {q['q']}")
                st.session_state.answers[q['id']] = st.radio(
                    f"Pilih jawaban No. {q['no']}:", 
                    options=q['options'], 
                    key=f"wa_{q['id']}"
                )
                st.markdown("---")

            if st.form_submit_button("Simpan & Lanjut ke Subtes 3 (AN) ➔"):
                st.session_state.current_subtest = 3
                st.rerun()
