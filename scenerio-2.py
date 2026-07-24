import streamlit as st

# Custom CSS for Dynamic Animated Background & Crisp White Text
st.markdown(
    """
    <style>
    /* Animated Moving Gradient Background */
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

    /* Force all standard text, headers, and markdown to white */
    body, p, span, label, div, h1, h2, h3, h4, h5, h6, .stMarkdown {
        color: #ffffff !important;
    }

    /* Widget Labels styling */
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
        text-shadow: 0px 2px 10px rgba(255, 255, 255, 0.3);
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
    st.markdown("### 📊 Select Quantity for Each Item")
    for item in selected_food:
        qty = st.slider(f"Quantity for {item}", min_value=1, max_value=10, value=1, key=item)
        food_quantities[item] = qty

delivery_instructions = st.text_area("Enter Delivery Instructions")

payment = st.radio(
    "Choose Payment Method",
    ["Cash on Delivery", "Credit Card", "Debit Card", "UPI"]
)

confirm_order = st.checkbox("I confirm that the above order details are correct.")

# Button
if st.button("Place Order"):
    if confirm_order:
        if not selected_food:
            st.error("⚠️ Please select at least one food item.")
        else:
            st.success("🎉 Order Placed Successfully!")
            
            # Consolidate order details into a single dictionary
            order_details = {
                "Customer Name": name,
                "Restaurant": restaurant,
                "Food Items & Quantities": food_quantities,
                "Delivery Instructions": delivery_instructions,
                "Payment Method": payment
            }
            
            # Display single JSON output
            st.json(order_details)
    else:
        st.warning("⚠️ Please confirm your order details before placing the order.")