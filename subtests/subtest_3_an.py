import streamlit as st
import streamlit.components.v1 as components
import time

def show_live_timer_an(seconds_remaining):
    components.html(f"""
    <div style="font-family: Arial, sans-serif; font-size: 20px; font-weight: bold; color: #d9534f; 
                background-color: #fdf7f7; padding: 10px 15px; border: 2px solid #d9534f; 
                border-radius: 8px; text-align: center; margin-bottom: 10px;">
        ⏱️ SISA WAKTU SUBTES 3 (AN): <span id="timer_display_an">--:--</span>
    </div>
    <script>
        var timeLeft = {seconds_remaining};
        function updateDisplay() {{
            var m = Math.floor(timeLeft / 60);
            var s = timeLeft % 60;
            var displayM = m < 10 ? "0" + m : m;
            var displayS = s < 10 ? "0" + s : s;
            var elem = document.getElementById("timer_display_an");
            if (elem) {{ elem.innerHTML = displayM + ":" + displayS; }}
            if (timeLeft <= 0) {{ if (elem) elem.innerHTML = "00:00 (WAKTU HABIS)"; }}
            else {{ timeLeft--; }}
        }}
        updateDisplay();
        setInterval(updateDisplay, 1000);
    </script>
    """, height=75)

def render_subtest_3_an():
    if "step_an" not in st.session_state:
        st.session_state.step_an = "instruction"
    if "answers" not in st.session_state:
        st.session_state.answers = {}

    # TAHAP 1: INSTRUKSI & SELURUH CONTOH (TANPA TIMER)
    if st.session_state.step_an == "instruction":
        st.title("📑 Petunjuk Subtes 03: AN (Analogi Kata)")
        st.info("💡 Bacalah seluruh petunjuk dan contoh di bawah ini. **Timer belum berjalan di halaman ini.**")
        st.markdown("""
        ### Aturan Pengerjaan:
        Ditentukan 3 (tiga) kata. Antara kata pertama dan kata kedua terdapat suatu hubungan tertentu. 
        Antara kata ketiga dan salah satu di antara lima kata pilihan harus pula terdapat **hubungan yang sama** itu. Carilah kata tersebut!

        ---
        ### Contoh 01:
        **Hutan : pohon = tembok : ?**
        * a) batu bata
        * b) rumah
        * c) semen
        * d) putih
        * e) dinding

        **Penjelasan:** Hubungan antara *hutan* dan *pohon* ialah bahwa hutan terdiri atas pohon-pohon. Maka hubungan antara *tembok* dan salah satu kata pilihan ialah bahwa tembok terdiri atas batu-batu bata.  
        **Jawaban yang benar:** **a) batu bata**

        ---
        ### Contoh 02:
        **Gelap : terang = basah : ?**
        * a) hujan
        * b) hari
        * c) lembab
        * d) angin
        * e) kering

        **Penjelasan:** *Gelap* adalah lawan kata dari *terang*, maka untuk *basah* lawannya ialah *kering*.  
        **Jawaban yang benar:** **e) kering**
        """)
        st.markdown("---")
        if st.button("Mulai Kerjakan Subtes 3 🚀", type="primary"):
            st.session_state.step_an = "test"
            st.session_state.start_time_an = time.time()
            st.rerun()

    # TAHAP 2: PENGERJAAN SOAL (TIMER 7 MENIT BERJALAN)
    elif st.session_state.step_an == "test":
        st.title("🧠 Subtes 03: AN (Analogi Kata)")
        
        # Alokasi resmi Subtes 3 AN = 7 Menit (420 Detik)
        elapsed = int(time.time() - st.session_state.start_time_an)
        remaining = max(0, 420 - elapsed)
        show_live_timer_an(remaining)

        if remaining == 0:
            st.warning("⏰ Waktu Subtes 3 telah habis!")
            if st.button("Selesaikan Ujian ➔"):
                st.session_state.current_subtest = 4
                st.rerun()
            st.stop()

        questions_an = [
            {"id": 41, "no": "41", "q": "Menemukan : menghilangkan = Mengingat : ?", "options": ["a) menghapal", "b) mengenai", "c) melupakan", "d) berpikir", "e) memimpikan"]},
            {"id": 42, "no": "42", "q": "Bunga : jambangan = Burung : ?", "options": ["a) sarang", "b) langit", "c) pagar", "d) pohon", "e) sangkar"]},
            {"id": 43, "no": "43", "q": "Kereta api : rel = Otobis : ?", "options": ["a) roda", "b) poros", "c) ban", "d) jalan raya", "e) kecepatan"]},
            {"id": 44, "no": "44", "q": "Perak : emas = Cincin : ?", "options": ["a) arloji", "b) berlian", "c) permata", "d) gelang", "e) platina"]},
            {"id": 45, "no": "45", "q": "Lingkaran : bola = Bujur sangkar : ?", "options": ["a) bentuk", "b) gambar", "c) segi empat", "d) kubus", "e) piramida"]},
            {"id": 46, "no": "46", "q": "Saran : kepustakaan = Merundingkan : ?", "options": ["a) menawarkan", "b) menentukan", "c) menilai", "d) menimbang", "e) merenungkan"]},
            {"id": 47, "no": "47", "q": "Lidah : asam = Hidung : ?", "options": ["a) mencium", "b) bernapas", "c) mengecap", "d) tengik", "e) asin"]},
            {"id": 48, "no": "48", "q": "Darah : pembuluh = Air : ?", "options": ["a) pintu air", "b) sungai", "c) talang", "d) hujan", "e) ember"]},
            {"id": 49, "no": "49", "q": "Saraf : penyalur = Pupil : ?", "options": ["a) penyinaran", "b) mata", "c) melihat", "d) cahaya", "e) pelindung"]},
            {"id": 50, "no": "50", "q": "Pengantar surat : pengantar telegram = Pandai besi : ?", "options": ["a) palu godam", "b) pedagang besi", "c) api", "d) tukang emas", "e) besi tempa"]},
            {"id": 51, "no": "51", "q": "Buta : warna = Tuli : ?", "options": ["a) pendengaran", "b) mendengar", "c) nada", "d) kata", "e) telinga"]},
            {"id": 52, "no": "52", "q": "Makanan : bumbu = Ceramah : ?", "options": ["a) penghinaan", "b) pidato", "c) kelakar", "d) kesan", "e) ayat"]},
            {"id": 53, "no": "53", "q": "Marah : emosi = Duka cita : ?", "options": ["a) suka cita", "b) sakit hati", "c) suasana hati", "d) sedih", "e) rindu"]},
            {"id": 54, "no": "54", "q": "Mantel : jubah = Wool : ?", "options": ["a) bahan sandang", "b) domba", "c) sutra", "d) jas", "e) tekstil"]},
            {"id": 55, "no": "55", "q": "Ketinggian puncak : tekanan udara = Ketinggian nada : ?", "options": ["a) garpu tala", "b) sopran", "c) nyanyian", "d) panjang senar", "e) suara"]},
            {"id": 56, "no": "56", "q": "Negara : revolusi = Hidup : ?", "options": ["a) biologi", "b) keturunan", "c) mutasi", "d) seleksi", "e) ilmu hewan"]},
            {"id": 57, "no": "57", "q": "Kekurangan : penemuan = Panas : ?", "options": ["a) haus", "b) khatulistiwa", "c) es", "d) matahari", "e) dingin"]},
            {"id": 58, "no": "58", "q": "Kayu : diketam = Besi : ?", "options": ["a) dipalu", "b) digergaji", "c) dituang", "d) dikikir", "e) ditempa"]},
            {"id": 59, "no": "59", "q": "Olahragawan : lembing = Cendekiawan : ?", "options": ["a) perpustakaan", "b) penelitian", "c) karya", "d) studi", "e) mikroskop"]},
            {"id": 60, "no": "60", "q": "Keledai : kuda pacuan = Pembakaran : ?", "options": ["a) pemadam api", "b) obor", "c) letupan", "d) korek api", "e) lautan api"]}
        ]

        with st.form("form_subtest_3"):
            for q in questions_an:
                st.markdown(f"**Soal {q['no']}.** {q['q']}")
                st.session_state.answers[q['id']] = st.radio(
                    f"Pilih jawaban No. {q['no']}:", 
                    options=q['options'], 
                    key=f"an_{q['id']}"
                )
                st.markdown("---")

            if st.form_submit_button("Simpan & Selesaikan Ujian ➔"):
                st.session_state.current_subtest = 4
                st.rerun()
