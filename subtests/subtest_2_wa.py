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
            if (timeLeft <= 0) {{ 
                if (elem) elem.innerHTML = "00:00 (WAKTU HABIS)"; 
                setTimeout(function() {{ window.parent.location.reload(); }}, 1000);
            }} else {{ 
                timeLeft--; 
            }}
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

    if st.session_state.step_wa == "instruction":
        st.title("📑 Petunjuk Subtes 02: WA (Mencari Kata Berbeda)")
        st.info("💡 Bacalah petunjuk di bawah ini dengan teliti. **Timer belum berjalan di halaman ini.**")
        st.markdown("""
        ### Aturan Pengerjaan:
        Ditentukan 5 kata. Empat dari 5 kata itu mempunyai kesamaan/kelompok tertentu. 
        Carilah **satu kata yang tidak memiliki kesamaan** dengan 4 kata lainnya.

        ---
        ### Contoh:
        a) meja | b) kursi | c) burung | d) lemari | e) tempat tidur  
        *Jawaban yang benar adalah* **c) burung** (karena yang lain adalah perabot rumah tangga).
        """)
        st.markdown("---")
        if st.button("Mulai Kerjakan Subtes 2 🚀", type="primary"):
            st.session_state.step_wa = "test"
            st.session_state.start_time_wa = time.time()
            st.rerun()

    elif st.session_state.step_wa == "test":
        st.title("🧠 Subtes 02: WA (Mencari Kata Berbeda)")
        
        elapsed = int(time.time() - st.session_state.start_time_wa)
        remaining = max(0, 360 - elapsed)
        show_live_timer_wa(remaining)

        if remaining <= 0:
            st.warning("⏰ Waktu Subtes 2 telah habis! Mengalihkan ke Subtes 3...")
            for q_id in range(21, 41):
                if f"wa_{q_id}" in st.session_state:
                    st.session_state.answers[q_id] = st.session_state[f"wa_{q_id}"]
            time.sleep(1)
            st.session_state.current_subtest = 3
            st.rerun()

        questions_wa = [
            {"id": 21, "no": "21", "opts": ["a) lingkaran", "b) panah", "c) elips", "d) busur", "e) lengkung"]},
            {"id": 22, "no": "22", "opts": ["a) mengetuk", "b) memaki", "c) menjatuhkan", "d) merusak", "e) memukul"]},
            {"id": 23, "no": "23", "opts": ["a) luas", "b) lebar", "c) panjang", "d) isi", "e) tinggi"]},
            {"id": 24, "no": "24", "opts": ["a) mengikat", "b) menyatukan", "c) melepaskan", "d) menyambung", "e) menggabungkan"]},
            {"id": 25, "no": "25", "opts": ["a) arah", "b) timur", "c) perjalanan", "d) utara", "e) selatan"]},
            {"id": 26, "no": "26", "opts": ["a) janji", "b) kontrak", "c) tugas", "d) persetujuan", "e) ikatan"]},
            {"id": 27, "no": "27", "opts": ["a) topi", "b) helm", "c) payung", "d) peci", "e) mahkota"]},
            {"id": 28, "no": "28", "opts": ["a) licin", "b) rata", "c) halus", "d) kasar", "e) teratur"]},
            {"id": 29, "no": "29", "opts": ["a) mobil", "b) sepeda motor", "c) truk", "d) sepeda", "e) bus"]},
            {"id": 30, "no": "30", "opts": ["a) biola", "b) seruling", "c) terompet", "d) harmonika", "e) kuis"]},
            {"id": 31, "no": "31", "opts": ["a) melengkung", "b) bungkuk", "c) bengkok", "d) miring", "e) lurus"]},
            {"id": 32, "no": "32", "opts": ["a) jam", "b) masehi", "c) bulan", "d) tahun", "e) abad"]},
            {"id": 33, "no": "33", "opts": ["a) kebijaksanaan", "b) keindahan", "c) keberanian", "d) kejujuran", "e) kebaikan"]},
            {"id": 34, "no": "34", "opts": ["a) berlari", "b) berjalan", "c) melompat", "d) memanjat", "e) berenang"]},
            {"id": 35, "no": "35", "opts": ["a) cermin", "b) teropong", "c) potret", "d) kacamata", "e) mikroskop"]},
            {"id": 36, "no": "36", "opts": ["a) panjang", "b) lonjong", "c) segitiga", "d) segi empat", "e) lingkaran"]},
            {"id": 37, "no": "37", "opts": ["a) cangkul", "b) sekop", "c) sabit", "d) gunting", "e) linggis"]},
            {"id": 38, "no": "38", "opts": ["a) keluarga", "b) suku", "c) bangsa", "d) perkumpulan", "e) masyarakat"]},
            {"id": 39, "no": "39", "opts": ["a) mengajar", "b) menasehati", "c) melatih", "d) membimbing", "e) membina"]},
            {"id": 40, "no": "40", "opts": ["a) sisik", "b) cangkang", "c) bulu", "d) kulit", "e) tanduk"]}
        ]

        with st.form("form_subtest_2"):
            for q in questions_wa:
                st.markdown(f"**Soal {q['no']}.** Pilih kata yang paling berbeda:")
                st.session_state.answers[q['id']] = st.radio(
                    f"Pilihan Jawaban No. {q['no']}:",
                    options=q['opts'],
                    key=f"wa_{q['id']}"
                )
                st.markdown("---")

            if st.form_submit_button("Simpan & Lanjut ke Subtes 3 (AN) ➔"):
                for q_id in range(21, 41):
                    if f"wa_{q_id}" in st.session_state:
                        st.session_state.answers[q_id] = st.session_state[f"wa_{q_id}"]
                st.session_state.current_subtest = 3
                st.rerun()
