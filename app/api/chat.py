from fastapi import APIRouter, HTTPException

from app.schemas.chat_request import ChatRequest
from app.agents.conversation_analyzer import ConversationAnalyzer
from app.agents.clarification_engine import ClarificationEngine
from app.agents.recommendation_engine import RecommendationEngine
from app.services.gemini_service import GeminiService
from app.security.prompt_guard import PromptGuard
from app.security.off_topic_guard import OffTopicGuard

router = APIRouter()

# Initialize services
analyzer = ConversationAnalyzer()
clarifier = ClarificationEngine()
recommender = RecommendationEngine()
gemini = GeminiService()
guard = PromptGuard()
off_topic_guard = OffTopicGuard()


@router.post("/chat")
def chat(request: ChatRequest):
    try:

        messages = request.messages

        if not messages:
            return {
                "reply": "Please provide a message.",
                "recommendations": [],
                "end_of_conversation": False
            }

        latest_message = messages[-1].content

        # Prompt injection protection
        if not guard.is_safe(latest_message):
            return {
                "reply": "Your request contains unsafe instructions.",
                "recommendations": [],
                "end_of_conversation": True
            }

        # Check relevance using the complete conversation
        conversation_text = " ".join(
            message.content for message in messages
        )

        if not off_topic_guard.is_relevant(conversation_text):
            return {
                "reply": "I can only help with SHL assessment recommendations.",
                "recommendations": [],
                "end_of_conversation": True
            }

        # Comparison placeholder
        if "compare" in conversation_text.lower():
            return {
                "reply": "Comparison feature is under development.",
                "recommendations": [],
                "end_of_conversation": True
            }

        # Analyze conversation
        context = analyzer.analyze(messages)

        # Clarification stage
        decision = clarifier.decide(context)

        if not decision["ready"]:
            return {
                "reply": decision["question"],
                "recommendations": [],
                "end_of_conversation": False
            }

        # Recommendation stage
        recommendations = recommender.recommend(context)

        # Generate final response
        reply = gemini.generate_reply(
            context=context,
            recommendations=recommendations
        )

        return {
            "reply": reply,
            "recommendations": recommendations,
            "end_of_conversation": True
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error: {str(e)}"
        )