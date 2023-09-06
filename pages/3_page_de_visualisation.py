import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

st.title('Page de visualisation des données')

if "data" not in st.session_state:
    st.warning('Veuillez d\'abord importer les données.')
else:
    data = st.session_state.data
    st.write('données d\'entrées.')
    st.dataframe(data.head())
    data1 = st.session_state.data1
    st.write('Données nettoyées et labelisées :')
    st.dataframe(data1.head())

    # Options pour l'utilisateur : sélectionner les colonnes pour les graphiques

    columns = data1.columns.tolist()

    # Graphique de dispersion
    st.header("Graphique de dispersion")
    x_axis = st.selectbox('Sélectionnez la colonne pour l\'axe X :', columns, key='x_axis')
    y_axis = st.selectbox('Sélectionnez la colonne pour l\'axe Y :', columns, key='y_axis')

    st.write(f'Graphique de dispersion entre {x_axis} et {y_axis}')

    fig, ax = plt.subplots()
    plt.scatter(data1[x_axis], data1[y_axis])
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    st.pyplot(fig)

    # Diagramme en barre
    st.header("Diagramme en barre")
    x_axis1 = st.selectbox('Sélectionnez la colonne pour l\'axe X :', columns, key='x_axis1')
    y_axis1 = st.selectbox('Sélectionnez la colonne pour l\'axe Y :', columns, key='y_axis1')

    st.write(f'Diagramme en barre entre {x_axis1} et {y_axis1}')
    plt.figure(figsize=(8, 6))
    fig, ax = plt.subplots()
    sns.barplot(x=data1[x_axis1], y=data1[y_axis1])
    plt.xlabel(x_axis1)
    plt.ylabel(y_axis1)
    st.pyplot(fig)

    # Diagramme circulaire
    st.header("Diagramme Circulaire")
    column_1 = st.selectbox('Sélectionnez la colonne pour le diagramme circulaire:', columns, key='column_1')

    st.write(f'Diagramme Circulaire pour la colonne {column_1}')
    pie_values = data1[column_1].value_counts()
    plt.figure(figsize=(8, 6))
    plt.pie(pie_values, labels=pie_values.index, autopct='%1.1f%%', startangle=140)
    st.pyplot(plt)

    # Diagramme linéaire
    st.header("Diagramme Linéaire")
    x_axis2 = st.selectbox('Sélectionnez la colonne pour l\'axe X du diagramme linéaire:', columns, key='x_axis2')
    y_axis2 = st.selectbox('Sélectionnez la colonne pour l\'axe Y du diagramme linéaire:', columns, key='y_axis2')

    st.write(f'Diagramme Linéaire entre {x_axis2} et {y_axis2}')
    plt.figure(figsize=(10, 6))
    sns.lineplot(x=data1[x_axis2], y=data1[y_axis2])
    plt.xlabel(x_axis2)
    plt.ylabel(y_axis2)
    st.pyplot(plt)

    # Sélection des colonnes pour le diagramme en barre pour une variable cible
    st.header("Diagramme en barre avec variable cible")
    x_axis3 = st.selectbox('Sélectionnez la colonne pour l\'axe X du diagramme linéaire:', columns, key='x_axis3')
    y_axis3 = st.selectbox('Sélectionnez la colonne pour l\'axe Y du diagramme linéaire:', columns, key='y_axis3')

    st.write(f'Diagramme en barre entre {y_axis3} et la variable cible {x_axis3}')
    plt.figure(figsize=(3, 1))
    grid = sns.FacetGrid(data1, col=x_axis3)
    grid.map(sns.countplot, y_axis3)
    plt.xlabel(y_axis3)
    st.pyplot(plt)


