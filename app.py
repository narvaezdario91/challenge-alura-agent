import src.shared.patch_xxhash  # noqa: F401
import asyncio
import streamlit as st
from dotenv import load_dotenv

from src.ui.state import init_session_state, get_compiled_graph
from src.ui.components.sidebar import render_sidebar
from src.ui.components.chat import render_chat_history, stream_graph_response

load_dotenv()

# Configuración de página de Streamlit
st.set_page_config(
    page_title="Agente RAG Alura",
    page_icon="🤖",
    layout="wide",
)

st.title("🤖 Agente Conversacional Alura - RAG + LangGraph")
st.caption("Asistente inteligente con recuperación local de documentos e inventario")

# Inicialización de estado y componentes
init_session_state()
render_sidebar()
render_chat_history()

# Obtener instancia cacheada del grafo del agente
app_graph = get_compiled_graph()

# Entrada del usuario
if prompt := st.chat_input("Escribe tu consulta aquí..."):
    # Guardar y mostrar mensaje del usuario
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Respuesta del asistente con streaming
    with st.chat_message("assistant"):
        placeholder = st.empty()
        try:
            full_response = asyncio.run(stream_graph_response(app_graph, prompt, placeholder))
            st.session_state.messages.append({"role": "assistant", "content": full_response})
        except Exception as e:
            st.error(f"Error de comunicación con el agente: {e}")
            st.info("Verifica que LM Studio esté corriendo y el servidor esté activo.")
