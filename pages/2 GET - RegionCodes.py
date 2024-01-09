import streamlit as st
import requests

st.title("GET - RegionCodes")

st.write("The \"Region Code\" API provides a mapping of region codes to their corresponding regions, enabling users to retrieve region-specific data from other APIs. The regions are categorized based on geographical, economic, and developmental criteria. Users can utilize the provided region codes to make targeted requests for information related to specific regions. ")
st.write()
st.code("https://world-bank-api.onrender.com/v1/api/RegionCodes")
st.write()
st.write("Each region code is associated with a descriptive name, making it easier for developers to integrate and use the API effectively. This API serves as a key reference for accessing comprehensive data sets tailored to different global and regional contexts.")
# Add a button to trigger data retrieval
if st.button("Test Endpoint"):
    api_url = "https://world-bank-api.onrender.com/v1/api/RegionCodes"
    response = requests.get(api_url)

    if response.status_code == 200:
        region_codes = response.json()
        st.write("Response:")
        st.json(region_codes)
    else:
        st.error(f"Failed to fetch country codes. Status Code: {response.status_code}")
