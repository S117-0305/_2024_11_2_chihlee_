import streamlit as st

#手動建立counter變數，並設定初始值為0
if "counter" not in st.session_state:
    #st.session_state.[counter] = 0
    st.session_state.counter = 1

def increment_counter(*args):
    st.session_state.counter += args[0]
    st.session_state.counter -= args[1]


st.header(f"這個網頁已經執行了{st.session_state.counter}次")  
st.button("再執行一次", key="reset", help="按下按鈕後，計數器會加1", on_click=increment_counter, args=(5,3))
