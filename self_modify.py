import os

def self_modify():
    filename = "proxy_agent/proxy_chat_agent.py"

    # اقرأ محتوى الملف
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # السطر اللي بنضيفه داخل الدالة
    line_to_add = "        response = {'response': response, 'used_agent': '🤖 ProxyChatAgent'}\n"

    # تأكد إنه ما تم التنقيح من قبل
    if any("response = {'response': response, 'used_agent'" in line for line in lines):
        print("⚠️ التنقيح موجود مسبقًا.")
        return

    # ابحث عن return response وأضف السطر قبله
    for i, line in enumerate(lines):
        if line.strip() == "return response":
            lines[i] = line_to_add + line
            break

    # اكتب الملف من جديد
    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(lines)

    print("✅ تم التنقيح بنجاح!")

if __name__ == "__main__":
    self_modify()
