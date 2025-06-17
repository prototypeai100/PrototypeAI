# Prototype AI: Multi-AI Orchestration App

> **Curious what happens when AIs talk to each other?**
> This app lets ChatGPT and Grok debate, collaborate, and synthesize ideas—like a panel of digital minds, just for you!
>
> **Now modular! See `ai_engines.py`, `prompts.py`, and `ui_helpers.py` for better organization and easier development.**

---

[![View on GitHub](https://img.shields.io/badge/GitHub-prototypeai100/PrototypeAI-blue?logo=github)](https://github.com/prototypeai100/PrototypeAI)

---

## 🚀 What is this?

- An open-source Streamlit app to orchestrate conversations between multiple leading AIs: **ChatGPT (gpt-4-turbo)** and **Grok (grok-3-latest)**
- The AIs debate and build on each other's ideas. At the end, you get a synthesized answer, blending the best from both.
- Use this for brainstorming, tech Q&A, or to see how two AIs can disagree and converge!

---

## 🖥️ Live Demo & Channel

- [YouTube: Prototype AI](https://www.youtube.com/@PrototypeAI01)
- *(Live public demo: coming soon!)*

---

## 📝 Features

- **True Orchestration:** Both AIs answer, critique, and build upon each other's ideas.
- **Session Memory:** The app remembers your ongoing discussion in each session.
- **Synthesis:** After orchestrating, both AIs co-create a final answer for you.
- **Multiple Modes:** Co-Creation (default), with roadmap for “Competitive” and “Critical” debate.
- **User Tip:** For quick, easy-to-read answers, just add "Keep your answer under 150 words."
- **API Cost Estimate:** See your token usage for OpenAI.
- **Security:** API keys are loaded via environment variables only—never commit secrets!
- **Beginner Friendly:** Detailed setup instructions below.

---

## ⚡ Quick Start

1. **Clone this repo:**
    ```bash
    git clone https://github.com/prototypeai100/PrototypeAI.git
    cd PrototypeAI
    ```

2. **Install Python 3.8+ (not 3.7 or below):**
    - [Download Python](https://www.python.org/downloads/)

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Get your API keys:**  
   - [OpenAI (ChatGPT)](https://chatgpt.com) *(sign in for API and usage)*  
   - [Grok (xAI)](https://grok.com) *(sign in for access or API keys—currently by invitation or paid plan)*

5. **Create your `.env` file:**  
   *(never commit your real keys! use `.env.example` as a template)*

6. **Run the app:**
    ```bash
    streamlit run ai_orchestration_app.py
    ```

7. **Ask your question and watch the AIs debate and synthesize an answer for you!**

---

## 🗂️ Code Structure (as of June 2025)

After June 2025, the project code is modularized for easier maintenance and extension:

