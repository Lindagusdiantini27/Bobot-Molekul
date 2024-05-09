import streamlit as st
st.set_page_config(page_title="Bobot Molekul Senyawa Kimia", page_icon="👩🏻‍🔬")

st.tittle("a captivating summary:sunglasses:")
# Definisikan fungsi untuk melakukan login
def login():
    username = ""
    password = ""
    with st.form("login_form"):
        st.image("cover.jpg")
        username = st.text_input("username")
        password = st.text_input("password", type="password")
        submit_button = st.form_submit_button("login")
    return username, password, submit_button

# Cek apakah session sudah terdaftar
if "login" not in st.session_state:
    st.session_state.login = False

# Tampilkan form login jika belum login
if not st.session_state.login:
    username, password, submit_button = login()
    if submit_button:
        if username == "Teman Kita" and password == "teman321":
            st.success("login berhasil")
            # Set session Login ke True
            st.session_state.login = True
            # Tampilkan konten aplikasi setelah login berhasil 

        else:
            st.warning("Username atau Password salah.")

# Tampilkan konten setelah login berhasil
else:
    st.sidebar.image("aka.png")
    username = "Teman Kita"
    st.sidebar.markdown(f"welcome, {username}👋🏻!")
    pilihan = st.sidebar.selectbox("Pilih", ["Dashboard", "Bobot Molekul", "Latihan Soal"])

    # Tampilkan konten aplikasi setelah login berhasil
            #Bobot Molekul
    if pilihan == "Bobot Molekul":
        st.header("Bobot Molekul")
        st.write('''H : 1.008,''')
        st.write('''He: 4.003,''')
        st.write('''Li: 6.941,''')
        st.write('''Be: 9.012,''')
        st.write('''B: 10.811,''')
        st.write('''C: 12.011,''')
        st.write('''N: 14.007,''')
        st.write('''O: 15.999,''')
        st.write('''F: 18.998,''')
        st.write('''Ne: 20.179,''')
        st.write('''Na: 22.989,''')
        st.write('''Mg: 24.305,''')
        st.write('''Al: 26.981,''')
        st.write('''Si: 28.085,''')
        st.write('''P: 30.973,''')
        st.write('''S: 32.065,''')
        st.write('''Cl: 34.453,''')
        st.write('''Ar: 39.948,''')
        st.write('''K: 39.098,''')
        st.write('''Ca: 40.078,''')
        st.write('''Sc: 44.955,''')
        st.write('''Ti: 47.867,''')
        st.write('''V: 50.941,''')
        st.write('''Cr: 51.996,''')
        st.write('''Mn: 54.938,''')
        st.write('''Fe: 55.845,''')
        st.write('''Co: 58.933,''')
        st.write('''Ni: 58.693,''')
        st.write('''Cu: 63.546,''')
        st.write('''Zn: 65.380,''')
        st.write('''Ga: 69.723,''')
        st.write('''Ge: 72.640,''')
        st.write('''As: 74.921,''')
        st.write('''Se: 78.960,''')
        st.write('''Br: 79.904,''')
        st.write('''Kr: 83.798,''')
        st.write('''Rb: 85.467,''')
        st.write('''Sr: 87.620,''')
        st.write('''Y: 88.905,''')
        st.write('''Zr: 91.224,''')
        st.write('''Nb: 92.906,''')
        st.write('''Mo: 94.960,''')
        st.write('''Ru: 101.070,''')
        st.write('''Rh: 102.905,''')
        st.write('''Pd: 106.420,''')
        st.write('''Ag: 107.868,''')
        st.write('''Cd: 112.411,''')
        st.write('''In: 114.818,''')
        st.write('''Sn: 118.710,''')
        st.write('''Sb: 121.760,''')
        st.write('''Te: 120.600,''')
        st.write('''I: 126.904,''')
        st.write('''Xe: 131.293,''')
        st.write('''Cs: 132.965,''')
        st.write('''Ba: 137.327,''')
        st.write('''La: 138.905,''')
        st.write('''Ce: 140.116,''')
        st.write('''Pr: 140.907,''')
        st.write('''Nd: 144.242,''')
        st.write('''Sm: 150.360,''')
        st.write('''Eu: 151.963,''')
        st.write('''Gd: 157.250,''')
        st.write('''Tb: 158.925,''')
        st.write('''Dy: 162.500,''')
        st.write('''Ho: 164.930,''')
        st.write('''Er: 167.259,''')
        st.write('''Tm: 168.934,''')
        st.write('''Yb: 173.054,''')
        st.write('''Lu: 174.966,''')
        st.write('''Hf: 178.490,''')
        st.write('''Ta: 180.947,''')
        st.write('''W: 183.840,''')
        st.write('''Re: 186.207,''')
        st.write('''Os: 190.230,''')
        st.write('''Ir: 192.217,''')
        st.write('''Pt: 195.084,''')
        st.write('''Au: 196.966,''')
        st.write('''Ag: 200.590,''')
        st.write('''Tl: 204.383,''')
        st.write('''Pb: 207.200,''')
        st.write('''Bi: 208.980,''')
        st.write('''Th: 232.038,''')
        st.write('''Pa: 231.035,''')
        st.write('''U: 238.028,''')
        
# Menampilkan judul dan instruksi latihan soal
        st.tittle("Latihan Soal Mudah")
        st.write("Silahkan kerjakan latihan soal tersebut:")
        
# Menampilkan setiap pertanyaan dan meminta jawaban dari pengguna
        score = 0
        for question, answer in question.items():
            user_answer = st.text_input(f"Pertanyaan: {question}")
        else:
            st.write("Jawaban Anda salah.")
            st.write(f"Jawaban yang benar adalah: {answer}")
                    
        st.write("")

# Penghapus 
        st.write("...")

# Menampilkan skor akhir
        st.write(f"skor akhir Anda adalah {score} dari {len(questions)} soal.")
st.markdown(
    
    """
    (style)
    footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        text-align: right;
        padding: Spx;
    }
    </style>
    ---
    , unsafe_allow_htm1=True)
st.markdown(
    ---

    <div class="footer">
        <p>Dibuat oleh: Kelompok 3</p>
        <p>Versi: 1.0</p>
        <p>o 2024 Hak Cipta</p>
    </div>
    ---
    , unsafe_allow_htm1=True)
    """


