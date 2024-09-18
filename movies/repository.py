
import os
import requests
import streamlit as st
from dotenv import load_dotenv
from login.service import logout


load_dotenv()


class MovieRepository:

    def __init__(self):
        self.__base_url = os.environ['BASE_URL']
        self.__movies_url = f'{self.__base_url}movies/'
        self.__headers = {
            'authorization': f'Bearer {st.session_state.token}'
        }

    def get_movies(self):
        response = requests.get(
            self.__movies_url,
            headers=self.__headers,
        )
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        
        raise Exception(f'Erro ao obter dados da API. Status Code: {response.status_code}')
    
    def create_movie(self, movie):
        response = requests.post(
            self.__movies_url,
            headers=self.__headers,
            data=movie,
        )
        if response.status_code == 201:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        
        raise Exception(f'Erro ao obter dados da API. Status Code: {response.status_code}')

    def get_movie_stats(self):
        '''Pega as estatisticas dos filmes'''
        response = requests.get(
            f'{self.__base_url}movies/stats/',
            headers=self.__headers,            
        )
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao obter dados da API. Status code: {response.status_code}')