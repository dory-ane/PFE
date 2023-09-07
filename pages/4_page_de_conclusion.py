import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Page de conclusion")
if "data" not in st.session_state:
    st.warning('Veuillez d\'abord importer, nettoyer et visualiser les données.')
else:
    data = st.session_state.data
    # Code pour télécharger le graphique
    # Vous pouvez ajouter ici un texte de conclusion ou un résumé des résultats
    st.markdown ("Merci d'avoir utilisé notre application pour le nettoyage et la visualisation de vos données,"
                 "les données nettoyées et/ou labelissées sont maintenant prêtes, vous pouvez télécharger le résultat")

    # Téléchargement des données nettoyées
    csv_data = data.to_csv(index=False) # ne pas inclure la colone d'index dans le fichier final
    st.download_button('Télécharger les données nettoyées', data=csv_data, file_name='donnees_nettoyees.csv',
                       mime='text/csv') # lié au bouton download permet de choisir le type de fichier format csv dans ce cas