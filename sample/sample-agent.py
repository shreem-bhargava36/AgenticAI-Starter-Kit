# AI Agent Arena - SAMPLE "Campus Helper" agent (teacher's version)
from google import genai
from google.genai import types

client = genai.Client()            # reads GEMINI_API_KEY
MODEL = "gemini-3.6-flash"         # club will confirm the exact model name

# ---- TOOLS: plain Python functions. The docstring tells the model when to use them ----
def get_timetable(day: str) -> str:
    """Return the class timetable for a day of the week, e.g. Monday."""
    data = {
        "monday": "DSA 9:00, AI 11:00, Lab 2:00",
        "tuesday": "Maths 10:00, Python 12:00",
        "wednesday": "AI 9:00, DBMS 11:00",
    }
    return data.get(day.lower(), "No classes found for that day.")

def get_mess_menu(meal: str) -> str:
    """Return today's mess menu for a meal: breakfast, lunch or dinner."""
    data = {
        "breakfast": "Poha, tea",
        "lunch": "Dal, rice, roti, paneer",
        "dinner": "Rajma, rice, roti",
    }
    return data.get(meal.lower(), "Meal not found. Try breakfast, lunch or dinner.")

# ---- ROLE: who the agent is and how it should answer ----
ROLE = ("You are a friendly campus helper for college students. "
        "Use your tools to answer timetable and mess menu questions. "
        "Keep answers short.")

# ---- SETUP ----
config = types.GenerateContentConfig(system_instruction=ROLE,
                                     tools=[get_timetable, get_mess_menu])
chat = client.chats.create(model=MODEL, config=config)

# ---- CHAT LOOP ----
print("Campus Helper ready. Type 'quit' to exit.")
while True:
    question = input("You: ")
    if question.strip().lower() == "quit":
        break
    try:
        print("Agent:", chat.send_message(question).text)
    except Exception as e:
        print("Something went wrong:", e)