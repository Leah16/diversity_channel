import streamlit as st
import packages.etlPythonSidebar as sidebar
from packages.chatbotWeb import chatbotMain

# Logo
st.logo("arts/dclogo.webp")

# Sidebar
sidebar.ETLsidebar()

chatbotMain()