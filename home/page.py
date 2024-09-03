import streamlit as st
import plotly.express as px
from movies.service import MovieService


def show_home():
    movie_service = MovieService()
    movie_stats = movie_service.get_movie_stats()

    st.title('Estatísticas de Filmes Cadastrados')

    if len(movie_stats['movies_by_genre']) > 0:
        st.subheader('Total de Filmes por Gênero:')
        fig = px.pie(
            movie_stats['movies_by_genre'],
            values='count',
            names='genre__name',
            title='Filmes por Gênero',
        )
        st.plotly_chart(fig)

    st.subheader('Total de Filmes Cadastrados:')
    st.write(movie_stats['total_movies'])

    st.subheader('Total de Avaliações:')
    st.write(movie_stats['total_reviews'])

    st.subheader('Média de Estrelas nas Avaliações:')
    st.write(movie_stats['average_stars'])
