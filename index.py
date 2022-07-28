import streamlit as st
import pandas as pd

st.text("Welcome to streamlit App")
if st.button('Say hello'):
    st.write('Why hello there')
if st.button("Clicked"):

    st.write('Goodbye')

