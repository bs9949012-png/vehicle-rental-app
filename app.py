import streamlit as st

st.title("Vehicle Rental App")

if "vehicles" not in st.session_state:
    st.session_state.vehicles = []

if "bookings" not in st.session_state:
    st.session_state.bookings = []

if "username" not in st.session_state:
    st.session_state.username = ""

if not st.session_state.username:
    st.write("## Login")
    entered_name = st.text_input("Enter your name to continue")
    if st.button("Login"):
        if entered_name:
            st.session_state.username = entered_name
            st.rerun()
else:
    st.write(f"### Welcome, {st.session_state.username}!")

    st.write("## Add a Vehicle")
    name = st.text_input("Vehicle name")
    vtype = st.selectbox("Vehicle type", ["Car", "Bike", "Scooter"])
    price = st.number_input("Price per day (₹)", min_value=0)
    city = st.text_input("City")

    if st.button("Add Vehicle"):
        if name and city:
            st.session_state.vehicles.append({
                "name": name, "type": vtype, "price": price, "city": city
            })

    st.write("## Available Vehicles")

    filter_city = st.text_input("Filter by city (leave blank for all)")
    filter_type = st.selectbox("Filter by type", ["All", "Car", "Bike", "Scooter"])

    filtered = st.session_state.vehicles
    if filter_city:
        filtered = [v for v in filtered if v["city"].lower() == filter_city.lower()]
    if filter_type != "All":
        filtered = [v for v in filtered if v["type"] == filter_type]

    for i, v in enumerate(filtered):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(f"{v['name']} ({v['type']}) - ₹{v['price']}/day - {v['city']}")
        with col2:
            if st.button("Book Now", key=f"book_{i}"):
                st.session_state.bookings.append(v)
                st.success(f"Booked {v['name']}!")

    st.write("## My Bookings")
    for b in st.session_state.bookings:
        st.write(f"{b['name']} ({b['type']}) - ₹{b['price']}/day - {b['city']}")