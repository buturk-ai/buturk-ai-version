import subprocess

def ask_llm(prompt):
    try:
        result = subprocess.run(
            ["ollama", "run", "llama3", prompt],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        output = result.stdout.decode("utf-8", errors="replace")
        return output.strip()

    except Exception as e:
        return f"❌ خطأ: {str(e)}"
