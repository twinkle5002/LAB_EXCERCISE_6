import streamlit as st

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
        background: linear-gradient(-45deg, #0f172a, #1e1b4b, #311042, #064e3b, #1e3a8a);
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

    .stTextInput label, .stSelectbox label, .stMultiSelect label, 
    .stSlider label, .stTextArea label, .stRadio label, .stCheckbox label, .stFileUploader label {
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

    /* 4. Inputs, Dropdowns, Text Areas, and Menus (White Background -> Dark Text) */
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

    /* 5. Custom Styling for Metrics & Info Boxes */
    div[data-testid="stMetricValue"] {
        color: #38bdf8 !important;
        font-size: 2rem !important;
    }

    /* Custom Button Styling */
    .stButton > button {
        width: 100%;
        background: linear-gradient(90deg, #3b82f6 0%, #8b5cf6 100%) !important;
        color: #ffffff !important;
        font-weight: bold !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 12px 24px !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0px 8px 20px rgba(59, 130, 246, 0.4);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App Title with Interactive Emoji
st.markdown("<h1><span class='interactive-emoji'>💼</span> Employee Feedback System</h1>", unsafe_allow_html=True)

# Input Widgets
emp_id = st.text_input("Enter Employee ID")
emp_name = st.text_input("Enter Employee Name")

department = st.selectbox(
    "Select Department",
    ["Human Resources", "Engineering", "Product", "Marketing", "Sales", "Finance"]
)

satisfaction = st.slider(
    "Rate Workplace Satisfaction (1 = Poor, 10 = Excellent)",
    min_value=1,
    max_value=10,
    value=5
)

facilities = st.multiselect(
    "Select Facilities Used",
    ["Cafeteria", "Gymnasium", "Transport Service", "Game Room", "Library", "Medical Room"]
)

# Individual satisfaction sliders for each selected facility
facility_ratings = {}
if facilities:
    st.markdown("### <span class='interactive-emoji'>⭐</span> Rate Selected Facilities", unsafe_allow_html=True)
    for facility in facilities:
        rating = st.slider(
            f"Satisfaction with {facility} (1-5)",
            min_value=1,
            max_value=5,
            value=3,
            key=facility
        )
        facility_ratings[facility] = rating

improvements = st.text_area("Recommend Improvements")

document = st.file_uploader(
    "Upload Supporting Document (Optional)",
    type=["pdf", "docx", "png", "jpg"]
)

# Submit Button & Output Display
if st.button("Submit Feedback"):
    if not emp_id or not emp_name:
        st.warning("⚠️ Please provide both your Employee ID and Employee Name before submitting.")
    else:
        # Success Information Block using st.info()
        st.info("✅ Thank you! Your feedback has been submitted successfully.")
        
        st.markdown("### <span class='interactive-emoji'>📊</span> Feedback Summary", unsafe_allow_html=True)
        
        # Display workplace satisfaction score using st.metric()
        st.metric(label="Overall Workplace Satisfaction Score", value=f"{satisfaction} / 10")
        
        # Display detailed feedback using st.write()
        st.write("---")
        st.write("**Employee ID:**", emp_id)
        st.write("**Employee Name:**", emp_name)
        st.write("**Department:**", department)
        st.write("**Facilities Used & Ratings:**", facility_ratings if facility_ratings else "None selected")
        st.write("**Recommended Improvements:**", improvements if improvements else "N/A")
        
        if document is not None:
            st.write("**Uploaded Document:**", document.name)