# Conversational Q&A Bot 🤖

A modern conversational chatbot powered by Google's Gemini 2.5 AI models with a beautiful Streamlit interface. The bot remembers your entire conversation history and provides intelligent, context-aware responses.

## Features

- **Conversational Memory** - Maintains full conversation history for context-aware responses
- **Real-time Streaming** - See responses appear in real-time as the AI generates them
- **Modern Chat UI** - Clean, intuitive chat interface built with Streamlit
- **Customizable Settings** - Adjust temperature, max tokens, and model selection
- **Multiple Gemini Models** - Choose from Gemini 2.5 Flash, Pro, or Flash-Lite

## Tech Stack

- **Python 3.12**
- **Streamlit** - Web interface
- **Google GenAI SDK** - Gemini API integration

## Prerequisites

- Python 3.7 or higher
- A Google Gemini API key ([Get one here](https://aistudio.google.com/app/apikey))

## Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd "Q&A bot"
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up your API key**
   
   Create a `.env` file in the project root:
   ```bash
   GEMINI_API_KEY=your_actual_api_key_here
   ```
   
   Replace `your_actual_api_key_here` with your actual Gemini API key.

## Usage

1. **Start the application**
   ```bash
   streamlit run app.py
   ```
   
   Or using the virtual environment directly:
   ```bash
   .\venv\Scripts\streamlit.exe run app.py
   ```

2. **Open your browser**
   
   The app will automatically open at `http://localhost:8501`

3. **Start chatting!**
   - Type your question in the chat input at the bottom
   - Press Enter or click the send button
   - Watch as the AI responds in real-time
   - Your conversation history is maintained throughout the session

## Configuration

Use the sidebar to customize your experience:

- **Gemini Model** - Select from:
  - `gemini-2.5-flash` - Balanced performance (default)
  - `gemini-2.5-pro` - Most capable, slower
  - `gemini-2.5-flash-lite` - Fastest, lighter
  
- **Max Output Tokens** - Control response length (64-2048)
- **Temperature** - Adjust creativity (0.0-1.0)
- **Clear History** - Reset the conversation

## Security

- Never commit your `.env` file to version control
- The `.gitignore` file is configured to exclude sensitive files
- Keep your API key confidential

## Troubleshooting

### API Key Error
```
API key not valid. Please pass a valid API key.
```
**Solution:** Make sure your `.env` file contains a valid API key from Google AI Studio.

### Module Not Found Error
```
ModuleNotFoundError: No module named 'google'
```
**Solution:** Ensure you're in the virtual environment and have installed all dependencies:
```bash
.\venv\Scripts\activate
pip install -r requirements.txt
```

### Streamlit Not Running
**Solution:** Use the full path to streamlit in your venv:
```bash
.\venv\Scripts\streamlit.exe run app.py
```

## License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## Author

Created with ❤️ using Google's Gemini AI


**Note:** This bot requires an active internet connection and a valid Gemini API key to function.
