import re, random
import streamlit as st
# LAPORAN AKHIR LPK
# TUGAS AKHIR LKP

data_unsur = {
    'H' :1.008,   'He':4.003,   'Li':6.941,   'Be':9.012,   'B' :10.811,  'C':12.011,   'N' :14.007,  'O' :15.999,  'F' :18.998,  'Ne':20.179,
    'Na':22.989,  'Mg':24.305,  'Al':26.981,  'Si':28.085,  'P' :30.973,  'S':32.065,   'Cl':34.453,  'Ar':39.948,  'K' :39.098,  'Ca':40.078,
    'Sc':44.955,  'Ti':47.867,  'V' :50.941,  'Cr':51.996,  'Mn':54.938,  'Fe':55.845,  'Co':58.933,  'Ni':58.693,  'Cu':63.546,  'Zn':65.380,
    'Ga':69.723,  'Ge':72.640,  'As':74.921,  'Se':78.960,  'Br':79.904,  'Kr':83.798,  'Rb':85.467,  'Sr':87.620,  'Y' :88.905,  'Zr':91.224,
    'Nb':92.906,  'Mo':94.960,  'Ru':101.070, 'Rh':102.905, 'Pd':106.420, 'Ag':107.868, 'Cd':112.411, 'In':114.818, 'Sn':118.710, 'Sb':121.760,
    'Te':120.600, 'I' :126.904, 'Xe':131.293, 'Cs':132.965, 'Ba':137.327, 'La':138.905, 'Ce':140.116, 'Pr':140.907, 'Nd':144.242, 'Sm':150.360,
    'Eu':151.963, 'Gd':157.250, 'Tb':158.925, 'Dy':162.500, 'Ho':164.930, 'Er':167.259, 'Tm':168.934, 'Yb':173.054, 'Lu':174.966, 'Hf':178.490,
    'Ta':180.947, 'W' :183.840, 'Re':186.207, 'Os':190.230, 'Ir':192.217, 'Pt':195.084, 'Au':196.966, 'Ag':200.590, 'Tl':204.383, 'Pb':207.200,
    'Bi':208.980, 'Th':232.038, 'Pa':231.035, 'U' :238.028}

def isPunyaAngka(string:str):
    punyaHuruf, punyaAngka = False, False
    for _ in str(string):
        if str(_).isalpha() : punyaHuruf = True
    for _ in str(string):
        if str(_).isdigit() : punyaAngka = True
    return(True if punyaHuruf and punyaAngka else False)

def DaftarSenyawa(senyawa):
    all_data = {}
    pengelompokan_senyawa = re.findall(r'[A-Z][a-z]?\d*', senyawa)
    for _ in pengelompokan_senyawa:
        if not isPunyaAngka(_):
            if _ not in list(all_data.keys()): all_data[_] = 1
            else: all_data[_] += 1
        else:
            unsur  = str(re.search(r'[A-Za-z]+', _).group())
            jumlah = int(re.search(r'\d+', str(_)).group())
            if unsur not in list(all_data.keys()): all_data[unsur] = jumlah
            else: all_data[unsur] += jumlah
    return(all_data)

def CalculateMass(data):
    nomor_atom, nomor_massa = 0, 0
    for _ in list(data.values()): nomor_atom += _
    for a, b in data.items(): nomor_massa += float(b*data_unsur[a])
    return(nomor_atom, nomor_massa)

def Display(data):
    st.write('')
    st.write('')
    st.write('Senyawa tersebut terdiri atas : ')
    for a, b in data.items():
        st.write('{} unsur {}'.format(str(b), str(a)))

def MenuUtama():
    pilihan = st.sidebar.selectbox('Menu', ['Hallo Teman AKA We Here For You', 'Anggota Kelompok', 'Daftar Unsur', 'Kalkulator Senyawa', 'Rumus dan Contoh Soal', 'Latihan Soal'])
    if pilihan == 'Hallo Teman AKA We Here For You': Landing()
    elif pilihan == 'Anggota Kelompok': Anggota()
    elif pilihan == 'Daftar Unsur': DisplayUnsur()
    elif pilihan == 'Kalkulator Senyawa': KalkulatorPintar()
    elif pilihan == 'Rumus dan Contoh Soal': Rumus()
    elif pilihan == 'Latihan Soal': Latsol()

