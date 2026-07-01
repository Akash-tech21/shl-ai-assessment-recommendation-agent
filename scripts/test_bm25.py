import os
import sys

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

sys.path.insert(0, PROJECT_ROOT)

from app.retrieval.bm25 import BM25Retriever

retriever = BM25Retriever()

results = retriever.search("Java developer", top_k=5)

for r in results:
    print(r["name"])