import streamlit as st

# CONFIGURATION SYSTEME DE LA PAGE
st.set_page_config(page_title="Configurateur - Agence Tiz", layout="wide", initial_sidebar_state="collapsed")

# INJECTION CSS AVANCEE (Cadres bleus et colonne sticky)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Montserrat', sans-serif;
        background-color: #FFFFFF;
        color: #111827;
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    .block-container { 
        padding-top: 3rem; 
        padding-bottom: 4rem; 
        max-width: 1200px;
    }

    /* Rendre la colonne de droite "Sticky" (Fixee au scroll) */
    [data-testid="column"]:nth-of-type(2) {
        position: -webkit-sticky;
        position: sticky;
        top: 3rem;
        align-self: flex-start;
        z-index: 100;
    }

    /* Design des cadres des conteneurs (Habillage Bleu) */
    [data-testid="stVerticalBlockBorderWrapper"] {
        border: 2px solid #2563EB !important;
        border-radius: 12px !important;
        background-color: #FAFAFA !important;
        padding: 0.5rem !important;
        box-shadow: 0 4px 10px rgba(37, 99, 235, 0.05);
    }

    /* Typographie */
    h1 { color: #111827; font-weight: 700; letter-spacing: -1px; font-size: 2.5rem; margin-bottom: 0.5rem; }
    h2 { color: #2563EB; font-weight: 700; font-size: 1.5rem; margin-top: 0.5rem; margin-bottom: 1.5rem;}
    h3 { color: #111827; font-weight: 600; font-size: 1.25rem; }
    p { color: #4B5563; font-size: 1rem; line-height: 1.6; }

    /* Boutons de l'interface */
    .stButton>button { 
        width: 100%; 
        background-color: #FFFFFF;
        color: #2563EB; 
        font-weight: 600; 
        border-radius: 6px; 
        border: 1px solid #2563EB; 
        padding: 0.85rem 1rem;
        transition: all 0.2s ease;
    }
    .stButton>button:hover { 
        background-color: #2563EB; 
        color: #FFFFFF; 
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.2);
    }
    
    /* Bouton d'action principal (Formulaire) */
    [data-testid="baseButton-primary"] {
        background-color: #111827 !important;
        color: white !important;
        border: none !important;
    }
    [data-testid="baseButton-primary"]:hover {
        background-color: #374151 !important;
    }

    /* Etiquettes de prix */
    .price-tag { color: #111827; font-weight: 700; float: right;}
    .recurring-tag { color: #2563EB; font-weight: 700; float: right;}
    
    /* Bloc de synthese mis en valeur */
    .highlight-total {
        background-color: #2563EB;
        color: white;
        padding: 1.5rem;
        border-radius: 8px;
        margin-top: 1.5rem;
        text-align: center;
    }
    .highlight-total .label { font-size: 0.9rem; text-transform: uppercase; letter-spacing: 1px; opacity: 0.9; }
    .highlight-total .value { font-size: 2rem; font-weight: 700; margin-top: 0.5rem; }
    .highlight-total .sub-value { font-size: 1.1rem; margin-top: 0.5rem; padding-top: 0.5rem; border-top: 1px solid rgba(255,255,255,0.2); }
    </style>
""", unsafe_allow_html=True)

# EN-TETE DE L'APPLICATION
st.markdown("""
    <div style='text-align: left; margin-bottom: 2rem;'>
        <h1 style='font-size: 3rem; margin-bottom: 0;'>Agence Tiz</h1>
        <p style='color: #2563EB; font-size: 1.25rem; font-weight: 600;'>Simulateur de budget et d'architecture digitale</p>
    </div>
""", unsafe_allow_html=True)

# BASE DE DONNEES ARCHITECTURE
SERVICES_UNIQUES = {
    "Audit UX & Strategie B2B": {"price": 1200, "desc": "Analyse du tunnel de conversion et positionnement."},
    "Creation Site Web Performant": {"price": 2800, "desc": "Conception orientee conversion et ergonomie."},
    "Configuration Google Ads": {"price": 950, "desc": "Setup initial, mots-cles et tracking."},
    "Design & Identite de Marque": {"price": 2500, "desc": "Creation de logo et univers graphique complet."},
    "Conception Supports Print": {"price": 1600, "desc": "Design de plaquettes et supports physiques."}
}

SERVICES_RECURRENTS = {
    "Accompagnement Co-Pilote": {"price": 1500, "desc": "Pilotage strategique et suivi mensuel du ROI."},
    "Gestion Google Ads": {"price": 500, "desc": "Ajustement mensuel des encheres et campagnes."},
    "Creation de Contenu SEO": {"price": 800, "desc": "Redaction web et optimisation continue."},
    "Maintenance Technique": {"price": 150, "desc": "Supervision, securite et mises a jour."}
}

PACKS_PRESETS = {
    "Pack Lancement": [
        "Audit UX & Strategie B2B", 
        "Creation Site Web Performant", 
        "Design & Identite de Marque"
    ],
    "Pack Acquisition": [
        "Configuration Google Ads", 
        "Creation Site Web Performant", 
        "Gestion Google Ads",
        "Maintenance Technique"
    ],
    "Pack Strategie Globale": [
        "Audit UX & Strategie B2B", 
        "Configuration Google Ads",
        "Accompagnement Co-Pilote",
        "Gestion Google Ads"
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

# STRUCTURE DE L'INTERFACE
col_main, col_sidebar = st.columns([6, 4], gap="large")

with col_main:
    # ETAPE 1 : CADRE BLEU
    with st.container(border=True):
        st.markdown("<h2>1. Configurations Recommandees</h2>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 0.95rem; margin-bottom: 1.5rem;'>Appliquez une structure eprouvee pour vos objectifs.</p>", unsafe_allow_html=True)
        
        col_p1, col_p2, col_p3 = st.columns(3)
        with col_p1:
            st.button("Pack Lancement", on_click=apply_pack, args=("Pack Lancement",))
        with col_p2:
            st.button("Pack Acquisition", on_click=apply_pack, args=("Pack Acquisition",))
        with col_p3:
            st.button("Pack Strategie Globale", on_click=apply_pack, args=("Pack Strategie Globale",))

    st.write("")
    st.write("")

    # ETAPE 2 : CADRE BLEU
    with st.container(border=True):
        st.markdown("<h2>2. Personnalisation du Perimetre</h2>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 0.95rem; margin-bottom: 1.5rem;'>Cochez les prestations pour affiner votre besoin.</p>", unsafe_allow_html=True)
        
        col_uniques, col_recurrents = st.columns(2, gap="medium")
        
        with col_uniques:
            st.markdown("<h4 style='color: #111827; padding-bottom: 0.5rem;'>Investissement Initial</h4>", unsafe_allow_html=True)
            for name, info in SERVICES_UNIQUES.items():
                label = f"{name} - {info['price']} €"
                st.checkbox(label, key=f"cb_{name}", help=info['desc'])
                    
        with col_recurrents:
            st.markdown("<h4 style='color: #111827; padding-bottom: 0.5rem;'>Accompagnement Mensuel</h4>", unsafe_allow_html=True)
            for name, info in SERVICES_RECURRENTS.items():
                label = f"{name} - {info['price']} € / m"
                st.checkbox(label, key=f"cb_{name}", help=info['desc'])

    st.write("")
    st.write("")

    # ETAPE 3 (FORMULAIRE DE CONTACT) : CADRE BLEU
    # Place en bas à gauche pour ne pas allonger la colonne sticky de droite
    with st.container(border=True):
        st.markdown("<h2>3. Valider le projet</h2>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 0.95rem;'>Transmettez cette simulation a notre equipe.</p>", unsafe_allow_html=True)
        
        with st.form("contact_form", clear_on_submit=True):
            nom = st.text_input("Nom & Prenom *")
            entreprise = st.text_input("Societe *")
            email = st.text_input("E-mail professionnel *")
            
            submit_btn = st.form_submit_button("Demander un rendez-vous", type="primary")

with col_sidebar:
    # L'ESTIMATION STICKY : CADRE BLEU
    with st.container(border=True):
        st.markdown("<h2 style='margin-top: 0;'>Votre Estimation</h2>", unsafe_allow_html=True)
        
        total_unique = 0
        total_recurrent = 0
        has_selection = False
        
        html_cart = "<ul style='list-style-type: none; padding: 0; margin: 0;'>"
        
        for item in SERVICES_UNIQUES:
            if st.session_state[f"cb_{item}"]:
                has_selection = True
                price = SERVICES_UNIQUES[item]["price"]
                total_unique += price
                html_cart += f"<li style='padding: 0.85rem 0; border-bottom: 1px solid #E5E7EB; color: #374151; font-size: 0.90rem;'>{item} <span class='price-tag'>{price} €</span></li>"
                
        for item in SERVICES_RECURRENTS:
            if st.session_state[f"cb_{item}"]:
                has_selection = True
                price = SERVICES_RECURRENTS[item]["price"]
                total_recurrent += price
                html_cart += f"<li style='padding: 0.85rem 0; border-bottom: 1px solid #E5E7EB; color: #374151; font-size: 0.90rem;'>{item} <span class='recurring-tag'>{price} € / m</span></li>"
        
        html_cart += "</ul>"
        
        if has_selection:
            st.markdown(html_cart, unsafe_allow_html=True)
            
            # Bloc total mis en valeur
            st.markdown(f"""
            <div class="highlight-total">
                <div class="label">Setup Initial H.T.</div>
                <div class="value">{total_unique} €</div>
                <div class="sub-value">Budget Mensuel : {total_recurrent} € / mois</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("<div style='background-color: #FFFFFF; padding: 2rem; border-radius: 8px; border: 1px dashed #9CA3AF; text-align: center; color: #6B7280;'>Cochez des options pour visualiser l'estimation en temps reel.</div>", unsafe_allow_html=True)

# Gestion de la soumission du formulaire (En dehors de la grille visuelle pour l'affichage de l'alerte)
if submit_btn:
    if nom and entreprise and email and has_selection:
        st.success(f"Dossier transmis. Un expert Tiz vous contactera sous 24h pour discuter de cette architecture (Setup: {total_unique}€ | Mensuel: {total_recurrent}€).")
    elif not has_selection:
        st.warning("Veuillez construire une configuration avant de valider.")
    else:
        st.error("Les champs marques d'un asterisque sont obligatoires.")
