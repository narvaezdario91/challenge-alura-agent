## Context

El proyecto requiere un sistema multi-agente que pueda escalar a futuro, integrando LangChain y LangGraph. Se necesita una estructura robusta para evitar que la lógica, el estado del agente y los prompts se mezclen. Tras investigar las convenciones oficiales y estándares de la industria (como el modelo SIDE - State, Instructions, Decisions, Execution), se ha optado por una **Arquitectura Basada en Componentes** aplicada de forma estricta.

## Goals / Non-Goals

**Goals:**
- Establecer un estándar jerárquico de directorios para todo el proyecto (`src/agents`, `src/config`, `src/shared`).
- Asegurar que cada nodo (nodes) o ruta (edges) de LangGraph encapsule su propia lógica y su prompt asociado.
- Preparar el terreno con un scaffolding estructurado (incluyendo un agente `rag_support` de muestra) para que los desarrolladores puedan comenzar a implementar inmediatamente con la arquitectura correcta.

**Non-Goals:**
- No implementaremos la lógica del LLM (llamadas reales a OpenAI, prompts complejos reales) en este cambio.
- No integraremos bases vectoriales ni configuraremos `langgraph.json` funcional, únicamente nos enfocamos en el scaffolding del código Python.

## Decisions

- **Arquitectura basada en componentes vs Archivos Monolíticos**: Se decidió agrupar por componente (ej. `src/agents/rag_support/nodes/generate/`) en lugar de archivos planos gigantes (`nodes.py` y `prompts.py`). Esto provee altísima cohesión. Si un nodo requiere un prompt, el archivo `prompt.py` vive al lado de su `node.py`. Si el nodo se elimina o refactoriza, el impacto es totalmente localizado.
- **`agent.py` como orquestador puro**: El archivo `agent.py` dentro de cada agente no tendrá lógica de negocio ni prompts, su única responsabilidad será instanciar `StateGraph`, importar nodos/rutas compilarlos, actuando como pegamento.
- **Re-exportación mediante `__init__.py`**: Cada carpeta de componentes exportará su función principal en su `__init__.py` para simplificar los imports en el `agent.py`.

## Risks / Trade-offs

- **Cantidad de archivos iniciales**: Puede haber una percepción de "exceso" de archivos pequeños al inicio (muchos directorios con `node.py` y `prompt.py`). 
  - *Mitigación*: La claridad mental al navegar y la facilidad para añadir un nuevo miembro al equipo a un agente específico justifican totalmente este modelo.
