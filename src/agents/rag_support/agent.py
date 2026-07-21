import src.shared.patch_xxhash  # noqa: F401
from langgraph.graph import StateGraph, START, END
from src.agents.rag_support.state import AgentState
from src.agents.rag_support.nodes.retrieve.node import retrieve_node
from src.agents.rag_support.nodes.generate.node import generate_node
from src.agents.rag_support.edges.intent_router.edge import route_intent


def build_graph():
    """Construye y compila el grafo del agente RAG."""
    workflow = StateGraph(AgentState)

    workflow.add_node("retrieve", retrieve_node)
    workflow.add_node("generate", generate_node)

    # Condición de inicio basada en el intent router
    workflow.add_conditional_edges(
        START,
        route_intent,
        {
            "retrieve": "retrieve",
            "generate": "generate",
        },
    )

    workflow.add_edge("retrieve", "generate")
    workflow.add_edge("generate", END)

    return workflow.compile()
