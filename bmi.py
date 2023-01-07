import streamlit as st
st.subheader("""BODY MASS INDEX CALCULATOR""")
st.image('BMI.jpg')
with st.form(key='BMI Calculator'):
    name = st.text_input("Please enter your name: ")
    weight = st.number_input("Please enter your weight in kilograms: ")
    height = st.number_input("Pleae enter your height in centimeter: ")
    submit_button = st.form_submit_button(label='Calculate')

if submit_button == True:
    bmi = round(weight/(height**2)*(100**2),2)
    #st.write((f"{name} your BMI is {bmi}"))

    if bmi < 18.5:
        st.write((f"{name} your bmi is {bmi} and you are Underweight"))
    elif bmi > 18.5 and bmi < 24.9:
        st.write((f"{name} your bmi is {bmi} and you have Normalweight"))
    elif bmi > 25 and bmi < 29.9:
        st.write((f"{name} your bmi is {bmi} and you are Over Weight"))
    elif bmi > 30 and bmi < 34.9:
        st.write((f"{name} your bmi is {bmi} and you are Obese"))
    elif bmi > 35 and bmi < 39.9:
        st.write((f"{name} your bmi is {bmi} and you are Seriously Obese"))
    elif bmi > 40:
        st.write((f"{name} your bmi is {bmi} and you are Morbidly Obese"))





    


