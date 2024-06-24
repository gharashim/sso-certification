import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

st.title("Streamlit with FastAPI and OpenID Connect")

if 'user' not in st.session_state:
    st.session_state.user = None

if st.session_state.user:
    st.write(f"Logged in as: {st.session_state.user['name']}")
    if st.button("Logout"):
        response = requests.get(f"{BASE_URL}/logout")
        st.session_state.user = None
        st.experimental_rerun()
else:
    st.write("You are not logged in.")
    if st.button("Login"):
        # Redirect to the FastAPI login endpoint
        st.write("Redirecting to login...")
        response = requests.get(f"{BASE_URL}/login")
        if response.status_code == 200:
            st.experimental_rerun()

if st.button("Protected Route"):
    if st.session_state.user:
        response = requests.get(f"{BASE_URL}/protected")
        if response.status_code == 200:
            st.write(response.json())
        else:
            st.write("Unauthorized")
    else:
        st.write("You need to log in first.")
