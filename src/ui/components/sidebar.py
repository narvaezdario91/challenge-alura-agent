import streamlit as st
from src.config.settings import settings
from src.shared.vector_store import get_vector_store


def render_sidebar():
    """Renderiza el panel lateral con la configuración e información del entorno."""
    with st.sidebar:
        st.header("⚙️ Configuración del Agente")
        st.markdown("---")

        st.subheader("🤖 Servidor LLM & Embeddings")
        st.info(f"**URL:** {settings.LLM_BASE_URL}")
        st.write(f"**Modelo LLM:** `{settings.LLM_MODEL_NAME}`")
        st.write(f"**Modelo Embedding:** `{settings.EMBEDDING_MODEL_NAME}`")

        st.markdown("---")
        st.subheader("📚 Almacenamiento Vectorial")
        st.caption("Base de conocimiento local basada en NumPy + Pickle")

        if st.button("🔄 Re-indexar Base de Conocimiento", use_container_width=True):
            with st.spinner("Re-indexando documentos de `knowledge_base/`..."):
                get_vector_store(force_reload=True)
                st.success("¡Base de conocimiento re-indexada exitosamente!")

        st.markdown("---")
        st.caption("Challenge Alura - Agente RAG Conversacional")
