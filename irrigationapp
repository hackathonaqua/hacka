import streamlit as st
import pandas as pd
import requests

# Sample data for demonstration purposes
soil_data = {
    "Soil Temperature (°C)": [20, 21, 22],
    "Soil Humidity (%)": [30, 35, 40],
    "Ambient Temperature (°C)": [25, 26, 27],
    "Ambient Humidity (%)": [50, 55, 60],
}

# Function to control sprinklers
def control_sprinklers(action):
    # Here, you'd typically send an HTTP request to the sprinkler controller
    url = "http://your_sprinkler_controller_api_endpoint"
    response = requests.post(url, json={"action": action})
    return response.status_code

# Streamlit UI
st.title("Smart Irrigation Management System")

st.header("Soil Moisture Profile")
st.write("Monitor soil data collected from the sensor network.")

# Display the soil data
soil_df = pd.DataFrame(soil_data)
st.dataframe(soil_df)

# Planning the plantation cycle
st.header("Plantation Cycle Planning")
st.write("Use the data to plan your irrigation needs.")

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

# Footer
st.write("This application helps farmers manage irrigation effectively using real-time data.")
