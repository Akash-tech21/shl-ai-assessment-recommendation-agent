from enum import Enum


class Intent(str, Enum):
    RECOMMEND = "recommend"
    COMPARE = "compare"
    REFINE = "refine"
    OFF_TOPIC = "off_topic"


class IntentClassifier:

    def predict(self, message: str) -> Intent:

        message = message.lower()

        if "compare" in message:
            return Intent.COMPARE

        if any(word in message for word in ["actually", "instead", "change", "modify"]):
            return Intent.REFINE

        return Intent.RECOMMEND