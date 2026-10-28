# University FAQ Semantic Search System

## Project Overview

This project is a Python-based semantic search system that retrieves relevant answers from a university FAQ dataset.

Unlike traditional keyword search, semantic search uses text embeddings to identify questions with similar meanings, even when they use different words.

The project was developed as part of the AWS SBG AI/ML Week 02 assignment.

## Objectives

- Load a CSV dataset using Pandas.
- Clean and preprocess FAQ data.
- Split FAQ text into manageable chunks.
- Generate text embeddings and store them in ChromaDB.
- Perform semantic similarity searches.
- Retrieve and display the top 3 most relevant FAQ matches.

## Technologies Used

- **Python** — Main programming language
- **Pandas** — Data loading and cleaning
- **ChromaDB** — Vector database and semantic similarity search
- **ChromaDB default embedding model** — Text-to-vector conversion
- **Jupyter Notebook** — Interactive implementation and testing

## Project Structure

```text
week-02/
├── data/
│   └── university_faqs.csv
├── faq_search.py
├── faq_search.ipynb
└── README.md
```

The root of the repository contains `requirements.txt` and `.gitignore`.

## Dataset

The project uses a sample university FAQ dataset containing 15 question-and-answer pairs.

The dataset includes four columns:

| Column | Description |
|---|---|
| id | Unique FAQ identifier |
| question | Frequently asked question |
| answer | Corresponding answer |
| category | FAQ category |

The FAQs cover registration, academics, technology, library services, housing, and student services.

The dataset contains illustrative answers and does not represent official university policies.

## How the System Works

1. **Data Loading:** Reads the CSV dataset using Pandas.
2. **Data Cleaning:** Removes missing values, empty questions, extra whitespace, and duplicate records.
3. **Text Chunking:** Combines questions and answers and splits long text into smaller chunks.
4. **Embedding Generation:** Converts text chunks into numerical vectors using ChromaDB's default embedding function.
5. **Vector Storage:** Stores embeddings, documents, and metadata in a persistent ChromaDB collection.
6. **Semantic Search:** Converts the user's query into an embedding and retrieves the three closest matches.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/ruthzerihun1629-alt/student-performance-data-processing.git
cd student-performance-data-processing
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

The required libraries include Pandas, ChromaDB, and Jupyter.

### 4. Run the Python script

From the repository root:

```bash
python week-02/faq_search.py
```

On the first run, ChromaDB may download its default embedding model. An internet connection is required for that download.

### 5. Run the Jupyter notebook

Start Jupyter:

```bash
jupyter notebook
```

Open `week-02/faq_search.ipynb` and run the cells in order.

Ensure that the dataset path points to `week-02/data/university_faqs.csv` when the working directory is the repository root.

## Example Queries

The following queries can be used to test the system:

```python
search_faqs(
    collection,
    "I forgot my university account password",
    top_k=3
)
```

```python
search_faqs(
    collection,
    "Where can I check my examination grades?",
    top_k=3
)
```

```python
search_faqs(
    collection,
    "How do I borrow books?",
    top_k=3
)
```

## Expected Results

For the query:

**"I forgot my university account password"**

The system should retrieve the FAQ about resetting a student portal password among the most relevant matches.

Each result displays:

- Match ranking
- FAQ category
- FAQ identifier
- Matching text
- Vector distance

Smaller vector distances indicate closer matches under the collection's configured distance metric.

The exact ranking and distances depend on the embedding model and query.

## Conclusion

This project demonstrates a basic semantic search pipeline using Pandas, text preprocessing, embeddings, and ChromaDB.

It provides practical experience with vector databases and semantic information retrieval, which are important foundations for modern AI applications such as retrieval-augmented generation (RAG).