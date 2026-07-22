# streamlit-ui

## Purpose
TBD

## Requirements

### Requirement: Interactive Streamlit Chat Interface
The system SHALL provide a web-based user interface using Streamlit to interact with the LangGraph RAG conversational agent in real-time.

#### Scenario: Streaming Chat Response in UI
- **WHEN** user submits a chat message via Streamlit input box
- **THEN** system streams LLM response tokens directly into the chat container in real time

#### Scenario: Render Chat History
- **WHEN** session re-runs or new messages are appended
- **THEN** system preserves and renders message history using `st.session_state`

### Requirement: Vector Store Management via Sidebar
The system SHALL provide a sidebar component in Streamlit to display environment settings and allow manual vector store re-indexing.

#### Scenario: Manual Re-indexing Trigger
- **WHEN** user clicks "Re-indexar Base de Conocimiento" button in sidebar
- **THEN** system triggers `get_vector_store(force_reload=True)` and notifies user upon completion
