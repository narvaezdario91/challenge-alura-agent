import src.shared.patch_xxhash  # noqa: F401
import asyncio
import sys
from dotenv import load_dotenv
from src.config.settings import settings
from src.shared.vector_store import get_vector_store
from src.agents.rag_support.agent import build_graph

load_dotenv()


async def main_async():
    print("==================================================")
    print("      Agente de Chat Alura - RAG + LM Studio     ")
    print("==================================================")
    print(f"Servidor LLM Target: {settings.LLM_BASE_URL}")
    print(f"Modelo LLM: {settings.LLM_MODEL_NAME}")
    print(f"Modelo Embeddings: {settings.EMBEDDING_MODEL_NAME}")
    print("==================================================\n")

    force_reindex = "--reindex" in sys.argv
    if force_reindex:
        print("Opción --reindex detectada. Re-indexando la base de conocimiento...")
        get_vector_store(force_reload=True)
    else:
        print("Cargando base de conocimiento...")
        get_vector_store(force_reload=False)

    app = build_graph()
    print("\n¡Agente listo! Escribe tu consulta (o 'salir' para finalizar).\n")

    while True:
        try:
            user_input = input("\nUsuario: ").strip()
            if not user_input:
                continue
            if user_input.lower() in ("salir", "exit", "quit"):
                print("¡Hasta luego!")
                break

            print("\nAsistente: ", end="", flush=True)

            inputs = {"messages": [("user", user_input)]}

            # Invocación en streaming a través del grafo
            async for event in app.astream_events(inputs, version="v2"):
                kind = event.get("event")
                if kind == "on_chat_model_stream":
                    chunk = event["data"]["chunk"]
                    if hasattr(chunk, "content") and chunk.content:
                        print(chunk.content, end="", flush=True)

            print()

        except KeyboardInterrupt:
            print("\nOperación cancelada. ¡Hasta luego!")
            break
        except Exception as e:
            print(f"\n[Error de comunicación]: {e}")
            print("Verifica que LM Studio esté corriendo y exponiendo la API en " + settings.LLM_BASE_URL)


def main():
    asyncio.run(main_async())


if __name__ == "__main__":
    main()
