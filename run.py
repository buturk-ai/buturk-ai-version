from PyQt5.QtWidgets import QApplication
import sys

# ✅ استدعاء فحص الوضع الآمن
from core.safety.safe_mode_config_block import check_safe_mode_config

# ✅ استدعاء الواجهة
from ui.main_window import MainWindow

# 🧠 أنشئ التطبيق أولًا
app = QApplication(sys.argv)

# ✅ فعّل الوضع الآمن
check_safe_mode_config()

# ✅ شغّل الواجهة
window = MainWindow()
window.show()

# ✅ ابدأ تشغيل التطبيق
sys.exit(app.exec_())
