from Data_ingestion.load_data import load_csv

import pandas as pd

def _drop_duplicate_ids(df: pd.DataFrame) -> pd.DataFrame:
    """
    Drops duplicate property IDs, keeping only the latest entry based on sale date.

    Args:
        df (pd.DataFrame): Raw housing dataset.

    Returns:
        pd.DataFrame: Cleaned dataset with one entry per property ID.
    """
    df = df.copy()
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date").drop_duplicates(subset="id", keep="last")
    return df.reset_index(drop=True)


def _drop_irrelevant_columns(df):
    """
    Drops columns that are not relevant for the current project.

    Args:
        df (pd.DataFrame): Input dataframe.

    Returns:
        pd.DataFrame: Dataframe with irrelevant columns removed.
    """
    cols_to_drop = ["sqft_living15", "sqft_lot15","date"]
    existing_cols_to_drop = [col for col in cols_to_drop if col in df.columns]
    df = df.drop(columns=existing_cols_to_drop)
    return df



def data_cleaning_pipeline(file_path: str):
    """
    Executes the data cleaning pipeline.
    
    Args:
        file_path (str): Path to the CSV dataset.

    Returns:
        pd.DataFrame: The fully processed DataFrame.
    """
    # Load
    df = load_csv(file_path)

    # Clean
    df = _drop_duplicate_ids(df)
    df = _drop_irrelevant_columns(df)
    
    df.to_csv('Data/cleaned_properties.csv')

    return df

