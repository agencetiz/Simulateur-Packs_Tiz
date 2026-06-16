import streamlit as st

# CONFIGURATION SYSTEME DE LA PAGE
st.set_page_config(page_title="Simulateur TIZ", layout="wide")

# INJECTION CSS POUR UN RENDU APPLICATION
st.markdown("""
    <style>
    .block-container { padding-top: 2rem; padding-bottom: 2rem; }
    h1, h2, h3 { color: #1E293B; margin-bottom: 0.5rem; }
    .stButton>button { width: 100%; font-weight: bold; border-radius: 8px; border: 1px solid #E2E8F0; }
    .stButton>button:hover { border-color: #3B82F6; color: #3B82F6; }
    .price-tag { color: #3B82F6; font-weight: 700; }
    .recurring-tag { color: #10B981; font-weight: 700; }
    .cart-box { background-color: #F8FAFC; padding: 20px; border-radius: 10px; border: 1px solid #E2E8F0; }
    </style>
""", unsafe_allow_html=True)

# TITRE DE L'APPLICATION
st.title("Configurateur de Projet - Agence TIZ")
st.markdown("Construisez votre strategie digitale sur-mesure. Les estimations se mettent a jour en temps reel.")
st.write("---")

# BASE DE DONNEES ARCHITECTURE (Uniques vs Recurrentes)
SERVICES_UNIQUES = {
    "Audit UX & Strategie B2B": {"price": 1200, "desc": "Analyse du tunnel de conversion et positionnement."},
    "Creation Site Nocode Agile (Duda/Shopify)": {"price": 2800, "desc": "Conception orientee performance et conversion."},
    "Setup Campagne Google Ads": {"price": 950, "desc": "Configuration initiale, mots-cles et tracking."},
    "Charte Graphique & Identite Visuelle": {"price": 2500, "desc": "Creation de logo et univers de marque complet."},
    "Conception de Supports Print": {"price": 1600, "desc": "Mise en page de plaquettes et supports de vente."}
}

SERVICES_RECURRENTS = {
    "Accompagnement Co-Pilote (Suivi ROI)": {"price": 1500, "desc": "Pilotage strategique mensuel et reunions progres."},
    "Gestion et Optimisation Google Ads": {"price": 500, "desc": "Ajustement mensuel des encheres et annonces."},
    "SEO & Creation de Contenu Mensuel": {"price": 800, "desc": "Redaction d'articles et optimisation continue."},
    "Maintenance, Hebergement & Securite": {"price": 150, "desc": "Mises a jour, sauvegardes et supervision technique."}
}

PACKS_PRESETS = {
    "Pack Lancement (100% Unique)": [
        "Audit UX & Strategie B2B", 
        "Creation Site Nocode Agile (Duda/Shopify)", 
        "Charte Graphique & Identite Visuelle"
    ],
    "Pack Generation de Leads (Mixte)": [
        "Setup Campagne Google Ads", 
        "Creation Site Nocode Agile (Duda/Shopify)", 
        "Gestion et Optimisation Google Ads",
        "Maintenance, Hebergement & Securite"
    ],
    "Pack Co-Pilote Integral": [
        "Audit UX & Strategie B2B", 
        "Setup Campagne Google Ads",
        "Accompagnement Co-Pilote (Suivi ROI)",
        "Gestion et Optimisation Google Ads"
    ]
}

# GESTION DE L'ETAT DU COMPOSANT VIA CALLBACKS
# Initialisation des variables de session pour chaque case a cocher
for service in list(SERVICES_UNIQUES.keys()) + list(SERVICES_RECURRENTS.keys()):
    if f"cb_{service}" not in st.session_state:
        st.session_state[f"cb_{service}"] = False

# Fonction appelee lors du clic sur un bouton de pack
def apply_pack(pack_name):
    pack_items = PACKS_PRESETS[pack_name]
    for service in list(SERVICES_UNIQUES.keys()) + list(SERVICES_RECURRENTS.keys()):
        # Coche la case si le service est dans le pack, decoche sinon
        st.session_state[f"cb_{service}"] = (service in pack_items)

# STRUCTURE DE L'INTERFACE EN 2 GRANDES COLONNES
col_main, col_sidebar = st.columns([6, 4], gap="large")

