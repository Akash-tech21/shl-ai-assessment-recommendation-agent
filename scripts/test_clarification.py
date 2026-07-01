import os
import sys

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

sys.path.insert(0, PROJECT_ROOT)

from app.agents.clarification_engine import ClarificationEngine

engine = ClarificationEngine()

# Example 1
context = {
    "role": "Java Developer",
    "experience": None,
    "skills": ["Java"],
    "assessment_types": [],
    "ready": False
}

print(engine.decide(context))