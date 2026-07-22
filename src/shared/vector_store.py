import os
import pickle
import numpy as np
from langchain_core.documents import Document
from src.config.settings import settings
from src.shared.llm_factory import get_embeddings_client
from src.shared.ingestion import load_all_knowledge_base

CACHE_FILE = ".vector_cache.pkl"


class LocalVectorStore:
    """VectorStore liviano basado en NumPy y Pickle que no requiere DLLs de C (gRPC/ChromaDB)."""

    def __init__(self, documents: list[Document] = None, embeddings_matrix: np.ndarray = None):
        self.documents = documents or []
        self.embeddings_matrix = embeddings_matrix

    def save(self, filepath: str = CACHE_FILE):
        with open(filepath, "wb") as f:
            pickle.dump({"documents": self.documents, "embeddings": self.embeddings_matrix}, f)
        print(f"Base vectorial guardada exitosamente en {filepath}")

    @classmethod
    def load(cls, filepath: str = CACHE_FILE):
        if not os.path.exists(filepath):
            return None
        with open(filepath, "rb") as f:
            data = pickle.load(f)
            return cls(documents=data["documents"], embeddings_matrix=data["embeddings"])

    def similarity_search(self, query_vector: list[float], k: int = 4) -> list[Document]:
        if not self.documents or self.embeddings_matrix is None or len(self.embeddings_matrix) == 0:
            return []

        q_vec = np.array(query_vector, dtype=np.float32)
        norm_q = np.linalg.norm(q_vec)
        if norm_q == 0:
            return self.documents[:k]

        matrix = self.embeddings_matrix
        norms_m = np.linalg.norm(matrix, axis=1)
        # Evitar división por cero
        norms_m[norms_m == 0] = 1e-10

        similarities = np.dot(matrix, q_vec) / (norms_m * norm_q)
        top_k_indices = np.argsort(similarities)[-k:][::-1]

        return [self.documents[idx] for idx in top_k_indices]


import time


def _embed_documents_in_batches(embeddings_client, texts: list[str], batch_size: int = 40, delay: float = 1.5) -> list[list[float]]:
    """Genera embeddings en lotes para evitar límites de tasa (429 Rate Limit)."""
    all_embeddings = []
    total = len(texts)
    num_batches = (total + batch_size - 1) // batch_size

    for i in range(0, total, batch_size):
        batch = texts[i : i + batch_size]
        current_batch_num = i // batch_size + 1
        print(f"Procesando lote {current_batch_num}/{num_batches} ({len(batch)} pasajes)...")

        retries = 0
        while retries < 5:
            try:
                batch_embeddings = embeddings_client.embed_documents(batch)
                all_embeddings.extend(batch_embeddings)
                break
            except Exception as e:
                err_msg = str(e).lower()
                if "429" in err_msg or "rate limit" in err_msg or "too many requests" in err_msg:
                    retries += 1
                    wait_time = retries * 6
                    print(f"Límite de tasa alcanzado (429). Reintentando en {wait_time}s (intento {retries}/5)...")
                    time.sleep(wait_time)
                else:
                    raise e

        if i + batch_size < total and delay > 0:
            time.sleep(delay)

    return all_embeddings


_store_instance = None


def get_vector_store(force_reload: bool = False) -> LocalVectorStore:
    """Obtiene o inicializa el VectorStore local."""
    global _store_instance

    if _store_instance is not None and not force_reload:
        return _store_instance

    if not force_reload and os.path.exists(CACHE_FILE):
        print(f"Cargando índice vectorial desde caché ({CACHE_FILE})...")
        store = LocalVectorStore.load(CACHE_FILE)
        if store and len(store.documents) > 0:
            _store_instance = store
            return _store_instance

    print("Indexando base de conocimiento mediante cliente de embeddings...")
    documents = load_all_knowledge_base()
    if not documents:
        print("Advertencia: No se encontraron documentos para indexar.")
        _store_instance = LocalVectorStore()
        return _store_instance

    embeddings_client = get_embeddings_client()
    texts = [doc.page_content for doc in documents]

    print(f"Generando embeddings para {len(texts)} pasajes...")
    try:
        embeddings_list = _embed_documents_in_batches(embeddings_client, texts)
        matrix = np.array(embeddings_list, dtype=np.float32)
        store = LocalVectorStore(documents=documents, embeddings_matrix=matrix)
        store.save(CACHE_FILE)
        _store_instance = store
        return _store_instance
    except Exception as e:
        print(f"Error generando embeddings: {e}")
        # Retornar store con embeddings vacíos temporalmente para no bloquear la ejecución
        _store_instance = LocalVectorStore(documents=documents, embeddings_matrix=None)
        return _store_instance


def retrieve_relevant_documents(query: str, k: int = 4) -> list[Document]:
    """Recupera los documentos más similares a la consulta del usuario."""
    store = get_vector_store()
    if not store.documents or store.embeddings_matrix is None:
        return []

    embeddings_client = get_embeddings_client()
    formatted_query = f"search_query: {query}" if not query.startswith("search_query:") else query

    try:
        q_vector = embeddings_client.embed_query(formatted_query)
        return store.similarity_search(q_vector, k=k)
    except Exception as e:
        print(f"Error al obtener embedding de consulta: {e}")
        return []
