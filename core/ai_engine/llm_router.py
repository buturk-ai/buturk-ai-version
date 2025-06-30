import subprocess

def run_model_direct(model: str, prompt: str):
    try:
        result = subprocess.run(
            ["ollama", "run", model, prompt],
            capture_output=True,
            text=True,
            encoding='utf-8'  # ✅ هذا يحل الترميز
        )
        return result
    except Exception as e:
        raise RuntimeError(f"حدث خطأ أثناء تشغيل ollama: {e}")
