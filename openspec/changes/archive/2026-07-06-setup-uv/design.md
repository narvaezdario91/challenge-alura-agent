## Context

El ecosistema actual de Python carece a menudo de estandarización en la resolución de dependencias, siendo lento y propenso a conflictos. `uv` es un instalador y resolutor de paquetes de Python ultra-rápido, escrito en Rust, que reemplaza herramientas como `pip`, `pip-tools`, `pipenv` y `poetry`. En nuestro proyecto Multi-Agente, la gestión rápida y reproducible de dependencias como `langgraph`, `langchain` y otras librerías de IA es fundamental.

## Goals / Non-Goals

**Goals:**
- Inicializar el proyecto con `uv` para gestionar dependencias.
- Estandarizar la definición de dependencias en un archivo `pyproject.toml`.
- Proveer instrucciones claras para los desarrolladores en el `README.md`.

**Non-Goals:**
- No migrar scripts complejos de CI/CD (si los hay) en esta etapa, solo el entorno local.
- No empaquetar el proyecto para PyPI.

## Decisions

- **Uso de `uv init`**: Utilizaremos `uv init` en la raíz del proyecto. Esto creará el archivo `pyproject.toml`. Si existe uno previo, lo actualizaremos.
- **Definición estándar `pyproject.toml`**: Añadiremos las dependencias de los frameworks (`langgraph`, `langchain`, etc.) bajo la tabla `[project.dependencies]`.
- **Bloqueo (Lockfile)**: Se generará un `uv.lock` que será versionado en Git para garantizar construcciones reproducibles.

## Risks / Trade-offs

- **Curva de adopción**: Los miembros del equipo acostumbrados a `pip` o `poetry` deberán aprender comandos de `uv`.
  - *Mitigación*: Documentar los 3-4 comandos clave (`uv run`, `uv sync`, `uv add`) directamente en el README, haciéndolo fácil de referenciar.
