# challenge-alura-agent

## Instalación y Configuración

Este proyecto utiliza [uv](https://docs.astral.sh/uv/) como gestor de paquetes y dependencias. `uv` reemplaza herramientas tradicionales como `pip` o `poetry`, ofreciendo instalaciones y resoluciones mucho más veloces.

### Comandos básicos de `uv`

1. **Sincronizar el entorno virtual**:
   Para crear el entorno virtual (`.venv`) e instalar todas las dependencias definidas en el `uv.lock`:
   ```bash
   uv sync
   ```

2. **Añadir nuevas dependencias**:
   ```bash
   uv add <paquete>
   ```

3. **Ejecutar comandos en el entorno**:
   No necesitas activar manualmente el `.venv`. Usa `uv run`:
   ```bash
   uv run python src/agents/rag_support/agent.py
   ```

---

## Estructura del Proyecto (Project Structure)

Este proyecto utiliza una **Arquitectura Basada en Componentes** diseñada especialmente para construir agentes escalables con LangGraph y LangChain.

### Patrón SIDE y Arquitectura basada en componentes

Para garantizar la alta cohesión y mantenibilidad, la arquitectura sigue los 4 pilares del framework **SIDE** (State, Instructions, Decisions, Execution):

- **[S]tate**: El estado global de cada agente se define en su propio `state.py`.
- **[I]nstructions**: Los prompts del LLM nunca se mezclan con el código lógico. Si un nodo o una ruta necesita un prompt, este se ubica en su archivo correspondiente `prompt.py` junto a la lógica.
- **[D]ecisions**: La lógica de enrutamiento y condicionales (edges de LangGraph) se encuentra dentro de la carpeta `edges/`.
- **[E]xecution**: La ejecución de tareas y herramientas (nodes de LangGraph) se ubica dentro de la carpeta `nodes/`.

Esta convención asegura que cada componente es auto-contenido. Si se elimina un nodo, su lógica y sus prompts desaparecen sin dejar código inactivo en archivos monolíticos.

### Árbol de Directorios

```text
src/
├── config/              # Configuraciones globales
├── shared/              # Utilidades y recursos compartidos
└── agents/
    └── rag_support/     # Agente de ejemplo (soporte RAG)
        ├── __init__.py
        ├── agent.py     # Orquestador puro (instancia y compila el StateGraph)
        ├── state.py     # Define el AgentState
        ├── system_prompt.py
        ├── edges/       # Decisions (Enrutamiento)
        │   └── intent_router/
        │       ├── __init__.py
        │       ├── edge.py    # Lógica de ruteo
        │       └── prompt.py  # Prompt para clasificar intención
        └── nodes/       # Execution (Lógica)
            ├── generate/
            │   ├── __init__.py
            │   ├── node.py    # Lógica de generación de respuesta
            │   └── prompt.py  # Prompt para RAG
            └── retrieve/
                ├── __init__.py
                └── node.py    # Nodo (ej. búsqueda DB vectorizada)
```
