import streamlit as st
import numpy as np
import pickle

# Load trained model
model = pickle.load(open("house_model.pkl", "rb"))

st.title("🏠 House Price Prediction using Linear Regression")
st.write("Enter the property details below to predict the house price.")

# Input fields
storey = st.number_input("Storey (Floor Number)", 1, 50, 5)
area = st.number_input("Built-up Area (sq. ft.)", 200, 10000, 1200)
location_grade = st.selectbox("Location Grade", ["Poor", "Average", "Good", "Very Good", "Premium"])
view_quality = st.selectbox("View Quality", ["Bad", "Average", "Good", "Very Good", "Excellent"])
facilities = st.slider("Facilities Rating (1–5)", 1, 5, 3)
house_age = st.number_input("Age of House (Years)", 0, 60, 10)

# Encode categories
location_map = {"Poor":1, "Average":2, "Good":3, "Very Good":4, "Premium":5}
view_map = {"Bad":1, "Average":2, "Good":3, "Very Good":4, "Excellent":5}

loc_val = location_map[location_grade]
view_val = view_map[view_quality]

if st.button("Predict Price"):
    input_data = np.array([[storey, area, loc_val, view_val, facilities, house_age]])
    predicted_price = model.predict(input_data)[0]

    st.subheader("📌 Estimated House Price:")
    st.success(f"₹ {int(predicted_price):,}")
