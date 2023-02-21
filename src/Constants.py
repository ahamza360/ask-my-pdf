import streamlit as st

OPEN_AI_API_KEY = ''

if OPEN_AI_API_KEY == '' and st.secrets["api_key"] != '':
    OPEN_AI_API_KEY = st.secrets["api_key"]