from app.retrieval.hybrid_retriever import HybridRetriever


class RecommendationEngine:

    def __init__(self):
        self.retriever = HybridRetriever()

    def recommend(self, context):

        role = context.get("role") or ""
        experience = context.get("experience") or ""
        skills = context.get("skills") or []
        assessment_types = context.get("assessment_types") or []

        query = f"""
Role: {role}

Experience: {experience}

Skills:
{' '.join(skills)}

Assessment Types:
{' '.join(assessment_types)}
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