with col_main:
    # ETAPE 1 : CONFIGURATION RAPIDE
    st.header("1. Configuration rapide (Packs)")
    st.markdown("Demarrez avec une base optimisee pour vos objectifs.")
    
    col_p1, col_p2, col_p3 = st.columns(3)
    with col_p1:
        st.button("Pack Lancement", on_click=apply_pack, args=("Pack Lancement (100% Unique)",), help="Creation de marque et plateforme web")
    with col_p2:
        st.button("Pack Lead Gen", on_click=apply_pack, args=("Pack Generation de Leads (Mixte)",), help="Site web + Acquisition Google Ads")
    with col_p3:
        st.button("Pack Co-Pilote", on_click=apply_pack, args=("Pack Co-Pilote Integral",), help="Strategie et accompagnement mensuel")

    st.write("")
    
    # ETAPE 2 : PERSONNALISEZ VOS OPTIONS
    st.header("2. Personnalisez vos options")
    st.markdown("Ajustez votre selection a la carte. Les options s'ajoutent a votre devis a droite.")
    
    col_uniques, col_recurrents = st.columns(2)
    
    # Colonne Prestations Uniques
    with col_uniques:
        st.subheader("Prestations Uniques (One-shot)")
        for name, info in SERVICES_UNIQUES.items():
            label = f"{name} - {info['price']} €"
            st.checkbox(label, key=f"cb_{name}", help=info['desc'])
                
    # Colonne Prestations Recurrentes
    with col_recurrents:
        st.subheader("Prestations Recurrentes (Mensuel)")
        for name, info in SERVICES_RECURRENTS.items():
            label = f"{name} - {info['price']} € / mois"
            st.checkbox(label, key=f"cb_{name}", help=info['desc'])

with col_sidebar:
    # PANIER & CALCUL EN TEMPS REEL
    st.header("Votre Estimation")
    
    total_unique = 0
    total_recurrent = 0
    has_selection = False
    
    st.markdown('<div class="cart-box">', unsafe_allow_html=True)
    
    # Verification des elements selectionnes via l'etat des cases a cocher
    for item in SERVICES_UNIQUES:
        if st.session_state[f"cb_{item}"]:
            has_selection = True
            price = SERVICES_UNIQUES[item]["price"]
            total_unique += price
            st.markdown(f"- {item} : <span class='price-tag'>{price} €</span>", unsafe_allow_html=True)
            
    for item in SERVICES_RECURRENTS:
        if st.session_state[f"cb_{item}"]:
            has_selection = True
            price = SERVICES_RECURRENTS[item]["price"]
            total_recurrent += price
            st.markdown(f"- {item} : <span class='recurring-tag'>{price} € / mois</span>", unsafe_allow_html=True)
    
    if has_selection:
        st.write("---")
        # Affichage des metriques (Separation Budget initial et mensuel)
        col_m1, col_m2 = st.columns(2)
        with col_m1:
            st.metric(label="BUDGET INITIAL (H.T.)", value=f"{total_unique} €")
        with col_m2:
            st.metric(label="BUDGET MENSUEL (H.T.)", value=f"{total_recurrent} €")
    else:
        st.info("Selectionnez des options a gauche ou choisissez un pack pour voir l'estimation.")
        
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.write("")
    
    # ETAPE 3 : NOUS CONTACTER POUR EN DISCUTER
    st.header("3. Nous contacter pour en discuter")
    st.markdown("Validez cette estimation avec l'equipe TIZ.")
    
    with st.form("contact_form", clear_on_submit=True):
        nom = st.text_input("Nom & Prenom *")
        entreprise = st.text_input("Societe *")
        email = st.text_input("E-mail professionnel *")
        telephone = st.text_input("Telephone")
        notes = st.text_area("Un detail a ajouter ? (Optionnel)")
        
        submit_btn = st.form_submit_button("Envoyer ma demande a TIZ", type="primary")
        
        if submit_btn:
            if nom and entreprise and email and has_selection:
                st.success(f"Transmission reussie. L'equipe TIZ vous contactera rapidement pour discuter de ce budget (Initial: {total_unique}€ | Mensuel: {total_recurrent}€).")
            elif not has_selection:
                st.warning("Veuillez selectionner au moins une prestation avant d'envoyer.")
            else:
                st.error("Merci de remplir les champs obligatoires (*).")
