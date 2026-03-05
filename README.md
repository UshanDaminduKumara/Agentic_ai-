# End-to-End AI Agent Chatbot

A production-ready, modular AI chatbot built with **FastAPI** (Backend), **Streamlit** (Frontend), and **LangGraph** (AI Orchestration). This project supports switching between LLM providers (Groq/OpenAI) and includes a web-search tool for real-time information.

## 🚀 Features
- **Multi-Model Support:** Switch between Groq (Llama 3) and OpenAI (GPT-4o mini).
- **Web Search Integration:** Uses Tavly API for real-time information retrieval.
- **Modular Architecture:** Clean separation between AI logic, API routing, and UI.
- **Interactive UI:** Dynamic sidebar for model configuration and system prompt customization.

---

## 🛠️ Tech Stack
- **Frameworks:** FastAPI, LangGraph, LangChain
- **Frontend:** Streamlit
- **LLM Providers:** Groq, OpenAI
- **Search Tool:** Tavly AI

---

## 📁 Project Structure
```text
├── agents/
│   ├── llm_provider.py    # LLM initialization logic
│   ├── tools.py           # Search tool configuration
│   └── ai_agents.py       # LangGraph React Agent logic
├── app/
│   ├── config.py          # API key & environment management
│   ├── models.py          # Pydantic schemas for data validation
│   └── route.py           # FastAPI chat endpoints
├── front_end/
│   └── app.py             # Streamlit interface
├── main.py                # Backend entry point (Uvicorn)
├── requirements.txt       # Dependencies
└── .env                   # API Keys (GitIgnored)