import streamlit as st

from mendeleev import element

def calculate_molecular_weight(formula):

    elements = []

    count = 0

    current_element = ""

    for char in formula :

        if char.issuper():

        if current_element:

elements.append((current_element, count if count>0 else 1))

            current_element = char 

            count = 0

        elif char.islower():

            current_element += char

        elif char.isdigit():

            count = count * 10 +

int(char)

    if current_element:

elements.append((current_element, count if count > 0 else 1))

    molecular_weight =

sum(element(e).atomic_weight * n for e, n in elements)

    return molecular_weight

#Streamlit app

st.title("Molecular Weight Calculator")

formula = st.text_input("Enter a chemical formula (e.g., H2O):")

if formula:

    try:

        molecular_weight = 

calculate_molecular_weight(formula)

        st.write(f"The molecular weight of {formula} is {molecular_weight:.2f} g/mol.")

    except Exception as e:

        st.write(f"Error: {e}")

import re

def hitung_bobot_molekul(formula):

    tabel_periodik = {

        'H': 1.088,

        'C': 12.011,

        'O': 15.999,

        'N': 14.007,

        'He': 4.003,

        'Li': 6.941,

        'Be': 9.012,

        'B': 10.811,

        'F': 18.998,

        'Ne': 20.180,

        'Na': 22.990,

        'Mg': 24.305,

        'Al': 26.982,

        'Si': 28.086,

        'P': 30.974,

        'S': 32.065,

        'Cl': 35.453,

        'Ar': 39.948,

        'K': 39.098,

        'Ca': 40.078,

        'Sc': 44.956,

        'Ti': 47.867,

        'V': 50.942,

        'Cr': 51.996,

        'Mn': 54.938,

        'Fe': 55.845,

        'Co': 58.933,

        'Ni': 58.693,

        'Cu': 63.546,

        'Zn': 65.380,

        'Ga': 69.723,

        'Ge': 72.640,

        'As': 74.922,

        'Se': 78.960,

        'Br': 79.904,

        'Kr': 83.798,

        'Rb': 85.467,

        'Sr': 87.620,

        'Y': 88.906,

        'Zr': 91.224,

        'Nb': 92.906,

        'Mo': 95.960,

        'Ru': 101.070,

        'Rh': 102.906,

        'Pd': 106.420,

        'Ag': 107.868,

        'Cd': 112.411,

        'In': 114.818,

        'Sn': 118.710,

        'Sb': 121.760,

        'Te': 127.600,

        'I': 126.904,

        'Xe': 131.293,

        'Cs': 132.905,

        'Ba': 137.327,

        'La': 138.905,

        'Ce': 140.116,

        'Pr': 140.908,

        'Nd': 144.242,

        'Sm': 150.360,

        'Eu': 151.964,

        'Gd': 157.250,

        'Tb': 158.926,

        'Dy': 162.500,

        'Ho': 164.930,

        'Er': 167.259,

        'Tm': 168.934,

        'Yb': 173.054,

        'Lu': 174.967,

        'Hf': 178.490,

        'Ta': 180.948,

        'W': 183.840,

        'Re': 186.207,

        'Os': 190.230,

        'Ir': 192.217,

        'Pt': 195.084,

        'Au': 196.966,

        'Hg': 200.590,

        'Tl': 204.383,

        'Pb': 207.200,

        'Bi': 208.980,

        'Th': 232.038,

        'Pa': 231.036,

        'U': 238.029, 

     # tambahkan atom-atom lainnya sesuai kebutuhan 
    
    }

    def hitung_bobot_molekul(atom, jumlah):

        return tabel_periodik[atom]*jumlah

    pattern = r'([A-Z][a-z]*)(\d*)'

    atom_jumlah = 

re.findall(pattern, formula)

    bobot_total = 0

    for atom, jumlah in atom_jumlah:

        jumlah = int(jumlah) if

jumlah else 1

        bobot_total +=

hitung_bobot_atom(atom, jumlah)

    return bobot_total

formula_molekul = 'H2O'

bobot = 

hitung_bobot_molekul(formula_molekul)

print(f'Bobot molekul {foemula_molekul}: {bobot}')

