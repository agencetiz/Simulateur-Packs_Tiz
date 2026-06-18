import streamlit as st
import os

# CONFIGURATION SYSTEME DE LA PAGE
st.set_page_config(page_title="Configurateur - Agence Tiz", layout="wide", initial_sidebar_state="collapsed")

# INJECTION CSS AVANCEE
st.markdown("""
    <style>
    /* Importation exacte de Montserrat */
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Montserrat', sans-serif;
        color: #111827;
    }
    
    .stApp {
        background-color: #F9FAFB;
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    .block-container { 
        padding-top: 1.5rem !important; 
        padding-bottom: 1.5rem !important; 
        max-width: 1200px;
    }

    [data-testid="column"]:nth-of-type(2) {
        position: -webkit-sticky;
        position: sticky;
        top: 1.5rem;
        align-self: flex-start;
        z-index: 100;
    }

    [data-testid="stVerticalBlockBorderWrapper"] {
        border: 1px solid #E5E7EB !important;
        border-radius: 12px !important;
        background-color: #FFFFFF !important;
        padding: 0.8rem 1rem !important;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03) !important;
        margin-bottom: 0.5rem !important;
    }

    h1 { color: #111827; font-weight: 800; letter-spacing: -0.5px; font-size: 1.7rem !important; margin: 0 !important; padding: 0 !important; }
    h2 { color: #2563EB; font-weight: 700; font-size: 1.1rem !important; margin: 0.2rem 0 0.4rem 0 !important; padding: 0 !important; }
    
    h3 { color: #111827; font-weight: 600; font-size: 0.9rem !important; margin: 0.2rem 0 1rem 0 !important; padding: 0 !important; border-bottom: 1px solid #F3F4F6; padding-bottom: 0.3rem !important; }
    p { color: #4B5563; font-size: 0.75rem !important; line-height: 1.3 !important; margin: 0 0 0.5rem 0 !important; padding: 0 !important; }

    div.row-widget.stCheckbox {
        margin-top: -0.2rem !important;
        margin-bottom: -0.2rem !important;
    }

    /* BOUTONS SECONDAIRES (Packs) */
    .stButton>button { 
        width: 100%; 
        background-color: #F8FAFC;
        color: #2563EB; 
        font-weight: 600; 
        border-radius: 8px; 
        border: 1px solid #E2E8F0; 
        padding: 0.4rem 0.5rem;
        transition: all 0.2s ease;
        font-size: 0.8rem !important;
        margin-top: 0.2rem;
    }
    
    /* ROLLOVER BOUTONS SECONDAIRES (Bleu) */
    .stButton>button:hover { 
        background-color: #2563EB !important; 
        border-color: #2563EB !important;
        box-shadow: 0 4px 6px -1px rgba(37, 99, 235, 0.2);
    }
    .stButton>button:hover * {
        color: #FFFFFF !important;
    }
    
    /* BOUTON PRIMAIRE (Validation - Rouge) - Ciblage exhaustif */
    button[data-testid="baseButton-primary"],
    button[kind="primaryFormSubmit"],
    button[kind="primary"] {
        background-color: #E11D48 !important; 
        border: none !important;
        border-radius: 8px !important;
        transition: all 0.2s ease !important;
    }
    
    /* FORCE LE TEXTE BLANC EN PERMANENCE POUR LE BOUTON ROUGE */
    button[data-testid="baseButton-primary"] p,
    button[data-testid="baseButton-primary"] span,
    button[data-testid="baseButton-primary"] div,
    button[kind="primaryFormSubmit"] p,
    button[kind="primaryFormSubmit"] span,
    button[kind="primaryFormSubmit"] div,
    button[kind="primary"] p,
    button[kind="primary"] span,
    button[kind="primary"] div {
        color: #FFFFFF !important;
    }
    
    /* ROLLOVER BOUTON PRIMAIRE (Rouge foncé) */
    button[data-testid="baseButton-primary"]:hover,
    button[kind="primaryFormSubmit"]:hover,
    button[kind="primary"]:hover {
        background-color: #BE123C !important;
        box-shadow: 0 4px 6px -1px rgba(225, 29, 72, 0.3) !important;
    }

    .price-tag { color: #111827; font-weight: 600; float: right;}
    .recurring-tag { color: #2563EB; font-weight: 600; float: right;}
    
    .highlight-total {
        background: linear-gradient(135deg, #2563EB 0%, #1D4ED8 100%);
        color: white;
        padding: 1.2rem;
        border-radius: 12px;
        margin-top: 1rem;
        text-align: center;
        box-shadow: 0 10px 15px -3px rgba(37, 99, 235, 0.2);
    }
    .highlight-total .label { font-size: 0.75rem; text-transform: uppercase; letter-spacing: 1.5px; opacity: 0.9; font-weight: 500;}
    .highlight-total .value { font-size: 1.6rem; font-weight: 800; margin-top: 0.2rem; }
    .highlight-total .sub-value { font-size: 0.85rem; margin-top: 0.4rem; padding-top: 0.4rem; border-top: 1px solid rgba(255,255,255,0.2); font-weight: 500;}
    </style>
""", unsafe_allow_html=True)

