from datetime import datetime
import pandas as pd

def _add_renovation_features(df):
    df["was_renovated"] = df["yr_renovated"] > 0
    df["years_since_renovation"] = (
        datetime.now().year - df["yr_renovated"]
    ).where(df["was_renovated"], 0)
    return df

def _encode_waterfront(df):
    df['waterfront'] = df['waterfront'].map({1: True, 0: False})
    return df

def _encode_view(df):
    view_map = {
        0: 'No view',
        1: 'Poor view',
        2: 'Fair view',
        3: 'Good view',
        4: 'Excellent view'
    }
    df['view'] = df['view'].map(view_map).fillna('Unknown view')
    return df

def _encode_condition(df):
    condition_map = {
        1: 'Poor condition',
        2: 'Fair condition',
        3: 'Average condition',
        4: 'Good condition',
        5: 'Excellent condition'
    }
    df['condition'] = df['condition'].map(condition_map).fillna('Unknown condition')
    return df

def _encode_grade(df):
    def grade_label(g):
        if g in [1, 2, 3]:
            return 'Below average construction and design'
        elif g == 7:
            return 'Average construction and design'
        elif g in [11, 12, 13]:
            return 'High quality construction and design'
        elif 4 <= g <= 6 or 8 <= g <= 10:
            return 'Above average construction and design'
        else:
            return 'Unknown grade'
    df['grade'] = df['grade'].apply(grade_label)
    return df


def _encode_features(df):
    df = _encode_waterfront(df)
    df = _encode_view(df)
    df = _encode_condition(df)
    df = _encode_grade(df)
    return df



def feature_engineering_pipeline(df: pd.DataFrame) -> pd.DataFrame:
    """
    Applies all feature engineering steps to the DataFrame.
    
    Args:
        df (pd.DataFrame): Cleaned DataFrame.

    Returns:
        pd.DataFrame: DataFrame with new features.
    """
    # Add features
    df = _add_renovation_features(df)
    df = _encode_features(df)
    
    # OPTIONAL: slice dataset to first 550 rows, matching enriched dataset on GitHub.
    # Comment out this line to process full dataset.
    df = df.iloc[:550]

    df.to_csv('Data/FE_properties.csv', index=False)

    return df
