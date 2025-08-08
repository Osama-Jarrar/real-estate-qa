
from sentence_transformers import SentenceTransformer
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS


def get_embedding_model():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )



def embed(documents, save_path="vector_store/"):
    
    
    embedding_model = get_embedding_model()
    db = FAISS.from_documents(documents, embedding_model)
    db.save_local(save_path)
    return db
