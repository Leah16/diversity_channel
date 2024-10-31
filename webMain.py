import streamlit as st
from packages.ETLPythonSidebar import ETLsidebar
from chatbot.chatbotMain import chatbotMain
# Layout
st.set_page_config(layout="wide")

# Logo
st.logo("Arts/dclogo.webp")

# Sidebar
ETLsidebar()

# Main page
chatbotMain()