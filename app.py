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
        "Audit UX & Strategie B2
