import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Configurateur de Packs - Agence TIZ", page_icon="🚀", layout="wide")

# En-tête de l'application
st.title("🚀 Configurateur de Packs Stratégiques - Agence TIZ")
st.markdown("""
Bienvenue sur le simulateur de l'Agence TIZ. Personnalisez votre accompagnement digital B2B ou choisissez un de nos packs préconfigurés pour démarrer rapidement. 
Notre objectif : devenir votre co-pilote business et livrer des résultats mesurables.
""")

# Définition du catalogue des prestations basé sur le modèle économique 2026
catalog = {
    "1. Conseil, Diagnostic & Audits Stratégiques": [
        "État des lieux et stratégie transversale",
        "Audit UX / UI (Expérience Utilisateur)",
        "Audit SEO & Sémantique",
        "Cadrage & Rédaction de cahiers des charges"
    ],
    "2. Identité de Marque & Création de Contenus (Branding & Copywriting)": [
        "Concept de communication & Charte graphique",
        "Copywriting de performance",
        "Création de supports Print & Corporate",
        "Production Multimédia & Vidéo"
    ],
    "3. Acquisition, Performance & Trafic (E-Marketing & Ads)": [
        "Gestion et Optimisation Google Ads",
        "Stratégie & Gestion Social Ads",
        "Accompagnement et Animation des Réseaux Sociaux"
    ],
    "4. Solutions Web Agiles & Plateformes Nocode": [
        "Conception de sites et Landing Pages Nocode (Duda, Shopify)",
        "Configuration e-commerce & Tracking avancé"
    ],
    "5. L'Offre Co-Pilote : Accompagnement Récurrent & Suivi ROI": [
        "Accompagnement stratégique et opérationnel récurrent",
        "Hébergement Haute Performance & Sécurité",
        "Maintenance & Supervision Analytique",
        "Réunions Progrès Mensuelles"
    ],
    "6. Transfert de Compétences & Formations": [
        "Formations Opérationnelles certifiées"
    ]
}

# Packs préconfigurés (judicieusement choisis selon les enjeux B2B)
packs = {
    "Pack Génération de Leads B2B": [
        "Audit UX / UI (Expérience Utilisateur)",
        "Conception de sites et Landing Pages Nocode (Duda, Shopify)",
        "Gestion et Optimisation Google Ads",
        "Réunions Progrès Mensuelles"
    ],
    "Pack Co-Pilote Stratégique": [
        "État des lieux et stratégie transversale",
        "Audit SEO & Sémantique",
        "Accompagnement stratégique et opérationnel récurrent",
        "Maintenance & Supervision Analytique",
        "Réunions Progrès Mensuelles"
    ],
    "Pack Identité & Lancement": [
        "Concept de communication & Charte graphique",
        "Copywriting de performance",
        "Création de supports Print & Corporate",
        "Conception de sites et Landing Pages Nocode (Duda, Shopify)"
    ]
}

# Initialisation de l'état de la session pour conserver les choix de l'utilisateur
if "selected_services" not in st.session_state:
    st.session_state.selected_services = []

# Fonction pour appliquer un pack préconfiguré
def set_pack(pack_name):
    st.session_state.selected_services = packs[pack_name]

# Section : Packs Préconfigurés
st.header("🎯 Choisissez un pack préconfiguré")
col1, col2, col3 = st.columns(3)

with col1:
    st.info("### 🚀 Génération de Leads B2B")
    st.markdown("Idéal pour acquérir de nouveaux clients rapidement via un tunnel optimisé.")
    if st.button("Sélectionner ce pack", key="btn_leads"):
        set_pack("Pack Génération de Leads B2B")

with col2:
    st.success("### 🧭 Co-Pilote Stratégique")
    st.markdown("L'offre d'accompagnement mensuel pour piloter votre croissance.")
    if st.button("Sélectionner ce pack", key="btn_copilote"):
        set_pack("Pack Co-Pilote Stratégique")

with col3:
    st.warning("### ✨ Identité & Lancement")
    st.markdown("Parfait pour poser les bases de votre marque et créer votre plateforme web.")
    if st.button("Sélectionner ce pack", key="btn_identite"):
        set_pack("Pack Identité & Lancement")

st.divider()

# Section : Configuration sur-mesure
st.header("🛠️ Ou personnalisez votre configuration")
st.markdown("Cochez ou décochez les prestations pour ajuster votre accompagnement :")

selected_now = []

# Affichage du catalogue sous forme d'accordéons
for category, services in catalog.items():
    with st.expander(category, expanded=False):
        for service in services:
            # Vérifier si le service est déjà sélectionné (soit manuellement, soit via un pack)
            is_checked = service in st.session_state.selected_services
            # Checkbox pour chaque prestation
            if st.checkbox(service, value=is_checked, key=service):
                selected_now.append(service)

# Mise à jour des services sélectionnés
st.session_state.selected_services = selected_now

st.divider()

# Section : Récapitulatif
st.header("📋 Votre sélection")
if st.session_state.selected_services:
    for s in st.session_state.selected_services:
        st.markdown(f"- ✅ {s}")
    
    st.write("---")
    st.subheader(f"Total : {len(st.session_state.selected_services)} prestation(s) sélectionnée(s).")
    
    # Formulaire de contact simulé
    with st.form("contact_form"):
        st.write("Laissez-nous vos coordonnées pour que Jean-François ou Laurent vous recontacte.")
        email = st.text_input("Votre adresse e-mail professionnel")
        entreprise = st.text_input("Nom de votre entreprise")
        submitted = st.form_submit_button("Envoyer ma demande de devis")
        
        if submitted:
            if email and entreprise:
                st.balloons()
                st.success(f"Merci ! Votre configuration a été transmise à l'Agence TIZ. Nous vous contacterons rapidement à l'adresse {email}.")
            else:
                st.error("Veuillez remplir votre e-mail et le nom de votre entreprise.")
else:
    st.info("Veuillez sélectionner des prestations ci-dessus ou choisir un pack préconfiguré pour voir le récapitulatif.")
