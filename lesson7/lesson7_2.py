from tools import taipei
import streamlit as st

@st.dialog("網路出現問題")
def vote(error):
    st.write(error)

try:
    ubike_data:list[dict] = taipei.get_ubikes()
except Exception as error:
    vote(error)
    st.write("請稍後再試!")
    st.stop()

st.table(ubike_data)                                                         