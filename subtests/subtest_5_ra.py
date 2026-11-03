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
            if (timeLeft <= 0) {{ if (elem) elem.innerHTML = "00:00 (WAKTU HABIS)"; }}
            else {{ timeLeft--; }}
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
        st.title("📑 Petunjuk Subtes 05: RA (Hitungan Aritmatika)")
        st.info("💡 Bacalah seluruh petunjuk dan contoh di bawah ini. **Timer belum berjalan di halaman ini.**")
        st.markdown("""
        ### Aturan Pengerjaan:
        Berikut adalah soal-soal hitungan cerita. Selesaikan perhitungan dan ketikkan **angka jawaban akhir** saja!

        ---
        ### Contoh 01:
        Sebatang pensil harganya 25 rupiah. Berapakah harga 3 batang?  
        **Jawaban:** **75**

        ---
        ### Contoh 02:
        Dengan sepeda Husin dapat mencapai 15 km dalam waktu 1 jam. Berapa km-kah yang dapat ia capai dalam waktu 4 jam?  
        **Jawaban:** **60**
        """)
        st.markdown("---")
        if st.button("Mulai Kerjakan Subtes 5 🚀", type="primary"):
            st.session_state.step_ra = "test"
            st.session_state.start_time_ra = time.time()
            st.rerun()

    elif st.session_state.step_ra == "test":
        st.title("🧠 Subtes 05: RA (Hitungan Aritmatika)")
        
        # Alokasi resmi Subtes 5 RA = 10 Menit (600 Detik)
        elapsed = int(time.time() - st.session_state.start_time_ra)
        remaining = max(0, 600 - elapsed)
        show_live_timer_ra(remaining)

        if remaining == 0:
            st.warning("⏰ Waktu Subtes 5 telah habis!")
            if st.button("Lanjut ke Subtes 6 (ZR) ➔"):
                st.session_state.current_subtest = 6
                st.rerun()
            st.stop()

        questions_ra = [
            {"id": 77, "no": "77", "q": "Jika seorang anak memiliki 50 rupiah dan memberikan 15 rupiah kepada orang lain, berapa rupiahkah yang masih tinggal padanya?"},
            {"id": 78, "no": "78", "q": "Berapa km-kah yang dapat ditempuh oleh kereta api dalam waktu 7 jam, jika kecepatannya 40 km/jam?"},
            {"id": 79, "no": "79", "q": "15 peti buah-buahan beratnya 250 kg dan setiap peti kosong beratnya 3 kg, berapakah berat buah-buahan itu?"},
            {"id": 80, "no": "80", "q": "Seseorang mempunyai persediaan rumput yang cukup untuk 7 ekor kuda selama 78 hari. Berapa harikah persediaan itu cukup untuk 21 ekor kuda?"},
            {"id": 81, "no": "81", "q": "3 batang coklat harganya Rp 5,- Berapa batangkah yang dapat kita beli dengan Rp 50,-?"},
            {"id": 82, "no": "82", "q": "Seseorang dapat berjalan 1,75 m dalam waktu ¼ detik. Berapakah meterkah yang dapat ia tempuh dalam waktu 10 detik?"},
            {"id": 83, "no": "83", "q": "Jika sebuah batu terletak 15 m di sebelah selatan dari sebatang pohon dan pohon itu berada 30 m di sebelah selatan dari sebuah rumah, berapa meterkah jarak antara batu dan rumah itu?"},
            {"id": 84, "no": "84", "q": "Jika 4 ½ m bahan sandang harganya Rp 90,- berapakah rupiahkah harganya 2 ½ m?"},
            {"id": 85, "no": "85", "q": "7 orang dapat menyelesaikan sesuatu pekerjaan dalam 6 hari. Berapa orangkah yang diperlukan untuk menyelesaikan pekerjaan itu dalam setengah hari?"},
            {"id": 86, "no": "86", "q": "Karena dipanaskan, kawat yang panjangnya 48 cm akan mengembang menjadi 52 cm. Setelah pemanasan, berapakah panjangnya kawat yang berukuran 72 cm?"},
            {"id": 87, "no": "87", "q": "Suatu pabrik dapat menghasilkan 304 batang pensil dalam waktu 8 jam. Berapa batangkah dihasilkan dalam waktu setengah jam?"},
            {"id": 88, "no": "88", "q": "Untuk suatu campuran diperlukan 2 bagian perak dan 3 bagian timah. Berapa gramkah perak yang diperlukan untuk mendapatkan campuran itu yang beratnya 15 gram?"},
            {"id": 89, "no": "89", "q": "Untuk setiap Rp 3,- yang dimiliki Sidin, Hamid memiliki Rp 5,- Jika mereka bersama mempunyai Rp 120,- berapa rupiahkah yang dimiliki Hamid?"},
            {"id": 90, "no": "90", "q": "Mesin A menenun 60 m kain, sedangkan mesin B menenun 40 m. Berapa meterkah yang ditenun mesin A, jika mesin B menenun 60 m?"},
            {"id": 91, "no": "91", "q": "Seseorang membelikan 1/10 dari uangnya untuk perangko dan 4 kali jumlah itu untuk alat tulis. Sisa uangnya masih Rp 60,- Berapa rupiahkah uang semula?"},
            {"id": 92, "no": "92", "q": "Di dalam dua peti terdapat 43 piring. Di dalam peti yang satu terdapat 9 piring lebih banyak dari pada di dalam peti yang lain. Berapa buah piring terdapat di dalam peti yang lebih kecil?"},
            {"id": 93, "no": "93", "q": "Suatu lembaran kain yang panjangnya 60 cm harus dibagikan sedemikian rupa sehingga panjangnya satu bagian ialah 2/3 dari bagian yang lain. Berapa panjangnya bagian yang terpendek?"},
            {"id": 94, "no": "94", "q": "Suatu perusahaan mengekspor ¾ dari hasil produksinya dan menjual 4/5 dari sisa itu dalam negeri. Berapa % kah hasil produksi yang masih tinggal?"},
            {"id": 95, "no": "95", "q": "Jika suatu botol berisi anggur hanya 7/8 bagian dan harganya ialah Rp 84,- berapakah harga anggur itu jika botol itu hanya terisi ½ penuh?"},
            {"id": 96, "no": "96", "q": "Di dalam suatu keluarga setiap anak perempuan mempunyai jumlah saudara laki-laki yang sama dengan jumlah saudara perempuan dan setiap anak laki-laki mempunyai dua kali lebih banyak saudara perempuan dari pada saudara laki-laki. Berapa anak laki-lakikah yang terdapat di dalam keluarga tersebut?"}
        ]

        with st.form("form_subtest_5"):
            for q in questions_ra:
                st.markdown(f"**Soal {q['no']}.** {q['q']}")
                st.session_state.answers[q['id']] = st.text_input(
                    f"Angka Jawaban No. {q['no']}:", 
                    key=f"ra_{q['id']}"
                )
                st.markdown("---")

            if st.form_submit_button("Simpan & Lanjut ke Subtes 6 (ZR) ➔"):
                st.session_state.current_subtest = 6
                st.rerun()
