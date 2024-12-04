# medical_care_page.py
import streamlit as st
import packages.etlPythonSidebar as sidebar

# Logo
st.logo("arts/dclogo.webp")

# Sidebar
sidebar.ETLsidebar()



st.title("How to Get Medical Care")

st.write("This page explains how to get medical care in Japan. When foreigners want to go to a hospital in Japan, they may not be able to get proper support from their company or school, even though they do not understand the language or the rules. Let's familiarize yourself with how to go to the hospital in advance.")

import streamlit as st

st.header("Types of medical institutions")

st.write("In Japan, when you feel sick, it is common to see a doctor at a clinic before going to a big hospital. It is useful to find a clinic near your home or office in case you get sick. If you need surgery or hospitalization, you can be referred to a small to medium-sized hospital or a major hospital, so go to a clinic first.")

st.markdown("""
* **Clinics:** In case of common illness or injury (colds, allergies, stomachaches, etc.)
* **Small and medium-sized hospitals:** In cases where surgery, hospitalization, or emergency medical care is required
* **Major hospitals:** For serious emergency patients, or advanced medical care
""")

st.subheader("Health insurance card")
st.write("Show your health insurance card at the medical institution. If you show your health insurance card, you can reduce the co-payment of your medical expenses.")

st.subheader("Clinical departments")
st.write("In Japan, medical institutions have various clinical departments according to the disease and injury.")

st.write("Here, we will tell you which department you should go to according to what kind of symptoms you have. If you do not know which department to go to, you should call and ask the hospital in advance.")

data = {
    "Department": [
        "Internal medicine",
        "Surgery",
        "Orthopedics",
        "Ophthalmology",
        "Dentistry",
        "Obstetrics",
        "Gynecology",
        "Dermatology",
        "Pediatrics"
    ],
    "Symptom": [
        "When you have a fever or a stomachache",
        "Cuts, fractures, or disorders that require surgery",
        "Pain in the lower back, knees, or shoulder joints",
        "When you have eye problems",
        "When you have a toothache from a cavity or other dental problem",
        "When you need medical attention for childbirth or pregnancy",
        "When there are symptoms related to diseases specific to women",
        "When you have a skin problem",
        "When a child is sick"
    ]
}

import pandas as pd
df = pd.DataFrame(data)

st.table(df)