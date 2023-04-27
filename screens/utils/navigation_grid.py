from PySide6.QtWidgets import *


class NavigationGrid(QWidget):
    def __init__(self):
        super().__init__()

        layout = QGridLayout()

        layout.addWidget(QLabel("Temp1"), 0, 1)
        layout.addWidget(QLabel("Temp2"), 0, 2)
        layout.addWidget(QLabel("Temp3"), 0, 3)
        self.setStyleSheet('border: 2px solid white')
        self.setMaximumHeight(100)
        self.setLayout(layout)
