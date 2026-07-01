import requests
from pathlib import Path

URL = "https://tcp-us-prod-rnd.shl.com/voiceRater/shl-ai-hiring/shl_product_catalog.json"

response = requests.get(URL)

print("Status Code:", response.status_code)
print("Content-Type:", response.headers.get("Content-Type"))
print("First 500 characters:\n")
print(response.text[:500])