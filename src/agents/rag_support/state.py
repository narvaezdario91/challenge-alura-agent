from typing import TypedDict, Annotated
import operator

class AgentState(TypedDict):
    messages: Annotated[list, operator.add]
    # Añadir más campos según necesidad (e.g. documents, current_intent)
