from app.retrieval.hybrid_retriever import HybridRetriever
from app.services.gemini_service import GeminiService


class ComparisonEngine:

    def __init__(self):
        self.retriever = HybridRetriever()
        self.llm = GeminiService()

    def compare(self, query: str):

        # Retrieve the two most relevant assessments
        assessments = self.retriever.search(query, top_k=2)

        if len(assessments) < 2:
            return {
                "reply": "I couldn't find two matching SHL assessments to compare.",
                "recommendations": [],
                "end_of_conversation": True
            }

        assessment_a = assessments[0]
        assessment_b = assessments[1]

        prompt = f"""
You are an SHL Assessment Expert.

Compare ONLY these two SHL assessments.

Assessment A

Name: {assessment_a['name']}
Description:
{assessment_a['description']}

Assessment B

Name: {assessment_b['name']}
Description:
{assessment_b['description']}

Return:

• Purpose
• Skills Measured
• Best Use Case
• Which assessment is more suitable and why

Maximum 150 words.
"""

        reply = self.llm.generate(prompt)

        recommendations = [
            {
                "name": assessment_a["name"],
                "url": assessment_a["url"],
                "test_type": ", ".join(assessment_a["keys"])
            },
            {
                "name": assessment_b["name"],
                "url": assessment_b["url"],
                "test_type": ", ".join(assessment_b["keys"])
            }
        ]

        return {
            "reply": reply,
            "recommendations": recommendations,
            "end_of_conversation": True
        }