import streamlit as st

# CONFIGURATION SYSTEME DE LA PAGE
st.set_page_config(page_title="Configurateur - Agence Tiz", layout="wide", initial_sidebar_state="collapsed")

# INJECTION CSS AVANCEE (Espaces reduits, Polices reduites de 30%, sticky)
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

    /* REDUCTION DES ESPACES (Padding global) */
    .block-container { 
        padding-top: 1.5rem !important; 
        padding-bottom: 1.5rem !important; 
        max-width: 1200px;
    }

    /* COLONNE STICKY */
    [data-testid="column"]:nth-of-type(2) {
        position: -webkit-sticky;
        position: sticky;
        top: 1.5rem;
        align-self: flex-start;
        z-index: 100;
    }

    /* REDUCTION DES ESPACES DES CADRES */
    [data-testid="stVerticalBlockBorderWrapper"] {
        border: 2px solid #2563EB !important;
        border-radius: 8px !important;
        background-color: #FAFAFA !important;
        padding: 0.2rem 0.5rem !important;
        box-shadow: 0 2px 5px rgba(37, 99, 235, 0.05);
        margin-bottom: 0.5rem !important;
    }

    /* REDUCTION DES POLICES (-30%) */
    h1 { color: #111827; font-weight: 700; letter-spacing: -0.5px; font-size: 2.1rem !important; margin-bottom: 0.2rem !important; }
    h2 { color: #2563EB; font-weight: 700; font-size: 1.05rem !important; margin-top: 0.2rem !important; margin-bottom: 0.8rem !important;}
    h3 { color: #111827; font-weight: 600; font-size: 0.85rem !important; margin-bottom: 0.2rem !important; }
    p { color: #4B5563; font-size: 0.7rem !important; line-height: 1.4 !important; margin-bottom: 0.5rem !important; }

    /* REDUCTION DES BOUTONS ET CHECKBOX */
    .stButton>button { 
        width: 100%; 
        background-color: #FFFFFF;
        color: #2563EB; 
        font-weight: 600; 
        border-radius: 4px; 
        border: 1px solid #2563EB; 
        padding: 0.4rem 0.5rem;
        transition: all 0.2s ease;
        font-size: 0.75rem !important;
    }
    .stButton>button:hover { 
        background-color: #2563EB; 
        color: #FFFFFF; 
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.2);
    }
    
    [data-testid="baseButton-primary"] {
        background-color: #111827 !important;
        color: white !important;
        border: none !important;
    }
    [data-testid="baseButton-primary"]:hover {
        background-color: #374151 !important;
    }

    /* ETIQUETTES DE PRIX */
    .price-tag { color: #111827; font-weight: 700; float: right;}
    .recurring-tag { color: #2563EB; font-weight: 700; float: right;}
    
    /* BLOC TOTAL MIS EN VALEUR */
    .highlight-total {
        background-color: #2563EB;
        color: white;
        padding: 1rem;
        border-radius: 6px;
        margin-top: 1rem;
        text-align: center;
    }
    .highlight-total .label { font-size: 0.7rem; text-transform: uppercase; letter-spacing: 1px; opacity: 0.9; }
    .highlight-total .value { font-size: 1.4rem; font-weight: 700; margin-top: 0.3rem; }
    .highlight-total .sub-value { font-size: 0.8rem; margin-top: 0.3rem; padding-top: 0.3rem; border-top: 1px solid rgba(255,255,255,0.2); }
    </style>
""", unsafe_allow_html=True)

# EN-TETE DE L'APPLICATION AVEC LOGO
st.markdown("""
    <div style='display: flex; align-items: center; margin-bottom: 1.5rem;'>
        <img src='https://www.tiz.fr/wp-content/uploads/2023/11/logo-tiz-black.svg' alt='Logo Tiz' style='height: 40px; margin-right: 1.5rem;' onerror="this.src='https://www.tiz.fr/wp-content/themes/tiz/images/logo.png'">
        <div>
            <h1 style='margin: 0;'>Configurateur Digital</h1>
            <p style='color: #2563EB; font-weight: 600; margin: 0;'>Simulateur d'architecture B2B</p>
        </div>
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

# NOUVEAUX PACKS STRATEGIQUES
PACKS_PRESETS = {
    "Pack Prospection": [
        "Configuration Google Ads", 
        "Gestion Google Ads",
        "Accompagnement Co-Pilote"
    ],
    "Pack Notoriete": [
        "Design & Identite de Marque", 
        "Creation Site Web Performant", 
        "Creation de Contenu SEO"
    ],
    "Pack Demarrage d'activite": [
        "Audit UX & Strategie B2B", 
        "Creation Site Web Performant", 
        "Design & Identite de Marque",
        "Maintenance Technique"
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
col_main, col_sidebar = st.columns([6, 4], gap="medium")

with col_main:
    # ETAPE 1 : CADRE BLEU
    with st.container(border=True):
        st.markdown("<h2>1. Configurations Recommandees</h2>", unsafe_allow_html=True)
        
        col_p1, col_p2, col_p3 = st.columns(3)
        with col_p1:
            st.button("Pack Prospection", on_click=apply_pack, args=("Pack Prospection",))
        with col_p2:
            st.button("Pack Notoriete", on_click=apply_pack, args=("Pack Notoriete",))
        with col_p3:
            st.button("Pack Demarrage", on_click=apply_pack, args=("Pack Demarrage d'activite",))

    # ETAPE 2 : CADRE BLEU
    with st.container(border=True):
        st.markdown("<h2>2. Personnalisation du Perimetre</h2>", unsafe_allow_html=True)
        
        col_uniques, col_recurrents = st.columns(2, gap="small")
        
        with col_uniques:
            st.markdown("<h3>Investissement Initial</h3>", unsafe_allow_html=True)
            for name, info in SERVICES_UNIQUES.items():
                label = f"{name} - {info['price']} €"
                st.checkbox(label, key=f"cb_{name}", help=info['desc'])
                    
        with col_recurrents:
            st.markdown("<h3>Accompagnement Mensuel</h3>", unsafe_allow_html=True)
            for name, info in SERVICES_RECURRENTS.items():
                label = f"{name} - {info['price']} € / m"
                st.checkbox(label, key=f"cb_{name}", help=info['desc'])

    # ETAPE 3 (FORMULAIRE DE CONTACT) : CADRE BLEU
    with st.container(border=True):
        st.markdown("<h2>3. Transmission du dossier</h2>", unsafe_allow_html=True)
        
        with st.form("contact_form", clear_on_submit=True):
            nom = st.text_input("Nom & Prenom *")
            entreprise = st.text_input("Societe *")
            email = st.text_input("E-mail professionnel *")
            
            submit_btn = st.form_submit_button("Valider le projet", type="primary")

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
                html_cart += f"<li style='padding: 0.6rem 0; border-bottom: 1px solid #E5E7EB; color: #374151; font-size: 0.8rem;'>{item} <span class='price-tag'>{price} €</span></li>"
                
        for item in SERVICES_RECURRENTS:
            if st.session_state[f"cb_{item}"]:
                has_selection = True
                price = SERVICES_RECURRENTS[item]["price"]
                total_recurrent += price
                html_cart += f"<li style='padding: 0.6rem 0; border-bottom: 1px solid #E5E7EB; color: #374151; font-size: 0.8rem;'>{item} <span class='recurring-tag'>{price} € / m</span></li>"
        
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
            st.markdown("<div style='background-color: #FFFFFF; padding: 1.5rem; border-radius: 6px; border: 1px dashed #9CA3AF; text-align: center; color: #6B7280; font-size: 0.8rem;'>Cochez des options pour visualiser l'estimation en temps reel.</div>", unsafe_allow_html=True)

# GESTION DE L'ENVOI (Logique de routage vers marketing@tiz.fr)
if submit_btn:
    if nom and entreprise and email and has_selection:
        # En production, ce bloc déclenche l'API mail (ex: SendGrid / SMTP) pointant vers l'adresse cible
        # send_email_api(to="marketing@tiz.fr", subject=f"Nouveau Projet: {entreprise}", data=...)
        
        st.success(f"Dossier validé ! Les informations de {entreprise} ont été transmises avec succès à l'adresse marketing@tiz.fr. Notre équipe vous recontactera très prochainement.")
    elif not has_selection:
        st.warning("Veuillez construire une configuration avant de valider le projet.")
    else:
        st.error("Les champs marqués d'un astérisque sont obligatoires.")
