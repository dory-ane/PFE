import streamlit as st
import pandas as pd
import io
st.title('Page de collecte')

if "data" not in st.session_state:
    # Code pour collecter les données
    st.write('Importez vos données ici :')

    uploaded_file = st.file_uploader('Choisissez un fichier', type=['csv', 'xlsx', 'xls'])
    url_input = st.text_input("Entrez un lien URL :")

    if uploaded_file is not None:
        # Lecture d'un fichier téléchargé
        content = uploaded_file.getvalue().decode("utf-8")  # Obtention du contenu du fichier
        # Après avoir obtenu le fichier sous forme de séquence de bytes, decode() permet de le
        # convertir en une chaîne de caractères (string) en utilisant l'encodage UTF-8.

        # Détection du séparateur en comptant le nombre d'occurrences de différentes options
        possible_separators = [",", ";", "\t"]  # Les séparateurs possibles : "\t" représente le caractère de tabulation
        separator_counts = {sep: content.count(sep) for sep in possible_separators}
        best_separator = max(separator_counts, key=separator_counts.get)

        if best_separator == "\t":
            delimiter = "\t"
        else:
            delimiter = best_separator

        # Lecture du contenu en utilisant le séparateur détecté
        data = pd.read_csv(io.StringIO(content), sep=delimiter)

        st.write('Aperçu des données :')
        st.dataframe(data.head(15))
        st.session_state.data = data

    elif url_input != "":
        # Lecture à partir d'une URL
        try:
            data = pd.read_csv(url_input)
            st.write('Aperçu des données :')
            st.dataframe(data.head())
            st.session_state.data = data
        except Exception as e:
            st.write("Impossible de charger les données à partir de l'URL. Erreur :", e)

else:
    st.write('Aperçu des données :')
    st.dataframe(st.session_state.data.head())
