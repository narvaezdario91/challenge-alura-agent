## Context

El proyecto `challenge-alura-agent` cuenta con un sistema inicial y scaffolding de directorios alineados al estándar Multi-Agente (Modelo SIDE) con Arquitectura Basada en Componentes de LangGraph. Al ser una estructura robusta y anidada, un README actualizado es crítico para que cualquier mantenedor pueda visualizar y comprender rápidamente las reglas del proyecto (ej. "los prompts de un nodo viven dentro de la carpeta del nodo").

## Goals / Non-Goals

**Goals:**
- Presentar de forma visual la estructura del proyecto dentro del `README.md`.
- Explicar brevemente los 4 pilares SIDE (State, Instructions, Decisions, Execution) en los que se basó esta arquitectura.

**Non-Goals:**
- No documentaremos código interno ni detalles técnicos sobre agentes específicos, sino la arquitectura genérica de la carpeta `src/`.

## Decisions

- **Visualización en formato árbol**: Usaremos un bloque de código formato árbol ASCII para mostrar la jerarquía. Este formato ha demostrado ser el más entendible y universal para explicar estructuras de archivos.
- **Sobreescritura o actualización del README**: El README se actualizará añadiendo una sección concreta, o bien reemplazando contenido temporal si el README actual está vacío o es irrelevante.

## Risks / Trade-offs

- **Desactualización del README**: La estructura podría evolucionar y el README desactualizarse. 
  - *Mitigación*: Se debe instruir al equipo (o agentes futuros) de que cualquier cambio masivo en la arquitectura base debe ir acompañado de una actualización en la documentación.
