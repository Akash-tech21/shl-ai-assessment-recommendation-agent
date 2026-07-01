class ClarificationEngine:

    def decide(self, context):

        role = context.get("role")
        experience = context.get("experience")

        # Missing role
        if not role:
            return {
                "ready": False,
                "question": "What role are you hiring for?"
            }

        # Missing experience
        if not experience:
            return {
                "ready": False,
                "question": "What is the expected experience level?"
            }

        # Everything required is available
        return {
            "ready": True,
            "question": None
        }