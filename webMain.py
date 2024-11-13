import streamlit as st
from packages.ETLPythonSidebar import ETLsidebar

st.logo("arts/dclogo.webp")
# Page configuration
st.set_page_config(
    page_title="ETL Diversity Channel",
    page_icon="🌏",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar
ETLsidebar()

# Main content
st.title("Welcome to ETL Diversity Channel")

# Information card layout
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### 🎯 About the Project
    This project is a collaboration between ETL, Sophia University, and 
    Diversity Channel Project in 2024. We are dedicated to providing 
    comprehensive life information support for foreigners in Japan.
    """)
    
with col2:
    st.markdown("""
    ### 🌟 Key Features
    - 📚 Japanese Education System Guide
    - 🏥 Healthcare Information
    - 🗾 Travel Information
    - 🤖 AI Assistant
    """)

# Feature section
st.markdown("### 💡 Getting Started")
st.info("Please select a topic from the left sidebar menu or use our AI assistant for help.")

st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("""
---
<div style='text-align: center; color: #666;'>
    © 2024 ETL Diversity Channel Project. All rights reserved.
</div>
""", unsafe_allow_html=True)