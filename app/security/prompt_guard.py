BLOCKED_PATTERNS = [
    "ignore previous instructions",
    "system prompt",
    "developer message",
    "act as",
    "bypass"
]

class PromptGuard:

    def is_safe(self, query: str):

        query = query.lower()

        return not any(
            p in query
            for p in BLOCKED_PATTERNS
        )