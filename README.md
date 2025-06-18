## 1. **Project Summary / Review**

### **What Does SynerAI Do?**

SynerAI is a Python/Streamlit app that enables real-time orchestration between top-tier AIs (ChatGPT & Grok, with easy extension for more) to:

* **Collaborate, debate, and critique** each other’s answers to a user’s question.
* Run in three modes:

  1. **Co-Creation:** AIs refine each other’s responses and synthesize a best answer.
  2. **Enhanced Debate:** AIs critique, self-evaluate, and surface differences before synthesis.
  3. **Critical Debate:** AIs challenge each other rigorously, exposing weaknesses and then improve.
* **Synthesized output:** Final answers are merged, showing both agreement and disagreement.
* **Voice input:** Users can ask questions via microphone.
* **Session memory:** Each AI keeps context over multiple rounds.
* **Visual UX:** Distinct chat bubbles for each AI, critiques, and syntheses.

### **Code Quality & Modularity**

* **Separation of concerns:** AI logic, UI helpers, prompts, and critique analysis are in separate files.
* **Extensible:** Adding a new AI or prompt style would be easy.
* **Reusable components:** Helper functions for display and AI calls.
* **Open-source ready:** Apache 2.0 licensing in place, and code is annotated for clarity.

---

## 2. SynerAI

**SynerAI** is an open-source orchestration platform that lets the world’s best AIs debate, critique, and co-create—so you get the sharpest, most nuanced answers, every time.

> **“What happens when AIs challenge and inspire each other?”**

---

## 🚀 Features

* **Multi-AI Orchestration:** ChatGPT and Grok collaborate, debate, and critique—simultaneously.
* **Three Modes:**

  * **Co-Creation:** Synthesize the best ideas from both AIs.
  * **Enhanced Debate:** Critique, difference-spotting, and self-evaluation.
  * **Critical Debate:** Maximum challenge, flaw-exposing, and improvement.
* **Real-Time Synthesis:** Combines perspectives into a final answer for the user.
* **Visual Chat UI:** Distinct, color-coded AI bubbles and critique displays.
* **Voice Input:** Ask questions by typing or speaking.
* **Session Memory:** Each AI “remembers” previous turns for coherent conversations.
* **Plug-and-Play Extensible:** Easy to add more AI engines or new orchestration modes.
* **Open Source & Free:** Apache 2.0 licensed. No lock-in.

---

## 🖥️ Demo

---

## ⚡ Quickstart

### **1. Clone & Install**

```bash
git clone https://github.com/prototypeai100/SynerAI.git
cd SynerAI
pip install -r requirements.txt
```

### **2. Set API Keys**

* **OpenAI:** [Get an OpenAI API key](https://platform.openai.com/account/api-keys)
* **Grok:** [Get a Grok/X.ai API key](https://x.ai/)

Create a `.env` file in the project root:

```
OPENAI_API_KEY=sk-...
GROK_API_KEY=...
```

### **3. Run the App**

```bash
streamlit run ai_orchestration_app.py
```
---

## 🎮 How It Works

1. **Ask a question:** Type or use voice input.
2. **Choose a mode:** Co-creation, Enhanced Debate, or Critical Debate.
3. **Watch AIs interact:** See how each AI answers, critiques, and synthesizes.
4. **Get the best answer:** The app delivers a blended, improved result—plus critiques, self-evaluations, and (optionally) a breakdown of disagreements.

---

## 🧩 Architecture Overview

* `ai_orchestration_app.py` — Main Streamlit UI and orchestration logic.
* `ai_engines.py` — Functions to query ChatGPT and Grok.
* `prompts.py` — All system and orchestration prompts.
* `critique_impact.py` — Logic to log and analyze how critiques improved responses.
* `ui_helpers.py` — Helper to render chat bubbles for AIs, critiques, etc.

---

## 🧑‍💻 For Developers

* **Add more AIs:** Implement a new function in `ai_engines.py` and wire up in the main app.
* **Change orchestration logic:** Tweak the turn-taking or critique logic in `ai_orchestration_app.py`.
* **Customize prompts:** Modify or extend system messages in `prompts.py`.

---

## 🔒 License

Apache License 2.0.
(C) 2025 PrototypeAI100

---

## 🙌 Acknowledgments

* Built on OpenAI and X.ai APIs.
* Inspired by the dream of AI collaboration.
* Special thanks to the open-source community.

---

## 🤝 Feedback & Contact

* **Issues? Ideas?** Open a GitHub issue or pull request.
* **Contact: prototypeai100@gmail.com

---

## 🌟 Why SynerAI?

> *Most AI apps use just one model. Here, AIs debate and refine each other’s thinking, producing more balanced, insightful, and trustworthy answers. You get not just a single answer—but a spectrum of perspectives.*


 
