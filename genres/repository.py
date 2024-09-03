import streamlit as st
import requests
from login.service import logout


class GenreRepository:
    """
    Classe para interagir com a API de gêneros.

    Esta classe fornece métodos para obter e criar gêneros via requisições HTTP
    para uma API RESTful.
    """
    def __init__(self):
        """
        Inicializa a classe GenreRepository com URLs base e cabeçalhos de autorização.

        Args:
            None
        """
        self.__base_url = 'https://ldickmann.pythonanywhere.com/api/v1/'
        self.__genres_url = f'{self.__base_url}genres/'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.token}'
        }

    def get_genres(self):
        """
        Obtém a lista de gêneros da API.

        Faz uma requisição GET para a URL de gêneros e retorna a lista de gêneros
        em formato JSON. Se o token de autorização for inválido, chama a função logout.

        Returns:
            dict: A lista de gêneros em formato JSON.
            None: Se o token de autorização for inválido.

        Raises:
            Exception: Se a requisição falhar com um código de status diferente de 200 ou 401.
        """
        response = requests.get(
            self.__genres_url,
            headers=self.__headers,
        )
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao obter dados da API. Status Code: {response.status_code}')

    def create_genre(self, genre):
        """
        Cria um novo gênero na API.

        Faz uma requisição POST para a URL de gêneros com os dados do novo gênero.
        Retorna os dados do gênero criado em formato JSON. Se o token de autorização
        for inválido, chama a função logout.

        Args:
            genre (dict): Dados do gênero a ser criado.

        Returns:
            dict: Dados do gênero criado em formato JSON se a requisição for bem-sucedida.
            None: Se o token de autorização for inválido.

        Raises:
            Exception: Se a requisição falhar com um código de status diferente de 201 ou 401.
        """
        response = requests.post(
            self.__genres_url,
            headers=self.__headers,
            data=genre,
        )
        if response.status_code == 201:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao obter dados da API. Status Code: {response.status_code}')
