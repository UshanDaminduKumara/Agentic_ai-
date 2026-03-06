import streamlit as st
import requests
# Modern clean UI styling
st.markdown("""
    <style>
        /* User bubble */
        div[data-testid="stChatMessage"] .user {
            background-color: #ffffff22 !important;
            border: 1px solid #a5d6a7 !important;
            border-radius: 12px !important;
            padding: 12px !important;
        }

        /* AI bubble */
        div[data-testid="stChatMessage"] .assistant {
            background-color: #dcedc8aa !important;
            border: 1px solid #81c784 !important;
            border-radius: 12px !important;
            padding: 12px !important;
        }

        /* Sidebar background */
        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #a5d6a7, #c8e6c9);
        }

        
    </style>
""", unsafe_allow_html=True)



st.set_page_config(page_title="AI Agent Chatbot", layout="centered")

st.title("AI Agent Chatbot")
st.markdown("Chat with powerful LLMs like Groq LLaMA3 and OpenAI GPT-4 with optional web search!")

# Sidebar form for input configuration
with st.sidebar:
    st.header("Agent Configuration")
    
    model_provider = st.selectbox("Model Provider", ["GOOGLE","Groq","OpenAI"])
    
    model_name = st.selectbox(
        "Model Name",
        ["gemini-2.5-flash-lite","llama-3.1-8b-instant","gpt-4o-mini"]
    )
    
    system_prompt = st.text_area(
        "System Prompt", 
        value="Act as an AI chatbot who is smart and friendly", 
        height=100
    )
    
    allow_search = st.checkbox("Enable Web Search Tool", value=False)

# Session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
for role, msg in st.session_state.chat_history:
    if role == "user":
        with st.chat_message("user"):
            st.markdown(msg)
    else:
        with st.chat_message("ai"):
            st.markdown(msg)

# Handle user input
user_query = st.chat_input("Type your message...")

if user_query:
    # Display user message
    with st.chat_message("user"):
        st.markdown(user_query)
    st.session_state.chat_history.append(("user", user_query))

    # Send request to FastAPI backend
    with st.chat_message("ai"):
        with st.spinner("Thinking..."):
            try:
                payload = {
                    "model_name": model_name,
                    "model_provider": model_provider,
                    "system_prompt": system_prompt,
                    "messages": [user_query],
                    "allow_search": allow_search
                }
                res = requests.post("http://127.0.0.1:8000/chat", json=payload)
                response = res.json()
                st.markdown(response)
                st.session_state.chat_history.append(("ai", response))
            except Exception as e:
                st.error(f"Error: {e}")