import json
from pathlib import Path


class CatalogCleaner:

    def __init__(self, catalog):
        self.catalog = catalog

    def clean(self):

        cleaned_catalog = []

        for item in self.catalog:

            cleaned = {

                "entity_id": item.get("entity_id", "").strip(),

                "name": item.get("name", "").strip(),

                "url": item.get("link", "").strip(),

                "description": item.get("description", "").strip(),

                "duration": item.get("duration", "").strip(),

                "job_levels": item.get("job_levels", []),

                "languages": item.get("languages", []),

                "remote": item.get("remote", "").lower() == "yes",

                "adaptive": item.get("adaptive", "").lower() == "yes",

                "keys": item.get("keys", [])

            }

            cleaned_catalog.append(cleaned)

        return cleaned_catalog

    def save(self, cleaned_catalog, output_path):

        output_path = Path(output_path)

        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, "w", encoding="utf-8") as file:

            json.dump(
                cleaned_catalog,
                file,
                indent=4,
                ensure_ascii=False
            )