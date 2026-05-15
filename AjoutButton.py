import pandas as pd
import streamlit as st
import numpy as np

def AjoutButton():
    st.title("Ajouter un nouvel élément")
    
    # Formulaire pour ajouter un nouvel élément
    with st.form(key='ajout_form'):
        nom = st.text_input("Nom de l'élément")
        description = st.text_area("Description de l'élément")
        submit_button = st.form_submit_button(label='Ajouter')
    
    if submit_button:
        # Logique pour ajouter l'élément à la base de données ou à la liste
        st.success(f"L'élément '{nom}' a été ajouté avec succès!")
        # Vous pouvez ajouter ici la logique pour enregistrer les données dans une base de données ou un fichier
if __name__ == "__main__":
    AjoutButton()