import streamlit as st
import requests

st.title("CountryFullReport")
st.write("The \"CountryFullReport\" API allows users to retrieve a comprehensive report for a specific country, covering various categories such as Agriculture and Rural Development, Aid Effectiveness, Climate Change, and more. Users can customize their requests by specifying the country code, start year, end year, and the desired reports to include.")
st.write()
st.code("https://world-bank-api.onrender.com/v1/api/CountryFullReport")
st.write()
st.write("Users can modify the input parameters, including the country code, start year, end year, and the selection of specific reports, to obtain a detailed and tailored report for analysis.")

# Input boxes for country code, start year, end year, and multiple indicator selections in 3 columns
col1, col2, col3 = st.columns(3)

# Column 1: Input box for country code
country_code = col1.text_input("Enter Country Code:", value="BGD")

# Column 2: Input box for start year
start_year = col2.text_input("Enter Start Year:", value="2000")

# Column 3: Input box for end year
end_year = col3.text_input("Enter End Year:", value="2002")

# Checkbox selection for reports
st.subheader("Select Reports to Include:")
reports = {
    "AgricultureAndRuralDevelopment": False,
    "AidEffectiveness": True,
    "ClimateChange": True,
    "EconomyAndGrowth": True,
    "Education": True,
    "EnergyAndMining": True,
    "Environment": True,
    "ExternalDebt": True,
    "FinancialSector": True,
    "Gender": True,
    "Health": True,
    "Infrastructure": True,
    "Poverty": True,
    "PrivateSector": True,
    "PublicSector": True,
    "ScienceAndTechnology": True,
    "SocialDevelopment": True,
    "SocialProtectionAndLabor": True,
    "Trade": True,
    "UrbanDevelopment": True
}

for key, value in reports.items():
    reports[key] = st.checkbox(key, value=value)

# Add a button to trigger data retrieval
if st.button("Test Endpoint"):
    api_url = "https://world-bank-api.onrender.com/v1/api/CountryFullReport"
    payload = {
        "country_code": country_code,
        "start_year": start_year,
        "end_year": end_year,
        "Reports": reports
    }

    response = requests.post(api_url, json=payload)

    if response.status_code == 200:
        country_report = response.json()
        st.write("Response:")
        st.json(country_report)
    else:
        st.error(f"Failed to fetch country report. Status Code: {response.status_code}")
