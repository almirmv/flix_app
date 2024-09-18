'''sitema de cache foi necessario pois o streamlit faz rerun da pagina
inteira ate mesmo quando se escolhe uma data! isso gerava varias requisiçoes
na API Actors. Com cache local na session, reolvemos e melhoramos o desempenho.'''
import streamlit as st
from actors.repository import ActorRepository


class ActorService:

    def __init__(self):
        self.actor_repository = ActorRepository()

    def get_actors(self):
        # checa se tem cache na session
        if 'actors' in st.session_state:
            return st.session_state.actors
        # sem cache, pega da API e salva na session
        actors = self.actor_repository.get_actors()
        st.session_state.actors = actors  # guarda na session
        return actors  # retorna None ou actors

    def create_actor(self, name, birthday, nationality):
        # validaçoes futuras ficam no serice...
        actor = dict(
            name=name,
            birthday=birthday,
            nationality=nationality,
        )
        new_actor = self.actor_repository.create_actor(actor)
        st.session_state.actors.append(new_actor)  # atualiza cache
        return new_actor
