class OffTopicGuard:

    ALLOWED_KEYWORDS = [
        "assessment",
        "candidate",
        "hiring",
        "job",
        "developer",
        "engineer",
        "manager",
        "java",
        "python",
        "sales",
        "personality",
        "reasoning",
        "shl",
        "test",
        "assessment"
    ]

    def is_relevant(self, query: str) -> bool:

        query = query.lower()

        return any(
            keyword in query
            for keyword in self.ALLOWED_KEYWORDS
        )