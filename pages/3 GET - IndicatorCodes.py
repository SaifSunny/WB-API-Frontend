import streamlit as st
import requests

st.title("GET - IndicatorCodes")
st.write("The \"GET - IndicatorCodes\" API provides a comprehensive mapping of indicator codes related to various thematic areas and subjects, allowing users to access specific data points from diverse sources. This API serves as a valuable reference for developers and analysts who seek to integrate and analyze World Bank data at a granular level.")
st.write()
st.code("https://world-bank-api.onrender.com/v1/api/IndicatorCodes")
st.write()
st.write("The indicators cover a wide range of topics such as Agriculture and Rural Development, Aid Effectiveness, Climate Change, Education, Health, and more. Users can explore the available indicators, their corresponding codes, and associated data points, enabling precise retrieval of information tailored to their analytical needs.")
# Add a button to trigger data retrieval
if st.button("Test Endpoint"):
    api_url = "https://world-bank-api.onrender.com/v1/api/IndicatorCodes"
    response = requests.get(api_url)

    if response.status_code == 200:
        region_codes = response.json()
        st.write("Response:")
        st.json(region_codes)
    else:
        st.error(f"Failed to fetch country codes. Status Code: {response.status_code}")
