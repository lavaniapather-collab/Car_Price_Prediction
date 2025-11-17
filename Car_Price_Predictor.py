import os
import pickle
import streamlit as st
import pandas as pd
import numpy as np

# Safe model path (works locally and on Streamlit Cloud)
model_path = os.path.join(os.path.dirname(__file__), "lr_model.pkl")

# Load the trained model
with open(model_path, "rb") as model_file:
    model = pickle.load(model_file)

# Streamlit App
st.set_page_config(page_title="Car Price Predictor", layout="centered")

st.title("🚗 Car Price Predictor")
st.markdown("### Predict the resale price of a car based on its features")

# User Inputs
present_price = st.number_input("Present Price (in Lakhs)", min_value=0.0, max_value=100.0, step=0.5)
kms_driven = st.number_input("Kms Driven", min_value=0, step=1000)
car_age = st.slider("Car Age (Years)", 0, 20, 5)
fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])
transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
seller_type = st.selectbox("Seller Type", ["Dealer", "Individual"])

# Encode categorical variables
fuel_type_petrol = 1 if fuel_type == "Petrol" else 0
fuel_type_diesel = 1 if fuel_type == "Diesel" else 0
fuel_type_cng = 1 if fuel_type == "CNG" else 0
transmission_manual = 1 if transmission == "Manual" else 0
transmission_auto = 1 if transmission == "Automatic" else 0

# Prepare data for prediction
input_data = pd.DataFrame({
    "Present_Price": [present_price],
    "Kms_Driven": [kms_driven],
    "Car_Age": [car_age],
    "Fuel_Type_CNG": [fuel_type_cng],
    "Fuel_Type_Diesel": [fuel_type_diesel],
    "Fuel_Type_Petrol": [fuel_type_petrol],
    "Transmission_Manual": [transmission_manual],
    "Transmission_Automatic": [transmission_auto],
})

# Prediction
if st.button("Predict Price"):
    prediction = model.predict(input_data)[0]
    st.success(f"💰 Estimated Selling Price: ₹{prediction:.2f} Lakhs")