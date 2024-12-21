import streamlit as st

#手動建立counter變數，並設定初始值為0
if "counter" not in st.session_state:
    #st.session_state.[counter] = 0
    st.session_state.counter = 1

def increment_counter(**kwargs):
    st.session_state.counter += kwargs["first"]
    st.session_state.counter -= kwargs["second"]


st.header(f"這個網頁已經執行了{st.session_state.counter}次")  
st.button("再執行一次",
           key="reset", 
           help="按下按鈕後，計數器會加1", 
           on_click=increment_counter, 
           kwargs={"first":5,"second":3})