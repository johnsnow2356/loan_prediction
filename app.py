import streamlit as st
import numpy as np
import joblib

# Load trained model
model = joblib.load('loan_model.pkl')

st.title("Loan Approval Predictor")

# Inputs
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
app_income = st.number_input("Applicant Income", min_value=0)
coapp_income = st.number_input("Coapplicant Income", min_value=0)
loan_amt = st.number_input("Loan Amount", min_value=0)
loan_term = st.selectbox("Loan Term", [360, 180, 240])
credit = st.selectbox("Credit History", [1, 0])
property_area = st.selectbox("Property Area", ["Urban", "Rural", "Semiurban"])

# Convert inputs to numerical format
input_data = [1 if gender == "Male" else 0,
              1 if married == "Yes" else 0,
              {"0": 0, "1": 1, "2": 2, "3+": 3}[dependents],
              1 if education == "Graduate" else 0,
              1 if self_employed == "Yes" else 0,
              app_income, coapp_income, loan_amt, loan_term, credit,
              {"Urban": 2, "Rural": 0, "Semiurban": 1}[property_area]]

# Predict
if st.button("Predict"):
    prediction = model.predict([input_data])
    st.success("Loan Approved!" if prediction[0] == 1 else "Loan Rejected")
