import streamlit as st

st.set_page_config(
    page_title="COVID-19 Risk App",
    layout="wide",
    page_icon="🦠"
)

from view import acceuil, prediction, statistique, recommandation

# -----------------------------
# État du menu
# -----------------------------
if "hide_menu" not in st.session_state:
    st.session_state.hide_menu = True

# -----------------------------
# Bouton ON / OFF
# -----------------------------
if st.sidebar.button(
    "👁️ Afficher le menu Streamlit" if st.session_state.hide_menu else "🙈 Cacher le menu Streamlit"
):
    st.session_state.hide_menu = not st.session_state.hide_menu

# -----------------------------
# CSS conditionnel
# -----------------------------
if st.session_state.hide_menu:
    st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# -----------------------------
# Navigation personnalisée
# -----------------------------
page = st.sidebar.selectbox(
    "📌 Navigation",
    ["Accueil", "Prédiction du risque", "Statistiques", "Recommandations médicales"]
)

if page == "Accueil":
    acceuil.show()
elif page == "Prédiction du risque":
    prediction.show()
elif page == "Statistiques":
    statistique.show()
elif page == "Recommandations médicales":
    recommandation.show()
