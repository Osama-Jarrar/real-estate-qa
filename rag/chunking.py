from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
import pandas as pd
from pathlib import Path



def load_data(csv_path: str) -> pd.DataFrame:
    """
    Loads the enriched real estate dataset.

    Args:
        csv_path (str): Path to the enriched CSV.

    Returns:
        pd.DataFrame: Loaded dataset.
    """
    df = pd.read_csv(csv_path)
    return df


def format_listing_text(row: pd.Series) -> str:
    """
    Converts a property row into a natural language description.

    Args:
        row (pd.Series): A row from the DataFrame.

    Returns:
        str: Natural language text for semantic search.
    """
    # Use your generated description if available
    if "description" in row and pd.notnull(row["description"]):
        return row["description"]


def row_to_documents(row: pd.Series, splitter: RecursiveCharacterTextSplitter) -> list:
    """
    Converts a DataFrame row to one or more LangChain Documents.

    Args:
        row (pd.Series): A row from the DataFrame.
        splitter (RecursiveCharacterTextSplitter): Text splitter instance.

    Returns:
        List[Document]: One or more chunks from the listing.
    """
    text = format_listing_text(row)
    metadata = {
        "id": row.get("id", None),
        "location": row.get("location", None),
        "price": row.get("price", None),
        "bedrooms": row.get("bedrooms", None),
        "bathrooms": row.get("bathrooms", None),
        "sqft_living": row.get("sqft_living", None),
        "sqft_lot": row.get("sqft_lot", None),
        "floors": row.get("floors", None),
        "waterfront": row.get("waterfront", None),
        "grade": row.get("grade", None),
        "sqft_above": row.get("sqft_above", None),
        "sqft_basement": row.get("sqft_basement", None),
        "yr_built": row.get("yr_built", None),
        "yr_renovated": row.get("yr_renovated", None),
        "zipcode": row.get("zipcode", None),
        "lat": row.get("lat", None),
        "long": row.get("long", None),
        "was_renovated": row.get("was_renovated", None),
        "years_since_renovation": row.get("years_since_renovation", None),
        "view": row.get("view", None),
        "condition": row.get("condition", None),
    }

    chunks = splitter.split_text(text)
    return [Document(page_content=chunk, metadata=metadata) for chunk in chunks]


def chunk_dataset(csv_path: str) -> list:
    """
    Full pipeline: loads CSV, splits rows into Documents with metadata.

    Args:
        csv_path (str): Path to enriched CSV.

    Returns:
        List[Document]: Chunked and metadata-tagged documents.
    """
    df = load_data(csv_path)
    
    # Define chunking rules
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=512,
        chunk_overlap=64,
        separators=[". ", "\n", ","],
    )

    documents = []
    for _, row in df.iterrows():
        documents.extend(row_to_documents(row, splitter))

    return documents

