# Chatbot using LangChain, Ollama, and Streamlit

A simple yet powerful chatbot interface built using LangChain, Ollama, and Streamlit. This project allows users to interact with an LLM-powered chatbot that uses Ollama models, all rendered beautifully in a Streamlit interface.

## Features
- **LLM Integration with Ollama**
    - Connects to Ollama models, enabling seamless chat functionality.
    - Allows users to send messages and receive responses using LangChain's integration with Ollama.
- **Real-time Chat with Streaming**
    - Implements real-time response streaming using Streamlit's chat interface.
    - Supports partial responses and updates as the model streams the result.
- **Persistent Chat History**
    - Keeps a record of the conversation, allowing users to see the chat history and context.
- **Interactive UI**
    - Streamlit provides a user-friendly interface with message bubbles for both human and AI messages.

## Screenshots
![Chatbot in Action](https://raw.githubusercontent.com/Mangaleshwaran2002/Ollama-Powered-LLM-CLI-Toolkit/refs/heads/master/screenshots/Screen_Recording.gif)

## Requirements

To run this application, you'll need to install the following Python packages:

* Python ≥ 3.8
* LangChain
* Ollama installed and running locally (ollama serve)
* Streamlit

### Setup

Step 1: **Clone the Repository**

```bash
git clone https://github.com/Mangaleshwaran2002/Chatbot-using-LangChain-Ollama-and-Streamlit.git
cd Chatbot-using-LangChain-Ollama-and-Streamlit
```

Step 2: **Install dependencies**

```bash
pip install -r requirements.txt
(or)
uv pip install -r requirements.txt
```

Step 3: **Ensure Ollama is running**

```bash
ollama serve  # Run in a separate terminal
```

Step 4: **Run the app**
```bash
streamlit run app.py
(or)
uv run streamlit run app.py
```

## Contributing
Contributions are welcome! Follow these steps:

1. Fork the repo and create a feature branch.
2. Write tests (if adding new logic) and ensure existing ones pass.
3. Keep the code style consistent with black / flake8.
4. Submit a Pull Request with a clear description of the change.
5. Please open an issue first if you’re planning a large modification.

## License
This project is licensed under the MIT License - see the LICENSE file for details.