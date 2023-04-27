import sys

from PySide6.QtWidgets import *

from screens.central_display import MainWindow

if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
