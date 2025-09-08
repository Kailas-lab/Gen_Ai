

import streamlit as st
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
import os
import re

# Directly set API Key (for testing only)
os.environ["GOOGLE_API_KEY"] = ""

# Initialize Gemini Model
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.9)

# Streamlit UI
st.set_page_config(page_title="🍽️ Restaurant Name Generator", page_icon="🍴")
st.title("🍽️ Restaurant Name Generator (Gemini)")

# Sidebar cuisine selection
cuisine = st.sidebar.selectbox(
    "Pick a Cuisine", 
    ("Indian", "Italian", "Mexican", "Arabic", "American")
)

if st.button("Generate Restaurant"):
    if cuisine:
        prompt = f"""
        Suggest a creative restaurant name and 5 popular menu items for a {cuisine} cuisine.
        Format strictly as:
        Restaurant Name: <name>
        Menu Items: item1, item2, item3, item4, item5
        """

        response = llm.invoke([HumanMessage(content=prompt)])
        text = response.content.strip()

        # Try to extract restaurant name
        name_match = re.search(r"Restaurant Name:\s*(.*)", text)
        restaurant_name = name_match.group(1).strip() if name_match else "Unknown Restaurant"

        # Try to extract menu items
        menu_match = re.search(r"Menu Items:\s*(.*)", text)
        if menu_match:
            menu_items = [item.strip() for item in menu_match.group(1).split(",")]
        else:
            # fallback: collect bullet/line items if formatted differently
            lines = text.split("\n")
            menu_items = [line.strip("-• ").strip() for line in lines if line and ("item" in line.lower() or "•" in line or "-" in line)]

        # Display results
        st.header(restaurant_name)
        st.write("**Menu Items**")
        if menu_items:
            for item in menu_items:
                st.write("-", item)
        else:
            st.write("⚠️ No menu items found.")
