from langchain_core.messages import SystemMessage
from src.agents.rag_support.state import AgentState
from src.agents.rag_support.system_prompt import RAG_SYSTEM_PROMPT, DIRECT_SYSTEM_PROMPT
from src.shared.llm_factory import get_llm_client


def generate_node(state: AgentState) -> dict:
    """Nodo que invoca al LLM para generar la respuesta final."""
    messages = list(state.get("messages", []))
    context_docs = state.get("context_documents", [])
    needs_rag = state.get("needs_rag", True)

    llm = get_llm_client()

    if needs_rag and context_docs:
        context_str = "\n\n".join(context_docs)
        system_content = RAG_SYSTEM_PROMPT.format(context=context_str)
    else:
        system_content = DIRECT_SYSTEM_PROMPT

    full_messages = [SystemMessage(content=system_content)] + messages
    response = llm.invoke(full_messages)

    return {"messages": [response]}
