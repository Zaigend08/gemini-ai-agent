import os
from dotenv import load_dotenv

load_dotenv()

MODEL_NAME = "gemini-3-flash-preview"
API_KEY = os.getenv("GOOGLE_API_KEY")