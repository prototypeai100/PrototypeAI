import openai
import requests
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GROK_API_KEY = os.getenv("GROK_API_KEY")

openai.api_key = OPENAI_API_KEY

def ask_chatgpt(prompt, history=None, system="You are ChatGPT, a thoughtful, detail-oriented AI."):
    messages = [{"role": "system", "content": system}]
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

def ask_grok(prompt, api_key=GROK_API_KEY, history=None, system="You are Grok, a concise, creative, slightly witty AI."):
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
