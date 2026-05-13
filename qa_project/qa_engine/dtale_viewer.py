import os
import pandas as pd
import dtale
import re


def clean_name(name: str) -> str:
    name = name.replace(".csv", "")
    name = re.sub(r"[^a-zA-Z0-9 ]", " ", name)
    name = re.sub(r"\s+", " ", name).strip()
    return name


def open_reports_in_dtale(reports_dir="reports"):
    sessions = {}

    for file in os.listdir(reports_dir):

        if not file.endswith(".csv"):
            continue

        path = os.path.join(reports_dir, file)
        df = pd.read_csv(path)

        name = clean_name(file)

        print(f"Starting D-Tale dataset: {name}")

        # 🚨 DO NOT force same port
        d = dtale.show(
            df,
            name=name
        )

        sessions[name] = d

    return sessions