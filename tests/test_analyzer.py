from app.agents.conversation_analyzer import ConversationAnalyzer


def test_analyzer():

    analyzer = ConversationAnalyzer()

    messages = [
        {
            "role": "user",
            "content": "Looking for a Python developer with 3 years experience."
        }
    ]

    context = analyzer.analyze(messages)

    assert context["ready"] is True