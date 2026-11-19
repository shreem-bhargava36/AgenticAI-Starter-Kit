"""Beginner-friendly AI agent starter for AgentForge.

Edit only the sections marked TODO during the workshop.
"""

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

# TODO 1: Create your tool(s).
# A tool is a normal Python function that gives your agent useful information
# or lets it perform a specific task. Write a clear docstring.
def my_tool(topic: str) -> str:
    """Return useful information about a topic. Replace this example with your own tool."""
    data = {
        "example": "Replace this sample result with information for your agent idea."
    }
    return data.get(topic.lower().strip(), "I don't have information about that topic yet.")


# TODO 2: Describe your agent's role, job, and answer style.
ROLE = (
    "You are a helpful assistant. Use your tools when they are relevant. "
    "If you do not know something, say so. Keep answers clear and short."
)


# TODO 3: Add all the functions you want the agent to use.
TOOLS = [my_tool]


# Do not change below this line unless your instructor asks you to.
config = types.GenerateContentConfig(
    system_instruction=ROLE,
    tools=TOOLS,
)

chat = client.chats.create(model=MODEL, config=config)

print(f"Agent ready! Model: {MODEL}")
print("Ask a question, or type 'quit' to exit.")

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
