# Method QA

CSV quality-check utility for product/catalog datasets, with issue reports saved as CSV and visualized in D-Tale.

## What This Project Does

- Loads a CSV from local path or URL.
- Runs QA checks for:
  - Empty required values
  - Duplicates in key columns
  - Special characters
  - Invalid URL format in URL fields
  - URL leakage in non-URL fields
  - URL leakage in category fields
  - HTML tags in text fields
  - Fully empty columns
- Saves:
  - One CSV per issue in `reports/`
  - Summary CSV in `reports/`
- Starts D-Tale sessions for:
  - Full source data
  - Each generated report CSV
- Opens all D-Tale URLs in browser tabs.

## Project Structure

- `qa_project/main.py`: entry script (load -> QA -> cleanup old reports -> save reports -> open D-Tale -> keep alive)
- `qa_project/qa_engine/engine.py`: orchestrates all QA checks
- `qa_project/qa_engine/checks.py`: all validation/check functions
- `qa_project/qa_engine/config.py`: regex patterns and key column config
- `qa_project/qa_engine/loader.py`: CSV loading from URL or local file
- `qa_project/qa_engine/reporter.py`: report CSV writers
- `qa_project/qa_engine/dtale_viewer.py`: opens report CSVs in D-Tale
- `reports/`: generated outputs

## Requirements

Create `requirements.txt` with:

```txt
pandas
requests
dtale