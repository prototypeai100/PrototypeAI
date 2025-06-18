def log_critique_impact(critique, revised_answer, ai_label):
    # This just queries ChatGPT with the CRITIQUE_IMPACT_PROMPT
    from prompts import CRITIQUE_IMPACT_PROMPT
    from ai_engines import ask_chatgpt
    prompt = (
        f"{CRITIQUE_IMPACT_PROMPT}\n\n"
        f"Critique given to {ai_label}:\n{critique}\n"
        f"{ai_label}'s revised answer:\n{revised_answer}\n"
    )
    return ask_chatgpt(prompt)