def Landing():
    st.title('Hallo Teman AKA We Here For You👩🏻‍🔬🧪')
    st.subheader('', divider='rainbow')
    st.write ('Massa molekul relatif adalah gabungan penjumlahan nilai massa atom relatif (Ar) dari atom-atom pembentuk molekul tersebut. Massa molekul relatif juga dapat didefinisikan sebagai perbandingan massa antara 1 molekul atau 1 satuan dari suatu zat terhadap 112 massa satu atom isotop karbon 12.')
    st.write ('Aplikasi ini merupakan aplikasi untuk menentukan Bobot Molekul senyawa kimia berdasarkan penjumlahan nomor atom yang diketahui, cukup dengan memasukkan senyawa kimia dengan tepat akan muncul hasil Bobot Molekul yang diinginkan')
    st.subheader('', divider='rainbow')
    st.title ('Selamat Mengerjakan🤩✊🏻')
    
def Anggota():
    st.title('👋🏻Anggota Kelompok👋🏻')
    st.subheader('', divider='rainbow')
    st.write("""
    1. Anisa Imanda Sirais (2360071)\n
    2. Aulia Qosimul Qisti(2360080)\n
    3. Cindy Nurfadila(2360091)\n
    4. Linda Gusdiantini(2360162)\n
    5. Wisnu Yanindra Kusuma(2360290)\n
    """)
    st.header('🫧Quotes🫧')
    st.write('Beautiful result do not come from easy steps, so never give up, keep trying, believe in your own abilities👩🏻‍💻👨🏼‍💻')
    st.subheader('', divider='rainbow')
    st.write('🧚🏻💃🏻🧜🏻🙆🏻‍♀️👩🏻‍🎓👨🏻‍🔬🧕🏻🦋🐣☘️💐')


def DisplayUnsur():
    st.title('📍Daftar Unsur Kimia📍')
    st.subheader('', divider='rainbow')
    st.write('')
    col1, col2, col3, col4 = st.columns(4, gap='small')
    daftar_data_unsur = list(data_unsur.items())
    daftar_data_unsur.insert(50,('I',126.904))
    with col1:
        for i in range(0,21):
            st.write('{} : {}'.format(daftar_data_unsur[i][0], daftar_data_unsur[i][1]))
    with col2:
        for i in range(21,42):
            st.write('{} : {}'.format(daftar_data_unsur[i][0], daftar_data_unsur[i][1]))
    with col3:
        for i in range(42,63):
            st.write('{} : {}'.format(daftar_data_unsur[i][0], daftar_data_unsur[i][1]))
    with col4:
        for i in range(63,84):
            st.write('{} : {}'.format(daftar_data_unsur[i][0], daftar_data_unsur[i][1]))

def KalkulatorPintar():
    senyawa = st.text_input('MASUKKAN SENYAWA DENGAN BENAR❗❗')
    st.subheader('', divider='rainbow')
    st.subheader('', divider='rainbow')
    if senyawa == '': pass
    else:
        try:
            data = DaftarSenyawa(senyawa)
            nomor_atom, nomor_massa = CalculateMass(data)
            st.title(senyawa)
            Display(data)
            st.write('')
            st.write('')
            st.write('Jumlah Senyawa : {}'.format(int(nomor_atom)))
            st.write('Bobot Molekul  : {} gr/mol'.format(nomor_massa))
        except Exception:
            st.write('Maaf, sepertinya anda memasukkan senyawa yang salah')

def Rumus():
    st.title('Rumus dan Contoh Soal✍🏻❕❕')
    st.subheader('', divider='rainbow')
    st.header('📌Rumus📌')
    st.write (""" Massa Molekul Relatif\n
    Mr molekul AxBy = (x. Ar A) + (y. Ar B) + dst')\n
    """)
    st.header('🧮Contoh soal🧮')
    st.write(""" Hitunglah massa molekul relatif senyawa (NH2)4SO4, jika diketahui Ar H = 1, N =14, O = 16, dan S = 32.\n
    Pembahasan\n
    Mr (NH2)4SO4 = (2 x Ar N) + (2 x 4 x Ar H) + (1 x Ar S) + (4 x Ar O)\n
    = (2 x 14) + (8 x 1) + (1 x 32) + (4 x 16)\n
    = 30n = 60\n
    = 132\n
    """)

