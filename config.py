import sys

sys.path.append("./models")
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODELS_DIR = os.path.join(BASE_DIR, "models")

TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")

TESTS_DIR = os.path.join(BASE_DIR, "tests")

UTILS_DIR = os.path.join(BASE_DIR, "utils")