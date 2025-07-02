# web_learning/summarizer.py

def summarize_text(text, max_length=1000):
    if len(text) <= max_length:
        return text
    return text[:max_length] + "..."
