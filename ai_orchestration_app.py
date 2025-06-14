# =============================================================================
#  Copyright 2025 prototypeai100
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
# =============================================================================

import streamlit as st
import openai
import requests
import os
from dotenv import load_dotenv

# ========== API Key & Security Notes ==========
load_dotenv()  # Loads .env from the current directory if present

st.set_page_config(
    page_title="🧑 ➡️ 🤖🤝🤖 ➡️ 🧑  AI-to-AI Debate & Co-Creation",
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

def ai_message_box(content, who):
    if who == "ChatGPT":
        color = CHATGPT_COLOR
        icon = "🧠"
    elif who == "Grok":
        color = GROK_COLOR
        icon = "🤖"
    else:
        color = "#e6f0fa"
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
total_openai_tokens = 0

def ask_chatgpt(prompt, history=None, system="You are ChatGPT, a thoughtful, detail-oriented AI."):
    global total_openai_tokens
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
    try:
        if hasattr(response, "usage") and hasattr(response.usage, "total_tokens"):
            total_openai_tokens += response.usage.total_tokens
    except Exception:
        pass
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

SYNTHESIZE_PROMPT = (
    "Imagine you're a friendly and enthusiastic moderator, summarizing the best ideas from a creative AI panel. "
    "Your job is to combine the top points from ChatGPT and Grok into one clear, engaging answer that would excite a curious YouTube viewer. "
    "Keep the tone upbeat, approachable, and a bit conversational—like explaining something cool to a friend. "
    "Encourage people to try the app or join the discussion themselves. "
    "For complicated topics, use short bullet points or a simple table for clarity."
)

# ========== MAIN TITLE (ALWAYS ON TOP) ==========
st.markdown("""
# 🧑‍💻 ➡️ 🤖🤝🤖 ➡️ 🧑
### AI-to-AI Debate & Co-Creation, Centered on You
""")

# ========== TOP EXPANDER: HOW IT WORKS & MODES & FLOW ==========
with st.expander("How It Works: Modes & Flow"):
    st.markdown("""
**You start the conversation at your computer.  
AIs debate and co-create—and the best answers come back, just for you!**

**Co-Creation:** Both AIs build, debate, and synthesize ideas (default mode, runs on 'Run Co-Creation').  
**Competitive & Critical:** Advanced orchestration modes—coming soon! See roadmap below.

---

**Co-Creation Mode (default):**
- You enter a topic or question.
- ChatGPT and Grok each respond in their own style.
- The AIs critique, debate, and build on each other's answers.
- At the end, their best points are combined into one final, synthesized answer—by BOTH AIs!

**Competitive Mode:**
- Each AI is rewarded for outperforming the other—whether by creativity, clarity, or persuasive power.  
*Goal: Simulate a competition where the best ideas, arguments, or insights rise to the top, not just agreement.*

**Critical Mode:**
- Both AIs rigorously critique and challenge each other, focusing on logical flaws, factual accuracy, and missing perspectives.  
*Goal: Simulate an in-depth debate, stress-testing each AI’s reasoning, and surfacing the strongest, most reliable arguments.*
""")

# ========== MODEL & CHARGE PANELS SIDE BY SIDE ==========
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div style='background:#eef2ff; border-radius:7px; padding:14px 18px; margin-bottom:2px; font-size:1.07em;'>
    <b>📌 Current AI Models</b><br>
    ChatGPT Model: <span style='color:#1e88e5'>gpt-4-turbo</span><br>
    Grok Model: <span style='color:#10a37f'>grok-3-latest</span>
    </div>
    """, unsafe_allow_html=True)
with col2:
    if total_openai_tokens > 0:
        estimated_cost = total_openai_tokens / 1_000_000 * 10  # $10/1M tokens output (update as needed)
        gpt_cost_str = f"${estimated_cost:.4f}"
    else:
        gpt_cost_str = "$0.0000"
    st.markdown(f"""
    <div style='background:#fef6e0; border-radius:7px; padding:14px 18px; margin-bottom:2px; font-size:1.07em;'>
    <b>💰 Estimated API Charges (Pseudo Estimate)</b><br>
    ChatGPT (GPT-4-turbo): {gpt_cost_str} <span style='color:#aaa'>(Display only, not guaranteed accurate)</span><br>
    Grok: <span style='color:#999'>Unknown (xAI does not provide cost info)</span><br>
    <small>Note: ChatGPT cost estimate is for reference only. Always check your OpenAI dashboard for billing.</small>
    </div>
    """, unsafe_allow_html=True)

# ========== USER TIP & INPUT ==========
st.markdown(
    "<div style='color:#666;font-size:1.04em;margin-bottom:6px;'>"
    "💡 <b>Tip:</b> For a fast, easy-to-read answer, just add: <i>“Keep your answer under 150 words.”</i>"
    "</div>",
    unsafe_allow_html=True,
)

user_question = st.text_area(
    "",
    height=100,
    placeholder="Describe a question, challenge, or topic for ChatGPT and Grok to debate and co-create an answer."
)

# ========== FUNCTIONAL BUTTONS IN A ROW ==========
colA, colB, colC = st.columns([1, 1, 1])
with colA:
    run_btn = st.button("▶️ Run Co-Creation", key="co_creation", use_container_width=True)
with colB:
    critical_mode = st.button("🛡️ Try Critical Mode (In Development)", key="critical", use_container_width=True)
with colC:
    competitive_mode = st.button("🏆 Try Competitive Mode (In Development)", key="competitive", use_container_width=True)

if critical_mode:
    st.warning("Critical Mode is currently a placeholder. In the future, AIs will debate more aggressively, seeking to expose each other’s weaknesses before synthesizing the best answer. (See developer roadmap.)")
if competitive_mode:
    st.warning("Competitive Mode is currently a placeholder. In the future, AIs will strive to outperform each other, and the app will highlight the most original, insightful, or compelling answer. (See developer roadmap.)")

with st.expander("🛠️ Developer Reminders / Roadmap"):
    st.markdown("""
- **Implement Critical Mode:** Add advanced orchestration where AIs "debate" and rigorously critique each other.
- **Implement Competitive Mode:** Add orchestration where AIs are rewarded for being more accurate, creative, or insightful than the other.
- **Session Memory:** Use Streamlit `st.session_state` to persist chat histories, enabling ongoing conversations—like ChatGPT and Grok web UIs.
- **User Suggestion for Short Answers:** Remind users to specify a word limit (e.g., “under 150 words”) for quick, easy-to-read answers.
- **Unified Error Handling:** Centralize API error management for robustness.
- **Security:** Use only environment variables for secrets. Avoid any plaintext files.
- **Shared Logic for AI Calls:** If API schemas converge, merge ask_chatgpt/ask_grok logic.
- **Feedback Loop / Self-improvement:** Plan for iterative prompting or learning from prior outcomes.
- **User/Dev UI Separation:** Allow toggling developer info so end users aren’t confused.
- **Metrics & Logging:** Add usage analytics and outcome evaluation.
- **Documentation:** Write usage and dev docs.
- **Testing:** Add unit/integration tests for orchestration logic.
- **Round Control:** Allow user or developer to select number of debate rounds (e.g., 3, 5, or 10). See round control pseudo-code below.
""")

# ====== ROUND CONTROL PSEUDO-CODE ======
# (unchanged, omitted for brevity)

# ========== MAIN LOGIC ==========

proceed_3 = st.button("Proceed 3 More Rounds (Pseudo)")
proceed_5 = st.button("Proceed 5 More Rounds (Pseudo)")
proceed_10 = st.button("Proceed 10 More Rounds (Pseudo)")

# === SESSION MEMORY: Persist chat history per session ===
if 'chatgpt_history' not in st.session_state:
    st.session_state['chatgpt_history'] = []
if 'grok_history' not in st.session_state:
    st.session_state['grok_history'] = []

if run_btn and user_question.strip():
    chatgpt_history = []
    grok_history = []

    # === Always 2 Rounds as before ===
    num_rounds = 2
    for i in range(num_rounds):
        if i == 0:
            gpt_prompt = f"{CHATGPT_VOICE}\n\nUser question:\n{user_question.strip()}"
        else:
            gpt_prompt = f"{CHATGPT_VOICE}\n\nUser question:\n{user_question.strip()}\n\nPrevious Grok draft:\n{grok_response}"
        gpt_response = ask_chatgpt(gpt_prompt, history=st.session_state['chatgpt_history'])
        ai_message_box(gpt_response, "ChatGPT")
        chatgpt_history.append({"role": "assistant", "content": gpt_response})

        grok_prompt = f"{GROK_VOICE}\n\nUser question:\n{user_question.strip()}\n\nPrevious ChatGPT draft:\n{gpt_response}"
        grok_response = ask_grok(grok_prompt, GROK_API_KEY, history=st.session_state['grok_history'])
        ai_message_box(grok_response, "Grok")
        grok_history.append({"role": "assistant", "content": grok_response})

        # Save to session for true session memory
        st.session_state['chatgpt_history'] += [{"role": "user", "content": user_question.strip()}] if i == 0 else []
        st.session_state['chatgpt_history'].append({"role": "assistant", "content": gpt_response})
        st.session_state['grok_history'] += [{"role": "user", "content": user_question.strip()}] if i == 0 else []
        st.session_state['grok_history'].append({"role": "assistant", "content": grok_response})

    # === SYNTHESIS PROMPT ===
    synthesis_prompt = (
        f"{SYNTHESIZE_PROMPT}\n\n"
        f"User question:\n{user_question.strip()}\n\n"
        f"Latest ChatGPT draft:\n{gpt_response}\n\n"
        f"Latest Grok draft:\n{grok_response}\n"
    )
    final_synthesis_chatgpt = ask_chatgpt(synthesis_prompt)
    final_synthesis_grok = ask_grok(synthesis_prompt, GROK_API_KEY)

    # Display both side by side
    col1, col2 = st.columns(2)
    with col1:
        ai_message_box(final_synthesis_chatgpt, "ChatGPT Synthesis")
    with col2:
        ai_message_box(final_synthesis_grok, "Grok Synthesis")

    st.markdown(
        """
        <div style='margin-top:28px; padding:18px; background:#f4efe5; border-radius:14px; font-size:1.13em; box-shadow:0 2px 8px #0001'>
        💡 <b>What would YOU ask our AI panel?</b><br>
        Drop your wildest question above and see how the AIs team up to answer.<br>
        <br>
        🚀 Curious about the code or want to join the project?<br>
        <a href='https://github.com/prototypeai100/PrototypeAI' target='_blank'><b>View it on GitHub</b></a> | 
        <a href='https://www.youtube.com/@PrototypeAI01' target='_blank'><b>Watch the journey on YouTube</b></a>
        </div>
        """,
        unsafe_allow_html=True,
    )

# === PSEUDO CONTINUE BUTTON LOGIC ===
if proceed_3:
    st.info("Pseudo: Would proceed 3 more rounds of AI-to-AI exchange here (not yet implemented).")
if proceed_5:
    st.info("Pseudo: Would proceed 5 more rounds of AI-to-AI exchange here (not yet implemented).")
if proceed_10:
    st.info("Pseudo: Would proceed 10 more rounds of AI-to-AI exchange here (not yet implemented).")

# ================= END OF FILE =================
