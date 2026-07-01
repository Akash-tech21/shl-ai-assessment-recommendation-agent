class ClarificationEngine:

    def decide(self, context):

        # Missing role
        if not context["role"]:
            return {
                "ready": False,
                "question": "What role are you hiring for?"
            }

        # Missing experience
        if not context["experience"]:
            return {
                "ready": False,
                "question": "What is the expected experience level?"
            }

        # Ready
        return {
            "ready": True,
            "question": None
        }