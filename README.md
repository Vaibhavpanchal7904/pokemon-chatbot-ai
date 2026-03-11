# Pokémon AI Chatbot

A beginner-friendly AI chatbot that answers Pokémon-related questions using real data from the PokeAPI and generates responses using a local LLM via Ollama.

## Technologies Used

Backend
- Python
- FastAPI
- LangGraph
- LangChain
- Ollama (Local LLM)

Frontend
- HTML
- CSS
- JavaScript

API
- PokeAPI

---

# Features

- Conversational Pokémon chatbot
- Uses real Pokémon data from PokeAPI
- Runs a local AI model using Ollama
- Maintains conversation context
- Simple web chat interface

---

# Project Structure

```
pokemon-chatbot
│
├── backend
│   ├── main.py
│   ├── controllers
│   ├── chatbot
│   ├── models
│   ├── prompts
│   └── services
│
├── frontend
│   ├── index.html
│   ├── styles.css
│   └── script.js
│
├── requirements.txt
└── README.md
```

---

# Prerequisites

Before running the project install:

1. Python 3.10 or higher  
2. Git (optional)  
3. Ollama for running local LLM

---

# Install Python

Download from:

https://www.python.org/downloads/

Verify installation:

```
python --version
```

---

# Install Ollama

Download from:

https://ollama.com

After installation verify:

```
ollama --version
```

---

# Download LLM Model

Run:

```
ollama pull llama3
```

This downloads the local LLM model.

---

# Project Setup

Clone repository:

```
git clone https://github.com/YOUR_USERNAME/pokemon-chatbot-ai.git
```

Go inside folder:

```
cd pokemon-chatbot-ai
```

---

# Create Virtual Environment

```
python -m venv venv
```

Activate it:

Windows:

```
venv\Scripts\activate
```

Mac/Linux:

```
source venv/bin/activate
```

---

# Install Dependencies

```
pip install -r requirements.txt
```

---

# Run Backend Server

```
uvicorn backend.main:app --reload
```

Backend will start at:

```
http://127.0.0.1:8000
```

---

# Run Frontend

Open:

```
frontend/index.html
```

in a browser.

---

# Example Questions

```
What is Pikachu?
Tell me about Bulbasaur
How is Pikachu different from Charizard?
```

---

# How It Works

1. User asks a question in the chat interface
2. Backend receives the request via FastAPI
3. Pokémon name is detected
4. Pokémon data is fetched from PokeAPI
5. Data is passed to the local LLM via Ollama
6. AI generates a conversational response

---

# Future Improvements

- Pokémon comparison feature
- Better entity detection
- Improved conversation memory
- Streaming AI responses
