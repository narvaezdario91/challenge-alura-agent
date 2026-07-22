import src.shared.patch_xxhash  # noqa: F401
import streamlit as st
from src.agents.rag_support.agent import build_graph
from src.shared.vector_store import get_vector_store


@st.cache_resource
def get_compiled_graph():
    """Cachea la compilación del grafo del agente para evitar recargas en cada evento."""
    return build_graph()


def init_session_state():
    """Inicializa el historial de mensajes en st.session_state si no existe."""
    if "messages" not in st.session_state:
        st.session_state.messages = []
