from pathlib import Path

# Project Root
PROJECT_ROOT = Path(__file__).resolve().parent

# Directories root
DATA_DIR = PROJECT_ROOT / "data"
EXTERNAL_DIR = DATA_DIR / "external"
RAW_DIR = DATA_DIR / "raw"
DB_DIR = DATA_DIR / "db"
MODEL_DIR = PROJECT_ROOT / "models"
PREPROCESSED_DIR = DATA_DIR / "preprocessed"
# DOCS_DIR = PROJECT_ROOT / "docs"
# IMAGES_DIR = DOCS_DIR / "images"
# HTML_DIR = RAW_DIR / "html"
# CSV_DIR = RAW_DIR / "csv"
# PDF_DIR = RAW_DIR / "pdf"
# TXT_DIR = RAW_DIR / "txt"
