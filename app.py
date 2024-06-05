import streamlit as st
import joblib
import pandas as pd

st.title('Menyelesaikan Permasalahan Institusi Pendidikan')

def predict_student(gender, marital_status, age, scholarship, debt, sem1, sem2):
    model = joblib.load('model.pkl')
    
    gender_model = (1 if gender == 'Male' else 0)
    status_model = (1 if marital_status == 'single' else 0)
    scholarship_model = (1 if scholarship == "Yes" else 0)
    debt_model = (1 if debt == 'Yes' else 0)
    
    to_pd = pd.DataFrame([{'Gender':gender_model,
              'Marital_status':status_model,
              'Age_at_enrollment':age,
              'Scholarship_holder':scholarship_model,
              'Debtor':debt_model,
              'Curricular_units_1st_sem_grade':sem1,
              'Curricular_units_2nd_sem_grade':sem2}])
    
    result = model.predict(to_pd)
    
    if result == 1:
        return "Dropout"
    return "Non-Dropout"
    
with st.form("my_form"):
    gender = st.selectbox(
        "What is your gender?",
        ("Male", "Female"))

    marital_status = st.selectbox(
        "What is your marital status?",
        ("Single", "Couple"))

    age = st.slider(
        "How old are you?", 
        0, 100, 25)

    scholarship = st.selectbox(
        "Are you a scholarship holder?",
        ("Yes", "No"))

    debt = st.selectbox(
        "Are you using a debt?",
        ("Yes", "No"))

    col1, col2 = st.columns(2)
    
    with col1:
        semester1_grade = st.number_input("Your semester 1 grade")
    with col2:
        semester2_grade = st.number_input("Your semester 2 grade")
    
    submitted = st.form_submit_button("Submit")
    if submitted:
        predict = predict_student(gender, marital_status, age, scholarship, debt, semester1_grade, semester2_grade)
        if predict == "Dropout":
            st.error('This student maybe dropout!', icon="🚨")
        else:
            st.success('This student maybe continue to learn!', icon="✅")


