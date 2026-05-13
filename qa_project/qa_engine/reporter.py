import os
import pandas as pd


def _safe_name(text: str) -> str:
    """
    Converts issue name into filesystem-safe filename
    """
    return (
        text.replace(" ", "_")
            .replace("#", "")
            .replace("__", "_")
    )


# =========================================================
# SAVE ISSUE-WISE CSV FILES
# =========================================================

def save_issue_reports(qa_results: dict, project_name: str, output_dir: str = "reports"):
    """
    Saves each QA issue dataframe into separate CSV files.

    Example:
        reports/zestdent_empty_SKU.csv
        reports/zestdent_duplicate_SKU.csv
    """

    os.makedirs(output_dir, exist_ok=True)

    for issue_name, df in qa_results.items():

        if df is None or df.empty:
            continue

        file_name = f"{project_name}_{_safe_name(issue_name)}.csv"
        file_path = os.path.join(output_dir, file_name)

        df.to_csv(file_path, index=False)


# =========================================================
# SAVE SUMMARY CSV
# =========================================================

def save_summary_csv(qa_summary: list, project_name: str, output_dir: str = "reports"):
    """
    Converts QA summary list into a CSV report.
    """

    os.makedirs(output_dir, exist_ok=True)

    df = pd.DataFrame(qa_summary)

    file_path = os.path.join(output_dir, f"{project_name}_qa_summary.csv")

    df.to_csv(file_path, index=False)

    return file_path