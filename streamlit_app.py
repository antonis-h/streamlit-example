from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.write("""
## Superstore Dataset
""")

with st.sidebar:
    st.write('External features')
    for i in range(1,5):
        box = st.checkbox(f'Option {i}')

data = pd.read_csv("https://raw.githubusercontent.com/jeaggo/tc3068/master/Superstore.csv")
data['Order Date'] = pd.to_datetime(data['Order Date'], format = '%m/%d/%Y')

st.title('Daily Sales')
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
day_chosen = st.sidebar.selectbox('Choose a day', days)
sales_day = data[data['Order Date'].dt.day_name() == f'{day_chosen}']

fig = plt.plot(sales_day['Order Date'],sales_day['Sales'].rolling(300).mean(),'x')
#st.pyplot(fig)

click = st.button("Don't press too hard")

if click:
    st.write("""
    Ouchhh :cry:
    """)
    
    
this = st.text_input('What')

st.write(this)
