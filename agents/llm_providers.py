from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from app.config import GOOGLE_API_KEY, GROQ_API_KEY,OPENAI_API_KEY
from langchain_google_genai import ChatGoogleGenerativeAI
def get_llm(provider, model):
    if provider == "Groq":
        if not GROQ_API_KEY:
            raise ValueError("GROQ_API_KEY not found in environment or config.py")
        return ChatGroq(model=model, api_key=GROQ_API_KEY)

    elif provider == "OpenAI":
        if not OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY not found in environment or config.py")
        return ChatOpenAI(model=model, api_key=OPENAI_API_KEY)
    elif provider == "GOOGLE":
        #print("Using Google Gemini model:", model)
        #print("GOOGLE_API_KEY:", GOOGLE_API_KEY)
        if not GOOGLE_API_KEY:
            raise ValueError("GOOGLE_API_KEY not found in environment or config.py")
        return ChatGoogleGenerativeAI(
        model=model,
        google_api_key=GOOGLE_API_KEY,
        temperature=0.7
        
    )
    
    else:
        raise ValueError(f"Unknown provider: {provider}")
