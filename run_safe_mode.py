from core.safe_mode_config_block import SAFEMODE, AUTO_EXECUTE, CONFIRMATION_REQUIRED

if SAFEMODE:
    print("🔒 الوضع الآمن مفعل.")
    if not AUTO_EXECUTE:
        print("⏸️ التنفيذ التلقائي معطل.")
    if CONFIRMATION_REQUIRED:
        print("✅ سيتطلب تأكيد قبل أي تعديل.")

# تابع تشغيل واجهة المستخدم أو المساعد
from ui.main_window import MainWindow
from PyQt5.QtWidgets import QApplication
import sys

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())