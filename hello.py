
# AI Agent Arena - setup check. Run: python hello.py
from google import genai
 
client = genai.Client()            # reads GEMINI_API_KEY from your system
MODEL = "gemini-3.6-flash"         # club will confirm the exact model name
 
reply = client.models.generate_content(model=MODEL, contents="Say hi in one line")
print(reply.text)
print("Setup OK! You are ready for AI Agent Arena.")