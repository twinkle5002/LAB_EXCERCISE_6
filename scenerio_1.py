import streamlit as st

st.title("Online Course Registration System")

# Input Widgets
name = st.text_input("Enter Student Name")
usn = st.text_input("Enter USN")

department = st.selectbox(
    "Select Department", 
    ["BCA", "B.Sc CS", "B.Tech AI", "MCA"]
)

courses = st.multiselect(
    "Select Courses", 
    ["Python", "Data Science", "Machine Learning", "Cyber Security", "Cloud Computing"]
)

timing = st.radio(
    "Preferred Class Timing", 
    ["Morning", "Evening"]
)

num_courses = st.number_input(
    "Number of Courses", 
    min_value=1, 
    max_value=5, 
    value=1
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
    st.write("**USN:**", usn)
    st.write("**Department:**", department)
    st.write("**Courses Selected:**", courses)
    st.write("**Preferred Timing:**", timing)
    st.write("**Number of Courses:**", num_courses)
    st.write("**Admission Date:**", admission_date)

    if photo is not None:
        st.image(photo, width=150)