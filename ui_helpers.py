import streamlit as st

CHATGPT_COLOR = "#d1e7dd"
GROK_COLOR = "#ffe3cc"
CRITIQUE_COLOR = "#f9ded7"
SELF_EVAL_COLOR = "#fff9e2"

def ai_message_box(content, who, color=None):
    if who == "ChatGPT":
        color = color or CHATGPT_COLOR
        icon = "🧠"
    elif who == "Grok":
        color = color or GROK_COLOR
        icon = "🤖"
    elif "critique" in who.lower():
        color = color or CRITIQUE_COLOR
        icon = "⚖️"
    elif "self-eval" in who.lower():
        color = color or SELF_EVAL_COLOR
        icon = "🔍"
    else:
        color = color or "#e6f0fa"
        icon = "🏁"
    st.markdown(
        f"""
        <div style="background:{color};border-radius:16px;padding:18px 16px 12px 16px;margin-bottom:8px;">
        <strong>{icon} {who}:</strong><br>{content}
        </div>
        """,
        unsafe_allow_html=True,
    )
