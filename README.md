# 🤖 Agente RAG Conversacional - Challenge Alura

[![Python](https://img.shields.io/badge/Python-3.14%2B-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Framework-LangGraph%20%7C%20LangChain-orange.svg)](https://www.langchain.com/)
[![Frontend](https://img.shields.io/badge/UI-Streamlit-red.svg)](https://streamlit.io/)
[![Cloud Deployment](https://img.shields.io/badge/Cloud-Oracle%20Cloud%20(OCI)-red.svg)](https://cloud.oracle.com/)
[![Trello Board](https://img.shields.io/badge/Trello-Board%20del%20Proyecto-0079BF.svg?logo=trello&logoColor=white)](https://trello.com/b/VW6bR5kG/challenge-1-alura)
[![Package Manager](https://img.shields.io/badge/Package%20Manager-uv-purple.svg)](https://docs.astral.sh/uv/)

## 📋 Resumen Ejecutivo

Sistema inteligente de asistencia conversacional con arquitectura **RAG (Retrieval-Augmented Generation)** y procesamiento de documentos. La solución está construida sobre **LangGraph** utilizando la convención modular **SIDE (State, Instructions, Decisions, Execution)** y soporta múltiples proveedores de LLM y Embeddings (LM Studio Local, OpenAI y **Cohere API**).

* 📌 **Tablero de Gestión del Proyecto (Trello):** [Challenge 1 Alura - Trello Board](https://trello.com/b/VW6bR5kG/challenge-1-alura)

Para maximizar la portabilidad y evitar incompatibilidades de seguridad en entornos Windows (bloqueos de DLLs de C/C++), el sistema utiliza un **`LocalVectorStore`** en memoria basado en **NumPy** y **Pickle**, garantizando alta velocidad de recuperación vectorial sin dependencias nativas bloqueadas.

---

## 🌐 Despliegue en la Nube (OCI) y Acceso en Vivo

La solución se encuentra **desplegada y operativa** en una máquina virtual de **Oracle Cloud Infrastructure (OCI)**.

* 🔗 **Acceso Público a la Web UI (Frontend):** [http://158.247.126.149:8501](http://158.247.126.149:8501)

### Detalles de la Infraestructura en OCI
* **Instancia:** Compute Instance en Ubuntu 22.04 LTS (Arquitectura Ampere A1 ARM64 - OCI Always Free).
* **Gestión de Red:** Configuración de reglas de entrada de seguridad (`Ingress Rules`) en la VCN de Oracle Cloud y ajuste de `iptables` en el sistema operativo para permitir conexiones externas en el puerto `8501`.
* **Ejecución Persistente:** Servidor Streamlit optimizado para acceso remoto sin restricciones CORS/XSRF y ejecuciones continuas en segundo plano.

---

## 🆕 Novedades y Funcionalidades Recientes

- 🌐 **Soporte Multi-Proveedor (LM Studio / OpenAI / Cohere API)**: Capacidad de alternar dinámicamente entre servidores locales y la API de Cohere (`command-r-08-2024` y `embed-multilingual-v3.0`).
- ⚡ **Resiliencia y Procesamiento por Lotes (Batching)**: Manejo automático de límites de tasa de peticiones (Rate Limit `429`) en proveedores cloud mediante división en lotes y reintentos exponenciales.
- 🎨 **Interfaz Gráfica Modular (Streamlit)**: Nueva UI interactiva ubicada en `src/ui/` con streaming de respuestas en tiempo real token por token y panel de control lateral para la re-indexación vectorial.
- 🛡️ **Filtro de Archivos Temporales**: Ignorado automático de archivos de bloqueo de Excel (`~$*.xlsx`) durante la ingesta de documentos.

---

## 🏗️ Arquitectura del Sistema

```text
                               +-------------------------+
                               |     Usuario (UI/CLI)    |
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
                                 | (Cohere / LM Studio)  |
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
- 📡 **Generación en Streaming**: Interfaz interactiva por consola y Web UI con salida en tiempo real token por token.

---

## ⚙️ Requisitos Previos y Configuración

### 1. Variables de Entorno (`.env`)
Crea un archivo `.env` en la raíz del proyecto basándote en `.env.example`:

```ini
# Configuración del Servidor LLM & Embeddings (Providers: lm_studio | openai | cohere)
LLM_PROVIDER=cohere
LLM_BASE_URL=http://127.0.0.1:1234/v1

# Modelos recomendados para Cohere
LLM_MODEL_NAME=command-r-08-2024
EMBEDDING_MODEL_NAME=embed-multilingual-v3.0

# API Keys
LLM_API_KEY=lm-studio
COHERE_API_KEY=tu_cohere_api_key_aqui

LLM_TEMPERATURE=0.1
LLM_STREAMING=true

# Configuración RAG
KNOWLEDGE_BASE_DIR=knowledge_base
CHUNK_SIZE=800
CHUNK_OVERLAP=150
```

---

## 🚀 Instalación y Ejecución Local

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

### 4. Re-indexar la Base de Conocimiento (Opcional)

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
│   │   ├── llm_factory.py  # Fábrica de clientes OpenAI / LM Studio / Cohere
│   │   ├── patch_xxhash.py # Parche de compatibilidad Windows DLL
│   │   └── vector_store.py # LocalVectorStore con batching y retry en NumPy/Pickle
│   ├── ui/                 # Componentes modulares de interfaz gráfica Streamlit
│   │   ├── state.py        # Gestión de st.session_state y caché de LangGraph
│   │   └── components/
│   │       ├── sidebar.py  # Barra lateral con controles e información
│   │       └── chat.py     # Componente de chat e interacción en streaming
│   └── agents/
│       └── rag_support/    # Definición del agente RAG en LangGraph
│           ├── agent.py    # Ensamble del StateGraph
│           ├── state.py    # Estado conversacional (AgentState)
│           ├── system_prompt.py
│           ├── edges/      # Enrutamiento condicional (intent_router)
│           └── nodes/      # Nodos de ejecución (retrieve y generate)
├── app.py                  # Entrypoint principal de Streamlit Web UI
├── main.py                 # CLI ejecutable con interfaz streaming
├── pyproject.toml          # Definición de proyecto y dependencias UV
└── README.md
```
