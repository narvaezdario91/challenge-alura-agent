## Why

La gestión de dependencias y entornos virtuales en Python tradicionalmente ha sido lenta y fragmentada (usando `pip`, `venv`, `pipenv`, o `poetry`). `uv` es un gestor de paquetes ultra rápido escrito en Rust que unifica la gestión de entornos, resolución de dependencias y ejecución, acelerando el desarrollo de forma significativa.

## What Changes

- Inicialización del proyecto con `uv` (`uv init` u homologación de un `pyproject.toml`).
- Creación de un archivo `pyproject.toml` para definir las dependencias principales (ej. `langgraph`, `langchain`, etc.).
- Cambio en el flujo de trabajo documentado en el `README.md`: de usar `pip` a usar comandos de `uv` (ej. `uv sync`, `uv run`).

## Capabilities

### New Capabilities
- `package-management`: Gestión moderna, rápida y unificada de las dependencias y entornos del proyecto.

### Modified Capabilities


## Impact

Mejora exponencialmente los tiempos de instalación de dependencias y garantiza construcciones reproducibles y estables gracias al uso de `uv.lock`. Esto afecta positivamente el flujo de trabajo local de todos los desarrolladores.
