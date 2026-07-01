import json
import time
import requests

from metrics import Metrics


with open(
    "evaluation/sample_queries.json",
    "r",
    encoding="utf-8"
) as f:

    queries = json.load(f)

recalls = []

times = []

for sample in queries:

    start = time.time()

    response = requests.post(

        "http://127.0.0.1:8000/chat",

        json={
            "messages": [
                {
                    "role": "user",
                    "content": sample["query"]
                }
            ]
        }
    )

    elapsed = time.time() - start

    body = response.json()

    recommendations = [

        item["name"]

        for item in body["recommendations"]

    ]

    recall = Metrics.recall_at_k(

        recommendations,

        sample["expected"]

    )

    recalls.append(recall)

    times.append(elapsed)

    print("=" * 60)

    print(sample["query"])

    print("Recall:", recall)

    print("Time:", round(elapsed, 2), "seconds")

print("=" * 60)

print("Average Recall:", sum(recalls) / len(recalls))

print("Average Response Time:", round(sum(times) / len(times), 2))