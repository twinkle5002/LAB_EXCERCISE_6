import streamlit as st

st.title("Student Registration Portal")

# Input Widgets
name = st.text_input("Enter Student Name")
age = st.number_input("Enter age")
gender = st.radio(
    "Select Gender",
    ["Male", "Female", "Transgender"]
)

department = st.selectbox(
    "Select Department", 
    ["BCA", "B.Sc CS", "B.Tech AI", "MCA"]
)

subjects = st.multiselect(
    "Select subject", 
    ["Python", "Data Science", "Machine Learning", "Cyber Security", "Cloud Computing"]
)

admission_date = st.date_input("Admission Date")

photo = st.file_uploader(
    "Upload Passport Size Photo", 
    type=["jpg", "jpeg", "png"]
)

# Button
if st.button("Register"):
    st.success("Registration Successful!")
    st.write("### Student Details")
    st.write("**Student Name:**", name)
    st.write("**Age:**", age)
    st.write("**Gender:**", gender)
    st.write("**Department:**", department)
    st.write("**Subjects Selected:**", subjects)
    st.write("**Admission Date:**", admission_date)

    if photo is not None:
        st.image(photo, width=150)