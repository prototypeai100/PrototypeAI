# =============================================================================
#  Copyright 2025 prototypeai100
#  Licensed under the Apache License, Version 2.0 (the "License");
#  http://www.apache.org/licenses/LICENSE-2.0
# =============================================================================

import streamlit as st
import openai
import requests
import os
from dotenv import load_dotenv

# NEW: For voice input
from audio_recorder_streamlit import audio_recorder
import speech_recognition as sr
import tempfile

# --- Modular imports (if separated, else keep helpers here)
# from ai_engines import ask_chatgpt, ask_grok
# from prompts import *
# from critique_impact import log_critique_impact
# from ui_helpers import ai_message_box, show_critique_impact

load_dotenv()

# 🧑 ➡️ 🤖🤝🤖 ➡️ 🧑 (reserve for future) 

st.set_page_config(
    page_title="AI-to-AI Orchestration", 
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

openai.api_key = OPENAI_API_KEY

# ========== STYLE HELPERS ==========
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
    elif "impact" in who.lower():
        color = "#e6f6f6"
        icon = "🧩"
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

# ========== AI QUERY FUNCTIONS ==========
def ask_chatgpt(prompt, history=None, system="You are ChatGPT, a thoughtful, detail-oriented AI."):
    messages = [
        {"role": "system", "content": system}
    ]
    if history:
        messages += history
    messages.append({"role": "user", "content": prompt})
    response = openai.chat.completions.create(
        model="gpt-4-turbo",
        messages=messages,
        max_tokens=2048,
        temperature=0.5
    )
    return response.choices[0].message.content.strip()

def ask_grok(prompt, api_key, history=None, system="You are Grok, a concise, creative, slightly witty AI."):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    messages = [{"role": "system", "content": system}]
    if history:
        messages += history
    messages.append({"role": "user", "content": prompt})
    data = {
        "model": "grok-3-latest",
        "messages": messages,
        "max_tokens": 2048,
        "temperature": 0.5
    }
    response = requests.post("https://api.x.ai/v1/chat/completions", headers=headers, json=data, timeout=60)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"].strip()

# ========== PROMPT HELPERS ==========
CHATGPT_VOICE = (
    "You are ChatGPT, an analytical, detail-oriented AI. "
    "After reading the prior draft(s), produce your answer in your own distinct voice: formal, thorough, and structured. "
    "AVOID repeating wording or content from the previous response—eliminate all redundancy. "
    "If the subject is technical or lengthy, use bullet lists or tables for clarity. "
    "If the prior AI brought up points you disagree with or think need refinement, state it respectfully and clearly. "
    "Begin your answer with: 'As ChatGPT, here’s my perspective:'"
)

GROK_VOICE = (
    "You are Grok, a creative, insightful, and concise AI with a slightly informal, conversational style. "
    "After reading the previous ChatGPT draft, produce your answer in your own distinct voice—more direct, witty, and human. "
    "Eliminate redundancy from previous drafts. If you can, rephrase or condense for brevity without losing meaning. "
    "For complex or technical topics, summarize with bullets or a table. "
    "If you disagree or wish to add nuance, state it openly, not as a review, but as a natural conversation. "
    "Begin your answer with: 'Hey, here’s Grok’s take:'"
)

CRITIQUE_CHATGPT = (
    "You are ChatGPT, an expert AI debate judge. Carefully read the previous answer by Grok and analyze it for any logical flaws, inaccuracies, or points needing clarification. "
    "Give a constructive but direct critique, mentioning strengths briefly and focusing on what could be improved, clarified, or corrected. "
    "Begin your response: 'As ChatGPT, here’s my critique of Grok’s answer:'"
)

CRITIQUE_GROK = (
    "You are Grok, a sharp and witty AI. Your job is to critically evaluate ChatGPT's previous answer. Point out any gaps, mistakes, or areas for improvement, and do so with your usual direct, informal style. "
    "Highlight strengths only briefly. "
    "Begin your response: 'Hey, Grok here—here’s what I think about ChatGPT’s answer:'"
)

CRITIQUE_IMPACT_PROMPT = (
    "Given the following critique and the next-round response, analyze which specific critique points led to major changes or improvements in the next answer. "
    "List the key points from the critique and, for each, state if it was addressed (and how) in the revised answer. Use a bullet list or a table."
)

SELF_EVAL_CHATGPT = (
    "Reflect on your latest answer as ChatGPT. What did you do well, what could be improved, and what would you do differently next time? Keep it honest and analytical."
)

SELF_EVAL_GROK = (
    "Reflect on your latest answer as Grok. What was your strongest point, and what would you do differently next round? Be concise and direct."
)

SYNTHESIZE_PROMPT = (
    "Imagine you're a friendly and enthusiastic moderator, summarizing the best ideas from a creative AI panel. "
    "Your job is to combine the top points from ChatGPT and Grok into one clear, engaging answer that would excite a curious YouTube viewer. "
    "Keep the tone upbeat, approachable, and a bit conversational—like explaining something cool to a friend. "
    "Encourage people to try the app or join the discussion themselves. "
    "For complicated topics, use short bullet points or a simple table for clarity."
)

DIFFERENCE_PROMPT = (
    "You are an impartial AI moderator. Compare the following two AI answers. List the main differences or disagreements in a clear, concise bullet list. "
    "Focus on substantive points, not style or phrasing."
)

DEBATE_SUMMARY_PROMPT = (
    "You are an impartial moderator. Summarize the debate between ChatGPT and Grok, focusing on the key points of disagreement, the flaws or weaknesses each AI found in the other's arguments, "
    "and any major changes in position or content over each round. Present the summary in a clear, readable format, using bullet points or a table if helpful."
)
# ------------- END OF PROMPTS --------------

# ========== MAIN TITLE ==========
st.markdown("""
### 🤖AI-to-AI Orchestration: Co-Creation, Enhanced & Critical Debate Modes
""")

# ========== USER INPUT ==========

user_text = st.text_area(
    "",
    height=100,
    placeholder="Ask anything, Grok and ChatGPT team up for your answer.",
    key="keyboard_input"
)

audio_bytes = audio_recorder(text="Microphone Input. If both text and voice are used, the voice input will take priority", pause_threshold=1.5, key="voice_input")
voice_text = ""

if audio_bytes:
    st.audio(audio_bytes, format="audio/wav")
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
        f.write(audio_bytes)
        temp_filename = f.name
    recognizer = sr.Recognizer()
    with sr.AudioFile(temp_filename) as source:
        audio = recognizer.record(source)
    try:
        voice_text = recognizer.recognize_google(audio)
        st.success(f"🎤 Recognized Voice Input: {voice_text}")
    except sr.UnknownValueError:
        st.warning("Could not understand audio. Please try again.")
    except Exception as e:
        st.warning(f"Error recognizing audio: {e}")
    finally:
        os.remove(temp_filename)

# Use voice input if available, else text input
final_user_prompt = voice_text if voice_text else user_text

# ========== FUNCTIONAL BUTTONS ==========
colA, colB, colC = st.columns([1, 1, 1])
with colA:
    run_btn = st.button("▶️ Run Co-Creation", key="co_creation", use_container_width=True)
with colB:
    enhanced_btn = st.button("🤺 Run Enhanced Debate", key="enhanced_debate", use_container_width=True)
with colC:
    critical_btn = st.button("🔥 Run Critical Debate", key="critical_debate", use_container_width=True)

# ========== MAIN LOGIC ==========

# --- (EXISTING) Co-Creation Mode ---
if run_btn and final_user_prompt.strip():
    st.markdown("## **Co-Creation (Default)**")
    chatgpt_history = []
    grok_history = []
    num_rounds = 2
    for i in range(num_rounds):
        if i == 0:
            gpt_prompt = f"{CHATGPT_VOICE}\n\nUser question:\n{final_user_prompt.strip()}"
        else:
            gpt_prompt = f"{CHATGPT_VOICE}\n\nUser question:\n{final_user_prompt.strip()}\n\nPrevious Grok draft:\n{grok_response}"
        gpt_response = ask_chatgpt(gpt_prompt, history=chatgpt_history)
        ai_message_box(gpt_response, "ChatGPT")
        chatgpt_history.append({"role": "assistant", "content": gpt_response})

        grok_prompt = f"{GROK_VOICE}\n\nUser question:\n{final_user_prompt.strip()}\n\nPrevious ChatGPT draft:\n{gpt_response}"
        grok_response = ask_grok(grok_prompt, GROK_API_KEY, history=grok_history)
        ai_message_box(grok_response, "Grok")
        grok_history.append({"role": "assistant", "content": grok_response})

    # Synthesis
    synthesis_prompt = (
        f"{SYNTHESIZE_PROMPT}\n\nUser question:\n{final_user_prompt.strip()}\n\n"
        f"Latest ChatGPT draft:\n{gpt_response}\n\n"
        f"Latest Grok draft:\n{grok_response}\n"
    )
    final_synthesis = ask_chatgpt(synthesis_prompt)
    st.markdown(
        f"<div style='background:#e9faed;padding:16px;border-radius:12px;font-size:1.1em;'><b>🟩 Synthesized Answer:</b><br>{final_synthesis}</div>",
        unsafe_allow_html=True
    )

# --- Enhanced Debate Mode ---
if enhanced_btn and final_user_prompt.strip():
    st.markdown("## **Enhanced Debate: 2 Rounds, Critique, Synthesis & Differences**")
    # Round 1
    col1, col2 = st.columns(2)
    with col1:
        chatgpt_r1 = ask_chatgpt(f"{CHATGPT_VOICE}\n\nUser question:\n{final_user_prompt.strip()}")
        ai_message_box(chatgpt_r1, "ChatGPT")
    with col2:
        grok_r1 = ask_grok(f"{GROK_VOICE}\n\nUser question:\n{final_user_prompt.strip()}", GROK_API_KEY)
        ai_message_box(grok_r1, "Grok")
    # Critiques
    st.markdown("### **Round 1 Critique**")
    col3, col4 = st.columns(2)
    with col3:
        critique_chatgpt_r1 = ask_chatgpt(
            f"{CRITIQUE_CHATGPT}\n\nUser question:\n{final_user_prompt.strip()}\n\nGrok's answer:\n{grok_r1}"
        )
        ai_message_box(critique_chatgpt_r1, "ChatGPT Critique", color="#fff2d9")
    with col4:
        critique_grok_r1 = ask_grok(
            f"{CRITIQUE_GROK}\n\nUser question:\n{final_user_prompt.strip()}\n\nChatGPT's answer:\n{chatgpt_r1}",
            GROK_API_KEY
        )
        ai_message_box(critique_grok_r1, "Grok Critique", color="#eaf7ff")
    # Round 2: improved
    st.markdown("## **Round 2 (Improved)**")
    col5, col6 = st.columns(2)
    with col5:
        chatgpt_r2 = ask_chatgpt(
            f"{CHATGPT_VOICE}\n\nUser question:\n{final_user_prompt.strip()}\n\n"
            f"Grok's initial answer:\n{grok_r1}\n\n"
            f"Grok's critique of you:\n{critique_grok_r1}"
        )
        ai_message_box(chatgpt_r2, "ChatGPT (Improved)")
    with col6:
        grok_r2 = ask_grok(
            f"{GROK_VOICE}\n\nUser question:\n{final_user_prompt.strip()}\n\n"
            f"ChatGPT's initial answer:\n{chatgpt_r1}\n\n"
            f"ChatGPT's critique of you:\n{critique_chatgpt_r1}",
            GROK_API_KEY
        )
        ai_message_box(grok_r2, "Grok (Improved)")
    # Critiques again
    st.markdown("### **Round 2 Critique**")
    col7, col8 = st.columns(2)
    with col7:
        critique_chatgpt_r2 = ask_chatgpt(
            f"{CRITIQUE_CHATGPT}\n\nUser question:\n{final_user_prompt.strip()}\n\nGrok's improved answer:\n{grok_r2}"
        )
        ai_message_box(critique_chatgpt_r2, "ChatGPT Critique (2nd round)", color="#fff2d9")
    with col8:
        critique_grok_r2 = ask_grok(
            f"{CRITIQUE_GROK}\n\nUser question:\n{final_user_prompt.strip()}\n\nChatGPT's improved answer:\n{chatgpt_r2}",
            GROK_API_KEY
        )
        ai_message_box(critique_grok_r2, "Grok Critique (2nd round)", color="#eaf7ff")
    # Self-eval
    show_self_eval = st.checkbox("Show each AI's self-evaluation of their final answer", value=True)
    if show_self_eval:
        col9, col10 = st.columns(2)
        with col9:
            selfeval_chatgpt = ask_chatgpt(
                f"{SELF_EVAL_CHATGPT}\n\nHere is your latest answer:\n{chatgpt_r2}"
            )
            ai_message_box(selfeval_chatgpt, "ChatGPT Self-Eval", color=SELF_EVAL_COLOR)
        with col10:
            selfeval_grok = ask_grok(
                f"{SELF_EVAL_GROK}\n\nHere is your latest answer:\n{grok_r2}",
                GROK_API_KEY
            )
            ai_message_box(selfeval_grok, "Grok Self-Eval", color=SELF_EVAL_COLOR)
    # Synthesis and differences
    st.markdown("---")
    st.subheader("🤝 **Common Ground / Synthesis**")
    synth_prompt = (
        f"{SYNTHESIZE_PROMPT}\n\nUser question:\n{final_user_prompt.strip()}\n\n"
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

    # NEW: Critique impact logging
    st.subheader("🧩 Critique Impact Analysis")
    impact_prompt = (
        f"{CRITIQUE_IMPACT_PROMPT}\n\n"
        f"Critique given to ChatGPT:\n{critique_grok_r1}\n"
        f"ChatGPT's revised answer:\n{chatgpt_r2}\n\n"
        f"Critique given to Grok:\n{critique_chatgpt_r1}\n"
        f"Grok's revised answer:\n{grok_r2}"
    )
    impact_analysis = ask_chatgpt(impact_prompt)
    ai_message_box(impact_analysis, "Critique Impact Log", color="#e6f6f6")

# --- Critical Debate Mode ---
if critical_btn and final_user_prompt.strip():
    st.markdown("## **Critical Debate: Two Rounds of Maximum Critique**")
    # Round 1: max critique
    col1, col2 = st.columns(2)
    with col1:
        chatgpt_r1 = ask_chatgpt(f"{CHATGPT_VOICE}\n\nUser question:\n{final_user_prompt.strip()}")
        ai_message_box(chatgpt_r1, "ChatGPT")
    with col2:
        grok_r1 = ask_grok(f"{GROK_VOICE}\n\nUser question:\n{final_user_prompt.strip()}", GROK_API_KEY)
        ai_message_box(grok_r1, "Grok")
    # Critical critiques
    st.markdown("### **Round 1: Critical Attack**")
    col3, col4 = st.columns(2)
    with col3:
        critique_chatgpt_r1 = ask_chatgpt(
            f"{CRITIQUE_CHATGPT}\n\n(Go deeper than usual, be highly rigorous and critical. Identify all possible flaws, weaknesses, missing evidence, and unexamined assumptions.)\n\nUser question:\n{final_user_prompt.strip()}\n\nGrok's answer:\n{grok_r1}"
        )
        ai_message_box(critique_chatgpt_r1, "ChatGPT Critique (Critical)", color="#fff2d9")
    with col4:
        critique_grok_r1 = ask_grok(
            f"{CRITIQUE_GROK}\n\n(Go deeper than usual, be highly rigorous and critical. Identify all possible flaws, weaknesses, missing evidence, and unexamined assumptions.)\n\nUser question:\n{final_user_prompt.strip()}\n\nChatGPT's answer:\n{chatgpt_r1}",
            GROK_API_KEY
        )
        ai_message_box(critique_grok_r1, "Grok Critique (Critical)", color="#eaf7ff")
    # Round 2: respond after being attacked
    st.markdown("## **Round 2: Rebuttal / Improved Answer**")
    col5, col6 = st.columns(2)
    with col5:
        chatgpt_r2 = ask_chatgpt(
            f"{CHATGPT_VOICE}\n\nAfter a highly critical critique, respond with your improved answer.\n\n"
            f"User question:\n{final_user_prompt.strip()}\n\n"
            f"Grok's initial answer:\n{grok_r1}\n\n"
            f"Grok's critique of you:\n{critique_grok_r1}"
        )
        ai_message_box(chatgpt_r2, "ChatGPT (Improved After Critique)")
    with col6:
        grok_r2 = ask_grok(
            f"{GROK_VOICE}\n\nAfter a highly critical critique, respond with your improved answer.\n\n"
            f"User question:\n{final_user_prompt.strip()}\n\n"
            f"ChatGPT's initial answer:\n{chatgpt_r1}\n\n"
            f"ChatGPT's critique of you:\n{critique_chatgpt_r1}",
            GROK_API_KEY
        )
        ai_message_box(grok_r2, "Grok (Improved After Critique)")
    # Second round of critiques (optional)
    st.markdown("### **Round 2: Rebuttal Critiques**")
    col7, col8 = st.columns(2)
    with col7:
        critique_chatgpt_r2 = ask_chatgpt(
            f"{CRITIQUE_CHATGPT}\n\nFocus on whether Grok's improved answer addressed your prior critiques, and what new weaknesses remain.\n\nUser question:\n{final_user_prompt.strip()}\n\nGrok's improved answer:\n{grok_r2}"
        )
        ai_message_box(critique_chatgpt_r2, "ChatGPT Critique (Rebuttal)", color="#fff2d9")
    with col8:
        critique_grok_r2 = ask_grok(
            f"{CRITIQUE_GROK}\n\nFocus on whether ChatGPT's improved answer addressed your prior critiques, and what new weaknesses remain.\n\nUser question:\n{final_user_prompt.strip()}\n\nChatGPT's improved answer:\n{chatgpt_r2}",
            GROK_API_KEY
        )
        ai_message_box(critique_grok_r2, "Grok Critique (Rebuttal)", color="#eaf7ff")
    # Synthesis and flaw summary
    st.markdown("---")
    st.subheader("🟩 **Critical Synthesis: Main Contested Flaws**")
    synthesis_prompt = (
        f"{DEBATE_SUMMARY_PROMPT}\n\n"
        f"User question:\n{final_user_prompt.strip()}\n\n"
        f"ChatGPT's critique of Grok (Round 1):\n{critique_chatgpt_r1}\n\n"
        f"Grok's critique of ChatGPT (Round 1):\n{critique_grok_r1}\n\n"
        f"ChatGPT improved answer:\n{chatgpt_r2}\n\n"
        f"Grok improved answer:\n{grok_r2}\n"
    )
    synthesis = ask_chatgpt(synthesis_prompt)
    st.markdown(
        f"<div style='background:#e9faed;padding:16px;border-radius:12px;font-size:1.1em;'><b>🟩 Synthesis:</b><br>{synthesis}</div>",
        unsafe_allow_html=True
    )
    # NEW: Critique impact
    st.subheader("🧩 Critique Impact Analysis (Critical Debate)")
    impact_prompt = (
        f"{CRITIQUE_IMPACT_PROMPT}\n\n"
        f"Critique given to ChatGPT:\n{critique_grok_r1}\n"
        f"ChatGPT's revised answer:\n{chatgpt_r2}\n\n"
        f"Critique given to Grok:\n{critique_chatgpt_r1}\n"
        f"Grok's revised answer:\n{grok_r2}"
    )
    impact_analysis = ask_chatgpt(impact_prompt)
    ai_message_box(impact_analysis, "Critique Impact Log", color="#e6f6f6")

# ================= END OF FILE =================
