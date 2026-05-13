import pandas as pd

qa_results = {}
qa_summary = []


# =========================================================
# RESET QA STATE
# =========================================================
def reset_qa_state():
    """
    Clears previous QA run state
    """
    global qa_results, qa_summary

    qa_results = {}
    qa_summary = []


# =========================================================
# STORE ISSUE DATAFRAME
# =========================================================
def add_issue(name, df):

    global qa_results

    qa_results[name] = df.copy()

    add_summary(name, df.shape[0])


# =========================================================
# STORE SUMMARY
# =========================================================
def add_summary(issue_name, row_count, extra_data=None):

    global qa_summary

    row = {
        "issue": issue_name,
        "rows": row_count
    }

    if extra_data:
        row.update(extra_data)

    qa_summary.append(row)


# =========================================================
# GETTERS
# =========================================================
def get_results():
    return qa_results


def get_summary():
    return qa_summary


# =========================================================
# HELPERS
# =========================================================
def norm(series):
    """
    Safe normalization
    """
    return series.fillna("").astype(str).str.strip()


def safe_col(df, col):
    return col in df.columns


def get_category_columns(df):
    return [c for c in df.columns if c.startswith("Category #")]