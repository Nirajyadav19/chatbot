import streamlit as st
import os

def login_page():

    st.title("🔐 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    env_user = os.getenv("APP_USERNAME") or st.secrets["APP_USERNAME"]
    env_pass = os.getenv("APP_PASSWORD") or st.secrets["APP_PASSWORD"]

    if st.button("Login"):

        if username == env_user and password == env_pass:
            st.session_state["logged_in"] = True
            st.session_state["user"] = username
            st.success("Login successful")
            st.rerun()
        else:
            st.error("Invalid credentials")

    st.stop()