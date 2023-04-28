from screens.nametag import Nametag
from screens.utils.navigation_grid import *


class MainWindow(QMainWindow):
    def __init__(self, main_path):
        super().__init__()
        self.setFixedSize(500, 500)
        self.setStyleSheet('background-color: black')
        self.stacked_widget = QStackedWidget(self)
        self.setCentralWidget(self.stacked_widget)

        # Screens
        nametag = Nametag(main_path, self.stacked_widget, "Ian Larsen", "Software Engineer")
        nametag2 = Nametag(main_path, self.stacked_widget, "Test", "Testing")

        # Add screens to grid
        self.stacked_widget.addWidget(nametag)
        self.stacked_widget.addWidget(nametag2)

        self.stacked_widget.setCurrentIndex(0)
