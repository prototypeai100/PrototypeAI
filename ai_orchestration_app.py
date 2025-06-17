import streamlit as st
import os
from dotenv import load_dotenv
from ai_engines import ask_chatgpt, ask_grok
from prompts import (
    CHATGPT_VOICE, GROK_VOICE, CRITIQUE_CHATGPT, CRITIQUE_GROK,
    SELF_EVAL_CHATGPT, SELF_EVAL_GROK, SYNTHESIZE_PROMPT, DIFFERENCE_PROMPT
)
from ui_helpers import ai_message_box

# ========== ENV AND PAGE CONFIG ==========
load_dotenv()

st.set_page_config(
    page_title="🧑 ➡️ 🤖🤝🤖 ➡️ 🧑  AI-to-AI Enhanced Debate",
    layout="wide",
    page_icon="🤖"
)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GROK_API_KEY = os.getenv("GROK_API_KEY")

if not OPENAI_API_KEY or not OPENAI_API_KEY.strip().lower().startswith("sk-"):
    st.error("OPENAI_API_KEY is missing or invalid! Set it securely in your .env file or as an OS environment variable.")
    st.stop()
if not GROK_API_KEY or len(GROK_API_KEY.strip()) < 16:
    st.error("GROK_API_KEY is missing or appears invalid! Set it securely in your .env file or as an OS environment variable.")
    st.stop()

# ========== MAIN TITLE ==========
st.markdown("""
# 🧑 ➡️ 🤖🤝🤖 ➡️ 🧑
### AI-to-AI Enhanced Debate: 2 Rounds, Synthesis & Differences
""")

# ========== USER INPUT ==========
user_question = st.text_area(
    "",
    height=100,
    placeholder="Describe a question, challenge, or topic for ChatGPT and Grok to debate and co-create an answer."
)

# ========== FUNCTIONAL BUTTONS ==========
colA, colB = st.columns([1, 1])
with colA:
    run_btn = st.button("▶️ Run Co-Creation", key="co_creation", use_container_width=True)
with colB:
    enhanced_btn = st.button("🤺 Run Enhanced Debate (2 Rounds)", key="enhanced_debate", use_container_width=True)

