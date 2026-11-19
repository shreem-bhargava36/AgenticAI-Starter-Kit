#AI Agent Arena - STARTER FILE. Change only the parts marked TODO.
from google import genai
from google.genai import types

client = genai.Client()            # reads GEMINI_API_KEY
MODEL = "gemini-3.6-flash"         # club will confirm the exact model name

# TODO 1: Write your tool(s). Rename this function and change what it does.
# The docstring is important: it tells the model when to use the tool.
def my_tool(topic: str) -> str:
    """Describe in one line what this tool does and when to use it."""
    data = {"example": "Replace this dummy data with your own idea."}
    return data.get(topic.lower(), "Nothing found.")

# TODO 2: Write your agent's role (who it is, what job it does, how it answers).
ROLE = "You are a helpful assistant. Use your tools when needed. Keep answers short."

# TODO 3: Add every tool you wrote to this list.
TOOLS = [my_tool]

# ---- Do not change below this line ----
config = types.GenerateContentConfig(system_instruction=ROLE, tools=TOOLS)
chat = client.chats.create(model=MODEL, config=config)

print("Agent ready. Type 'quit' to exit.")
while True:
    question = input("You: ")
    if question.strip().lower() == "quit":
        break
    try:
        print("Agent:", chat.send_message(question).text)
    except Exception as e:
        print("Something went wrong:", e)