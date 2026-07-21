import os
import glob
import pandas as pd
from pypdf import PdfReader
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from src.config.settings import settings


def load_pdf_documents(knowledge_base_dir: str) -> list[Document]:
    """Carga y procesa todos los archivos PDF en la base de conocimiento usando pypdf."""
    documents = []
    pdf_files = glob.glob(os.path.join(knowledge_base_dir, "*.pdf"))

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=settings.CHUNK_SIZE,
        chunk_overlap=settings.CHUNK_OVERLAP,
    )

    for pdf_path in pdf_files:
        try:
            filename = os.path.basename(pdf_path)
            reader = PdfReader(pdf_path)
            raw_docs = []
            for i, page in enumerate(reader.pages):
                text = page.extract_text() or ""
                if text.strip():
                    raw_docs.append(
                        Document(
                            page_content=text,
                            metadata={"source_file": filename, "page": i + 1, "file_type": "pdf"},
                        )
                    )

            split_docs = text_splitter.split_documents(raw_docs)

            for doc in split_docs:
                # Nomic Embed Text v1.5 requiere el prefijo search_document:
                doc.page_content = f"search_document: {doc.page_content}"
                documents.append(doc)
        except Exception as e:
            print(f"Error procesando PDF {pdf_path}: {e}")

    return documents


def load_excel_documents(knowledge_base_dir: str) -> list[Document]:
    """Carga y procesa archivos Excel transformando filas en registros estructurados."""
    documents = []
    excel_files = glob.glob(os.path.join(knowledge_base_dir, "*.xlsx")) + glob.glob(os.path.join(knowledge_base_dir, "*.xls"))

    for excel_path in excel_files:
        try:
            filename = os.path.basename(excel_path)
            xls = pd.ExcelFile(excel_path)
            for sheet_name in xls.sheet_names:
                df = pd.read_excel(xls, sheet_name=sheet_name)
                df = df.dropna(how="all")

                for idx, row in df.iterrows():
                    # Formatear la fila como clave: valor
                    row_str = " | ".join([f"{col}: {val}" for col, val in row.items() if pd.notna(val)])
                    content = f"search_document: [Inventario/Fila {idx+1} - Hoja: {sheet_name}]\n{row_str}"

                    doc = Document(
                        page_content=content,
                        metadata={
                            "source_file": filename,
                            "sheet_name": sheet_name,
                            "row_index": idx + 1,
                            "file_type": "excel",
                        },
                    )
                    documents.append(doc)
        except Exception as e:
            print(f"Error procesando Excel {excel_path}: {e}")

    return documents


def load_all_knowledge_base(knowledge_base_dir: str | None = None) -> list[Document]:
    """Carga todos los documentos (PDFs y Excel) de la base de conocimiento."""
    kb_dir = knowledge_base_dir or settings.KNOWLEDGE_BASE_DIR
    if not os.path.exists(kb_dir):
        print(f"Advertencia: El directorio {kb_dir} no existe.")
        return []

    pdf_docs = load_pdf_documents(kb_dir)
    excel_docs = load_excel_documents(kb_dir)

    all_docs = pdf_docs + excel_docs
    print(f"Total de documentos procesados: {len(all_docs)} (PDFs: {len(pdf_docs)}, Excel: {len(excel_docs)})")
    return all_docs
