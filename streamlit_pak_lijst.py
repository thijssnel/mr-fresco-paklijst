import streamlit as st
import pandas as pd
import streamlit as st
from math import ceil

# Titel en logo in kolommen
col1, col2 = st.columns([2, 1])  # Verdeling van kolommen: 1 deel logo, 6 delen titel

with col2:
    st.image("logo.png", width=50)  # Voeg het pad naar je logo toe en pas de breedte aan

with col1:
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
        'Shortrib', 'Pasta', 'Salade', 'Bittergarnituur', 'Erwtensoep', 
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

ingrediënten_dict, spullen_dict, drank_dict = {},{},{}

# Configuratie: Ingrediënten per gerecht
recepten = {
    'Burger': {
        'hamburger': 1,
        'broodjes': 1,
        'augurk pot': 1/50,
        'tomaat bak': 1/200,
        'mesclun': 1/50,
        'BBQ saus': 1/150,
        'mayonaise pot': 1/200,
        'ui zakken': 1/50,
        'pak kaas': 1/50
    },
    'Tortila': {
        'tortila': 1,
        'pulled chicken': 1/2,
        'mango': 1/10,
        'salsa': 1/100,
        'guacamole': 1/100,
        'komkommer bak':1/200,
        'zak sla': 1/20
    },
    'Kipsate':{

    },
    'Friet':{

    },
    'Biefstuk':{

    },
    'Shortrib':{

    },
    'Pasta':{

    },
    'Salade':{

    },
    'Bittergarnituur':{'Bitterbal': 1/20, 
                       'Kaasstengel': 1/20, 
                        'Frikadel':1/20, 
                        'Kaassoufle': 1/20, 
                        'Kipcorn': 1/20,

    },
    'Erwtensoep': {

    },
    'Curryworst':{

    },
    'Curry':{

    }
}

drank_ratio = {
    'Drankpakket alcohol' : {'fust': 1/100*tijd,
                             'cola': 1/20*tijd,
                             'sinas': 1/50*tijd,
                             'cola zero':1/25*tijd,
                             'ice tea sparkeling': 1/30*tijd,
                             'ice tea green': 1/30*tijd,
                             'rode wijn': 1/40*tijd,
                             'witte wijn': 1/30*tijd,
                             'rosé': 1/30*tijd,
                             'spa blauw': 1/50*tijd,
                             'spa rood': 1/50*tijd}
}

spullen_ratio = {
    'statafels' :{'Statefels': 1}
}
# Bereken ingrediënten
for gerecht, aantal in eten_dict.items():
    if gerecht in recepten:
        for ingrediënt, ratio in recepten[gerecht].items():
            if ingrediënt in ingrediënten_dict:
                ingrediënten_dict[ingrediënt] += ceil(aantal * ratio)
            else:
                ingrediënten_dict[ingrediënt] = ceil(aantal * ratio)

# Bereken drank
for drank, aantal in drinken_dict.items():
    if drank in drank_ratio:
        for item, ratio in drank_ratio[drank].items():
            if item in drank_dict:
                drank_dict[item] += ceil(aantal * ratio)
            else:
                drank_dict[item] = ceil(aantal * ratio)

# Bereken spullen 
for spul, aantal in spullen_dict.items():
    if spul in spullen_ratio:
        for item, ratio in spullen_ratio[spul].items():
            if item in spullen_dict:
                spullen_dict[item] += ceil(aantal * ratio)
            else:
                spullen_dict[item] = ceil(aantal * ratio)

# Bereken spullen 
for gerecht, aantal in eten_dict.items():
    if gerecht in spullen_ratio:
        for item, ratio in spullen_ratio[gerecht].items():
            if item in spullen_dict:
                spullen_dict[item] += ceil(aantal * ratio)
            else:
                spullen_dict[item] = ceil(aantal * ratio)

# Bereken spullen 
for drank, aantal in drinken_dict.items():
    if drank in spullen_ratio:
        for item, ratio in spullen_ratio[drank].items():
            if item in spullen_dict:
                spullen_dict[item] += ceil(aantal * ratio)
            else:
                spullen_dict[item] = ceil(aantal * ratio)

col1, col2, col3 = st.columns(3)
# Overzicht met afvinkboxen
with col1:
    st.title("ingrediënten")
    for ingrediënt, hoeveelheid in ingrediënten_dict.items():
        st.checkbox(f"{ingrediënt}: {hoeveelheid}", key=f"check_{ingrediënt}")

with col2:
    st.title("drank")
    for drank, hoeveelheid in drank_dict.items():
        st.checkbox(f"{drank}: {hoeveelheid}", key=f"check_{drank}")

with col3:
    st.title("spullen")
    for spul, hoeveelheid in spullen_dict.items():
        st.checkbox(f"{spul}: {hoeveelheid}", key=f"check_{spul}")