# ========== MAIN LOGIC ==========
if enhanced_btn and user_question.strip():
    # ---- Round 1: Both answer ----
    st.markdown("## **Round 1**")
    col1, col2 = st.columns(2)
    with col1:
        chatgpt_r1 = ask_chatgpt(
            f"{CHATGPT_VOICE}\n\nUser question:\n{user_question.strip()}"
        )
        ai_message_box(chatgpt_r1, "ChatGPT")
    with col2:
        grok_r1 = ask_grok(
            f"{GROK_VOICE}\n\nUser question:\n{user_question.strip()}",
            GROK_API_KEY
        )
        ai_message_box(grok_r1, "Grok")
    # ---- Round 1: Each critiques the other's answer ----
    st.markdown("### **Round 1 Critique**")
    col3, col4 = st.columns(2)
    with col3:
        critique_chatgpt_r1 = ask_chatgpt(
            f"{CRITIQUE_CHATGPT}\n\nUser question:\n{user_question.strip()}\n\nGrok's answer:\n{grok_r1}"
        )
        ai_message_box(critique_chatgpt_r1, "ChatGPT Critique", color="#fff2d9")
    with col4:
        critique_grok_r1 = ask_grok(
            f"{CRITIQUE_GROK}\n\nUser question:\n{user_question.strip()}\n\nChatGPT's answer:\n{chatgpt_r1}",
            GROK_API_KEY
        )
        ai_message_box(critique_grok_r1, "Grok Critique", color="#eaf7ff")
    # ---- Round 2: Both answer again, having seen critique ----
    st.markdown("## **Round 2 (Improved)**")
    col5, col6 = st.columns(2)
    with col5:
        chatgpt_r2 = ask_chatgpt(
            f"{CHATGPT_VOICE}\n\nUser question:\n{user_question.strip()}\n\n"
            f"Grok's initial answer:\n{grok_r1}\n\n"
            f"Grok's critique of you:\n{critique_grok_r1}"
        )
        ai_message_box(chatgpt_r2, "ChatGPT (Improved)")
    with col6:
        grok_r2 = ask_grok(
            f"{GROK_VOICE}\n\nUser question:\n{user_question.strip()}\n\n"
            f"ChatGPT's initial answer:\n{chatgpt_r1}\n\n"
            f"ChatGPT's critique of you:\n{critique_chatgpt_r1}",
            GROK_API_KEY
        )
        ai_message_box(grok_r2, "Grok (Improved)")
    # ---- Round 2: Critique again ----
    st.markdown("### **Round 2 Critique**")
    col7, col8 = st.columns(2)
    with col7:
        critique_chatgpt_r2 = ask_chatgpt(
            f"{CRITIQUE_CHATGPT}\n\nUser question:\n{user_question.strip()}\n\nGrok's improved answer:\n{grok_r2}"
        )
        ai_message_box(critique_chatgpt_r2, "ChatGPT Critique (2nd round)", color="#fff2d9")
    with col8:
        critique_grok_r2 = ask_grok(
            f"{CRITIQUE_GROK}\n\nUser question:\n{user_question.strip()}\n\nChatGPT's improved answer:\n{chatgpt_r2}",
            GROK_API_KEY
        )
        ai_message_box(critique_grok_r2, "Grok Critique (2nd round)", color="#eaf7ff")
    # ---- Self-evaluation (optional, toggleable) ----
    show_self_eval = st.checkbox("Show each AI's self-evaluation of their final answer", value=True)
    if show_self_eval:
        col9, col10 = st.columns(2)
        with col9:
            selfeval_chatgpt = ask_chatgpt(
                f"{SELF_EVAL_CHATGPT}\n\nHere is your latest answer:\n{chatgpt_r2}"
            )
            ai_message_box(selfeval_chatgpt, "ChatGPT Self-Eval", color="#fff9e2")
        with col10:
            selfeval_grok = ask_grok(
                f"{SELF_EVAL_GROK}\n\nHere is your latest answer:\n{grok_r2}",
                GROK_API_KEY
            )
            ai_message_box(selfeval_grok, "Grok Self-Eval", color="#fff9e2")
    # ---- Synthesis and Differences ----
    st.markdown("---")
    st.subheader("🤝 **Common Ground / Synthesis**")
    synth_prompt = (
        f"{SYNTHESIZE_PROMPT}\n\nUser question:\n{user_question.strip()}\n\n"
        f"ChatGPT final answer:\n{chatgpt_r2}\n\nGrok final answer:\n{grok_r2}"
    )
    synthesis = ask_chatgpt(synth_prompt)
    st.markdown(
        f"<div style='background:#e9faed;padding:16px;border-radius:12px;font-size:1.1em;'><b>🟩 Synthesized Answer:</b><br>{synthesis}</div>",
        unsafe_allow_html=True
    )
    st.subheader("🔎 **Main Differences**")
    diff_prompt = (
        f"{DIFFERENCE_PROMPT}\n\n---\nChatGPT answer:\n{chatgpt_r2}\n---\nGrok answer:\n{grok_r2}\n---"
    )
    differences = ask_chatgpt(diff_prompt)
    st.markdown(
        f"<div style='background:#fff7e5;padding:16px;border-radius:12px;font-size:1.04em;'><b>🟥 Key Differences:</b><br>{differences}</div>",
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <div style='margin-top:18px; padding:14px; background:#f0f6ff; border-radius:12px; font-size:1.05em;'>
        💡 <b>Try another topic, or see what happens if you ask for more than two rounds!</b>
        </div>
        """,
        unsafe_allow_html=True,
    )
