# pipelines/full_pipeline.py



from Data_preprocessing.clean_data import data_cleaning_pipeline
from Data_preprocessing.preprocess_data import feature_engineering_pipeline
from Data_preprocessing.description_enrichment import enrichment_pipeline

import pandas as pd

def full_pipeline(file_path: str) -> pd.DataFrame:
    df = data_cleaning_pipeline(file_path)
    df = feature_engineering_pipeline(df)
    df = enrichment_pipeline(df)
    return df
