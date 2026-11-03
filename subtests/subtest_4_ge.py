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
