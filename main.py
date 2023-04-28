import os
import sys

from PySide6.QtWidgets import *

from screens.central_display import MainWindow

if __name__ == "__main__":
    main_path = os.path.dirname(os.path.abspath(__file__))
    app = QApplication()
    window = MainWindow(main_path)
    window.show()
    sys.exit(app.exec())
