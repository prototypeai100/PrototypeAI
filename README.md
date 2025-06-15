# Prototype AI: Multi-AI Orchestration App

![Prototype AI Banner](assets/PrototypeAI_Banner.png)

> **Curious what happens when AIs talk to each other?**
> This app lets ChatGPT and Grok debate, collaborate, and synthesize ideas—like a panel of digital minds, just for you!

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
   - [OpenAI (ChatGPT)](https://platform.openai.com/api-keys)  
   - [Grok (xAI)](https://x.ai) *(currently by invitation or paid plan)*

5. **Create your `.env` file:**  
   *(never commit your real keys! use `.env.example` as a template)*

6. **Run the app:**
    ```bash
    streamlit run ai_orchestration_app.py
    ```

7. **Ask your question and watch the AIs debate and synthesize an answer for you!**

---

## 🔎 Multi-AI Uniqueness Reviews

We regularly ask the world’s leading AIs (Perplexity, Grok, Claude, ChatGPT, Gemini, and others) to check if this project is truly unique, and to evaluate its value for society.

**Read the latest results:**  
[2025-06-14-uniqueness-review.md](2025-06-14-uniqueness-review.md)

---

## 🛣️ Roadmap & Future Vision

- **Multimedia Support:**  
  Enable video, audio, and image inputs/outputs, so users can interact with AIs not just via text, but also with voice, video, and other media.  
  *Imagine uploading a video or speaking your question to get a real-time AI panel debate—making the experience richer and more accessible to everyone.*

- **Business & Commercial Applications:**  
  This approach empowers new businesses to **leverage multiple AIs for smarter, more adaptive solutions**. Enterprises and developers can select the best AI for each use case, combine insights from different engines, and offer users true freedom—**letting anyone pick or blend the right AI at any moment**.

- **Freedom of AI Choice:**  
  Our vision is to let users orchestrate, mix, and match any number of AIs—unlocking creativity and innovation in personal and professional contexts.  
  *The future is open, collaborative, and user-powered.*

- **Scalability & Extensibility:**  
  Plans to add support for more AI engines (Claude, Gemini, etc.) and custom orchestration logic, so anyone can build their own AI “panel of experts.”

---

## 🤝 Contributing

- Open to feedback, issues, and pull requests!
- See [issues](https://github.com/prototypeai100/PrototypeAI/issues) or suggest new features via GitHub.

---

## 📄 License

This project is licensed under the [Apache 2.0 License](LICENSE).

---

## ⭐ Stay in Touch

- [YouTube: Prototype AI](https://www.youtube.com/@PrototypeAI01)
- [GitHub: prototypeai100/PrototypeAI](https://github.com/prototypeai100/PrototypeAI)
