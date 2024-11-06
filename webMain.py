import streamlit as st
from packages.ETLPythonSidebar import ETLsidebar
from chatbot.chatbotMain import chatbotMain
# Layout
st.set_page_config(layout="wide")

# Logo
st.logo("arts/dclogo.webp")

# Sidebar
ETLsidebar()

# Main page
st.title("Welcome to ETL Diversity Channel")

st.write("This project is a collaboration between ETL, Sophia University and Diversity Channel Project, 2024.")

st.write("This website provides information about the education system in Japan, how to get medical care, and travel information in Japan.")

st.write("You can also use the chatbot to get information about Japan.")