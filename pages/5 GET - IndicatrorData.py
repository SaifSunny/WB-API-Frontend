import streamlit as st
import requests

st.title("GET - IndicatorData")
st.write("The \"GET - IndicatorData\" API provides a dynamic and interactive platform for users to retrieve detailed data on specific indicators from the World Bank. This API allows users to explore and analyze a wide array of indicators, ranging from economic metrics to social and environmental statistics. It serves as a valuable resource for developers, researchers, and data enthusiasts seeking to access granular information for a given country and indicator.")
st.write()
st.code("https://world-bank-api.onrender.com/v1/api/IndicatorData?country={countryCode}&indicator={indicatorCode}")

# Input boxes for country and indicator arranged side by side
col1, col2 = st.columns(2)
country_code = col1.text_input("Enter Country Code:", value="BGD")
indicator_code = col2.text_input("Enter Indicator Code:", value="WBIN-0111")

# Add a button to trigger data retrieval
if st.button("Test Endpoint"):
    api_url = f"https://world-bank-api.onrender.com/v1/api/IndicatorData?country={country_code}&indicator={indicator_code}"
    response = requests.get(api_url)

    if response.status_code == 200:
        indicator_data = response.json()
        st.write("Response:")
        st.json(indicator_data)
    else:
        st.error(f"Failed to fetch indicator data. Status Code: {response.status_code}")
