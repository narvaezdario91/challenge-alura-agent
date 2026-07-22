import asyncio
import streamlit as st


def render_chat_history():
    """Renderiza los mensajes acumulados en el historial de sesión de Streamlit."""
    for message in st.session_state.messages:
        role = message["role"]
        content = message["content"]
        with st.chat_message(role):
            st.markdown(content)


async def stream_graph_response(app, user_input, placeholder):
    """Ejecuta el streaming de eventos de LangGraph e imprime cada token en la UI."""
    inputs = {"messages": [("user", user_input)]}
    full_response = ""

    async for event in app.astream_events(inputs, version="v2"):
        kind = event.get("event")
        if kind == "on_chat_model_stream":
            chunk = event["data"]["chunk"]
            if hasattr(chunk, "content") and chunk.content:
                full_response += chunk.content
                placeholder.markdown(full_response + "▌")

    placeholder.markdown(full_response)
    return full_response
