from core.ai_engine.llm_router import run_model_direct

models = ["llama3:latest", "codellama:34b", "deepseek-coder:latest"]
prompt = "اكتب كود بايثون يطبع الأرقام من 1 إلى 10"

for model in models:
    print(f"\n🔍 اختبار النموذج: {model}")
    try:
        result = run_model_direct(model=model, prompt=prompt)

        output = ""
        if result.stdout:
            output = result.stdout if isinstance(result.stdout, str) else result.stdout.decode('utf-8', errors='ignore')
        elif result.stderr:
            output = result.stderr if isinstance(result.stderr, str) else result.stderr.decode('utf-8', errors='ignore')

        print(f"✅ النتيجة:\n{output.strip() if output else '🚫 لم يتم استلام نتيجة'}\n")

    except Exception as e:
        print(f"❌ خطأ أثناء تشغيل النموذج {model}: {e}")
