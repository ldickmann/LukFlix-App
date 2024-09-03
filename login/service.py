import streamlit as st
from api.service import Auth


def login(username, password):
    """
    Realiza o login do usuário utilizando o serviço de autenticação.

    Args:
        username (str): O nome de usuário do usuário.
        password (str): A senha do usuário.

    Returns:
        None
    """
    auth_service = Auth()
    response = auth_service.get_token(
        username=username,
        password=password
    )
    if response.get('error'):
        st.error(f'Erro ao realizar login: {response.get("error")}')
    else:
        st.session_state.token = response.get('access')
        st.rerun()


def logout():
    for key in st.session_state.key():
        del st.session_state[key]
    st.rerun()
