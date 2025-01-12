# J.A.R.V.I.S AI Assistant 1.1 🤖

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](https://opensource.org/licenses/MIT)

J.A.R.V.I.S (Just A Rather Very Intelligent System) is an AI assistant built by **Nirbhay** (a.k.a Strange Stark), inspired by the fictional AI from *Iron Man*. This assistant performs a variety of tasks, such as answering questions, controlling system operations, and providing smart responses, all powered by Python and external APIs.

## 🌟 Features

- **Voice Recognition**: Capture user commands through speech.
- **Text-to-Speech (TTS)**: J.A.R.V.I.S responds audibly with spoken feedback.
- **System Commands**: Perform system operations like shutdown, restart, and log out.
- **Web Search**: Search Wikipedia, Google, and YouTube.
- **News Updates**: Get real-time news from the top news sources.
- **Battery Information**: Check battery status, percentage, and time left.
- **Email & WhatsApp**: Send emails and WhatsApp messages directly from J.A.R.V.I.S.
- **Chat History**: Keeps track of interactions and provides context to MetaAI for intelligent responses.
- **Calculator**: A built-in calculator for quick math.
- **IP Address**: Fetch your public IP address.
  
## 🔧 Libraries & Dependencies

This project relies on the following libraries:

- **wikipedia**: For Wikipedia search.
- **pyautogui**: For automating system interactions.
- **requests**: To make API requests for weather, news, etc.
- **psutil**: To monitor system resources (battery status, CPU usage).
- **pywhatkit**: For controlling YouTube and WhatsApp.
- **pyfiglet**: For generating ASCII art.
- **meta_ai_api**: Integration with MetaAI for intelligent responses.
- **smtplib**: To send emails via SMTP.
- **webbrowser**: To open URLs in the browser.
- **time**, **os**, **datetime**: For system interactions and time-based operations.

### Installation

Follow these steps to set up J.A.R.V.I.S on your local machine:

1. **Clone the repository**:

    ```bash
    git clone https://github.com/lordstarkk/JARIVIS-1.1-PYTHON-AI-ASSISTANT
    cd JARIVIS-1.1-PYTHON-AI-ASSISTANT
    ```

2. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

    _Note: Some libraries may require additional installation steps or permissions depending on your operating system._

---

## 🚀 Usage

To launch J.A.R.V.I.S, follow these steps:

1. **Run the main script**:

    ```bash
    python main.py
    ```

2. **Command Examples**:

   Here are some voice commands you can try:

   - **System Commands**:
     - "Shutdown system"
     - "Restart system"
     - "Log out"

   - **Web Search**:
     - "Search about [topic]"
     - "Open YouTube"
     - "Open [website]"

   - **Battery & System Info**:
     - "What is the battery status?"
     - "What is the time?"
   
   - **Messaging**:
     - "Send email to [name] with subject [subject]"
     - "Send a WhatsApp message to [contact]"

   - **Calculator**:
     - "Calculate [math expression]"

---

## 🧠 MetaAI Integration

J.A.R.V.I.S leverages **MetaAI** to provide intelligent and context-aware responses. The assistant remembers previous conversations, allowing it to offer more relevant answers by using chat history stored in a file.

### Chat History:

- **What it does**: J.A.R.V.I.S stores a log of every interaction in a `chat_history.txt` file.
- **Why it matters**: This allows MetaAI to use past queries as context for smarter responses.
- **How it works**: Upon every launch, the chat history is passed to MetaAI to improve the assistant's answers.

```python
# Function to read chat history from file
def read_chat_history():
    try:
        with open(CHAT_HISTORY_FILE, "r") as file:
            return file.read()
    except FileNotFoundError:
        return ""

# Process user query and use chat history for MetaAI prompt
response = ai.prompt(
    message=f"""
    Current chat history:
    {read_chat_history()}

    Here's the user's query: {query}
    """
)
```

📝 To-Do List
Error Handling: Improve error handling for unreliable network connections or unavailable APIs.
More System Operations: Add functionality to control IoT devices (e.g., lights, thermostats).
User Profiles: Implement user preferences, names, and history.
Mobile App: Create a mobile app to interact with the assistant remotely.
Multilingual Support: Add support for multiple languages.
Cloud Integration: Enable cloud storage for data, allowing access across devices.
💡 Contributing
We welcome contributions! If you’d like to help improve the assistant, please fork the repository, make your changes, and submit a pull request.

Steps to contribute:

Fork the repository
Create a new branch (git checkout -b feature-name)
Make your changes
Commit your changes (git commit -am 'Add new feature')
Push to the branch (git push origin feature-name)
Submit a pull request
🛠 License
This project is open-source and licensed under the MIT License. You are free to use, modify, and distribute this software as per the terms of the license.

📢 Contact
For any issues, questions, or suggestions, please feel free to open an issue or contact the creator:

Email: starkforbusiness1@gmail.com
Twitter: @strangexstark
### Thank you for using J.A.R.V.I.S! We hope it helps make your life easier. Stay tuned for more updates!
