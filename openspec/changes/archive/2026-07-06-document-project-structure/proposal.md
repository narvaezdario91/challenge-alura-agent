## Why

Actualmente, el proyecto cuenta con una arquitectura multi-agente basada en componentes (para LangChain y LangGraph) que es altamente modular y escalable. Sin embargo, para que nuevos desarrolladores o cualquier miembro del equipo pueda comprender rápidamente dónde ubicar el código, los prompts o la lógica de enrutamiento, es de vital importancia documentar esta estructura explícitamente en el archivo `README.md` del proyecto.

## What Changes

- Modificación del archivo `README.md` en la raíz del proyecto.
- Adición de una sección "Estructura del Proyecto" (Project Structure) que explique de forma visual (con un árbol de directorios) cómo funciona la arquitectura basada en componentes.
- Explicación de dónde colocar nuevos agentes, nodos, rutas y prompts, alineándolo conceptualmente con el marco SIDE (State, Instructions, Decisions, Execution).

## Capabilities

### New Capabilities
- `project-documentation`: Documentación general del proyecto, arquitectura y lineamientos para desarrolladores.

### Modified Capabilities


## Impact

El principal impacto es la mejora inmediata en el proceso de "onboarding" (integración) de nuevos desarrolladores al proyecto. Al tener la arquitectura documentada directamente en el README, se establecen convenciones claras que ayudarán a prevenir el desorden (spaghetti code) a medida que el proyecto crezca.
