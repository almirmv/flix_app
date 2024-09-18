'''Camada Service de Genres. Montar, concatenar, validar, limpar dados'''
import streamlit as st
from genres.repository import GenreRepository


class GenreService:

    # inicializa o repository
    def __init__(self):
        self.genre_repository = GenreRepository()

    def get_genres(self):
        # checa se tem cache na session
        if 'genres' in st.session_state:
            return st.session_state.genres
        # sem cache, pega da API e salva na session
        genres = self.genre_repository.get_genres()
        st.session_state.genres = genres  # guarda na session
        return genres  # retorna None ou genres

    def create_genre(self, name):
        genre = dict(
            name=name,
        )
        new_genre = self.genre_repository.create_genre(genre)
        st.session_state.genres.append(new_genre)
        return new_genre
