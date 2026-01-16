import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

def show():
    st.title("📊 Statistiques COVID-19")

    col1, col2 = st.columns([2, 1])

    df = pd.read_csv("covid19_data.csv")

    with col1:
        st.info("""
        ### 📊 Statistiques clés
        
        Ce dataset contient :
        - *1 048 576* patients
        - *21* caractéristiques
        - Données du gouvernement mexicain
        """)

    st.subheader("Répartition par âge")
    df["AGE"] = pd.to_numeric(df["AGE"], errors="coerce")
    fig1 = px.histogram(df, x="AGE", nbins=20)
    st.plotly_chart(fig1, use_container_width=True)

    st.subheader("Répartition par sexe")
    fig2 = px.pie(df, names="SEX")
    st.plotly_chart(fig2, use_container_width=True)

    




    

    
