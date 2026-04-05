import streamlit as st

def login_page():

    st.title("🔐 Login")

    # Read secrets safely
    usernames = st.secrets.get("APP_USERNAMES", [])
    passwords = st.secrets.get("APP_PASSWORDS", [])

    # Debug (remove later)
    # st.write(usernames, passwords)

    USER_DB = dict(zip(usernames, passwords))

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        if email in USER_DB and USER_DB[email] == password:
            st.session_state["authenticated"] = True
            st.success("Login successful ✅")
            st.rerun()
        else:
            st.error("Invalid email or password ❌")
