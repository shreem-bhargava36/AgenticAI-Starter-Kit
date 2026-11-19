"""Check that the Gemini API key and Python package are configured."""

import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")

if not API_KEY or API_KEY == "PASTE_YOUR_GEMINI_API_KEY_HERE":
    raise SystemExit(
        "GEMINI_API_KEY is missing. Copy .env.example to .env "
        "and paste your key into the .env file."
    )

client = genai.Client(api_key=API_KEY)

try:
    response = client.models.generate_content(
        model=MODEL,
        contents="Say hello in one short sentence.",
    )
    print(response.text or "The model returned an empty response.")
    print("\nSetup OK! You are ready to build an AI agent.")
except Exception as error:
    print(f"Gemini API test failed: {error}")
    print("Check your API key, internet connection, and model access.")
