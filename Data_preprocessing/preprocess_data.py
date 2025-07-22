from datetime import datetime


def add_renovation_features(df):
    df["was_renovated"] = df["yr_renovated"] > 0
    df["years_since_renovation"] = (
        datetime.now().year - df["yr_renovated"]
    ).where(df["was_renovated"], 0)
    return df

