import streamlit as st
import requests

st.title("GET - CountryCodes")

st.write("The \"Get Country Codes\" API provides a comprehensive list of country codes that users can use to retrieve data from various APIs. "
             "It serves as a reference for users who want to access country-specific information from different sources. ")
st.write()
st.code("https://world-bank-api.onrender.com/v1/api/CountryCodes")
st.write("The API returns a list of standardized country codes, enabling users to select the relevant code when making requests to other APIs.")

# Add a button to trigger data retrieval
if st.button("Test Endpoint"):
    api_url = "https://world-bank-api.onrender.com/v1/api/CountryCodes"
    response = requests.get(api_url)

    if response.status_code == 200:
        country_codes = response.json()
        st.write("Response:")
        st.json(country_codes)
    else:
        st.error(f"Failed to fetch country codes. Status Code: {response.status_code}")
