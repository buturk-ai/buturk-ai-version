import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget, QPushButton
from core.llm_engine import ask_llm
from utils.session import save_message, load_last_session

def launch_app():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("مساعد بوتركي 1 - AI Dev Super Edition")
        self.setGeometry(100, 100, 800, 600)

        self.chat_area = QTextEdit()
        self.chat_area.setReadOnly(True)

        self.input_area = QTextEdit()
        self.input_area.setFixedHeight(80)
        self.input_area.keyPressEvent = self.handle_key_press

        self.send_button = QPushButton("أرسل")
        self.send_button.clicked.connect(self.handle_send)

        layout = QVBoxLayout()
        layout.addWidget(self.chat_area)
        layout.addWidget(self.input_area)
        layout.addWidget(self.send_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # تحميل آخر جلسة
        self.chat_area.append("✅ تم تحميل آخر جلسة\n")
        for msg in load_last_session():
            self.chat_area.append(msg)

    def handle_key_press(self, event):
        if event.key() == 16777220 and not (event.modifiers() & 0x02000000):  # Enter بدون Shift
            self.handle_send()
        else:
            QTextEdit.keyPressEvent(self.input_area, event)

    def handle_send(self):
        user_input = self.input_area.toPlainText().strip()
        if not user_input:
            return

        self.chat_area.append(f"👤: {user_input}")
        self.input_area.clear()

        try:
            response = ask_llm(user_input)
        except Exception as e:
            response = f"❌ خطأ: {e}"

        self.chat_area.append(f"🤖: {response}")

        save_message(f"👤: {user_input}")
        save_message(f"🤖: {response}")
