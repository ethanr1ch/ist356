import streamlit as st

st.title("Area and Perimeter Calculator")

length = st.number_input("Enter the length of the rectangle:", min_value=0.0, step=0.1)
width = st.number_input("Enter the width of the rectangle:", min_value=0.0, step=0.1)

if length > 0 and width > 0:
    area = length * width
    perimeter = 2 * (length + width)
    st.write(f"The area of the rectangle is {area:.2f} square units.")
    st.write(f"The perimeter of the rectangle is {perimeter:.2f} units.")