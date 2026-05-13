import pandas as pd

qa_results = {}
qa_summary = []


def add_issue(name, df):
    qa_results[name] = df.copy()
    qa_summary.append({"issue": name, "rows": df.shape[0]})


def norm(series):
    return series.astype(str).fillna("").str.strip()


def safe_col(df, col):
    return col in df.columns


def get_category_columns(df):
    return [c for c in df.columns if c.startswith("Category #")]