import pandas as pd
import numpy as np
from pathlib import Path

def load_data():
    file_path = Path(__file__).resolve().parent / "data" / "StudentsPerformance.csv"
    return pd.read_csv(file_path)

def clean_data(data):
    cleaned = data.copy()

    cleaned.columns = (
        cleaned.columns.str.strip()
        .str.lower()
        .str.replace(r"\s+", "_", regex=True)
        .str.replace("/", "_", regex=False)
    )

    for column in cleaned.select_dtypes(include=["object"]).columns:
        cleaned[column] = cleaned[column].str.strip()

    cleaned = cleaned.drop_duplicates()

    score_columns = ["math_score", "reading_score", "writing_score"]

    for column in score_columns:
        cleaned[column] = pd.to_numeric(cleaned[column], errors="coerce")

        
        cleaned.loc[
            ~cleaned[column].between(0, 100), column
        ] = np.nan

    
    cleaned = cleaned.dropna(subset=score_columns)

    
    for column in cleaned.select_dtypes(include=["object"]).columns:
        cleaned[column] = cleaned[column].fillna("Unknown")

    return cleaned.reset_index(drop=True)



def calculate_statistics(data):
    subjects = ["math_score", "reading_score", "writing_score"]

    for subject in subjects:
        scores = data[subject].to_numpy()

        print(f"\n{subject.replace('_', ' ').title()}")
        print("Mean:", round(np.mean(scores), 2))
        print("Median:", round(np.median(scores), 2))
        print("Standard deviation:", round(np.std(scores), 2))
        print("25th percentile:", round(np.percentile(scores, 25), 2))
        print("75th percentile:", round(np.percentile(scores, 75), 2))


def calculate_averages(data):
    scores = data[
        ["math_score", "reading_score", "writing_score"]
    ].to_numpy()

    result = data.copy()
    result["average_score"] = np.mean(scores, axis=1)

    result["performance"] = np.where(
        result["average_score"] >= 50,
        "Pass",
        "Fail"
    )

    return result


def main():
    df = load_data()
    print("Original dataset shape:", df.shape)

    cleaned_df = clean_data(df)
    print("Cleaned dataset shape:", cleaned_df.shape)

    calculate_statistics(cleaned_df)

    result = calculate_averages(cleaned_df)

    print("\nFirst 10 student results:")
    print(result[["average_score", "performance"]].head(10))

    print("\nOverall class average:",
          round(np.mean(result["average_score"]), 2))


if __name__ == "__main__":
    main()