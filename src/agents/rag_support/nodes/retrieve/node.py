from src.agents.rag_support.state import AgentState
from src.shared.vector_store import retrieve_relevant_documents


def retrieve_node(state: AgentState) -> dict:
    """Nodo que recupera contexto relevante de la base de conocimiento ChromaDB."""
    messages = state.get("messages", [])
    if not messages:
        return {"context_documents": []}

    last_message = messages[-1].content
    docs = retrieve_relevant_documents(last_message, k=4)

    formatted_docs = []
    for doc in docs:
        source = doc.metadata.get("source_file", "Desconocido")
        # Remover prefijo de indexación si existe para limpiar la lectura del LLM
        content = doc.page_content.replace("search_document: ", "")
        formatted_docs.append(f"--- Fuente: {source} ---\n{content}")

    return {"context_documents": formatted_docs}
