from app.retrieval.retriever import SHLRetriever
from app.retrieval.bm25 import BM25Retriever
from app.retrieval.filter import MetadataFilter


class HybridRetriever:

    def __init__(self):
        self.filter = MetadataFilter()
        self.faiss = SHLRetriever()
        self.bm25 = BM25Retriever()
       

    def search(self, query, context=None, top_k=10):
        # FAISS search
        faiss_results = self.faiss.search(query, top_k=top_k)

        # BM25 search
        bm25_results = self.bm25.search(query, top_k=top_k)

        # Merge by entity_id
        merged = {}

        for item in faiss_results + bm25_results:
            merged[item["entity_id"]] = item

        results = list(merged.values())

        # Apply metadata filtering if context is provided
        if context is not None:
            results = self.filter.filter(results, context)

        return results[:top_k]