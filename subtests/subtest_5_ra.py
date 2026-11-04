import streamlit as st
import streamlit.components.v1 as components
import time

def show_live_timer_ra(seconds_remaining):
    components.html(f"""
    <div style="font-family: Arial, sans-serif; font-size: 20px; font-weight: bold; color: #d9534f; 
                background-color: #fdf7f7; padding: 10px 15px; border: 2px solid #d9534f; 
                border-radius: 8px; text-align: center; margin-bottom: 10px;">
        ⏱️ SISA WAKTU SUBTES 5 (RA): <span id="timer_display_ra">--:--</span>
    </div>
    <script>
        var timeLeft = {seconds_remaining};
        function updateDisplay() {{
            var m = Math.floor(timeLeft / 60);
            var s = timeLeft % 60;
            var displayM = m < 10 ? "0" + m : m;
            var displayS = s < 10 ? "0" + s : s;
            var elem = document.getElementById("timer_display_ra");
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

def render_subtest_5_ra():
    if "step_ra" not in st.session_state:
        st.session_state.step_ra = "instruction"
    if "answers" not in st.session_state:
        st.session_state.answers = {}

    if st.session_state.step_ra == "instruction":
        st.title("📑 Petunjuk Subtes 05: RA (Soal Hitungan)")
        st.info("💡 Bacalah petunjuk di bawah ini dengan teliti. **Timer belum berjalan di halaman ini.**")
        st.markdown("""
        ### Aturan Pengerjaan:
        Ketikkan jawaban berupa **angka hasil perhitungan** secara langsung pada kolom isian di bawah tiap soal.

        ---
        ### Contoh:
        **Sebatang pensil harganya Rp 25,-. Berapakah harga 3 batang pensil?**  
        *Penjelasan:* 25 × 3 = 75.  
        **Ketikkan Jawaban:** **75**
        """)
        st.markdown("---")
        if st.button("Mulai Kerjakan Subtes 5 🚀", type="primary"):
            st.session_state.step_ra = "test"
            st.session_state.start_time_ra = time.time()
            st.rerun()

    elif st.session_state.step_ra == "test":
        st.title("🧠 Subtes 05: RA (Soal Hitungan)")
        
        elapsed = int(time.time() - st.session_state.start_time_ra)
        remaining = max(0, 600 - elapsed)
        show_live_timer_ra(remaining)

        if remaining <= 0:
            st.warning("⏰ Waktu Subtes 5 telah habis! Mengalihkan ke Subtes 6...")
            for q_id in range(77, 97):
                if f"ra_{q_id}" in st.session_state:
                    st.session_state.answers[q_id] = st.session_state[f"ra_{q_id}"]
            time.sleep(1)
            st.session_state.current_subtest = 6
            st.rerun()

        questions_ra = [
            {"id": 77, "no": "77", "q": "Jika seorang anak memiliki 5 kelereng dan diberi lagi 30 kelereng, berapa jumlah kelerengnya sekarang?"},
            {"id": 78, "no": "78", "q": "Berapa hasil dari 35 dikali 8?"},
            {"id": 79, "no": "79", "q": "Seorang pedagang membeli barang seharga Rp 180,- dan menjualnya Rp 205,-. Berapa keuntungan pedagang tersebut?"},
            {"id": 80, "no": "80", "q": "Jarak dari kota A ke B adalah 130 km. Sebuah mobil menempuhnya dalam waktu 5 jam. Berapa km/jam kecepatan rata-rata mobil tersebut?"},
            {"id": 81, "no": "81", "q": "3 orang pekerja dapat menyelesaikan sebuah pekerjaan dalam 10 hari. Berapa hari pekerjaan itu selesai jika dikerjakan oleh 1 orang?"},
            {"id": 82, "no": "82", "q": "Suatu kawat sepanjang 140 cm dipotong menjadi 2 bagian dengan perbandingan 1 : 1. Berapa cm panjang masing-masing potongan?"},
            {"id": 83, "no": "83", "q": "Sebuah mobil menempuh jarak 15 km dengan 1 liter bensin. Berapa km jarak yang ditempuh dengan 3 liter bensin?"},
            {"id": 84, "no": "84", "q": "Jika 1/4 dari sebuah angka adalah 12,5, berapakah angka tersebut?"},
            {"id": 85, "no": "85", "q": "Suatu kain panjangnya 120 meter dipotong 30%. Berapa meter sisa kain tersebut?"},
            {"id": 86, "no": "86", "q": "Berapakah hasil dari 156 dibagi 2?"},
            {"id": 87, "no": "87", "q": "Seorang pekerja mendapat upah Rp 114,- untuk 6 jam kerja. Berapa upahnya per jam?"},
            {"id": 88, "no": "88", "q": "Suatu kolam diisi air oleh 2 pipa. Pipa A mengisi 2 liter/menit, pipa B mengisi 4 liter/menit. Berapa liter air yang masuk dalam 1 menit?"},
            {"id": 89, "no": "89", "q": "Seorang ibu membeli 3 kg gula dengan harga Rp 25,- per kg. Berapa total harga yang harus dibayar?"},
            {"id": 90, "no": "90", "q": "Berapakah 75% dari 120?"},
            {"id": 91, "no": "91", "q": "Sebuah bak berisi 180 liter air. Jika dikosongkan dengan debit 1,5 liter/detik, berapa detik waktu yang dibutuhkan?"},
            {"id": 92, "no": "92", "q": "Berapakah hasil dari 85 dibagi 5?"},
            {"id": 93, "no": "93", "q": "Suatu persegi panjang memiliki panjang 9 cm dan lebar 4 cm. Berapakah luasnya dalam cm²?"},
            {"id": 94, "no": "94", "q": "Jika 45 dibagi dengan suatu angka hasilnya adalah 9, berapakah angka tersebut?"},
            {"id": 95, "no": "95", "q": "Seorang pedagang mendapat keuntungan Rp 12,- dari setiap barang yang dijual. Jika ia menjual 4 barang, berapa total keuntungannya?"},
            {"id": 96, "no": "96", "q": "Suatu proyek membutuhkan waktu 12 hari jika dikerjakan oleh 1 orang. Jika ada 12 orang pekerja, berapa hari proyek tersebut selesai?"}
        ]

        with st.form("form_subtest_5"):
            for q in questions_ra:
                st.markdown(f"**Soal {q['no']}.** {q['q']}")
                st.session_state.answers[q['id']] = st.text_input(
                    f"Jawaban Hitungan No. {q['no']}:", 
                    key=f"ra_{q['id']}"
                )
                st.markdown("---")

            if st.form_submit_button("Simpan & Lanjut ke Subtes 6 (ZR) ➔"):
                for q_id in range(77, 97):
                    if f"ra_{q_id}" in st.session_state:
                        st.session_state.answers[q_id] = st.session_state[f"ra_{q_id}"]
                st.session_state.current_subtest = 6
                st.rerun()
