import streamlit as st
import packages.ETLPythonSidebar as sidebar
from chatbot.chatbotMain import chatbotMain
# Logo
st.logo("arts/dclogo.webp")

# Sidebar
sidebar.ETLsidebar()

st.title("Chatbot")

st.write("This is the chatbot page")

chatbotMain()