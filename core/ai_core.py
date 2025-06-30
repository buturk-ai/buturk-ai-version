# core/ai_core.py
import requests

OLLAMA_URL = "http://localhost:11435/api/generate"
MODEL = "llama3"

def ask_llm(prompt, system=""):
    prompt = f"""
أجب باللغة العربية الفصحى فقط.
كن ذكيًا، مختصرًا، واضحًا.
لا تشرح إن لم يُطلب منك.

السؤال:
{prompt}
    """

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "system": system,
        "stream": False,
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=60)
        return response.json()['response']
    except Exception as e:
        return f"[LLM ERROR]: {str(e)}"
