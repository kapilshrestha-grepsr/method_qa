from qa_engine import load_csv, run_qa
from qa_engine.reporter import save_issue_reports, save_summary_csv
from qa_engine.dtale_viewer import open_reports_in_dtale
import webbrowser
import time


# =========================================================
# CONFIG
# =========================================================
project_name = "zestdent"
source = "/home/kapil/Downloads/202605011459-zestdent_2026-05-01.csv"


# =========================================================
# LOAD DATA
# =========================================================
df = load_csv(source)


# =========================================================
# RUN QA ENGINE
# =========================================================
qa_results, qa_summary = run_qa(df)


# =========================================================
# SAVE REPORTS
# =========================================================
save_summary_csv(qa_summary, project_name)
save_issue_reports(qa_results, project_name)

print("\nReports generated in /reports folder")


# =========================================================
# OPEN DTALE (MULTI DATASET SAFE)
# =========================================================
sessions = open_reports_in_dtale("reports")


# =========================================================
# COLLECT URLs
# =========================================================
urls = []

print("\nD-Tale URLs:\n")

for name, session in sessions.items():
    try:
        url = session._main_url
        print(f"{name}: {url}")
        urls.append(url)
    except Exception as e:
        print(f"{name}: Failed -> {e}")


# =========================================================
# OPEN ALL TABS
# =========================================================
print("\nOpening all D-Tale tabs...\n")

for url in urls:
    webbrowser.open_new_tab(url)
    time.sleep(0.3)


# =========================================================
# KEEP ALIVE (IMPORTANT)
# =========================================================
print("\nKeeping server alive...")

while True:
    time.sleep(10)