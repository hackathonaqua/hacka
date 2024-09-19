import streamlit as st
import pandas as pd
import requests
import numpy as np
import plotly.graph_objs as go

pip install plotly

# Sample data for demonstration purposes
soil_data = {
    "Soil Temperature (°C)": [20, 21, 22, 23, 24, 22, 21],
    "Soil Humidity (%)": [30, 35, 40, 32, 38, 36, 34],
    "Ambient Temperature (°C)": [25, 26, 27, 28, 29, 30, 31],
    "Ambient Humidity (%)": [50, 55, 60, 58, 56, 54, 52],
}

# Function to control sprinklers
def control_sprinklers(action):
    url = "http://your_sprinkler_controller_api_endpoint"
    response = requests.post(url, json={"action": action})
    return response.status_code

# Function to fetch weather forecast (placeholder)
def get_weather_forecast():
    return {
        "Temperature (°C)": 28,
        "Humidity (%)": 60,
        "Rain Probability (%)": 20
    }

# Function to suggest crops based on soil conditions
def suggest_crop(soil_humidity):
    return "Wheat" if soil_humidity < 40 else "Paddy"

# Streamlit UI
st.title("Smart Irrigation Management System")

st.header("Soil Moisture Profile")
st.write("Monitor soil data collected from the sensor network.")
soil_df = pd.DataFrame(soil_data)
st.dataframe(soil_df)

# Visualize soil temperature and humidity
fig_temp = go.Figure()
fig_temp.add_trace(go.Scatter(x=soil_df.index, y=soil_df["Soil Temperature (°C)"], mode='lines+markers', name='Soil Temperature (°C)', line=dict(color='blue')))
fig_temp.add_trace(go.Scatter(x=soil_df.index, y=soil_df["Soil Humidity (%)"], mode='lines+markers', name='Soil Humidity (%)', line=dict(color='green')))
fig_temp.update_layout(title='Soil Temperature and Humidity Over Time', xaxis_title='Time (Days)', yaxis_title='Value', legend=dict(x=0, y=1))
st.plotly_chart(fig_temp)

# Gathering Soil
st.header("Gathering Soil Data")
soil_sample = st.text_input("Enter soil sample ID", "")

# Analyzing Soil
if st.button("Analyze Soil"):
    st.success("Soil analyzed successfully! Data recorded.")

# Separate the data
st.header("Soil Data Summary")
soil_temperature = soil_df["Soil Temperature (°C)"].mean()
soil_humidity = soil_df["Soil Humidity (%)"].mean()
ambient_temperature = soil_df["Ambient Temperature (°C)"].mean()
ambient_humidity = soil_df["Ambient Humidity (%)"].mean()

st.write(f"Average Soil Temperature: {soil_temperature:.2f} °C")
st.write(f"Average Soil Humidity: {soil_humidity:.2f} %")
st.write(f"Average Ambient Temperature: {ambient_temperature:.2f} °C")
st.write(f"Average Ambient Humidity: {ambient_humidity:.2f} %")

# Weather Forecast
st.header("Weather Forecast")
weather = get_weather_forecast()
st.write(f"Temperature: {weather['Temperature (°C)']} °C")
st.write(f"Humidity: {weather['Humidity (%)']} %")
st.write(f"Rain Probability: {weather['Rain Probability (%)']} %")

# Crop Forecast
st.header("Crop Forecast")
current_crop = st.selectbox("Select Current Crop", ["Paddy", "Wheat"])
suggested_crop = suggest_crop(soil_humidity)
st.write(f"Suggested Crop for Next Season: {suggested_crop}")

# Planning Phases
st.header("Planning Phases")
phase = st.selectbox("Select Phase", ["Field Preparation", "Plantation", "Growth", "Harvest"])

# Field Preparation Phase
if phase == "Field Preparation":
    st.subheader("Field Preparation Phase")
    crop_area = st.number_input("Select Crop Area (hectares)", min_value=1)
    seeds_quantity = st.number_input("Seeds Quantity (kg)", min_value=1)
    pesticides = st.text_input("Pesticide Type", "Insecticide")
    field_preparation_steps = st.text_area("How to Prepare the Field", "Tilling, leveling, etc.")
    st.write("Sprinkler Usage Suggestion: Water the field before planting.")

# Plantation Phase
elif phase == "Plantation":
    st.subheader("Plantation Phase")
    plantation_time = st.date_input("Select Time of Plantation")

# Growth Phase
elif phase == "Growth":
    st.subheader("Growth Phase")
    pesticides_usage = st.text_input("Pesticide Usage Suggestion", "Apply fungicide if needed.")
    st.write("Sprinkler Usage Suggestion: Water regularly based on soil moisture.")

# Harvest Phase
elif phase == "Harvest":
    st.subheader("Harvest Phase")
    harvesting_time = st.date_input("Select Harvesting Time")
    storage_suggestion = st.text_area("Storage Suggestion", "Store in a cool, dry place.")

# Estimation Section
st.header("Estimation")
manpower_estimate = st.number_input("Estimated Manpower Required", min_value=1)
machinery_estimate = st.number_input("Estimated Machinery Required", min_value=1)
cost_estimate = st.number_input("Estimated Cost (in currency)", min_value=0)

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

# Footer
st.write("This application helps farmers manage irrigation effectively using real-time data and analytics.")
