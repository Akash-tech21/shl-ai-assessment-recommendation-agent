import json

from app.services.gemini_service import GeminiService


class ConversationAnalyzer:

    def __init__(self):
        self.llm = GeminiService()

    def analyze(self, messages):

        conversation = "\n".join(
            f"{msg['role']}: {msg['content']}"
            for msg in messages
        )

        prompt = f"""
You are an AI assistant that extracts hiring requirements.

Analyze the conversation and return ONLY valid JSON.

Schema:

{{
    "role": "",
    "experience": "",
    "skills": [],
    "job_levels":"",
    "assessment_types": [],
    "remote":null,
    "adaptive":null,
    "ready": true
}}

Rules:
- If a value is unknown, return null.
- Do not include markdown.
- Do not include explanations.
- Return JSON only.

Conversation:

{conversation}
"""

        response = self.llm.generate(prompt)

        try:
            return json.loads(response)

        except Exception:
            return {
                "role": None,
                "experience": None,
                "skills": [],
                "assessment_types": [],
                "ready": False
            }