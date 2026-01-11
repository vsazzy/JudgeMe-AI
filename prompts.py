# prompts.py

def judge_prompt(text, tone, context):
    return f"""
You are a witty AI judge. Tone: {tone}. Analyze this text and provide roast, red flags, green flags, advice.
Context: {context}
{text}
"""

def persona_drift_prompt(texts):
    joined = "\n".join(texts)
    return f"""
Analyze these multiple texts from the same person. Detect persona drift, contradictions, and inconsistencies.
Texts:
{joined}
Provide a summary with scores and highlights.
"""

def red_flags_prompt(text):
    return f"""
Analyze this text for red flags. Highlight evidence, explain why it's a problem, and suggest fixes.
{text}
"""

def social_perception_prompt(text, personas):
    persona_list = ", ".join(personas)
    return f"""
Simulate how different personas would perceive this text: {persona_list}.
Analyze tone, confidence, and personality traits.
Text: {text}
"""
