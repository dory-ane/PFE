import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

st.title('Page de nettoyage des données')

if "data" not in st.session_state:
    st.warning('Veuillez d\'abord importer les données.')
else:
    data = st.session_state.data
    st.write('Données importées :')
    st.dataframe(data.head())

    # Code pour nettoyer les données (exemple : suppression des lignes avec des valeurs manquantes)
    # Regardons si le jeu de données contient des valeurs manquantes
    data.info()

    # Pour afficher la somme du nombre de valeur manqauntes par colonne; pour classer par ordre decroissaht
    data.isnull().sum().sort_values(ascending=False)

    # Affiche les valeurs statistiques des variables numériques
    #data.describe()

    # Affiche les valeurs statistiques des variables catégorielles
    if all(data[column].dtype == 'object' for column in data.columns):
       data.describe(include='O')
    else :
        data.describe()

    # Identifions les différents types de nos données
    data.dtypes

    # Separons la base de données en 2 groupe (1 groupe de variable catégorielle et 1 de variable numérique)
    cat_data = data.select_dtypes(include=['object']).copy()
    num_data = data.select_dtypes(exclude=['object']).copy()

    # Renseignons les données manquantes ==> pour les variables catégoriques,
    # on remplace les valeurs manquantes par la valeur la plus présente dans la colone
    cat_data = cat_data.apply(lambda x: x.fillna(x.value_counts().index[0]))

    # Renseignons les données manquantes ==> pour les variables numérique, on remplace
    # les valeurs manquantes de chaque colonne par la médiane de la colonne correspondante
    num_data = num_data.fillna(num_data.median())

    # Verifions si notre remplacement à fonctionner en essayant de visualiser
    # la somme des valeurs manquantes de chaque colonne de notre jeu de données
    cat_data.isnull().sum()
    num_data.isnull().sum()

    # Labelissons les varaiables catégorielles
    # Créons une instance de LabelEncoder
    label = LabelEncoder()
    for column in cat_data.columns:
        cat_data[column] = label.fit_transform(cat_data[column].astype(str))

    # Supprimer les colonnes en double
    cat_data = cat_data.loc[:, ~cat_data.columns.duplicated()]

    # Concatenons nos 2 datatframe en 1 dataframe pouvant être exploitable
    data1 = pd.concat([cat_data, num_data], axis=1)
    st.session_state.data1 = data1

    # data = data.dropna()


    st.write('Aperçu des données nettoyées :')
    st.dataframe(data1.head())
