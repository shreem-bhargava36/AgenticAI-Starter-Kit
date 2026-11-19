import streamlit as st
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load environment variables
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = os.getenv("GEMINI_MODEL", "gemini-3.5-flash-lite")

st.set_page_config(
    page_title="My AI Agent",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 My AI Assistant")
st.caption("Powered by Google Gemini")

# Check API key
if not API_KEY:
    st.error("Gemini API key not found. Check your .env file.")
    st.stop()

# Create Gemini client
client = genai.Client(api_key=API_KEY)

# Create chat session
def create_chat():
    return client.chats.create(
        model=MODEL,
        config=types.GenerateContentConfig(
            system_instruction=(
                "You are a helpful AI assistant. "
                "Give clear, friendly and useful answers."
            )
        )
    )

# Initialize session state
if "chat" not in st.session_state:
    st.session_state.chat = create_chat()
    st.session_state.messages = []

# Sidebar
with st.sidebar:
    st.header("Settings")
    if st.button("🗑️ Clear Chat"):
        st.session_state.chat = create_chat()
        st.session_state.messages = []
        st.rerun()

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
prompt = st.chat_input("Ask me anything...")

if prompt:
    # Display user message
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Get AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = st.session_state.chat.send_message(prompt)
                answer = response.text or "I couldn't generate a response."
                st.markdown(answer)

                st.session_state.messages.append(
                    {"role": "assistant", "content": answer}
                )

            except Exception as e:
                st.error(f"Error: {e}")