from src.agents.rag_support.state import AgentState

GREETINGS_KEYWORDS = {"hola", "buenas", "buenos dias", "buenas tardes", "buenas noches", "saludos", "gracias", "adios", "chao"}


def route_intent(state: AgentState) -> str:
    """Evalúa la intención de la última consulta del usuario.
    Retorna 'retrieve' si requiere búsqueda RAG, o 'generate' si es saludo/conversación directa.
    """
    messages = state.get("messages", [])
    if not messages:
        return "generate"

    last_message = messages[-1].content.strip().lower()

    # Si es una palabra o frase corta de saludo/agradecimiento
    words = set(last_message.split())
    if len(words) <= 3 and words.intersection(GREETINGS_KEYWORDS):
        state["needs_rag"] = False
        return "generate"

    state["needs_rag"] = True
    return "retrieve"
