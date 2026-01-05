import streamlit as st

def render_header():
    st.set_page_config(page_title="Judge Me AI 😈", layout="centered")
    st.title("😈 Judge Me AI")
    st.caption("Get roasted, read, and rebuilt by AI")
    st.caption("An AI that sees through you… politely or brutally")

def user_inputs():
    text = st.text_area(
        "Paste your bio / resume / dating profile / chats (at your own risk) 👇",
        height=180
    )

    tone = st.select_slider(
        "How honest should I be?",
        options=["Gentle", "Honest", "Brutal"]
    )

    context = st.selectbox(
        "What is this for?",
        ["Dating", "Career", "Social Media", "General"]
    )

    return text, tone, context
