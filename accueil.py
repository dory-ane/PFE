import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Page d\'accueil')

st.markdown("Hello, Bienvenue sur notre application de nettoyage et de visualisation de la donnée.  "
            "Merci d'avoir choisi notre solution pour l'analyse de vos données.  "
            "En espérant que notre application vous plaira et qu\'elle répondra à vos besoins,"
            "nous vous souhaitons une agréable expérience et une bonne analyse")

st.sidebar.write(
    "<div style='text-align:right; font-size:small;'>Conçu par Doriane Mbouzang </div>",
    unsafe_allow_html=True
)


