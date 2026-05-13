from qa_engine import load_csv, run_qa
from qa_engine.reporter import save_issue_reports, save_summary_csv
from qa_engine.dtale_viewer import open_reports_in_dtale
import webbrowser
import time
import dtale
import os
import glob


# =========================================================
# CONFIG
# =========================================================
project_name = "biohorizons"
source = "/home/kapil/Downloads/202605010805-biohorizons_com_2026-05-01.csv"

# =========================================================
# LOAD FULL DATASET
# =========================================================
df = load_csv(source)


# =========================================================
# RUN QA
# =========================================================
qa_results, qa_summary = run_qa(df)


# =========================================================
# CLEAN OLD REPORTS
# =========================================================
reports_dir = "reports"

os.makedirs(reports_dir, exist_ok=True)

csv_files = glob.glob(os.path.join(reports_dir, "*.csv"))

if csv_files:

    print("\nRemoving old report CSVs...\n")

    for file in csv_files:

        print(f"Deleting: {os.path.basename(file)}")
        os.remove(file)

    print("\nOld reports cleanup completed.")

else:
    print("\nNo old report CSVs found.")


# =========================================================
# SAVE REPORTS
# =========================================================
save_summary_csv(qa_summary, project_name)
save_issue_reports(qa_results, project_name)

print("\nReports generated in /reports folder")


# =========================================================
# OPEN FULL DATA FIRST (ALWAYS GUARANTEED)
# =========================================================
print("\nOpening FULL DATA in D-Tale...\n")

full_session = dtale.show(df, name="full data")

full_url = full_session._main_url

print(f"full data: {full_url}")


# =========================================================
# OPEN QA REPORTS
# =========================================================
sessions = open_reports_in_dtale("reports")


# =========================================================
# COLLECT QA URLS
# =========================================================
urls = [full_url]

print("\nQA D-Tale URLs:\n")

for name, session in sessions.items():
    try:
        url = session._main_url
        print(f"{name}: {url}")
        urls.append(url)
    except Exception as e:
        print(f"{name}: Failed -> {e}")


# =========================================================
# OPEN ALL TABS (FULL DATA ALWAYS INCLUDED)
# =========================================================
print("\nOpening all D-Tale tabs...\n")

for url in urls:
    webbrowser.open_new_tab(url)
    time.sleep(0.3)


# =========================================================
# KEEP ALIVE
# =========================================================
print("\nKeeping server alive...")

while True:
    time.sleep(10)