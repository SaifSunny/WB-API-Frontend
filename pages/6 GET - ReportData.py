import streamlit as st
import requests

st.title("ReportData")
st.write("The \"ReportData\" API allows users to retrieve data for specific reports from the World Bank. Users can customize their requests by specifying the desired country and report, enabling them to obtain targeted and relevant data. The API supports various parameters, including country code and report code.")
st.write()
st.code("https://world-bank-api.onrender.com/v1/api/ReportData?country={countryCode}&report={reportCode}")
st.write()
st.write("Users can customize their requests by specifying the desired country and report code, providing flexibility in fetching data tailored to specific research needs.")

# Input boxes for country and report code arranged side by side
col1, col2 = st.columns(2)

# Set default value for country code to "USA" and report code to "WBRE-01"
country_code = col1.text_input("Enter Country Code:", value="USA")
report_code = col2.text_input("Enter Report Code:", value="WBRE-01")

# Add a button to trigger data retrieval
if st.button("Test Endpoint"):
    api_url = f"https://world-bank-api.onrender.com/v1/api/ReportData?country={country_code}&report={report_code}"
    response = requests.get(api_url)

    if response.status_code == 200:
        report_data = response.json()
        st.write("Response:")
        st.json(report_data)
    else:
        st.error(f"Failed to fetch report data. Status Code: {response.status_code}")
