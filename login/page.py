import streamlit as st
from login.service import login

def show_login():
    st.title('Login')

    username = st.text_input("uruário")
    password = st.text_input(label='senha', type='password')
    if st.button("Entrar"):
        login(
            username=username,
            password=password
        )