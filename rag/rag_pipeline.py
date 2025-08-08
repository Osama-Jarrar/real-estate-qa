import os
from rag.embedding import embed
from rag.retrieve import retrieve_ids_with_scores
from rag.chunking import chunk_dataset
from langchain.vectorstores import FAISS
from rag.embedding import get_embedding_model  # used if loading existing store

def rag_pipeline(file_path: str, query: str, k: int = 5, vector_store_path: str = "vector_store/"):
    if os.path.exists(os.path.join(vector_store_path, "index.faiss")):
        print(f"[INFO] Using existing vector store at: {vector_store_path}")
    else:
        print(f"[INFO] Vector store not found. Embedding documents into: {vector_store_path}")
        docs = chunk_dataset(file_path)
        embed(docs, save_path=vector_store_path)

    results = retrieve_ids_with_scores(query, k=k, path=vector_store_path)
    return results
