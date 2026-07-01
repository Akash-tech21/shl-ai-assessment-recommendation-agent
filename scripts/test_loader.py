import os
import sys

# Add project root to sys.path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

from app.data_loader.loader import CatalogLoader

loader = CatalogLoader("data/raw/shl_catalog.json")

catalog = loader.load_catalog()

if catalog:
    print(f"Loaded {len(catalog)} assessments")
    print(catalog[0])