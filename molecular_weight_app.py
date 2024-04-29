import streamlit as st

from mendeleev import element

def

calculate_molecular_weight(formula):

    elements = []

    count = 0

    current_element = ""

    for char in formula :

        if char.issuper():

            if current_element:

elements.append((current_element, count if count > 0 else 1))

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

sum(element(e).atomic_weight * n for e, n in element)

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

