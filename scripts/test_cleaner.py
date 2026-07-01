import os
import sys

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

sys.path.insert(0, PROJECT_ROOT)

from app.data_loader.loader import CatalogLoader
from app.data_loader.cleaner import CatalogCleaner

loader = CatalogLoader(
    "data/raw/shl_catalog.json"
)

catalog = loader.load_catalog()

cleaner = CatalogCleaner(catalog)

clean_catalog = cleaner.clean()

cleaner.save(
    clean_catalog,
    "data/processed/catalog_clean.json"
)

print(f"Saved {len(clean_catalog)} assessments.")

print()

print(clean_catalog[0])