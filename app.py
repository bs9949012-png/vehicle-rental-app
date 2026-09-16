import streamlit as st

st.title("Vehicle Rental - Add a Vehicle")

if "vehicles" not in st.session_state:
    st.session_state.vehicles = []

name = st.text_input("Vehicle name")
vtype = st.selectbox("Vehicle type", ["Car", "Bike", "Scooter"])
price = st.number_input("Price per day (₹)", min_value=0)
city = st.text_input("City")

if st.button("Add Vehicle"):
    if name and city:
        st.session_state.vehicles.append({
            "name": name, "type": vtype, "price": price, "city": city
        })

st.write("### Available Vehicles")

st.write("#### Filter")
filter_city = st.text_input("Filter by city (leave blank for all)")
filter_type = st.selectbox("Filter by type", ["All", "Car", "Bike", "Scooter"])

filtered = st.session_state.vehicles

if filter_city:
    filtered = [v for v in filtered if v["city"].lower() == filter_city.lower()]

if filter_type != "All":
    filtered = [v for v in filtered if v["type"] == filter_type]

for v in filtered:
    st.write(f"{v['name']} ({v['type']}) - ₹{v['price']}/day - {v['city']}")