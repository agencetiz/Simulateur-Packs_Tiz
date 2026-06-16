import streamlit as st

# ⚙️ CONFIGURATION SYSTÈME DE LA PAGE
st.set_page_config(page_title="Simulateur TIZ", page_icon="💻", layout="wide")

# 🎨 INJECTION CSS (Sécurisée) POUR UN RENDU "APPLICATION"
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

# 🚀 TITRE DE L'APPLICATION
st.title("💻 Configurateur de Projet - Agence TIZ")
st.markdown("Construisez votre stratégie digitale sur-mesure. Les estimations se mettent à jour en temps réel.")
st.write("---")

# 🗄️ BASE DE DONNÉES ARCHITECTURE (Uniques vs Récurrentes)
SERVICES_UNIQUES = {
    "Audit UX & Stratégie B2B": {"price": 1200, "desc": "Analyse du tunnel de conversion et positionnement."},
    "Création Site Nocode Agile (Duda/Shopify)": {"price": 2800, "desc": "Conception orientée performance et conversion."},
    "Setup Campagne Google Ads": {"price": 950, "desc": "Configuration initiale, mots-clés et tracking."},
    "Charte Graphique & Identité Visuelle": {"price": 2500, "desc": "Création de logo et univers de marque complet."},
    "Conception de Supports Print": {"price": 1600, "desc": "Mise en page de plaquettes et supports de vente."}
}

SERVICES_RECURRENTS = {
    "Accompagnement Co-Pilote (Suivi ROI)": {"price": 1500, "desc": "Pilotage stratégique mensuel et réunions progrès."},
    "Gestion et Optimisation Google Ads": {"price": 500, "desc": "Ajustement mensuel des enchères et annonces."},
    "SEO & Création de Contenu Mensuel": {"price": 800, "desc": "Rédaction d'articles et optimisation continue."},
    "Maintenance, Hébergement & Sécurité": {"price": 150, "desc": "Mises à jour, sauvegardes et supervision technique."}
}

PACKS_PRESETS = {
    "Pack Lancement (100% Unique)": [
        "Audit UX & Stratégie B2B", 
        "Création Site Nocode Agile (Duda/Shopify)", 
        "Charte Graphique & Identité Visuelle"
    ],
    "Pack Génération de Leads (Mixte)": [
        "Setup Campagne Google Ads", 
        "Création Site Nocode Agile (Duda/Shopify)", 
        "Gestion et Optimisation Google Ads",
        "Maintenance, Hébergement & Sécurité"
    ],
    "Pack Co-Pilote Intégral": [
        "Audit UX & Stratégie B2B", 
        "Setup Campagne Google Ads",
        "Accompagnement Co-Pilote (Suivi ROI)",
        "Gestion et Optimisation Google Ads"
    ]
}

# 🧠 GESTION DE L'ÉTAT DU COMPOSANT (State Management)
if "selected_items" not in st.session_state:
    st.session_state.selected_items = []

def apply_pack(pack_name):
    st.session_state.selected_items = PACKS_PRESETS[pack_name]

# 📐 STRUCTURE DE L'INTERFACE EN 2 GRANDES COLONNES (Gauche: Choix, Droite: Panier & Contact)
col_main, col_sidebar = st.columns([6, 4], gap="large")

current_selection = []

