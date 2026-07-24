import streamlit as st

# Custom CSS for Dynamic Animated Background, Text Formatting & Interactive Emojis
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
        background: linear-gradient(-45deg, #0f172a, #1e1b4b, #311042, #431407, #064e3b);
        background-size: 400% 400%;
        animation: gradientAnimation 15s ease infinite;
    }

    /* 2. Interactive Animated Emojis */
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
    .stSlider label, .stTextArea label, .stRadio label, .stCheckbox label {
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

    /* 5. JSON Output display (Black Text on White Background) */
    div[data-testid="stJson"] {
        background-color: #ffffff !important;
        border-radius: 10px;
        padding: 10px;
    }
    
    div[data-testid="stJson"] * {
        color: #111827 !important;
    }

    /* Custom Button Styling */
    .stButton > button {
        width: 100%;
        background: linear-gradient(90deg, #ff7e5f 0%, #feb47b 100%) !important;
        color: #ffffff !important;
        font-weight: bold !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 12px 24px !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0px 8px 20px rgba(255, 126, 95, 0.4);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App Title with Interactive Emoji
st.markdown("<h1><span class='interactive-emoji'>🍕</span> Online Food Ordering App</h1>", unsafe_allow_html=True)

# Input Widgets
name = st.text_input("Enter Customer Name")

restaurant = st.selectbox(
    "Select Restaurant", 
    ["8th Day Café & Bakery", "Roastery Coffee House", "Flurys (Park Street)", "Potboiler Coffee House", "Cafe AD-91"]
)

selected_food = st.multiselect(
    "Select food to be ordered", 
    [
        "Avocado Toast",
        "Club Sandwich",
        "Breakfast Burrito",
        "Caprese Panini",
        "Bagel with Smoked Salmon",
        "Açaí Bowl",
        "Quinoa & Roasted Veggie Salad",
        "Almond Croissant",
        "Spinach & Feta Danish",
        "Banana Bread"
    ]
)

# Individual quantity sliders for each selected food item
food_quantities = {}
if selected_food:
    st.markdown("### <span class='interactive-emoji'>📊</span> Select Quantity for Each Item", unsafe_allow_html=True)
    for item in selected_food:
        qty = st.slider(f"Quantity for {item}", min_value=1, max_value=10, value=1, key=item)
        food_quantities[item] = qty

delivery_instructions = st.text_area("Enter Delivery Instructions")

payment = st.radio(
    "Choose Payment Method",
    ["Cash on Delivery", "Credit Card", "Debit Card", "UPI"]
)

confirm_order = st.checkbox("I confirm that the above order details are correct.")

# Button & Output
if st.button("Place Order"):
    if confirm_order:
        if not selected_food:
            st.error("⚠️ Please select at least one food item.")
        else:
            st.markdown("### <span class='interactive-emoji'>🎉</span> Order Placed Successfully!", unsafe_allow_html=True)
            
            # Consolidate order details into a single dictionary
            order_details = {
                "Customer Name": name,
                "Restaurant": restaurant,
                "Food Items & Quantities": food_quantities,
                "Delivery Instructions": delivery_instructions,
                "Payment Method": payment
            }
            
            # Display output JSON on light background with black text
            st.json(order_details)
    else:
        st.warning("⚠️ Please confirm your order details before placing the order.")