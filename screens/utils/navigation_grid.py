from PySide6.QtWidgets import *

from screens.utils.image_button import ImageButton


class NavigationGrid(QWidget):
    def __init__(self, main_path):
        super().__init__()
        self.setFixedSize(500, 500 / 3 - 40)
        # Test QR Code picture
        qr_test = ImageButton(main_path + "/assets/images/qr_test", 500, self.handleTestClick, self)

        # Set navigation layout grid
        layout = QGridLayout()
        layout.addWidget(QLabel("Temp1"), 0, 1)
        layout.addWidget(qr_test, 0, 2)
        layout.addWidget(QLabel("Temp3"), 0, 3)

        self.setLayout(layout)

    def handleTestClick(self):
        print("hello, I've been clicked")
