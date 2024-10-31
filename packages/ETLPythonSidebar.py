import streamlit as st

def ETLsidebar():
    with st.sidebar:
        # Home
        st.page_link("webMain.py", label="Home", icon="🏠")
        # Tabs
        education_tabs, healthCare_tabs, travelInfo_tabs = st.tabs(["Education", "Healthcare", "Travel"])

        # Footer
        st.divider()
        footer_html = """<div style='text-align: center;'>
        <p>ETL, Sophia University</p>
        </div>"""
        st.markdown(footer_html, unsafe_allow_html=True)
        footer_html = """<div style='text-align: center;'>
        <p>Diversity Channel Project, 2024</p>
        </div>"""
        st.markdown(footer_html, unsafe_allow_html=True)

    with education_tabs:
        
        st.page_link("pages/example_one.py", label="First page", icon="🔥")
        st.page_link("pages/example_two.py", label="Second page", icon="🔥")
