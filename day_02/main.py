import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog

# If you compiled a resources.qrc → resources_rc.py, keep this import.
# If you don't have a .qrc, you can delete this try/except.
try:
    import resources_rc  # noqa: F401
except Exception:
    pass


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Change this to your .ui file name (the one you saved from Designer)
        uic.loadUi("Window1.ui", self)
        self.setWindowTitle("My PyQt App")

        # --- Example wiring spot (safe to leave empty now) ---
        # if hasattr(self, "pushButton"):
        #     self.pushButton.clicked.connect(self.open_secret)

    # Example: open a secondary window/dialog designed in Designer
    def open_secret(self):
        dlg = SecretDialog(self)
        dlg.exec()


class SecretDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        # If you designed a second UI (e.g., secret.ui), load it; otherwise fallback
        try:
            uic.loadUi("secret.ui", self)
        except Exception:
            self.setWindowTitle("Secret")
            self.resize(320, 180)


def main():
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
