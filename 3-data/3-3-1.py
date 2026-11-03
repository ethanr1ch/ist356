import streamlit as st
import pandas as pd
import numpy as np
import requests

url = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/json-samples/employees-dict.json"
response = requests.get(url)
employees = response.json()

# data = employees['sales']
# df = pd.DataFrame(data)

# st.write(employees)
# st.write("Sales Data:")
# st.write(df)

dfs = []

for key in employees.keys():
    df = pd.DataFrame(employees[key])
    df['department'] = key
    dfs.append(df)


combined_df = pd.concat(dfs, ignore_index=True)

st.dataframe(combined_df)
st.write(employees)
