from .checks import (
    check_empty_values,
    check_duplicates,
    check_special_characters,
    check_url_format,
    check_url_leakage,
    check_categories,
    check_html_tags,
    check_fully_empty_columns
)

from .config import (
    FIXED_REQUIRED_COLUMNS,
    UNIQUE_COLUMNS,
    URL_COLUMNS
)

from .helpers import qa_results, qa_summary


def run_qa(df):

    print("=" * 80)
    print("QA ENGINE STARTED")
    print("=" * 80)

    check_empty_values(df, FIXED_REQUIRED_COLUMNS)
    check_duplicates(df, UNIQUE_COLUMNS)
    check_special_characters(df, exclude_columns=URL_COLUMNS)
    check_url_format(df, URL_COLUMNS)
    check_url_leakage(df, URL_COLUMNS)
    check_categories(df)
    check_html_tags(df)
    check_fully_empty_columns(df)

    print("QA COMPLETED")

    return qa_results, qa_summary