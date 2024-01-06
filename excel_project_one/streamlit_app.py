import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# Display Title and Description
st.title("Vendor Managemnt Portal")
st.markdown("Enter the details of the new vendor below.")

# Establishing a Google Sheets Connection
conn = st.connection("gsheets", type=GSheetsConnection)

# Fetch existing vendors data
#existing_data = conn.read(worksheet="Vendors", usecols=list(range(6)), ttl=5)
#existing_data = existing_data.dropna(how="all")

# List of Business Types and Products
BUSINESS_TYPES = [
    "Manufacturer",
    "Distributor",
    "Wholesaler",
    "Retailer",
    "Service Provider",
]

PRODUCTS = [
    "Electronics",
    "Apparel",
    "Groceries",
    "Software",
    "Other",
]

# Onboarding New Vendor Form
with st.form(key="vendor_form"):
    company_name = st.text_input(label="Company Name*")
    business_type = st.selectbox("Business Type*", optiuons=BUSINESS_TYPES, index=None)
    products = st.multiselect("Products Offered", options=PRODUCTS)
    years_in_business = st.slider("Years in Business", 0, 50, 5)
    onboarding_date = st.date_input(label="Onbaording Date")
    additional_info = st.text_area(label="Addtional Notes")

    # Mark mandatory fields
    st.markdown("**required")

    submit_button = st.form_submit_button(label="Submit Vendor Details")

    # If the submit button is pressed
    if submit_button:
        st.write("You Pressed Submit")

