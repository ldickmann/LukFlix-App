import requests


# Classe de serviço para autenticação do usuário.
class Auth:
    def __init__(self):
        """
        Inicializa a classe Auth com a URL base e a URL de autenticação.
        """
        self.__base_url = 'https://ldickmann.pythonanywhere.com/api/v1/'
        self.__auth_url = f'{self.__base_url}authentication/token/'

    def get_token(self, username, password):
        """
        Recupera um token de autenticação para o nome de usuário e senha fornecidos.

        Args:
            username (str): O nome de usuário do usuário.
            password (str): A senha do usuário.

        Returns:
            dict: Um dicionário contendo o token de autenticação se bem-sucedido,
            ou uma mensagem de erro se a autenticação falhar.
        """
        auth_payload = {
            'username': username,
            'password': password
        }
        auth_response = requests.post(
            self.__auth_url,
            data=auth_payload
        )
        if auth_response.status_code == 200:
            return auth_response.json()
        return {'error': f'Erro ao autenticar. Status code: {auth_response.status_code}'}
