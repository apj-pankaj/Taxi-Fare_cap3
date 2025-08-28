import streamlit as st
import pandas as pd
import joblib


model = joblib.load(r"D:\DS ML&AI\Capstone3\env\Scripts\linear_model.pkl")

st.title("Taxi Fare Calculation")
st.divider()
st.markdown("Enter trip details below:")
st.divider()


fare_amount = st.number_input("Base Fare Amount", min_value=0.0, format="%0.2f")
trip_duration = st.number_input("Trip Duration minutes", min_value=0.0, format="%0.2f")
pickup_hour = st.number_input("Pickup hour",  min_value=1, max_value=24)
tip_amount = st.number_input("Tip Amoount", min_value=0.0, format="%0.2f")
trip_distance = st.number_input("Trip Distance", min_value=0.0, format="%.2f")
tolls_amount = st.number_input("Tolls Amount", min_value=0.0, format="%.2f")
passenger_count = st.number_input("Passenger Count", min_value=1,max_value=5, step=1)
is_night = st.selectbox("Is late Night", ['1','0'])
st.divider()
if st.button("Calculate Fare"):
    user_input = pd.DataFrame([{
        "fare_amount": fare_amount,
        "trip_duration": trip_duration,
        "pickup_hour":pickup_hour,
        "tip_amount":tip_amount,
        "trip_distance": trip_distance,
        "tolls_amount":tolls_amount,
        "passenger_count": passenger_count,
        "is_night":is_night    
     
    }])

    fare_pred = model.predict(user_input)
    total_fare = fare_pred[0]
    st.divider()
    st.success(f"Estimated Total Amount: Rs{total_fare:.2f}")
