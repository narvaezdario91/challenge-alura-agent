## ADDED Requirements

### Requirement: Document Component-Based Architecture
The project README SHALL contain a section titled "Estructura del Proyecto" that explains the component-based architecture for LangGraph agents.

#### Scenario: Explaining directory layout
- **WHEN** a developer reads the README
- **THEN** they see an ASCII directory tree representing the `src/` folder structure
- **THEN** they see an explanation of how nodes, edges, and prompts are grouped together

### Requirement: Document SIDE Framework
The project README SHALL explain the 4 pillars of the SIDE framework (State, Instructions, Decisions, Execution) and how they map to the project's files.

#### Scenario: Mapping SIDE to files
- **WHEN** a developer reads the architecture section
- **THEN** they understand that State maps to `state.py`, Instructions to `prompt.py`, Decisions to `edges/`, and Execution to `nodes/`
