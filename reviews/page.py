import pandas as pd
import streamlit as st
from movies.service import MovieService
from reviews.service import ReviewService
from st_aggrid import AgGrid


def show_reviews():
    review_service = ReviewService()
    reviews = review_service.get_reviews()

    if reviews:
        st.write('Lista Avaliações')
        reviews_df = pd.json_normalize(reviews)
        # aggrid so aceita dataframe, usamos pandas para converter
        AgGrid(
            data=reviews_df,
            key='reviews_grid',
        )
    else:
        st.warning('Nenhuma avaliação encontrada')

    # cadastrar nova avaliação
    st.title('Cadastrar nova avaliação')
    movie_service = MovieService()
    movies = movie_service.get_movies()
    # para mostrar lista com nomes dos filmes e nao os ids
    movie_titles = {movie['title']: movie['id'] for movie in movies}
    selected_movie_title = st.selectbox('Filme', list(movie_titles.keys()))

    stars = st.number_input(
        label='Estrelas',
        min_value=0,
        max_value=5,
        step=1,
    )

    comment = st.text_area('Comentário')

    if st.button('Cadastrar'):
        new_review = review_service.create_review(
            movie=movie_titles[selected_movie_title],  # atraves do nome pegamos o id
            stars=stars,
            comment=comment,
        )
        if new_review:
            st.rerun()
        else:
            st.error('Erro ao cadastrar avaliação. verifique os campos.')
