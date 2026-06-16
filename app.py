import streamlit as st

# CONFIGURATION SYSTEME DE LA PAGE
st.set_page_config(page_title="Configurateur - Agence TIZ", layout="wide", initial_sidebar_state="collapsed")

# INJECTION CSS AVANCEE POUR DESIGN HAUT DE GAMME (Marque Blanche)
st.markdown("""
    <style>
    /* Importation d'une typographie premium */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');

    /* Application de la police et masquage des elements natifs Streamlit */
    html, body, [class*="css"]  {
        font-family: 'Plus Jakarta Sans', sans-serif;
        background-color: #F8FAFC;
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Conteneur principal */
    .block-container { 
        padding-top: 3rem; 
        padding-bottom: 3rem; 
        max-width: 1400px;
    }

    /* Typographie et Titres */
    h1, h2, h3 { color: #0F172A; font-weight: 700; letter-spacing: -0.02em; }
    p { color: #475569; font-size: 1.05rem; }

    /* Design des boutons (Orange TIZ & Navy) */
    .stButton>button { 
        width: 100%; 
        background-color: #FFFFFF;
        color: #0F172A; 
        font-weight: 600; 
        border-radius: 8px; 
        border: 2px solid #E2E8F0; 
        padding: 0.75rem 1rem;
        transition: all 0.3s ease;
    }
    .stButton>button:hover { 
        border-color: #FF5C00; 
        color: #FF5C00; 
        box-shadow: 0 4px 14px rgba(255, 92, 0, 0.15);
        transform: translateY(-2px);
    }
    
    /* Bouton principal (Formulaire) */
    [data-testid="baseButton-primary"] {
        background-color: #FF5C00;
        color: white;
        border: none;
    }
    [data-testid="baseButton-primary"]:hover {
        background-color: #E05000;
        color: white;
    }

    /* Panneau de Devis (Glassmorphism / Shadow) */
    .cart-box { 
        background-color: #FFFFFF; 
        padding: 30px; 
        border-radius: 16px; 
        border: 1px solid #E2E8F0;
        box-shadow: 0 20px 40px rgba(15, 23, 42, 0.05); 
    }
    
    /* Tags de prix */
    .price-tag { color: #0F172A; font-weight: 700; float: right;}
    .recurring-tag { color: #FF5C00; font-weight: 700; float: right;}
    
    /* Lignes de separation personnalisees */
    hr {
        border: 0;
        height: 1px;
        background: #E2E8F0;
        margin: 2rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# EN-TETE DE L'APPLICATION (Style Agence)
st.markdown("""
    <div style='text-align: left; margin-bottom: 2rem;'>
        <h1 style='color: #FF5C00; font-size: 1.2rem; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 0;'>Agence TIZ</h1>
        <h2 style='font-size: 2.5rem; margin-top: 0;'>Configurateur Strategique 2026</h2>
        <p style='color: #64748B; font-size: 1.1rem;'>Selectionnez vos solutions B2B. L'architecture de votre budget s'actualise en temps reel.</p>
    </div>
    <hr>
""", unsafe_allow_html=True)

# BASE DE DONNEES ARCHITECTURE
SERVICES_UNIQUES = {
    "Audit UX & Strategie B2B": {"price": 1200, "desc": "Analyse du tunnel de conversion et positionnement."},
    "Creation Site Nocode Agile": {"price": 2800, "desc": "Conception Duda/Shopify orientee performance."},
    "Setup Campagne Google Ads": {"price": 950, "desc": "Configuration initiale, mots-cles et tracking."},
    "Charte Graphique & Branding": {"price": 2500, "desc": "Creation de logo et univers de marque."},
    "Conception Supports Print": {"price": 1600, "desc": "Mise en page de plaquettes commerciales."}
}

SERVICES_RECURRENTS = {
    "Accompagnement Co-Pilote": {"price": 1500, "desc": "Pilotage strategique et suivi mensuel du ROI."},
    "Optimisation Google Ads": {"price": 500, "desc": "Ajustement mensuel des encheres et annonces."},
    "SEO & Creation de Contenu": {"price": 800, "desc": "Redaction mensuelle et optimisation continue."},
    "Maintenance & Securite": {"price": 150, "desc": "Supervision technique et mises a jour."}
}

PACKS_PRESETS = {
    "Lancement (100% Unique)": [
        "Audit UX & Strategie B2B", 
        "Creation Site Nocode Agile", 
        "Charte Graphique & Branding"
    ],
    "Lead Generation (Mixte)": [
        "Setup Campagne Google Ads", 
        "Creation Site Nocode Agile", 
        "Optimisation Google Ads",
        "Maintenance & Securite"
    ],
    "Co-Pilote Integral": [
        "Audit UX & Strategie B2B", 
        "Setup Campagne Google Ads",
        "Accompagnement Co-Pilote",
        "Optimisation Google Ads"
    ]
}

# GESTION DE L'ETAT
for service in list(SERVICES_UNIQUES.keys()) + list(SERVICES_RECURRENTS.keys()):
    if f"cb_{service}" not in st.session_state:
        st.session_state[f"cb_{service}"] = False

def apply_pack(pack_name):
    pack_items = PACKS_PRESETS[pack_name]
    for service in list(SERVICES_UNIQUES.keys()) + list(SERVICES_RECURRENTS.keys()):
        st.session_state[f"cb_{service}"] = (service in pack_items)

# STRUCTURE DE L'INTERFACE (GRILLE CSS VIA STREAMLIT COLUMNS)
col_main, col_sidebar = st.columns([6, 4], gap="large")

with col_main:
    # ETAPE 1
    st.markdown("<h3>1. Pre-configurations strategiques</h3>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 0.95rem; margin-bottom: 1.5rem;'>Chargez une structure de projet optimisee pour gagner du temps.</p>", unsafe_allow_html=True)
    
    col_p1, col_p2, col_p3 = st.columns(3)
    with col_p1:
        st.button("Pack Lancement", on_click=apply_pack, args=("Lancement (100% Unique)",))
    with col_p2:
        st.button("Pack Lead Gen", on_click=apply_pack, args=("Lead Generation (Mixte)",))
    with col_p3:
        st.button("Pack Co-Pilote", on_click=apply_pack, args=("Co-Pilote Integral",))

    st.markdown("<hr style='margin: 3rem 0;'>", unsafe_allow_html=True)
    
    # ETAPE 2
    st.markdown("<h3>2. Construction sur-mesure</h3>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 0.95rem; margin-bottom: 1.5rem;'>Ajustez librement les leviers de votre accompagnement.</p>", unsafe_allow_html=True)
    
    col_uniques, col_recurrents = st.columns(2, gap="medium")
    
    with col_uniques:
        st.markdown("<h4 style='color: #0F172A; border-bottom: 2px solid #E2E8F0; padding-bottom: 0.5rem;'>Investissement Initial</h4>", unsafe_allow_html=True)
        st.write("")
        for name, info in SERVICES_UNIQUES.items():
            label = f"{name} - {info['price']} €"
            st.checkbox(label, key=f"cb_{name}", help=info['desc'])
                
    with col_recurrents:
        st.markdown("<h4 style='color: #0F172A; border-bottom: 2px solid #E2E8F0; padding-bottom: 0.5rem;'>Abonnement Mensuel</h4>", unsafe_allow_html=True)
        st.write("")
        for name, info in SERVICES_RECURRENTS.items():
            label = f"{name} - {info['price']} € / m"
            st.checkbox(label, key=f"cb_{name}", help=info['desc'])

with col_sidebar:
    st.markdown('<div class="cart-box">', unsafe_allow_html=True)
    st.markdown("<h3 style='margin-top: 0; color: #0F172A;'>Synthese Financiere</h3>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 0.9rem; margin-bottom: 2rem;'>Budget estimatif hors taxes.</p>", unsafe_allow_html=True)
    
    total_unique = 0
    total_recurrent = 0
    has_selection = False
    
    html_cart = "<ul style='list-style-type: none; padding: 0; margin: 0;'>"
    
    for item in SERVICES_UNIQUES:
        if st.session_state[f"cb_{item}"]:
            has_selection = True
            price = SERVICES_UNIQUES[item]["price"]
            total_unique += price
            html_cart += f"<li style='padding: 0.75rem 0; border-bottom: 1px solid #F1F5F9; color: #334155; font-size: 0.95rem;'>{item} <span class='price-tag'>{price} €</span></li>"
            
    for item in SERVICES_RECURRENTS:
        if st.session_state[f"cb_{item}"]:
            has_selection = True
            price = SERVICES_RECURRENTS[item]["price"]
            total_recurrent += price
            html_cart += f"<li style='padding: 0.75rem 0; border-bottom: 1px solid #F1F5F9; color: #334155; font-size: 0.95rem;'>{item} <span class='recurring-tag'>{price} € / m</span></li>"
    
    html_cart += "</ul>"
    
    if has_selection:
        st.markdown(html_cart, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        
        col_m1, col_m2 = st.columns(2)
        with col_m1:
            st.metric(label="SETUP INITIAL", value=f"{total_unique} €")
        with col_m2:
            st.metric(label="RECURRENT", value=f"{total_recurrent} €")
    else:
        st.markdown("<div style='background-color: #F8FAFC; padding: 1.5rem; border-radius: 8px; text-align: center; color: #94A3B8;'>Aucune solution selectionnee</div>", unsafe_allow_html=True)
        
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # FORMULAIRE DE CONTACT
    st.markdown("<h3>3. Valider l'architecture</h3>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 0.95rem;'>Echangeons sur cette configuration.</p>", unsafe_allow_html=True)
    
    with st.form("contact_form", clear_on_submit=True):
        nom = st.text_input("Nom & Prenom *")
        entreprise = st.text_input("Societe *")
        email = st.text_input("E-mail professionnel *")
        
        submit_btn = st.form_submit_button("Solliciter l'equipe TIZ", type="primary")
        
        if submit_btn:
            if nom and entreprise and email and has_selection:
                st.success(f"Dossier transmis. Un conseiller TIZ vous contactera sous 24h pour valider ce dimensionnement (Setup: {total_unique}€ | Mensuel: {total_recurrent}€).")
            elif not has_selection:
                st.warning("Veuillez concevoir une configuration avant de soumettre.")
            else:
                st.error("Les champs marques d'un asterisque sont obligatoires.")
