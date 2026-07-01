from fastapi import APIRouter

from app.schemas.chat_request import ChatRequest
from app.agents.conversation_analyzer import ConversationAnalyzer
from app.agents.clarification_engine import ClarificationEngine
from app.agents.recommendation_engine import RecommendationEngine
from app.services.gemini_service import GeminiService
from app.security.prompt_guard import PromptGuard
from app.security.off_topic_guard import OffTopicGuard


router = APIRouter()

analyzer = ConversationAnalyzer()
clarifier = ClarificationEngine()
recommender = RecommendationEngine()
gemini = GeminiService()
guard = PromptGuard()
off_topic_guard = OffTopicGuard()

@router.post("/chat")
def chat(request: ChatRequest):
    
    # Convert Pydantic models to dictionaries
    messages = [msg.model_dump() for msg in request.messages]

    # Get latest user message
    latest_message = messages[-1]["content"].lower()

    # Prompt Injection Protection
    if not guard.is_safe(latest_message):
        return {
            "reply": "I can only assist with SHL assessment recommendations. Please ask about hiring needs, assessments, or candidate evaluation.",
            "recommendations": [],
            "end_of_conversation": True
        }

    # Handle comparison requests (placeholder)
    if "compare" in latest_message:
        return {
            "reply": "Comparison feature is under development.",
            "recommendations": [],
            "end_of_conversation": True
        }

    # Analyze conversation
    context = analyzer.analyze(messages)

    # Decide if more information is needed
    decision = clarifier.decide(context)

    if not decision["ready"]:
        return {
            "reply": decision["question"],
            "recommendations": [],
            "end_of_conversation": False
        }

    # Get recommendations
    recommendations = recommender.recommend(context)

    # Generate Gemini response
    reply = gemini.generate_reply(
        context,
        recommendations
    )

    return {
        "reply": reply,
        "recommendations": recommendations,
        "end_of_conversation": True
    }