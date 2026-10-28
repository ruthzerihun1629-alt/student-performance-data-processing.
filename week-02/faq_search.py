import pandas as pd 
from pathlib import Path
import chromadb

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
def store_embeddings(chunks):
    client = chromadb.PersistentClient(path="week-02/chroma_db")

    collection = client.get_or_create_collection(
        name="university_faqs"
    )

    collection.upsert(
        ids=[f"chunk_{i}" for i in range(len(chunks))],
        documents=[chunk["text"] for chunk in chunks],
        metadatas=[
            {
                "faq_id": chunk["faq_id"],
                "category": chunk["category"]
            }
            for chunk in chunks
        ]
    )

    print("Embeddings stored successfully!")
    print("Total stored chunks:", collection.count())

    return collection

def search_faqs(collection, query, top_k=3):
    results = collection.query(
        query_texts=[query],
        n_results=top_k
    )

    print(f"\nSearch query: {query}")
    print(f"\nTop {top_k} matches:\n")

    for i, (document, distance, metadata) in enumerate(
        zip(
            results["documents"][0],
            results["distances"][0],
            results["metadatas"][0]
        ),
        start=1
    ):
        print(f"Match {i}")
        print(f"Category: {metadata['category']}")
        print(f"FAQ ID: {metadata['faq_id']}")
        print(f"Text: {document}")
        print(f"Distance: {distance:.4f}")
        print("-" * 50)



if __name__ == "__main__":
    df = load_faqs()

    cleaned_df = clean_faqs(df)
    print("\nCleaned dataset shape:", cleaned_df.shape)

    chunks = chunk_faqs(cleaned_df)
    print("Total chunks:", len(chunks))

    collection = store_embeddings(chunks)

    search_faqs(
        collection,
        "I forgot my university account password",
        top_k=3
    )