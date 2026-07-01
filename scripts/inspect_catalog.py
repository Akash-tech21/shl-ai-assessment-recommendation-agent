import json

with open("data/raw/shl_catalog.json", "r", encoding="utf-8") as file:
    data = json.load(file)

print("Type:", type(data))

if isinstance(data, list):
    print("Total Assessments:", len(data))
    print("\nFirst Assessment:\n")
    print(data[0])

elif isinstance(data, dict):
    print("Keys:")
    print(data.keys())