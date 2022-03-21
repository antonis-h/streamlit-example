from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

st.write("""
## Checking the buttons :cry:

Go ahead and experiment!
""")

with st.sidebar:
    st.write('External features')
    for i in range(5):
        box = st.checkbox(f'Option {i}')

st.title('Experimenting with Streamlit')

click = st.button("Don't press too hard")

if click:
    st.write('Oucchhh ')
    
    
this = st.text_input('What')

st.title(this)
