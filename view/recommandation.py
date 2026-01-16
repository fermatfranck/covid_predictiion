import streamlit as st

def show():
    st.title("💡 Recommandations médicales")

    st.subheader("⚠️ Patients à haut risque")
    st.markdown("""
    - Consultez **immédiatement** un médecin ou un service d'urgence si symptômes graves
    - Surveillez la **saturation en oxygène** (SpO₂) et la température
    - Maintenez un **isolement strict** pour éviter la contamination
    - Suivi médical rapproché avec examens réguliers
    - Prenez vos médicaments habituels pour les maladies chroniques
    """)

    st.subheader("✅ Patients à faible risque")
    st.markdown("""
    - Repos et hydratation suffisants
    - Respect des **gestes barrières** : masque, lavage des mains, distanciation
    - Surveillance des symptômes : fièvre, toux, difficultés respiratoires
    - Consulter un médecin en cas d'aggravation
    - Vaccination à jour recommandée
    """)

    st.subheader("💊 Conseils généraux")
    st.markdown("""
    - Évitez la consommation excessive d’alcool
    - Adoptez une alimentation équilibrée pour renforcer le système immunitaire
    - Maintenez une activité physique adaptée si l'état le permet
    """)

    st.info("⚕️ Ces recommandations sont informatives et **ne remplacent pas un avis médical professionnel**.")
