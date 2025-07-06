# agent_assistant
🤖 Autonomous AI Research Assistant

A powerful, web-based AI agent that autonomously researches any given topic, synthesizes information from multiple sources, and generates a structured, well-sourced report. Built with Python, Streamlit, and LangChain.

## ✨ Features

* **Autonomous Web Research:** Utilizes the Tavily Search API to find relevant and up-to-date sources on any topic.
* **Intelligent Content Scraping:** Reads and extracts the main content from web pages, filtering out ads and boilerplate.
* **RAG (Retrieval-Augmented Generation) Core:** Creates a persistent vector knowledge base using ChromaDB and OpenAI Embeddings to "teach" the agent the information it finds.
* **AI-Powered Synthesis:** Uses GPT-4 to generate high-quality, coherent reports based on the collected and verified information.
* **Interactive UI:** A clean and professional user interface built with Streamlit, featuring a secure password-protected entry.
* **Animated Feedback:** Includes Lottie animations for a dynamic and engaging user experience during processing.

## 🚀 Live Demo

*[This section is reserved for your Streamlit Community Cloud app link once deployment is complete]*

## 🛠️ How to Set Up and Run Locally

Follow these steps to get the project running on your local machine.

**1. Clone the repository:**
```bash
git clone [https://github.com/CaganSevketoglu/AI-Proposal-Assistant.git](https://github.com/CaganSevketoglu/AI-Proposal-Assistant.git)
cd AI-Proposal-Assistant
2. Create and Activate a Virtual Environment:

Bash

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies:

Bash

pip install -r requirements.txt
(Note: You will need to create a requirements.txt file by running pip freeze > requirements.txt in your active terminal.)

4. Set Up API Keys:
Create a .streamlit/secrets.toml file in the root directory and add your keys:

Ini, TOML

OPENAI_API_KEY="sk-..."
TAVILY_API_KEY="tvly-..."
APP_PASSWORD="your_secret_password"
5. Run the Application:

Bash

streamlit run app.py

💻 Tech Stack
Language: Python

Framework: Streamlit

AI/LLM Orchestration: LangChain

Core AI Models: OpenAI (GPT-4, Embeddings)

Search: Tavily AI API

Vector Store: ChromaDB

Web Scraping: Requests, BeautifulSoup4