# EN-TETE DE L'APPLICATION (Logo agrandi et titre décalé)
col_logo, col_title = st.columns([2, 8], gap="large")
with col_logo:
    logo_path = "logo-tiz.webp"
    if os.path.exists(logo_path):
        st.image(logo_path, width=140)
    else:
        st.error("⚠️ Placez logo-tiz.webp ici")

with col_title:
    st.markdown("<div style='padding-top: 10px;'><h1 style='margin-bottom:0;'>Configurateur digital</h1><p style='color: #2563EB; font-weight: 600; margin-top:0;'>Simulateur d'architecture B2B</p></div>", unsafe_allow_html=True)

# BASE DE DONNEES ARCHITECTURE (Textes passés en minuscules)
SERVICES_UNIQUES = {
    "Audit UX & stratégie B2B": {"price": 1200, "desc": "Analyse du tunnel de conversion et positionnement."},
    "Création site web performant": {"price": 2800, "desc": "Conception orientée conversion et ergonomie."},
    "Configuration Google Ads": {"price": 950, "desc": "Setup initial, mots-clés et tracking."},
    "Design & identité de marque": {"price": 2500, "desc": "Création de logo et univers graphique complet."},
    "Conception supports print": {"price": 1600, "desc": "Design de plaquettes et supports physiques."}
}

SERVICES_RECURRENTS = {
    "Accompagnement co-pilote": {"price": 1500, "desc": "Pilotage stratégique et suivi mensuel du ROI."},
    "Gestion Google Ads": {"price": 500, "desc": "Ajustement mensuel des enchères et campagnes."},
    "Création de contenu SEO": {"price": 800, "desc": "Rédaction web et optimisation continue."},
    "Maintenance technique": {"price": 150, "desc": "Supervision, sécurité et mises à jour."}
}

