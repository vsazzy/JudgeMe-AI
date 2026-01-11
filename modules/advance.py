import streamlit as st
from llm import get_judgement
from prompts import persona_drift_prompt, red_flags_prompt, social_perception_prompt

def run():
    st.title("Advanced Personality Analysis")

    feature = st.radio("Select Feature", [
        "Persona Drift Analysis",
        "Explainable Red Flags",
        "Social Perception Simulator"
    ])

    if feature == "Persona Drift Analysis":
        texts = st.text_area("Paste multiple texts (one per line)").split("\n")
        if st.button("Analyze Drift"):
            prompt = persona_drift_prompt(texts)
            result = get_judgement(prompt)
            st.markdown("---")
            st.write(result)

    elif feature == "Explainable Red Flags":
        text = st.text_area("Paste text to analyze")
        if st.button("Analyze Red Flags"):
            prompt = red_flags_prompt(text)
            result = get_judgement(prompt)
            st.markdown("---")
            st.write(result)

    elif feature == "Social Perception Simulator":
        text = st.text_area("Paste text to see how others perceive it")
        persona = st.multiselect("Select Personas", ["Recruiter", "Friend", "Ex", "Therapist", "Stranger"])
        if st.button("Simulate"):
            prompt = social_perception_prompt(text, persona)
            result = get_judgement(prompt)
            st.markdown("---")
            st.write(result)
