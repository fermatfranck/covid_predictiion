import streamlit as st
from PIL import Image
import os
from pathlib import Path

def show():
    st.title("🦠 Bienvenue dans l'application COVID-19")

    # Charger l’image (chemin sûr)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = Path(__file__).parent.parent / "assets" / "123.jpg"
    image = Image.open(image_path)

    # Afficher l’image
    st.image(image, use_container_width=True)

    st.write("""
    Cette application utilise l'apprentissage automatique pour analyser et prédire les risques 
    associés à la maladie à coronavirus (COVID-19).
    
    """)

      # Présentation de la maladie
    st.header("📋 Qu'est-ce que le COVID-19 ?")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        La *maladie à coronavirus (COVID-19)* est une maladie infectieuse causée par un coronavirus 
        récemment découvert. 
        
        ### Symptômes principaux
        - Maladie respiratoire légère à modérée
        - La plupart des personnes se rétablissent sans traitement particulier
        
        ### Populations à risque
        Les personnes suivantes sont plus susceptibles de développer une forme grave :
        - 👴 *Personnes âgées*
        - ❤️ *Maladies cardiovasculaires*
        - 🩺 *Diabète*
        - 🫁 *Maladies respiratoires chroniques*
        - 🎗️ *Cancer*
        """)
    
    
    
    # Objectif du projet
    st.header("🎯 Objectif du Projet")
    st.markdown("""
    L'objectif principal est de *construire un modèle d'apprentissage automatique* qui, 
    en fonction des symptômes, de l'état et des antécédents médicaux d'un patient, 
    permet de *prédire si le patient est à haut risque* ou non.
    
    ### Pourquoi c'est important ?
    - 🏥 *Optimiser l'allocation des ressources médicales*
    - ⚡ *Intervention rapide pour les patients à risque*
    - 📈 *Planification efficace des soins de santé*
    """)
    
   
    

    st.markdown("")

    st.subheader("📌 Fonctionnalités principales")
    st.markdown("""
    ✔ Prédiction par Machine Learning  
    ✔ Visualisation des données  
    ✔ Aide à la décision médicale  
    """)

    st.info("👉 Utilisez le menu à gauche pour naviguer.")
