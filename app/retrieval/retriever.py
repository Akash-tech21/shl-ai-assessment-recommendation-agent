import faiss
import pickle
import numpy as np

from app.retrieval.embedder import SHLEmbedder


class SHLRetriever:

    def __init__(self):

        self.embedder = SHLEmbedder()

        self.index = faiss.read_index(
            "data/vectorstore/shl_index.faiss"
        )

        with open(
            "data/vectorstore/metadata.pkl",
            "rb"
        ) as f:

            self.metadata = pickle.load(f)

    def search(self, query, top_k=5):

        query_vector = self.embedder.embed(query)

        query_vector = np.array(
            [query_vector],
            dtype="float32"
        )

        distances, indices = self.index.search(
            query_vector,
            top_k
        )

        results = []

        for idx in indices[0]:

            results.append(
                self.metadata[idx]
            )

        return results