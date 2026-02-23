import streamlit as st
from config.settings import PAGE_TITLE
from services.gemini_service import get_gemini_response
from utils.session_manager import init_session, add_user_message, add_bot_message, clear_chat
from ui.chat_ui import apply_styles, sidebar_controls, render_header, display_messages

st.set_page_config(page_title=PAGE_TITLE, page_icon="🤖", layout="wide")

apply_styles()
init_session()
sidebar_controls(clear_chat)
render_header(PAGE_TITLE)
display_messages(st.session_state.messages)

user_input = st.chat_input("Message Gemini...")

if user_input:
    add_user_message(user_input)

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = get_gemini_response(user_input, st.session_state.messages)
            st.markdown(response)

    add_bot_message(response)