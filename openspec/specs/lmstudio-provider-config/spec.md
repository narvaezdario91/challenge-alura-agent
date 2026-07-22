# lmstudio-provider-config

## Purpose
TBD

## Requirements

### Requirement: Externalized LLM Configuration
The system SHALL load LLM and Embedding provider settings from external environment variables without hardcoding endpoints or model names.

#### Scenario: Load LM Studio Settings
- **WHEN** application initializes
- **THEN** system loads `LLM_BASE_URL`, `LLM_MODEL_NAME`, `LLM_API_KEY`, and `LLM_STREAMING` from `.env` file or environment variables

### Requirement: LLM and Embedding Factory
The system SHALL instantiate ChatOpenAI and OpenAIEmbeddings clients directed to the configured `LLM_BASE_URL`.

#### Scenario: Instantiate Chat Client for LM Studio
- **WHEN** agent requests an LLM instance
- **THEN** factory returns a ChatOpenAI client connected to `http://127.0.0.1:1234/v1` with streaming enabled

#### Scenario: Instantiate Embeddings Client for Nomic
- **WHEN** ingestion pipeline or retriever requests an embeddings client
- **THEN** factory returns an OpenAIEmbeddings client connected to `http://127.0.0.1:1234/v1` configured for `nomic-embed-text-v1.5`
