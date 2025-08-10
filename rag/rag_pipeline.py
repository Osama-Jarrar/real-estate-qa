import os
from rag.embedding import embed
from rag.retrieve import retrieve_ids_with_scores
from rag.chunking import chunk_dataset
from langchain.vectorstores import FAISS
from rag.embedding import get_embedding_model  # used if loading existing store
import pandas as pd


def rag_pipeline(file_path: str, query: str, k: int = 5, vector_store_path: str = "vector_store/", data_path: str = "Data/", raw_data_path: str = "Data/kc_house_data.csv"):
    
    if os.path.exists(os.path.join(data_path, "enriched_properties.csv")):
        print(f"[INFO] Using existing dataset at: {data_path}")
    else:
        print(f"[INFO] dataset not found. generating new data from raw data in: {data_path}")
        from Data_preprocessing.data_preprocessing_pipeline import full_pipeline
        full_pipeline(raw_data_path)
    
    if os.path.exists(os.path.join(vector_store_path, "index.faiss")):
        print(f"[INFO] Using existing vector store at: {vector_store_path}")
    else:
        print(f"[INFO] Vector store not found. Embedding documents into: {vector_store_path}")
        docs = chunk_dataset(file_path)
        embed(docs, save_path=vector_store_path)

    results = retrieve_ids_with_scores(query, k=k, path=vector_store_path)
    x = finalResult(results)
    return x

def finalResult(results):
    final_results = []
    df = pd.read_csv('Data/enriched_properties.csv')

    for result in results:
        doc_id = result["id"]
        score = result["score"]
        row = df[df['id'] == doc_id]
        if not row.empty:
            item = row.iloc[0].to_dict()   # convert the row to a dict
            item['score'] = score          
            final_results.append(item)
        else:
            print(f"[WARN] ID {doc_id} not found in dataset.")

    return final_results

