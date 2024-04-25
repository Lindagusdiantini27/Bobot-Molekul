impor  streamlit as st

st.title('Test Running Streamlit')

def hitung_bobot_molekul(senyawa):
    
    mol = formula(senyawa)

    return mol.mass

def main():
    
    senyawa = input('Masukkan rumus senyawa kimia:')

    try:
        bobot_molekul = 

hitung_bobot_molekul(senyawa)

        print(f'Bobot molekul dari {senyawa} adalah {bobot_molekul:.2f}g/mol')

        except:

            print('Terjadi kesalahan dalam menghitung bobot molekul. Pastikan rumus senyawa benar.')

if __name__ == '__main__':
    main()

