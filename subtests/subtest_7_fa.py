import streamlit as st
import streamlit.components.v1 as components
import time
import os

def show_live_timer_fa(seconds_remaining):
    components.html(f"""
    <div style="font-family: Arial, sans-serif; font-size: 20px; font-weight: bold; color: #d9534f; 
                background-color: #fdf7f7; padding: 10px 15px; border: 2px solid #d9534f; 
                border-radius: 8px; text-align: center; margin-bottom: 10px;">
        ⏱️ SISA WAKTU SUBTES 7 (FA): <span id="timer_display_fa">--:--</span>
    </div>
    <script>
        var timeLeft = {seconds_remaining};
        function updateDisplay() {{
            var m = Math.floor(timeLeft / 60);
            var s = timeLeft % 60;
            var displayM = m < 10 ? "0" + m : m;
            var displayS = s < 10 ? "0" + s : s;
            var elem = document.getElementById("timer_display_fa");
            if (elem) {{ elem.innerHTML = displayM + ":" + displayS; }}
            if (timeLeft <= 0) {{ if (elem) elem.innerHTML = "00:00 (WAKTU HABIS)"; }}
            else {{ timeLeft--; }}
        }}
        updateDisplay();
        setInterval(updateDisplay, 1000);
    </script>
    """, height=75)

def render_subtest_7_fa():
    if "step_fa" not in st.session_state:
        st.session_state.step_fa = "instruction"
    if "answers" not in st.session_state:
        st.session_state.answers = {}

    # TAHAP 1: PETUNJUK LENGKAP & CONTOH (TANPA TIMER)
    if st.session_state.step_fa == "instruction":
        st.title("📑 Petunjuk Subtes 07: FA (Pemilihan Bentuk)")
        st.info("💡 Bacalah petunjuk dan pelajari contoh di bawah ini dengan teliti. **Timer belum berjalan di halaman ini.**")
        
        st.markdown("""
        ### Aturan Pengerjaan:
        Pada persoalan berikutnya, setiap soal memperlihatkan **suatu bentuk tertentu yang terpotong menjadi beberapa bagian**.

        Carilah di antara bentuk-bentuk utama yang ditentukan (**a, b, c, d, e**) bentuk yang dibangun dengan cara **menyusun potongan-potongan itu** sedemikian rupa, sehingga **tidak ada kelebihan sudut atau ruang di antaranya**.
        """)

        petunjuk_img_path = "images/subtest_7_petunjuk.png"
        if os.path.exists(petunjuk_img_path):
            st.image(petunjuk_img_path, caption="Lembar Petunjuk & Contoh Subtes 07 (FA)", use_container_width=True)
        else:
            st.warning("⚠️ File gambar `images/subtest_7_petunjuk.png` belum diunggah ke GitHub.")

        st.markdown("""
        ---
        ### Penjelasan Contoh Soal:
        * **Contoh 07**: Potongan-potongan pada contoh 07 jika disusun (digabungkan) akan menghasilkan bentuk **a** (Lingkaran utuh).
        * **Contoh kedua**: Potongan-potongan contoh kedua setelah disusun menghasilkan bentuk **e**.
        * **Contoh ketiga**: Potongan-potongan contoh ketiga setelah disusun menghasilkan bentuk **b**.
        * **Contoh keempat**: Potongan-potongan contoh keempat setelah disusun menghasilkan bentuk **d**.
        """)
        st.markdown("---")
        
        if st.button("Mulai Kerjakan Subtes 7 🚀", type="primary"):
            st.session_state.step_fa = "test"
            st.session_state.start_time_fa = time.time()
            st.rerun()

    # TAHAP 2: PENGERJAAN SOAL (TIMER 7 MENIT BERJALAN)
    elif st.session_state.step_fa == "test":
        st.title("🧠 Subtes 07: FA (Pemilihan Bentuk)")
        
        # Alokasi resmi Subtes 7 FA = 7 Menit (420 Detik)
        elapsed = int(time.time() - st.session_state.start_time_fa)
        remaining = max(0, 420 - elapsed)
        show_live_timer_fa(remaining)

        if remaining == 0:
            st.warning("⏰ Waktu Subtes 7 telah habis!")
            if st.button("Lanjut ke Subtes 8 ➔"):
                st.session_state.current_subtest = 8
                st.rerun()
            st.stop()

        soal_img_path = "images/subtest_7_soal.png"
        if os.path.exists(soal_img_path):
            st.image(soal_img_path, caption="Lembar Soal Subtes 07 (FA) No. 117 - 136", use_container_width=True)
        else:
            st.warning("⚠️ File gambar `images/subtest_7_soal.png` belum diunggah ke GitHub.")

        st.subheader("📝 Lembar Jawaban (Soal No. 117 - 136)")

        options_fa = ["a", "b", "c", "d", "e"]

        with st.form("form_subtest_7"):
            col1, col2 = st.columns(2)
            
            # Kolom 1: Soal 117 - 126
            with col1:
                st.markdown("#### Bagian 1 (No. 117 - 126)")
                for q_id in range(117, 127):
                    st.session_state.answers[q_id] = st.radio(
                        f"Pilih Jawaban No. {q_id}:",
                        options=options_fa,
                        horizontal=True,
                        key=f"fa_{q_id}"
                    )
            
            # Kolom 2: Soal 127 - 136
            with col2:
                st.markdown("#### Bagian 2 (No. 127 - 136)")
                for q_id in range(127, 137):
                    st.session_state.answers[q_id] = st.radio(
                        f"Pilih Jawaban No. {q_id}:",
                        options=options_fa,
                        horizontal=True,
                        key=f"fa_{q_id}"
                    )

            st.markdown("---")
            if st.form_submit_button("Simpan & Lanjut ke Subtes 8 ➔"):
                st.session_state.current_subtest = 8
                st.rerun()
