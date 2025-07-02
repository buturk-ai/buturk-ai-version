# gui/chat_window.py

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QLineEdit, QPushButton, QLabel
from PyQt5.QtCore import Qt
from proxy_agent.proxy_chat_agent import ProxyChatAgent

class ChatWindow(QWidget):
    def __init__(self, agents):
        super().__init__()
        self.setWindowTitle("🤖 بوتركي - مساعدك الذكي")
        self.setGeometry(300, 100, 600, 500)

        self.agent = ProxyChatAgent(agents)

        self.layout = QVBoxLayout()
        self.chat_history = QTextEdit()
        self.chat_history.setReadOnly(True)

        self.input_box = QLineEdit()
        self.input_box.returnPressed.connect(self.send_message)

        self.send_button = QPushButton("إرسال")
        self.send_button.clicked.connect(self.send_message)

        self.layout.addWidget(QLabel("🧠 المحادثة:"))
        self.layout.addWidget(self.chat_history)
        self.layout.addWidget(self.input_box)
        self.layout.addWidget(self.send_button)
        self.setLayout(self.layout)

    def send_message(self):
        user_text = self.input_box.text().strip()
        if not user_text:
            return

        self.chat_history.append(f"🧑‍💻 أنت: {user_text}")
        self.input_box.clear()

        result = self.agent.respond_as_you(user_text)

        # يتم عرض الرد مباشرة كنص
        reply = result
        agent_name = "🤖 ProxyChatAgent"

        self.chat_history.append(f"{agent_name}: {reply}")
