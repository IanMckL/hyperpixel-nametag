import sys

from PySide6.QtWidgets import QApplication, QMainWindow

if __name__ == "__main__":
    app = QApplication([])
    window = QMainWindow()
    window.setFixedSize(500, 500)
    window.show()
    sys.exit(app.exec())
