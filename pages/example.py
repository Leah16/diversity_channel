import streamlit as st
import packages.etlPythonSidebar as sidebar

# Logo
st.logo("arts/dclogo.webp")

# Sidebar
sidebar.ETLsidebar()

st.title("Example")
st.write("This is the example page")