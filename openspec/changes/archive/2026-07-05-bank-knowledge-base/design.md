## Context

Para entrenar y probar un agente RAG (Retrieval-Augmented Generation) con LangChain y LangGraph, se necesitan datos que reflejen el nivel de complejidad del mundo real. La creación de documentos Markdown de un banco digital ficticio (AluraBank) proporciona este entorno, ya que incluye variabilidad de reglas, límites numéricos y flujos condicionales que retarán al agente.

## Goals / Non-Goals

**Goals:**
- Generar cinco documentos en formato Markdown que sirvan como base de conocimiento.
- Incluir casos lógicos complejos (e.g., límites diferenciados por nivel de usuario, plazos estrictos para reclamos) para probar las capacidades de razonamiento y extracción del RAG.

**Non-Goals:**
- Construir el sistema RAG o los nodos de LangGraph en esta etapa. Este cambio abarca estrictamente la creación de la base de datos (archivos).

## Decisions

- **Formato de Archivo:** Markdown (`.md`).
  *Razón:* Es fácilmente procesable por herramientas como `MarkdownHeaderTextSplitter` de LangChain, lo que permite preservar la jerarquía de los títulos como metadatos valiosos dentro de la base vectorial.
- **Estructura del Contenido:** Textos con alto nivel de condicionalidad ("Si X, entonces Y").
  *Razón:* Un RAG básico suele fallar en condicionales. Proveer este nivel de detalle servirá de benchmark para el sistema de recuperación y razonamiento (Agentic RAG).
- **Datos Seguros:** Uso de datos totalmente ficticios ("AluraBank").
  *Razón:* Evita problemas de privacidad (PII) o el uso de datos confidenciales del mundo real.

## Risks / Trade-offs

- **Riesgo:** Los documentos pueden crecer en complejidad y el LLM de recuperación podría alucinar, cruzando reglas de diferentes políticas.
  *Mitigación:* Los documentos estarán fuertemente estructurados usando encabezados H2 y H3 claros, y listas con viñetas para delimitar las reglas y facilitar la tarea del RAG.
