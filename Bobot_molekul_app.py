import streamlit as st
st.set_page_bobot molekul(page_tittle="Bobot Molekul Senyawa Kimia", page_icon="👩🏻‍🔬")

st.tittle("a captivating summary:sunglasses:")
# Definisikan fungsi untuk melakukan login
def login():
    username = --
    password = --
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
        tabel_periodik = {
            'H': 1.008,
            'He': 4.003,
            'Li': 6.941,
            'Be': 9.012,
            'B': 10.811,
            'C': 12.011,
            'N': 14.007,
            'O': 15.999,
            'F': 18.998,
            'Ne': 20.179,
            'Na': 22.989,
            'Mg': 24.305,
            'Al': 26.981,
            'Si': 28.085,
            'P': 30.973,
            'S': 32.065,
            'Cl': 34.453,
            'Ar': 39.948,
            'K': 39.098,
            'Ca': 40.078,
            'Sc': 44.955,
            'Ti': 47.867,
            'V': 50.941,
            'Cr': 51.996,
            'Mn': 54.938,
            'Fe': 55.845,
            'Co': 58.933,
            'Ni': 58.693,
            'Cu': 63.546,
            'Zn': 65.380,
            'Ga': 69.723,
            'Ge': 72.640,
            'As': 74.921,
            'Se': 78.960,
            'Br': 79.904,
            'Kr': 83.798,
            'Rb': 85.467,
            'Sr': 87.620,
            'Y': 88.905,
            'Zr': 91.224,
            'Nb': 92.906,
            'Mo': 94.960,
            'Ru': 101.070,
            'Rh': 102.905,
            'Pd': 106.420,
            'Ag': 107.868,
            'Cd': 112.411,
            'In': 114.818,
            'Sn': 118.710,
            'Sb': 121.760,
            'Te': 120.600,
            'I': 126.904,
            'Xe': 131.293,
            'Cs': 132.965,
            'Ba': 137.327,
            'La': 138.905,
            'Ce': 140.116,
            'Pr': 140.907,
            'Nd': 144.242,
            'Sm': 150.360,
            'Eu': 151.963,
            'Gd': 157.250,
            'Tb': 158.925,
            'Dy': 162.500,
            'Ho': 164.930,
            'Er': 167.259,
            'Tm': 168.934,
            'Yb': 173.054,
            'Lu': 174.966,
            'Hf': 178.490,
            'Ta': 180.947,
            'W': 183.840,
            'Re': 186.207,
            'Os': 190.230,
            'Ir': 192.217,
            'Pt': 195.084,
            'Au': 196.966,
            'Ag': 200.590,
            'Tl': 204.383,
            'Pb': 207.200,
            'Bi': 208.980,
            'Th': 232.038,
            'Pa': 231.035,
            'U': 238.028,
        
# Menampilkan judul dan instruksi latihan soal
        st.tittle("Latihan Soal Mudah")
        st.write("Silakan kerjakan latihan soal tersebut"):
        
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
    ---
    <style>
    .footer { 
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
        <p>o 2024 Hak Cipta</p>
    </div>
    ---
    , unsafe_allow_htm1=True)


