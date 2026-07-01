import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

from app.data_loader.loader import CatalogLoader
from app.data_loader.validator import CatalogValidator

loader = CatalogLoader("data/raw/shl_catalog.json")

catalog = loader.load_catalog()

validator = CatalogValidator(catalog)

report = validator.validate()

print("\nValidation Report\n")

for key, value in report.items():
    print(f"{key}: {value}")