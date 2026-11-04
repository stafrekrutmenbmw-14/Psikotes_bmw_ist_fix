import streamlit as st
import streamlit.components.v1 as components
import time

def show_live_timer_se(seconds_remaining):
    components.html(f"""
    <div style="font-family: Arial, sans-serif; font-size: 20px; font-weight: bold; color: #d9534f; 
                background-color: #fdf7f7; padding: 10px 15px; border: 2px solid #d9534f; 
                border-radius: 8px; text-align: center; margin-bottom: 10px;">
        ⏱️ SISA WAKTU SUBTES 1 (SE): <span id="timer_display_se">--:--</span>
    </div>
    <script>
        var timeLeft = {seconds_remaining};
        function updateDisplay() {{
            var m = Math.floor(timeLeft / 60);
            var s = timeLeft % 60;
            var displayM = m < 10 ? "0" + m : m;
            var displayS = s < 10 ? "0" + s : s;
            var elem = document.getElementById("timer_display_se");
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

def render_subtest_1_se():
    if "step_se" not in st.session_state:
        st.session_state.step_se = "instruction"
    if "answers" not in st.session_state:
        st.session_state.answers = {}

    if st.session_state.step_se == "instruction":
        st.title("📑 Petunjuk Subtes 01: SE (Melengkapi Kalimat)")
        st.info("💡 Bacalah petunjuk dan contoh di bawah ini dengan teliti. **Timer belum berjalan di halaman ini.**")
        st.markdown("""
        ### Aturan Pengerjaan:
        Pada soal-soal berikut diberikan kalimat-kalimat yang belum selesai. Carilah satu kata dari 5 pilihan yang tersedia (a, b, c, d, e) yang paling tepat untuk melengkapi kalimat tersebut.

        ---
        ### Contoh:
        **Seekor kuda mempunyai kesamaan terbanyak dengan seekor ...**  
        a) kucing | b) bajing | c) keledai | d) lembu | e) anjing  
        *Jawaban yang benar adalah* **c) keledai**.
        """)
        st.markdown("---")
        if st.button("Mulai Kerjakan Subtes 1 🚀", type="primary"):
            st.session_state.step_se = "test"
            st.session_state.start_time_se = time.time()
            st.rerun()

    elif st.session_state.step_se == "test":
        st.title("🧠 Subtes 01: SE (Melengkapi Kalimat)")
        
        elapsed = int(time.time() - st.session_state.start_time_se)
        remaining = max(0, 360 - elapsed)
        show_live_timer_se(remaining)

        if remaining <= 0:
            st.warning("⏰ Waktu Subtes 1 telah habis! Mengalihkan ke Subtes 2...")
            for q_id in range(1, 21):
                if f"se_{q_id}" in st.session_state:
                    st.session_state.answers[q_id] = st.session_state[f"se_{q_id}"]
            time.sleep(1)
            st.session_state.current_subtest = 2
            st.rerun()

        questions_se = [
            {"id": 1, "no": "01", "q": "Pengaruh seseorang terhadap orang lain harus tergantung pada ...", "opts": ["a) kekuasaan", "b) bujukan", "c) kekayaan", "d) keberanian", "e) kewibawaan"]},
            {"id": 2, "no": "02", "q": "Lawan dari 'hemat' adalah ...", "opts": ["a) murah hati", "b) kikir", "c) boros", "d) kaya", "e) bernafsu"]},
            {"id": 3, "no": "03", "q": "Bencana alam yang sering terjadi di daerah gunung berapi adalah ...", "opts": ["a) banjir", "b) angin taufan", "c) tanah longsor", "d) gempa bumi", "e) tsunami"]},
            {"id": 4, "no": "04", "q": "Lawan dari 'setia' adalah ...", "opts": ["a) jahat", "b) benci", "c) bohong", "d) khianat", "e) lari"]},
            {"id": 5, "no": "05", "q": "Harimau mempunyai kesamaan terbanyak dengan ...", "opts": ["a) serigala", "b) singa", "c) beruang", "d) kuku", "e) gajah"]},
            {"id": 6, "no": "06", "q": "Seorang anak yang baru lahir ... mempunyai rambut.", "opts": ["a) selalu", "b) biasanya", "c) tidak pernah", "d) kadang-kadang", "e) jarang"]},
            {"id": 7, "no": "07", "q": "Mentega dibuat dari ...", "opts": ["a) susu", "b) buah-buahan", "c) lemak", "d) tumbuh-tumbuhan", "e) minyak"]},
            {"id": 8, "no": "08", "q": "Pada jumlah yang sama, nilai uang kertas ... nilai uang logam.", "opts": ["a) lawan", "b) lebih tinggi", "c) lebih rendah", "d) sama dengan", "e) berubah-ubah"]},
            {"id": 9, "no": "09", "q": "Suatu dugaan yang belum terbukti kebenarannya disebut ...", "opts": ["a) kenyataan", "b) fakta", "c) peristiwa", "d) hukum", "e) hipotesis"]},
            {"id": 10, "no": "10", "q": "Alas sepatu biasanya dibuat dari ...", "opts": ["a) kulit", "b) sol", "c) plastik", "d) karet", "e) kain"]},
            {"id": 11, "no": "11", "q": "Di tempat kerja harus selalu disediakan ...", "opts": ["a) makanan", "b) alat pemadam", "c) kotak PPPK", "d) air minum", "e) tempat istirahat"]},
            {"id": 12, "no": "12", "q": "Panjang sebuah pensil pada umumnya adalah ... cm.", "opts": ["a) 5", "b) 10", "c) 15", "d) 20", "e) 30"]},
            {"id": 13, "no": "13", "q": "Orang yang tidak suka perubahan disebut ...", "opts": ["a) radikal", "b) maju", "c) luwes", "d) konservatif", "e) ekstrem"]},
            {"id": 14, "no": "14", "q": "Matahari ... terbit di sebelah timur.", "opts": ["a) kadang-kadang", "b) sering", "c) biasanya", "d) tidak pernah", "e) selalu"]},
            {"id": 15, "no": "15", "q": "Jarak antara Jakarta dan Surabaya kira-kira ... km.", "opts": ["a) 200", "b) 500", "c) 800", "d) 1200", "e) 1500"]},
            {"id": 16, "no": "16", "q": "Kekuatan sebuah jembatan tergantung pada ... bahannya.", "opts": ["a) kekuatan", "b) berat", "c) harga", "d) warna", "e) keindahan"]},
            {"id": 17, "no": "17", "q": "Anak-anak ... lebih pendek dari orang dewasa.", "opts": ["a) selalu", "b) biasanya", "c) tidak pernah", "d) kadang-kadang", "e) jarang"]},
            {"id": 18, "no": "18", "q": "Kota yang terletak di Jawa Barat adalah ...", "opts": ["a) Semarang", "b) Bandung", "c) Surabaya", "d) Yogyakarta", "e) Surakarta"]},
            {"id": 19, "no": "19", "q": "Kemenangan dalam pertandingan olahraga tergantung pada ...", "opts": ["a) Keberuntungan", "b) Penonton", "c) kemungkinan menang", "d) Hadiah", "e) Wasit"]},
            {"id": 20, "no": "20", "q": "Tinggi badan rata-rata pria Indonesia adalah sekitar ... cm.", "opts": ["a) 120", "b) 130", "c) 165", "d) 190", "e) 200"]}
        ]

        with st.form("form_subtest_1"):
            for q in questions_se:
                st.markdown(f"**Soal {q['no']}.** {q['q']}")
                st.session_state.answers[q['id']] = st.radio(
                    f"Pilih Jawaban No. {q['no']}:",
                    options=q['opts'],
                    key=f"se_{q['id']}"
                )
                st.markdown("---")

            if st.form_submit_button("Simpan & Lanjut ke Subtes 2 (WA) ➔"):
                for q_id in range(1, 21):
                    if f"se_{q_id}" in st.session_state:
                        st.session_state.answers[q_id] = st.session_state[f"se_{q_id}"]
                st.session_state.current_subtest = 2
                st.rerun()
