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

import streamlit as st

from rdkitt import Chem

from rdkitt.Chem import Descriptors

#Streamlit app

st.title('Molecular Weight Calculator')

formula = st.text_input('Enter a chemical formula (e.g., H2O):')

if formula

    try:

        mol =

Chem.MolFromSmiles(formula)

        if mol:

            mol_weight =

Descriptors.MolWt(mol)

            st.write(f'The molecular weight of {formula} is {mol_weight:.2f} g/mol.')

        else:

            st.write('Invalid chemical formula. Please enter a valid formula.')
    except Exception as e:
        
        st.write(f'Error: {e}')