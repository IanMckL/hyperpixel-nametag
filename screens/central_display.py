from screens.utils.navigation_grid import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(500, 500)
        self.setStyleSheet('background-color: black')
        self.stacked_widget = QStackedWidget(self)
        self.setCentralWidget(self.stacked_widget)
        self.stacked_widget.addWidget(NavigationGrid())
