import os
import streamlit as st

def ETLsidebar():
    with st.sidebar:

        # 主导航 
        st.page_link("webMain.py", label="Home", icon="🏠")
        st.page_link("pages/chatbot.py", label="Chatbot", icon="💬")
        st.page_link("pages/rag.py", label="Knowledge Base", icon="📚")
        
        # Tabs
        education_tabs, healthCare_tabs, travelInfo_tabs, misc_tabs = st.tabs([
            "📚 Education",
            "🏥 Healthcare",
            "✈️ Travel",
            "📌 Misc"
        ])

        # Footer
        st.divider
        footer_html = """<div style='text-align: center;'>
        <p>ETL, Sophia University</p>
        </div>"""
        st.markdown(footer_html, unsafe_allow_html=True)
        footer_html = """<div style='text-align: center;'>
        <p>Diversity Channel Project, 2024</p>
        </div>"""
        st.markdown(footer_html, unsafe_allow_html=True)

    with education_tabs:
        create_page_link("The_education_system_in_Japan")
        create_page_link("example")
    with healthCare_tabs:
        create_page_link("How_To_Get_Medicial_Care")
        create_page_link("example")
    with travelInfo_tabs:
        create_page_link("example")
    with misc_tabs:
        create_page_link("example")

def create_page_link(fileName):
    file_path = f"pages/{fileName}.py"
    label = fileName.replace("_", " ").title()
    st.page_link(file_path, label=label, icon="🔥")
    
