import streamlit as st
import os

# CONFIGURATION SYSTEME DE LA PAGE
st.set_page_config(page_title="Configurateur - Agence Tiz", layout="wide", initial_sidebar_state="collapsed")

# INJECTION CSS AVANCEE (Design moderne, Montserrat, espacements optimises)
st.markdown("""
    <style>
    /* Importation exacte de Montserrat */
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Montserrat', sans-serif;
        color: #111827;
    }
    
    /* Fond de l'application subtilement grise pour faire ressortir les cartes blanches */
    .stApp {
        background-color: #F9FAFB;
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* COMPRESSION DES ESPACES GLOBAUX */
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

    /* DESIGN MODERNE DES CARTES (UI) */
    [data-testid="stVerticalBlockBorderWrapper"] {
        border: 1px solid #E5E7EB !important;
        border-radius: 12px !important;
        background-color: #FFFFFF !important;
        padding: 0.8rem 1rem !important;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03) !important;
        margin-bottom: 0.5rem !important;
    }

    /* TYPOGRAPHIE (Titre reduit de 20%, espacement sous les h3) */
    h1 { color: #111827; font-weight: 800; letter-spacing: -0.5px; font-size: 1.7rem !important; margin: 0 !important; padding: 0 !important; }
    h2 { color: #2563EB; font-weight: 700; font-size: 1.1rem !important; margin: 0.2rem 0 0.4rem 0 !important; padding: 0 !important; }
    
    /* Ajout d'un petit espace sous les sous-titres (Investissement/Accompagnement) */
    h3 { color: #111827; font-weight: 600; font-size: 0.9rem !important; margin: 0.2rem 0 1rem 0 !important; padding: 0 !important; border-bottom: 1px solid #F3F4F6; padding-bottom: 0.3rem !important; }
    p { color: #4B5563; font-size: 0.75rem !important; line-height: 1.3 !important; margin: 0 0 0.5rem 0 !important; padding: 0 !important; }

    /* CHECKBOX STREAMLIT - Design plus propre */
    div.row-widget.stCheckbox {
        margin-top: -0.2rem !important;
        margin-bottom: -0.2rem !important;
    }

    /* BOUTONS D'ACTION (Packs) */
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
    
    /* ROLLOVER DES BOUTONS (Texte blanc) */
    .stButton>button:hover { 
        background-color: #2563EB !important; 
        color: #FFFFFF !important; 
        border-color: #2563EB !important;
        box-shadow: 0 4px 6px -1px rgba(37, 99, 235, 0.2);
    }
    
    /* BOUTON DE SOUMISSION PRIMAIRE */
    [data-testid="baseButton-primary"] {
        background-color: #111827 !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
    }
    [data-testid="baseButton-primary"]:hover {
        background-color: #374151 !important;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }

    /* ETIQUETTES DE PRIX */
    .price-tag { color: #111827; font-weight: 600; float: right;}
    .recurring-tag { color: #2563EB; font-weight: 600; float: right;}
    
    /* BLOC TOTAL FINAL MODERNE */
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

# EN-TETE DE L'APPLICATION AVEC FICHIER .WEBP LOCAL
col_logo, col_title = st.columns([1, 8], gap="small")
with col_logo:
    logo_path = "logo-tiz.webp"
    if os.path.exists(logo_path):
        st.image(logo_path, width=70)
    else:
        st.error("⚠️ Placez logo-tiz.webp ici")

with col_title:
    st.markdown("<h1 style='margin-bottom:0;'>Configurateur Digital</h1><p style='color: #2563EB; font-weight: 600; margin-top:0;'>Simulateur d'architecture B2B</p>", unsafe_allow_html=True)

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
    # ETAPE 1 : RECOMMANDATIONS
    with st.container(border=True):
        st.markdown("<h2>1. Configurations Recommandées</h2>", unsafe_allow_html=True)
        col_p1, col_p2, col_p3 = st.columns(3)
        with col_p1:
            st.button("Pack Prospection", on_click=apply_pack, args=("Pack Prospection",))
        with col_p2:
            st.button("Pack Notoriété", on_click=apply_pack, args=("Pack Notoriete",))
        with col_p3:
            st.button("Pack Démarrage", on_click=apply_pack, args=("Pack Demarrage d'activite",))

    # ETAPE 2 : PERSONNALISATION
    with st.container(border=True):
        st.markdown("<h2>2. Personnalisation du Périmètre</h2>", unsafe_allow_html=True)
        col_uniques, col_recurrents = st.columns(2, gap="medium")
        with col_uniques:
            st.markdown("<h3>Investissement Initial</h3>", unsafe_allow_html=True)
            for name, info in SERVICES_UNIQUES.items():
                st.checkbox(f"{name} - {info['price']} €", key=f"cb_{name}", help=info['desc'])
        with col_recurrents:
            st.markdown("<h3>Accompagnement Mensuel</h3>", unsafe_allow_html=True)
            for name, info in SERVICES_RECURRENTS.items():
                st.checkbox(f"{name} - {info['price']} € / m", key=f"cb_{name}", help=info['desc'])

    # ETAPE 3 : FORMULAIRE
    with st.container(border=True):
        st.markdown("<h2>3. Transmission du dossier</h2>", unsafe_allow_html=True)
        with st.form("contact_form", clear_on_submit=True):
            nom = st.text_input("Nom & Prénom *")
            entreprise = st.text_input("Société *")
            email = st.text_input("E-mail professionnel *")
            submit_btn = st.form_submit_button("Valider le projet", type="primary")

with col_sidebar:
    # L'ESTIMATION (STICKY)
    with st.container(border=True):
        st.markdown("<h2>Votre Estimation</h2>", unsafe_allow_html=True)
        
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
            html_cart += "<h3 style='color: #111827; border-bottom: none; padding-bottom: 0; margin-top: 0.5rem !important;'>Dépenses Fixes (Setup)</h3>"
            html_cart += "<ul style='list-style-type: none; padding: 0; margin: 0 0 0.8rem 0;'>"
            for item in SERVICES_UNIQUES:
                if st.session_state[f"cb_{item}"]:
                    price = SERVICES_UNIQUES[item]["price"]
                    html_cart += f"<li style='padding: 0.4rem 0; color: #4B5563; font-size: 0.8rem; border-bottom: 1px dashed #E5E7EB;'>{item} <span class='price-tag'>{price} €</span></li>"
            html_cart += f"<li style='padding: 0.5rem 0 0 0; color: #111827; font-size: 0.85rem; font-weight: 700; text-align: right;'>Sous-total Fixe : {total_unique} €</li>"
            html_cart += "</ul>"

        # CALCUL ET AFFICHAGE RECURRENT MENSUEL
        for item in SERVICES_RECURRENTS:
            if st.session_state[f"cb_{item}"]:
                has_selection = True
                total_recurrent += SERVICES_RECURRENTS[item]["price"]

        if total_recurrent > 0:
            html_cart += "<h3 style='color: #111827; border-bottom: none; padding-bottom: 0; margin-top: 1rem !important;'>Accompagnement Mensuel</h3>"
            html_cart += "<ul style='list-style-type: none; padding: 0; margin: 0 0 0.5rem 0;'>"
            for item in SERVICES_RECURRENTS:
                if st.session_state[f"cb_{item}"]:
                    price = SERVICES_RECURRENTS[item]["price"]
                    html_cart += f"<li style='padding: 0.4rem 0; color: #4B5563; font-size: 0.8rem; border-bottom: 1px dashed #E5E7EB;'>{item} <span class='recurring-tag'>{price} € / m</span></li>"
            html_cart += f"<li style='padding: 0.5rem 0 0 0; color: #2563EB; font-size: 0.85rem; font-weight: 700; text-align: right;'>Sous-total Mensuel : {total_recurrent} € / m</li>"
            html_cart += "</ul>"
        
        if has_selection:
            st.markdown(html_cart, unsafe_allow_html=True)
            
            # BLOC TOTAL MIS EN VALEUR
            st.markdown(f"""
            <div class="highlight-total">
                <div class="label">Total Setup H.T.</div>
                <div class="value">{total_unique} €</div>
                <div class="sub-value">Total Mensuel : {total_recurrent} € / mois</div>
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
