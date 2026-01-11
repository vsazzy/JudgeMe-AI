import streamlit as st

page = st.sidebar.radio("Navigate", ["Judge Me AI", "Advanced Analysis"])

if page == "Judge Me AI":
    from modules.judge_me import run as run_mvp
    run_mvp()

elif page == "Advanced Analysis":
    from modules.advance import run as run_advanced
    run_advanced()
