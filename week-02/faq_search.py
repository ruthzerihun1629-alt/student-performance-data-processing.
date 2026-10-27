import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent / "data" / "university_faqs.csv"


def load_faqs():
    df = pd.read_csv(DATA_PATH)

    print("Dataset loaded successfully!")
    print("Shape:", df.shape)
    print(df.head())

    return df

def clean_faqs(df):
    cleaned = df.copy()

    # Remove FAQs with missing questions or answers
    cleaned = cleaned.dropna(subset=["question", "answer"])

    # Remove extra whitespace
    for column in ["question", "answer", "category"]:
        cleaned[column] = cleaned[column].fillna("Unknown")
        cleaned[column] = cleaned[column].astype(str).str.strip()
        cleaned[column] = cleaned[column].str.replace(
            r"\s+", " ", regex=True
        )

    # Remove empty questions and answers
    cleaned = cleaned[
        (cleaned["question"] != "") &
        (cleaned["answer"] != "")
    ]

    # Remove repeated questions, ignoring case
    cleaned = cleaned.drop_duplicates(
        subset=["question"], keep="first"
    )

    cleaned = cleaned.reset_index(drop=True)

    return cleaned


def chunk_faqs(df, max_words=100):
    chunks = []

    for _, row in df.iterrows():
        text = f"Question: {row['question']} Answer: {row['answer']}"
        words = text.split()

        for start in range(0, len(words), max_words):
            chunk = " ".join(words[start:start + max_words])

            chunks.append({
                "faq_id": str(row["id"]),
                "category": row["category"],
                "text": chunk
            })

    return chunks

if __name__ == "__main__":
    df = load_faqs()

    cleaned_df = clean_faqs(df)
    print("\nCleaned dataset shape:", cleaned_df.shape)

    chunks = chunk_faqs(cleaned_df)
    print("Total chunks:", len(chunks))

    print("\nFirst chunk:")
    print(chunks[0])

    load_faqs()