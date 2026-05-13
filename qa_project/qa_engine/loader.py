import pandas as pd
import requests
from io import StringIO
import os

def load_csv(source):
    """
    Loads CSV from either:
    - URL (http/https)
    - Local file path
    """

    # -----------------------
    # CASE 1: URL
    # -----------------------
    if source.startswith("http://") or source.startswith("https://"):
        response = requests.get(source)
        response.raise_for_status()
        return pd.read_csv(StringIO(response.text), dtype=str)

    # -----------------------
    # CASE 2: LOCAL FILE
    # -----------------------
    if os.path.exists(source):
        return pd.read_csv(source, dtype=str)

    raise ValueError(f"Invalid source: {source}")