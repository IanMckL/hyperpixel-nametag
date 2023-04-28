from PySide6.QtWidgets import QWidget, QVBoxLayout

from screens.utils.navigation_grid import NavigationGrid
from screens.utils.text_box import TextBox


class Nametag(QWidget):
    def __init__(self, main_path, main_stack, name, title):
        super().__init__()

        self.name_label = TextBox(main_path, f'{name}', size=70)
        self.title_label = TextBox(main_path, f'{title}', size=40)

        layout = QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.title_label)
        layout.addWidget(NavigationGrid(main_path, main_stack))

        self.setLayout(layout)
