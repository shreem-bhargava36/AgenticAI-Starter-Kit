# 🤖 Agentic AI Starter Kit

A beginner-friendly Python starter kit to build AI agents using Google's Gemini API. It includes a command-line AI agent, a web-based chatbot, and a sample Campus Helper agent.

## ✨ Features

- 🧠 Gemini-powered AI assistant
- 💬 Interactive command-line chatbot
- 🌐 Streamlit-based web interface
- 🔧 Custom Python tool integration
- 💭 Conversation history during a chat session
- 🗑️ Clear chat functionality
- 🎓 Sample Campus Helper agent
- 🔐 Environment-variable-based API key management

## 🛠️ Tech Stack

- Python
- Google Gemini API
- Google Gen AI SDK
- Streamlit
- python-dotenv

## 📁 Project Structure

```text
Agentic-AI-Starter-Kit/
│
├── app.py
├── hello.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env.example
│
├── starter_code/
│   └── agent.py
│
└── sample/
    └── campus_helper.py
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/shreem-bhargava36/AgenticAI-Starter-Kit.git
cd AgenticAI-Starter-Kit
```

### 2. Create a virtual environment

**Windows:**

```powershell
python -m venv .venv
.venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure your Gemini API key

Create a `.env` file in the project root using `.env.example` as a template.

Add:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
GEMINI_MODEL=YOUR_SUPPORTED_GEMINI_MODEL
```

Get an API key from [Google AI Studio](https://aistudio.google.com/apikey).

**Important:** Never upload your `.env` file or expose your API key publicly.

## 🧪 Test Gemini API Connection

Run:

```bash
python hello.py
```

A successful connection should display a confirmation message.

## 💻 Run the Command-Line AI Agent

```bash
python starter_code/agent.py
```

Start chatting with your Gemini-powered agent.

Type `exit` to stop the conversation.

## 🌐 Run the Web Application

Launch the Streamlit chatbot:

```bash
python -m streamlit run app.py
```

Open your browser at:

```text
http://localhost:8501
```

### Web Application Features

- Interactive chat interface
- Gemini-generated responses
- Conversation history
- Clear chat option
- Simple and beginner-friendly interface

## 🎓 Run the Sample Campus Helper Agent

```bash
python sample/campus_helper.py
```

The sample demonstrates how an AI agent can use Python functions as tools to answer campus-related questions.

**Note:** The timetable and mess menu use sample data, not live college information.

## 🔧 Building Your Own AI Agent

To customize the starter agent:

1. Define the agent's role using a system instruction.
2. Create Python functions for specific tasks.
3. Register your functions as tools.
4. Connect the tools to the Gemini model.
5. Test the agent with different questions.

## 🔒 Security

- Store API keys in `.env`.
- Keep `.env` out of GitHub.
- Use `.env.example` to document required environment variables.
- Never hardcode API keys in Python files.

## 🎯 Project Goal

Make learning Agentic AI easier for beginners by providing a simple, working foundation for building AI assistants that can interact with tools and perform useful tasks.

