# Week 01 — Student Performance Data Processing

## Project Overview

This project analyzes student examination results using Python, Pandas, and NumPy. It demonstrates how to load a raw CSV dataset, clean the data using functions, and perform statistical analysis.

The dataset contains 1,000 student records, including mathematics, reading, and writing examination scores.

## Objectives

- Load student performance data from a CSV file.
- Clean and prepare the dataset using Python functions.
- Handle missing values, duplicate records, inconsistent text, and invalid scores.
- Perform statistical calculations using NumPy.
- Calculate individual student averages and classify performance.
- Run the analysis in both a Python script and a Jupyter notebook.

## Data Cleaning

The `clean_data()` function performs the following operations:

1. Standardizes column names.
2. Removes extra whitespace from text values.
3. Removes duplicate records.
4. Converts examination scores to numeric values.
5. Identifies invalid scores outside the 0–100 range.
6. Removes rows with missing or invalid scores.
7. Fills missing categorical values with `Unknown`.

The original dataset contains no missing values or duplicate records, so the cleaned dataset retains all 1,000 rows.

## NumPy Analysis

The project uses NumPy to calculate:

- Mean
- Median
- Standard deviation
- 25th and 75th percentiles
- Individual student averages
- Pass/fail classifications using `np.where()`

For demonstration, a student average of 50 or above is classified as `Pass`. This is an illustrative threshold, not an official academic grading policy.

## Results

| Subject | Mean | Median | Standard Deviation |
|---|---:|---:|---:|
| Mathematics | 66.09 | 66 | 15.16 |
| Reading | 69.17 | 70 | 14.59 |
| Writing | 68.05 | 69 | 15.19 |

**Overall class average:** 67.77

Reading has the highest average score, while mathematics has the lowest.

## Project Files

- `student_performance.py` — Standalone Python data-processing application.
- `student_performance.ipynb` — Interactive notebook with explanations and saved outputs.
- `data/StudentsPerformance.csv` — Raw student examination dataset.

## How to Run

From the repository root, install the dependencies:

```bash
python -m pip install -r requirements.txt
```

Then run:

```bash
python week-01/student_performance.py
```

To use the notebook, open `student_performance.ipynb` in VS Code or Jupyter and run the cells in order.

## Conclusion

This project demonstrates the essential stages of a data-processing workflow: data loading, cleaning, validation, and statistical analysis. It also highlights how NumPy can be used to understand patterns in student examination performance.