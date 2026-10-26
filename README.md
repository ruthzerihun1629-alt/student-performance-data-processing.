# AWS SBG — Python & AI/ML Weekly Tasks

This repository contains my weekly Python and AI/ML learning tasks. Each task focuses on applying programming concepts through practical projects involving data processing, analysis, and problem-solving.

## Repository Structure

```text
student-performance-data-processing/
├── README.md
├── requirements.txt
├── .gitignore
└── week-01/
    ├── README.md
    ├── student_performance.py
    ├── student_performance.ipynb
    └── data/
        └── StudentsPerformance.csv
```

## Technologies Used

- Python
- Pandas
- NumPy
- Jupyter Notebook
- Google Colab
- Git and GitHub

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/ruthzerihun1629-alt/student-performance-data-processing.git
cd student-performance-data-processing
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**Windows (PowerShell):**

```powershell
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the Python script

```bash
python week-01/student_performance.py
```

### 5. Run the notebook

Open `week-01/student_performance.ipynb` in VS Code or Jupyter Notebook and run all cells.

The notebook reads the CSV dataset from the `week-01/data/` folder. When using Google Colab, upload the dataset into the appropriate folder before running the notebook.

## Weekly Tasks

| Week | Project | Description |
|---|---|---|
| 01 | Student Performance Data Processing | Clean and analyze student examination scores using Pandas and NumPy |

## Environment and Version Control

The `.venv/` directory contains local dependencies and is excluded from Git using `.gitignore`. Python cache files and notebook checkpoints are also ignored.

Dependencies are listed in `requirements.txt` to make the project reproducible.

## Author

Ruth Zerihun

[GitHub](https://github.com/ruthzerihun1629-alt)