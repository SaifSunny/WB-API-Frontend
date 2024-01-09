import streamlit as st
import requests

st.title("GET - ReportCodes")
st.write("The \"GET - ReportCodes\" API offers a comprehensive compilation of report codes, each associated with specific thematic areas, allowing users to retrieve detailed reports on diverse topics from the World Bank. This API serves as a valuable resource for developers, researchers, and analysts who wish to access comprehensive information organized by specific report categories. Thematic areas covered by the reports include Agriculture and Rural Development, Aid Effectiveness, Climate Change, Education, Health, Infrastructure, Poverty, and more.")
st.write()
st.code("https://world-bank-api.onrender.com/v1/api/ReportCodes")

# Add a button to trigger data retrieval
if st.button("Test Endpoint"):
    api_url = "https://world-bank-api.onrender.com/v1/api/ReportCodes"
    response = requests.get(api_url)

    if response.status_code == 200:
        region_codes = response.json()
        st.write("Response:")
        st.json(region_codes)
    else:
        st.error(f"Failed to fetch country codes. Status Code: {response.status_code}")
