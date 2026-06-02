# AIML Python Scripts & Notebooks

This repository contains a collection of Python scripts and Jupyter Notebooks demonstrating various fundamental concepts in Python programming, NumPy, and Pandas.

## Contents

### 1. Core Python (`python/`)
- **`python/Exception_Handling.py`**: Examples of handling exceptions in Python (e.g., `ZeroDivisionError`, `TypeError`, `ValueError`).
- **`python/Word_Search.py`**: A simple script to read from a text file and search for a specific word ("Python").
- **`python/code.py`**: Demonstrates reading from and writing to a file (`sample.txt`).
- **`python/calculator.py`**: A simple calculator module with basic arithmetic operations (addition, subtraction, multiplication, division).
- **`python/list_operations.py`**: Demonstrates various operations on Python lists, including append, insert, remove, pop, and list comprehensions.

### 2. NumPy Tutorials (`numPy/`)
- **`numPy/numpy1.ipynb`**: Introduction to NumPy arrays, core structures, and memory comparison.
- **`numPy/numpy2.ipynb`**: Array attributes, creation methods, and performance comparison.
- **`numPy/numpy3.ipynb`**: Array basics, vectorization, and vector normalization examples.
- **`numPy/numpy4.ipynb`**: Useful mathematical and statistical functions (Sum, Product, Min, Max, Mean, Median, Std Dev, Exponentials, Logarithms, Rounding, and Clipping).
- **`numPy/numpy5_broadcasting.ipynb`**: NumPy Broadcasting and Vectorized Operations. Explains dimension compatibility, how scalar-array operations work, and how broadcasting applies to 2D/3D arrays.

### 3. Pandas Tutorials (`pandas/`)
- **`pandas/panda1.ipynb`**: Introduction to Pandas Series, dictionaries, custom indexing, and basic DataFrame setup.
- **`pandas/Creating DataFrame.ipynb`**: Comprehensive guide on constructing DataFrames from dictionaries of lists, lists of dictionaries, nested lists, and NumPy arrays.
- **`pandas/Selecting and Filtering.ipynb`**: Detailed examples on selecting columns, label-based indexing (`.loc`), position-based indexing (`.iloc`), and boolean filtering.
- **`pandas/Data Cleaning.ipynb`**: Data Cleaning in Pandas. Explains checking for null values with `.isna()`, dropping missing rows/columns with `.dropna()`, filling missing values with `.fillna()`, and general value replacement with `.replace()`.
- **`pandas/Grouping and Aggregation.ipynb`**: Grouping and Aggregating Data in Pandas. Covers `.groupby()`, descriptive statistics per group (mean, sum, count), and the multi-functional `.agg()` method.
- **`pandas/Merging and Joining.ipynb`**: Data Merging and Joining in Pandas. Detailed examples of merging on keys (`pd.merge`), concatenating along axes (`pd.concat`), and index-based joins (`.join`).
- **`pandas/csv.ipynb`**: Reading and exploring external datasets. Covers loading data from CSV files (`pd.read_csv()`), structured JSON files (`pd.read_json()`), and analyzing the Tips dataset using basic DataFrame inspection methods (`.head()`, `.tail()`, `.info()`, `.describe()`, `.columns`, and `.shape`).
- **`pandas/Filtering.ipynb`**: Demonstrates various indexing, column selection, row retrieval using `.loc`, and complex conditional/boolean filtering techniques.

### 4. Data Visualization (`data_visualization/`)
- **`data_visualization/matplotlib_basics.ipynb`**: Matplotlib Basics. Introducing basic plotting: Line plots, Bar charts, Scatter plots, and plot customizations (labels, titles, legends, grids, and colors).

## Getting Started

1. Clone the repository.
2. Ensure you have the necessary dependencies installed (Jupyter, NumPy, Pandas):
   ```bash
   pip install jupyter numpy pandas
   ```
3. Launch Jupyter Notebook or JupyterLab to view and run the notebooks:
   ```bash
   jupyter lab
   ```
