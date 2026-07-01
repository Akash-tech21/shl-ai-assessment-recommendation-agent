class Metrics:

    @staticmethod
    def recall_at_k(recommended, expected):

        if len(expected) == 0:
            return 1.0

        hits = 0

        for item in recommended:

            if item in expected:
                hits += 1

        return hits / len(expected)