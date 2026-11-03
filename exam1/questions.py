import streamlit as st

from figures import *

new = df8.pivot(index="COLA", columns="COLB", values="COLC")
new2 = df8.pivot(index="COLB", columns="COLA", values="COLC")

st.write(new)
st.write(new2)
