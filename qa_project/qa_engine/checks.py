from .helpers import add_issue, norm, safe_col, get_category_columns
from .config import (
    SPECIAL_CHAR_PATTERN,
    URL_PATTERN,
    HTML_PATTERN
)
def check_empty_values(df, columns):
    for col in columns:
        if not safe_col(df, col):
            continue

        mask = df[col].isna() | norm(df[col]).eq("")
        add_issue(f"empty_{col}", df[mask])


def check_duplicates(df, columns):
    for col in columns:
        if not safe_col(df, col):
            continue

        mask = norm(df[col]).duplicated(keep=False)
        add_issue(f"duplicate_{col}", df[mask])


def check_special_characters(df, exclude_columns):
    for col in df.columns:
        if col in exclude_columns:
            continue

        mask = df[col].astype(str).str.contains(
            SPECIAL_CHAR_PATTERN,
            regex=True,
            na=False
        )

        add_issue(f"special_chars_{col}", df[mask])


def check_url_format(df, url_columns):
    for col in url_columns:
        if not safe_col(df, col):
            continue

        mask = ~norm(df[col]).str.match(r"^https?://", na=False)
        mask &= norm(df[col]).ne("")

        add_issue(f"invalid_url_{col}", df[mask])


def check_url_leakage(df, url_columns):

    # normalize URL column names for comparison
    normalized_url_cols = {
        c.lower().replace(" ", "")
        for c in url_columns
    }

    for col in df.columns:

        normalized_col = col.lower().replace(" ", "")

        # skip ALL url-like columns
        if normalized_col in normalized_url_cols:
            continue

        values = df[col].fillna("").astype(str)

        mask = values.str.contains(URL_PATTERN, na=False)

        if mask.any():
            add_issue(f"url_leak_{col}", df[mask])


def check_categories(df):
    cat_cols = get_category_columns(df)

    for col in cat_cols:
        mask = df[col].astype(str).str.contains(URL_PATTERN, na=False)

        if mask.any():
            add_issue(f"category_url_leak_{col}", df[mask])



# =========================================================
# HTML TAG CHECK
# =========================================================

def check_html_tags(df, exclude_columns=None):

    if exclude_columns is None:
        exclude_columns = []

    normalized_excluded = {
        c.lower().replace(" ", "")
        for c in exclude_columns
    }

    for col in df.columns:

        normalized_col = col.lower().replace(" ", "")

        # skip excluded columns if needed
        if normalized_col in normalized_excluded:
            continue

        values = df[col].fillna("").astype(str)

        mask = values.str.contains(
            HTML_PATTERN,
            regex=True,
            na=False
        )

        if mask.any():
            add_issue(f"html_tags_{col}", df[mask])



# =========================================================
# FULLY EMPTY COLUMNS CHECK
# =========================================================
def check_fully_empty_columns(df):
    """
    Detect columns where ALL rows are empty/null
    """

    from .helpers import qa_summary

    null_columns = []

    for col in df.columns:

        values = norm(df[col])

        # entire column empty
        if values.eq("").all():
            null_columns.append(col)

    # print nicely
    if null_columns:

        print("\nNULL COLUMNS:")
        print(", ".join(null_columns))

        # add to summary
        qa_summary.append({
            "issue": "fully_empty_columns",
            "rows": len(null_columns),
            "columns": ", ".join(null_columns)
        })

    else:
        print("\nNo fully empty columns found.")