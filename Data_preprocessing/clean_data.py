import pandas as pd

def drop_duplicate_ids(df: pd.DataFrame) -> pd.DataFrame:
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


def drop_irrelevant_columns(df):
    """
    Drops columns that are not relevant for the current project.

    Args:
        df (pd.DataFrame): Input dataframe.

    Returns:
        pd.DataFrame: Dataframe with irrelevant columns removed.
    """
    cols_to_drop = ["sqft_living15", "sqft_lot15"]
    existing_cols_to_drop = [col for col in cols_to_drop if col in df.columns]
    df = df.drop(columns=existing_cols_to_drop)
    return df
