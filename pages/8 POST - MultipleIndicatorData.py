import streamlit as st
import requests

st.title("MultipleIndicatorData")
st.write("The \"MultipleIndicatorData\" API allows users to retrieve data for multiple indicators within a specified time range for a specific country. Users can customize their requests by providing the country code, start year, end year, and a list of indicator codes.")
st.write()
st.code("https://world-bank-api.onrender.com/v1/api/MultipleIndicatorData")
st.write()
st.write("Users can modify the input parameters, including the country code, start year, end year, and the list of indicator codes, to obtain data for multiple indicators for analysis.")

# Input boxes for country code, start year, and end year in 2 columns
col1, col2 = st.columns(2)

# Column 1: Input box for country code
country_code = col1.text_input("Enter Country Code:", value="BGD")
indicators_input = col1.text_input("Enter Indicator Codes (comma-separated):", value="WBIN-0010, WBIN-0163")
indicators = [indicator.strip() for indicator in indicators_input.split(',')]


# Column 2: Input boxes for start year and end year
start_year = col2.text_input("Enter Start Year:", value="2000")
end_year = col2.text_input("Enter End Year:", value="2002")


# Add a button to trigger data retrieval
if st.button("Test Endpoint"):
    api_url = "https://world-bank-api.onrender.com/v1/api/MultipleIndicatorData"
    payload = {
        "country_code": country_code,
        "start_year": start_year,
        "end_year": end_year,
        "Indicators": indicators
    }

    response = requests.post(api_url, json=payload)

    if response.status_code == 200:
        multiple_indicator_data = response.json()
        st.write("Response:")
        st.json(multiple_indicator_data)
    else:
        st.error(f"Failed to fetch multiple indicator data. Status Code: {response.status_code}")
