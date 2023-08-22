import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Page d\'accueil')

column_1,column_2=st.columns(2)
with column_1:
    st.write("Bonjour")

with column_2:
    st.write("Aurevoir")
