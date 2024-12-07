import streamlit as st
import joblib

model = joblib.load("decisiontree.pkl")

with st.form("my_form"):
    st.write("Insert data")
    sex = 0 if st.selectbox("Sex", ["Male", "Female"]) == "Female" else 1
    age = st.number_input("Age", 1)
    hypertension = st.toggle("Ever had hypertension?")
    heart_disease = st.toggle("Ever had Heart Disease")
    ever_married = st.toggle("Ever married")
    work_type = st.selectbox("Work Type", ["Never worked", "With children", "Government job", "Self-employed", "Private"])
    match work_type:
        case "Never worked": work_type = 0
        case "With children": work_type = 1
        case "Government job": work_type = 2
        case "Self-employed": work_type = 3
        case "Private": work_type = 3
    residence_type = st.selectbox("Residence Type", ["Urban", "Rural"])
    match residence_type:
        case "Urban": residence_type = 0
        case "Rural": residence_type = 1
    avg_glucose_level = st.number_input("Average Glucose Level", 1.00)
    bmi = st.number_input("BMI", 1.0)
    smoking_status = st.toggle("Ever smoked?")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
if submitted:
    st.write("Prediction:")
    prediction = model.predict([[sex, age, hypertension, heart_disease, ever_married, work_type, residence_type, avg_glucose_level, bmi, smoking_status]])
    prediction = "Has stroke" if prediction == 1 else "Does not have stroke"
    st.write(prediction)
