import streamlit as st

def apply_styles():
    st.markdown("""
    <style>

    /* 🌌 Animated Background */
    .stApp {
        background: linear-gradient(-45deg, #0f172a, #020617, #020617, #0f172a);
        background-size: 400% 400%;
        animation: gradientBG 12s ease infinite;
        color: white;
    }

    @keyframes gradientBG {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    /* 🧊 Glass Container */
    .block-container {
        padding-top: 2rem;
        backdrop-filter: blur(12px);
    }

    /* 💬 Chat Bubbles */
    .stChatMessage {
        border-radius: 20px;
        padding: 16px;
        font-size: 15px;
        backdrop-filter: blur(10px);
        box-shadow: 0 8px 32px rgba(0,0,0,0.3);
        border: 1px solid rgba(255,255,255,0.08);
        transition: 0.3s;
    }

    .stChatMessage:hover {
        transform: scale(1.01);
    }

    .stChatMessage.user {
        background: linear-gradient(135deg,#2563eb,#1d4ed8);
        color: white;
    }

    .stChatMessage.assistant {
        background: rgba(255,255,255,0.08);
        color: #e5e7eb;
    }

    /* 🤖 Header Glow */
    .ai-title {
        text-align: center;
        font-size: 42px;
        font-weight: 700;
        background: linear-gradient(90deg,#60a5fa,#a78bfa,#22d3ee);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .ai-subtitle {
        text-align: center;
        color: #94a3b8;
        margin-bottom: 30px;
    }

    /* 🟢 Online Status */
    .status {
        display:flex;
        justify-content:center;
        gap:8px;
        color:#22c55e;
        font-size:14px;
        margin-bottom:20px;
    }

    .dot {
        height:10px;
        width:10px;
        background:#22c55e;
        border-radius:50%;
        animation: pulse 1.5s infinite;
    }

    @keyframes pulse {
        0% {transform: scale(0.9); opacity: 0.7;}
        70% {transform: scale(1.3); opacity: 0;}
        100% {transform: scale(0.9); opacity: 0;}
    }

    /* ✍️ Input Bar */
    .stChatInput input {
        border-radius: 25px;
        background: rgba(255,255,255,0.08);
        color: white;
        border: 1px solid rgba(255,255,255,0.1);
        padding: 14px;
    }

    /* 🎛️ Sidebar */
    section[data-testid="stSidebar"] {
        background: rgba(255,255,255,0.05);
        backdrop-filter: blur(20px);
        border-right: 1px solid rgba(255,255,255,0.08);
    }

    /* 🧼 Scrollbar */
    ::-webkit-scrollbar {
        width: 6px;
    }
    ::-webkit-scrollbar-thumb {
        background: #60a5fa;
        border-radius: 10px;
    }

    </style>
    """, unsafe_allow_html=True)


def sidebar_controls(clear_chat_fn):
    with st.sidebar:
        st.markdown("## ⚙️ AI Control Hub")
        st.button("🧹 Clear Conversation", use_container_width=True, on_click=clear_chat_fn)

        st.markdown("---")
        st.markdown("### 🤖 Model")
        st.caption("gemini-2.5-flash")

        st.markdown("### 🌡️ Creativity")
        st.slider("Temperature", 0.0, 1.0, 0.7)

        st.markdown("### 📊 Max Tokens")
        st.slider("Response Length", 100, 2000, 800)


def render_header(title):
    st.markdown(f'<div class="ai-title">{title}</div>', unsafe_allow_html=True)
    st.markdown('<div class="status"><div class="dot"></div> AI Online</div>', unsafe_allow_html=True)
    st.markdown('<div class="ai-subtitle">Next-gen conversational experience powered by Gemini</div>', unsafe_allow_html=True)


def display_messages(messages):
    for msg in messages:
        role = "user" if msg["role"] == "user" else "assistant"
        avatar = "🧑‍💻" if role == "user" else "🤖"

        with st.chat_message(role, avatar=avatar):
            st.markdown(msg["parts"][0])