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

def render_subtest_3_an():
    if "step_an" not in st.session_state:
        st.session_state.step_an = "instruction"
    if "answers" not in st.session_state:
        st.session_state.answers = {}

    if st.session_state.step_an == "instruction":
        st.title("📑 Petunjuk Subtes 03: AN (Hubungan Kata / Analogi)")
        st.info("💡 Bacalah petunjuk di bawah ini dengan teliti. **Timer belum berjalan di halaman ini.**")
        st.markdown("""
        ### Aturan Pengerjaan:
        Ditentukan tiga kata. Antara kata pertama dan kata kedua terdapat suatu hubungan tertentu. 
        Antara kata ketiga dan salah satu kata di antara 5 pilihan (a, b, c, d, e) harus pula terdapat **hubungan yang sama**.

        ---
        ### Contoh:
        **hutan : pohon = sawah : ...**  
        a) beras | b) petani | c) padi | d) tanah | e) basah  
        *Jawaban yang benar adalah* **c) padi** (karena hutan terdiri atas pohon, sawah terdiri atas padi).
        """)
        st.markdown("---")
        if st.button("Mulai Kerjakan Subtes 3 🚀", type="primary"):
            st.session_state.step_an = "test"
            st.session_state.start_time_an = time.time()
            st.rerun()

    elif st.session_state.step_an == "test":
        st.title("🧠 Subtes 03: AN (Hubungan Kata)")
        
        elapsed = int(time.time() - st.session_state.start_time_an)
        remaining = max(0, 420 - elapsed)
        show_live_timer_an(remaining)

        if remaining <= 0:
            st.warning("⏰ Waktu Subtes 3 telah habis! Mengalihkan ke Subtes 4...")
            for q_id in range(41, 61):
                if f"an_{q_id}" in st.session_state:
                    st.session_state.answers[q_id] = st.session_state[f"an_{q_id}"]
            time.sleep(1)
            st.session_state.current_subtest = 4
            st.rerun()

        questions_an = [
            {"id": 41, "no": "41", "q": "menemukan : menghilangkan = mengingat : ...", "opts": ["a) menghapal", "b) memikirkan", "c) melupakan", "d) membayangkan", "e) mengulas"]},
            {"id": 42, "no": "42", "q": "bunga : vas = burung : ...", "opts": ["a) sarang", "b) langit", "c) pohon", "d) dahan", "e) sangkar"]},
            {"id": 43, "no": "43", "q": "kereta api : rel = bus : ...", "opts": ["a) roda", "b) bensin", "c) sopir", "d) jalan raya", "e) stasiun"]},
            {"id": 44, "no": "44", "q": "sepatu : kaki = cincin : ...", "opts": ["a) tangan", "b) perhiasan", "c) emas", "d) gelang", "e) jari"]},
            {"id": 45, "no": "45", "q": "lingkaran : bola = bujur sangkar : ...", "opts": ["a) segi empat", "b) piramida", "c) balok", "d) kubus", "e) segi tiga"]},
            {"id": 46, "no": "46", "q": "meminta : mengemis = menyuruh : ...", "opts": ["a) menawarkan", "b) memaksa", "c) mengajak", "d) memerintah", "e) mengimbau"]},
            {"id": 47, "no": "47", "q": "bunga : layu = mentega : ...", "opts": ["a) cair", "b) asin", "c) manis", "d) tengik", "e) beku"]},
            {"id": 48, "no": "48", "q": "siang : malam = terang : ...", "opts": ["a) kelam", "b) sungai", "c) gelap", "d) awan", "e) senja"]},
            {"id": 49, "no": "49", "q": "helm : kepala = perisai : ...", "opts": ["a) dada", "b) perang", "c) senjata", "d) baju besi", "e) pelindung"]},
            {"id": 50, "no": "50", "q": "kayu : tukang kayu = emas : ...", "opts": ["a) tambang", "b) Perhiasan", "c) kaya", "d) tukang emas", "e) toko emas"]},
            {"id": 51, "no": "51", "q": "lukisan : pelukis = lagu : ...", "opts": ["a) penyanyi", "b) musik", "c) nada", "d) komponis", "e) panggung"]},
            {"id": 52, "no": "52", "q": "tangis : duka = tawa : ...", "opts": ["a) riang", "b) senyum", "c) kelakar", "d) gembira", "e) pesta"]},
            {"id": 53, "no": "53", "q": "cuaca : iklim = perasaan : ...", "opts": ["a) jiwa", "b) watak", "c) suasana hati", "d) fikiran", "e) emosi"]},
            {"id": 54, "no": "54", "q": "domba : bulu = ulat sutra : ...", "opts": ["a) kempis", "b) daun", "c) sutra", "d) kepompong", "e) benang"]},
            {"id": 55, "no": "55", "q": "tinggi nada : frekuensi = nyaring nada : ...", "opts": ["a) amplitudo", "b) ritme", "c) tempo", "d) panjang senar", "e) pemutar"]},
            {"id": 56, "no": "56", "q": "evolusi : revolusi = merayap : ...", "opts": ["a) berjalan", "b) berlari", "c) mutasi", "d) melompat", "e) terbang"]},
            {"id": 57, "no": "57", "q": "air : uap = es : ...", "opts": ["a) dingin", "b) beku", "c) es", "d) salju", "e) air"]},
            {"id": 58, "no": "58", "q": "pensil : diraut = pisau : ...", "opts": ["a) tajam", "b) memotong", "c) besi", "d) dikikir", "e) diasa"]},
            {"id": 59, "no": "59", "q": "kuman : mikroskop = bintang : ...", "opts": ["a) malam", "b) langit", "c) teropong", "d) masehi", "e) mikroskop"]},
            {"id": 60, "no": "60", "q": "api : kebakaran = banjir : ...", "opts": ["a) air", "b) hujan", "c) sungai", "d) bencana", "e) lautan api"]}
        ]

        with st.form("form_subtest_3"):
            for q in questions_an:
                st.markdown(f"**Soal {q['no']}.** {q['q']}")
                st.session_state.answers[q['id']] = st.radio(
                    f"Pilih Jawaban No. {q['no']}:",
                    options=q['opts'],
                    key=f"an_{q['id']}"
                )
                st.markdown("---")

            if st.form_submit_button("Simpan & Lanjut ke Subtes 4 (GE) ➔"):
                for q_id in range(41, 61):
                    if f"an_{q_id}" in st.session_state:
                        st.session_state.answers[q_id] = st.session_state[f"an_{q_id}"]
                st.session_state.current_subtest = 4
                st.rerun()
