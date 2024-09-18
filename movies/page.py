import pandas as pd
import streamlit as st
from datetime import datetime
from st_aggrid import AgGrid
from actors.service import ActorService
from genres.service import GenreService
from movies.service import MovieService


def show_movies():
    movie_service = MovieService()
    movies = movie_service.get_movies()
    if movies:
        st.write('Lista Filmes')
        # aggrid so aceita dataframe, usamos pandas para converter
        movies_df = pd.json_normalize(movies)
        # remover coluna actors pois é multivalores, e remover id para elegancia        movies_df = movies_df.drop(columns=['actors', 'genre.id'])
        AgGrid(
            data=movies_df,
            key='movies_grid',
        )
    else:
        st.warning('Nenhum filme encontrado')

    # cadastrar novos filmes
    st.title('Cadastrar novo Filme')
    title = st.text_input('Título')
    release_date = st.date_input(
        label='Data de lançamento',
        value=datetime.today(),
        min_value=datetime(1800, 1, 1).date(),
        max_value=datetime.today(),
        format='DD/MM/YYYY',
    )

    # vai precisar carregar a lista de generos ---------
    genre_service = GenreService()
    genres = genre_service.get_genres()
    # list compreesion
    genres_names = {genre['name']: genre['id'] for genre in genres}
    selected_genres_name = st.selectbox('Gênero', list(genres_names.keys()))

    # vai precisar carregar a lista de Atores ----------
    actor_service = ActorService()
    actors = actor_service.get_actors()
    # list compreesion
    actor_names = {actor['name']: actor['id'] for actor in actors}
    selected_actors_names = st.multiselect('Atores/Atrizes', list(actor_names.keys()))
    # outra lis compreensin para listar apenas ids ex. [1,3,7]
    selected_actors_ids = [actor_names[name] for name in selected_actors_names]

    resume = st.text_area('Resumo')
    if st.button('Cadastrar'):
        new_movie = movie_service.create_movie(
            title=title,
            release_date=release_date,
            genre=genres_names[selected_genres_name],
            actors=selected_actors_ids,
            resume=resume,
        )
        if new_movie:
            st.rerun()
        else:
            st.error('Erro ao cadastrar filme. Verifique os campos')
