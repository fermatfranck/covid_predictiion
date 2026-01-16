import streamlit as st

st.set_page_config(
    page_title="COVID-19 Risk App",
    layout="wide",
    page_icon="🦠"
)

from view import acceuil, prediction, statistique, recommandation



# -----------------------------
# Cacher le menu Streamlit
# -----------------------------
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
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