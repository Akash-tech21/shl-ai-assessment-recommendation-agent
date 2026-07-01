import os
import sys

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)
sys.path.insert(0, PROJECT_ROOT)

from evaluation.metrics import Metrics

recommended = [
    "Java 8 (New)",
    "Core Java (Advanced Level) (New)"
]

expected = [
    "Java 8 (New)"
]

print(Metrics.recall_at_k(recommended, expected))