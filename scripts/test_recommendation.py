import os
import sys

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

sys.path.insert(0, PROJECT_ROOT)

from app.agents.recommendation_engine import RecommendationEngine

engine = RecommendationEngine()

context = {
    "role": "Java Developer",
    "experience": "4",
    "skills": ["Java"],
    "assessment_types": []
}

results = engine.recommend(context)

for assessment in results:

    print(assessment["name"])