def ControlSoal():
    GS = Soal()
    soal, senyawa, jawaban, jawaban_rinci = GS.MenuSoal()
    st.write(soal)
    st.subheader(senyawa)
    st.write('')
    jawaban_user = st.text_input('Masukkan {} {}'.format(str(soal.split(' ')[1]), str(soal.split(' ')[2])))
    return(soal, senyawa, jawaban, jawaban_rinci, jawaban_user)

if 'generate_button' not in st.session_state: st.session_state.generate_button = False
if 'submit_button'   not in st.session_state: st.session_state.submit_button   = False

def Latsol():
    generate_button = st.button('Generate')
    st.write('')
    if generate_button:
        SimpanSoal()
    if st.session_state.generate_button and st.session_state.generate_button is not None:
        data = st.session_state.soal_sementara
        print(data)
        DisplaySoal(data.get('soal'), data.get('senyawa'))
        jawaban_user = st.text_input('Masukkan jawaban')
        submit_button = st.button('Submit')
        if submit_button:
            afkhBenar = CheckJawabanUser(jawaban_user, data.get('jawaban'))
            if afkhBenar:
                st.subheader('Jawaban anda benar!')
                st.write('Jawaban yang lebih rinci adalah {}'.format(str(data.get('jawaban_rinci'))))
            else:
                st.subheader('Maaf, jawaban anda salah')
                st.write('Jawaban yang benar adalah {}'.format(str(data.get('jawaban_rinci'))))

def DisplaySoal(soal, senyawa):
    st.write(soal)
    st.subheader(senyawa)
    st.write('') 

def SimpanSoal():
    st.session_state.generate_button = True
    GS = Soal()
    soal, senyawa, jawaban, jawaban_rinci = GS.MenuSoal()
    data = {'soal':soal, 'senyawa':senyawa, 'jawaban':jawaban, 'jawaban_rinci':jawaban_rinci}
    st.session_state.soal_sementara = data

def CheckJawabanUser(jawaban_user, jawaban):
    try:
        jaw = int(float(jawaban_user))
        print(jaw)
        if jaw in jawaban: return(True)
        else: return(False)
    except Exception: return(False)

class Soal():

    def __init__(self):
        self.nama_unsur = list(data_unsur.keys())
        self.nama_unsur.insert(50,'I')

    def MenuSoal(self):
        soal, senyawa, jawaban, jawaban_rinci = random.choice([self.SoalTipe1(),self.SoalTipe2()])
        return(soal, senyawa, jawaban, jawaban_rinci)

    def SoalTipe1(self):
        senyawa, nomor_atom, nomor_massa = self.RandomizerSenyawa()
        soal = 'Berapa jumlah atom dari senyawa berikut'
        jawaban = [int(nomor_atom)]
        jawaban_rinci = int(nomor_atom)
        return(soal, senyawa, jawaban, jawaban_rinci)

    def SoalTipe2(self):
        senyawa, nomor_atom, nomor_massa = self.RandomizerSenyawa()
        soal = 'Berapa jumlah massa dari senyawa berikut'
        jawaban = [int(nomor_massa)-1, int(nomor_massa), int(nomor_massa)+1]
        jawaban_rinci = nomor_massa
        return(soal, senyawa, jawaban, jawaban_rinci)

    def RandomizerSenyawa(self):
        kode_senyawa = ''.join(['{}{}'.format(str(random.choice(self.nama_unsur)),str(random.randint(2,12) if random.choice([True,False]) else '')) for i in range(random.randint(2,5))])
        nomor_atom, nomor_massa = self.GetJawaban(DaftarSenyawa(kode_senyawa))
        return(kode_senyawa, nomor_atom, nomor_massa)

    def GetJawaban(self, data):
        nomor_atom, nomor_massa = 0, 0
        for _ in list(data.values()): nomor_atom += _
        for a, b in data.items(): nomor_massa += float(b*data_unsur[a])
        return(nomor_atom, nomor_massa)

if __name__ == '__main__':
    MenuUtama()

