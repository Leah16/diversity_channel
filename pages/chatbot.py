import streamlit as st
import packages.ETLPythonSidebar as sidebar
from packages.chatbotMain import chatbotMain

# Logo
st.logo("arts/dclogo.webp")

# Introduction
st.title("Japanese AI Assistant")
st.write("""
Meet Sakura, your friendly AI guide for all things Japan!
""")

# Sidebar
sidebar.ETLsidebar()

chatbotMain()