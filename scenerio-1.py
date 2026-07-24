import streamlit as st
import pandas as pd

# Custom CSS for Animated Moving Gradient Background, Smart Text Formatting & Interactive Emojis
st.markdown(
    """
    <style>
    /* 1. Animated Moving Gradient Background */
    @keyframes gradientAnimation {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .stApp {
        background: linear-gradient(-45deg, #0f172a, #1e3a8a, #311042, #047857, #1e1b4b);
        background-size: 400% 400%;
        animation: gradientAnimation 15s ease infinite;
    }

    /* 2. Interactive Bouncing Emojis */
    @keyframes subtlePulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.15); }
    }

    .interactive-emoji {
        display: inline-block;
        transition: transform 0.3s ease;
        animation: subtlePulse 2.5s infinite;
        cursor: pointer;
    }

    .interactive-emoji:hover {
        transform: scale(1.4) rotate(12deg);
    }

    /* 3. Outer Page Text & Labels -> Bright White */
    body, p, span, label, div, h1, h2, h3, h4, h5, h6, .stMarkdown {
        color: #ffffff !important;
    }

    .stTextInput label, .stNumberInput label, .stRadio label, 
    .stSelectbox label, .stMultiSelect label, .stDateInput label, 
    .stFileUploader label {
        color: #ffffff !important;
        font-weight: 600 !important;
    }

    /* Title Styling */
    h1 {
        color: #ffffff !important;
        font-weight: 800 !important;
        text-align: center;
        margin-bottom: 30px !important;
        text-shadow: 0px 2px 10px rgba(255, 255, 255, 0.3);
    }

    /* Glassmorphism Container Panel */
    div[data-testid="stVerticalBlock"] > div {
        background-color: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.15);
        padding: 20px;
        border-radius: 15px;
        backdrop-filter: blur(10px);
    }

    /* 4. Inputs, Dropdowns, Date Input, and Menus (White Background -> Dark Text) */
    input, textarea, [data-baseweb="select"] {
        background-color: #ffffff !important;
        color: #111827 !important;
        border-radius: 8px !important;
    }

    /* Dropdown Menu Items & Selected Options */
    [data-baseweb="popover"], [data-baseweb="menu"], [role="option"] {
        background-color: #ffffff !important;
        color: #111827 !important;
    }
    
    [role="option"] * {
        color: #111827 !important;
    }

    /* Multiselect Tags/Badges */
    [data-baseweb="tag"] {
        background-color: #e2e8f0 !important;
        color: #0f172a !important;
    }
    [data-baseweb="tag"] * {
        color: #0f172a !important;
    }

    /* 5. Table Output Display (White Background -> Dark Text) */
    div[data-testid="stTable"] {
        background-color: #ffffff !important;
        border-radius: 10px;
        padding: 10px;
    }
    
    div[data-testid="stTable"] * {
        color: #111827 !important;
    }

    /* Custom Button Styling */
    .stButton > button {
        width: 100%;
        background: linear-gradient(90deg, #10b981 0%, #3b82f6 100%) !important;
        color: #ffffff !important;
        font-weight: bold !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 12px 24px !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0px 8px 20px rgba(16, 185, 129, 0.4);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App Title with Interactive Emoji
st.markdown("<h1><span class='interactive-emoji'>🎓</span> Student Registration Portal</h1>", unsafe_allow_html=True)

# Input Widgets
name = st.text_input("Enter Student Name")

age = st.number_input(
    "Enter Age",
    min_value=1,
    max_value=100,
    value=18
)

gender = st.radio(
    "Select Gender",
    ["Male", "Female", "Transgender"]
)

department = st.selectbox(
    "Select Department",
    ["BCA", "B.Sc CS", "B.Tech AI", "MCA"]
)

subjects = st.multiselect(
    "Select Subjects",
    ["Python", "Data Science", "Machine Learning", "Cyber Security", "Cloud Computing"]
)

admission_date = st.date_input("Date of Admission")

photo = st.file_uploader(
    "Upload Profile Photo",
    type=["jpg", "jpeg", "png"]
)

# Button & Registration Logic
if st.button("Register"):
    if not name:
        st.warning("⚠️ Please enter the student's name.")
    else:
        # Success Message
        st.success("🎉 Registration Successful!")
        
        st.markdown("### <span class='interactive-emoji'>📋</span> Student Details Summary", unsafe_allow_html=True)
        
        # Format details into a Pandas DataFrame for st.table()
        details = {
            "Field": ["Student Name", "Age", "Gender", "Department", "Subjects Selected", "Admission Date"],
            "Information": [
                name,
                str(age),
                gender,
                department,
                ", ".join(subjects) if subjects else "None Selected",
                str(admission_date)
            ]
        }
        
        df = pd.DataFrame(details)
        
        # Display summary in table format
        st.table(df)
        
        # Display Profile Photo if uploaded
        if photo is not None:
            st.markdown("### <span class='interactive-emoji'>🖼️</span> Profile Photo", unsafe_allow_html=True)
            st.image(photo, width=150)