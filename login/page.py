import streamlit as st
from login.service import login


def show_login():
    """
    Exibe a interface de login para o usuário.

    Esta função cria uma interface de login utilizando o Streamlit, onde o usuário pode
    inserir seu nome de usuário e senha. Quando o botão de login é pressionado, a função
    `login` é chamada com os dados fornecidos.
    """
    st.title('Login')

    username = st.text_input('Usuário')
    password = st.text_input(
        label='Senha',
        type='password'
    )

    if st.button('Login'):
        login(
            username=username,
            password=password
        )
