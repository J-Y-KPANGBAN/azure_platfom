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

# Ce code crée une interface utilisateur avec Streamlit pour ajouter un nouvel élément. Il comprend un formulaire avec des champs pour le nom et la description de l'élément, ainsi qu'un bouton de soumission. Lorsque le bouton est cliqué, un message de succès est affiché. Vous pouvez personnaliser la logique pour enregistrer les données selon vos besoins.
def main():
    AjoutButton()
    