import src.shared.patch_xxhash  # noqa: F401
import os
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    LLM_PROVIDER: str = "lm_studio"
    LLM_BASE_URL: str = "http://127.0.0.1:1234/v1"
    LLM_MODEL_NAME: str = "nvidia/nemotron-3-nano-4b"
    EMBEDDING_MODEL_NAME: str = "nomic-ai/nomic-embed-text-v1.5-GGUF"
    LLM_API_KEY: str = "lm-studio"
    COHERE_API_KEY: str = ""
    LLM_TEMPERATURE: float = 0.1
    LLM_STREAMING: bool = True

    KNOWLEDGE_BASE_DIR: str = "knowledge_base"
    CHUNK_SIZE: int = 800
    CHUNK_OVERLAP: int = 150

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()
