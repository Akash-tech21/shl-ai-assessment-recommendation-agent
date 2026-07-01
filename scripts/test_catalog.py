import json

with open("data/raw/shl_catalog.json", "r", encoding="utf-8") as f:
    catalog = json.load(f)

print(f"Total assessments: {len(catalog)}")
print("First assessment:", catalog[0]["name"])