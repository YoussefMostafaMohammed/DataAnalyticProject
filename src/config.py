from pathlib import Path

# Base project directory (two levels up from src/)
BASE_DIR = Path(__file__).resolve().parent.parent

# Data folders
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

# Raw CSV files
CUSTOMERS_CSV = RAW_DATA_DIR / "customers.csv"
PRODUCTS_CSV = RAW_DATA_DIR / "products.csv"
SALES_CSV = RAW_DATA_DIR / "sales_transactions.csv"

# Reports / figures folder
REPORTS_DIR = BASE_DIR / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"

# Visualization settings
SEABORN_STYLE = "whitegrid"
