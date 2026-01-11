import streamlit as st
from prompts import judge_prompt
from llm import get_judgement
from ui import render_header, user_inputs

def run():
    render_header()
    text, tone, context = user_inputs()

    if st.button("Judge Me 😈"):
        if not text.strip():
            st.warning("Paste something first. I can’t judge air.")
        else:
            with st.spinner("Judging you silently..."):
                prompt = judge_prompt(text, tone, context)
                result = get_judgement(prompt)

            st.markdown("---")
            st.markdown(result)
