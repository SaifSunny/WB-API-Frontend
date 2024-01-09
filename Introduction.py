import streamlit as st

st.set_page_config(
    page_title="World Bank Data API",
    page_icon="👋",
)
st.sidebar.success("Select an API above.")

st.title("Introduction")
st.write("Welcome to the SDG Data API, a powerful tool that provides seamless access to Sustainable Development Goals (SDG) data collected from the World Bank website. Our API is designed to offer comprehensive information on various aspects of global development, allowing users to retrieve data effortlessly and integrate it into their applications, analyses, and projects.")

st.subheader("Base URL")
st.code("https://world-bank-api.onrender.com/v1/api/")
st.subheader("API Endpoints")

st.subheader("1. GET - CountryCodes")
st.write("Retrieve a comprehensive list of country codes to identify specific nations in the World Bank database.")
st.code("{BASE URL}/CountryCodes")

st.subheader("2. GET - RegionCodes")
st.write("Access region codes, such as South Asia, Western World, and more, to categorize countries based on geographical regions.")
st.code("{BASE URL}/RegionCodes")

st.subheader("3. GET - IndicatorCode")
st.write("Obtain SDG indicator codes to uniquely identify and reference specific indicators.")
st.code("{BASE URL}/IndicatorCode")

st.subheader("4. GET - ReportCodes")
st.write("Retrieve complete report codes, such as agriculture, education, and more, to navigate through various thematic areas.")
st.code("{BASE URL}/ReportCodes")

st.subheader("5. GET - IndicatorData")
st.write("Retrieve SDG indicator data by specifying the indicator code and country code within the time range of 1960-2022.")
st.code("{BASE URL}/IndicatorData?country={countryCode}&indicator={indicatorCode}")

st.subheader("6. GET - ReportData")
st.write("Access report data by specifying the report code and country code within the time range of 1960-2022.")
st.code("{BASE URL}/ReportData?country={countryCode}&report={reportCode}")

st.subheader("7. POST - CountryAllReports")
st.write("Retrieve data for all reports by specifying the indicator code, country code, and custom start and end years.")
st.code("{BASE URL}/CountryAllReports")
st.write("Request Body")
st.code("""
{
    "country_code": "BGD",
    "start_year": "1990",
    "end_year": "2020",
    "Reports": {
        "AgricultureAndRuralDevelopment": false,
        "AidEffectiveness": true,
        "ClimateChange": true,
        "EconomyAndGrowth": true,
        "Education": true,
        "EnergyAndMining": true,
        "Environment": true,
        "ExternalDebt": true,
        "FinancialSector": true,
        "Gender": true,
        "Health": true,
        "Infrastructure": true,
        "Poverty": true,
        "PrivateSector": true,
        "PublicSector": true,
        "ScienceAndTechnology": true,
        "SocialDevelopment": true,
        "SocialProtectionAndLabor": true,
        "Trade": true,
        "UrbanDevelopment": true
    }
}
""")

st.subheader("8. POST - MultipleIndicatorData")
st.write("Retrieve data for multiple indicators by specifying the indicator codes, country code, and custom start and end years.")
st.code("{BASE URL}/MultipleIndicatorData")
st.write("Request Body")
st.code("""
{
    "country_code": "BGD",
    "start_year": "2000",
    "end_year": "2002",
    "Indicators": [
        "WBIN-0010",
        "WBIN-0163"
    ]
}
""")
