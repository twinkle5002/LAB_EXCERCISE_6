import streamlit as st

# Custom CSS to force white text and high contrast
st.markdown(
    """
    <style>
    /* Gradient Background */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #311042 100%);
    }

    /* Force all standard text, headers, and markdown to white */
    body, p, span, label, div, h1, h2, h3, h4, h5, h6, .stMarkdown {
        color: #ffffff !important;
    }

    /* Widget Labels styling to ensure readability */
    .stTextInput label, .stSelectbox label, .stMultiSelect label, 
    .stSlider label, .stTextArea label, .stRadio label, .stCheckbox label {
        color: #ffffff !important;
        font-weight: 600 !important;
    }

    /* Glassmorphism Container */
    div[data-testid="stVerticalBlock"] > div {
        background-color: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.15);
        padding: 20px;
        border-radius: 15px;
        backdrop-filter: blur(10px);
    }

    /* Title Styling */
    h1 {
        color: #ffffff !important;
        font-weight: 800 !important;
        text-align: center;
        margin-bottom: 30px !important;
        text-shadow: 0px 2px 10px rgba(255, 255, 255, 0.2);
    }

    /* Input fields background & text */
    input, textarea, div[role="combobox"] {
        color: #ffffff !important;
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

st.title("🍕 Online Food Ordering App")

# Input Widgets
name = st.text_input("Enter Customer Name")

restaurant = st.selectbox(
    "Select Restaurant", 
    ["8th Day Café & Bakery", "Roastery Coffee House", "Flurys (Park Street)", "Potboiler Coffee House", "Cafe AD-91"]
)

food = st.multiselect(
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

quantity = st.slider("Select Quantity", 1, 10, 1) 

delivery_instructions = st.text_area("Enter Delivery Instructions")

payment = st.radio(
    "Choose Payment Method",
    ["Cash on Delivery", "Credit Card", "Debit Card", "UPI"]
)

confirm_order = st.checkbox("I confirm that the above order details are correct.")

# Button
if st.button("Place Order"):
    if confirm_order:
        st.success("🎉 Order Placed Successfully!")
        
        # Consolidate details into a single dictionary
        order_details = {
            "Customer Name": name,
            "Restaurant": restaurant,
            "Food Items": food,
            "Quantity": quantity,
            "Delivery Instructions": delivery_instructions,
            "Payment Method": payment
        }
        
        # Display as a single JSON view
        st.json(order_details)
    else:
        st.warning("⚠️ Please confirm your order details before placing the order.")