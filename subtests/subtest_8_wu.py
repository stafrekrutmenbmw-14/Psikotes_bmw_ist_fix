import streamlit as st
import streamlit.components.v1 as components
import time
import os

def show_live_timer_wu(seconds_remaining):
    components.html(f"""
    <div style="font-family: Arial, sans-serif; font-size: 20px; font-weight: bold; color: #d9534f; 
                background-color: #fdf7f7; padding: 10px 15px; border: 2px solid #d9534f; 
                border-radius: 8px; text-align: center; margin-bottom: 10px;">
        ⏱️ SISA WAKTU SUBTES 8 (WU): <span id="timer_display_wu">--:--</span>
    </div>
    <script>
        var timeLeft = {seconds_remaining};
        function updateDisplay() {{
            var m = Math.floor(timeLeft / 60);
            var s = timeLeft % 60;
            var displayM = m < 10 ? "0" + m : m;
            var displayS = s < 10 ? "0" + s : s;
            var elem = document.getElementById("timer_display_wu");
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

def render_subtest_8_wu():
    if "step_wu" not in st.session_state:
        st.session_state.step_wu = "instruction"
    if "answers" not in st.session_state:
        st.session_state.answers = {}

    if st.session_state.step_wu == "instruction":
        st.title("📑 Petunjuk Subtes 08: WU (Benda Ruang)")
        st.info("💡 Bacalah petunjuk di bawah ini dengan teliti. **Timer belum berjalan di halaman ini.**")
        st.markdown("""
        ### Aturan Pengerjaan:
        Ditentukan 5 kubus (**a, b, c, d, e**). Setiap soal memperlihatkan salah satu kubus yang ditentukan di dalam kedudukan yang berbeda (diputar/digulingkan). Carilah kubus yang dimaksudkan itu!
        """)

        petunjuk_img_path = "images/subtest_8_petunjuk.png"
        if os.path.exists(petunjuk_img_path):
            st.image(petunjuk_img_path, caption="Lembar Petunjuk & Contoh Subtes 08 (WU)", use_container_width=True)
        else:
            st.warning("⚠️ File gambar `images/subtest_8_petunjuk.png` belum diunggah ke GitHub.")

        st.markdown("---")
        if st.button("Mulai Kerjakan Subtes 8 🚀", type="primary"):
            st.session_state.step_wu = "test"
            st.session_state.start_time_wu = time.time()
            st.rerun()

    elif st.session_state.step_wu == "test":
        st.title("🧠 Subtes 08: WU (Benda Ruang)")
        
        elapsed = int(time.time() - st.session_state.start_time_wu)
        remaining = max(0, 540 - elapsed)
        show_live_timer_wu(remaining)

        if remaining <= 0:
            st.warning("⏰ Waktu Subtes 8 telah habis! Menyimpan seluruh jawaban dan mengalihkan ke Hasil Ujian...")
            for q_id in range(137, 157):
                if f"wu_{q_id}" in st.session_state:
                    st.session_state.answers[q_id] = st.session_state[f"wu_{q_id}"]
            time.sleep(1)
            st.session_state.page = "result"
            st.rerun()

        soal_img_path = "images/subtest_8_soal.png"
        if os.path.exists(soal_img_path):
            st.image(soal_img_path, caption="Lembar Soal Subtes 08 (WU) No. 137 - 156", use_container_width=True)
        else:
            st.warning("⚠️ File gambar `images/subtest_8_soal.png` belum diunggah ke GitHub.")

        st.subheader("📝 Lembar Jawaban (Soal No. 137 - 156)")

        options_wu = ["a", "b", "c", "d", "e"]

        with st.form("form_subtest_8"):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("#### Bagian 1 (No. 137 - 146)")
                for q_id in range(137, 147):
                    st.session_state.answers[q_id] = st.radio(
                        f"Pilih Jawaban No. {q_id}:",
                        options=options_wu,
                        horizontal=True,
                        key=f"wu_{q_id}"
                    )
            with col2:
                st.markdown("#### Bagian 2 (No. 147 - 156)")
                for q_id in range(147, 157):
                    st.session_state.answers[q_id] = st.radio(
                        f"Pilih Jawaban No. {q_id}:",
                        options=options_wu,
                        horizontal=True,
                        key=f"wu_{q_id}"
                    )

            st.markdown("---")
            if st.form_submit_button("Simpan & Selesaikan Ujian 🏁"):
                for q_id in range(137, 157):
                    if f"wu_{q_id}" in st.session_state:
                        st.session_state.answers[q_id] = st.session_state[f"wu_{q_id}"]
                st.session_state.page = "result"
                st.rerun()
