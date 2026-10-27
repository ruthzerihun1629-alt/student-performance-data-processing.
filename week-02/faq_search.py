import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent / "data" / "university_faqs.csv"


def load_faqs():
    df = pd.read_csv(DATA_PATH)

    print("Dataset loaded successfully!")
    print("Shape:", df.shape)
    print(df.head())

    return df


if __name__ == "__main__":
    load_faqs()