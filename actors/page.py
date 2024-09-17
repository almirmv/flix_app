import pandas as pd
import streamlit as st
from st_aggrid import AgGrid


actors = [
    {
        'id': 1,
        'name': 'Leonardo Di Caprio'
    },
    {
        'id': 2,
        'name': 'Jim Carrey'
    },
    {
        'id': 3,
        'name': 'Robert de Niro'
    },
]
def show_actors():
    st.write('Lista de Atores/Atrizes')
    AgGrid(
        data=pd.DataFrame(actors),
        key='actors_grid',
    )

    st.title('Cdastrar novo Ator')
    name = st.text_input("Nome do Ator")
    if st.button('Cadastrar'):
        st.success(f'Ator {name} cadastrado!')