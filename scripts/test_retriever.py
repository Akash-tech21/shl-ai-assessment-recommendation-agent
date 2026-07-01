import os
import sys

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

sys.path.insert(0, PROJECT_ROOT)

from app.retrieval.retriever import SHLRetriever

retriever = SHLRetriever()

results = retriever.search(

    "Hiring a Java developer with stakeholder communication skills",

    top_k=5

)

for i, assessment in enumerate(results, start=1):

    print("=" * 60)

    print(f"Rank {i}")

    print("Name:", assessment["name"])

    print("URL:", assessment["url"])

    print()