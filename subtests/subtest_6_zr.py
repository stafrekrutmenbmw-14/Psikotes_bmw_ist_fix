import streamlit as st
import streamlit.components.v1 as components
import time

def show_live_timer_zr(seconds_remaining):
    components.html(f"""
    <div style="font-family: Arial, sans-serif; font-size: 20px; font-weight: bold; color: #d9534f; 
                background-color: #fdf7f7; padding: 10px 15px; border: 2px solid #d9534f; 
                border-radius: 8px; text-align: center; margin-bottom: 10px;">
        ⏱️ SISA WAKTU SUBTES 6 (ZR): <span id="timer_display_zr">--:--</span>
    </div>
    <script>
        var timeLeft = {seconds_remaining};
        function updateDisplay() {{
            var m = Math.floor(timeLeft / 60);
            var s = timeLeft % 60;
            var displayM = m < 10 ? "0" + m : m;
            var displayS = s < 10 ? "0" + s : s;
            var elem = document.getElementById("timer_display_zr");
            if (elem) {{ elem.innerHTML = displayM + ":" + displayS; }}
            if (timeLeft <= 0) {{ if (elem) elem.innerHTML = "00:00 (WAKTU HABIS)"; }}
            else {{ timeLeft--; }}
        }}
        updateDisplay();
        setInterval(updateDisplay, 1000);
    </script>
    """, height=75)

def render_subtest_6_zr():
    if "step_zr" not in st.session_state:
        st.session_state.step_zr = "instruction"
    if "answers" not in st.session_state:
        st.session_state.answers = {}

    if st.session_state.step_zr == "instruction":
        st.title("📑 Petunjuk Subtes 06: ZR (Deret Angka)")
        st.info("💡 Bacalah seluruh petunjuk dan contoh di bawah ini. **Timer belum berjalan di halaman ini.**")
        st.markdown("""
        ### Aturan Pengerjaan:
        Pada persoalan berikut diberikan deret angka. Setiap deret tersusun menurut pola/aturan tertentu. 
        Carilah **satu angka berikutnya** dan ketikkan pada kolom jawaban!

        ---
        ### Contoh 01:
        **2  4  6  8  10  12  14  ?**  
        *Penjelasan:* Angka berikutnya selalu ditambah 2.  
        **Jawaban:** **16**

        ---
        ### Contoh 02:
        **9  7  10  8  11  9  12  ?**  
        *Penjelasan:* Polanya berganti-ganti dikurangi 2 lalu ditambah 3.  
        **Jawaban:** **10**
        """)
        st.markdown("---")
        if st.button("Mulai Kerjakan Subtes 6 🚀", type="primary"):
            st.session_state.step_zr = "test"
            st.session_state.start_time_zr = time.time()
            st.rerun()

    elif st.session_state.step_zr == "test":
        st.title("🧠 Subtes 06: ZR (Deret Angka)")
        
        # Alokasi resmi Subtes 6 ZR = 10 Menit (600 Detik)
        elapsed = int(time.time() - st.session_state.start_time_zr)
        remaining = max(0, 600 - elapsed)
        show_live_timer_zr(remaining)

        if remaining == 0:
            st.warning("⏰ Waktu Subtes 6 telah habis!")
            if st.button("Selesaikan Seluruh Ujian ➔"):
                st.session_state.current_subtest = 7
                st.rerun()
            st.stop()

        questions_zr = [
            {"id": 97, "no": "97", "q": "6   9   12   15   18   21   24   ?"},
            {"id": 98, "no": "98", "q": "15   16   18   19   21   22   24   ?"},
            {"id": 99, "no": "99", "q": "19   18   22   21   25   24   28   ?"},
            {"id": 100, "no": "100", "q": "16   12   17   13   18   14   19   ?"},
            {"id": 101, "no": "101", "q": "2   4   8   10   20   22   44   ?"},
            {"id": 102, "no": "102", "q": "15   13   16   12   17   11   18   ?"},
            {"id": 103, "no": "103", "q": "25   22   11   33   30   15   45   ?"},
            {"id": 104, "no": "104", "q": "49   51   54   27   9   11   14   ?"},
            {"id": 105, "no": "105", "q": "2   3   1   3   4   2   4   ?"},
            {"id": 106, "no": "106", "q": "19   17   20   16   21   15   22   ?"},
            {"id": 107, "no": "107", "q": "94   92   46   44   22   20   10   ?"},
            {"id": 108, "no": "108", "q": "5   8   9   8   11   12   11   ?"},
            {"id": 109, "no": "109", "q": "12   15   19   23   28   33   39   ?"},
            {"id": 110, "no": "110", "q": "7   5   10   7   21   17   68   ?"},
            {"id": 111, "no": "111", "q": "11   15   18   9   13   16   8   ?"},
            {"id": 112, "no": "112", "q": "3   8   15   24   35   48   63   ?"},
            {"id": 113, "no": "113", "q": "4   5   7   4   8   13   7   ?"},
            {"id": 114, "no": "114", "q": "8   5   15   18   6   3   9   ?"},
            {"id": 115, "no": "115", "q": "15   6   18   10   30   23   69   ?"},
            {"id": 116, "no": "116", "q": "5   35   28   4   11   77   70   ?"}
        ]

        with st.form("form_subtest_6"):
            for q in questions_zr:
                st.markdown(f"**Soal {q['no']}.** {q['q']}")
                st.session_state.answers[q['id']] = st.text_input(
                    f"Angka Selanjutnya No. {q['no']}:", 
                    key=f"zr_{q['id']}"
                )
                st.markdown("---")

            if st.form_submit_button("Simpan & Selesaikan Seluruh Ujian ➔"):
                st.session_state.current_subtest = 7
                st.rerun()
