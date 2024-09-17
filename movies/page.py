import pandas as pd
import streamlit as st
from st_aggrid import AgGrid



movies = [
    {
        'id': 1,
        'name': 'Matrix'
    },
    {
        'id': 2,
        'name': 'Rambo'
    },
    {
        'id': 3,
        'name': 'De volta para o futuro'
    },
]
def show_movies():
    st.write('Lista Filmes')
    # aggrid so aceita dataframe, usamos pandas para converter
    AgGrid(
        data=pd.DataFrame(movies),
        key='movies_grid',
    )
