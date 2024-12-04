import pandas as pd
import streamlit as st
import packages.etlPythonSidebar as sidebar
# Logo
st.logo("arts/dclogo.webp")

# Sidebar
sidebar.ETLsidebar()

# 主标题
st.header("The education system in Japan")

# 介绍部分
st.write("""School education in Japan starts with kindergarten for infants, and after completing nine years of compulsory education in elementary school (6 years) and junior high school (3 years), students move on to senior high school (3 years). In Japan, universities, junior colleges, and vocational schools are educational institutions for those who have graduated from high school (or those who have the same or higher academic ability) (Fig. 1).

Each of them has different duration and curriculum. Each school year starts in April, except for a few. Since many exams are held for April intake, you need to pay attention to the schedule.""")

# 1. 大学和短期大学部分
st.subheader("1. University (Under and Graduate schools), Junior college")
st.write("""Usually, the duration for a university is 4 years, and for junior college is 2 years. (As for graduate schools, 2 years for master's programs, 5 years for doctoral programs, and 2 years for professional degree programs.)All of them are divided into national, public (prefectural, municipal, etc.) and private schools, but the majority are private schools. Currently, about half of Japanese high school graduates go on to universities and junior colleges. As of May 1, 2012, of the 137,756 international students, 69,274 were enrolled in universities, 39,641 in graduate schools, and 1,603 in junior colleges.""")

# 大学方面
st.write("**Aspect of universities (and graduate schools)**")
st.write("""Four-year universities consist of faculties, which are broadly divided into the humanities (Faculty of Letters, Faculty of Foreign Languages, etc), social sciences (Faculty of Law, Faculty of Economics, Faculty of Commerce etc.), and natural sciences (Faculty of Science, Faculty of Engineering, Faculty of Agriculture etc.), with faculties further divided into departments (Department of English Literature, Department of Law, Department of Economics etc.). Graduate schools award "master's", "doctoral", and "professional" degrees according to these systems and departments. Universities usually require four years to graduate with a minimum of 124 credits, and a "bachelor's" degree is awarded upon graduation.""")

# 短期大学方面
st.write("**Aspect of Junior colleges**")
st.write("""Junior colleges consist of departments rather than faculties, and are divided into humanities (Japanese literature, English literature, etc.), social sciences (business, secretarial, etc.), liberal arts (liberal arts, international culture, etc.), industrial sciences (automotive, electrical, etc.), medical sciences (nursing, clinical engineering, etc.), education (early childhood education, child welfare, etc.), home economics (food and nutrition, fashion design, etc.), arts (fine arts, design, etc.), and others.

More than 62 credits are required to graduate. (In the case where duration is 3 years, it would be more than 93 credits.)

Upon graduation, students are awarded a "Junior College Degree".""")

# 2. 职业学校部分
st.subheader("2. Vocational schools")
st.write("""Vocational schools are positioned as institutions of higher education that provide "vocational education" with the approval of the prefectural governor.
As of May 1, 2012, there were 25,167 international students studying at vocational schools, and the number of students entering vocational schools in Japan exceeds the number entering junior colleges, giving them a solid position in society.""")

# 职业学校方面
st.write("**Aspect of vocational schools**")
st.write("""The purpose of vocational schools is to "cultivate vocational skills that are immediately useful in society," so they provide education that is closely linked to the occupation, and students learn the knowledge and skills necessary for the job.""")

# 创建职业学校教育领域表格
data = {
    "8 fields of Vocational Schools' education": [
        "Technology",
        "Business",
        "Medical Care",
        "Personal Care and Nutrition",
        "Culture and General Education",
        "Education and Welfare",
        "Fashion and Home Economics",
        "Agriculture"
    ],
    "Key Courses": [
        "Architecture, Civil engineering, Location survey, Construction, Electronic engineering, Electricity, Broadcasting, Communications, Automobile engineering, Mechanics, Information, computers, Air mechanics, etc.",
        "Bookkeeping, Accounting, Auditing, Management, Office administration, Tourism, Hotel service, Business, Medical office administration, etc.",
        "Nursing, Clinical assay, Clinical engineering, Medical radiations, Dental health, Dental engineering, Rehabilitation, Judo-orthopedics, Acupuncture, Moxacautery, etc.",
        "Nutrition, Culinary, Confectionary, Breadmaking, Barber, Beautician, Makeup, Esthetic, Nail, etc.",
        "Music, Fine arts, Sculpture, Design, Audio visual arts, Photography, Language, Interpreter, Veterinary, Animal Groomers, Civil servant, sports, etc.",
        "Child care, Early childhood education, Social welfare, Welfare caretaking, etc.",
        "Dressmaking, Fashion design, Japanese traditional dressmaking, Kimono, Fashion business, etc.",
        "Agriculture, Gardening, Landscaping, Bio technology, etc."
    ]
}

df = pd.DataFrame(data)
st.table(df)