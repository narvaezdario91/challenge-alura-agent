## ADDED Requirements

### Requirement: Base Project Structure
The project SHALL have a standardized directory structure containing `src/agents`, `src/config`, and `src/shared`.

#### Scenario: Validating directory existence
- **WHEN** the scaffolding is applied
- **THEN** the folders `src/agents`, `src/config`, and `src/shared` exist with their respective `__init__.py` files

### Requirement: Component-Based Architecture for Agents
Every LangGraph agent in the system SHALL follow a component-based architecture where nodes and edges are grouped in directories with their corresponding prompts.

#### Scenario: Scaffolding `rag_support` agent
- **WHEN** the `rag_support` agent is scaffolded
- **THEN** it contains a `nodes` directory and an `edges` directory
- **THEN** it contains a sample node directory (e.g. `nodes/generate/`) containing `__init__.py`, `node.py`, and `prompt.py`
- **THEN** it contains a sample edge directory (e.g. `edges/intent_router/`) containing `__init__.py`, `edge.py`, and `prompt.py`

### Requirement: Agent Orchestrator
Each agent SHALL have an `agent.py` file that acts purely as an orchestrator to compile the `StateGraph` without containing business logic or prompts.

#### Scenario: `agent.py` structure
- **WHEN** reviewing the scaffolded `rag_support/agent.py`
- **THEN** it defines a `StateGraph` using the agent's state
- **THEN** it imports nodes and edges from their respective component directories
- **THEN** it does not define prompts or internal node logic
