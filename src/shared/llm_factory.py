from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_cohere import ChatCohere, CohereEmbeddings
from src.config.settings import settings


def get_llm_client(streaming: bool | None = None):
    """Retorna una instancia configurada del cliente LLM según LLM_PROVIDER ('lm_studio', 'openai', 'cohere')."""
    is_streaming = streaming if streaming is not None else settings.LLM_STREAMING
    provider = settings.LLM_PROVIDER.lower().strip()

    if provider == "cohere":
        api_key = settings.COHERE_API_KEY or settings.LLM_API_KEY
        model_name = settings.LLM_MODEL_NAME if ("command" in settings.LLM_MODEL_NAME.lower() or "c4ai" in settings.LLM_MODEL_NAME.lower()) else "command-r-08-2024"
        return ChatCohere(
            cohere_api_key=api_key,
            model=model_name,
            temperature=settings.LLM_TEMPERATURE,
            streaming=is_streaming,
        )

    return ChatOpenAI(
        base_url=settings.LLM_BASE_URL,
        api_key=settings.LLM_API_KEY,
        model=settings.LLM_MODEL_NAME,
        temperature=settings.LLM_TEMPERATURE,
        streaming=is_streaming,
    )


def get_embeddings_client():
    """Retorna una instancia configurada del cliente de Embeddings según LLM_PROVIDER."""
    provider = settings.LLM_PROVIDER.lower().strip()

    if provider == "cohere":
        api_key = settings.COHERE_API_KEY or settings.LLM_API_KEY
        embedding_model = settings.EMBEDDING_MODEL_NAME if "embed" in settings.EMBEDDING_MODEL_NAME else "embed-multilingual-v3.0"
        return CohereEmbeddings(
            cohere_api_key=api_key,
            model=embedding_model,
        )

    return OpenAIEmbeddings(
        base_url=settings.LLM_BASE_URL,
        api_key=settings.LLM_API_KEY,
        model=settings.EMBEDDING_MODEL_NAME,
        check_embedding_ctx_length=False,
    )

