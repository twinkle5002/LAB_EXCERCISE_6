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
        background: linear-gradient(-45deg, #1e1b4b, #311042, #831843, #701a75, #0f172a);
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
    .stRadio label, .stNumberInput label, .stSelectSlider label, .stCheckbox label {
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

    /* Custom Button Styling */
    .stButton > button {
        width: 100%;
        background: linear-gradient(90deg, #ec4899 0%, #8b5cf6 100%) !important;
        color: #ffffff !important;
        font-weight: bold !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 12px 24px !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0px 8px 20px rgba(236, 72, 153, 0.4);
    }

    /* Container for Markdown Output Box */
    .booking-summary {
        background-color: #ffffff !important;
        color: #111827 !important;
        padding: 20px;
        border-radius: 12px;
        margin-top: 15px;
    }
    .booking-summary * {
        color: #111827 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App Title with Interactive Emoji
st.markdown("<h1><span class='interactive-emoji'>🎬</span> Movie Ticket Booking System</h1>", unsafe_allow_html=True)

# Input Widgets
name = st.text_input("Enter Customer Name")

movie = st.selectbox(
    "Select Movie",
    ["Inception", "Interstellar", "The Dark Knight", "Avatar: The Way of Water", "Dune: Part Two"]
)

show_timing = st.radio(
    "Select Show Timing",
    ["10:00 AM (Morning)", "02:30 PM (Matinee)", "06:00 PM (Evening)", "09:30 PM (Night)"]
)

num_tickets = st.number_input(
    "Number of Tickets",
    min_value=1,
    max_value=10,
    value=1
)

seat_type = st.select_slider(
    "Select Seat Type",
    options=["Silver", "Gold", "Platinum", "Recliner"]
)

snacks = st.multiselect(
    "Choose Snacks",
    ["Popcorn (salted)", "Cheese Popcorn", "Nachos with Dip", "Coca-Cola", "Hot Dog", "Chocolates"]
)

agree_terms = st.checkbox("I agree to the Terms and Conditions.")

# Button & Booking Confirmation
if st.button("Book Ticket"):
    if not agree_terms:
        st.warning("⚠️ Please agree to the Terms and Conditions before booking your tickets.")
    elif not name:
        st.warning("⚠️ Please enter your name.")
    else:
        # Trigger confetti/balloons animation
        st.balloons()
        
        # Display Success Message
        st.success("🎉 Ticket Booking Confirmed!")
        
        # Display booking details using formatted markdown inside a white-card block
        summary_html = f"""
        <div class="booking-summary">
            <h3><span class="interactive-emoji">🎟️</span> Booking Details</h3>
            <p><strong>Customer Name:</strong> {name}</p>
            <p><strong>Movie:</strong> {movie}</p>
            <p><strong>Show Timing:</strong> {show_timing}</p>
            <p><strong>Number of Tickets:</strong> {num_tickets}</p>
            <p><strong>Seat Type:</strong> {seat_type}</p>
            <p><strong>Snacks Selected:</strong> {", ".join(snacks) if snacks else "None"}</p>
        </div>
        """
        st.markdown(summary_html, unsafe_allow_html=True)