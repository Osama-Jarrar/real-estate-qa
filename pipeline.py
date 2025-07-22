# pipeline.py

from Data_ingestion.load_data import load_csv
from Data_preprocessing.clean_data import drop_duplicate_ids, drop_irrelevant_columns
from Data_preprocessing.preprocess_data import add_renovation_features

def run_data_pipeline(file_path: str):
    """
    Executes the full data preprocessing pipeline.
    
    Args:
        file_path (str): Path to the CSV dataset.

    Returns:
        pd.DataFrame: The fully processed DataFrame.
    """
    # Load
    df = load_csv(file_path)

    # Clean
    df = drop_duplicate_ids(df)
    df = drop_irrelevant_columns(df)

    # Preprocess / Feature engineering
    df = add_renovation_features(df)

    return df
