from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_DIR = BASE_DIR / "input"

OUTPUT_DIR = BASE_DIR / "output"

REPORT_DIR = BASE_DIR / "reports"

DEVELOPMENT_FILE = INPUT_DIR / "dev_data.csv"

MODEL_FILE = INPUT_DIR / "LR_SCorecard.pkl"

VALIDATION_FILE = INPUT_DIR / "oot_data.csv"

OOT_FILE = INPUT_DIR / "oot_data.csv"

DEVELOPMENT_RESULTS_FILE = (
    INPUT_DIR /
    "development_results.xlsx"
)