from collections import Counter


class CatalogValidator:
    def __init__(self, catalog):
        self.catalog = catalog

    def validate(self):
        report = {
            "total_records": len(self.catalog),
            "missing_name": 0,
            "missing_description": 0,
            "missing_link": 0,
            "duplicate_links": 0,
            "duplicate_names": 0,
        }

        names = []
        links = []

        for item in self.catalog:

            if not item.get("name"):
                report["missing_name"] += 1

            if not item.get("description"):
                report["missing_description"] += 1

            if not item.get("link"):
                report["missing_link"] += 1

            names.append(item.get("name"))
            links.append(item.get("link"))

        report["duplicate_names"] = sum(
            count - 1 for count in Counter(names).values() if count > 1
        )

        report["duplicate_links"] = sum(
            count - 1 for count in Counter(links).values() if count > 1
        )

        return report