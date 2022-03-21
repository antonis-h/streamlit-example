from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

st.title('Experimenting with Streamlit')

click = st.button("Don't press too hard")

if click:
    st.write('Oucchhh ',:cry:)
this = st.text_input('What')

st.title(this)
