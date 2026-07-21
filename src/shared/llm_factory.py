from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from src.config.settings import settings


def get_llm_client(streaming: bool | None = None) -> ChatOpenAI:
    """Retorna una instancia configurada de ChatOpenAI dirigida al servidor LM Studio u otro endpoint OpenAI compatible."""
    is_streaming = streaming if streaming is not None else settings.LLM_STREAMING
    return ChatOpenAI(
        base_url=settings.LLM_BASE_URL,
        api_key=settings.LLM_API_KEY,
        model=settings.LLM_MODEL_NAME,
        temperature=settings.LLM_TEMPERATURE,
        streaming=is_streaming,
    )


def get_embeddings_client() -> OpenAIEmbeddings:
    """Retorna una instancia configurada de OpenAIEmbeddings dirigida a LM Studio."""
    return OpenAIEmbeddings(
        base_url=settings.LLM_BASE_URL,
        api_key=settings.LLM_API_KEY,
        model=settings.EMBEDDING_MODEL_NAME,
        check_embedding_ctx_length=False,
    )
