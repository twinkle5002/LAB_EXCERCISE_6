import streamlit as st

st.title("Online Food Ordering App")

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
        st.success("Order Placed Successfully!")
        
        # Consolidate all order details into a single dictionary
        order_details = {
            "Customer Name": name,
            "Restaurant": restaurant,
            "Food Items": food,
            "Quantity": quantity,
            "Delivery Instructions": delivery_instructions,
            "Payment Method": payment
        }
        
        # Display the single JSON object
        st.json(order_details)
    else:
        st.warning("Please confirm your order details before placing the order.")
