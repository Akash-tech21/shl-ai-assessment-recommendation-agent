import os
import sys
import json

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)
sys.path.insert(0, PROJECT_ROOT)

from app.retrieval.embedder import SHLEmbedder

# Load cleaned catalog
with open("data/processed/catalog_clean.json", "r", encoding="utf-8") as f:
    catalog = json.load(f)

embedder = SHLEmbedder()

# Temporary list in memory
embeddings = []

for assessment in catalog:

    text = f"""
    Name: {assessment['name']}

    Description: {assessment['description']}

    Job Levels: {' '.join(assessment['job_levels'])}

    Skills: {' '.join(assessment['keys'])}
    """

    vector = embedder.embed(text)

    embeddings.append(vector)

print(f"Generated {len(embeddings)} embeddings")
print(f"Dimension: {embeddings[0].shape}")