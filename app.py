import streamlit as st

st.write("""
Multiplication of two numbers.
This app takes two numbres as input,  and shows their product as the output.
""")

st.header('Input Numbers :')

num1 = st.number_input('Enter first number : ')
num2 = st.number_input('Enter second number : ')

data = {'First_Number': num1,
        'Second Number': num2,
        }

st.subheader("Input From User")
st.write(data)

result = data['First_Number']*data['Second Number']

st.subheader('Result of multiplication is : ')
st.write(result)