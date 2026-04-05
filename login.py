import streamlit as st
import os

def login_page():

    st.title("🔐 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # ---- Read from .env (local) OR Streamlit Secrets (cloud) ----
    env_users = os.getenv("APP_USERNAMES")
    env_passwords = os.getenv("APP_PASSWORDS")

    if env_users and env_passwords:
        usernames = env_users.split(",")
        passwords = env_passwords.split(",")
    else:
        usernames = st.secrets.get("APP_USERNAMES", [])
        passwords = st.secrets.get("APP_PASSWORDS", [])

    USER_DB = dict(zip(usernames, passwords))

    # ---- Login Check ----
    if st.button("Login"):

        if username in USER_DB and USER_DB[username] == password:
            st.session_state["logged_in"] = True
            st.session_state["user"] = username
            st.success("Login successful ✅")
            st.rerun()
        else:
            st.error("Invalid credentials ❌")

    st.stop()
