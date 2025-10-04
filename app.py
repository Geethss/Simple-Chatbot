import os
import streamlit as st
from google import genai
from typing import List, Dict
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Gemini Q&A", layout="centered")

st.title("Conversational Q&A Bot 🤖")
st.write("This bot remembers your conversation. Ask it anything!")

api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    st.error("GEMINI_API_KEY environment variable not set. Please set it to run this app.")
    st.stop()

try:
    client = genai.Client(api_key=api_key)
except Exception as e:
    st.error(f"Error initializing Gemini client: {e}")
    st.stop()


with st.sidebar:
    st.header("⚙️ Settings")
    model_name = st.selectbox(
        "Gemini model",
        options=["gemini-2.5-flash", "gemini-2.5-pro", "gemini-2.5-flash-lite"],
        index=0
    )
    max_tokens = st.slider("Max output tokens", 64, 2048, 512, step=64)
    temperature = st.slider("Temperature", 0.0, 1.0, 0.7, step=0.05)
    st.markdown("---")
    if st.button("Clear Conversation History"):
        st.session_state.history = []
        st.rerun()
    st.caption("Note: API key must be set in your environment.")


if "history" not in st.session_state:
    st.session_state.history: List[Dict[str, str]] = []

def call_gemini_stream(prompt_text: str, model_name: str, max_output_tokens: int, temperature: float, history: List[Dict[str, str]]):
    """
    Calls the Gemini API with the given prompt and conversation history.
    Returns a generator that yields response chunks for streaming.
    """
    try:
        conversation_context = ""
        for turn in history:
            conversation_context += f"User: {turn['q']}\nAssistant: {turn['a']}\n\n"
        
        full_prompt = conversation_context + f"User: {prompt_text}\nAssistant:"
        
        config = {
            "max_output_tokens": max_output_tokens,
            "temperature": temperature
        }
        
        response = client.models.generate_content(
            model=model_name,
            contents=full_prompt,
            config=config
        )
        

        if hasattr(response, 'text'):
            yield response.text
        elif hasattr(response, 'candidates') and response.candidates:
            for candidate in response.candidates:
                if hasattr(candidate, 'content') and hasattr(candidate.content, 'parts'):
                    for part in candidate.content.parts:
                        if hasattr(part, 'text'):
                            yield part.text
                elif hasattr(candidate, 'text'):
                    yield candidate.text
        else:
            yield str(response)
            
    except Exception as e:
        st.error(f"An error occurred while calling the Gemini API: {e}")
        yield ""


for turn in st.session_state.history:
    with st.chat_message("user"):
        st.markdown(turn["q"])
    with st.chat_message("assistant"):
        st.markdown(turn["a"])

if prompt := st.chat_input("Ask anything..."):
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_answer = ""
        
        for chunk in call_gemini_stream(
            prompt.strip(),
            model_name=model_name,
            max_output_tokens=max_tokens,
            temperature=temperature,
            history=st.session_state.history
        ):
            full_answer += chunk
            response_placeholder.markdown(full_answer)

    if full_answer:
        st.session_state.history.append({"q": prompt.strip(), "a": full_answer})
