import streamlit as st
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
import os

# Set API Key (make sure to keep it safe in real apps)
os.environ["GOOGLE_API_KEY"] = "AIzaSyDawUYRDIv0j94bMLOnvuTTNdkaZiwRqzM"

# Initialize Gemini Model
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.9)

# Streamlit UI
st.set_page_config(page_title="🤖 Gemini Chatbot", page_icon="💬")
st.title("🤖 Gemini Chatbot")

# User input
user_input = st.text_input("Type your message:")

if st.button("Ask Gemini"):
    if user_input.strip() != "":
        response = llm.invoke([HumanMessage(content=user_input)])
        st.write("**Gemini:**", response.content)
