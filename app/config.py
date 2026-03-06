import os
from dotenv import load_dotenv

# Absolute path to project root
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)
ENV_PATH = os.path.join(ROOT_DIR, ".env")

# Force load .env
load_dotenv(ENV_PATH)

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

print("GROQ_API_KEY:", GROQ_API_KEY)
print("OPENAI_API_KEY:", OPENAI_API_KEY)
print("TAVILY_API_KEY:", TAVILY_API_KEY)
print("GOOGLE_API_KEY:", GOOGLE_API_KEY)
import os
from dotenv import find_dotenv

print("FOUND .env AT:", find_dotenv())
