import pandas as pd
import streamlit as st
from datetime import datetime
from st_aggrid import AgGrid
from actors.service import ActorService


def show_actors():
    actor_service = ActorService()
    actors = actor_service.get_actors()
    if actors:
        st.write('Lista de Atores/Atrizes')
        actors_df = pd.json_normalize(actors)
        AgGrid(
            data=actors_df,
            reload_data=True,
            key='actors_grid',
        )
    else:
        st.warning('Nenhum(a) ator/atriz cadastrado(a)')

    st.title('Novo cadastro do(a) Ator/Atriz')
    name = st.text_input('Nome do(a) Ator/Atriz')
    birthday = st.date_input(
        label='Data de Nascimento',
        value=datetime.today(),
        min_value=datetime(1800, 1, 1).date(),
        max_value=datetime.today(),
        format='DD/MM/YYYY',
    )
    nationality_dropdown = [
        'USA', 'BR', 'JP', 'KR', 'CN', 'IN', 'UK',
        'FR', 'IT', 'DE', 'CA', 'AU', 'CO', 'CL',
        'BO', 'UY', 'AR', 'PE', 'PT', 'IR'
    ]
    nationality = st.selectbox(
        label='Nacionalidade',
        options=nationality_dropdown,
    )

    if st.button('Cadastrar'):
        new_actor = actor_service.create_actor(
            name=name,
            birthday=birthday,
            nationality=nationality,
        )
        if new_actor:
            st.rerun()
        else:
            st.error('Erro ao cadastrar ator/atriz. Verifique os campos')
