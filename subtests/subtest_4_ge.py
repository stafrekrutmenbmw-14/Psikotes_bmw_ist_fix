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

def render_subtest_4_ge():
    if "step_ge" not in st.session_state:
        st.session_state.step_ge = "instruction"
    if "answers" not in st.session_state:
        st.session_state.answers = {}

    if st.session_state.step_ge == "instruction":
        st.title("📑 Petunjuk Subtes 04: GE (Kesamaan Kata)")
        st.info("💡 Bacalah petunjuk di bawah ini dengan teliti. **Timer belum berjalan di halaman ini.**")
        st.markdown("""
        ### Aturan Pengerjaan:
        Ditentukan dua kata. Carilah **satu kata penggolongan/kesamaan umum** yang mencakup pengertian kedua kata tersebut.

        ---
        ### Contoh:
        **Mawar - Melati**  
        *Kesamaan:* **Bunga** (atau Kembang).
        """)
        st.markdown("---")
        if st.button("Mulai Kerjakan Subtes 4 🚀", type="primary"):
            st.session_state.step_ge = "test"
            st.session_state.start_time_ge = time.time()
            st.rerun()

    elif st.session_state.step_ge == "test":
        st.title("🧠 Subtes 04: GE (Kesamaan Kata)")
        
        elapsed = int(time.time() - st.session_state.start_time_ge)
        remaining = max(0, 480 - elapsed)
        show_live_timer_ge(remaining)

        if remaining <= 0:
            st.warning("⏰ Waktu Subtes 4 telah habis! Mengalihkan ke Subtes 5...")
            for q_id in range(61, 77):
                if f"ge_{q_id}" in st.session_state:
                    st.session_state.answers[q_id] = st.session_state[f"ge_{q_id}"]
            time.sleep(1)
            st.session_state.current_subtest = 5
            st.rerun()

        questions_ge = [
            {"id": 61, "no": "61", "q": "Mawar - Melati"},
            {"id": 62, "no": "62", "q": "Mata - Telinga"},
            {"id": 63, "no": "63", "q": "Intan - Arang"},
            {"id": 64, "no": "64", "q": "Hujan - Salju"},
            {"id": 65, "no": "65", "q": "Surat - Telegram"},
            {"id": 66, "no": "66", "q": "Kaca Mata - Teropong"},
            {"id": 67, "no": "67", "q": "Lambung - Usus"},
            {"id": 68, "no": "68", "q": "Banyak - Sedikit"},
            {"id": 69, "no": "69", "q": "Telur - Benih"},
            {"id": 70, "no": "70", "q": "Bendera - Lencana"},
            {"id": 71, "no": "71", "q": "Rumput - Gajah"},
            {"id": 72, "no": "72", "q": "Ember - Kantong"},
            {"id": 73, "no": "73", "q": "Awal - Akhir"},
            {"id": 74, "no": "74", "q": "Kikir - Dermawan"},
            {"id": 75, "no": "75", "q": "Penjualan - Pembelian"},
            {"id": 76, "no": "76", "q": "Atas - Bawah"}
        ]

        with st.form("form_subtest_4"):
            for q in questions_ge:
                st.markdown(f"**Soal {q['no']}.** {q['q']}")
                st.session_state.answers[q['id']] = st.text_input(
                    f"Ketikkan Kata Kesamaan No. {q['no']}:",
                    key=f"ge_{q['id']}"
                )
                st.markdown("---")

            if st.form_submit_button("Simpan & Lanjut ke Subtes 5 (RA) ➔"):
                for q_id in range(61, 77):
                    if f"ge_{q_id}" in st.session_state:
                        st.session_state.answers[q_id] = st.session_state[f"ge_{q_id}"]
                st.session_state.current_subtest = 5
                st.rerun()
