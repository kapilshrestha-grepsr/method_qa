from .helpers import add_issue, norm, safe_col, get_category_columns
from .config import SPECIAL_CHAR_PATTERN, URL_PATTERN


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
    for col in df.columns:
        if col in url_columns:
            continue

        mask = df[col].astype(str).str.contains(URL_PATTERN, na=False)
        add_issue(f"url_leak_{col}", df[mask])


def check_categories(df):
    cat_cols = get_category_columns(df)

    for col in cat_cols:
        mask = df[col].astype(str).str.contains(URL_PATTERN, na=False)

        if mask.any():
            add_issue(f"category_url_leak_{col}", df[mask])