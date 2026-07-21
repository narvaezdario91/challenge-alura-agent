# rag-chat-agent

## Purpose
TBD

## Requirements

### Requirement: Conversational Agent with RAG Pipeline
The system SHALL process user queries by routing intent and retrieving relevant information from ingested PDF and Excel documents before generating a response.

#### Scenario: RAG Retrieval and Response Generation
- **WHEN** user sends a query regarding company policies or supermarket inventory
- **THEN** system retrieves relevant document chunks from ChromaDB and generates a response based on the retrieved context

#### Scenario: Streaming Output Generation
- **WHEN** LLM produces response tokens
- **THEN** system streams each token in real-time to the caller

### Requirement: Document Ingestion for PDF and Excel
The system SHALL ingest PDF files and Excel spreadsheets located in `knowledge_base/` into the local vector store.

#### Scenario: PDF Document Ingestion
- **WHEN** PDF files are processed during ingestion
- **THEN** system extracts text, splits it into semantic chunks with overlapping boundaries, and stores embeddings with `search_document:` prefix

#### Scenario: Excel Document Ingestion
- **WHEN** Excel files are processed during ingestion
- **THEN** system formats rows into structured textual key-value records and stores their embeddings in the vector store
