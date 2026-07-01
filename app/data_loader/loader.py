import json
from pathlib import Path


class CatalogLoader:
    def __init__(self, file_path: str):
        self.file_path = Path(file_path)

    def load_catalog(self):
        """Load the SHL catalog safely."""

        with open(
            self.file_path,
            "r",
            encoding="utf-8",
            errors="replace"
        ) as file:
            content = file.read()

        try:
            data = json.loads(content, strict=False)
            return data

        except json.JSONDecodeError as e:
            print(f"JSON Error: {e}")
            return None