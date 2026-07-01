from app.retrieval.hybrid_retriever import HybridRetriever


class RecommendationEngine:

    def __init__(self):
        self.retriever = HybridRetriever()

    def recommend(self, context):

        query = f"""
        Role: {context["role"]}

        Experience: {context["experience"]}

        Skills: {' '.join(context["skills"])}

        Assessment Types:
        {' '.join(context["assessment_types"])}
        """

        results = self.retriever.search(
            query=query,
            context=context,
            top_k=10
        )

        recommendations = []

        for item in results:
            recommendations.append({
                "name": item["name"],
                "url": item["url"],
                "test_type": ", ".join(item.get("keys", []))
            })

        return recommendations