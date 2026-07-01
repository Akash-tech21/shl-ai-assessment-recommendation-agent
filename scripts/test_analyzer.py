import os
import sys

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

sys.path.insert(0, PROJECT_ROOT)

from app.agents.conversation_analyzer import ConversationAnalyzer

messages = [

    {

        "role":"user",

        "content":"Hiring a Java developer."

    },

    {

        "role":"assistant",

        "content":"Sure. What experience level?"

    },

    {

        "role":"user",

        "content":"4 years."
    }

]

analyzer = ConversationAnalyzer()

print(analyzer.analyze(messages))