with col_main:
    # ==========================================
    # ÉTAPE 1 : CONFIGURATION RAPIDE
    # ==========================================
    st.header("1️⃣ Configuration rapide (Packs)")
    st.markdown("Démarrez avec une base optimisée pour vos objectifs.")
    
    col_p1, col_p2, col_p3 = st.columns(3)
    with col_p1:
        if st.button("🚀 Pack Lancement", help="Création de marque et plateforme web"):
            apply_pack("Pack Lancement (100% Unique)")
    with col_p2:
        if st.button("🎯 Pack Lead Gen", help="Site web + Acquisition Google Ads"):
            apply_pack("Pack Génération de Leads (Mixte)")
    with col_p3:
        if st.button("🤝 Pack Co-Pilote", help="Stratégie et accompagnement mensuel"):
            apply_pack("Pack Co-Pilote Intégral")

    st.write("")
    
    # ==========================================
    # ÉTAPE 2 : PERSONNALISEZ VOS OPTIONS
    # ==========================================
    st.header("2️⃣ Personnalisez vos options")
    st.markdown("Ajustez votre sélection à la carte. Les options s'ajoutent à votre devis à droite.")
    
    col_uniques, col_recurrents = st.columns(2)
    
    # Colonne Prestations Uniques
    with col_uniques:
        st.subheader("🔹 Prestations Uniques (One-shot)")
        for name, info in SERVICES_UNIQUES.items():
            is_selected = name in st.session_state.selected_items
            label = f"{name} — {info['price']} €"
            if st.checkbox(label, value=is_selected, key=f"cb_{name}", help=info['desc']):
                current_selection.append(name)
                
    # Colonne Prestations Récurrentes
    with col_recurrents:
        st.subheader("🔄 Prestations Récurrentes (Mensuel)")
        for name, info in SERVICES_RECURRENTS.items():
            is_selected = name in st.session_state.selected_items
            label = f"{name} — {info['price']} € / mois"
            if st.checkbox(label, value=is_selected, key=f"cb_{name}", help=info['desc']):
                current_selection.append(name)

# Synchronisation stricte de la mémoire
st.session_state.selected_items = current_selection

with col_sidebar:
    # ==========================================
    # PANIER & CALCUL EN TEMPS RÉEL
    # ==========================================
    st.header("📋 Votre Estimation")
    
    total_unique = 0
    total_recurrent = 0
    
    st.markdown('<div class="cart-box">', unsafe_allow_html=True)
    
    if st.session_state.selected_items:
        for item in st.session_state.selected_items:
            # Vérification dans les prestations uniques
            if item in SERVICES_UNIQUES:
                price = SERVICES_UNIQUES[item]["price"]
                total_unique += price
                st.markdown(f"✅ {item} : `<span class='price-tag'>{price} €</span>`", unsafe_allow_html=True)
            # Vérification dans les prestations récurrentes
            elif item in SERVICES_RECURRENTS:
                price = SERVICES_RECURRENTS[item]["price"]
                total_recurrent += price
                st.markdown(f"🔄 {item} : `<span class='recurring-tag'>{price} € / mois</span>`", unsafe_allow_html=True)
                
        st.write("---")
        
        # Affichage des métriques (Séparation Budget initial et mensuel)
        col_m1, col_m2 = st.columns(2)
        with col_m1:
            st.metric(label="BUDGET INITIAL (H.T.)", value=f"{total_unique} €")
        with col_m2:
            st.metric(label="BUDGET MENSUEL (H.T.)", value=f"{total_recurrent} €")
            
    else:
        st.info("Sélectionnez des options à gauche ou choisissez un pack pour voir l'estimation.")
        
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.write("")
    
    # ==========================================
    # ÉTAPE 3 : NOUS CONTACTER POUR EN DISCUTER
    # ==========================================
    st.header("3️⃣ Nous contacter pour en discuter")
    st.markdown("Validez cette estimation avec l'équipe TIZ.")
    
    with st.form("contact_form", clear_on_submit=True):
        nom = st.text_input("Nom & Prénom *")
        entreprise = st.text_input("Société *")
        email = st.text_input("E-mail professionnel *")
        telephone = st.text_input("Téléphone")
        notes = st.text_area("Un détail à ajouter ? (Optionnel)")
        
        submit_btn = st.form_submit_button("Envoyer ma demande à TIZ", type="primary")
        
        if submit_btn:
            if nom and entreprise and email and st.session_state.selected_items:
                st.balloons()
                st.success(f"Transmission réussie ! Jean-François ou l'équipe TIZ vous contactera rapidement pour discuter de ce budget (Initial: {total_unique}€ | Mensuel: {total_recurrent}€).")
            elif not st.session_state.selected_items:
                st.warning("Veuillez sélectionner au moins une prestation avant d'envoyer.")
            else:
                st.error("Merci de remplir les champs obligatoires (*).")
