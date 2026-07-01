import google.generativeai as genai

from app.core.config import settings

genai.configure(api_key=settings.GEMINI_API_KEY)


class GeminiService:

    def __init__(self):
        self.model = genai.GenerativeModel(settings.MODEL_NAME)

    def generate(self, prompt: str) -> str:
        response = self.model.generate_content(prompt)
        return response.text

    def generate_reply(self, context, recommendations):

        recommendation_list = "\n".join(
            f"- {item['name']}" for item in recommendations
        )

        prompt = f"""
You are an SHL assessment recommendation assistant.

Candidate Requirements:
Role: {context['role']}
Experience: {context['experience']}
Skills: {', '.join(context['skills'])}

Recommended SHL Assessments:
{recommendation_list}

Explain why these assessments are appropriate in a concise and professional manner.
"""

        return self.generate(prompt)