import streamlit as st

# Configuration de la page en mode large pour tout faire tenir sur un écran
st.set_page_config(page_title="Configurateur Agence TIZ", page_icon="📐", layout="wide")

# CSS personnalisé pour épurer l'interface et la rendre "logiciel"
st.markdown("""
    <style>
    .block-container { padding-top: 1.5rem; padding-bottom: 1rem; }
    h1, h2, h3 { margin-bottom: 0.5rem; padding-bottom: 0px; }
    div.stButton > button { width: 100%; font-weight: bold; }
    .price-tag { color: #263A7C; font-weight: bold; }
    </style>
""", unsafe_scale=True)

# Titre principal discret et pro
st.title("📐 Configurateur de Prestations - Agence TIZ")
st.markdown("Composez votre accompagnement sur-mesure ou choisissez un pack préconfiguré. Tout se met à jour instantanément.")

# --- BASE DE DONNÉES DES PRESTATIONS & PRIX ---
SERVICES = {
    "🌐 SOLUTIONS DIGITALES": {
        "Audit UX & Stratégie B2B": {"price": 1200, "desc": "Analyse du tunnel de conversion et positionnement."},
        "Landing Page / Site Nocode Agile (Duda/Shopify)": {"price": 2800, "desc": "Conception orientée performance et conversion."},
        "Campagne Google Ads (SEA) & Tracking": {"price": 950, "desc": "Configuration et optimisation du trafic qualifié."},
        "SEO & Stratégie de Contenu Sémantique": {"price": 1100, "desc": "Optimisation du référencement naturel durable."},
        "Accompagnement Co-Pilote (Suivi mensuel ROI)": {"price": 1500, "desc": "Pilotage stratégique mensuel et réunions progrès."}
    },
    "🖨️ PRESTATIONS BRANDING & PRINT": {
        "Charte Graphique & Identité Visuelle": {"price": 2500, "desc": "Création de logo, palettes et univers de marque complet."},
        "Conception de Supports Print (Plaquette Éditoriale)": {"price": 1600, "desc": "Mise en page pro pour vos supports physiques de vente."},
        "Copywriting de Performance & Ligne Éditoriale": {"price": 850, "desc": "Rédaction d'impact pour supports digitaux ou physiques."}
    }
}

# Définition des packs pour l'auto-sélection
PACKS_PRESETS = {
    "Pack Lead Gen B2B (100% Digital)": [
        "Audit UX & Stratégie B2B", 
        "Landing Page / Site Nocode Agile (Duda/Shopify)", 
        "Campagne Google Ads (SEA) & Tracking"
    ],
    "Pack Image & Print (Branding)": [
        "Charte Graphique & Identité Visuelle", 
        "Conception de Supports Print (Plaquette Éditoriale)", 
        "Copywriting de Performance & Ligne Éditoriale"
    ],
    "Pack Performance Globale (Digital + Print)": [
        "Audit UX & Stratégie B2B", 
        "Landing Page / Site Nocode Agile (Duda/Shopify)",
        "Campagne Google Ads (SEA) & Tracking",
        "Charte Graphique & Identité Visuelle",
        "Conception de Supports Print (Plaquette Éditoriale)"
    ]
}

# --- GESTION DE L'ÉTAT (SESSION STATE) ---
if "selected_items" not in st.session_state:
    st.session_state.selected_items = []

# Fonctions de rappel pour les boutons de packs
def apply_pack(pack_name):
    st.session_state.selected_items = PACKS_PRESETS[pack_name]

# --- SECTION 1 : LES BOUTONS DE PACKS RAPIDES ---
st.subheader("🎯 Étape 1 : Choisir une configuration rapide (Optionnel)")
col_p1, col_p2, col_p3 = st.columns(3)

with col_p1:
    if st.button("🚀 Pack Lead Gen B2B", help="Audit + Site Web + Google Ads"):
        apply_pack("Pack Lead Gen B2B (100% Digital)")
with col_p2:
    if st.button("🎨 Pack Image & Print", help="Charte graphique + Plaquette + Rédaction"):
        apply_pack("Pack Image & Print (Branding)")
with col_p3:
    if st.button("⚡ Pack Performance Globale", help="La totale pour un lancement réussi"):
        apply_pack("Pack Performance Globale (Digital + Print)")

st.write("---")

# --- SECTION 2 : AFFICHAGE DOUBLE COLONNE (CONFIGURATION & DEVIS) ---
col_left, col_right = st.columns([5, 3])

# Liste de contrôle temporaire pour reconstruire l'état à chaque interaction
current_selection = []

with col_left:
    st.subheader("🛠️ Étape 2 : Personnalisez vos options")
    
    for category, items in SERVICES.items():
        st.markdown(f"#### {category}")
        for name, info in items.items():
            # Vérifie si l'item doit être coché (suite au clic d'un bouton ou d'une coche précédente)
            is_selected = name in st.session_state.selected_items
            
            # Label propre incluant le prix
            label = f"**{name}** — {info['price']} €"
            
            # Affichage de la case à cocher
            if st.checkbox(label, value=is_selected, key=f"cb_{name}"):
                current_selection.append(name)
        st.write("")

# Synchronisation de la sélection
st.session_state.selected_items = current_selection

with col_right:
    st.subheader("📋 Votre Estimation en Temps Réel")
    
    if st.session_state.selected_items:
        total_price = 0
        # Conteneur visuel pour faire ressortir le devis
        with st.container(border=True):
            for item_name in st.session_state.selected_items:
                # Retrouver le prix dans la structure de données
                price = 0
                for cat in SERVICES.values():
                    if item_name in cat:
                        price = cat[item_name]["price"]
                        break
                total_price += price
                st.markdown(f"🔹 {item_name} : `{price} €`")
            
            st.write("---")
            st.metric(label="MONTANT TOTAL ESTIMÉ (H.T.)", value=f"{total_price} €")
        
        # Formulaire d'engagement direct
        st.write("")
        st.subheader("📬 Étape 3 : Recevoir ce devis par écrit")
        with st.form("devis_form", clear_on_submit=True):
            nom = st.text_input("Votre nom *")
            entreprise = st.text_input("Nom de l'entreprise *")
            email = st.text_input("Adresse e-mail pro *")
            telephone = st.text_input("Téléphone")
            
            submit = st.form_submit_button("Demander la validation de mon conseiller TIZ")
            if submit:
                if nom and entreprise and email:
                    st.balloons()
                    st.success(f"Merci {nom} ! Jean-François Marnette va étudier votre configuration pour l'entreprise {entreprise} et vous recontacter sous 24h.")
                else:
                    st.error("Veuillez remplir les champs obligatoires (*)")
    else:
        st.info("Cochez des options à gauche ou cliquez sur un pack en haut pour générer votre devis en direct.")
