# Prototype AI: Multi-AI Orchestration App

![Prototype AI Banner](assets/PrototypeAI_Banner.png)

> **Curious what happens when AIs talk to each other?**
> This app lets ChatGPT and Grok debate, collaborate, and synthesize ideas—like a panel of digital minds, just for you!

---

## 🚀 What is this?

- An open-source Streamlit app to orchestrate conversations between two leading AIs: **ChatGPT (gpt-4-turbo)** and **Grok (grok-3-latest)**
- The AIs debate and build on each other's ideas. At the end, you get a synthesized answer, blending the best from both.
- You can use this for brainstorming, tech Q&A, or just to see how two AIs can disagree and converge!

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
    git clone https://github.com/yourusername/PrototypeAI.git
    cd PrototypeAI
    ```

2. **Install Python 3.8+ (not 3.7 or below):**
    - [Download Python](https://www.python.org/downloads/)

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Get your API keys:**  
   - [OpenAI (ChatGPT)](https://platform.openai.com/api-keys)  
   - [Grok (xAI)](https://x.ai) *(currently by invitation or paid plan)*

5. **Create your `.env` file:**  
   *(never commit your real keys! use `.env.example` as a template)*  
