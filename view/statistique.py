import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

def show():
    st.title("📊 Statistiques COVID-19")

    df = pd.read_csv("covid19_data.csv")

    st.subheader("Répartition par âge")
    df["AGE"] = pd.to_numeric(df["AGE"], errors="coerce")
    fig1 = px.histogram(df, x="AGE", nbins=20)
    st.plotly_chart(fig1, use_container_width=True)

    st.subheader("Répartition par sexe")
    fig2 = px.pie(df, names="SEX")
    st.plotly_chart(fig2, use_container_width=True)


    st.subheader("Répartition par âge")

    df["AGE"] = pd.to_numeric(df["AGE"], errors="coerce")

    fig, ax = plt.subplots()
    ax.hist(df["AGE"].dropna(), bins=20)
    ax.set_title("Distribution des âges des patients")
    ax.set_xlabel("Âge")
    ax.set_ylabel("Nombre de patients")

    st.pyplot(fig)

    
