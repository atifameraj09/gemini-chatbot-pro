import streamlit as st

def init_session():
    if "messages" not in st.session_state:
        st.session_state.messages = []

def add_user_message(message):
    st.session_state.messages.append({"role": "user", "parts": [message]})

def add_bot_message(message):
    st.session_state.messages.append({"role": "model", "parts": [message]})

def clear_chat():
    st.session_state.messages = []