from PySide6.QtWidgets import QWidget, QVBoxLayout

from screens.utils.navigation_grid import NavigationGrid
from screens.utils.text_box import TextBox


class Nametag(QWidget):
    def __init__(self, main_path):
        super().__init__()

        self.name_label = TextBox(main_path, "Ian Larsen", size=70)
        self.title_label = TextBox(main_path, "Software Engineer", size=40)

        layout = QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.title_label)
        layout.addWidget(NavigationGrid(main_path))

        self.setLayout(layout)
