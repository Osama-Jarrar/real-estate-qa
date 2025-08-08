from rag.embedding import get_embedding_model
from langchain.vectorstores import FAISS
from sklearn.preprocessing import MinMaxScaler
import numpy as np

model = get_embedding_model()


def retrieve_ids_with_scores(query, k=5, normalize=True, sort_desc=True, path="vector_store/"):
    db = FAISS.load_local(path, model, allow_dangerous_deserialization=True)
    results = db.similarity_search_with_score(query, k=k)

    if normalize:
        scores = np.array([score for _, score in results]).reshape(-1, 1)
        scaler = MinMaxScaler()
        norm_scores = scaler.fit_transform(scores)
        scored_results = [(doc, float(1 - norm_score)) for (doc, _), norm_score in zip(results, norm_scores)]
    else:
        scored_results = [(doc, -score) for doc, score in results]  # higher = better

    if sort_desc:
        scored_results.sort(key=lambda x: x[1], reverse=True)

    final_output = []
    for doc, score in scored_results:
        property_id = doc.metadata.get("id")
        if property_id is not None and score > 0.5:
            final_output.append({
                "id": property_id,
                "score": round(score, 4)
            })

    return final_output
