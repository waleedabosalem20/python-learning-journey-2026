# Python Data Experiments

A collection of small Python scripts I wrote while learning programming basics and data cleaning techniques — the foundation for data engineering.

## About This Repo

These are my early exercises and experiments as I teach myself Python with a focus on handling real-world messy data (something data engineers deal with every day).

Started in February 2026 as part of self-study before university.  
Goal: Build practical skills step-by-step (string parsing → list processing → eventually pandas, ETL, APIs, pipelines).

## What's Inside

### string-parsing
Extracting structured data (name, role, age) from inconsistent, messy strings with extra spaces, typos, symbols, and varying formats.

- Learned: `.find()`, `.strip()`, `.lower()`, `.replace()`, dynamic slicing instead of hard-coded positions

### list-processing
Finding missing values (`None`) in lists and reporting their 0-based position.

- Learned: for loops, conditionals, manual indexing, `for ... else` pattern, `is None` checks

## Why I'm Doing This

I want to become a data engineer, so I'm starting with the fundamentals:  
- Cleaning dirty data  
- Writing reusable logic  
- Understanding how to make code work on unpredictable inputs

Future plans:  
- Add pandas data cleaning scripts  
- Simple ETL (API → clean → save to file/DB)  
- Basic Spark/PySpark exercises  
- Mini data pipelines

## Tech Used So Far
- Python 3 (core language only — no external libraries yet)

## How to Run
Just open any .py file and run it:
```bash
python string-parsing/exercise_1.py
