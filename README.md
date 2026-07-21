# 🤖 Agente RAG Conversacional - Challenge Alura

[![Python](https://img.shields.io/badge/Python-3.14%2B-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Framework-LangGraph%20%7C%20LangChain-orange.svg)](https://www.langchain.com/)
[![LLM Provider](https://img.shields.io/badge/LLM-LM%20Studio%20Local-green.svg)](https://lmstudio.ai/)
[![Package Manager](https://img.shields.io/badge/Package%20Manager-uv-purple.svg)](https://docs.astral.sh/uv/)

## 📋 Resumen Ejecutivo

Sistema inteligente de asistencia conversacional con arquitectura **RAG (Retrieval-Augmented Generation)** y procesamiento local. La solución está construida sobre **LangGraph** utilizando la convención modular **SIDE (State, Instructions, Decisions, Execution)** y consume modelos de lenguaje y embeddings ejecutados localmente mediante **LM Studio**.

Para maximizar la portabilidad y evitar incompatibilidades de seguridad en entornos Windows (bloqueos de DLLs de C/C++), el sistema utiliza un **`LocalVectorStore`** en memoria basado en **NumPy** y **Pickle**, garantizando alta velocidad de recuperación vectorial sin dependencias nativas bloqueadas.

---

## 🏗️ Arquitectura del Sistema

```text
                               +-------------------------+
                               |     Usuario (CLI)       |
                               +------------+------------+
                                            |
                                            v
                               +------------+------------+
                               |     Intent Router       |
                               | (Clasificador de flujo) |
                               +-----+---------------+---+
                                     |               |
                    [Pregunta sobre datos]     [Saludo / Conversación]
                                     |               |
                                     v               |
                         +-----------+-----------+   |
                         |     Retrieve Node     |   |
                         | (NumPy LocalVectorStore|  |
                         +-----------+-----------+   |
                                     |               |
                                     +-------+-------+
                                             |
                                             v
                                 +-----------+-----------+
                                 |     Generate Node     |
                                 |  (LM Studio Streaming)|
                                 +-----------------------+
```

### Principios de Arquitectura (Patrón SIDE)

- **[S]tate (`state.py`)**: Centraliza el estado conversacional del grafo (`AgentState`).
- **[I]nstructions (`system_prompt.py`)**: Aisla los prompts del sistema y plantillas contextuales.
- **[D]ecisions (`edges/`)**: Define la lógica condicional y enrutamiento inteligente de consultas.
- **[E]xecution (`nodes/`)**: Implementa la ejecución de tareas puras (recuperación de contexto y generación de respuestas en streaming).

---

## ✨ Características Clave

- 🧠 **Agente Autónomo en LangGraph**: Grafo de estados con capacidad de evaluar la intención de la consulta antes de decidir si requiere consulta documental (RAG) o respuesta directa.
- 📄 **Ingesta Multiformato**: Procesamiento automático de documentos **PDF** (fragmentación semántica) e **inventarios Excel** (estructuración clave-valor por filas).
- ⚡ **LocalVectorStore Pure-Python**: Almacenamiento y búsqueda vectorial rápida por Similitud de Coseno con **NumPy**, eliminando bloqueos de DLLs locales.
- 🛡️ **Compatibilidad Windows (`patch_xxhash`)**: Parche preventivo integrado para evitar fallos de ejecución por directivas de seguridad de Windows en dependencias internas de LangSmith.
- 📡 **Generación en Streaming**: Interfaz interactiva por consola con salida en tiempo real token por token.

---

## ⚙️ Requisitos Previos y Configuración

### 1. Servidor Local de LLM & Embeddings (LM Studio)
Asegúrate de tener instalado [LM Studio](https://lmstudio.ai/) y servir los siguientes modelos a través del servidor local (`http://127.0.0.1:1234/v1`):
* **Modelo LLM Chat**: `nvidia/nemotron-3-nano-4b` o `qwen2.5-coder-7b-instruct`.
* **Modelo Embeddings**: `nomic-ai/nomic-embed-text-v1.5-GGUF`.

### 2. Variables de Entorno (`.env`)
Crea un archivo `.env` en la raíz del proyecto basándote en `.env.example`:

```ini
# Configuración del Servidor LLM & Embeddings (LM Studio)
LLM_PROVIDER=lm_studio
LLM_BASE_URL=http://127.0.0.1:1234/v1
LLM_MODEL_NAME=nvidia/nemotron-3-nano-4b
EMBEDDING_MODEL_NAME=nomic-ai/nomic-embed-text-v1.5-GGUF
LLM_API_KEY=lm-studio
LLM_TEMPERATURE=0.1
LLM_STREAMING=true

# Configuración RAG
KNOWLEDGE_BASE_DIR=knowledge_base
CHUNK_SIZE=800
CHUNK_OVERLAP=150
```

---

## 🚀 Instalación y Ejecución

Este proyecto utiliza **[uv](https://docs.astral.sh/uv/)** para una gestión ultra rápida de dependencias y entornos virtuales.

### 1. Sincronizar Entorno Virtual

```bash
uv sync
```

### 2. Iniciar la Interfaz Web con Streamlit

Ejecuta la aplicación gráfica en tu navegador:

```bash
uv run streamlit run app.py
```

### 3. Iniciar el Agente en Consola (CLI)

También puedes interactuar mediante consola:

```bash
uv run python main.py
```


### 3. Re-indexar la Base de Conocimiento (Opcional)

Si agregas o modificas documentos dentro de la carpeta `knowledge_base/`, puedes forzar la re-indexación vectorial pasando el parámetro `--reindex`:

```bash
uv run python main.py --reindex
```

---

## 📁 Estructura del Proyecto

```text
challenge-alura-agent/
├── knowledge_base/         # Documentos fuente (PDFs y Excels de políticas/inventario)
├── src/
│   ├── config/             # Configuración centralizada Pydantic Settings
│   │   └── settings.py
│   ├── shared/             # Módulos transversales y fábrica de clientes
│   │   ├── ingestion.py    # Procesamiento e ingesta de PDF/Excel
│   │   ├── llm_factory.py  # Fábrica de clientes OpenAI / LM Studio
│   │   ├── patch_xxhash.py # Parche de compatibilidad Windows DLL
│   │   └── vector_store.py # LocalVectorStore basado en NumPy y Pickle
│   └── agents/
│       └── rag_support/    # Definición del agente RAG en LangGraph
│           ├── agent.py    # Ensamble del StateGraph
│           ├── state.py    # Estado conversacional (AgentState)
│           ├── system_prompt.py
│           ├── edges/      # Enrutamiento condicional (intent_router)
│           └── nodes/      # Nodos de ejecución (retrieve y generate)
├── main.py                 # CLI ejecutable con interfaz streaming
├── pyproject.toml          # Definición de proyecto y dependencias UV
└── README.md
```
