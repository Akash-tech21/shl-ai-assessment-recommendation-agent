import os
import sys
import json

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

sys.path.insert(0, PROJECT_ROOT)

from app.retrieval.embedder import SHLEmbedder
from app.retrieval.vector_store import SHLVectorStore

with open(
    "data/processed/catalog_clean.json",
    encoding="utf-8"
) as f:

    catalog = json.load(f)

embedder = SHLEmbedder()

embeddings = []

metadata = []

for assessment in catalog:

    text = f"""
    Name: {assessment['name']}

    Description:
    {assessment['description']}

    Job Levels:
    {' '.join(assessment['job_levels'])}

    Skills:
    {' '.join(assessment['keys'])}
    """

    vector = embedder.embed(text)

    embeddings.append(vector)

    metadata.append(assessment)

dimension = embeddings[0].shape[0]

store = SHLVectorStore(dimension)

store.add(embeddings, metadata)

store.save("data/vectorstore")

print("Vector Store Created Successfully")