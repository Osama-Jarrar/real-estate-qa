# main.py


from rag.rag_pipeline import rag_pipeline

from rag.retrieve import retrieve_ids_with_scores

if __name__ == "__main__":

    RAW_PATH = "Data/enriched_properties.csv"
    

    x = rag_pipeline(RAW_PATH,"house less than 450k")
    print(x)