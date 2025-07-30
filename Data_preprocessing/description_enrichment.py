
import pandas as pd
from pathlib import Path
from utils.model_loader import load_quantized_phi4_generator

CHECKPOINT_PATH = Path("Data/enriched_properties_temp.csv")
FINAL_OUTPUT_PATH = Path("Data/enriched_properties.csv")

BATCH_SIZE = 25
generator = load_quantized_phi4_generator()

# === Prompt Template ===
# === Prompt template ===
def _build_prompt(row):
    return f"""You are a real estate assistant. Generate a concise property listing description based on the following features:

- Price: {row['price']}
- Number of bedrooms: {row['bedrooms']}
- Number of bathrooms, where .5 accounts for a room with a toilet but no shower: {row['bathrooms']}
- Square footage of the apartments interior living space: {row['sqft_living']}
- Square footage of the land space for the house: {row['sqft_lot']}
- Number of floors (levels) in the house: {row['floors']}
- does the apartment overlook a waterfront or not: {row['waterfront']}
- view : {row['view']}
- condition: {row['condition']}
- grade: {row['grade']}
- The square footage of the interior housing space that is above ground level: {row['sqft_above']}
- The square footage of the interior housing space that is below ground level: {row['sqft_basement']}
- The year the house was initially built: {row['yr_built']}
- The year of the house’s last renovation: {row['yr_renovated']}
- What zipcode area the house is in: {row['zipcode']}
- Lattitude: {row['lat']}
- Longitude: {row['long']}
- was renovatedt: {row['was_renovated']}
- years since renovation: {row['years_since_renovation']}


Description:""".strip()


# === Load Dataset and Merge Checkpoint ===
def _prepare_dataset(df):
    df = df.copy()
    df.set_index("id", inplace=True)
    df["description"] = df.get("description", pd.NA)

    if CHECKPOINT_PATH.exists():
        checkpoint_df = pd.read_csv(CHECKPOINT_PATH).set_index("id")
        df.update(checkpoint_df)
        print(f"Loaded checkpoint with {checkpoint_df['description'].notna().sum()} enriched rows.")

    df.fillna("N/A", inplace=True)
    return df

# === Enrichment Logic ===
def _enrich_missing_descriptions(df):
    to_enrich = df[df["description"].isna() | (df["description"] == "N/A")]
    print(f"{len(to_enrich)} rows need enrichment")

    enriched = 0
    prompts, indices = [], []

    for i, (idx, row) in enumerate(to_enrich.iterrows(), 1):
        prompts.append(_build_prompt(row))
        indices.append(idx)

        if len(prompts) == BATCH_SIZE or i == len(to_enrich):
            try:
                outputs = generator(prompts, max_new_tokens=300, do_sample=True, temperature=0.7)
                for j, out in enumerate(outputs):
                    desc = out[0]["generated_text"].split("Description:")[-1].strip()
                    df.at[indices[j], "description"] = desc
                enriched += len(prompts)
                print(f"Enriched {enriched} rows... checkpointing")
                df[["description"]].to_csv(CHECKPOINT_PATH)
            except Exception as e:
                print(f"Error during batch enrichment: {e}")
            prompts, indices = [], []

# === Save Final Output ===
def _finalize(df):
    df.to_csv(FINAL_OUTPUT_PATH)
    print(f"Saved enriched dataset to {FINAL_OUTPUT_PATH}")
    if CHECKPOINT_PATH.exists():
        CHECKPOINT_PATH.unlink()
        print("Checkpoint removed.")

# === Main Pipeline ===
def enrichment_pipeline(df: pd.DataFrame) -> pd.DataFrame:
    df = _prepare_dataset(df)
    _enrich_missing_descriptions(df)
    _finalize(df)
    return df
