import streamlit as st
import numpy as np
import joblib

# -----------------------------
# Chargement du modèle (une seule fois)
# -----------------------------
@st.cache_resource
def load_model():
    model = joblib.load("svm_model.pkl")
    scaler = joblib.load("scaler.pkl")
    return model, scaler

model, scaler = load_model()

def show():
    # -----------------------------
    # CSS sombre
    # -----------------------------
    st.markdown("""
    <style>
    .stApp {background-color:#1e1e1e;color:#f0f0f0;}
    h1,h2,h3 {color:#f0f0f0;}
    div.stButton > button:first-child {
        background-color:#0d3b66;
        color:white;
        height:3em;
        width:100%;
        border-radius:10px;
        font-size:16px;
    }
    </style>
    """, unsafe_allow_html=True)

    # -----------------------------
    # Titre
    # -----------------------------
    st.title("🦠 Prédiction du risque COVID-19")
    st.write("""
    Ce modèle prédit si un patient COVID-19 est **à haut risque**
    ou **à faible risque** en fonction de ses caractéristiques médicales.
    """)

    st.markdown("---")

    # -----------------------------
    # Dictionnaire âge
    # -----------------------------
    age_dict = {
        1: "0-12 ans",
        2: "13-18 ans",
        3: "19-35 ans",
        4: "36-55 ans",
        5: "56 ans et plus"
    }

    st.subheader("👤 Informations du patient")

    AGE_GROUP = st.selectbox("Tranche d'âge", list(age_dict.values()))
    AGE_NUM = [k for k, v in age_dict.items() if v == AGE_GROUP][0]

    SEX = st.radio("Sexe", ["Homme", "Femme"])
    SEX_NUM = 1 if SEX == "Homme" else 2

    PREGNANT = 2
    if SEX_NUM == 2:
        preg = st.radio("Enceinte ?", ["Oui", "Non"])
        PREGNANT = 1 if preg == "Oui" else 2

    # -----------------------------
    # Antécédents médicaux
    # -----------------------------
    factors = {
        "PNEUMONIA": "Pneumonie",
        "DIABETES": "Diabète",
        "HIPERTENSION": "Hypertension",
        "CARDIOVASCULAR": "Maladie cardiovasculaire",
        "OBESITY": "Obésité",
        "RENAL_CHRONIC": "Maladie rénale chronique",
        "COPD": "BPCO",
        "ASTHMA": "Asthme",
        "INMSUPR": "Immunodépression",
        "OTHER_DISEASE": "Autres maladies",
        "TOBACCO": "Tabagisme"
    }

    user_input = {}
    for k, v in factors.items():
        user_input[k] = 1 if st.radio(f"{v} ?", ["Oui", "Non"], key=k) == "Oui" else 2

    # -----------------------------
    # Données d'entrée
    # -----------------------------
    input_data = np.array([[ 
        AGE_NUM,
        SEX_NUM,
        PREGNANT,
        user_input["PNEUMONIA"],
        user_input["DIABETES"],
        user_input["HIPERTENSION"],
        user_input["CARDIOVASCULAR"],
        user_input["OBESITY"],
        user_input["RENAL_CHRONIC"],
        user_input["COPD"],
        user_input["ASTHMA"],
        user_input["INMSUPR"],
        user_input["OTHER_DISEASE"],
        user_input["TOBACCO"]
    ]])

    # -----------------------------
    # Prédiction
    # -----------------------------
    if st.button("🔍 Prédire le risque"):
        input_scaled = scaler.transform(input_data)

        if hasattr(model, "decision_function"):
            score = model.decision_function(input_scaled)
            prob = 1 / (1 + np.exp(-score))
            prob = prob[0]
        else:
            prob = model.predict_proba(input_scaled)[0][1]

        pred = model.predict(input_scaled)[0]

        st.markdown("---")

        if pred == 1:
            st.error("⚠️ Patient à **HAUT RISQUE**")
            st.markdown(f"### Fiabilité de la prédiction : **{(1-prob)*100:.1f}%**")
        else:
            st.success("✅ Patient à **FAIBLE RISQUE**")
            st.markdown(f"### Fiabilité de la prédiction : **{prob*100:.1f}%**")
