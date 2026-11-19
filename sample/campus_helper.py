"""Example agent: a simple campus helper using two Python tools."""

import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")

if not API_KEY or API_KEY == "PASTE_YOUR_GEMINI_API_KEY_HERE":
    raise SystemExit(
        "GEMINI_API_KEY is missing. Copy .env.example to .env "
        "and add your Gemini API key."
    )

client = genai.Client(api_key=API_KEY)


# Tools: plain Python functions. Their docstrings explain when to use them.
def get_timetable(day: str) -> str:
    """Return the sample class timetable for a day, such as Monday or Tuesday."""
    data = {
        "monday": "DSA 9:00 AM, AI 11:00 AM, Lab 2:00 PM",
        "tuesday": "Maths 10:00 AM, Python 12:00 PM",
        "wednesday": "AI 9:00 AM, DBMS 11:00 AM",
    }
    return data.get(day.lower().strip(), "No sample timetable found for that day.")


def get_mess_menu(meal: str) -> str:
    """Return the sample mess menu for breakfast, lunch, or dinner."""
    data = {
        "breakfast": "Poha and tea",
        "lunch": "Dal, rice, roti, and paneer",
        "dinner": "Rajma, rice, and roti",
    }
    return data.get(meal.lower().strip(), "Choose breakfast, lunch, or dinner.")


ROLE = (
    "You are a friendly campus helper for college students. "
    "Use get_timetable for timetable questions and get_mess_menu for meal questions. "
    "These are sample details, not live college data. Keep answers short."
)

config = types.GenerateContentConfig(
    system_instruction=ROLE,
    tools=[get_timetable, get_mess_menu],
)

chat = client.chats.create(model=MODEL, config=config)

print(f"Campus Helper ready! Model: {MODEL}")
print("Ask about the sample timetable or mess menu, or type 'quit' to exit.")

while True:
    try:
        question = input("\nYou: ").strip()
        if question.lower() in {"quit", "exit"}:
            print("Goodbye!")
            break
        if not question:
            continue

        response = chat.send_message(question)
        print("Agent:", response.text or "I couldn't generate a text response.")
    except KeyboardInterrupt:
        print("\nGoodbye!")
        break
    except Exception as error:
        print(f"Something went wrong: {error}")
        print("Check your API key, internet connection, and model access.")
