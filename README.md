# AgenticAI Starter Kit

Welcome to **AgenticAI**! Build your first AI agent with Python and the Gemini API.

This starter kit is designed for beginners. You will create Python tools, give your agent a role, and let Gemini decide when to use the tools.

## Project structure

```text
AgenticAI-Starter-Kit/
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
├── hello.py
├── starter_code/
│   └── agent.py
└── sample/
    └── campus_helper.py
```

## 1. Requirements

- Python 3.10 or newer
- A Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey)
- VS Code (recommended)

## 2. Open the project

Download the ZIP from GitHub and extract it. In VS Code, choose **File → Open Folder** and open the extracted `AgenticAI-Starter-Kit` folder.

Open the VS Code terminal: **Terminal → New Terminal**.

## 3. Create and activate a virtual environment

**Windows (PowerShell):**

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use Command Prompt:

```bat
.venv\Scripts\activate.bat
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 4. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 5. Add your Gemini API key

1. Make a copy of `.env.example` in the project root.
2. Rename the copy to `.env`.
3. Open `.env` and replace the placeholder with your own key.

Example:

```env
GEMINI_API_KEY=your_real_api_key_here
GEMINI_MODEL=gemini-3.8-flash
```

**Never commit or share `.env`.** The `.gitignore` file prevents it from being uploaded. The `.env.example` template is safe to upload because it contains no real key.

If the workshop team announces a different model, change `GEMINI_MODEL` in your local `.env` file.

## 6. Test your setup

Run:

```bash
python hello.py
```

You should see a short response from Gemini and a setup-success message. If it fails, check that your key is correct, the Gemini API is enabled for your key, and your internet connection works.

## 7. Build your own agent

Open:

```text
starter_code/agent.py
```

During the workshop, edit the three `TODO` sections:

1. **TODO 1 — Tools:** Write Python function(s) that do a useful task. Add a clear docstring explaining what each tool does.
2. **TODO 2 — Role:** Tell the agent who it is, what it should do, and how it should answer.
3. **TODO 3 — Tool list:** Add every function you want Gemini to be able to call to `TOOLS`.

Run your agent from the project root:

```bash
python starter_code/agent.py
```

Type `quit` to stop the agent.

## 8. Try the sample agent

The sample campus helper demonstrates two tools: a sample timetable lookup and a sample mess-menu lookup.

```bash
python sample/campus_helper.py
```

The timetable and menu are demonstration data, not live college information.

## Common problems

- **`ModuleNotFoundError`:** Activate your virtual environment and run `pip install -r requirements.txt`.
- **API key missing:** Confirm that your file is named `.env` (not `.env.txt`) and is in the project root.
- **Invalid API key / permission error:** Create or check your key in Google AI Studio.
- **Model not found / unavailable:** Ask the workshop team which model is enabled for your API key, then update `GEMINI_MODEL` in `.env`.
- **PowerShell activation blocked:** Use the Command Prompt activation command shown above.

## Workshop rules

- Change the `TODO` sections in `starter_code/agent.py`.
- Never upload your API key or `.env` file.
- Test your agent before presenting or submitting it.
- Keep your tool focused and useful. Be creative!

Happy building!

**Team AgenticAI ❤️**
