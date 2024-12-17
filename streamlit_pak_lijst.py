import streamlit as st
import pandas as pd

# Titel
st.title(':blue-background[mr fresco pak lijst]')

# Inputvelden
pax = int(st.text_input("Aantal mensen?",value=100))
tijd = st.slider("Hoelang duurt de klus?", 0, 24)

# Kolommen voor selectie
eten_col, drinken_col, decoratie_col = st.columns(3)
eten_dict, drinken_dict, decoratie_dict = {},{},{}
with eten_col:
    eten_items = st.multiselect("Eten", [
        'Burger', 'Kipsate', 'Friet', 'Tortila', 'Biefstuk', 
        'Shortrib', 'Pasta', 'Salade', 'Bitterbal', 'Kaasstengel', 
        'Frikadel', 'Kaassoufle', 'Kipcorn', 'Erwtensoep', 
        'Curryworst', 'Curry'
    ])
    for item in eten_items:
        eten_dict[item] = pax


with drinken_col:
    drinken_items = st.multiselect("Drinken", [
        'Drankpakket alcohol', 'Drankpakket alcoholvrij', 
        'Chocomel', 'Glühwein'
    ])
    for item in drinken_items:
        drinken_dict[item] = pax

with decoratie_col:
    decoratie_items = st.multiselect("Decoratie", [
        'Statafels', 'Lichten'
    ])
    for item in decoratie_items:
        decoratie_dict[item] = pax
# Knop om aanpassingen te tonen
if st.checkbox("Aanpassingen"):
    st.write("### Geef hoeveelheden aan:")
    
    # Tweede kolom voor hoeveelheden
    hoeveelheden_col = st.columns(3)
    
    with hoeveelheden_col[0]:
        st.write("**Eten**")
        for item in eten_items:
            eten_dict[item] = st.number_input(f"{item}", value=eten_dict[item], min_value=0, step=1, key=f"eten_{item}")
    
    with hoeveelheden_col[1]:
        st.write("**Drinken**")
        for item in drinken_items:
            drinken_dict[item] = st.number_input(f"{item}", value=drinken_dict[item], min_value=0, step=1, key=f"drinken_{item}")

    with hoeveelheden_col[2]: 
        st.write("**Decoratie**")
        for item in decoratie_items:
            decoratie_dict[item] = st.number_input(f"{item}", value=decoratie_dict[item], min_value=0, step=1, key=f"decoratie_{item}")

    # Toon een overzicht van de ingevoerde hoeveelheden
    st.write("### Overzicht hoeveelheden:")
    data = {
        "Categorie": [],
        "Item": [],
        "Hoeveelheid": []
    }
    
    for item, qty in eten_dict.items():
        data["Categorie"].append("Eten")
        data["Item"].append(item)
        data["Hoeveelheid"].append(qty)
    
    for item, qty in drinken_dict.items():
        data["Categorie"].append("Drinken")
        data["Item"].append(item)
        data["Hoeveelheid"].append(qty)
    
    for item, qty in decoratie_dict.items():
        data["Categorie"].append("Decoratie")
        data["Item"].append(item)
        data["Hoeveelheid"].append(qty)
    
    df = pd.DataFrame(data)
    st.table(df)