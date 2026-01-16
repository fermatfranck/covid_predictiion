import streamlit as st

def show():
    st.title("🦠 Bienvenue dans l'application COVID-19")

    st.write("""
    Cette application permet de :
    - Prédire le **risque COVID-19** d'un patient.
    - Analyser des **statistiques épidémiologiques**.
    - Fournir des **recommandations médicales** adaptées.
    """)
    

    st.markdown("")

    st.subheader("📌 Fonctionnalités principales")
    st.markdown("""
    ✔ Prédiction par Machine Learning  
    ✔ Visualisation des données  
    ✔ Aide à la décision médicale  
    """)

    st.info("👉 Utilisez le menu à gauche pour naviguer.")
