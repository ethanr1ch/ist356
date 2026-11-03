import streamlit as st

st.title("Order Tracker'")

st.session_state.total = 0
st.session_state.history = []

amount = st.number_input("Order Amount:")
total_button = st.button("Calculate Total",
                          type = "primary")
clear_button = st.button("Clear")



st.write(f"Total Order: {st.session_state.total}")
st.write(f"History: {st.session_state.history}")