PACKS_PRESETS = {
    "Pack prospection": [
        "Configuration Google Ads", 
        "Gestion Google Ads",
        "Accompagnement co-pilote"
    ],
    "Pack notoriété": [
        "Design & identité de marque", 
        "Création site web performant", 
        "Création de contenu SEO"
    ],
    "Pack démarrage d'activité": [
        "Audit UX & stratégie B2B", 
        "Création site web performant", 
        "Design & identité de marque",
        "Maintenance technique"
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
    # ETAPE 1
    with st.container(border=True):
        st.markdown("<h2>1. Configurations recommandées</h2>", unsafe_allow_html=True)
        col_p1, col_p2, col_p3 = st.columns(3)
        with col_p1:
            st.button("Pack prospection", on_click=apply_pack, args=("Pack prospection",))
        with col_p2:
            st.button("Pack notoriété", on_click=apply_pack, args=("Pack notoriété",))
        with col_p3:
            st.button("Pack démarrage", on_click=apply_pack, args=("Pack démarrage d'activité",))

    # ETAPE 2
    with st.container(border=True):
        st.markdown("<h2>2. Personnalisation du périmètre</h2>", unsafe_allow_html=True)
        col_uniques, col_recurrents = st.columns(2, gap="medium")
        with col_uniques:
            st.markdown("<h3>Investissement initial</h3>", unsafe_allow_html=True)
            for name, info in SERVICES_UNIQUES.items():
                st.checkbox(f"{name} - {info['price']} €", key=f"cb_{name}", help=info['desc'])
        with col_recurrents:
            st.markdown("<h3>Accompagnement mensuel</h3>", unsafe_allow_html=True)
            for name, info in SERVICES_RECURRENTS.items():
                st.checkbox(f"{name} - {info['price']} € / m", key=f"cb_{name}", help=info['desc'])

    # ETAPE 3
    with st.container(border=True):
        st.markdown("<h2>3. Transmission du dossier</h2>", unsafe_allow_html=True)
        with st.form("contact_form", clear_on_submit=True):
            nom = st.text_input("Nom & prénom *")
            entreprise = st.text_input("Société *")
            email = st.text_input("E-mail professionnel *")
            submit_btn = st.form_submit_button("Valider le projet", type="primary")

with col_sidebar:
    # L'ESTIMATION
    with st.container(border=True):
        st.markdown("<h2>Votre estimation</h2>", unsafe_allow_html=True)
        
        total_unique = 0
        total_recurrent = 0
        has_selection = False
        html_cart = ""
        
        # CALCUL ET AFFICHAGE SETUP INITIAL
        for item in SERVICES_UNIQUES:
            if st.session_state[f"cb_{item}"]:
                has_selection = True
                total_unique += SERVICES_UNIQUES[item]["price"]
        
        if total_unique > 0:
            html_cart += "<h3 style='color: #111827; border-bottom: none; padding-bottom: 0; margin-top: 0.5rem !important;'>Dépenses fixes (setup)</h3>"
            html_cart += "<ul style='list-style-type: none; padding: 0; margin: 0 0 0.8rem 0;'>"
            for item in SERVICES_UNIQUES:
                if st.session_state[f"cb_{item}"]:
                    price = SERVICES_UNIQUES[item]["price"]
                    html_cart += f"<li style='padding: 0.4rem 0; color: #4B5563; font-size: 0.8rem; border-bottom: 1px dashed #E5E7EB;'>{item} <span class='price-tag'>{price} €</span></li>"
            html_cart += f"<li style='padding: 0.5rem 0 0 0; color: #111827; font-size: 0.85rem; font-weight: 700; text-align: right;'>Sous-total fixe : {total_unique} €</li>"
            html_cart += "</ul>"

        # CALCUL ET AFFICHAGE RECURRENT MENSUEL
        for item in SERVICES_RECURRENTS:
            if st.session_state[f"cb_{item}"]:
                has_selection = True
                total_recurrent += SERVICES_RECURRENTS[item]["price"]

        if total_recurrent > 0:
            html_cart += "<h3 style='color: #111827; border-bottom: none; padding-bottom: 0; margin-top: 1rem !important;'>Accompagnement mensuel</h3>"
            html_cart += "<ul style='list-style-type: none; padding: 0; margin: 0 0 0.5rem 0;'>"
            for item in SERVICES_RECURRENTS:
                if st.session_state[f"cb_{item}"]:
                    price = SERVICES_RECURRENTS[item]["price"]
                    html_cart += f"<li style='padding: 0.4rem 0; color: #4B5563; font-size: 0.8rem; border-bottom: 1px dashed #E5E7EB;'>{item} <span class='recurring-tag'>{price} € / m</span></li>"
            html_cart += f"<li style='padding: 0.5rem 0 0 0; color: #2563EB; font-size: 0.85rem; font-weight: 700; text-align: right;'>Sous-total mensuel : {total_recurrent} € / m</li>"
            html_cart += "</ul>"
        
        if has_selection:
            st.markdown(html_cart, unsafe_allow_html=True)
            
            # BLOC TOTAL MIS EN VALEUR
            st.markdown(f"""
            <div class="highlight-total">
                <div class="label">Total setup H.T.</div>
                <div class="value">{total_unique} €</div>
                <div class="sub-value">Total mensuel : {total_recurrent} € / mois</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("<div style='background-color: #F8FAFC; padding: 1.5rem; border-radius: 8px; border: 1px dashed #CBD5E1; text-align: center; color: #64748B; font-size: 0.8rem;'>Cochez des options pour visualiser l'estimation détaillée en temps réel.</div>", unsafe_allow_html=True)

# GESTION DE L'ENVOI
if submit_btn:
    if nom and entreprise and email and has_selection:
        st.success(f"Dossier validé ! Les informations de {entreprise} ont été transmises avec succès à l'adresse marketing@tiz.fr. Notre équipe vous recontactera très prochainement.")
    elif not has_selection:
        st.warning("Veuillez construire une configuration avant de valider le projet.")
    else:
        st.error("Les champs marqués d'un astérisque sont obligatoires.")
