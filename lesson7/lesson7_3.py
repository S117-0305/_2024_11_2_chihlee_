import streamlit as st

st.title("次數範例")
count = 0

increament = st.button("每次加一")
if increament:
    count += 1

st.write("次數=",count)