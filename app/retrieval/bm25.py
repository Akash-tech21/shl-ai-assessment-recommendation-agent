import json
from rank_bm25 import BM25Okapi


class BM25Retriever:

    def __init__(self):

        with open(
            "data/processed/catalog_clean.json",
            "r",
            encoding="utf-8"
        ) as f:
            self.catalog = json.load(f)

        corpus = []

        for item in self.catalog:

            text = f"""
            {item['name']}
            {item['description']}
            {' '.join(item['keys'])}
            {' '.join(item['job_levels'])}
            """

            corpus.append(text.lower().split())

        self.bm25 = BM25Okapi(corpus)

    def search(self, query, top_k=5):

        tokens = query.lower().split()

        scores = self.bm25.get_scores(tokens)

        ranked = sorted(
            zip(scores, self.catalog),
            reverse=True,
            key=lambda x: x[0]
        )

        return [item for _, item in ranked[:top_k]]