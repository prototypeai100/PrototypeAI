# UI helper for displaying AI chat bubbles with color and icon.

def ai_message_box(content, who, color=None):
    CHATGPT_COLOR = "#d1e7dd"
    GROK_COLOR = "#ffe3cc"
    CRITIQUE_COLOR = "#f9ded7"
    SELF_EVAL_COLOR = "#fff9e2"
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
    elif "impact" in who.lower():
        color = "#e6f6f6"
        icon = "🧩"
    else:
        color = color or "#e6f0fa"
        icon = "🏁"
    import streamlit as st
    st.markdown(
        f"""
        <div style="background:{color};border-radius:16px;padding:18px 16px 12px 16px;margin-bottom:8px;">
        <strong>{icon} {who}:</strong><br>{content}
        </div>
        """,
        unsafe_allow_html=True,
    )
