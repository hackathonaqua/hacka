import streamlit as st
import pandas as pd
import requests
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Sample historical soil moisture data for demonstration purposes
historical_data = {
    "Days": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Soil Humidity (%)": [30, 35, 34, 40, 38, 45, 44, 50, 52, 55],
}

# Convert to DataFrame
historical_df = pd.DataFrame(historical_data)

# Function to control sprinklers
def control_sprinklers(action):
    # Here, you'd typically send an HTTP request to the sprinkler controller
    url = "http://your_sprinkler_controller_api_endpoint"
    response = requests.post(url, json={"action": action})
    return response.status_code

# Function for predictive analytics
def predict_soil_humidity(df):
    X = df['Days'].values.reshape(-1, 1)  # Reshape for sklearn
    y = df['Soil Humidity (%)'].values
    
    model = LinearRegression()
    model.fit(X, y)
    
    # Predicting for the next 5 days
    future_days = np.array(range(len(df) + 1, len(df) + 6)).reshape(-1, 1)
    predictions = model.predict(future_days)
    
    return future_days.flatten(), predictions

# Streamlit UI
st.title("Smart Irrigation Management System")

st.header("Soil Moisture Profile")
st.write("Monitor soil data collected from the sensor network.")

# Display the soil data
soil_data = {
    "Soil Temperature (°C)": [20, 21, 22],
    "Soil Humidity (%)": [30, 35, 40],
    "Ambient Temperature (°C)": [25, 26, 27],
    "Ambient Humidity (%)": [50, 55, 60],
}
soil_df = pd.DataFrame(soil_data)
st.dataframe(soil_df)

# Planning the plantation cycle
st.header("Plantation Cycle Planning")
phase = st.selectbox("Select Growth Phase", ["Field Preparation", "Plantation", "Growth", "Harvest"])
if phase == "Field Preparation":
    st.write("Consider irrigation based on initial soil moisture levels.")
elif phase == "Plantation":
    st.write("Irrigation may be needed for seed germination.")
elif phase == "Growth":
    st.write("Monitor moisture levels frequently to maintain optimal conditions.")
elif phase == "Harvest":
    st.write("Minimize irrigation to prepare for harvest.")

# Sprinkler control section
st.header("Smart Sprinkler Control")
action = st.radio("Choose an action", ["START", "STOP"])
if st.button("Control Sprinkler"):
    status_code = control_sprinklers(action)
    if status_code == 200:
        st.success(f"Sprinkler action '{action}' executed successfully!")
    else:
        st.error("Failed to execute sprinkler action.")

# On-demand irrigation
st.header("On-Demand Irrigation")
if st.button("Irrigate Now"):
    control_sprinklers("START")
    st.success("Irrigation started on demand.")

if st.button("Stop Irrigation"):
    control_sprinklers("STOP")
    st.success("Irrigation stopped.")

# Predictive Analytics Section
st.header("Predictive Analytics for Soil Humidity")
future_days, predictions = predict_soil_humidity(historical_df)

# Plotting the historical data and predictions
plt.figure(figsize=(10, 5))
plt.plot(historical_df['Days'], historical_df['Soil Humidity (%)'], label='Historical Soil Humidity', marker='o')
plt.plot(future_days, predictions, label='Predicted Soil Humidity', marker='x', linestyle='--')
plt.xlabel("Days")
plt.ylabel("Soil Humidity (%)")
plt.title("Soil Humidity Prediction")
plt.xticks(np.arange(1, 16, 1))
plt.grid()
plt.legend()
st.pyplot(plt)

# Footer
st.write("This application helps farmers manage irrigation effectively using real-time data and predictive analytics.")
